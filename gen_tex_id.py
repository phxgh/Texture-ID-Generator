import glob
import os


FILE_PATH = 'game/engine/tex_id.odin'
FILE_PACKAGE = 'engine'

ENUM_NAME = 'Tex_ID'


def _to_ada_case(s: str) -> str:
    words = s.split('_')
    return '_'.join(word.capitalize() for word in words)


if __name__ == '__main__':
    pattern = 'assets/textures/*.png'
    with open(FILE_PATH, 'w+t') as file:
        if file is None:
            print('Failed to open file at path ', FILE_PATH)
            exit(1)
        file.write(f'package {FILE_PACKAGE}\n\n{ENUM_NAME} :: enum\n')
        file.write('{')

        matches = glob.glob(pattern)
        if matches is None:
            print(f'Failed to find matches at {pattern}')
            exit(1)
        for i, m in enumerate(matches):
            name = os.path.basename(m).removesuffix('.png')
            file.write(f'\n\t{_to_ada_case(name)} = 0x{i},')

        file.write('\n}')
    print('Generated Texture IDs!')
