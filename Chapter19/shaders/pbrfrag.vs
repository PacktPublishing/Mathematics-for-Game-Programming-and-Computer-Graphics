#version 330 core
out vec4 frag_color;
//in vec2 UV;
in vec3 world_pos;
in vec3 normal;
in vec3 cam_pos;

// material parameters
uniform vec3  albedo;
uniform float metallic;
uniform float roughness;
uniform float ao;


struct light
{
    vec3 position;
    vec3 color;
    float attenuation;
};

#define NUM_LIGHTS 3
uniform light light_data[NUM_LIGHTS];

const float PI = 3.14159265359;

vec3 Fresnel(float HoV, vec3 metalness)
{
    return metalness + (1.0 - metalness) * pow(clamp(1.0 - HoV, 0.0, 1.0), 5.0);
}

float GGX(float NoH, float roughness)
{
    float a = roughness*roughness;
    float a2 = a*a;
    float NoH2 = NoH*NoH;
    float numerator = a2;
    float denominator = (NoH2 * (a2 - 1.0) + 1.0);
    denominator = PI * denominator * denominator;
    return numerator / denominator;
}

float GASchlick(float Ndot, float roughness)
{
    float r = (roughness + 1.0);
    float k = (r*r) / 8.0;
    float numerator   = Ndot;
    float denominator = Ndot * (1.0 - k) + k;
    return numerator / denominator;
}

float GASmith(float NoV, float NoL, float roughness)
{
    float gas2  = GASchlick(NoV, roughness);
    float gas1  = GASchlick(NoL, roughness);
    return gas1 * gas2;
}


void main()
{
    vec3 N = normalize(normal);
    vec3 V = normalize(cam_pos - world_pos);

    vec3 metalness = vec3(0.01);
    metalness = mix(metalness, albedo, metallic);

    // reflectance equation
    vec3 Lo = vec3(0.0);
    for(int i = 0; i < NUM_LIGHTS; ++i) //each light
    {
        // calculate per-light radiance
        vec3 L = normalize(light_data[i].position - world_pos);
        vec3 H = normalize(V + L);
        float distance    = length(light_data[i].position - world_pos);
        float attenuation = light_data[i].attenuation / (distance * distance);
        vec3 radiance     = light_data[i].color * light_data[i].attenuation;

        // Cook-Torrance BRDF
        float D = GGX(max(dot(N, H), 0.0), roughness);
        float G   = GASmith(max(dot(N, V), 0.0), max(dot(N, L), 0.0), roughness);
        vec3 F    = Fresnel(max(dot(H, V), 0.0), metalness);

        vec3 kS = F;
        vec3 kD = vec3(1.0) - kS;
        kD *= 1.0 - metallic;

        vec3 numerator    = D * G * F;
        float denominator = 4.0 * max(dot(N, V), 0.0) * max(dot(N, L), 0.0) + 0.0001;
        vec3 specular     = numerator / denominator;

        // add to outgoing radiance Lo
        float NoL = max(dot(N, L), 0.0);
        Lo += (albedo / PI + specular) * radiance * NoL;
    }

    vec3 ambient = vec3(0.01) * albedo * ao;
    vec3 color = ambient + Lo;

    color = color / (color + vec3(1.0));
    color = pow(color, vec3(1.0/2.2));

    frag_color = vec4(color, 1.0);
}