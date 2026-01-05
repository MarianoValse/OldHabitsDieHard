class HabitoService:

    @staticmethod
    def filtrar_activos(habitos):
        return [h for h in habitos if h.activo]

    @staticmethod
    def ordenar_por_dificultad(habitos):
        return sorted(habitos, key=lambda h: h.dificultad.factor)

    # @staticmethod
    # def ordenar_por_orden(habitos):
    #     return sorted(habitos, key=lambda h: h.orden)