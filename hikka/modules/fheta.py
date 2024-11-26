__version__ = (6, 6, 6)

#             ███████╗██╗  ██╗███████╗████████╗█████╗ 
#             ██╔════╝██║  ██║██╔════╝╚══██╔══╝██╔══██╗
#             █████╗  ███████║█████╗     ██║   ███████║
#             ██╔══╝  ██╔══██║██╔══╝     ██║   ██╔══██║
#             ██║     ██║  ██║███████╗   ██║   ██║  ██║

# meta developer: @Foxy437
# change-log: ?????????
# meta banner: https://camo.githubusercontent.com/5091a8298e4c92787a9aabf61f5a5797ac01b9bc0fd08b44fc54b1f8dfd6cc60/68747470733a2f2f692e696d67686970706f2e636f6d2f66696c65732f5967473232303844674d2e6a7067
# meta pic: https://camo.githubusercontent.com/5091a8298e4c92787a9aabf61f5a5797ac01b9bc0fd08b44fc54b1f8dfd6cc60/68747470733a2f2f692e696d67686970706f2e636f6d2f66696c65732f5967473232303844674d2e6a7067
# ©️ Fixyres, 2024
# 🌐 https://github.com/Fixyres/FHeta
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 🔑 http://www.apache.org/licenses/LICENSE-2.0

import requests
import asyncio
import aiohttp
from .. import loader, utils
import json
import io
import inspect
from hikkatl.types import Message
import random
from ..types import InlineQuery
import difflib

@loader.tds
class FHeta(loader.Module):
    '''Module for searching modules! Upload your modules to FHeta via fheta_robot.t.me!'''
    
    strings = {
        "name": "FHeta",
        "search": "<emoji document_id=5188311512791393083>🔎</emoji> <b>Searching...</b>",
        "no_query": "<emoji document_id=5348277823133999513>❌</emoji> <b>Enter a query to search.</b>",
        "no_modules_found": "<emoji document_id=5348277823133999513>❌</emoji> <b>No modules found.</b>",
        "commands": "\n<emoji document_id=5190498849440931467>👨‍💻</emoji> <b>Commands:</b>\n{commands_list}",
        "description": "\n<emoji document_id=5433653135799228968>📁</emoji> <b>Description:</b> {description}",
        "result": "<emoji document_id=5188311512791393083>🔎</emoji> <b>Result {index} by query:</b> <code>{query}</code>\n<code>{module_name}</code> by {author}\n<emoji document_id=4985961065012527769>🖥</emoji> <b>Repository:</b> {repo_url}\n<emoji document_id=5307585292926984338>💾</emoji> <b>Command for installation:</b> <code>{install_command}</code>{description}{commands}\n\n\n",
        "fetch_failed": "<emoji document_id=5348277823133999513>❌</emoji> <b>Error.</b>",
        "closest_match": "<emoji document_id=5188311512791393083>🔎</emoji> <b>Result by query:</b> <code>{query}</code>\n<code>{module_name}</code> by {author}\n<emoji document_id=4985961065012527769>🖥</emoji> <b>Repository:</b> {repo_url}\n<emoji document_id=5307585292926984338>💾</emoji> <b>Command for installation:</b> <code>{install_command}</code>{description}{commands}\n\n\n",
        "inline_commandss": "\n<emoji document_id=5372981976804366741>🤖</emoji> <b>Inline commands:</b>\n{inline_list}",
        "language": "en_doc"
    }

    strings_ru = {
        "name": "FHeta",
        "search": "<emoji document_id=5188311512791393083>🔎</emoji> <b>Поиск...</b>",
        "no_query": "<emoji document_id=5348277823133999513>❌</emoji> <b>Введите запрос для поиска.</b>",
        "no_modules_found": "<emoji document_id=5348277823133999513>❌</emoji> <b>Модули не найдены.</b>",
        "commands": "\n<emoji document_id=5190498849440931467>👨‍💻</emoji> <b>Команды:</b>\n{commands_list}",
        "description": "\n<emoji document_id=5433653135799228968>📁</emoji> <b>Описание:</b> {description}",
        "result": "<emoji document_id=5188311512791393083>🔎</emoji> <b>Результат {index} по запросу:</b> <code>{query}</code>\n<code>{module_name}</code> от {author}\n<emoji document_id=4985961065012527769>🖥</emoji> <b>Репозиторий:</b> {repo_url}\n<emoji document_id=5307585292926984338>💾</emoji> <b>Команда для установки:</b> <code>{install_command}</code>{description}{commands}\n\n\n",
        "fetch_failed": "<emoji document_id=5348277823133999513>❌</emoji> <b>Ошибка.</b>",
        "closest_match": "<emoji document_id=5188311512791393083>🔎</emoji> <b>Результат по запросу:</b> <code>{query}</code>\n<code>{module_name}</code> от {author}\n<emoji document_id=4985961065012527769>🖥</emoji> <b>Репозиторий:</b> {repo_url}\n<emoji document_id=5307585292926984338>💾</emoji> <b>Команда для установки:</b> <code>{install_command}</code>{description}{commands}\n\n\n",
        "inline_commandss": "\n<emoji document_id=5372981976804366741>🤖</emoji> <b>Инлайн команды:</b>\n{inline_list}",
        "language": "ru_doc"
    }

    strings_ua = {
        "name": "FHeta",
        "search": "<emoji document_id=5188311512791393083>🔎</emoji> <b>Пошук...</b>",
        "no_query": "<emoji document_id=5348277823133999513>❌</emoji> <b>Введіть запит для пошуку.</b>",
        "no_modules_found": "<emoji document_id=5348277823133999513>❌</emoji> <b>Модулі не знайдені.</b>",
        "commands": "\n<emoji document_id=5190498849440931467>👨‍💻</emoji> <b>Команди:</b>\n{commands_list}",
        "description": "\n<emoji document_id=5433653135799228968>📁</emoji> <b>Опис:</b> {description}",
        "result": "<emoji document_id=5188311512791393083>🔎</emoji> <b>Результат {index} за запитом:</b> <code>{query}</code>\n<code>{module_name}</code> від {author}\n<emoji document_id=4985961065012527769>🖥</emoji> <b>Репозиторій:</b> {repo_url}\n<emoji document_id=5307585292926984338>💾</emoji> <b>Команда для встановлення:</b> <code>{install_command}</code>{description}{commands}\n\n\n",
        "fetch_failed": "<emoji document_id=5348277823133999513>❌</emoji> <b>Помилка.</b>",
        "closest_match": "<emoji document_id=5188311512791393083>🔎</emoji> <b>Результат за запитом:</b> <code>{query}</code>\n<code>{module_name}</code> від {author}\n<emoji document_id=4985961065012527769>🖥</emoji> <b>Репозиторій:</b> {repo_url}\n<emoji document_id=5307585292926984338>💾</emoji> <b>Команда для встановлення:</b> <code>{install_command}</code>{description}{commands}\n\n\n",
        "inline_commandss": "\n<emoji document_id=5372981976804366741>🤖</emoji> <b>Інлайн команди:</b>\n{inline_list}",
        "language": "ua_doc"
    }

    @loader.command(ru_doc="(запрос) - искать модули.", ua_doc="(запит) - шукати модулі.")
    async def fhetacmd(self, message):
        '''(query) - search modules.'''
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings["no_query"])
            return

        search_message = await utils.answer(message, self.strings["search"])
        modules = await self.search_modules(args)

        if not modules:
            modules = await self.search_modules(args.replace(" ", ""))

        if not modules:
            url = "https://raw.githubusercontent.com/Fixyres/FHeta/refs/heads/main/modules.json"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.text()
                        all_modules = json.loads(data)

                        module_names = [module['name'] for module in all_modules if 'name' in module]
                        closest_matches = difflib.get_close_matches(args, module_names, n=1, cutoff=0.5)
                        
                        if closest_matches:
                            closest_module = next((m for m in all_modules if isinstance(m, dict) and 'name' in m and m['name'] == closest_matches[0]), None)
                            if closest_module:
                                formatted_module = await self.format_module(closest_module, args)
                                banner_url = closest_module.get("banner", None)

                                if banner_url:
                                    async with aiohttp.ClientSession() as session:
                                        async with session.get(banner_url) as response:
                                            if response.status == 200:
                                                banner_data = await response.read()
                                                file = io.BytesIO(banner_data)
                                                file.name = "banner.jpg"
                                                await message.client.send_file(
                                                    message.peer_id,
                                                    file,
                                                    caption=formatted_module,
                                                    reply_to=message.id
                                                )
                                                await search_message.delete()
                                                return

                            await utils.answer(search_message, formatted_module)
                            return

            await utils.answer(search_message, self.strings["no_modules_found"])
            return

        seen_modules = set()
        formatted_modules = []
        result_index = 1

        current_language = self.strings.get("language", "doc")
        
        for module in modules[:50]:
            try:
                repo_url = f"https://github.com/{module['repo']}"
                install = module['install']

                commands_section = ""
                inline_commands_section = ""

                if "commands" in module and module['commands']:                             
                    normal_commands = []                                         
                    inline_commands = []                                         

                    for cmd in module['commands']:                               
                            description = cmd.get('description', {}).get(current_language, cmd.get('description', {}).get("doc"))  

                            if isinstance(description, dict):                     
                                    description = description.get('doc', '')             

                            if cmd.get("inline", False):                         
                                    if description:                                 
                                            cmd_entry = f"<code>@{self.inline.bot_username} {cmd['name']}</code> {utils.escape_html(description)}"   
                                    else:                                            
                                            cmd_entry = f"<code>@{self.inline.bot_username} {cmd['name']}</code>"  
                                    inline_commands.append(cmd_entry)                
                            else:                                                 
                                    if description:                                 
                                            cmd_entry = f"<code>{self.get_prefix()}{cmd['name']}</code> {utils.escape_html(description)}" 
                                    else:                                            
                                            cmd_entry = f"<code>{self.get_prefix()}{cmd['name']}</code>" 
                                    normal_commands.append(cmd_entry)                

                    if normal_commands:                                          
                            commands_section = self.strings["commands"].format(commands_list="\n".join(normal_commands)) 

                    if inline_commands:                                          
                            inline_commands_section = self.strings["inline_commandss"].format(    
                                    inline_list="\n".join(inline_commands))                   
            
                description_section = ""
                if "description" in module and module["description"]:
                    description_section = self.strings["description"].format(description=utils.escape_html(module["description"]))

                author_info = utils.escape_html(module.get("author", "???"))
                module_name = utils.escape_html(module['name'].replace('.py', ''))
                module_namee = utils.escape_html(module['name'].replace('.py', '').lower())
                module_key = f"{module_namee}_{author_info}"

                if module_key in seen_modules:
                    continue
                seen_modules.add(module_key)

                thumbnail_url = module.get("banner", None)
                result = self.strings["result"].format(
                    index=result_index,
                    query=args,
                    module_name=module_name,
                    author=author_info,
                    repo_url=repo_url,
                    install_command=f"{self.get_prefix()}{install}",
                    description=description_section,
                    commands=commands_section + inline_commands_section
                )
                formatted_modules.append((result, thumbnail_url))
                result_index += 1
            except Exception:
                continue

        if len(formatted_modules) == 1:
            result_text, thumbnail_url = formatted_modules[0]
            if thumbnail_url:
                async with aiohttp.ClientSession() as session:
                    async with session.get(thumbnail_url) as response:
                        if response.status == 200:
                            banner_data = await response.read()
                            file = io.BytesIO(banner_data)
                            file.name = "banner.jpg"
                            closest_match_result = self.strings["closest_match"].format(
                                query=args,
                                module_name=module_name,
                                author=author_info,
                                repo_url=repo_url,
                                install_command=f"{self.get_prefix()}{install}",
                                description=description_section,
                                commands=commands_section + inline_commands_section
                            )
                            await message.client.send_file(
                                message.peer_id,
                                file,
                                caption=closest_match_result,
                                reply_to=message.id
                            )
                            await search_message.delete()
                            return

            closest_match_result = self.strings["closest_match"].format(
                query=args,
                module_name=module_name,
                author=author_info,
                repo_url=repo_url,
                install_command=f"{self.get_prefix()}{install}",
                description=description_section,
                commands=commands_section + inline_commands_section
            )

            await utils.answer(search_message, closest_match_result)
        else:
            results = "".join([item[0] for item in formatted_modules])
            await utils.answer(search_message, results)
    
    async def search_modules(self, query: str):
        url = "https://raw.githubusercontent.com/Fixyres/FHeta/refs/heads/main/modules.json"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.text()
                    modules = json.loads(data)

                    found_modules = [
                        module for module in modules
                        if query.lower() in module.get("name", "").lower()
                    ]
                    
                    if not found_modules:
                        found_modules = [
                            module for module in modules
                            if any(query.lower() in cmd.get("name", "").lower() for cmd in module.get("commands", []))
                        ]
                    
                    if not found_modules:
                        found_modules = [
                            module for module in modules
                            if query.lower() in module.get("author", "").lower()
                        ]

                    if not found_modules:
                        found_modules = [
                            module for module in modules
                            if query.lower() in module.get("description", "").lower()
                        ]

                    return found_modules

    async def format_module(self, module, query):
        repo_url = f"https://github.com/{module['repo']}"
        install = module['install']
        current_language = self.strings.get("language", "doc")
        commands_section = ""
        inline_commands_section = ""

        if "commands" in module and module['commands']:
            normal_commands = []
            inline_commands = []

            for cmd in module['commands']:
                description = cmd.get('description', {}).get(current_language, cmd.get('description', {}).get("doc"))

                if isinstance(description, dict):
                    description = description.get('doc', '')

                if cmd.get("inline", False):
                    if description:
                        cmd_entry = f"<code>@{self.inline.bot_username} {cmd['name']}</code> {utils.escape_html(description)}"
                    else:
                        cmd_entry = f"<code>@{self.inline.bot_username} {cmd['name']}</code>"
                    inline_commands.append(cmd_entry)
                else:
                    if description:
                        cmd_entry = f"<code>{self.get_prefix()}{cmd['name']}</code> {utils.escape_html(description)}"
                    else:
                        cmd_entry = f"<code>{self.get_prefix()}{cmd['name']}</code>"
                    normal_commands.append(cmd_entry)

            if normal_commands:
                commands_section = self.strings["commands"].format(commands_list="\n".join(normal_commands))

            if inline_commands:
                inline_commands_section = self.strings["inline_commandss"].format(
                    inline_list="\n".join(inline_commands))

        description_section = ""
        if "description" in module and module["description"]:
            description_section = self.strings["description"].format(description=utils.escape_html(module["description"]))

        author_info = utils.escape_html(module.get("author", "???"))
        module_name = utils.escape_html(module['name'].replace('.py', ''))

        return self.strings["closest_match"].format(
            query=query,
            module_name=module_name,
            author=author_info,
            repo_url=repo_url,
            install_command=f"{self.get_prefix()}{install}",
            description=description_section,
            commands=commands_section + inline_commands_section
            )