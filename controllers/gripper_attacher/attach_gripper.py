from controller import Supervisor

sup = Supervisor()
timestep = int(sup.getBasicTimeStep())

# Un paso para asegurar carga de escena
sup.step(timestep)

# Localiza el Connector activo en el flange
conn = sup.getFromDef('FLANGE_CONN')
conn_children = conn.getField('children')

# Importa el PROTO del gripper al Connector
gripper_proto = sup.getProtoDeclaration('protos/AdaptiveGripper.proto', 'AdaptiveGripper')
conn_children.importMFNodeFromString(-1, gripper_proto)

# Bucle vacío (o tu lógica de RL después)
while sup.step(timestep) != -1:
    pass
