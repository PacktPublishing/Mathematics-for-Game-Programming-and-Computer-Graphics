#version 330 core
in vec3 position;
in vec3 vertex_normal;
in vec2 vertex_uv;
uniform mat4 projection_mat;
uniform mat4 model_mat;
uniform mat4 view_mat;
out vec3 normal;
out vec2 UV;
out vec3 world_pos;
out vec3 cam_pos;

void main()
{
    gl_Position = projection_mat * transpose(view_mat) * transpose(model_mat) * vec4(position, 1);
    UV = vertex_uv;
    normal = mat3(transpose(model_mat)) * vertex_normal;
    world_pos = (transpose(model_mat) * vec4(position, 1)).rgb;
    cam_pos = vec3(inverse(transpose(model_mat)) *
                    vec4(view_mat[3][0], view_mat[3][1], view_mat[3][2],1));
}