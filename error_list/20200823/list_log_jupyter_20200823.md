## Original File URL: https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py


### Error 1, [Traceback at line 45](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L45)<br />45..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 953, in _find_and_load_unlocked
<br />ModuleNotFoundError: No module named 'mlmodels.model_sklearn.sklearn'



### Error 2, [Traceback at line 57](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L57)<br />57..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 3, [Traceback at line 64](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L64)<br />64..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/example//sklearn_titanic_svm.py", line 20, in <module>
<br />    module        =  module_load( model_uri= model_uri )                           # Load file definition
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_sklearn.sklearn notfound, No module named 'mlmodels.model_sklearn.sklearn', tuple index out of range



### Error 4, [Traceback at line 128](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L128)<br />128..Traceback (most recent call last):
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/autogluon/utils/tabular/ml/trainer/abstract_trainer.py", line 360, in train_single_full
<br />    Y_train=y_train, Y_test=y_test, scheduler_options=(self.scheduler_func, self.scheduler_options), verbosity=self.verbosity)
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/autogluon/utils/tabular/ml/models/lgb/lgb_model.py", line 283, in hyperparameter_tune
<br />    directory=directory, lgb_model=self, **params_copy)
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/autogluon/core/decorator.py", line 69, in register_args
<br />    self.update(**kwvars)
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/autogluon/core/decorator.py", line 79, in update
<br />    hp = v.get_hp(name=k)
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/autogluon/core/space.py", line 451, in get_hp
<br />    default_value=self._default)
<br />  File "ConfigSpace/hyperparameters.pyx", line 773, in ConfigSpace.hyperparameters.UniformIntegerHyperparameter.__init__
<br />  File "ConfigSpace/hyperparameters.pyx", line 843, in ConfigSpace.hyperparameters.UniformIntegerHyperparameter.check_default
<br />ValueError: Illegal default value 36



### Error 5, [Traceback at line 357](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L357)<br />357..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 953, in _find_and_load_unlocked
<br />ModuleNotFoundError: No module named 'mlmodels.model_sklearn.sklearn'



### Error 6, [Traceback at line 369](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L369)<br />369..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 7, [Traceback at line 376](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L376)<br />376..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/example//sklearn_titanic_randomForest.py", line 21, in <module>
<br />    module        =  module_load( model_uri= model_uri )                           # Load file definition
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_sklearn.sklearn notfound, No module named 'mlmodels.model_sklearn.sklearn', tuple index out of range



### Error 8, [Traceback at line 427](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L427)<br />427..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/example//keras-textcnn.py", line 37, in <module>
<br />    _, _   =  module.fit(model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars)          # fit the model
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/model_keras/textcnn.py", line 69, in fit
<br />    Xtrain, Xtest, ytrain, ytest = get_dataset(data_pars)
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/model_keras/textcnn.py", line 143, in get_dataset
<br />    maxlen       = data_pars['data_info']['maxlen']
<br />KeyError: 'data_info'



### Error 9, [Traceback at line 446](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L446)<br />446..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/example//lightgbm_home_retail.py", line 21, in <module>
<br />    pars = json.load(open( data_path , mode='r'))
<br />FileNotFoundError: [Errno 2] No such file or directory: 'hyper_lightgbm_home_retail.json'
<br />SyntaxError: invalid syntax



### Error 10, [Traceback at line 474](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L474)<br />474..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/example//lightgbm_glass.py", line 16, in <module>
<br />    print( os.getcwd())
<br />NameError: name 'os' is not defined



### Error 11, [Traceback at line 552](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L552)<br />552..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
<br />  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
<br />  File "<frozen importlib._bootstrap_external>", line 674, in exec_module
<br />  File "<frozen importlib._bootstrap_external>", line 781, in get_code
<br />  File "<frozen importlib._bootstrap_external>", line 741, in source_to_code
<br />  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/model_sklearn/model_lightgbm.py", line 316
<br />    else:
<br />       ^
<br />SyntaxError: invalid syntax



### Error 12, [Traceback at line 572](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L572)<br />572..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 13, [Traceback at line 579](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L579)<br />579..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/example//lightgbm.py", line 23, in <module>
<br />    module        =  module_load( model_uri= model_uri)
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_sklearn.model_lightgbm notfound, invalid syntax (model_lightgbm.py, line 316), tuple index out of range



### Error 14, [Traceback at line 596](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L596)<br />596..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/example//lightgbm_titanic.py", line 21, in <module>
<br />    pars = json.load(open( data_path , mode='r'))
<br />FileNotFoundError: [Errno 2] No such file or directory: 'hyper_lightgbm_titanic.json'



### Error 15, [Traceback at line 623](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L623)<br />623..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/example//sklearn_titanic_randomForest_example2.py", line 22, in <module>
<br />    pars = json.load(open( data_path , mode='r'))
<br />FileNotFoundError: [Errno 2] No such file or directory: '../mlmodels/dataset/json/hyper_titanic_randomForest.json'



### Error 16, [Traceback at line 637](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L637)<br />637..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/example//tensorflow__lstm_json.py", line 13, in <module>
<br />    print( os.getcwd())
<br />NameError: name 'os' is not defined



### Error 17, [Traceback at line 651](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L651)<br />651..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 953, in _find_and_load_unlocked
<br />ModuleNotFoundError: No module named 'mlmodels.model_sklearn.sklearn'



### Error 18, [Traceback at line 663](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L663)<br />663..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 19, [Traceback at line 670](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L670)<br />670..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/example//sklearn.py", line 34, in <module>
<br />    module        =  module_load( model_uri= model_uri )                           # Load file definition
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_sklearn.sklearn notfound, No module named 'mlmodels.model_sklearn.sklearn', tuple index out of range



### Error 20, [Traceback at line 686](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L686)<br />686..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/example//keras_charcnn_reuters.py", line 28, in <module>
<br />    pars = json.load(open( config_path , mode='r'))[config_mode]
<br />FileNotFoundError: [Errno 2] No such file or directory: 'reuters_charcnn.json'



### Error 21, [Traceback at line 712](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L712)<br />712..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 953, in _find_and_load_unlocked
<br />ModuleNotFoundError: No module named 'mlmodels.model_sklearn.sklearn'



### Error 22, [Traceback at line 724](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L724)<br />724..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 23, [Traceback at line 731](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L731)<br />731..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
<br />  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
<br />  File "<frozen importlib._bootstrap_external>", line 678, in exec_module
<br />  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/model_gluon/gluon_automl.py", line 14, in <module>
<br />    import autogluon as ag
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/autogluon/__init__.py", line 6, in <module>
<br />    from .utils.try_import import *
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/autogluon/utils/__init__.py", line 5, in <module>
<br />    from .dataset import *
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/autogluon/utils/dataset.py", line 3, in <module>
<br />    import mxnet as mx
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/__init__.py", line 31, in <module>
<br />    from . import contrib
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/__init__.py", line 31, in <module>
<br />    from . import onnx
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/onnx/__init__.py", line 19, in <module>
<br />    from .onnx2mx.import_model import import_model, get_model_metadata
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/onnx/onnx2mx/__init__.py", line 20, in <module>
<br />    from . import import_model
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/onnx/onnx2mx/import_model.py", line 22, in <module>
<br />    from .import_onnx import GraphProto
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/onnx/onnx2mx/import_onnx.py", line 26, in <module>
<br />    from ._import_helper import _convert_map as convert_map
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/onnx/onnx2mx/_import_helper.py", line 21, in <module>
<br />    from ._op_translations import identity, random_uniform, random_normal, sample_multinomial
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/onnx/onnx2mx/_op_translations.py", line 22, in <module>
<br />    from . import _translation_utils as translation_utils
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/onnx/onnx2mx/_translation_utils.py", line 23, in <module>
<br />    from .... import  module
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/module/__init__.py", line 22, in <module>
<br />    from .base_module import BaseModule
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/module/base_module.py", line 31, in <module>
<br />    from ..model import BatchEndParam
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/model.py", line 46, in <module>
<br />    from sklearn.base import BaseEstimator
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/example/sklearn.py", line 34, in <module>
<br />    module        =  module_load( model_uri= model_uri )                           # Load file definition
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_sklearn.sklearn notfound, No module named 'mlmodels.model_sklearn.sklearn', tuple index out of range



### Error 24, [Traceback at line 782](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L782)<br />782..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 25, [Traceback at line 789](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L789)<br />789..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/example//gluon_automl_titanic.py", line 22, in <module>
<br />    module        =  module_load( model_uri= model_uri )                           # Load file definition
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_gluon.gluon_automl notfound, Module model_sklearn.sklearn notfound, No module named 'mlmodels.model_sklearn.sklearn', tuple index out of range, tuple index out of range



### Error 26, [Traceback at line 803](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L803)<br />803..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 953, in _find_and_load_unlocked
<br />ModuleNotFoundError: No module named 'mlmodels.model_sklearn.sklearn'



### Error 27, [Traceback at line 815](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L815)<br />815..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 28, [Traceback at line 822](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L822)<br />822..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/example//benchmark_timeseries_m5.py", line 27, in <module>
<br />    import mxnet as mx
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/__init__.py", line 31, in <module>
<br />    from . import contrib
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/__init__.py", line 31, in <module>
<br />    from . import onnx
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/onnx/__init__.py", line 19, in <module>
<br />    from .onnx2mx.import_model import import_model, get_model_metadata
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/onnx/onnx2mx/__init__.py", line 20, in <module>
<br />    from . import import_model
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/onnx/onnx2mx/import_model.py", line 22, in <module>
<br />    from .import_onnx import GraphProto
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/onnx/onnx2mx/import_onnx.py", line 26, in <module>
<br />    from ._import_helper import _convert_map as convert_map
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/onnx/onnx2mx/_import_helper.py", line 21, in <module>
<br />    from ._op_translations import identity, random_uniform, random_normal, sample_multinomial
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/onnx/onnx2mx/_op_translations.py", line 22, in <module>
<br />    from . import _translation_utils as translation_utils
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/onnx/onnx2mx/_translation_utils.py", line 23, in <module>
<br />    from .... import  module
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/module/__init__.py", line 22, in <module>
<br />    from .base_module import BaseModule
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/module/base_module.py", line 31, in <module>
<br />    from ..model import BatchEndParam
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/model.py", line 46, in <module>
<br />    from sklearn.base import BaseEstimator
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/example/sklearn.py", line 34, in <module>
<br />    module        =  module_load( model_uri= model_uri )                           # Load file definition
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_sklearn.sklearn notfound, No module named 'mlmodels.model_sklearn.sklearn', tuple index out of range



### Error 29, [Traceback at line 862](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L862)<br />862..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 72, in module_load
<br />    module = import_module(f"mlmodels.{model_name}")
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/importlib/__init__.py", line 126, in import_module
<br />    return _bootstrap._gcd_import(name[level:], package, level)
<br />  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
<br />  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
<br />  File "<frozen importlib._bootstrap>", line 953, in _find_and_load_unlocked
<br />ModuleNotFoundError: No module named 'mlmodels.model_sklearn.sklearn'



### Error 30, [Traceback at line 874](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L874)<br />874..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 84, in module_load
<br />    model_name = str(Path(model_uri).parts[-2]) + "." + str(model_name)
<br />IndexError: tuple index out of range



### Error 31, [Traceback at line 881](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L881)<br />881..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/example/benchmark_timeseries_m5.py", line 27, in <module>
<br />    import mxnet as mx
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/__init__.py", line 31, in <module>
<br />    from . import contrib
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/__init__.py", line 31, in <module>
<br />    from . import onnx
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/onnx/__init__.py", line 19, in <module>
<br />    from .onnx2mx.import_model import import_model, get_model_metadata
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/onnx/onnx2mx/__init__.py", line 20, in <module>
<br />    from . import import_model
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/onnx/onnx2mx/import_model.py", line 22, in <module>
<br />    from .import_onnx import GraphProto
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/onnx/onnx2mx/import_onnx.py", line 26, in <module>
<br />    from ._import_helper import _convert_map as convert_map
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/onnx/onnx2mx/_import_helper.py", line 21, in <module>
<br />    from ._op_translations import identity, random_uniform, random_normal, sample_multinomial
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/onnx/onnx2mx/_op_translations.py", line 22, in <module>
<br />    from . import _translation_utils as translation_utils
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/contrib/onnx/onnx2mx/_translation_utils.py", line 23, in <module>
<br />    from .... import  module
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/module/__init__.py", line 22, in <module>
<br />    from .base_module import BaseModule
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/module/base_module.py", line 31, in <module>
<br />    from ..model import BatchEndParam
<br />  File "/opt/hostedtoolcache/Python/3.6.11/x64/lib/python3.6/site-packages/mxnet/model.py", line 46, in <module>
<br />    from sklearn.base import BaseEstimator
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/example/sklearn.py", line 34, in <module>
<br />    module        =  module_load( model_uri= model_uri )                           # Load file definition
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/models.py", line 89, in module_load
<br />    raise NameError(f"Module {model_name} notfound, {e1}, {e2}")
<br />NameError: Module model_sklearn.sklearn notfound, No module named 'mlmodels.model_sklearn.sklearn', tuple index out of range



### Error 32, [Traceback at line 929](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L929)<br />929..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/example//lightgbm_glass.py", line 16, in <module>
<br />    print( os.getcwd())
<br />NameError: name 'os' is not defined
<br />SyntaxError: invalid syntax



### Error 33, [Traceback at line 963](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L963)<br />963..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/example//arun_model.py", line 27, in <module>
<br />    pars = json.load(open(config_path , mode='r'))[config_mode]
<br />FileNotFoundError: [Errno 2] No such file or directory: 'https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/model_keras/ardmn.json'



### Error 34, [Traceback at line 975](https://github.com/arita37/mlmodels_store/blob/master/log_jupyter/log_jupyter.py#L975)<br />975..Traceback (most recent call last):
<br />  File "https://github.com/arita37/mlmodels/tree/13f78dac13e826a41e3a7922ab3568a9b02adef6/mlmodels/example//arun_hyper.py", line 2, in <module>
<br />    from jsoncomment import JsonComment ; json = JsonComment(), copy
<br />NameError: name 'copy' is not defined
