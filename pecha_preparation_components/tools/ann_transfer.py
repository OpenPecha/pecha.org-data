from pathlib import Path

from antx import transfer  # installed from wheel in github repo


class TransferAnnotations:
    def __init__(self, origin, target):
        self.target_file = Path(target)
        self.out_file = None
        self.origin = Path(origin).read_text()
        self.target = Path(target).read_text()

    def transfer_segmentation(self):
        """
        transfers linereturns and chapter annotations in the following format: "ch-{num} "
        """
        anns = [
            ['segmentation', '(\n)'],
            ['chapters', r'(ch-[0-9]+ )']
        ]
        res = self.transfer_anns(anns)
        self.__prepare_out_folder()
        self.out_file.write_text(res)

    def transfer_anns(self, anns):
        return transfer(self.origin, anns, self.target)

    def __prepare_out_folder(self):
        parts = list(self.target_file.parts)
        parts[0] = 'output'  # change input to output, but maintain the subfolders
        out_path = Path('/'.join(parts))
        out_path.parent.mkdir(parents=True, exist_ok=True)
        self.out_file = out_path
