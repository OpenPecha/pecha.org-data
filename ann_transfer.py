from pathlib import Path

from pecha_preparation_components import TransferAnnotations

origin = Path('input/ann_transfer/chojuk segmented.txt')
target = Path('input/ann_transfer/chojuk clean.txt')

ta = TransferAnnotations(origin, target)
result = ta.transfer_segmentation()
