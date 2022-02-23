usuarios_data_science = {12, 76, 88, 90, 13}
usuarios_machine_learning = {13, 23, 88, 55}

assistiram_um_curso = usuarios_data_science | usuarios_machine_learning
assistiram_dois_cursos = usuarios_data_science & usuarios_machine_learning
assistiram_somente_data_science = usuarios_data_science - usuarios_machine_learning
nao_assistiram_machine_learning = assistiram_dois_cursos ^ assistiram_somente_data_science

print(assistiram_um_curso)
print(assistiram_dois_cursos)
print(assistiram_somente_data_science)
print(nao_assistiram_machine_learning)
