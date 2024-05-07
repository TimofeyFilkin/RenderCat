#version 430

out vec4 FragColor;

void main(){
    vec3 col = vec3(1, 0, 0);
    FragColor = vec4(col, 1.0);
}