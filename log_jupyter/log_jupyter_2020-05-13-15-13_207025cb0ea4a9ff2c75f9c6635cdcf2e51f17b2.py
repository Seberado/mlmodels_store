
  test_jupyter /home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json Namespace(config_file='/home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json', config_mode='test', do='test_jupyter', folder=None, log_file=None, save_folder='ztest/') 

  ml_test --do test_jupyter 





 ************************************************************************************************************************

 ******** TAG ::  {'github_repo_url': 'https://github.com/arita37/mlmodels/tree/207025cb0ea4a9ff2c75f9c6635cdcf2e51f17b2', 'url_branch_file': 'https://github.com/arita37/mlmodels/blob/dev/', 'repo': 'arita37/mlmodels', 'branch': 'dev', 'sha': '207025cb0ea4a9ff2c75f9c6635cdcf2e51f17b2', 'workflow': 'test_jupyter'}

 ******** GITHUB_WOKFLOW : https://github.com/arita37/mlmodels/actions?query=workflow%3Atest_jupyter

 ******** GITHUB_REPO_BRANCH : https://github.com/arita37/mlmodels/tree/dev/

 ******** GITHUB_REPO_URL : https://github.com/arita37/mlmodels/tree/207025cb0ea4a9ff2c75f9c6635cdcf2e51f17b2

 ******** GITHUB_COMMIT_URL : https://github.com/arita37/mlmodels/commit/207025cb0ea4a9ff2c75f9c6635cdcf2e51f17b2

 ************************************************************************************************************************
/home/runner/work/mlmodels/mlmodels/mlmodels/example/
############ List of files ################################
['ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//sklearn_titanic_svm.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//lightgbm.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//sklearn_titanic_randomForest.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//fashion_MNIST_mlmodels.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//lightgbm_home_retail.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//keras_charcnn_reuters.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//gluon_automl.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//vison_fashion_MNIST.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//tensorflow_1_lstm.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//vision_mnist.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//lightgbm_glass.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//keras-textcnn.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//sklearn_titanic_randomForest_example2.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//mnist_mlmodels_.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//gluon_automl_titanic.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//tensorflow__lstm_json.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//sklearn.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//lightgbm_titanic.ipynb', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//vision_mnist.py', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//benchmark_timeseries_m4.py', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//arun_hyper.py', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//lightgbm_glass.py', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//benchmark_timeseries_m5.py', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example//arun_model.py', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example/benchmark_timeseries_m4.py', 'ipython /home/runner/work/mlmodels/mlmodels/mlmodels/example/benchmark_timeseries_m5.py']





 ************************************************************************************************************************
############ Running Jupyter files ################################





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//sklearn_titanic_svm.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mModuleNotFoundError[0m                       Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/models.py[0m in [0;36mmodule_load[0;34m(model_uri, verbose, env_build)[0m
[1;32m     71[0m         [0mmodel_name[0m [0;34m=[0m [0mmodel_uri[0m[0;34m.[0m[0mreplace[0m[0;34m([0m[0;34m".py"[0m[0;34m,[0m [0;34m""[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0;32m---> 72[0;31m         [0mmodule[0m [0;34m=[0m [0mimport_module[0m[0;34m([0m[0;34mf"mlmodels.{model_name}"[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     73[0m         [0;31m# module    = import_module("mlmodels.model_tf.1_lstm")[0m[0;34m[0m[0;34m[0m[0;34m[0m[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py[0m in [0;36mimport_module[0;34m(name, package)[0m
[1;32m    125[0m             [0mlevel[0m [0;34m+=[0m [0;36m1[0m[0;34m[0m[0;34m[0m[0m
[0;32m--> 126[0;31m     [0;32mreturn[0m [0m_bootstrap[0m[0;34m.[0m[0m_gcd_import[0m[0;34m([0m[0mname[0m[0;34m[[0m[0mlevel[0m[0;34m:[0m[0;34m][0m[0;34m,[0m [0mpackage[0m[0;34m,[0m [0mlevel[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m    127[0m [0;34m[0m[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/_bootstrap.py[0m in [0;36m_gcd_import[0;34m(name, package, level)[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/_bootstrap.py[0m in [0;36m_find_and_load[0;34m(name, import_)[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/_bootstrap.py[0m in [0;36m_find_and_load_unlocked[0;34m(name, import_)[0m

[0;31mModuleNotFoundError[0m: No module named 'mlmodels.model_sklearn.sklearn'

During handling of the above exception, another exception occurred:

[0;31mIndexError[0m                                Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/models.py[0m in [0;36mmodule_load[0;34m(model_uri, verbose, env_build)[0m
[1;32m     83[0m             [0mmodel_name[0m [0;34m=[0m [0mPath[0m[0;34m([0m[0mmodel_uri[0m[0;34m)[0m[0;34m.[0m[0mstem[0m  [0;31m# remove .py[0m[0;34m[0m[0;34m[0m[0m
[0;32m---> 84[0;31m             [0mmodel_name[0m [0;34m=[0m [0mstr[0m[0;34m([0m[0mPath[0m[0;34m([0m[0mmodel_uri[0m[0;34m)[0m[0;34m.[0m[0mparts[0m[0;34m[[0m[0;34m-[0m[0;36m2[0m[0;34m][0m[0;34m)[0m [0;34m+[0m [0;34m"."[0m [0;34m+[0m [0mstr[0m[0;34m([0m[0mmodel_name[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     85[0m             [0;31m# print(model_name)[0m[0;34m[0m[0;34m[0m[0;34m[0m[0m

[0;31mIndexError[0m: tuple index out of range

During handling of the above exception, another exception occurred:

[0;31mNameError[0m                                 Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//sklearn_titanic_svm.ipynb[0m in [0;36m<module>[0;34m[0m
[1;32m      3[0m [0;34m[0m[0m
[1;32m      4[0m [0mmodel_uri[0m    [0;34m=[0m [0;34m"model_sklearn.sklearn.py"[0m[0;34m[0m[0;34m[0m[0m
[0;32m----> 5[0;31m [0mmodule[0m        [0;34m=[0m  [0mmodule_load[0m[0;34m([0m [0mmodel_uri[0m[0;34m=[0m [0mmodel_uri[0m [0;34m)[0m                           [0;31m# Load file definition[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      6[0m [0;34m[0m[0m
[1;32m      7[0m model_pars, data_pars, compute_pars, out_pars = module.get_params(param_pars={

[0;32m~/work/mlmodels/mlmodels/mlmodels/models.py[0m in [0;36mmodule_load[0;34m(model_uri, verbose, env_build)[0m
[1;32m     87[0m [0;34m[0m[0m
[1;32m     88[0m         [0;32mexcept[0m [0mException[0m [0;32mas[0m [0me2[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
[0;32m---> 89[0;31m             [0;32mraise[0m [0mNameError[0m[0;34m([0m[0;34mf"Module {model_name} notfound, {e1}, {e2}"[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     90[0m [0;34m[0m[0m
[1;32m     91[0m     [0;32mif[0m [0mverbose[0m[0;34m:[0m [0mprint[0m[0;34m([0m[0mmodule[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m

[0;31mNameError[0m: Module model_sklearn.sklearn notfound, No module named 'mlmodels.model_sklearn.sklearn', tuple index out of range





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//lightgbm.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mFileNotFoundError[0m                         Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//lightgbm.ipynb[0m in [0;36m<module>[0;34m[0m
[1;32m      4[0m [0mdata_path[0m [0;34m=[0m [0;34m'lightgbm_titanic.json'[0m[0;34m[0m[0;34m[0m[0m
[1;32m      5[0m [0;34m[0m[0m
[0;32m----> 6[0;31m [0mpars[0m [0;34m=[0m [0mjson[0m[0;34m.[0m[0mload[0m[0;34m([0m[0mopen[0m[0;34m([0m [0mdata_path[0m [0;34m,[0m [0mmode[0m[0;34m=[0m[0;34m'r'[0m[0;34m)[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      7[0m [0;32mfor[0m [0mkey[0m[0;34m,[0m [0mpdict[0m [0;32min[0m  [0mpars[0m[0;34m.[0m[0mitems[0m[0;34m([0m[0;34m)[0m [0;34m:[0m[0;34m[0m[0;34m[0m[0m
[1;32m      8[0m   [0mglobals[0m[0;34m([0m[0;34m)[0m[0;34m[[0m[0mkey[0m[0;34m][0m [0;34m=[0m [0mpdict[0m[0;34m[0m[0;34m[0m[0m

[0;31mFileNotFoundError[0m: [Errno 2] No such file or directory: 'lightgbm_titanic.json'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//sklearn_titanic_randomForest.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mModuleNotFoundError[0m                       Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/models.py[0m in [0;36mmodule_load[0;34m(model_uri, verbose, env_build)[0m
[1;32m     71[0m         [0mmodel_name[0m [0;34m=[0m [0mmodel_uri[0m[0;34m.[0m[0mreplace[0m[0;34m([0m[0;34m".py"[0m[0;34m,[0m [0;34m""[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0;32m---> 72[0;31m         [0mmodule[0m [0;34m=[0m [0mimport_module[0m[0;34m([0m[0;34mf"mlmodels.{model_name}"[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     73[0m         [0;31m# module    = import_module("mlmodels.model_tf.1_lstm")[0m[0;34m[0m[0;34m[0m[0;34m[0m[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py[0m in [0;36mimport_module[0;34m(name, package)[0m
[1;32m    125[0m             [0mlevel[0m [0;34m+=[0m [0;36m1[0m[0;34m[0m[0;34m[0m[0m
[0;32m--> 126[0;31m     [0;32mreturn[0m [0m_bootstrap[0m[0;34m.[0m[0m_gcd_import[0m[0;34m([0m[0mname[0m[0;34m[[0m[0mlevel[0m[0;34m:[0m[0;34m][0m[0;34m,[0m [0mpackage[0m[0;34m,[0m [0mlevel[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m    127[0m [0;34m[0m[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/_bootstrap.py[0m in [0;36m_gcd_import[0;34m(name, package, level)[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/_bootstrap.py[0m in [0;36m_find_and_load[0;34m(name, import_)[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/_bootstrap.py[0m in [0;36m_find_and_load_unlocked[0;34m(name, import_)[0m

[0;31mModuleNotFoundError[0m: No module named 'mlmodels.model_sklearn.sklearn'

During handling of the above exception, another exception occurred:

[0;31mIndexError[0m                                Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/models.py[0m in [0;36mmodule_load[0;34m(model_uri, verbose, env_build)[0m
[1;32m     83[0m             [0mmodel_name[0m [0;34m=[0m [0mPath[0m[0;34m([0m[0mmodel_uri[0m[0;34m)[0m[0;34m.[0m[0mstem[0m  [0;31m# remove .py[0m[0;34m[0m[0;34m[0m[0m
[0;32m---> 84[0;31m             [0mmodel_name[0m [0;34m=[0m [0mstr[0m[0;34m([0m[0mPath[0m[0;34m([0m[0mmodel_uri[0m[0;34m)[0m[0;34m.[0m[0mparts[0m[0;34m[[0m[0;34m-[0m[0;36m2[0m[0;34m][0m[0;34m)[0m [0;34m+[0m [0;34m"."[0m [0;34m+[0m [0mstr[0m[0;34m([0m[0mmodel_name[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     85[0m             [0;31m# print(model_name)[0m[0;34m[0m[0;34m[0m[0;34m[0m[0m

[0;31mIndexError[0m: tuple index out of range

During handling of the above exception, another exception occurred:

[0;31mNameError[0m                                 Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//sklearn_titanic_randomForest.ipynb[0m in [0;36m<module>[0;34m[0m
[1;32m      2[0m [0;34m[0m[0m
[1;32m      3[0m [0mmodel_uri[0m    [0;34m=[0m [0;34m"model_sklearn.sklearn.py"[0m[0;34m[0m[0;34m[0m[0m
[0;32m----> 4[0;31m [0mmodule[0m        [0;34m=[0m  [0mmodule_load[0m[0;34m([0m [0mmodel_uri[0m[0;34m=[0m [0mmodel_uri[0m [0;34m)[0m                           [0;31m# Load file definition[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      5[0m [0;34m[0m[0m
[1;32m      6[0m model_pars, data_pars, compute_pars, out_pars = module.get_params(param_pars={

[0;32m~/work/mlmodels/mlmodels/mlmodels/models.py[0m in [0;36mmodule_load[0;34m(model_uri, verbose, env_build)[0m
[1;32m     87[0m [0;34m[0m[0m
[1;32m     88[0m         [0;32mexcept[0m [0mException[0m [0;32mas[0m [0me2[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
[0;32m---> 89[0;31m             [0;32mraise[0m [0mNameError[0m[0;34m([0m[0;34mf"Module {model_name} notfound, {e1}, {e2}"[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     90[0m [0;34m[0m[0m
[1;32m     91[0m     [0;32mif[0m [0mverbose[0m[0;34m:[0m [0mprint[0m[0;34m([0m[0mmodule[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m

[0;31mNameError[0m: Module model_sklearn.sklearn notfound, No module named 'mlmodels.model_sklearn.sklearn', tuple index out of range





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//fashion_MNIST_mlmodels.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mModuleNotFoundError[0m                       Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//fashion_MNIST_mlmodels.ipynb[0m in [0;36m<module>[0;34m[0m
[0;32m----> 1[0;31m [0;32mfrom[0m [0mgoogle[0m[0;34m.[0m[0mcolab[0m [0;32mimport[0m [0mdrive[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      2[0m [0mdrive[0m[0;34m.[0m[0mmount[0m[0;34m([0m[0;34m'/content/drive'[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m

[0;31mModuleNotFoundError[0m: No module named 'google.colab'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//lightgbm_home_retail.ipynb 

Deprecaton set to False
[0;31m---------------------------------------------------------------------------[0m
[0;31mFileNotFoundError[0m                         Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//lightgbm_home_retail.ipynb[0m in [0;36m<module>[0;34m[0m
[1;32m      1[0m [0mdata_path[0m [0;34m=[0m [0;34m'hyper_lightgbm_home_retail.json'[0m[0;34m[0m[0;34m[0m[0m
[1;32m      2[0m [0;34m[0m[0m
[0;32m----> 3[0;31m [0mpars[0m [0;34m=[0m [0mjson[0m[0;34m.[0m[0mload[0m[0;34m([0m[0mopen[0m[0;34m([0m [0mdata_path[0m [0;34m,[0m [0mmode[0m[0;34m=[0m[0;34m'r'[0m[0;34m)[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      4[0m [0;32mfor[0m [0mkey[0m[0;34m,[0m [0mpdict[0m [0;32min[0m  [0mpars[0m[0;34m.[0m[0mitems[0m[0;34m([0m[0;34m)[0m [0;34m:[0m[0;34m[0m[0;34m[0m[0m
[1;32m      5[0m   [0mglobals[0m[0;34m([0m[0;34m)[0m[0;34m[[0m[0mkey[0m[0;34m][0m [0;34m=[0m [0mpdict[0m[0;34m[0m[0;34m[0m[0m

[0;31mFileNotFoundError[0m: [Errno 2] No such file or directory: 'hyper_lightgbm_home_retail.json'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//keras_charcnn_reuters.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mFileNotFoundError[0m                         Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//keras_charcnn_reuters.ipynb[0m in [0;36m<module>[0;34m[0m
[0;32m----> 1[0;31m [0mpars[0m [0;34m=[0m [0mjson[0m[0;34m.[0m[0mload[0m[0;34m([0m[0mopen[0m[0;34m([0m [0mconfig_path[0m [0;34m,[0m [0mmode[0m[0;34m=[0m[0;34m'r'[0m[0;34m)[0m[0;34m)[0m[0;34m[[0m[0mconfig_mode[0m[0;34m][0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      2[0m [0mmodel_pars[0m      [0;34m=[0m [0mpath_norm_dict[0m[0;34m([0m [0mpars[0m[0;34m[[0m[0;34m'model_pars'[0m[0;34m][0m [0;34m)[0m[0;34m[0m[0;34m[0m[0m
[1;32m      3[0m [0mdata_pars[0m       [0;34m=[0m [0mpath_norm_dict[0m[0;34m([0m [0mpars[0m[0;34m[[0m[0;34m'data_pars'[0m[0;34m][0m [0;34m)[0m[0;34m[0m[0;34m[0m[0m
[1;32m      4[0m [0mcompute_pars[0m    [0;34m=[0m [0mpath_norm_dict[0m[0;34m([0m [0mpars[0m[0;34m[[0m[0;34m'compute_pars'[0m[0;34m][0m [0;34m)[0m[0;34m[0m[0;34m[0m[0m
[1;32m      5[0m [0mout_pars[0m        [0;34m=[0m [0mpath_norm_dict[0m[0;34m([0m [0mpars[0m[0;34m[[0m[0;34m'out_pars'[0m[0;34m][0m [0;34m)[0m[0;34m[0m[0;34m[0m[0m

[0;31mFileNotFoundError[0m: [Errno 2] No such file or directory: 'reuters_charcnn.json'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//gluon_automl.ipynb 

/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/mxnet/optimizer/optimizer.py:167: UserWarning: WARNING: New optimizer gluonnlp.optimizer.lamb.LAMB is overriding existing optimizer mxnet.optimizer.optimizer.LAMB
  Optimizer.opt_registry[name].__name__))
Loaded data from: https://autogluon.s3.amazonaws.com/datasets/Inc/train.csv | Columns = 15 / 15 | Rows = 39073 -> 39073
Warning: `hyperparameter_tune=True` is currently experimental and may cause the process to hang. Setting `auto_stack=True` instead is recommended to achieve maximum quality models.
Beginning AutoGluon training ... Time limit = 120s
AutoGluon will save models to dataset/
Train Data Rows:    39073
Train Data Columns: 15
Preprocessing data ...
Here are the first 10 unique label values in your data:  [' Tech-support' ' Transport-moving' ' Other-service' ' ?'
 ' Handlers-cleaners' ' Sales' ' Craft-repair' ' Adm-clerical'
 ' Exec-managerial' ' Prof-specialty']
AutoGluon infers your prediction problem is: multiclass  (because dtype of label-column == object)
If this is wrong, please specify `problem_type` argument in fit() instead (You may specify problem_type as one of: ['binary', 'multiclass', 'regression'])

Feature Generator processed 39073 data points with 14 features
Original Features:
	int features: 6
	object features: 8
Generated Features:
	int features: 0
All Features:
	int features: 6
	object features: 8
	Data preprocessing and feature engineering runtime = 0.25s ...
AutoGluon will gauge predictive performance using evaluation metric: accuracy
To change this, specify the eval_metric argument of fit()
AutoGluon will early stop models using evaluation metric: accuracy
Saving dataset/learner.pkl
Beginning hyperparameter tuning for Gradient Boosting Model...
Hyperparameter search space for Gradient Boosting Model: 
num_leaves:   Int: lower=26, upper=30
learning_rate:   Real: lower=0.005, upper=0.2
feature_fraction:   Real: lower=0.75, upper=1.0
min_data_in_leaf:   Int: lower=2, upper=30
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/autogluon/utils/tabular/ml/trainer/abstract_trainer.py", line 360, in train_single_full
    Y_train=y_train, Y_test=y_test, scheduler_options=(self.scheduler_func, self.scheduler_options), verbosity=self.verbosity)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/autogluon/utils/tabular/ml/models/lgb/lgb_model.py", line 283, in hyperparameter_tune
    directory=directory, lgb_model=self, **params_copy)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/autogluon/core/decorator.py", line 69, in register_args
    self.update(**kwvars)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/autogluon/core/decorator.py", line 79, in update
    hp = v.get_hp(name=k)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/autogluon/core/space.py", line 451, in get_hp
    default_value=self._default)
  File "ConfigSpace/hyperparameters.pyx", line 773, in ConfigSpace.hyperparameters.UniformIntegerHyperparameter.__init__
  File "ConfigSpace/hyperparameters.pyx", line 843, in ConfigSpace.hyperparameters.UniformIntegerHyperparameter.check_default
Warning: Exception caused LightGBMClassifier to fail during hyperparameter tuning... Skipping this model.
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/autogluon/utils/tabular/ml/trainer/abstract_trainer.py", line 360, in train_single_full
    Y_train=y_train, Y_test=y_test, scheduler_options=(self.scheduler_func, self.scheduler_options), verbosity=self.verbosity)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/autogluon/utils/tabular/ml/models/lgb/lgb_model.py", line 283, in hyperparameter_tune
    directory=directory, lgb_model=self, **params_copy)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/autogluon/core/decorator.py", line 69, in register_args
    self.update(**kwvars)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/autogluon/core/decorator.py", line 79, in update
    hp = v.get_hp(name=k)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/autogluon/core/space.py", line 451, in get_hp
    default_value=self._default)
  File "ConfigSpace/hyperparameters.pyx", line 773, in ConfigSpace.hyperparameters.UniformIntegerHyperparameter.__init__
  File "ConfigSpace/hyperparameters.pyx", line 843, in ConfigSpace.hyperparameters.UniformIntegerHyperparameter.check_default
ValueError: Illegal default value 36
Saving dataset/models/trainer.pkl
Beginning hyperparameter tuning for Neural Network...
Hyperparameter search space for Neural Network: 
network_type:   Categorical['widedeep', 'feedforward']
layers:   Categorical[[100], [1000], [200, 100], [300, 200, 100]]
activation:   Categorical['relu', 'softrelu', 'tanh']
embedding_size_factor:   Real: lower=0.5, upper=1.5
use_batchnorm:   Categorical[True, False]
dropout_prob:   Real: lower=0.0, upper=0.5
learning_rate:   Real: lower=0.0001, upper=0.01
weight_decay:   Real: lower=1e-12, upper=0.1
AutoGluon Neural Network infers features are of the following types:
{
    "continuous": [
        "age",
        "education-num",
        "hours-per-week"
    ],
    "skewed": [
        "fnlwgt",
        "capital-gain",
        "capital-loss"
    ],
    "onehot": [
        "sex",
        "class"
    ],
    "embed": [
        "workclass",
        "education",
        "marital-status",
        "relationship",
        "race",
        "native-country"
    ],
    "language": []
}


Saving dataset/models/NeuralNetClassifier/train_tabNNdataset.pkl
Saving dataset/models/NeuralNetClassifier/validation_tabNNdataset.pkl
Starting Experiments
Num of Finished Tasks is 0
Num of Pending Tasks is 5
  0%|          | 0/5 [00:00<?, ?it/s]Loading: dataset/models/NeuralNetClassifier/train_tabNNdataset.pkl
Loading: dataset/models/NeuralNetClassifier/validation_tabNNdataset.pkl
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
Saving dataset/models/NeuralNetClassifier/trial_0_tabularNN.pkl
Finished Task with config: {'activation.choice': 0, 'dropout_prob': 0.1, 'embedding_size_factor': 1.0, 'layers.choice': 0, 'learning_rate': 0.0005, 'network_type.choice': 0, 'use_batchnorm.choice': 0, 'weight_decay': 1e-06} and reward: 0.3862
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\xb9\x99\x99\x99\x99\x99\x9aX\x15\x00\x00\x00embedding_size_factorq\x03G?\xf0\x00\x00\x00\x00\x00\x00X\r\x00\x00\x00layers.choiceq\x04K\x00X\r\x00\x00\x00learning_rateq\x05G?@bM\xd2\xf1\xa9\xfcX\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G>\xb0\xc6\xf7\xa0\xb5\xed\x8du.' and reward: 0.3862
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\xb9\x99\x99\x99\x99\x99\x9aX\x15\x00\x00\x00embedding_size_factorq\x03G?\xf0\x00\x00\x00\x00\x00\x00X\r\x00\x00\x00layers.choiceq\x04K\x00X\r\x00\x00\x00learning_rateq\x05G?@bM\xd2\xf1\xa9\xfcX\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G>\xb0\xc6\xf7\xa0\xb5\xed\x8du.' and reward: 0.3862
 40%|████      | 2/5 [00:50<01:15, 25.13s/it]Loading: dataset/models/NeuralNetClassifier/train_tabNNdataset.pkl
Loading: dataset/models/NeuralNetClassifier/validation_tabNNdataset.pkl
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
Saving dataset/models/NeuralNetClassifier/trial_1_tabularNN.pkl
Finished Task with config: {'activation.choice': 2, 'dropout_prob': 0.14621682290342328, 'embedding_size_factor': 0.6036093827231163, 'layers.choice': 2, 'learning_rate': 0.0003444093159222698, 'network_type.choice': 1, 'use_batchnorm.choice': 1, 'weight_decay': 0.0032119675001038026} and reward: 0.3574
Finished Task with config: b"\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x02X\x0c\x00\x00\x00dropout_probq\x02G?\xc2\xb7;\x9c?c\x97X\x15\x00\x00\x00embedding_size_factorq\x03G?\xe3P\xc4\x9f\xcbXSX\r\x00\x00\x00layers.choiceq\x04K\x02X\r\x00\x00\x00learning_rateq\x05G?6\x92:\xbf\x92'cX\x13\x00\x00\x00network_type.choiceq\x06K\x01X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x01X\x0c\x00\x00\x00weight_decayq\x08G?jO\xfb\xeb\xcc\xe3Bu." and reward: 0.3574
Finished Task with config: b"\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x02X\x0c\x00\x00\x00dropout_probq\x02G?\xc2\xb7;\x9c?c\x97X\x15\x00\x00\x00embedding_size_factorq\x03G?\xe3P\xc4\x9f\xcbXSX\r\x00\x00\x00layers.choiceq\x04K\x02X\r\x00\x00\x00learning_rateq\x05G?6\x92:\xbf\x92'cX\x13\x00\x00\x00network_type.choiceq\x06K\x01X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x01X\x0c\x00\x00\x00weight_decayq\x08G?jO\xfb\xeb\xcc\xe3Bu." and reward: 0.3574
 60%|██████    | 3/5 [01:40<01:05, 32.80s/it] 60%|██████    | 3/5 [01:40<01:07, 33.65s/it]
Loading: dataset/models/NeuralNetClassifier/train_tabNNdataset.pkl
Loading: dataset/models/NeuralNetClassifier/validation_tabNNdataset.pkl
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
Saving dataset/models/NeuralNetClassifier/trial_2_tabularNN.pkl
Finished Task with config: {'activation.choice': 0, 'dropout_prob': 0.011492933134801321, 'embedding_size_factor': 1.2371779804249403, 'layers.choice': 2, 'learning_rate': 0.0001855914386737694, 'network_type.choice': 1, 'use_batchnorm.choice': 0, 'weight_decay': 0.00023238564786049582} and reward: 0.3852
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\x87\x89\x9b_\x97\xba\xa1X\x15\x00\x00\x00embedding_size_factorq\x03G?\xf3\xcb{#T\x1ahX\r\x00\x00\x00layers.choiceq\x04K\x02X\r\x00\x00\x00learning_rateq\x05G?(SjQ\xac\xca\xf3X\x13\x00\x00\x00network_type.choiceq\x06K\x01X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G?.u\x91\x83\xe6\xd8\xf8u.' and reward: 0.3852
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\x87\x89\x9b_\x97\xba\xa1X\x15\x00\x00\x00embedding_size_factorq\x03G?\xf3\xcb{#T\x1ahX\r\x00\x00\x00layers.choiceq\x04K\x02X\r\x00\x00\x00learning_rateq\x05G?(SjQ\xac\xca\xf3X\x13\x00\x00\x00network_type.choiceq\x06K\x01X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G?.u\x91\x83\xe6\xd8\xf8u.' and reward: 0.3852
Please either provide filename or allow plot in get_training_curves
Time for Neural Network hyperparameter optimization: 152.83834791183472
Best hyperparameter configuration for Tabular Neural Network: 
{'activation.choice': 0, 'dropout_prob': 0.1, 'embedding_size_factor': 1.0, 'layers.choice': 0, 'learning_rate': 0.0005, 'network_type.choice': 0, 'use_batchnorm.choice': 0, 'weight_decay': 1e-06}
Saving dataset/models/trainer.pkl
Loading: dataset/models/NeuralNetClassifier/trial_0_tabularNN.pkl
Loading: dataset/models/NeuralNetClassifier/trial_1_tabularNN.pkl
Loading: dataset/models/NeuralNetClassifier/trial_2_tabularNN.pkl
Fitting model: weighted_ensemble_k0_l1 ... Training model for up to 119.75s of the -35.39s of remaining time.
Ensemble size: 71
Ensemble weights: 
[0.6056338  0.15492958 0.23943662]
	0.3934	 = Validation accuracy score
	1.05s	 = Training runtime
	0.0s	 = Validation runtime
Saving dataset/models/weighted_ensemble_k0_l1/model.pkl
Saving dataset/models/trainer.pkl
Saving dataset/models/trainer.pkl
Saving dataset/models/trainer.pkl
AutoGluon training complete, total runtime = 156.48s ...
Loading: dataset/models/trainer.pkl
Loaded data from: https://autogluon.s3.amazonaws.com/datasets/Inc/test.csv | Columns = 15 / 15 | Rows = 9769 -> 9769
Loading: dataset/models/trainer.pkl
Loading: dataset/models/weighted_ensemble_k0_l1/model.pkl
Loading: dataset/models/NeuralNetClassifier/trial_0_tabularNN.pkl
Loading: dataset/models/NeuralNetClassifier/trial_2_tabularNN.pkl
Loading: dataset/models/NeuralNetClassifier/trial_1_tabularNN.pkl
test

  #### Module init   ############################################ 

  <module 'mlmodels.model_gluon.gluon_automl' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluon_automl.py'> 

  #### Loading params   ############################################## 
/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/mxnet/optimizer/optimizer.py:167: UserWarning: WARNING: New optimizer gluonnlp.optimizer.lamb.LAMB is overriding existing optimizer mxnet.optimizer.optimizer.LAMB
  Optimizer.opt_registry[name].__name__))
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 523, in main
    test_cli(arg)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 453, in test_cli
    test_module(arg.model_uri, param_pars=param_pars)  # '1_lstm'
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 257, in test_module
    model_pars, data_pars, compute_pars, out_pars = module.get_params(param_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluon_automl.py", line 109, in get_params
    return model_pars, data_pars, compute_pars, out_pars
UnboundLocalError: local variable 'model_pars' referenced before assignment





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//vison_fashion_MNIST.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mModuleNotFoundError[0m                       Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//vison_fashion_MNIST.ipynb[0m in [0;36m<module>[0;34m[0m
[0;32m----> 1[0;31m [0;32mfrom[0m [0mgoogle[0m[0;34m.[0m[0mcolab[0m [0;32mimport[0m [0mdrive[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      2[0m [0mdrive[0m[0;34m.[0m[0mmount[0m[0;34m([0m[0;34m'/content/drive'[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m

[0;31mModuleNotFoundError[0m: No module named 'google.colab'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//tensorflow_1_lstm.ipynb 

/home/runner/work/mlmodels/mlmodels
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6]}
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/compat/v2_compat.py:68: disable_resource_variables (from tensorflow.python.ops.variable_scope) is deprecated and will be removed in a future version.
Instructions for updating:
non-resource variables are not supported in the long term
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6]}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv
         Date        Open        High  ...       Close   Adj Close   Volume
0  2016-11-02  778.200012  781.650024  ...  768.700012  768.700012  1872400
1  2016-11-03  767.250000  769.950012  ...  762.130005  762.130005  1943200
2  2016-11-04  750.659973  770.359985  ...  762.020020  762.020020  2134800
3  2016-11-07  774.500000  785.190002  ...  782.520020  782.520020  1585100
4  2016-11-08  783.400024  795.632996  ...  790.510010  790.510010  1350800

[5 rows x 7 columns]
          0         1         2         3         4         5
0  0.706562  0.629914  0.682052  0.599302  0.599302  0.153665
1  0.458824  0.320251  0.598101  0.478596  0.478596  0.174523
2  0.083484  0.331101  0.437246  0.476576  0.476576  0.230969
3  0.622851  0.723606  0.854891  0.853206  0.853206  0.069025
4  0.824209  1.000000  1.000000  1.000000  1.000000  0.000000
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6]}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv
         Date        Open        High  ...       Close   Adj Close   Volume
0  2016-11-02  778.200012  781.650024  ...  768.700012  768.700012  1872400
1  2016-11-03  767.250000  769.950012  ...  762.130005  762.130005  1943200
2  2016-11-04  750.659973  770.359985  ...  762.020020  762.020020  2134800
3  2016-11-07  774.500000  785.190002  ...  782.520020  782.520020  1585100
4  2016-11-08  783.400024  795.632996  ...  790.510010  790.510010  1350800

[5 rows x 7 columns]
          0         1         2         3         4         5
0  0.706562  0.629914  0.682052  0.599302  0.599302  0.153665
1  0.458824  0.320251  0.598101  0.478596  0.478596  0.174523
2  0.083484  0.331101  0.437246  0.476576  0.476576  0.230969
3  0.622851  0.723606  0.854891  0.853206  0.853206  0.069025
4  0.824209  1.000000  1.000000  1.000000  1.000000  0.000000
5  0.745928  0.883387  0.838176  0.904464  0.904464  0.370110
6  1.000000  0.881878  0.467996  0.486496  0.486496  1.000000
7  0.216516  0.077549  0.433808  0.329598  0.329598  0.318466
8  0.195249  0.000000  0.000000  0.000000  0.000000  0.671960
9  0.000000  0.173783  0.369041  0.411721  0.411721  0.304384
test

  #### Module init   ############################################ 
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/compat/v2_compat.py:68: disable_resource_variables (from tensorflow.python.ops.variable_scope) is deprecated and will be removed in a future version.
Instructions for updating:
non-resource variables are not supported in the long term

  <module 'mlmodels.model_tf.1_lstm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf/1_lstm.py'> 

  #### Loading params   ############################################## 

  ############# Data, Params preparation   ################# 

  #### Model init   ############################################ 

  <mlmodels.model_tf.1_lstm.Model object at 0x7f5a2f7f4ac8> 

  #### Fit   ######################################################## 
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas'}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv
         Date        Open        High  ...       Close   Adj Close   Volume
0  2016-11-02  778.200012  781.650024  ...  768.700012  768.700012  1872400
1  2016-11-03  767.250000  769.950012  ...  762.130005  762.130005  1943200
2  2016-11-04  750.659973  770.359985  ...  762.020020  762.020020  2134800
3  2016-11-07  774.500000  785.190002  ...  782.520020  782.520020  1585100
4  2016-11-08  783.400024  795.632996  ...  790.510010  790.510010  1350800

[5 rows x 7 columns]
          0         1         2         3         4         5
0  0.706562  0.629914  0.682052  0.599302  0.599302  0.153665
1  0.458824  0.320251  0.598101  0.478596  0.478596  0.174523
2  0.083484  0.331101  0.437246  0.476576  0.476576  0.230969
3  0.622851  0.723606  0.854891  0.853206  0.853206  0.069025
4  0.824209  1.000000  1.000000  1.000000  1.000000  0.000000

  #### Predict   #################################################### 
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas'}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv
         Date        Open        High  ...       Close   Adj Close   Volume
0  2016-11-02  778.200012  781.650024  ...  768.700012  768.700012  1872400
1  2016-11-03  767.250000  769.950012  ...  762.130005  762.130005  1943200
2  2016-11-04  750.659973  770.359985  ...  762.020020  762.020020  2134800
3  2016-11-07  774.500000  785.190002  ...  782.520020  782.520020  1585100
4  2016-11-08  783.400024  795.632996  ...  790.510010  790.510010  1350800

[5 rows x 7 columns]
          0         1         2         3         4         5
0  0.706562  0.629914  0.682052  0.599302  0.599302  0.153665
1  0.458824  0.320251  0.598101  0.478596  0.478596  0.174523
2  0.083484  0.331101  0.437246  0.476576  0.476576  0.230969
3  0.622851  0.723606  0.854891  0.853206  0.853206  0.069025
4  0.824209  1.000000  1.000000  1.000000  1.000000  0.000000
5  0.745928  0.883387  0.838176  0.904464  0.904464  0.370110
6  1.000000  0.881878  0.467996  0.486496  0.486496  1.000000
7  0.216516  0.077549  0.433808  0.329598  0.329598  0.318466
8  0.195249  0.000000  0.000000  0.000000  0.000000  0.671960
9  0.000000  0.173783  0.369041  0.411721  0.411721  0.304384
[[ 0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00
   0.00000000e+00  0.00000000e+00]
 [ 7.26428330e-02  1.55150518e-02  1.34217605e-01 -2.58480478e-02
  -6.69654757e-02  1.14876218e-02]
 [-2.20347531e-02 -5.49045252e-03  1.67343274e-01  5.20004183e-02
  -3.16380933e-02 -9.05584777e-04]
 [-4.01820689e-02  1.01164907e-01  6.55476898e-02  1.03012711e-01
   1.17591619e-01 -7.28533939e-02]
 [ 4.34980661e-01 -2.16421396e-01  1.30733460e-01  2.07787514e-01
   3.10301423e-01  6.08249754e-02]
 [ 6.44609183e-02 -5.43516725e-02  2.58534364e-02  7.30995610e-02
  -7.27143735e-02 -2.15381235e-01]
 [ 6.46227598e-01 -2.57754117e-01  1.08865522e-01  5.63549846e-02
   3.13269496e-02  5.15304923e-01]
 [-1.11102939e-01  1.29630834e-01  8.47604752e-01 -2.95484483e-01
   3.76255542e-01  9.63786781e-01]
 [-4.19633567e-01  4.49557081e-02  3.07437927e-01  3.25595915e-01
   2.33728543e-01  4.22723800e-01]
 [ 0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00
   0.00000000e+00  0.00000000e+00]]

  #### Get  metrics   ################################################ 

  #### Save   ######################################################## 

  #### Load   ######################################################## 
model_tf/1_lstm.py
model_tf.1_lstm.py
<module 'mlmodels.model_tf.1_lstm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf/1_lstm.py'>
<module 'mlmodels.model_tf.1_lstm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf/1_lstm.py'>

  #### Loading params   ############################################## 

  ############# Data, Params preparation   ################# 

  {'learning_rate': 0.001, 'num_layers': 1, 'size': 6, 'size_layer': 128, 'timestep': 4, 'epoch': 2, 'output_size': 6} {'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas'} {} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/', 'model_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/model'} 

  #### Loading dataset   ############################################# 
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas'}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv
         Date        Open        High  ...       Close   Adj Close   Volume
0  2016-11-02  778.200012  781.650024  ...  768.700012  768.700012  1872400
1  2016-11-03  767.250000  769.950012  ...  762.130005  762.130005  1943200
2  2016-11-04  750.659973  770.359985  ...  762.020020  762.020020  2134800
3  2016-11-07  774.500000  785.190002  ...  782.520020  782.520020  1585100
4  2016-11-08  783.400024  795.632996  ...  790.510010  790.510010  1350800

[5 rows x 7 columns]

  #### Model init  ############################################# 

  #### Model fit   ############################################# 
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas'}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv
         Date        Open        High  ...       Close   Adj Close   Volume
0  2016-11-02  778.200012  781.650024  ...  768.700012  768.700012  1872400
1  2016-11-03  767.250000  769.950012  ...  762.130005  762.130005  1943200
2  2016-11-04  750.659973  770.359985  ...  762.020020  762.020020  2134800
3  2016-11-07  774.500000  785.190002  ...  782.520020  782.520020  1585100
4  2016-11-08  783.400024  795.632996  ...  790.510010  790.510010  1350800

[5 rows x 7 columns]
          0         1         2         3         4         5
0  0.706562  0.629914  0.682052  0.599302  0.599302  0.153665
1  0.458824  0.320251  0.598101  0.478596  0.478596  0.174523
2  0.083484  0.331101  0.437246  0.476576  0.476576  0.230969
3  0.622851  0.723606  0.854891  0.853206  0.853206  0.069025
4  0.824209  1.000000  1.000000  1.000000  1.000000  0.000000

  #### Predict   ##################################################### 
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas', 'train': 0}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv
         Date        Open        High  ...       Close   Adj Close   Volume
0  2016-11-02  778.200012  781.650024  ...  768.700012  768.700012  1872400
1  2016-11-03  767.250000  769.950012  ...  762.130005  762.130005  1943200
2  2016-11-04  750.659973  770.359985  ...  762.020020  762.020020  2134800
3  2016-11-07  774.500000  785.190002  ...  782.520020  782.520020  1585100
4  2016-11-08  783.400024  795.632996  ...  790.510010  790.510010  1350800

[5 rows x 7 columns]
          0         1         2         3         4         5
0  0.706562  0.629914  0.682052  0.599302  0.599302  0.153665
1  0.458824  0.320251  0.598101  0.478596  0.478596  0.174523
2  0.083484  0.331101  0.437246  0.476576  0.476576  0.230969
3  0.622851  0.723606  0.854891  0.853206  0.853206  0.069025
4  0.824209  1.000000  1.000000  1.000000  1.000000  0.000000
5  0.745928  0.883387  0.838176  0.904464  0.904464  0.370110
6  1.000000  0.881878  0.467996  0.486496  0.486496  1.000000
7  0.216516  0.077549  0.433808  0.329598  0.329598  0.318466
8  0.195249  0.000000  0.000000  0.000000  0.000000  0.671960
9  0.000000  0.173783  0.369041  0.411721  0.411721  0.304384

  #### metrics   ##################################################### 
{'loss': 0.47429081052541733, 'loss_history': []}

  #### Plot   ######################################################## 

  #### Save   ######################################################## 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/'}
Model saved in path: /home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm//model//model.ckpt

  #### Load   ######################################################## 
2020-05-13 15:16:28.531737: W tensorflow/core/framework/op_kernel.cc:1651] OP_REQUIRES failed at save_restore_v2_ops.cc:184 : Not found: Key Variable not found in checkpoint
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/', 'model_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/model'}
Failed Restoring from checkpoint failed. This is most likely due to a Variable name or other graph key that is missing from the checkpoint. Please ensure that you have not altered the graph expected based on the checkpoint. Original error:

Key Variable not found in checkpoint
	 [[node save_1/RestoreV2 (defined at opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/framework/ops.py:1748) ]]

Original stack trace for 'save_1/RestoreV2':
  File "opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
  File "home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 523, in main
    test_cli(arg)
  File "home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 455, in test_cli
    test(arg.model_uri)  # '1_lstm'
  File "home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 189, in test
    module.test()
  File "home/runner/work/mlmodels/mlmodels/mlmodels/model_tf/1_lstm.py", line 320, in test
    session = load(out_pars)
  File "home/runner/work/mlmodels/mlmodels/mlmodels/model_tf/1_lstm.py", line 199, in load
    return load_tf(load_pars)
  File "home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 474, in load_tf
    saver      = tf.compat.v1.train.Saver()
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 828, in __init__
    self.build()
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 840, in build
    self._build(self._filename, build_save=True, build_restore=True)
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 878, in _build
    build_restore=build_restore)
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 508, in _build_internal
    restore_sequentially, reshape)
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 328, in _AddRestoreOps
    restore_sequentially)
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 575, in bulk_restore
    return io_ops.restore_v2(filename_tensor, names, slices, dtypes)
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/gen_io_ops.py", line 1696, in restore_v2
    name=name)
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/framework/op_def_library.py", line 794, in _apply_op_helper
    op_def=op_def)
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/util/deprecation.py", line 507, in new_func
    return func(*args, **kwargs)
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/framework/ops.py", line 3357, in create_op
    attrs, op_def, compute_device)
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/framework/ops.py", line 3426, in _create_op_internal
    op_def=op_def)
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/framework/ops.py", line 1748, in __init__
    self._traceback = tf_stack.extract_stack()

model_tf/1_lstm.py
model_tf.1_lstm.py
<module 'mlmodels.model_tf.1_lstm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf/1_lstm.py'>
<module 'mlmodels.model_tf.1_lstm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf/1_lstm.py'>

  #### Loading params   ############################################## 

  ############# Data, Params preparation   ################# 

  {'learning_rate': 0.001, 'num_layers': 1, 'size': 6, 'size_layer': 128, 'timestep': 4, 'epoch': 2, 'output_size': 6} {'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas'} {} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/', 'model_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/model'} 

  #### Loading dataset   ############################################# 
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas'}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv
         Date        Open        High  ...       Close   Adj Close   Volume
0  2016-11-02  778.200012  781.650024  ...  768.700012  768.700012  1872400
1  2016-11-03  767.250000  769.950012  ...  762.130005  762.130005  1943200
2  2016-11-04  750.659973  770.359985  ...  762.020020  762.020020  2134800
3  2016-11-07  774.500000  785.190002  ...  782.520020  782.520020  1585100
4  2016-11-08  783.400024  795.632996  ...  790.510010  790.510010  1350800

[5 rows x 7 columns]

  #### Model init  ############################################# 

  #### Model fit   ############################################# 
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas'}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv
         Date        Open        High  ...       Close   Adj Close   Volume
0  2016-11-02  778.200012  781.650024  ...  768.700012  768.700012  1872400
1  2016-11-03  767.250000  769.950012  ...  762.130005  762.130005  1943200
2  2016-11-04  750.659973  770.359985  ...  762.020020  762.020020  2134800
3  2016-11-07  774.500000  785.190002  ...  782.520020  782.520020  1585100
4  2016-11-08  783.400024  795.632996  ...  790.510010  790.510010  1350800

[5 rows x 7 columns]
          0         1         2         3         4         5
0  0.706562  0.629914  0.682052  0.599302  0.599302  0.153665
1  0.458824  0.320251  0.598101  0.478596  0.478596  0.174523
2  0.083484  0.331101  0.437246  0.476576  0.476576  0.230969
3  0.622851  0.723606  0.854891  0.853206  0.853206  0.069025
4  0.824209  1.000000  1.000000  1.000000  1.000000  0.000000

  #### Predict   ##################################################### 
{'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv', 'data_type': 'pandas', 'train': 0}
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/timeseries/GOOG-year.csv
         Date        Open        High  ...       Close   Adj Close   Volume
0  2016-11-02  778.200012  781.650024  ...  768.700012  768.700012  1872400
1  2016-11-03  767.250000  769.950012  ...  762.130005  762.130005  1943200
2  2016-11-04  750.659973  770.359985  ...  762.020020  762.020020  2134800
3  2016-11-07  774.500000  785.190002  ...  782.520020  782.520020  1585100
4  2016-11-08  783.400024  795.632996  ...  790.510010  790.510010  1350800

[5 rows x 7 columns]
          0         1         2         3         4         5
0  0.706562  0.629914  0.682052  0.599302  0.599302  0.153665
1  0.458824  0.320251  0.598101  0.478596  0.478596  0.174523
2  0.083484  0.331101  0.437246  0.476576  0.476576  0.230969
3  0.622851  0.723606  0.854891  0.853206  0.853206  0.069025
4  0.824209  1.000000  1.000000  1.000000  1.000000  0.000000
5  0.745928  0.883387  0.838176  0.904464  0.904464  0.370110
6  1.000000  0.881878  0.467996  0.486496  0.486496  1.000000
7  0.216516  0.077549  0.433808  0.329598  0.329598  0.318466
8  0.195249  0.000000  0.000000  0.000000  0.000000  0.671960
9  0.000000  0.173783  0.369041  0.411721  0.411721  0.304384

  #### metrics   ##################################################### 
{'loss': 0.4834538847208023, 'loss_history': []}

  #### Plot   ######################################################## 

  #### Save   ######################################################## 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/'}
Model saved in path: /home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm//model//model.ckpt

  #### Load   ######################################################## 
2020-05-13 15:16:29.631170: W tensorflow/core/framework/op_kernel.cc:1651] OP_REQUIRES failed at save_restore_v2_ops.cc:184 : Not found: Key Variable not found in checkpoint
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/', 'model_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/model'}
Failed Restoring from checkpoint failed. This is most likely due to a Variable name or other graph key that is missing from the checkpoint. Please ensure that you have not altered the graph expected based on the checkpoint. Original error:

Key Variable not found in checkpoint
	 [[node save_1/RestoreV2 (defined at opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/framework/ops.py:1748) ]]

Original stack trace for 'save_1/RestoreV2':
  File "opt/hostedtoolcache/Python/3.6.10/x64/bin/ml_models", line 11, in <module>
    load_entry_point('mlmodels', 'console_scripts', 'ml_models')()
  File "home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 523, in main
    test_cli(arg)
  File "home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 457, in test_cli
    test_global(arg.model_uri)  # '1_lstm'
  File "home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 200, in test_global
    module.test()
  File "home/runner/work/mlmodels/mlmodels/mlmodels/model_tf/1_lstm.py", line 320, in test
    session = load(out_pars)
  File "home/runner/work/mlmodels/mlmodels/mlmodels/model_tf/1_lstm.py", line 199, in load
    return load_tf(load_pars)
  File "home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 474, in load_tf
    saver      = tf.compat.v1.train.Saver()
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 828, in __init__
    self.build()
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 840, in build
    self._build(self._filename, build_save=True, build_restore=True)
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 878, in _build
    build_restore=build_restore)
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 508, in _build_internal
    restore_sequentially, reshape)
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 328, in _AddRestoreOps
    restore_sequentially)
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 575, in bulk_restore
    return io_ops.restore_v2(filename_tensor, names, slices, dtypes)
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/gen_io_ops.py", line 1696, in restore_v2
    name=name)
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/framework/op_def_library.py", line 794, in _apply_op_helper
    op_def=op_def)
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/util/deprecation.py", line 507, in new_func
    return func(*args, **kwargs)
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/framework/ops.py", line 3357, in create_op
    attrs, op_def, compute_device)
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/framework/ops.py", line 3426, in _create_op_internal
    op_def=op_def)
  File "opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/framework/ops.py", line 1748, in __init__
    self._traceback = tf_stack.extract_stack()






 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//vision_mnist.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mModuleNotFoundError[0m                       Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//vision_mnist.ipynb[0m in [0;36m<module>[0;34m[0m
[0;32m----> 1[0;31m [0;32mfrom[0m [0mgoogle[0m[0;34m.[0m[0mcolab[0m [0;32mimport[0m [0mdrive[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      2[0m [0mdrive[0m[0;34m.[0m[0mmount[0m[0;34m([0m[0;34m'/content/drive'[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m

[0;31mModuleNotFoundError[0m: No module named 'google.colab'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//lightgbm_glass.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mNameError[0m                                 Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//lightgbm_glass.ipynb[0m in [0;36m<module>[0;34m[0m
[1;32m      8[0m [0;32mimport[0m [0mjson[0m[0;34m[0m[0;34m[0m[0m
[1;32m      9[0m [0;34m[0m[0m
[0;32m---> 10[0;31m [0mprint[0m[0;34m([0m [0mos[0m[0;34m.[0m[0mgetcwd[0m[0;34m([0m[0;34m)[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m
[0;31mNameError[0m: name 'os' is not defined





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//keras-textcnn.ipynb 

WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/resource_variable_ops.py:1630: calling BaseResourceVariable.__init__ (from tensorflow.python.ops.resource_variable_ops) with constraint is deprecated and will be removed in a future version.
Instructions for updating:
If using Keras pass *_constraint arguments to layers.
Model: "model_1"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
input_1 (InputLayer)            (None, 400)          0                                            
__________________________________________________________________________________________________
embedding_1 (Embedding)         (None, 400, 50)      500         input_1[0][0]                    
__________________________________________________________________________________________________
conv1d_1 (Conv1D)               (None, 398, 128)     19328       embedding_1[0][0]                
__________________________________________________________________________________________________
conv1d_2 (Conv1D)               (None, 397, 128)     25728       embedding_1[0][0]                
__________________________________________________________________________________________________
conv1d_3 (Conv1D)               (None, 396, 128)     32128       embedding_1[0][0]                
__________________________________________________________________________________________________
global_max_pooling1d_1 (GlobalM (None, 128)          0           conv1d_1[0][0]                   
__________________________________________________________________________________________________
global_max_pooling1d_2 (GlobalM (None, 128)          0           conv1d_2[0][0]                   
__________________________________________________________________________________________________
global_max_pooling1d_3 (GlobalM (None, 128)          0           conv1d_3[0][0]                   
__________________________________________________________________________________________________
concatenate_1 (Concatenate)     (None, 384)          0           global_max_pooling1d_1[0][0]     
                                                                 global_max_pooling1d_2[0][0]     
                                                                 global_max_pooling1d_3[0][0]     
__________________________________________________________________________________________________
dense_1 (Dense)                 (None, 1)            385         concatenate_1[0][0]              
==================================================================================================
Total params: 78,069
Trainable params: 78,069
Non-trainable params: 0
__________________________________________________________________________________________________
Loading data...
Downloading data from https://s3.amazonaws.com/text-datasets/imdb.npz

    8192/17464789 [..............................] - ETA: 0s
   24576/17464789 [..............................] - ETA: 46s
   57344/17464789 [..............................] - ETA: 39s
   90112/17464789 [..............................] - ETA: 37s
  122880/17464789 [..............................] - ETA: 36s
  278528/17464789 [..............................] - ETA: 20s
  581632/17464789 [..............................] - ETA: 11s
 1171456/17464789 [=>............................] - ETA: 6s 
 2326528/17464789 [==>...........................] - ETA: 3s
 4685824/17464789 [=======>......................] - ETA: 1s
 7225344/17464789 [===========>..................] - ETA: 0s
 9748480/17464789 [===============>..............] - ETA: 0s
12288000/17464789 [====================>.........] - ETA: 0s
14467072/17464789 [=======================>......] - ETA: 0s
16990208/17464789 [============================>.] - ETA: 0s
17465344/17464789 [==============================] - 1s 0us/step
Pad sequences (samples x time)...
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/math_grad.py:1424: where (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
2020-05-13 15:16:42.086318: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 AVX512F FMA
2020-05-13 15:16:42.090708: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2095090000 Hz
2020-05-13 15:16:42.090913: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x55bc79cf3b70 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-13 15:16:42.090927: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py:422: The name tf.global_variables is deprecated. Please use tf.compat.v1.global_variables instead.

Train on 25000 samples, validate on 25000 samples
Epoch 1/1

   32/25000 [..............................] - ETA: 4:49 - loss: 6.7083 - accuracy: 0.5625
   64/25000 [..............................] - ETA: 2:54 - loss: 6.7083 - accuracy: 0.5625
   96/25000 [..............................] - ETA: 2:16 - loss: 6.8680 - accuracy: 0.5521
  128/25000 [..............................] - ETA: 1:57 - loss: 7.4270 - accuracy: 0.5156
  160/25000 [..............................] - ETA: 1:46 - loss: 7.3791 - accuracy: 0.5188
  192/25000 [..............................] - ETA: 1:40 - loss: 7.5069 - accuracy: 0.5104
  224/25000 [..............................] - ETA: 1:35 - loss: 7.4613 - accuracy: 0.5134
  256/25000 [..............................] - ETA: 1:30 - loss: 7.4869 - accuracy: 0.5117
  288/25000 [..............................] - ETA: 1:27 - loss: 7.3472 - accuracy: 0.5208
  320/25000 [..............................] - ETA: 1:24 - loss: 7.4750 - accuracy: 0.5125
  352/25000 [..............................] - ETA: 1:21 - loss: 7.3617 - accuracy: 0.5199
  384/25000 [..............................] - ETA: 1:19 - loss: 7.3871 - accuracy: 0.5182
  416/25000 [..............................] - ETA: 1:18 - loss: 7.5192 - accuracy: 0.5096
  448/25000 [..............................] - ETA: 1:16 - loss: 7.4955 - accuracy: 0.5112
  480/25000 [..............................] - ETA: 1:15 - loss: 7.5388 - accuracy: 0.5083
  512/25000 [..............................] - ETA: 1:15 - loss: 7.6666 - accuracy: 0.5000
  544/25000 [..............................] - ETA: 1:14 - loss: 7.5257 - accuracy: 0.5092
  576/25000 [..............................] - ETA: 1:13 - loss: 7.4537 - accuracy: 0.5139
  608/25000 [..............................] - ETA: 1:13 - loss: 7.3892 - accuracy: 0.5181
  640/25000 [..............................] - ETA: 1:12 - loss: 7.5229 - accuracy: 0.5094
  672/25000 [..............................] - ETA: 1:11 - loss: 7.6438 - accuracy: 0.5015
  704/25000 [..............................] - ETA: 1:11 - loss: 7.5795 - accuracy: 0.5057
  736/25000 [..............................] - ETA: 1:10 - loss: 7.6250 - accuracy: 0.5027
  768/25000 [..............................] - ETA: 1:09 - loss: 7.6866 - accuracy: 0.4987
  800/25000 [..............................] - ETA: 1:09 - loss: 7.5900 - accuracy: 0.5050
  832/25000 [..............................] - ETA: 1:08 - loss: 7.5192 - accuracy: 0.5096
  864/25000 [>.............................] - ETA: 1:08 - loss: 7.5069 - accuracy: 0.5104
  896/25000 [>.............................] - ETA: 1:07 - loss: 7.5297 - accuracy: 0.5089
  928/25000 [>.............................] - ETA: 1:07 - loss: 7.6005 - accuracy: 0.5043
  960/25000 [>.............................] - ETA: 1:07 - loss: 7.6347 - accuracy: 0.5021
  992/25000 [>.............................] - ETA: 1:07 - loss: 7.6048 - accuracy: 0.5040
 1024/25000 [>.............................] - ETA: 1:06 - loss: 7.6217 - accuracy: 0.5029
 1056/25000 [>.............................] - ETA: 1:06 - loss: 7.5940 - accuracy: 0.5047
 1088/25000 [>.............................] - ETA: 1:06 - loss: 7.6102 - accuracy: 0.5037
 1120/25000 [>.............................] - ETA: 1:06 - loss: 7.5845 - accuracy: 0.5054
 1152/25000 [>.............................] - ETA: 1:05 - loss: 7.6267 - accuracy: 0.5026
 1184/25000 [>.............................] - ETA: 1:05 - loss: 7.6407 - accuracy: 0.5017
 1216/25000 [>.............................] - ETA: 1:05 - loss: 7.6162 - accuracy: 0.5033
 1248/25000 [>.............................] - ETA: 1:05 - loss: 7.6420 - accuracy: 0.5016
 1280/25000 [>.............................] - ETA: 1:05 - loss: 7.6906 - accuracy: 0.4984
 1312/25000 [>.............................] - ETA: 1:04 - loss: 7.7017 - accuracy: 0.4977
 1344/25000 [>.............................] - ETA: 1:04 - loss: 7.7123 - accuracy: 0.4970
 1376/25000 [>.............................] - ETA: 1:04 - loss: 7.7669 - accuracy: 0.4935
 1408/25000 [>.............................] - ETA: 1:04 - loss: 7.8191 - accuracy: 0.4901
 1440/25000 [>.............................] - ETA: 1:04 - loss: 7.8263 - accuracy: 0.4896
 1472/25000 [>.............................] - ETA: 1:03 - loss: 7.8125 - accuracy: 0.4905
 1504/25000 [>.............................] - ETA: 1:03 - loss: 7.8093 - accuracy: 0.4907
 1536/25000 [>.............................] - ETA: 1:03 - loss: 7.8463 - accuracy: 0.4883
 1568/25000 [>.............................] - ETA: 1:03 - loss: 7.8524 - accuracy: 0.4879
 1600/25000 [>.............................] - ETA: 1:03 - loss: 7.8295 - accuracy: 0.4894
 1632/25000 [>.............................] - ETA: 1:02 - loss: 7.8076 - accuracy: 0.4908
 1664/25000 [>.............................] - ETA: 1:02 - loss: 7.7956 - accuracy: 0.4916
 1696/25000 [=>............................] - ETA: 1:02 - loss: 7.8474 - accuracy: 0.4882
 1728/25000 [=>............................] - ETA: 1:02 - loss: 7.8441 - accuracy: 0.4884
 1760/25000 [=>............................] - ETA: 1:02 - loss: 7.8409 - accuracy: 0.4886
 1792/25000 [=>............................] - ETA: 1:02 - loss: 7.8891 - accuracy: 0.4855
 1824/25000 [=>............................] - ETA: 1:02 - loss: 7.8936 - accuracy: 0.4852
 1856/25000 [=>............................] - ETA: 1:01 - loss: 7.8732 - accuracy: 0.4865
 1888/25000 [=>............................] - ETA: 1:01 - loss: 7.8453 - accuracy: 0.4883
 1920/25000 [=>............................] - ETA: 1:01 - loss: 7.8184 - accuracy: 0.4901
 1952/25000 [=>............................] - ETA: 1:01 - loss: 7.8237 - accuracy: 0.4898
 1984/25000 [=>............................] - ETA: 1:01 - loss: 7.7748 - accuracy: 0.4929
 2016/25000 [=>............................] - ETA: 1:01 - loss: 7.7655 - accuracy: 0.4936
 2048/25000 [=>............................] - ETA: 1:01 - loss: 7.7714 - accuracy: 0.4932
 2080/25000 [=>............................] - ETA: 1:01 - loss: 7.7698 - accuracy: 0.4933
 2112/25000 [=>............................] - ETA: 1:01 - loss: 7.8046 - accuracy: 0.4910
 2144/25000 [=>............................] - ETA: 1:00 - loss: 7.8097 - accuracy: 0.4907
 2176/25000 [=>............................] - ETA: 1:00 - loss: 7.8005 - accuracy: 0.4913
 2208/25000 [=>............................] - ETA: 1:00 - loss: 7.7430 - accuracy: 0.4950
 2240/25000 [=>............................] - ETA: 1:00 - loss: 7.7145 - accuracy: 0.4969
 2272/25000 [=>............................] - ETA: 1:00 - loss: 7.7071 - accuracy: 0.4974
 2304/25000 [=>............................] - ETA: 1:00 - loss: 7.7065 - accuracy: 0.4974
 2336/25000 [=>............................] - ETA: 1:00 - loss: 7.7126 - accuracy: 0.4970
 2368/25000 [=>............................] - ETA: 1:00 - loss: 7.7055 - accuracy: 0.4975
 2400/25000 [=>............................] - ETA: 59s - loss: 7.6794 - accuracy: 0.4992 
 2432/25000 [=>............................] - ETA: 59s - loss: 7.6729 - accuracy: 0.4996
 2464/25000 [=>............................] - ETA: 59s - loss: 7.6915 - accuracy: 0.4984
 2496/25000 [=>............................] - ETA: 59s - loss: 7.6912 - accuracy: 0.4984
 2528/25000 [==>...........................] - ETA: 59s - loss: 7.7030 - accuracy: 0.4976
 2560/25000 [==>...........................] - ETA: 59s - loss: 7.7026 - accuracy: 0.4977
 2592/25000 [==>...........................] - ETA: 59s - loss: 7.6962 - accuracy: 0.4981
 2624/25000 [==>...........................] - ETA: 59s - loss: 7.6841 - accuracy: 0.4989
 2656/25000 [==>...........................] - ETA: 59s - loss: 7.6608 - accuracy: 0.5004
 2688/25000 [==>...........................] - ETA: 58s - loss: 7.6723 - accuracy: 0.4996
 2720/25000 [==>...........................] - ETA: 58s - loss: 7.6779 - accuracy: 0.4993
 2752/25000 [==>...........................] - ETA: 58s - loss: 7.6833 - accuracy: 0.4989
 2784/25000 [==>...........................] - ETA: 58s - loss: 7.6611 - accuracy: 0.5004
 2816/25000 [==>...........................] - ETA: 58s - loss: 7.6557 - accuracy: 0.5007
 2848/25000 [==>...........................] - ETA: 58s - loss: 7.6612 - accuracy: 0.5004
 2880/25000 [==>...........................] - ETA: 58s - loss: 7.6613 - accuracy: 0.5003
 2912/25000 [==>...........................] - ETA: 58s - loss: 7.6561 - accuracy: 0.5007
 2944/25000 [==>...........................] - ETA: 58s - loss: 7.6510 - accuracy: 0.5010
 2976/25000 [==>...........................] - ETA: 57s - loss: 7.6512 - accuracy: 0.5010
 3008/25000 [==>...........................] - ETA: 57s - loss: 7.6819 - accuracy: 0.4990
 3040/25000 [==>...........................] - ETA: 57s - loss: 7.6969 - accuracy: 0.4980
 3072/25000 [==>...........................] - ETA: 57s - loss: 7.7016 - accuracy: 0.4977
 3104/25000 [==>...........................] - ETA: 57s - loss: 7.6617 - accuracy: 0.5003
 3136/25000 [==>...........................] - ETA: 57s - loss: 7.6764 - accuracy: 0.4994
 3168/25000 [==>...........................] - ETA: 57s - loss: 7.6618 - accuracy: 0.5003
 3200/25000 [==>...........................] - ETA: 57s - loss: 7.6331 - accuracy: 0.5022
 3232/25000 [==>...........................] - ETA: 57s - loss: 7.6287 - accuracy: 0.5025
 3264/25000 [==>...........................] - ETA: 57s - loss: 7.6196 - accuracy: 0.5031
 3296/25000 [==>...........................] - ETA: 56s - loss: 7.6248 - accuracy: 0.5027
 3328/25000 [==>...........................] - ETA: 56s - loss: 7.6344 - accuracy: 0.5021
 3360/25000 [===>..........................] - ETA: 56s - loss: 7.6255 - accuracy: 0.5027
 3392/25000 [===>..........................] - ETA: 56s - loss: 7.6124 - accuracy: 0.5035
 3424/25000 [===>..........................] - ETA: 56s - loss: 7.6218 - accuracy: 0.5029
 3456/25000 [===>..........................] - ETA: 56s - loss: 7.6223 - accuracy: 0.5029
 3488/25000 [===>..........................] - ETA: 56s - loss: 7.6139 - accuracy: 0.5034
 3520/25000 [===>..........................] - ETA: 56s - loss: 7.6187 - accuracy: 0.5031
 3552/25000 [===>..........................] - ETA: 56s - loss: 7.6235 - accuracy: 0.5028
 3584/25000 [===>..........................] - ETA: 55s - loss: 7.6238 - accuracy: 0.5028
 3616/25000 [===>..........................] - ETA: 55s - loss: 7.6412 - accuracy: 0.5017
 3648/25000 [===>..........................] - ETA: 55s - loss: 7.6330 - accuracy: 0.5022
 3680/25000 [===>..........................] - ETA: 55s - loss: 7.6416 - accuracy: 0.5016
 3712/25000 [===>..........................] - ETA: 55s - loss: 7.6501 - accuracy: 0.5011
 3744/25000 [===>..........................] - ETA: 55s - loss: 7.6502 - accuracy: 0.5011
 3776/25000 [===>..........................] - ETA: 55s - loss: 7.6341 - accuracy: 0.5021
 3808/25000 [===>..........................] - ETA: 55s - loss: 7.6425 - accuracy: 0.5016
 3840/25000 [===>..........................] - ETA: 55s - loss: 7.6267 - accuracy: 0.5026
 3872/25000 [===>..........................] - ETA: 55s - loss: 7.6270 - accuracy: 0.5026
 3904/25000 [===>..........................] - ETA: 54s - loss: 7.6156 - accuracy: 0.5033
 3936/25000 [===>..........................] - ETA: 54s - loss: 7.6277 - accuracy: 0.5025
 3968/25000 [===>..........................] - ETA: 54s - loss: 7.6125 - accuracy: 0.5035
 4000/25000 [===>..........................] - ETA: 54s - loss: 7.6206 - accuracy: 0.5030
 4032/25000 [===>..........................] - ETA: 54s - loss: 7.6324 - accuracy: 0.5022
 4064/25000 [===>..........................] - ETA: 54s - loss: 7.6289 - accuracy: 0.5025
 4096/25000 [===>..........................] - ETA: 54s - loss: 7.6442 - accuracy: 0.5015
 4128/25000 [===>..........................] - ETA: 54s - loss: 7.6518 - accuracy: 0.5010
 4160/25000 [===>..........................] - ETA: 54s - loss: 7.6482 - accuracy: 0.5012
 4192/25000 [====>.........................] - ETA: 54s - loss: 7.6520 - accuracy: 0.5010
 4224/25000 [====>.........................] - ETA: 54s - loss: 7.6666 - accuracy: 0.5000
 4256/25000 [====>.........................] - ETA: 53s - loss: 7.6738 - accuracy: 0.4995
 4288/25000 [====>.........................] - ETA: 53s - loss: 7.6523 - accuracy: 0.5009
 4320/25000 [====>.........................] - ETA: 53s - loss: 7.6560 - accuracy: 0.5007
 4352/25000 [====>.........................] - ETA: 53s - loss: 7.6666 - accuracy: 0.5000
 4384/25000 [====>.........................] - ETA: 53s - loss: 7.6701 - accuracy: 0.4998
 4416/25000 [====>.........................] - ETA: 53s - loss: 7.6527 - accuracy: 0.5009
 4448/25000 [====>.........................] - ETA: 53s - loss: 7.6735 - accuracy: 0.4996
 4480/25000 [====>.........................] - ETA: 53s - loss: 7.6700 - accuracy: 0.4998
 4512/25000 [====>.........................] - ETA: 53s - loss: 7.6734 - accuracy: 0.4996
 4544/25000 [====>.........................] - ETA: 53s - loss: 7.6801 - accuracy: 0.4991
 4576/25000 [====>.........................] - ETA: 53s - loss: 7.6968 - accuracy: 0.4980
 4608/25000 [====>.........................] - ETA: 52s - loss: 7.6799 - accuracy: 0.4991
 4640/25000 [====>.........................] - ETA: 52s - loss: 7.6798 - accuracy: 0.4991
 4672/25000 [====>.........................] - ETA: 52s - loss: 7.6699 - accuracy: 0.4998
 4704/25000 [====>.........................] - ETA: 52s - loss: 7.6601 - accuracy: 0.5004
 4736/25000 [====>.........................] - ETA: 52s - loss: 7.6666 - accuracy: 0.5000
 4768/25000 [====>.........................] - ETA: 52s - loss: 7.6666 - accuracy: 0.5000
 4800/25000 [====>.........................] - ETA: 52s - loss: 7.6666 - accuracy: 0.5000
 4832/25000 [====>.........................] - ETA: 52s - loss: 7.6666 - accuracy: 0.5000
 4864/25000 [====>.........................] - ETA: 52s - loss: 7.6572 - accuracy: 0.5006
 4896/25000 [====>.........................] - ETA: 51s - loss: 7.6478 - accuracy: 0.5012
 4928/25000 [====>.........................] - ETA: 51s - loss: 7.6480 - accuracy: 0.5012
 4960/25000 [====>.........................] - ETA: 51s - loss: 7.6419 - accuracy: 0.5016
 4992/25000 [====>.........................] - ETA: 51s - loss: 7.6482 - accuracy: 0.5012
 5024/25000 [=====>........................] - ETA: 51s - loss: 7.6422 - accuracy: 0.5016
 5056/25000 [=====>........................] - ETA: 51s - loss: 7.6484 - accuracy: 0.5012
 5088/25000 [=====>........................] - ETA: 51s - loss: 7.6516 - accuracy: 0.5010
 5120/25000 [=====>........................] - ETA: 51s - loss: 7.6576 - accuracy: 0.5006
 5152/25000 [=====>........................] - ETA: 51s - loss: 7.6666 - accuracy: 0.5000
 5184/25000 [=====>........................] - ETA: 51s - loss: 7.6666 - accuracy: 0.5000
 5216/25000 [=====>........................] - ETA: 51s - loss: 7.6754 - accuracy: 0.4994
 5248/25000 [=====>........................] - ETA: 50s - loss: 7.6812 - accuracy: 0.4990
 5280/25000 [=====>........................] - ETA: 50s - loss: 7.6869 - accuracy: 0.4987
 5312/25000 [=====>........................] - ETA: 50s - loss: 7.6926 - accuracy: 0.4983
 5344/25000 [=====>........................] - ETA: 50s - loss: 7.6982 - accuracy: 0.4979
 5376/25000 [=====>........................] - ETA: 50s - loss: 7.6894 - accuracy: 0.4985
 5408/25000 [=====>........................] - ETA: 50s - loss: 7.7006 - accuracy: 0.4978
 5440/25000 [=====>........................] - ETA: 50s - loss: 7.6976 - accuracy: 0.4980
 5472/25000 [=====>........................] - ETA: 50s - loss: 7.7115 - accuracy: 0.4971
 5504/25000 [=====>........................] - ETA: 50s - loss: 7.7196 - accuracy: 0.4965
 5536/25000 [=====>........................] - ETA: 50s - loss: 7.7220 - accuracy: 0.4964
 5568/25000 [=====>........................] - ETA: 50s - loss: 7.7244 - accuracy: 0.4962
 5600/25000 [=====>........................] - ETA: 49s - loss: 7.7214 - accuracy: 0.4964
 5632/25000 [=====>........................] - ETA: 49s - loss: 7.7265 - accuracy: 0.4961
 5664/25000 [=====>........................] - ETA: 49s - loss: 7.7235 - accuracy: 0.4963
 5696/25000 [=====>........................] - ETA: 49s - loss: 7.7258 - accuracy: 0.4961
 5728/25000 [=====>........................] - ETA: 49s - loss: 7.7255 - accuracy: 0.4962
 5760/25000 [=====>........................] - ETA: 49s - loss: 7.7252 - accuracy: 0.4962
 5792/25000 [=====>........................] - ETA: 49s - loss: 7.7275 - accuracy: 0.4960
 5824/25000 [=====>........................] - ETA: 49s - loss: 7.7298 - accuracy: 0.4959
 5856/25000 [======>.......................] - ETA: 49s - loss: 7.7138 - accuracy: 0.4969
 5888/25000 [======>.......................] - ETA: 49s - loss: 7.7187 - accuracy: 0.4966
 5920/25000 [======>.......................] - ETA: 48s - loss: 7.7158 - accuracy: 0.4968
 5952/25000 [======>.......................] - ETA: 48s - loss: 7.7027 - accuracy: 0.4976
 5984/25000 [======>.......................] - ETA: 48s - loss: 7.6999 - accuracy: 0.4978
 6016/25000 [======>.......................] - ETA: 48s - loss: 7.6870 - accuracy: 0.4987
 6048/25000 [======>.......................] - ETA: 48s - loss: 7.6869 - accuracy: 0.4987
 6080/25000 [======>.......................] - ETA: 48s - loss: 7.6818 - accuracy: 0.4990
 6112/25000 [======>.......................] - ETA: 48s - loss: 7.6767 - accuracy: 0.4993
 6144/25000 [======>.......................] - ETA: 48s - loss: 7.6691 - accuracy: 0.4998
 6176/25000 [======>.......................] - ETA: 48s - loss: 7.6666 - accuracy: 0.5000
 6208/25000 [======>.......................] - ETA: 48s - loss: 7.6617 - accuracy: 0.5003
 6240/25000 [======>.......................] - ETA: 48s - loss: 7.6519 - accuracy: 0.5010
 6272/25000 [======>.......................] - ETA: 48s - loss: 7.6593 - accuracy: 0.5005
 6304/25000 [======>.......................] - ETA: 47s - loss: 7.6642 - accuracy: 0.5002
 6336/25000 [======>.......................] - ETA: 47s - loss: 7.6787 - accuracy: 0.4992
 6368/25000 [======>.......................] - ETA: 47s - loss: 7.6787 - accuracy: 0.4992
 6400/25000 [======>.......................] - ETA: 47s - loss: 7.6762 - accuracy: 0.4994
 6432/25000 [======>.......................] - ETA: 47s - loss: 7.6642 - accuracy: 0.5002
 6464/25000 [======>.......................] - ETA: 47s - loss: 7.6666 - accuracy: 0.5000
 6496/25000 [======>.......................] - ETA: 47s - loss: 7.6595 - accuracy: 0.5005
 6528/25000 [======>.......................] - ETA: 47s - loss: 7.6572 - accuracy: 0.5006
 6560/25000 [======>.......................] - ETA: 47s - loss: 7.6596 - accuracy: 0.5005
 6592/25000 [======>.......................] - ETA: 47s - loss: 7.6689 - accuracy: 0.4998
 6624/25000 [======>.......................] - ETA: 47s - loss: 7.6689 - accuracy: 0.4998
 6656/25000 [======>.......................] - ETA: 46s - loss: 7.6781 - accuracy: 0.4992
 6688/25000 [=======>......................] - ETA: 46s - loss: 7.6758 - accuracy: 0.4994
 6720/25000 [=======>......................] - ETA: 46s - loss: 7.6849 - accuracy: 0.4988
 6752/25000 [=======>......................] - ETA: 46s - loss: 7.6825 - accuracy: 0.4990
 6784/25000 [=======>......................] - ETA: 46s - loss: 7.6802 - accuracy: 0.4991
 6816/25000 [=======>......................] - ETA: 46s - loss: 7.6734 - accuracy: 0.4996
 6848/25000 [=======>......................] - ETA: 46s - loss: 7.6733 - accuracy: 0.4996
 6880/25000 [=======>......................] - ETA: 46s - loss: 7.6800 - accuracy: 0.4991
 6912/25000 [=======>......................] - ETA: 46s - loss: 7.6777 - accuracy: 0.4993
 6944/25000 [=======>......................] - ETA: 46s - loss: 7.6865 - accuracy: 0.4987
 6976/25000 [=======>......................] - ETA: 46s - loss: 7.6864 - accuracy: 0.4987
 7008/25000 [=======>......................] - ETA: 46s - loss: 7.6797 - accuracy: 0.4991
 7040/25000 [=======>......................] - ETA: 45s - loss: 7.6797 - accuracy: 0.4991
 7072/25000 [=======>......................] - ETA: 45s - loss: 7.6710 - accuracy: 0.4997
 7104/25000 [=======>......................] - ETA: 45s - loss: 7.6774 - accuracy: 0.4993
 7136/25000 [=======>......................] - ETA: 45s - loss: 7.6731 - accuracy: 0.4996
 7168/25000 [=======>......................] - ETA: 45s - loss: 7.6730 - accuracy: 0.4996
 7200/25000 [=======>......................] - ETA: 45s - loss: 7.6794 - accuracy: 0.4992
 7232/25000 [=======>......................] - ETA: 45s - loss: 7.6772 - accuracy: 0.4993
 7264/25000 [=======>......................] - ETA: 45s - loss: 7.6751 - accuracy: 0.4994
 7296/25000 [=======>......................] - ETA: 45s - loss: 7.6771 - accuracy: 0.4993
 7328/25000 [=======>......................] - ETA: 45s - loss: 7.6708 - accuracy: 0.4997
 7360/25000 [=======>......................] - ETA: 45s - loss: 7.6645 - accuracy: 0.5001
 7392/25000 [=======>......................] - ETA: 44s - loss: 7.6625 - accuracy: 0.5003
 7424/25000 [=======>......................] - ETA: 44s - loss: 7.6666 - accuracy: 0.5000
 7456/25000 [=======>......................] - ETA: 44s - loss: 7.6563 - accuracy: 0.5007
 7488/25000 [=======>......................] - ETA: 44s - loss: 7.6482 - accuracy: 0.5012
 7520/25000 [========>.....................] - ETA: 44s - loss: 7.6523 - accuracy: 0.5009
 7552/25000 [========>.....................] - ETA: 44s - loss: 7.6463 - accuracy: 0.5013
 7584/25000 [========>.....................] - ETA: 44s - loss: 7.6424 - accuracy: 0.5016
 7616/25000 [========>.....................] - ETA: 44s - loss: 7.6384 - accuracy: 0.5018
 7648/25000 [========>.....................] - ETA: 44s - loss: 7.6365 - accuracy: 0.5020
 7680/25000 [========>.....................] - ETA: 44s - loss: 7.6367 - accuracy: 0.5020
 7712/25000 [========>.....................] - ETA: 44s - loss: 7.6348 - accuracy: 0.5021
 7744/25000 [========>.....................] - ETA: 43s - loss: 7.6369 - accuracy: 0.5019
 7776/25000 [========>.....................] - ETA: 43s - loss: 7.6311 - accuracy: 0.5023
 7808/25000 [========>.....................] - ETA: 43s - loss: 7.6273 - accuracy: 0.5026
 7840/25000 [========>.....................] - ETA: 43s - loss: 7.6392 - accuracy: 0.5018
 7872/25000 [========>.....................] - ETA: 43s - loss: 7.6374 - accuracy: 0.5019
 7904/25000 [========>.....................] - ETA: 43s - loss: 7.6433 - accuracy: 0.5015
 7936/25000 [========>.....................] - ETA: 43s - loss: 7.6376 - accuracy: 0.5019
 7968/25000 [========>.....................] - ETA: 43s - loss: 7.6397 - accuracy: 0.5018
 8000/25000 [========>.....................] - ETA: 43s - loss: 7.6417 - accuracy: 0.5016
 8032/25000 [========>.....................] - ETA: 43s - loss: 7.6456 - accuracy: 0.5014
 8064/25000 [========>.....................] - ETA: 43s - loss: 7.6381 - accuracy: 0.5019
 8096/25000 [========>.....................] - ETA: 43s - loss: 7.6287 - accuracy: 0.5025
 8128/25000 [========>.....................] - ETA: 43s - loss: 7.6364 - accuracy: 0.5020
 8160/25000 [========>.....................] - ETA: 42s - loss: 7.6290 - accuracy: 0.5025
 8192/25000 [========>.....................] - ETA: 42s - loss: 7.6292 - accuracy: 0.5024
 8224/25000 [========>.....................] - ETA: 42s - loss: 7.6331 - accuracy: 0.5022
 8256/25000 [========>.....................] - ETA: 42s - loss: 7.6406 - accuracy: 0.5017
 8288/25000 [========>.....................] - ETA: 42s - loss: 7.6426 - accuracy: 0.5016
 8320/25000 [========>.....................] - ETA: 42s - loss: 7.6371 - accuracy: 0.5019
 8352/25000 [=========>....................] - ETA: 42s - loss: 7.6409 - accuracy: 0.5017
 8384/25000 [=========>....................] - ETA: 42s - loss: 7.6410 - accuracy: 0.5017
 8416/25000 [=========>....................] - ETA: 42s - loss: 7.6484 - accuracy: 0.5012
 8448/25000 [=========>....................] - ETA: 42s - loss: 7.6521 - accuracy: 0.5009
 8480/25000 [=========>....................] - ETA: 42s - loss: 7.6612 - accuracy: 0.5004
 8512/25000 [=========>....................] - ETA: 42s - loss: 7.6612 - accuracy: 0.5004
 8544/25000 [=========>....................] - ETA: 41s - loss: 7.6684 - accuracy: 0.4999
 8576/25000 [=========>....................] - ETA: 41s - loss: 7.6756 - accuracy: 0.4994
 8608/25000 [=========>....................] - ETA: 41s - loss: 7.6809 - accuracy: 0.4991
 8640/25000 [=========>....................] - ETA: 41s - loss: 7.6826 - accuracy: 0.4990
 8672/25000 [=========>....................] - ETA: 41s - loss: 7.6825 - accuracy: 0.4990
 8704/25000 [=========>....................] - ETA: 41s - loss: 7.6860 - accuracy: 0.4987
 8736/25000 [=========>....................] - ETA: 41s - loss: 7.6842 - accuracy: 0.4989
 8768/25000 [=========>....................] - ETA: 41s - loss: 7.6841 - accuracy: 0.4989
 8800/25000 [=========>....................] - ETA: 41s - loss: 7.6840 - accuracy: 0.4989
 8832/25000 [=========>....................] - ETA: 41s - loss: 7.6840 - accuracy: 0.4989
 8864/25000 [=========>....................] - ETA: 41s - loss: 7.6805 - accuracy: 0.4991
 8896/25000 [=========>....................] - ETA: 41s - loss: 7.6804 - accuracy: 0.4991
 8928/25000 [=========>....................] - ETA: 40s - loss: 7.6821 - accuracy: 0.4990
 8960/25000 [=========>....................] - ETA: 40s - loss: 7.6786 - accuracy: 0.4992
 8992/25000 [=========>....................] - ETA: 40s - loss: 7.6803 - accuracy: 0.4991
 9024/25000 [=========>....................] - ETA: 40s - loss: 7.6870 - accuracy: 0.4987
 9056/25000 [=========>....................] - ETA: 40s - loss: 7.6869 - accuracy: 0.4987
 9088/25000 [=========>....................] - ETA: 40s - loss: 7.6886 - accuracy: 0.4986
 9120/25000 [=========>....................] - ETA: 40s - loss: 7.6868 - accuracy: 0.4987
 9152/25000 [=========>....................] - ETA: 40s - loss: 7.6850 - accuracy: 0.4988
 9184/25000 [==========>...................] - ETA: 40s - loss: 7.6867 - accuracy: 0.4987
 9216/25000 [==========>...................] - ETA: 40s - loss: 7.6849 - accuracy: 0.4988
 9248/25000 [==========>...................] - ETA: 40s - loss: 7.6849 - accuracy: 0.4988
 9280/25000 [==========>...................] - ETA: 40s - loss: 7.6782 - accuracy: 0.4992
 9312/25000 [==========>...................] - ETA: 40s - loss: 7.6798 - accuracy: 0.4991
 9344/25000 [==========>...................] - ETA: 39s - loss: 7.6765 - accuracy: 0.4994
 9376/25000 [==========>...................] - ETA: 39s - loss: 7.6715 - accuracy: 0.4997
 9408/25000 [==========>...................] - ETA: 39s - loss: 7.6764 - accuracy: 0.4994
 9440/25000 [==========>...................] - ETA: 39s - loss: 7.6747 - accuracy: 0.4995
 9472/25000 [==========>...................] - ETA: 39s - loss: 7.6731 - accuracy: 0.4996
 9504/25000 [==========>...................] - ETA: 39s - loss: 7.6747 - accuracy: 0.4995
 9536/25000 [==========>...................] - ETA: 39s - loss: 7.6682 - accuracy: 0.4999
 9568/25000 [==========>...................] - ETA: 39s - loss: 7.6666 - accuracy: 0.5000
 9600/25000 [==========>...................] - ETA: 39s - loss: 7.6698 - accuracy: 0.4998
 9632/25000 [==========>...................] - ETA: 39s - loss: 7.6666 - accuracy: 0.5000
 9664/25000 [==========>...................] - ETA: 39s - loss: 7.6571 - accuracy: 0.5006
 9696/25000 [==========>...................] - ETA: 38s - loss: 7.6508 - accuracy: 0.5010
 9728/25000 [==========>...................] - ETA: 38s - loss: 7.6477 - accuracy: 0.5012
 9760/25000 [==========>...................] - ETA: 38s - loss: 7.6415 - accuracy: 0.5016
 9792/25000 [==========>...................] - ETA: 38s - loss: 7.6400 - accuracy: 0.5017
 9824/25000 [==========>...................] - ETA: 38s - loss: 7.6385 - accuracy: 0.5018
 9856/25000 [==========>...................] - ETA: 38s - loss: 7.6417 - accuracy: 0.5016
 9888/25000 [==========>...................] - ETA: 38s - loss: 7.6325 - accuracy: 0.5022
 9920/25000 [==========>...................] - ETA: 38s - loss: 7.6295 - accuracy: 0.5024
 9952/25000 [==========>...................] - ETA: 38s - loss: 7.6235 - accuracy: 0.5028
 9984/25000 [==========>...................] - ETA: 38s - loss: 7.6252 - accuracy: 0.5027
10016/25000 [===========>..................] - ETA: 38s - loss: 7.6268 - accuracy: 0.5026
10048/25000 [===========>..................] - ETA: 38s - loss: 7.6300 - accuracy: 0.5024
10080/25000 [===========>..................] - ETA: 37s - loss: 7.6332 - accuracy: 0.5022
10112/25000 [===========>..................] - ETA: 37s - loss: 7.6257 - accuracy: 0.5027
10144/25000 [===========>..................] - ETA: 37s - loss: 7.6258 - accuracy: 0.5027
10176/25000 [===========>..................] - ETA: 37s - loss: 7.6320 - accuracy: 0.5023
10208/25000 [===========>..................] - ETA: 37s - loss: 7.6306 - accuracy: 0.5024
10240/25000 [===========>..................] - ETA: 37s - loss: 7.6277 - accuracy: 0.5025
10272/25000 [===========>..................] - ETA: 37s - loss: 7.6218 - accuracy: 0.5029
10304/25000 [===========>..................] - ETA: 37s - loss: 7.6160 - accuracy: 0.5033
10336/25000 [===========>..................] - ETA: 37s - loss: 7.6177 - accuracy: 0.5032
10368/25000 [===========>..................] - ETA: 37s - loss: 7.6193 - accuracy: 0.5031
10400/25000 [===========>..................] - ETA: 37s - loss: 7.6224 - accuracy: 0.5029
10432/25000 [===========>..................] - ETA: 37s - loss: 7.6211 - accuracy: 0.5030
10464/25000 [===========>..................] - ETA: 36s - loss: 7.6212 - accuracy: 0.5030
10496/25000 [===========>..................] - ETA: 36s - loss: 7.6272 - accuracy: 0.5026
10528/25000 [===========>..................] - ETA: 36s - loss: 7.6302 - accuracy: 0.5024
10560/25000 [===========>..................] - ETA: 36s - loss: 7.6274 - accuracy: 0.5026
10592/25000 [===========>..................] - ETA: 36s - loss: 7.6203 - accuracy: 0.5030
10624/25000 [===========>..................] - ETA: 36s - loss: 7.6190 - accuracy: 0.5031
10656/25000 [===========>..................] - ETA: 36s - loss: 7.6220 - accuracy: 0.5029
10688/25000 [===========>..................] - ETA: 36s - loss: 7.6150 - accuracy: 0.5034
10720/25000 [===========>..................] - ETA: 36s - loss: 7.6123 - accuracy: 0.5035
10752/25000 [===========>..................] - ETA: 36s - loss: 7.6096 - accuracy: 0.5037
10784/25000 [===========>..................] - ETA: 36s - loss: 7.6097 - accuracy: 0.5037
10816/25000 [===========>..................] - ETA: 36s - loss: 7.6057 - accuracy: 0.5040
10848/25000 [============>.................] - ETA: 36s - loss: 7.6058 - accuracy: 0.5040
10880/25000 [============>.................] - ETA: 35s - loss: 7.6074 - accuracy: 0.5039
10912/25000 [============>.................] - ETA: 35s - loss: 7.5978 - accuracy: 0.5045
10944/25000 [============>.................] - ETA: 35s - loss: 7.5994 - accuracy: 0.5044
10976/25000 [============>.................] - ETA: 35s - loss: 7.5982 - accuracy: 0.5045
11008/25000 [============>.................] - ETA: 35s - loss: 7.6039 - accuracy: 0.5041
11040/25000 [============>.................] - ETA: 35s - loss: 7.6055 - accuracy: 0.5040
11072/25000 [============>.................] - ETA: 35s - loss: 7.6071 - accuracy: 0.5039
11104/25000 [============>.................] - ETA: 35s - loss: 7.6072 - accuracy: 0.5039
11136/25000 [============>.................] - ETA: 35s - loss: 7.5992 - accuracy: 0.5044
11168/25000 [============>.................] - ETA: 35s - loss: 7.6021 - accuracy: 0.5042
11200/25000 [============>.................] - ETA: 35s - loss: 7.5982 - accuracy: 0.5045
11232/25000 [============>.................] - ETA: 35s - loss: 7.5984 - accuracy: 0.5045
11264/25000 [============>.................] - ETA: 34s - loss: 7.5999 - accuracy: 0.5044
11296/25000 [============>.................] - ETA: 34s - loss: 7.5960 - accuracy: 0.5046
11328/25000 [============>.................] - ETA: 34s - loss: 7.5881 - accuracy: 0.5051
11360/25000 [============>.................] - ETA: 34s - loss: 7.5883 - accuracy: 0.5051
11392/25000 [============>.................] - ETA: 34s - loss: 7.5764 - accuracy: 0.5059
11424/25000 [============>.................] - ETA: 34s - loss: 7.5821 - accuracy: 0.5055
11456/25000 [============>.................] - ETA: 34s - loss: 7.5877 - accuracy: 0.5052
11488/25000 [============>.................] - ETA: 34s - loss: 7.5852 - accuracy: 0.5053
11520/25000 [============>.................] - ETA: 34s - loss: 7.5841 - accuracy: 0.5054
11552/25000 [============>.................] - ETA: 34s - loss: 7.5830 - accuracy: 0.5055
11584/25000 [============>.................] - ETA: 34s - loss: 7.5846 - accuracy: 0.5054
11616/25000 [============>.................] - ETA: 33s - loss: 7.5874 - accuracy: 0.5052
11648/25000 [============>.................] - ETA: 33s - loss: 7.5890 - accuracy: 0.5051
11680/25000 [=============>................] - ETA: 33s - loss: 7.5931 - accuracy: 0.5048
11712/25000 [=============>................] - ETA: 33s - loss: 7.5907 - accuracy: 0.5050
11744/25000 [=============>................] - ETA: 33s - loss: 7.5948 - accuracy: 0.5047
11776/25000 [=============>................] - ETA: 33s - loss: 7.6028 - accuracy: 0.5042
11808/25000 [=============>................] - ETA: 33s - loss: 7.6043 - accuracy: 0.5041
11840/25000 [=============>................] - ETA: 33s - loss: 7.6045 - accuracy: 0.5041
11872/25000 [=============>................] - ETA: 33s - loss: 7.6124 - accuracy: 0.5035
11904/25000 [=============>................] - ETA: 33s - loss: 7.6125 - accuracy: 0.5035
11936/25000 [=============>................] - ETA: 33s - loss: 7.6101 - accuracy: 0.5037
11968/25000 [=============>................] - ETA: 33s - loss: 7.6128 - accuracy: 0.5035
12000/25000 [=============>................] - ETA: 33s - loss: 7.6142 - accuracy: 0.5034
12032/25000 [=============>................] - ETA: 32s - loss: 7.6131 - accuracy: 0.5035
12064/25000 [=============>................] - ETA: 32s - loss: 7.6120 - accuracy: 0.5036
12096/25000 [=============>................] - ETA: 32s - loss: 7.6096 - accuracy: 0.5037
12128/25000 [=============>................] - ETA: 32s - loss: 7.6135 - accuracy: 0.5035
12160/25000 [=============>................] - ETA: 32s - loss: 7.6174 - accuracy: 0.5032
12192/25000 [=============>................] - ETA: 32s - loss: 7.6138 - accuracy: 0.5034
12224/25000 [=============>................] - ETA: 32s - loss: 7.6127 - accuracy: 0.5035
12256/25000 [=============>................] - ETA: 32s - loss: 7.6191 - accuracy: 0.5031
12288/25000 [=============>................] - ETA: 32s - loss: 7.6167 - accuracy: 0.5033
12320/25000 [=============>................] - ETA: 32s - loss: 7.6181 - accuracy: 0.5032
12352/25000 [=============>................] - ETA: 32s - loss: 7.6157 - accuracy: 0.5033
12384/25000 [=============>................] - ETA: 32s - loss: 7.6109 - accuracy: 0.5036
12416/25000 [=============>................] - ETA: 31s - loss: 7.6172 - accuracy: 0.5032
12448/25000 [=============>................] - ETA: 31s - loss: 7.6161 - accuracy: 0.5033
12480/25000 [=============>................] - ETA: 31s - loss: 7.6138 - accuracy: 0.5034
12512/25000 [==============>...............] - ETA: 31s - loss: 7.6066 - accuracy: 0.5039
12544/25000 [==============>...............] - ETA: 31s - loss: 7.6055 - accuracy: 0.5040
12576/25000 [==============>...............] - ETA: 31s - loss: 7.6069 - accuracy: 0.5039
12608/25000 [==============>...............] - ETA: 31s - loss: 7.6022 - accuracy: 0.5042
12640/25000 [==============>...............] - ETA: 31s - loss: 7.5999 - accuracy: 0.5044
12672/25000 [==============>...............] - ETA: 31s - loss: 7.5940 - accuracy: 0.5047
12704/25000 [==============>...............] - ETA: 31s - loss: 7.5858 - accuracy: 0.5053
12736/25000 [==============>...............] - ETA: 31s - loss: 7.5896 - accuracy: 0.5050
12768/25000 [==============>...............] - ETA: 31s - loss: 7.5886 - accuracy: 0.5051
12800/25000 [==============>...............] - ETA: 30s - loss: 7.5852 - accuracy: 0.5053
12832/25000 [==============>...............] - ETA: 30s - loss: 7.5866 - accuracy: 0.5052
12864/25000 [==============>...............] - ETA: 30s - loss: 7.5891 - accuracy: 0.5051
12896/25000 [==============>...............] - ETA: 30s - loss: 7.5905 - accuracy: 0.5050
12928/25000 [==============>...............] - ETA: 30s - loss: 7.5919 - accuracy: 0.5049
12960/25000 [==============>...............] - ETA: 30s - loss: 7.5968 - accuracy: 0.5046
12992/25000 [==============>...............] - ETA: 30s - loss: 7.5970 - accuracy: 0.5045
13024/25000 [==============>...............] - ETA: 30s - loss: 7.5995 - accuracy: 0.5044
13056/25000 [==============>...............] - ETA: 30s - loss: 7.5985 - accuracy: 0.5044
13088/25000 [==============>...............] - ETA: 30s - loss: 7.5975 - accuracy: 0.5045
13120/25000 [==============>...............] - ETA: 30s - loss: 7.5930 - accuracy: 0.5048
13152/25000 [==============>...............] - ETA: 30s - loss: 7.5897 - accuracy: 0.5050
13184/25000 [==============>...............] - ETA: 29s - loss: 7.5899 - accuracy: 0.5050
13216/25000 [==============>...............] - ETA: 29s - loss: 7.5842 - accuracy: 0.5054
13248/25000 [==============>...............] - ETA: 29s - loss: 7.5833 - accuracy: 0.5054
13280/25000 [==============>...............] - ETA: 29s - loss: 7.5835 - accuracy: 0.5054
13312/25000 [==============>...............] - ETA: 29s - loss: 7.5779 - accuracy: 0.5058
13344/25000 [===============>..............] - ETA: 29s - loss: 7.5804 - accuracy: 0.5056
13376/25000 [===============>..............] - ETA: 29s - loss: 7.5795 - accuracy: 0.5057
13408/25000 [===============>..............] - ETA: 29s - loss: 7.5809 - accuracy: 0.5056
13440/25000 [===============>..............] - ETA: 29s - loss: 7.5845 - accuracy: 0.5054
13472/25000 [===============>..............] - ETA: 29s - loss: 7.5847 - accuracy: 0.5053
13504/25000 [===============>..............] - ETA: 29s - loss: 7.5860 - accuracy: 0.5053
13536/25000 [===============>..............] - ETA: 29s - loss: 7.5896 - accuracy: 0.5050
13568/25000 [===============>..............] - ETA: 28s - loss: 7.5920 - accuracy: 0.5049
13600/25000 [===============>..............] - ETA: 28s - loss: 7.5922 - accuracy: 0.5049
13632/25000 [===============>..............] - ETA: 28s - loss: 7.5924 - accuracy: 0.5048
13664/25000 [===============>..............] - ETA: 28s - loss: 7.5926 - accuracy: 0.5048
13696/25000 [===============>..............] - ETA: 28s - loss: 7.5950 - accuracy: 0.5047
13728/25000 [===============>..............] - ETA: 28s - loss: 7.5951 - accuracy: 0.5047
13760/25000 [===============>..............] - ETA: 28s - loss: 7.5986 - accuracy: 0.5044
13792/25000 [===============>..............] - ETA: 28s - loss: 7.5966 - accuracy: 0.5046
13824/25000 [===============>..............] - ETA: 28s - loss: 7.5967 - accuracy: 0.5046
13856/25000 [===============>..............] - ETA: 28s - loss: 7.5947 - accuracy: 0.5047
13888/25000 [===============>..............] - ETA: 28s - loss: 7.5993 - accuracy: 0.5044
13920/25000 [===============>..............] - ETA: 28s - loss: 7.5983 - accuracy: 0.5045
13952/25000 [===============>..............] - ETA: 27s - loss: 7.6029 - accuracy: 0.5042
13984/25000 [===============>..............] - ETA: 27s - loss: 7.6019 - accuracy: 0.5042
14016/25000 [===============>..............] - ETA: 27s - loss: 7.6043 - accuracy: 0.5041
14048/25000 [===============>..............] - ETA: 27s - loss: 7.5989 - accuracy: 0.5044
14080/25000 [===============>..............] - ETA: 27s - loss: 7.6002 - accuracy: 0.5043
14112/25000 [===============>..............] - ETA: 27s - loss: 7.6058 - accuracy: 0.5040
14144/25000 [===============>..............] - ETA: 27s - loss: 7.6048 - accuracy: 0.5040
14176/25000 [================>.............] - ETA: 27s - loss: 7.6028 - accuracy: 0.5042
14208/25000 [================>.............] - ETA: 27s - loss: 7.6029 - accuracy: 0.5042
14240/25000 [================>.............] - ETA: 27s - loss: 7.5988 - accuracy: 0.5044
14272/25000 [================>.............] - ETA: 27s - loss: 7.6000 - accuracy: 0.5043
14304/25000 [================>.............] - ETA: 27s - loss: 7.5980 - accuracy: 0.5045
14336/25000 [================>.............] - ETA: 27s - loss: 7.5992 - accuracy: 0.5044
14368/25000 [================>.............] - ETA: 26s - loss: 7.6005 - accuracy: 0.5043
14400/25000 [================>.............] - ETA: 26s - loss: 7.6017 - accuracy: 0.5042
14432/25000 [================>.............] - ETA: 26s - loss: 7.6092 - accuracy: 0.5037
14464/25000 [================>.............] - ETA: 26s - loss: 7.6126 - accuracy: 0.5035
14496/25000 [================>.............] - ETA: 26s - loss: 7.6084 - accuracy: 0.5038
14528/25000 [================>.............] - ETA: 26s - loss: 7.6096 - accuracy: 0.5037
14560/25000 [================>.............] - ETA: 26s - loss: 7.6161 - accuracy: 0.5033
14592/25000 [================>.............] - ETA: 26s - loss: 7.6162 - accuracy: 0.5033
14624/25000 [================>.............] - ETA: 26s - loss: 7.6152 - accuracy: 0.5034
14656/25000 [================>.............] - ETA: 26s - loss: 7.6133 - accuracy: 0.5035
14688/25000 [================>.............] - ETA: 26s - loss: 7.6144 - accuracy: 0.5034
14720/25000 [================>.............] - ETA: 26s - loss: 7.6145 - accuracy: 0.5034
14752/25000 [================>.............] - ETA: 25s - loss: 7.6146 - accuracy: 0.5034
14784/25000 [================>.............] - ETA: 25s - loss: 7.6148 - accuracy: 0.5034
14816/25000 [================>.............] - ETA: 25s - loss: 7.6159 - accuracy: 0.5033
14848/25000 [================>.............] - ETA: 25s - loss: 7.6160 - accuracy: 0.5033
14880/25000 [================>.............] - ETA: 25s - loss: 7.6223 - accuracy: 0.5029
14912/25000 [================>.............] - ETA: 25s - loss: 7.6203 - accuracy: 0.5030
14944/25000 [================>.............] - ETA: 25s - loss: 7.6225 - accuracy: 0.5029
14976/25000 [================>.............] - ETA: 25s - loss: 7.6246 - accuracy: 0.5027
15008/25000 [=================>............] - ETA: 25s - loss: 7.6258 - accuracy: 0.5027
15040/25000 [=================>............] - ETA: 25s - loss: 7.6309 - accuracy: 0.5023
15072/25000 [=================>............] - ETA: 25s - loss: 7.6290 - accuracy: 0.5025
15104/25000 [=================>............] - ETA: 25s - loss: 7.6291 - accuracy: 0.5024
15136/25000 [=================>............] - ETA: 24s - loss: 7.6281 - accuracy: 0.5025
15168/25000 [=================>............] - ETA: 24s - loss: 7.6282 - accuracy: 0.5025
15200/25000 [=================>............] - ETA: 24s - loss: 7.6222 - accuracy: 0.5029
15232/25000 [=================>............] - ETA: 24s - loss: 7.6233 - accuracy: 0.5028
15264/25000 [=================>............] - ETA: 24s - loss: 7.6234 - accuracy: 0.5028
15296/25000 [=================>............] - ETA: 24s - loss: 7.6215 - accuracy: 0.5029
15328/25000 [=================>............] - ETA: 24s - loss: 7.6256 - accuracy: 0.5027
15360/25000 [=================>............] - ETA: 24s - loss: 7.6247 - accuracy: 0.5027
15392/25000 [=================>............] - ETA: 24s - loss: 7.6288 - accuracy: 0.5025
15424/25000 [=================>............] - ETA: 24s - loss: 7.6298 - accuracy: 0.5024
15456/25000 [=================>............] - ETA: 24s - loss: 7.6269 - accuracy: 0.5026
15488/25000 [=================>............] - ETA: 24s - loss: 7.6320 - accuracy: 0.5023
15520/25000 [=================>............] - ETA: 23s - loss: 7.6291 - accuracy: 0.5024
15552/25000 [=================>............] - ETA: 23s - loss: 7.6292 - accuracy: 0.5024
15584/25000 [=================>............] - ETA: 23s - loss: 7.6342 - accuracy: 0.5021
15616/25000 [=================>............] - ETA: 23s - loss: 7.6342 - accuracy: 0.5021
15648/25000 [=================>............] - ETA: 23s - loss: 7.6333 - accuracy: 0.5022
15680/25000 [=================>............] - ETA: 23s - loss: 7.6314 - accuracy: 0.5023
15712/25000 [=================>............] - ETA: 23s - loss: 7.6373 - accuracy: 0.5019
15744/25000 [=================>............] - ETA: 23s - loss: 7.6364 - accuracy: 0.5020
15776/25000 [=================>............] - ETA: 23s - loss: 7.6365 - accuracy: 0.5020
15808/25000 [=================>............] - ETA: 23s - loss: 7.6346 - accuracy: 0.5021
15840/25000 [==================>...........] - ETA: 23s - loss: 7.6308 - accuracy: 0.5023
15872/25000 [==================>...........] - ETA: 23s - loss: 7.6289 - accuracy: 0.5025
15904/25000 [==================>...........] - ETA: 22s - loss: 7.6271 - accuracy: 0.5026
15936/25000 [==================>...........] - ETA: 22s - loss: 7.6243 - accuracy: 0.5028
15968/25000 [==================>...........] - ETA: 22s - loss: 7.6253 - accuracy: 0.5027
16000/25000 [==================>...........] - ETA: 22s - loss: 7.6292 - accuracy: 0.5024
16032/25000 [==================>...........] - ETA: 22s - loss: 7.6312 - accuracy: 0.5023
16064/25000 [==================>...........] - ETA: 22s - loss: 7.6342 - accuracy: 0.5021
16096/25000 [==================>...........] - ETA: 22s - loss: 7.6361 - accuracy: 0.5020
16128/25000 [==================>...........] - ETA: 22s - loss: 7.6362 - accuracy: 0.5020
16160/25000 [==================>...........] - ETA: 22s - loss: 7.6372 - accuracy: 0.5019
16192/25000 [==================>...........] - ETA: 22s - loss: 7.6382 - accuracy: 0.5019
16224/25000 [==================>...........] - ETA: 22s - loss: 7.6411 - accuracy: 0.5017
16256/25000 [==================>...........] - ETA: 22s - loss: 7.6440 - accuracy: 0.5015
16288/25000 [==================>...........] - ETA: 22s - loss: 7.6440 - accuracy: 0.5015
16320/25000 [==================>...........] - ETA: 21s - loss: 7.6469 - accuracy: 0.5013
16352/25000 [==================>...........] - ETA: 21s - loss: 7.6460 - accuracy: 0.5013
16384/25000 [==================>...........] - ETA: 21s - loss: 7.6488 - accuracy: 0.5012
16416/25000 [==================>...........] - ETA: 21s - loss: 7.6507 - accuracy: 0.5010
16448/25000 [==================>...........] - ETA: 21s - loss: 7.6536 - accuracy: 0.5009
16480/25000 [==================>...........] - ETA: 21s - loss: 7.6536 - accuracy: 0.5008
16512/25000 [==================>...........] - ETA: 21s - loss: 7.6555 - accuracy: 0.5007
16544/25000 [==================>...........] - ETA: 21s - loss: 7.6555 - accuracy: 0.5007
16576/25000 [==================>...........] - ETA: 21s - loss: 7.6537 - accuracy: 0.5008
16608/25000 [==================>...........] - ETA: 21s - loss: 7.6537 - accuracy: 0.5008
16640/25000 [==================>...........] - ETA: 21s - loss: 7.6528 - accuracy: 0.5009
16672/25000 [===================>..........] - ETA: 21s - loss: 7.6556 - accuracy: 0.5007
16704/25000 [===================>..........] - ETA: 20s - loss: 7.6529 - accuracy: 0.5009
16736/25000 [===================>..........] - ETA: 20s - loss: 7.6538 - accuracy: 0.5008
16768/25000 [===================>..........] - ETA: 20s - loss: 7.6556 - accuracy: 0.5007
16800/25000 [===================>..........] - ETA: 20s - loss: 7.6593 - accuracy: 0.5005
16832/25000 [===================>..........] - ETA: 20s - loss: 7.6602 - accuracy: 0.5004
16864/25000 [===================>..........] - ETA: 20s - loss: 7.6575 - accuracy: 0.5006
16896/25000 [===================>..........] - ETA: 20s - loss: 7.6594 - accuracy: 0.5005
16928/25000 [===================>..........] - ETA: 20s - loss: 7.6639 - accuracy: 0.5002
16960/25000 [===================>..........] - ETA: 20s - loss: 7.6639 - accuracy: 0.5002
16992/25000 [===================>..........] - ETA: 20s - loss: 7.6657 - accuracy: 0.5001
17024/25000 [===================>..........] - ETA: 20s - loss: 7.6630 - accuracy: 0.5002
17056/25000 [===================>..........] - ETA: 20s - loss: 7.6630 - accuracy: 0.5002
17088/25000 [===================>..........] - ETA: 19s - loss: 7.6621 - accuracy: 0.5003
17120/25000 [===================>..........] - ETA: 19s - loss: 7.6595 - accuracy: 0.5005
17152/25000 [===================>..........] - ETA: 19s - loss: 7.6559 - accuracy: 0.5007
17184/25000 [===================>..........] - ETA: 19s - loss: 7.6586 - accuracy: 0.5005
17216/25000 [===================>..........] - ETA: 19s - loss: 7.6550 - accuracy: 0.5008
17248/25000 [===================>..........] - ETA: 19s - loss: 7.6542 - accuracy: 0.5008
17280/25000 [===================>..........] - ETA: 19s - loss: 7.6524 - accuracy: 0.5009
17312/25000 [===================>..........] - ETA: 19s - loss: 7.6613 - accuracy: 0.5003
17344/25000 [===================>..........] - ETA: 19s - loss: 7.6604 - accuracy: 0.5004
17376/25000 [===================>..........] - ETA: 19s - loss: 7.6569 - accuracy: 0.5006
17408/25000 [===================>..........] - ETA: 19s - loss: 7.6552 - accuracy: 0.5007
17440/25000 [===================>..........] - ETA: 19s - loss: 7.6526 - accuracy: 0.5009
17472/25000 [===================>..........] - ETA: 19s - loss: 7.6543 - accuracy: 0.5008
17504/25000 [====================>.........] - ETA: 18s - loss: 7.6517 - accuracy: 0.5010
17536/25000 [====================>.........] - ETA: 18s - loss: 7.6526 - accuracy: 0.5009
17568/25000 [====================>.........] - ETA: 18s - loss: 7.6518 - accuracy: 0.5010
17600/25000 [====================>.........] - ETA: 18s - loss: 7.6466 - accuracy: 0.5013
17632/25000 [====================>.........] - ETA: 18s - loss: 7.6449 - accuracy: 0.5014
17664/25000 [====================>.........] - ETA: 18s - loss: 7.6458 - accuracy: 0.5014
17696/25000 [====================>.........] - ETA: 18s - loss: 7.6415 - accuracy: 0.5016
17728/25000 [====================>.........] - ETA: 18s - loss: 7.6441 - accuracy: 0.5015
17760/25000 [====================>.........] - ETA: 18s - loss: 7.6407 - accuracy: 0.5017
17792/25000 [====================>.........] - ETA: 18s - loss: 7.6408 - accuracy: 0.5017
17824/25000 [====================>.........] - ETA: 18s - loss: 7.6374 - accuracy: 0.5019
17856/25000 [====================>.........] - ETA: 18s - loss: 7.6357 - accuracy: 0.5020
17888/25000 [====================>.........] - ETA: 17s - loss: 7.6409 - accuracy: 0.5017
17920/25000 [====================>.........] - ETA: 17s - loss: 7.6418 - accuracy: 0.5016
17952/25000 [====================>.........] - ETA: 17s - loss: 7.6427 - accuracy: 0.5016
17984/25000 [====================>.........] - ETA: 17s - loss: 7.6393 - accuracy: 0.5018
18016/25000 [====================>.........] - ETA: 17s - loss: 7.6385 - accuracy: 0.5018
18048/25000 [====================>.........] - ETA: 17s - loss: 7.6420 - accuracy: 0.5016
18080/25000 [====================>.........] - ETA: 17s - loss: 7.6412 - accuracy: 0.5017
18112/25000 [====================>.........] - ETA: 17s - loss: 7.6395 - accuracy: 0.5018
18144/25000 [====================>.........] - ETA: 17s - loss: 7.6438 - accuracy: 0.5015
18176/25000 [====================>.........] - ETA: 17s - loss: 7.6438 - accuracy: 0.5015
18208/25000 [====================>.........] - ETA: 17s - loss: 7.6405 - accuracy: 0.5017
18240/25000 [====================>.........] - ETA: 17s - loss: 7.6397 - accuracy: 0.5018
18272/25000 [====================>.........] - ETA: 16s - loss: 7.6389 - accuracy: 0.5018
18304/25000 [====================>.........] - ETA: 16s - loss: 7.6356 - accuracy: 0.5020
18336/25000 [=====================>........] - ETA: 16s - loss: 7.6348 - accuracy: 0.5021
18368/25000 [=====================>........] - ETA: 16s - loss: 7.6341 - accuracy: 0.5021
18400/25000 [=====================>........] - ETA: 16s - loss: 7.6383 - accuracy: 0.5018
18432/25000 [=====================>........] - ETA: 16s - loss: 7.6383 - accuracy: 0.5018
18464/25000 [=====================>........] - ETA: 16s - loss: 7.6425 - accuracy: 0.5016
18496/25000 [=====================>........] - ETA: 16s - loss: 7.6459 - accuracy: 0.5014
18528/25000 [=====================>........] - ETA: 16s - loss: 7.6468 - accuracy: 0.5013
18560/25000 [=====================>........] - ETA: 16s - loss: 7.6435 - accuracy: 0.5015
18592/25000 [=====================>........] - ETA: 16s - loss: 7.6468 - accuracy: 0.5013
18624/25000 [=====================>........] - ETA: 16s - loss: 7.6477 - accuracy: 0.5012
18656/25000 [=====================>........] - ETA: 16s - loss: 7.6469 - accuracy: 0.5013
18688/25000 [=====================>........] - ETA: 15s - loss: 7.6502 - accuracy: 0.5011
18720/25000 [=====================>........] - ETA: 15s - loss: 7.6502 - accuracy: 0.5011
18752/25000 [=====================>........] - ETA: 15s - loss: 7.6470 - accuracy: 0.5013
18784/25000 [=====================>........] - ETA: 15s - loss: 7.6470 - accuracy: 0.5013
18816/25000 [=====================>........] - ETA: 15s - loss: 7.6479 - accuracy: 0.5012
18848/25000 [=====================>........] - ETA: 15s - loss: 7.6503 - accuracy: 0.5011
18880/25000 [=====================>........] - ETA: 15s - loss: 7.6536 - accuracy: 0.5008
18912/25000 [=====================>........] - ETA: 15s - loss: 7.6536 - accuracy: 0.5008
18944/25000 [=====================>........] - ETA: 15s - loss: 7.6512 - accuracy: 0.5010
18976/25000 [=====================>........] - ETA: 15s - loss: 7.6553 - accuracy: 0.5007
19008/25000 [=====================>........] - ETA: 15s - loss: 7.6569 - accuracy: 0.5006
19040/25000 [=====================>........] - ETA: 15s - loss: 7.6602 - accuracy: 0.5004
19072/25000 [=====================>........] - ETA: 14s - loss: 7.6602 - accuracy: 0.5004
19104/25000 [=====================>........] - ETA: 14s - loss: 7.6650 - accuracy: 0.5001
19136/25000 [=====================>........] - ETA: 14s - loss: 7.6658 - accuracy: 0.5001
19168/25000 [======================>.......] - ETA: 14s - loss: 7.6626 - accuracy: 0.5003
19200/25000 [======================>.......] - ETA: 14s - loss: 7.6642 - accuracy: 0.5002
19232/25000 [======================>.......] - ETA: 14s - loss: 7.6682 - accuracy: 0.4999
19264/25000 [======================>.......] - ETA: 14s - loss: 7.6698 - accuracy: 0.4998
19296/25000 [======================>.......] - ETA: 14s - loss: 7.6746 - accuracy: 0.4995
19328/25000 [======================>.......] - ETA: 14s - loss: 7.6714 - accuracy: 0.4997
19360/25000 [======================>.......] - ETA: 14s - loss: 7.6753 - accuracy: 0.4994
19392/25000 [======================>.......] - ETA: 14s - loss: 7.6761 - accuracy: 0.4994
19424/25000 [======================>.......] - ETA: 14s - loss: 7.6785 - accuracy: 0.4992
19456/25000 [======================>.......] - ETA: 14s - loss: 7.6784 - accuracy: 0.4992
19488/25000 [======================>.......] - ETA: 13s - loss: 7.6745 - accuracy: 0.4995
19520/25000 [======================>.......] - ETA: 13s - loss: 7.6753 - accuracy: 0.4994
19552/25000 [======================>.......] - ETA: 13s - loss: 7.6776 - accuracy: 0.4993
19584/25000 [======================>.......] - ETA: 13s - loss: 7.6737 - accuracy: 0.4995
19616/25000 [======================>.......] - ETA: 13s - loss: 7.6744 - accuracy: 0.4995
19648/25000 [======================>.......] - ETA: 13s - loss: 7.6752 - accuracy: 0.4994
19680/25000 [======================>.......] - ETA: 13s - loss: 7.6744 - accuracy: 0.4995
19712/25000 [======================>.......] - ETA: 13s - loss: 7.6783 - accuracy: 0.4992
19744/25000 [======================>.......] - ETA: 13s - loss: 7.6798 - accuracy: 0.4991
19776/25000 [======================>.......] - ETA: 13s - loss: 7.6798 - accuracy: 0.4991
19808/25000 [======================>.......] - ETA: 13s - loss: 7.6782 - accuracy: 0.4992
19840/25000 [======================>.......] - ETA: 13s - loss: 7.6767 - accuracy: 0.4993
19872/25000 [======================>.......] - ETA: 12s - loss: 7.6728 - accuracy: 0.4996
19904/25000 [======================>.......] - ETA: 12s - loss: 7.6720 - accuracy: 0.4996
19936/25000 [======================>.......] - ETA: 12s - loss: 7.6728 - accuracy: 0.4996
19968/25000 [======================>.......] - ETA: 12s - loss: 7.6705 - accuracy: 0.4997
20000/25000 [=======================>......] - ETA: 12s - loss: 7.6720 - accuracy: 0.4997
20032/25000 [=======================>......] - ETA: 12s - loss: 7.6750 - accuracy: 0.4995
20064/25000 [=======================>......] - ETA: 12s - loss: 7.6743 - accuracy: 0.4995
20096/25000 [=======================>......] - ETA: 12s - loss: 7.6750 - accuracy: 0.4995
20128/25000 [=======================>......] - ETA: 12s - loss: 7.6765 - accuracy: 0.4994
20160/25000 [=======================>......] - ETA: 12s - loss: 7.6742 - accuracy: 0.4995
20192/25000 [=======================>......] - ETA: 12s - loss: 7.6757 - accuracy: 0.4994
20224/25000 [=======================>......] - ETA: 12s - loss: 7.6780 - accuracy: 0.4993
20256/25000 [=======================>......] - ETA: 11s - loss: 7.6787 - accuracy: 0.4992
20288/25000 [=======================>......] - ETA: 11s - loss: 7.6802 - accuracy: 0.4991
20320/25000 [=======================>......] - ETA: 11s - loss: 7.6794 - accuracy: 0.4992
20352/25000 [=======================>......] - ETA: 11s - loss: 7.6809 - accuracy: 0.4991
20384/25000 [=======================>......] - ETA: 11s - loss: 7.6847 - accuracy: 0.4988
20416/25000 [=======================>......] - ETA: 11s - loss: 7.6831 - accuracy: 0.4989
20448/25000 [=======================>......] - ETA: 11s - loss: 7.6809 - accuracy: 0.4991
20480/25000 [=======================>......] - ETA: 11s - loss: 7.6793 - accuracy: 0.4992
20512/25000 [=======================>......] - ETA: 11s - loss: 7.6801 - accuracy: 0.4991
20544/25000 [=======================>......] - ETA: 11s - loss: 7.6830 - accuracy: 0.4989
20576/25000 [=======================>......] - ETA: 11s - loss: 7.6823 - accuracy: 0.4990
20608/25000 [=======================>......] - ETA: 11s - loss: 7.6808 - accuracy: 0.4991
20640/25000 [=======================>......] - ETA: 11s - loss: 7.6815 - accuracy: 0.4990
20672/25000 [=======================>......] - ETA: 10s - loss: 7.6785 - accuracy: 0.4992
20704/25000 [=======================>......] - ETA: 10s - loss: 7.6800 - accuracy: 0.4991
20736/25000 [=======================>......] - ETA: 10s - loss: 7.6799 - accuracy: 0.4991
20768/25000 [=======================>......] - ETA: 10s - loss: 7.6762 - accuracy: 0.4994
20800/25000 [=======================>......] - ETA: 10s - loss: 7.6733 - accuracy: 0.4996
20832/25000 [=======================>......] - ETA: 10s - loss: 7.6703 - accuracy: 0.4998
20864/25000 [========================>.....] - ETA: 10s - loss: 7.6710 - accuracy: 0.4997
20896/25000 [========================>.....] - ETA: 10s - loss: 7.6681 - accuracy: 0.4999
20928/25000 [========================>.....] - ETA: 10s - loss: 7.6710 - accuracy: 0.4997
20960/25000 [========================>.....] - ETA: 10s - loss: 7.6732 - accuracy: 0.4996
20992/25000 [========================>.....] - ETA: 10s - loss: 7.6739 - accuracy: 0.4995
21024/25000 [========================>.....] - ETA: 10s - loss: 7.6717 - accuracy: 0.4997
21056/25000 [========================>.....] - ETA: 9s - loss: 7.6724 - accuracy: 0.4996 
21088/25000 [========================>.....] - ETA: 9s - loss: 7.6732 - accuracy: 0.4996
21120/25000 [========================>.....] - ETA: 9s - loss: 7.6688 - accuracy: 0.4999
21152/25000 [========================>.....] - ETA: 9s - loss: 7.6688 - accuracy: 0.4999
21184/25000 [========================>.....] - ETA: 9s - loss: 7.6673 - accuracy: 0.5000
21216/25000 [========================>.....] - ETA: 9s - loss: 7.6688 - accuracy: 0.4999
21248/25000 [========================>.....] - ETA: 9s - loss: 7.6681 - accuracy: 0.4999
21280/25000 [========================>.....] - ETA: 9s - loss: 7.6717 - accuracy: 0.4997
21312/25000 [========================>.....] - ETA: 9s - loss: 7.6709 - accuracy: 0.4997
21344/25000 [========================>.....] - ETA: 9s - loss: 7.6695 - accuracy: 0.4998
21376/25000 [========================>.....] - ETA: 9s - loss: 7.6673 - accuracy: 0.5000
21408/25000 [========================>.....] - ETA: 9s - loss: 7.6673 - accuracy: 0.5000
21440/25000 [========================>.....] - ETA: 9s - loss: 7.6666 - accuracy: 0.5000
21472/25000 [========================>.....] - ETA: 8s - loss: 7.6645 - accuracy: 0.5001
21504/25000 [========================>.....] - ETA: 8s - loss: 7.6638 - accuracy: 0.5002
21536/25000 [========================>.....] - ETA: 8s - loss: 7.6609 - accuracy: 0.5004
21568/25000 [========================>.....] - ETA: 8s - loss: 7.6624 - accuracy: 0.5003
21600/25000 [========================>.....] - ETA: 8s - loss: 7.6680 - accuracy: 0.4999
21632/25000 [========================>.....] - ETA: 8s - loss: 7.6680 - accuracy: 0.4999
21664/25000 [========================>.....] - ETA: 8s - loss: 7.6687 - accuracy: 0.4999
21696/25000 [=========================>....] - ETA: 8s - loss: 7.6673 - accuracy: 0.5000
21728/25000 [=========================>....] - ETA: 8s - loss: 7.6645 - accuracy: 0.5001
21760/25000 [=========================>....] - ETA: 8s - loss: 7.6596 - accuracy: 0.5005
21792/25000 [=========================>....] - ETA: 8s - loss: 7.6575 - accuracy: 0.5006
21824/25000 [=========================>....] - ETA: 8s - loss: 7.6610 - accuracy: 0.5004
21856/25000 [=========================>....] - ETA: 7s - loss: 7.6617 - accuracy: 0.5003
21888/25000 [=========================>....] - ETA: 7s - loss: 7.6617 - accuracy: 0.5003
21920/25000 [=========================>....] - ETA: 7s - loss: 7.6603 - accuracy: 0.5004
21952/25000 [=========================>....] - ETA: 7s - loss: 7.6631 - accuracy: 0.5002
21984/25000 [=========================>....] - ETA: 7s - loss: 7.6617 - accuracy: 0.5003
22016/25000 [=========================>....] - ETA: 7s - loss: 7.6617 - accuracy: 0.5003
22048/25000 [=========================>....] - ETA: 7s - loss: 7.6638 - accuracy: 0.5002
22080/25000 [=========================>....] - ETA: 7s - loss: 7.6631 - accuracy: 0.5002
22112/25000 [=========================>....] - ETA: 7s - loss: 7.6625 - accuracy: 0.5003
22144/25000 [=========================>....] - ETA: 7s - loss: 7.6618 - accuracy: 0.5003
22176/25000 [=========================>....] - ETA: 7s - loss: 7.6639 - accuracy: 0.5002
22208/25000 [=========================>....] - ETA: 7s - loss: 7.6639 - accuracy: 0.5002
22240/25000 [=========================>....] - ETA: 6s - loss: 7.6659 - accuracy: 0.5000
22272/25000 [=========================>....] - ETA: 6s - loss: 7.6625 - accuracy: 0.5003
22304/25000 [=========================>....] - ETA: 6s - loss: 7.6604 - accuracy: 0.5004
22336/25000 [=========================>....] - ETA: 6s - loss: 7.6625 - accuracy: 0.5003
22368/25000 [=========================>....] - ETA: 6s - loss: 7.6598 - accuracy: 0.5004
22400/25000 [=========================>....] - ETA: 6s - loss: 7.6632 - accuracy: 0.5002
22432/25000 [=========================>....] - ETA: 6s - loss: 7.6632 - accuracy: 0.5002
22464/25000 [=========================>....] - ETA: 6s - loss: 7.6612 - accuracy: 0.5004
22496/25000 [=========================>....] - ETA: 6s - loss: 7.6612 - accuracy: 0.5004
22528/25000 [==========================>...] - ETA: 6s - loss: 7.6625 - accuracy: 0.5003
22560/25000 [==========================>...] - ETA: 6s - loss: 7.6591 - accuracy: 0.5005
22592/25000 [==========================>...] - ETA: 6s - loss: 7.6598 - accuracy: 0.5004
22624/25000 [==========================>...] - ETA: 6s - loss: 7.6605 - accuracy: 0.5004
22656/25000 [==========================>...] - ETA: 5s - loss: 7.6612 - accuracy: 0.5004
22688/25000 [==========================>...] - ETA: 5s - loss: 7.6626 - accuracy: 0.5003
22720/25000 [==========================>...] - ETA: 5s - loss: 7.6605 - accuracy: 0.5004
22752/25000 [==========================>...] - ETA: 5s - loss: 7.6599 - accuracy: 0.5004
22784/25000 [==========================>...] - ETA: 5s - loss: 7.6606 - accuracy: 0.5004
22816/25000 [==========================>...] - ETA: 5s - loss: 7.6592 - accuracy: 0.5005
22848/25000 [==========================>...] - ETA: 5s - loss: 7.6613 - accuracy: 0.5004
22880/25000 [==========================>...] - ETA: 5s - loss: 7.6613 - accuracy: 0.5003
22912/25000 [==========================>...] - ETA: 5s - loss: 7.6619 - accuracy: 0.5003
22944/25000 [==========================>...] - ETA: 5s - loss: 7.6639 - accuracy: 0.5002
22976/25000 [==========================>...] - ETA: 5s - loss: 7.6646 - accuracy: 0.5001
23008/25000 [==========================>...] - ETA: 5s - loss: 7.6640 - accuracy: 0.5002
23040/25000 [==========================>...] - ETA: 4s - loss: 7.6666 - accuracy: 0.5000
23072/25000 [==========================>...] - ETA: 4s - loss: 7.6666 - accuracy: 0.5000
23104/25000 [==========================>...] - ETA: 4s - loss: 7.6666 - accuracy: 0.5000
23136/25000 [==========================>...] - ETA: 4s - loss: 7.6653 - accuracy: 0.5001
23168/25000 [==========================>...] - ETA: 4s - loss: 7.6640 - accuracy: 0.5002
23200/25000 [==========================>...] - ETA: 4s - loss: 7.6666 - accuracy: 0.5000
23232/25000 [==========================>...] - ETA: 4s - loss: 7.6646 - accuracy: 0.5001
23264/25000 [==========================>...] - ETA: 4s - loss: 7.6653 - accuracy: 0.5001
23296/25000 [==========================>...] - ETA: 4s - loss: 7.6679 - accuracy: 0.4999
23328/25000 [==========================>...] - ETA: 4s - loss: 7.6712 - accuracy: 0.4997
23360/25000 [===========================>..] - ETA: 4s - loss: 7.6725 - accuracy: 0.4996
23392/25000 [===========================>..] - ETA: 4s - loss: 7.6758 - accuracy: 0.4994
23424/25000 [===========================>..] - ETA: 3s - loss: 7.6758 - accuracy: 0.4994
23456/25000 [===========================>..] - ETA: 3s - loss: 7.6758 - accuracy: 0.4994
23488/25000 [===========================>..] - ETA: 3s - loss: 7.6758 - accuracy: 0.4994
23520/25000 [===========================>..] - ETA: 3s - loss: 7.6751 - accuracy: 0.4994
23552/25000 [===========================>..] - ETA: 3s - loss: 7.6725 - accuracy: 0.4996
23584/25000 [===========================>..] - ETA: 3s - loss: 7.6712 - accuracy: 0.4997
23616/25000 [===========================>..] - ETA: 3s - loss: 7.6705 - accuracy: 0.4997
23648/25000 [===========================>..] - ETA: 3s - loss: 7.6712 - accuracy: 0.4997
23680/25000 [===========================>..] - ETA: 3s - loss: 7.6686 - accuracy: 0.4999
23712/25000 [===========================>..] - ETA: 3s - loss: 7.6705 - accuracy: 0.4997
23744/25000 [===========================>..] - ETA: 3s - loss: 7.6718 - accuracy: 0.4997
23776/25000 [===========================>..] - ETA: 3s - loss: 7.6724 - accuracy: 0.4996
23808/25000 [===========================>..] - ETA: 3s - loss: 7.6686 - accuracy: 0.4999
23840/25000 [===========================>..] - ETA: 2s - loss: 7.6692 - accuracy: 0.4998
23872/25000 [===========================>..] - ETA: 2s - loss: 7.6711 - accuracy: 0.4997
23904/25000 [===========================>..] - ETA: 2s - loss: 7.6718 - accuracy: 0.4997
23936/25000 [===========================>..] - ETA: 2s - loss: 7.6737 - accuracy: 0.4995
23968/25000 [===========================>..] - ETA: 2s - loss: 7.6737 - accuracy: 0.4995
24000/25000 [===========================>..] - ETA: 2s - loss: 7.6736 - accuracy: 0.4995
24032/25000 [===========================>..] - ETA: 2s - loss: 7.6724 - accuracy: 0.4996
24064/25000 [===========================>..] - ETA: 2s - loss: 7.6717 - accuracy: 0.4997
24096/25000 [===========================>..] - ETA: 2s - loss: 7.6723 - accuracy: 0.4996
24128/25000 [===========================>..] - ETA: 2s - loss: 7.6730 - accuracy: 0.4996
24160/25000 [===========================>..] - ETA: 2s - loss: 7.6717 - accuracy: 0.4997
24192/25000 [============================>.] - ETA: 2s - loss: 7.6698 - accuracy: 0.4998
24224/25000 [============================>.] - ETA: 1s - loss: 7.6685 - accuracy: 0.4999
24256/25000 [============================>.] - ETA: 1s - loss: 7.6691 - accuracy: 0.4998
24288/25000 [============================>.] - ETA: 1s - loss: 7.6685 - accuracy: 0.4999
24320/25000 [============================>.] - ETA: 1s - loss: 7.6666 - accuracy: 0.5000
24352/25000 [============================>.] - ETA: 1s - loss: 7.6672 - accuracy: 0.5000
24384/25000 [============================>.] - ETA: 1s - loss: 7.6704 - accuracy: 0.4998
24416/25000 [============================>.] - ETA: 1s - loss: 7.6679 - accuracy: 0.4999
24448/25000 [============================>.] - ETA: 1s - loss: 7.6679 - accuracy: 0.4999
24480/25000 [============================>.] - ETA: 1s - loss: 7.6685 - accuracy: 0.4999
24512/25000 [============================>.] - ETA: 1s - loss: 7.6679 - accuracy: 0.4999
24544/25000 [============================>.] - ETA: 1s - loss: 7.6710 - accuracy: 0.4997
24576/25000 [============================>.] - ETA: 1s - loss: 7.6710 - accuracy: 0.4997
24608/25000 [============================>.] - ETA: 0s - loss: 7.6722 - accuracy: 0.4996
24640/25000 [============================>.] - ETA: 0s - loss: 7.6716 - accuracy: 0.4997
24672/25000 [============================>.] - ETA: 0s - loss: 7.6710 - accuracy: 0.4997
24704/25000 [============================>.] - ETA: 0s - loss: 7.6679 - accuracy: 0.4999
24736/25000 [============================>.] - ETA: 0s - loss: 7.6641 - accuracy: 0.5002
24768/25000 [============================>.] - ETA: 0s - loss: 7.6641 - accuracy: 0.5002
24800/25000 [============================>.] - ETA: 0s - loss: 7.6648 - accuracy: 0.5001
24832/25000 [============================>.] - ETA: 0s - loss: 7.6648 - accuracy: 0.5001
24864/25000 [============================>.] - ETA: 0s - loss: 7.6666 - accuracy: 0.5000
24896/25000 [============================>.] - ETA: 0s - loss: 7.6672 - accuracy: 0.5000
24928/25000 [============================>.] - ETA: 0s - loss: 7.6678 - accuracy: 0.4999
24960/25000 [============================>.] - ETA: 0s - loss: 7.6685 - accuracy: 0.4999
24992/25000 [============================>.] - ETA: 0s - loss: 7.6666 - accuracy: 0.5000
25000/25000 [==============================] - 74s 3ms/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000
Loading data...
Using TensorFlow backend.





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//sklearn_titanic_randomForest_example2.ipynb 

Deprecaton set to False
[0;31m---------------------------------------------------------------------------[0m
[0;31mFileNotFoundError[0m                         Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//sklearn_titanic_randomForest_example2.ipynb[0m in [0;36m<module>[0;34m[0m
[1;32m      3[0m [0;32mimport[0m [0mjson[0m[0;34m[0m[0;34m[0m[0m
[1;32m      4[0m [0mdata_path[0m [0;34m=[0m [0;34m'../mlmodels/dataset/json/hyper_titanic_randomForest.json'[0m[0;34m[0m[0;34m[0m[0m
[0;32m----> 5[0;31m [0mpars[0m [0;34m=[0m [0mjson[0m[0;34m.[0m[0mload[0m[0;34m([0m[0mopen[0m[0;34m([0m [0mdata_path[0m [0;34m,[0m [0mmode[0m[0;34m=[0m[0;34m'r'[0m[0;34m)[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      6[0m [0;32mfor[0m [0mkey[0m[0;34m,[0m [0mpdict[0m [0;32min[0m  [0mpars[0m[0;34m.[0m[0mitems[0m[0;34m([0m[0;34m)[0m [0;34m:[0m[0;34m[0m[0;34m[0m[0m
[1;32m      7[0m   [0mglobals[0m[0;34m([0m[0;34m)[0m[0;34m[[0m[0mkey[0m[0;34m][0m [0;34m=[0m [0mpdict[0m[0;34m[0m[0;34m[0m[0m

[0;31mFileNotFoundError[0m: [Errno 2] No such file or directory: '../mlmodels/dataset/json/hyper_titanic_randomForest.json'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//mnist_mlmodels_.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mModuleNotFoundError[0m                       Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//mnist_mlmodels_.ipynb[0m in [0;36m<module>[0;34m[0m
[0;32m----> 1[0;31m [0;32mfrom[0m [0mgoogle[0m[0;34m.[0m[0mcolab[0m [0;32mimport[0m [0mdrive[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      2[0m [0mdrive[0m[0;34m.[0m[0mmount[0m[0;34m([0m[0;34m'/content/drive'[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m

[0;31mModuleNotFoundError[0m: No module named 'google.colab'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//gluon_automl_titanic.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mFileNotFoundError[0m                         Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//gluon_automl_titanic.ipynb[0m in [0;36m<module>[0;34m[0m
[1;32m      8[0m     [0mchoice[0m[0;34m=[0m[0;34m'json'[0m[0;34m,[0m[0;34m[0m[0;34m[0m[0m
[1;32m      9[0m     [0mconfig_mode[0m[0;34m=[0m [0;34m'test'[0m[0;34m,[0m[0;34m[0m[0;34m[0m[0m
[0;32m---> 10[0;31m     [0mdata_path[0m[0;34m=[0m [0;34m'../mlmodels/dataset/json/gluon_automl.json'[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     11[0m )

[0;32m~/work/mlmodels/mlmodels/mlmodels/model_gluon/gluon_automl.py[0m in [0;36mget_params[0;34m(choice, data_path, config_mode, **kw)[0m
[1;32m     80[0m             __file__)).parent.parent / "model_gluon/gluon_automl.json" if data_path == "dataset/" else data_path
[1;32m     81[0m [0;34m[0m[0m
[0;32m---> 82[0;31m         [0;32mwith[0m [0mopen[0m[0;34m([0m[0mdata_path[0m[0;34m,[0m [0mencoding[0m[0;34m=[0m[0;34m'utf-8'[0m[0;34m)[0m [0;32mas[0m [0mconfig_f[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     83[0m             [0mconfig[0m [0;34m=[0m [0mjson[0m[0;34m.[0m[0mload[0m[0;34m([0m[0mconfig_f[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[1;32m     84[0m             [0mconfig[0m [0;34m=[0m [0mconfig[0m[0;34m[[0m[0mconfig_mode[0m[0;34m][0m[0;34m[0m[0;34m[0m[0m

[0;31mFileNotFoundError[0m: [Errno 2] No such file or directory: '../mlmodels/dataset/json/gluon_automl.json'
/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/mxnet/optimizer/optimizer.py:167: UserWarning: WARNING: New optimizer gluonnlp.optimizer.lamb.LAMB is overriding existing optimizer mxnet.optimizer.optimizer.LAMB
  Optimizer.opt_registry[name].__name__))





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//tensorflow__lstm_json.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mNameError[0m                                 Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//tensorflow__lstm_json.ipynb[0m in [0;36m<module>[0;34m[0m
[1;32m      5[0m [0;32mimport[0m [0mjson[0m[0;34m[0m[0;34m[0m[0m
[1;32m      6[0m [0;34m[0m[0m
[0;32m----> 7[0;31m [0mprint[0m[0;34m([0m [0mos[0m[0;34m.[0m[0mgetcwd[0m[0;34m([0m[0;34m)[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m
[0;31mNameError[0m: name 'os' is not defined





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//sklearn.ipynb 

[0;31m---------------------------------------------------------------------------[0m
[0;31mModuleNotFoundError[0m                       Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/models.py[0m in [0;36mmodule_load[0;34m(model_uri, verbose, env_build)[0m
[1;32m     71[0m         [0mmodel_name[0m [0;34m=[0m [0mmodel_uri[0m[0;34m.[0m[0mreplace[0m[0;34m([0m[0;34m".py"[0m[0;34m,[0m [0;34m""[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0;32m---> 72[0;31m         [0mmodule[0m [0;34m=[0m [0mimport_module[0m[0;34m([0m[0;34mf"mlmodels.{model_name}"[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     73[0m         [0;31m# module    = import_module("mlmodels.model_tf.1_lstm")[0m[0;34m[0m[0;34m[0m[0;34m[0m[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/__init__.py[0m in [0;36mimport_module[0;34m(name, package)[0m
[1;32m    125[0m             [0mlevel[0m [0;34m+=[0m [0;36m1[0m[0;34m[0m[0;34m[0m[0m
[0;32m--> 126[0;31m     [0;32mreturn[0m [0m_bootstrap[0m[0;34m.[0m[0m_gcd_import[0m[0;34m([0m[0mname[0m[0;34m[[0m[0mlevel[0m[0;34m:[0m[0;34m][0m[0;34m,[0m [0mpackage[0m[0;34m,[0m [0mlevel[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m    127[0m [0;34m[0m[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/_bootstrap.py[0m in [0;36m_gcd_import[0;34m(name, package, level)[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/_bootstrap.py[0m in [0;36m_find_and_load[0;34m(name, import_)[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/importlib/_bootstrap.py[0m in [0;36m_find_and_load_unlocked[0;34m(name, import_)[0m

[0;31mModuleNotFoundError[0m: No module named 'mlmodels.model_sklearn.sklearn'

During handling of the above exception, another exception occurred:

[0;31mIndexError[0m                                Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/models.py[0m in [0;36mmodule_load[0;34m(model_uri, verbose, env_build)[0m
[1;32m     83[0m             [0mmodel_name[0m [0;34m=[0m [0mPath[0m[0;34m([0m[0mmodel_uri[0m[0;34m)[0m[0;34m.[0m[0mstem[0m  [0;31m# remove .py[0m[0;34m[0m[0;34m[0m[0m
[0;32m---> 84[0;31m             [0mmodel_name[0m [0;34m=[0m [0mstr[0m[0;34m([0m[0mPath[0m[0;34m([0m[0mmodel_uri[0m[0;34m)[0m[0;34m.[0m[0mparts[0m[0;34m[[0m[0;34m-[0m[0;36m2[0m[0;34m][0m[0;34m)[0m [0;34m+[0m [0;34m"."[0m [0;34m+[0m [0mstr[0m[0;34m([0m[0mmodel_name[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     85[0m             [0;31m# print(model_name)[0m[0;34m[0m[0;34m[0m[0;34m[0m[0m

[0;31mIndexError[0m: tuple index out of range

During handling of the above exception, another exception occurred:

[0;31mNameError[0m                                 Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//sklearn.ipynb[0m in [0;36m<module>[0;34m[0m
[1;32m      1[0m [0;32mfrom[0m [0mmlmodels[0m[0;34m.[0m[0mmodels[0m [0;32mimport[0m [0mmodule_load[0m[0;34m[0m[0;34m[0m[0m
[1;32m      2[0m [0;34m[0m[0m
[0;32m----> 3[0;31m [0mmodule[0m        [0;34m=[0m  [0mmodule_load[0m[0;34m([0m [0mmodel_uri[0m[0;34m=[0m [0mmodel_uri[0m [0;34m)[0m                           [0;31m# Load file definition[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      4[0m [0mmodel[0m         [0;34m=[0m  [0mmodule[0m[0;34m.[0m[0mModel[0m[0;34m([0m[0mmodel_pars[0m[0;34m=[0m[0mmodel_pars[0m[0;34m,[0m [0mdata_pars[0m[0;34m=[0m[0mdata_pars[0m[0;34m,[0m [0mcompute_pars[0m[0;34m=[0m[0mcompute_pars[0m[0;34m)[0m             [0;31m# Create Model instance[0m[0;34m[0m[0;34m[0m[0m
[1;32m      5[0m [0mmodel[0m[0;34m,[0m [0msess[0m   [0;34m=[0m  [0mmodule[0m[0;34m.[0m[0mfit[0m[0;34m([0m[0mmodel[0m[0;34m,[0m [0mdata_pars[0m[0;34m=[0m[0mdata_pars[0m[0;34m,[0m [0mcompute_pars[0m[0;34m=[0m[0mcompute_pars[0m[0;34m,[0m [0mout_pars[0m[0;34m=[0m[0mout_pars[0m[0;34m)[0m          [0;31m# fit the model[0m[0;34m[0m[0;34m[0m[0m

[0;32m~/work/mlmodels/mlmodels/mlmodels/models.py[0m in [0;36mmodule_load[0;34m(model_uri, verbose, env_build)[0m
[1;32m     87[0m [0;34m[0m[0m
[1;32m     88[0m         [0;32mexcept[0m [0mException[0m [0;32mas[0m [0me2[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
[0;32m---> 89[0;31m             [0;32mraise[0m [0mNameError[0m[0;34m([0m[0;34mf"Module {model_name} notfound, {e1}, {e2}"[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     90[0m [0;34m[0m[0m
[1;32m     91[0m     [0;32mif[0m [0mverbose[0m[0;34m:[0m [0mprint[0m[0;34m([0m[0mmodule[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m

[0;31mNameError[0m: Module model_sklearn.sklearn notfound, No module named 'mlmodels.model_sklearn.sklearn', tuple index out of range





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//lightgbm_titanic.ipynb 

Deprecaton set to False
[0;31m---------------------------------------------------------------------------[0m
[0;31mFileNotFoundError[0m                         Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example//lightgbm_titanic.ipynb[0m in [0;36m<module>[0;34m[0m
[1;32m      1[0m [0mdata_path[0m [0;34m=[0m [0;34m'hyper_lightgbm_titanic.json'[0m[0;34m[0m[0;34m[0m[0m
[1;32m      2[0m [0;34m[0m[0m
[0;32m----> 3[0;31m [0mpars[0m [0;34m=[0m [0mjson[0m[0;34m.[0m[0mload[0m[0;34m([0m[0mopen[0m[0;34m([0m [0mdata_path[0m [0;34m,[0m [0mmode[0m[0;34m=[0m[0;34m'r'[0m[0;34m)[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      4[0m [0;32mfor[0m [0mkey[0m[0;34m,[0m [0mpdict[0m [0;32min[0m  [0mpars[0m[0;34m.[0m[0mitems[0m[0;34m([0m[0;34m)[0m [0;34m:[0m[0;34m[0m[0;34m[0m[0m
[1;32m      5[0m   [0mglobals[0m[0;34m([0m[0;34m)[0m[0;34m[[0m[0mkey[0m[0;34m][0m [0;34m=[0m [0mpdict[0m[0;34m[0m[0;34m[0m[0m

[0;31mFileNotFoundError[0m: [Errno 2] No such file or directory: 'hyper_lightgbm_titanic.json'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//vision_mnist.py 

[0;36m  File [0;32m"/home/runner/work/mlmodels/mlmodels/mlmodels/example/vision_mnist.py"[0;36m, line [0;32m15[0m
[0;31m    !git clone https://github.com/ahmed3bbas/mlmodels.git[0m
[0m    ^[0m
[0;31mSyntaxError[0m[0;31m:[0m invalid syntax






 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//benchmark_timeseries_m4.py 






 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//arun_hyper.py 

[0;31m---------------------------------------------------------------------------[0m
[0;31mNameError[0m                                 Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example/arun_hyper.py[0m in [0;36m<module>[0;34m[0m
[1;32m      3[0m [0;32mfrom[0m [0mmlmodels[0m[0;34m.[0m[0mmodels[0m [0;32mimport[0m [0mmodule_load[0m[0;34m[0m[0;34m[0m[0m
[1;32m      4[0m [0;32mfrom[0m [0mmlmodels[0m[0;34m.[0m[0mutil[0m [0;32mimport[0m [0mpath_norm_dict[0m[0;34m,[0m [0mpath_norm[0m[0;34m,[0m [0mparams_json_load[0m[0;34m[0m[0;34m[0m[0m
[0;32m----> 5[0;31m [0mprint[0m[0;34m([0m[0mmlmodels[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m      6[0m [0;34m[0m[0m
[1;32m      7[0m [0;34m[0m[0m

[0;31mNameError[0m: name 'mlmodels' is not defined





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//lightgbm_glass.py 

Deprecaton set to False
/home/runner/work/mlmodels/mlmodels
[0;31m---------------------------------------------------------------------------[0m
[0;31mFileNotFoundError[0m                         Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example/lightgbm_glass.py[0m in [0;36m<module>[0;34m[0m
[1;32m     20[0m [0;34m[0m[0m
[1;32m     21[0m [0;34m[0m[0m
[0;32m---> 22[0;31m [0mpars[0m [0;34m=[0m [0mjson[0m[0;34m.[0m[0mload[0m[0;34m([0m[0mopen[0m[0;34m([0m [0mconfig_path[0m [0;34m,[0m [0mmode[0m[0;34m=[0m[0;34m'r'[0m[0;34m)[0m[0;34m)[0m[0;34m[[0m[0mconfig_mode[0m[0;34m][0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     23[0m [0mprint[0m[0;34m([0m[0mpars[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[1;32m     24[0m [0;34m[0m[0m

[0;31mFileNotFoundError[0m: [Errno 2] No such file or directory: 'lightgbm_glass.json'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//benchmark_timeseries_m5.py 

[0;36m  File [0;32m"/home/runner/work/mlmodels/mlmodels/mlmodels/example/benchmark_timeseries_m5.py"[0;36m, line [0;32m248[0m
[0;31m    We then reshape the forecasts into the correct data shape for submission ...[0m
[0m          ^[0m
[0;31mSyntaxError[0m[0;31m:[0m invalid syntax






 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example//arun_model.py 

<module 'mlmodels' from '/home/runner/work/mlmodels/mlmodels/mlmodels/__init__.py'>
/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/ardmn.json
[0;31m---------------------------------------------------------------------------[0m
[0;31mFileNotFoundError[0m                         Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example/arun_model.py[0m in [0;36m<module>[0;34m[0m
[1;32m     25[0m [0;31m# Model Parameters[0m[0;34m[0m[0;34m[0m[0;34m[0m[0m
[1;32m     26[0m [0;31m# model_pars, data_pars, compute_pars, out_pars[0m[0;34m[0m[0;34m[0m[0;34m[0m[0m
[0;32m---> 27[0;31m [0mpars[0m [0;34m=[0m [0mjson[0m[0;34m.[0m[0mload[0m[0;34m([0m[0mopen[0m[0;34m([0m[0mconfig_path[0m [0;34m,[0m [0mmode[0m[0;34m=[0m[0;34m'r'[0m[0;34m)[0m[0;34m)[0m[0;34m[[0m[0mconfig_mode[0m[0;34m][0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     28[0m [0;32mfor[0m [0mkey[0m[0;34m,[0m [0mpdict[0m [0;32min[0m  [0mpars[0m[0;34m.[0m[0mitems[0m[0;34m([0m[0;34m)[0m [0;34m:[0m[0;34m[0m[0;34m[0m[0m
[1;32m     29[0m   [0mglobals[0m[0;34m([0m[0;34m)[0m[0;34m[[0m[0mkey[0m[0;34m][0m [0;34m=[0m [0mpath_norm_dict[0m[0;34m([0m [0mpdict[0m   [0;34m)[0m   [0;31m###Normalize path[0m[0;34m[0m[0;34m[0m[0m

[0;31mFileNotFoundError[0m: [Errno 2] No such file or directory: '/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/ardmn.json'





 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example/benchmark_timeseries_m4.py 






 ************************************************************************************************************************
ipython https://github.com/arita37/mlmodels/blob/dev/mlmodels/example/benchmark_timeseries_m5.py 

[0;36m  File [0;32m"/home/runner/work/mlmodels/mlmodels/mlmodels/example/benchmark_timeseries_m5.py"[0;36m, line [0;32m248[0m
[0;31m    We then reshape the forecasts into the correct data shape for submission ...[0m
[0m          ^[0m
[0;31mSyntaxError[0m[0;31m:[0m invalid syntax

