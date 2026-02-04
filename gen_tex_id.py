import glob
import os


TEXTURE_PATTERN = 'assets/textures/*.png'

FILE_PATH = 'source/engine/tex_id.odin'
FILE_PACKAGE = 'engine'

ENUM_NAME = 'Tex_ID'


def _to_ada_case(s: str) -> str:
    words = s.split('_')
    return '_'.join(word.capitalize() for word in words)


if __name__ == '__main__':
    with open(FILE_PATH, 'w+t') as file:
        if file is None:
            print('Failed to open file at path ', FILE_PATH)
            exit(1)
        file.write(f'package {FILE_PACKAGE}\n\n{ENUM_NAME} :: enum ')
        file.write('{')

        matches = glob.glob(TEXTURE_PATTERN)
        if matches is None:
            print(f'Failed to find matches at {TEXTURE_PATTERN}')
            exit(1)
        for m in matches:
            name = os.path.basename(m).removesuffix('.png')
            file.write(f'\n\t{_to_ada_case(name)},')

        file.write('\n}')
    print('Generated Texture IDs!')
