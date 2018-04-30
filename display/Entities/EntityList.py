from display.Entities import Entity, BorderEntity
class EntityList:

    DEFAULT_ENTITY = None
    DEFAULT_BORDER_ENTITY = None

    INSTANCE = None
    ENTITY_REGISTRY = {}

    def __init__(self):
        self.load_entities()

    def register_entity(entity:Entity ):
        entID = len(EntityList.ENTITY_REGISTRY.keys())
        EntityList.ENTITY_REGISTRY[entID] = entity
        print(entID, ":: registered entity:",entity.get_entity_name())
        return entity

    def load_entities(self):
        EntityList.DEFAULT_ENTITY = EntityList.register_entity(Entity())
        EntityList.DEFAULT_BORDER_ENTITY = EntityList.register_entity(BorderEntity())



if not (EntityList.INSTANCE):
    EntityList.INSTANCE = EntityList()
