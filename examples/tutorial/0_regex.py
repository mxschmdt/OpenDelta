from transformers import AutoModelForSequenceClassification
model = AutoModelForSequenceClassification.from_pretrained("roberta-base")
# suppose we load BART

from opendelta import Visualization
print("before modify")
Visualization(model).structure_graph()

from opendelta import LoraModel
import re
delta_model = LoraModel(backbone_model=model, modified_modules=[re.compile('(\d)+\.output.dense'), 'attention.output.dense'])
print("after modify")
delta_model.log()
# This will visualize the backbone after modification and other information.