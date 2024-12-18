from pyfrotz.ovos import FrotzSkill
from pyfrotz.parsers import zork_intro_parser


class ZorkSkill(FrotzSkill):
    def __init__(self, *args, **kwargs):
        # game is english only, apply bidirectional translation
        super().__init__(*args,
                         game_id="zork_1",
                         game_lang="en-us",
                         game_data=f'{self.root_dir}/res/{self.game_id}.z5',
                         intro_parser=zork_intro_parser,
                         **kwargs)
