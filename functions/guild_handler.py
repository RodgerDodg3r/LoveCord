from functions.json_handler import *

def guild_get_data(guild_id) -> dict:

    path = f"data/guilds/{guild_id}.json"
    if (json_file_exists(path) == False):
        return {}
    return json_get_file_data(path)


def guild_sync_config_with_template(guild_id: int):

    path = f"data/guilds/{guild_id}.json"
    template_data = json_get_file_data("data/guilds/template.json")
    guild_data = {}

    if (json_file_exists(path) == False):
        guild_data = template_data

    if (json_file_exists(path) == True):
        guild_data = json_get_file_data(path)
        for key in template_data:
            if (key not in guild_data):
                guild_data[key] = template_data[key]
    
    guild_save_data(guild_id, guild_data)

def guild_save_data(guild_id, guild_data: dict):    
    path = f"data/guilds/{guild_id}.json"
    json_save(path, guild_data)

    
def guild_delete_data(guild_id):
    path = f"data/guilds/{guild_id}.json"
    if (json_file_exists(path) == False):
        return
    os.remove(path)
