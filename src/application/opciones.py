class Opciones():
    def enviarOpciones(self):
        opciones = [["1", "2", "3", "4"]]
        keyboard = {
            "keyboard": opciones,
            "one_time_keyboard": True,
            "remove_keyboard": True,
            "resize_keyboard": True,
        }
        return keyboard

    # def enviarOpcionesSolicitud(self, chatId, first_name):
    #     opciones = [["ACTIVAR_"+first_name +
    #                  "("+chatId+")", "CANCELAR_"+first_name+"("+chatId+")"]]
    #     keyboard = {
    #         "keyboard": opciones,
    #         "one_time_keyboard": True,
    #         "remove_keyboard": True,
    #         "resize_keyboard": True,
    #     }
    #     return keyboard
