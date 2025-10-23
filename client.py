import grpc
import hello_pb2
import hello_pb2_grpc

SERVER = 'localhost:50051'


def run():
    """Ejecutar cliente interactivo"""
    channel = grpc.insecure_channel(SERVER)
    stub = hello_pb2_grpc.UserServiceStub(channel)
    
    while True:
        print("\n=== Menú CRUD ===")
        print("1. Crear usuario")
        print("2. Buscar usuario por ID")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")
        
        opc = input("Elige una opción: ").strip()
        
        if opc == '1':
            name = input('Nombre: ')
            email = input('Email: ')
            try:
                resp = stub.CreateUser(hello_pb2.UserRequest(name=name, email=email))
                if resp.message == "Usuario creado":
                    print(f'✓ Usuario creado exitosamente - ID: {resp.id}')
                else:
                    print(f'✗ {resp.message}')
            except Exception as e:
                print(f'✗ Error: {e}')
        
        elif opc == '2':
            try:
                id_ = int(input('ID: '))
                resp = stub.GetUser(hello_pb2.UserIdRequest(id=id_))
                if resp.id > 0:
                    print(f'✓ Usuario encontrado:')
                    print(f'  ID: {resp.id}')
                    print(f'  Nombre: {resp.name}')
                    print(f'  Email: {resp.email}')
                else:
                    print(f'✗ {resp.message}')
            except ValueError:
                print('✗ Error: Debes ingresar un número válido')
            except Exception as e:
                print(f'✗ Error: {e}')
        
        elif opc == '3':
            try:
                id_ = int(input('ID: '))
                name = input('Nuevo nombre: ')
                email = input('Nuevo email: ')
                resp = stub.UpdateUser(hello_pb2.UserRequest(id=id_, name=name, email=email))
                if resp.message == "Usuario actualizado":
                    print(f'✓ Usuario actualizado exitosamente')
                else:
                    print(f'✗ {resp.message}')
            except ValueError:
                print('✗ Error: Debes ingresar un número válido')
            except Exception as e:
                print(f'✗ Error: {e}')
        
        elif opc == '4':
            try:
                id_ = int(input('ID a eliminar: '))
                resp = stub.DeleteUser(hello_pb2.UserIdRequest(id=id_))
                if resp.message == "Usuario eliminado":
                    print(f'✓ Usuario eliminado exitosamente')
                else:
                    print(f'✗ {resp.message}')
            except ValueError:
                print('✗ Error: Debes ingresar un número válido')
            except Exception as e:
                print(f'✗ Error: {e}')
        
        elif opc == '5':
            print("¡Hasta luego!")
            break
        
        else:
            print('✗ Opción no válida')


if __name__ == '__main__':
    run()
