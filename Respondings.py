from PikaPY import Pikanetwork
import asyncio


async def main():

    username = 'Fireor' # "Legacity" # 

    limit = 20

    async with Pikanetwork() as API:

        profile = await API.Profile("fireor")

        if profile is None:
            return
        
        g = await profile.guild()

        members = await g.member_list()

        
        members_stats = await asyncio.gather(*(API.Stats(member, 'bedwars', 'total', 'all_modes') for member in members))

        for member in members_stats:

                if member:
                    print(f"{member}: {await member.wins(leaderboard=False)}")


asyncio.run(main())