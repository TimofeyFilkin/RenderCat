#version 330 core

layout (location=0) out vec4 FragColor;

in vec2 uv_0;
in vec3 normal;
in vec3 fragPos;

struct Light {
    vec3 position;
    vec3 Ia;
    vec3 Id;
    vec3 Is;
};

uniform Light light;
uniform sampler2D u_texture_0;
uniform vec3 camPos;

vec3 getLight(vec3 Color){
    vec3 Normal = normalize(normal);

    vec3 ambient = light.Ia;

    vec3 lightDir = normalize(light.position-fragPos);
    float diff = max(0, dot(lightDir, normal));
    vec3 diffuse = diff * light.Id;

    vec3 viewDir = normalize(camPos - fragPos);
    vec3 reflectDir = reflect(-lightDir, Normal);
    float spec = pow(max(dot(viewDir, reflectDir), 0), 32);
    vec3 specular = spec * light.Is;

    return Color * (ambient+diffuse+specular);
}

void main(){
    float gamma = 2;
    vec3 col = texture(u_texture_0, uv_0).rgb;

    col = getLight(col);

    col = pow(col, 1/vec3(gamma));
    FragColor = vec4(col, 1.0);
}