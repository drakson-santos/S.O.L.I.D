# Observe que nossa classe UserController é responsavel por salvar um novo usuario no banco de dados.
# Dentro do método save_user é criado uma instancia do banco MongoDb e logo depois o usuario é salvo.

# Problema: Caso em algum momento seja necessario alterar o banco de dados, como por exemplo; para um banco
# em memoria, será preciso alterar a linha 22, no lugar de instanciado o banco MongoDb, será
# criada uma instancia do banco em memoria.
#
# Ou seja, nossa classe UserController foi modificada! E esse principio tem como regra que uma classe jamais
# deve ser modificada.
# #

#Problema
class DatabaseMongoDb:

    def save(self, data):
        # Implementa a logica para salvar em um banco MongoDb
        pass

class UserController:

    def save_user(self, user):
        database_mongodb = DatabaseMongoDb()
        database_mongodb.save(user)

# Note que nosso codigo agora permite facilmente a mundaça para qualquer outro banco, sem que seja
# preciso modificar a classe UserController.
# Estamos aberto para extensão, mas agora não precisamos mais de modificacao.

# Solucao
class IDatabase:
    def save(self, data):
        raise NotImplementedError()

class DatabaseInMemory(IDatabase):

    def save(self, data):
        # Implementa a logica para salvar em um banco em memoria
        pass

class DatabaseMongoDb(IDatabase):

    def save(self, data):
        # Implementa a logica para salvar em um banco MongoDb
        pass

class UserController:

    def __init__(self, database: IDatabase):
        self.database: IDatabase = database

    def save_user(self, user):
        self.database.save(user)

databaseInMemory = DatabaseInMemory()
userController = UserController()
userController.save_user({})

databaseInMemory = DatabaseInMemory()
userController = UserController(databaseInMemory)
userController.save_user({})