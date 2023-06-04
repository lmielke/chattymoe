# statefile.py
import os, shutil
from jinja2 import Environment, FileSystemLoader
import chattymoe.settings as sts


class Template:
    """Generates a statefile and places it into the correct product folder

    [description]
    """

    def __init__(self, *args, verbose: int = 0, **kwargs ) -> None:
        self.verbose = verbose

    def generate_statefiles(self, buildFiles=None, *args, service=None, **kwargs) -> None:
        for buildLevel, genParams in buildFiles.items():
            docf = self.gen_from_template(*args, **genParams.get('template'), **kwargs)
            # safe gen result and copy it to Dockerilfe repo
            with open(genParams.get('tgt'), 'w') as t:
                t.write(docf)
            # only the _up files need to be copied to state_ups to be used by compose
            if buildLevel == sts.phases.get(service, [None])[-1]:
                self.copy_statefile(genParams, *args, **kwargs)

    def gen_from_template(self, *args, templatePath:str, params:dict, **kwargs) -> None:
        #target, template, tParams, dataSource, data
        env = Environment(loader=FileSystemLoader([os.path.dirname(templatePath)]))
        return env.get_template(os.path.basename(templatePath)).render(params=params)

    def copy_statefile(self, genParams, *args, **kwargs) -> None:
        shutil.copyfile(
                        genParams.get('tgt'),
                        os.path.join(sts.stateUpsDir, genParams.get('buildId')),
                        )

    def __str__(self, *args, **kwargs):
        dotPath = f"{__file__.replace(sts.projectPath, '').strip(os.sep).replace(os.sep, '.')}"
        return dotPath
