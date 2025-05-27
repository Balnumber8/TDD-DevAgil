class agenda:
    def __int__(self):
        self.consultas = []
    def agendar(self, paciente, data, hora, medico):
        for consulta in self.consultas:
            if consulta['data'] == data and consulta['hora'] == hora and consulta['medico'] == medico:
                raise ValueError("Já existe uma consulta agendada para este médico nesta data e hora.")   
        consulta = {
            'paciente': paciente,
            'data': data,
            'hora': hora
        }
        self.consultas.append(consulta)
        return consulta