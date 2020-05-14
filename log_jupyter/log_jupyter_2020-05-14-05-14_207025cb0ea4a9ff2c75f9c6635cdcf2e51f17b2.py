
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
 40%|████      | 2/5 [00:51<01:17, 25.81s/it]Loading: dataset/models/NeuralNetClassifier/train_tabNNdataset.pkl
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
Finished Task with config: {'activation.choice': 0, 'dropout_prob': 0.16225073303365936, 'embedding_size_factor': 0.5128241641455085, 'layers.choice': 2, 'learning_rate': 0.00010944933130666803, 'network_type.choice': 0, 'use_batchnorm.choice': 1, 'weight_decay': 5.671126353425917e-10} and reward: 0.3056
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\xc4\xc4\xa1\xcc\x10\xd8\x11X\x15\x00\x00\x00embedding_size_factorq\x03G?\xe0i\x0e8\xb3O\xd4X\r\x00\x00\x00layers.choiceq\x04K\x02X\r\x00\x00\x00learning_rateq\x05G?\x1c\xb1\x051\xb2*?X\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x01X\x0c\x00\x00\x00weight_decayq\x08G>\x03|` i\r\xd8u.' and reward: 0.3056
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\xc4\xc4\xa1\xcc\x10\xd8\x11X\x15\x00\x00\x00embedding_size_factorq\x03G?\xe0i\x0e8\xb3O\xd4X\r\x00\x00\x00layers.choiceq\x04K\x02X\r\x00\x00\x00learning_rateq\x05G?\x1c\xb1\x051\xb2*?X\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x01X\x0c\x00\x00\x00weight_decayq\x08G>\x03|` i\r\xd8u.' and reward: 0.3056
 60%|██████    | 3/5 [01:42<01:06, 33.46s/it] 60%|██████    | 3/5 [01:42<01:08, 34.32s/it]
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
Finished Task with config: {'activation.choice': 2, 'dropout_prob': 0.479028964847451, 'embedding_size_factor': 0.6303388985460417, 'layers.choice': 3, 'learning_rate': 0.005433029438173294, 'network_type.choice': 0, 'use_batchnorm.choice': 1, 'weight_decay': 1.0265202281421257e-05} and reward: 0.3782
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x02X\x0c\x00\x00\x00dropout_probq\x02G?\xde\xa8i\x1av\xd1{X\x15\x00\x00\x00embedding_size_factorq\x03G?\xe4+\xbc{T\xdcuX\r\x00\x00\x00layers.choiceq\x04K\x03X\r\x00\x00\x00learning_rateq\x05G?v@\xf1\xbc\x15"/X\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x01X\x0c\x00\x00\x00weight_decayq\x08G>\xe5\x87\x16\xa8\xa2\xfb\xabu.' and reward: 0.3782
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x02X\x0c\x00\x00\x00dropout_probq\x02G?\xde\xa8i\x1av\xd1{X\x15\x00\x00\x00embedding_size_factorq\x03G?\xe4+\xbc{T\xdcuX\r\x00\x00\x00layers.choiceq\x04K\x03X\r\x00\x00\x00learning_rateq\x05G?v@\xf1\xbc\x15"/X\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x01X\x0c\x00\x00\x00weight_decayq\x08G>\xe5\x87\x16\xa8\xa2\xfb\xabu.' and reward: 0.3782
Please either provide filename or allow plot in get_training_curves
Time for Neural Network hyperparameter optimization: 156.41520810127258
Best hyperparameter configuration for Tabular Neural Network: 
{'activation.choice': 0, 'dropout_prob': 0.1, 'embedding_size_factor': 1.0, 'layers.choice': 0, 'learning_rate': 0.0005, 'network_type.choice': 0, 'use_batchnorm.choice': 0, 'weight_decay': 1e-06}
Saving dataset/models/trainer.pkl
Loading: dataset/models/NeuralNetClassifier/trial_0_tabularNN.pkl
Loading: dataset/models/NeuralNetClassifier/trial_1_tabularNN.pkl
Loading: dataset/models/NeuralNetClassifier/trial_2_tabularNN.pkl
Fitting model: weighted_ensemble_k0_l1 ... Training model for up to 119.75s of the -38.96s of remaining time.
Ensemble size: 51
Ensemble weights: 
[0.47058824 0.37254902 0.15686275]
	0.3926	 = Validation accuracy score
	1.05s	 = Training runtime
	0.0s	 = Validation runtime
Saving dataset/models/weighted_ensemble_k0_l1/model.pkl
Saving dataset/models/trainer.pkl
Saving dataset/models/trainer.pkl
Saving dataset/models/trainer.pkl
AutoGluon training complete, total runtime = 160.05s ...
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

  <mlmodels.model_tf.1_lstm.Model object at 0x7f43a248ba58> 

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
[[ 0.          0.          0.          0.          0.          0.        ]
 [-0.02941159 -0.10653286 -0.03441275  0.00807309 -0.09299517 -0.27912092]
 [ 0.12537602  0.07504924  0.08517335 -0.01082737  0.02684639  0.14648797]
 [ 0.10365332  0.20766743  0.371503   -0.0528238   0.11874559  0.14896639]
 [-0.02163674  0.26766306  0.09428775 -0.09187119 -0.13044766  0.01832332]
 [ 0.68504566  0.12050505  0.38830525 -0.31551239 -0.05384317  0.50750339]
 [-0.26118913 -0.55509466  0.50228113  0.17081445 -0.06666289  0.4749077 ]
 [-0.31490925 -0.20095307  0.20310743  0.17125537  0.23940867 -0.49817827]
 [ 0.26551405  0.19622158  0.3756263  -0.03320869 -0.43354025  0.21801127]
 [ 0.          0.          0.          0.          0.          0.        ]]

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
{'loss': 0.48557939752936363, 'loss_history': []}

  #### Plot   ######################################################## 

  #### Save   ######################################################## 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/'}
Model saved in path: /home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm//model//model.ckpt

  #### Load   ######################################################## 
2020-05-14 05:17:16.093091: W tensorflow/core/framework/op_kernel.cc:1651] OP_REQUIRES failed at save_restore_v2_ops.cc:184 : Not found: Key Variable not found in checkpoint
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
{'loss': 0.39384324476122856, 'loss_history': []}

  #### Plot   ######################################################## 

  #### Save   ######################################################## 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/'}
Model saved in path: /home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm//model//model.ckpt

  #### Load   ######################################################## 
2020-05-14 05:17:17.220266: W tensorflow/core/framework/op_kernel.cc:1651] OP_REQUIRES failed at save_restore_v2_ops.cc:184 : Not found: Key Variable not found in checkpoint
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
   24576/17464789 [..............................] - ETA: 48s
   57344/17464789 [..............................] - ETA: 42s
  106496/17464789 [..............................] - ETA: 33s
  212992/17464789 [..............................] - ETA: 22s
  401408/17464789 [..............................] - ETA: 14s
  802816/17464789 [>.............................] - ETA: 8s 
 1605632/17464789 [=>............................] - ETA: 4s
 3211264/17464789 [====>.........................] - ETA: 2s
 6242304/17464789 [=========>....................] - ETA: 1s
 9273344/17464789 [==============>...............] - ETA: 0s
12320768/17464789 [====================>.........] - ETA: 0s
15319040/17464789 [=========================>....] - ETA: 0s
17465344/17464789 [==============================] - 1s 0us/step
Pad sequences (samples x time)...
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/math_grad.py:1424: where (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
2020-05-14 05:17:29.626999: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 AVX512F FMA
2020-05-14 05:17:29.630912: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2095074999 Hz
2020-05-14 05:17:29.631051: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x562ca359e070 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-14 05:17:29.631065: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py:422: The name tf.global_variables is deprecated. Please use tf.compat.v1.global_variables instead.

Train on 25000 samples, validate on 25000 samples
Epoch 1/1

   32/25000 [..............................] - ETA: 4:51 - loss: 8.6249 - accuracy: 0.4375
   64/25000 [..............................] - ETA: 2:58 - loss: 7.6666 - accuracy: 0.5000
   96/25000 [..............................] - ETA: 2:18 - loss: 8.1458 - accuracy: 0.4688
  128/25000 [..............................] - ETA: 1:59 - loss: 7.5468 - accuracy: 0.5078
  160/25000 [..............................] - ETA: 1:47 - loss: 7.5708 - accuracy: 0.5063
  192/25000 [..............................] - ETA: 1:39 - loss: 7.2673 - accuracy: 0.5260
  224/25000 [..............................] - ETA: 1:34 - loss: 7.5297 - accuracy: 0.5089
  256/25000 [..............................] - ETA: 1:30 - loss: 7.5468 - accuracy: 0.5078
  288/25000 [..............................] - ETA: 1:26 - loss: 7.6134 - accuracy: 0.5035
  320/25000 [..............................] - ETA: 1:23 - loss: 7.8104 - accuracy: 0.4906
  352/25000 [..............................] - ETA: 1:21 - loss: 7.9715 - accuracy: 0.4801
  384/25000 [..............................] - ETA: 1:20 - loss: 8.0260 - accuracy: 0.4766
  416/25000 [..............................] - ETA: 1:18 - loss: 7.9983 - accuracy: 0.4784
  448/25000 [..............................] - ETA: 1:17 - loss: 8.1116 - accuracy: 0.4710
  480/25000 [..............................] - ETA: 1:16 - loss: 8.0500 - accuracy: 0.4750
  512/25000 [..............................] - ETA: 1:15 - loss: 8.0559 - accuracy: 0.4746
  544/25000 [..............................] - ETA: 1:14 - loss: 7.9485 - accuracy: 0.4816
  576/25000 [..............................] - ETA: 1:13 - loss: 8.0393 - accuracy: 0.4757
  608/25000 [..............................] - ETA: 1:12 - loss: 7.8936 - accuracy: 0.4852
  640/25000 [..............................] - ETA: 1:12 - loss: 7.8343 - accuracy: 0.4891
  672/25000 [..............................] - ETA: 1:11 - loss: 7.8492 - accuracy: 0.4881
  704/25000 [..............................] - ETA: 1:10 - loss: 7.8409 - accuracy: 0.4886
  736/25000 [..............................] - ETA: 1:10 - loss: 7.8125 - accuracy: 0.4905
  768/25000 [..............................] - ETA: 1:09 - loss: 7.7664 - accuracy: 0.4935
  800/25000 [..............................] - ETA: 1:09 - loss: 7.8008 - accuracy: 0.4913
  832/25000 [..............................] - ETA: 1:08 - loss: 7.7403 - accuracy: 0.4952
  864/25000 [>.............................] - ETA: 1:08 - loss: 7.6489 - accuracy: 0.5012
  896/25000 [>.............................] - ETA: 1:08 - loss: 7.6837 - accuracy: 0.4989
  928/25000 [>.............................] - ETA: 1:07 - loss: 7.7327 - accuracy: 0.4957
  960/25000 [>.............................] - ETA: 1:07 - loss: 7.7305 - accuracy: 0.4958
  992/25000 [>.............................] - ETA: 1:07 - loss: 7.7594 - accuracy: 0.4940
 1024/25000 [>.............................] - ETA: 1:06 - loss: 7.7565 - accuracy: 0.4941
 1056/25000 [>.............................] - ETA: 1:06 - loss: 7.7537 - accuracy: 0.4943
 1088/25000 [>.............................] - ETA: 1:06 - loss: 7.7371 - accuracy: 0.4954
 1120/25000 [>.............................] - ETA: 1:05 - loss: 7.7488 - accuracy: 0.4946
 1152/25000 [>.............................] - ETA: 1:05 - loss: 7.7598 - accuracy: 0.4939
 1184/25000 [>.............................] - ETA: 1:05 - loss: 7.7055 - accuracy: 0.4975
 1216/25000 [>.............................] - ETA: 1:04 - loss: 7.7044 - accuracy: 0.4975
 1248/25000 [>.............................] - ETA: 1:04 - loss: 7.7403 - accuracy: 0.4952
 1280/25000 [>.............................] - ETA: 1:04 - loss: 7.7625 - accuracy: 0.4938
 1312/25000 [>.............................] - ETA: 1:04 - loss: 7.7017 - accuracy: 0.4977
 1344/25000 [>.............................] - ETA: 1:04 - loss: 7.6780 - accuracy: 0.4993
 1376/25000 [>.............................] - ETA: 1:04 - loss: 7.7335 - accuracy: 0.4956
 1408/25000 [>.............................] - ETA: 1:03 - loss: 7.6993 - accuracy: 0.4979
 1440/25000 [>.............................] - ETA: 1:03 - loss: 7.6879 - accuracy: 0.4986
 1472/25000 [>.............................] - ETA: 1:03 - loss: 7.6979 - accuracy: 0.4980
 1504/25000 [>.............................] - ETA: 1:03 - loss: 7.6870 - accuracy: 0.4987
 1536/25000 [>.............................] - ETA: 1:03 - loss: 7.6067 - accuracy: 0.5039
 1568/25000 [>.............................] - ETA: 1:03 - loss: 7.5688 - accuracy: 0.5064
 1600/25000 [>.............................] - ETA: 1:02 - loss: 7.5708 - accuracy: 0.5063
 1632/25000 [>.............................] - ETA: 1:02 - loss: 7.5163 - accuracy: 0.5098
 1664/25000 [>.............................] - ETA: 1:02 - loss: 7.4915 - accuracy: 0.5114
 1696/25000 [=>............................] - ETA: 1:02 - loss: 7.4677 - accuracy: 0.5130
 1728/25000 [=>............................] - ETA: 1:02 - loss: 7.4537 - accuracy: 0.5139
 1760/25000 [=>............................] - ETA: 1:02 - loss: 7.4750 - accuracy: 0.5125
 1792/25000 [=>............................] - ETA: 1:01 - loss: 7.5040 - accuracy: 0.5106
 1824/25000 [=>............................] - ETA: 1:01 - loss: 7.5321 - accuracy: 0.5088
 1856/25000 [=>............................] - ETA: 1:01 - loss: 7.5840 - accuracy: 0.5054
 1888/25000 [=>............................] - ETA: 1:01 - loss: 7.5610 - accuracy: 0.5069
 1920/25000 [=>............................] - ETA: 1:01 - loss: 7.5788 - accuracy: 0.5057
 1952/25000 [=>............................] - ETA: 1:01 - loss: 7.5802 - accuracy: 0.5056
 1984/25000 [=>............................] - ETA: 1:01 - loss: 7.5893 - accuracy: 0.5050
 2016/25000 [=>............................] - ETA: 1:01 - loss: 7.5677 - accuracy: 0.5064
 2048/25000 [=>............................] - ETA: 1:00 - loss: 7.5693 - accuracy: 0.5063
 2080/25000 [=>............................] - ETA: 1:00 - loss: 7.5413 - accuracy: 0.5082
 2112/25000 [=>............................] - ETA: 1:00 - loss: 7.5795 - accuracy: 0.5057
 2144/25000 [=>............................] - ETA: 1:00 - loss: 7.5522 - accuracy: 0.5075
 2176/25000 [=>............................] - ETA: 1:00 - loss: 7.5680 - accuracy: 0.5064
 2208/25000 [=>............................] - ETA: 1:00 - loss: 7.5486 - accuracy: 0.5077
 2240/25000 [=>............................] - ETA: 1:00 - loss: 7.5503 - accuracy: 0.5076
 2272/25000 [=>............................] - ETA: 1:00 - loss: 7.5519 - accuracy: 0.5075
 2304/25000 [=>............................] - ETA: 59s - loss: 7.5734 - accuracy: 0.5061 
 2336/25000 [=>............................] - ETA: 59s - loss: 7.5747 - accuracy: 0.5060
 2368/25000 [=>............................] - ETA: 59s - loss: 7.5695 - accuracy: 0.5063
 2400/25000 [=>............................] - ETA: 59s - loss: 7.6027 - accuracy: 0.5042
 2432/25000 [=>............................] - ETA: 59s - loss: 7.5973 - accuracy: 0.5045
 2464/25000 [=>............................] - ETA: 59s - loss: 7.6044 - accuracy: 0.5041
 2496/25000 [=>............................] - ETA: 59s - loss: 7.6175 - accuracy: 0.5032
 2528/25000 [==>...........................] - ETA: 59s - loss: 7.6060 - accuracy: 0.5040
 2560/25000 [==>...........................] - ETA: 59s - loss: 7.6067 - accuracy: 0.5039
 2592/25000 [==>...........................] - ETA: 58s - loss: 7.5838 - accuracy: 0.5054
 2624/25000 [==>...........................] - ETA: 58s - loss: 7.5907 - accuracy: 0.5050
 2656/25000 [==>...........................] - ETA: 58s - loss: 7.5800 - accuracy: 0.5056
 2688/25000 [==>...........................] - ETA: 58s - loss: 7.5868 - accuracy: 0.5052
 2720/25000 [==>...........................] - ETA: 58s - loss: 7.5821 - accuracy: 0.5055
 2752/25000 [==>...........................] - ETA: 58s - loss: 7.5775 - accuracy: 0.5058
 2784/25000 [==>...........................] - ETA: 58s - loss: 7.5620 - accuracy: 0.5068
 2816/25000 [==>...........................] - ETA: 57s - loss: 7.5632 - accuracy: 0.5067
 2848/25000 [==>...........................] - ETA: 57s - loss: 7.5912 - accuracy: 0.5049
 2880/25000 [==>...........................] - ETA: 57s - loss: 7.6027 - accuracy: 0.5042
 2912/25000 [==>...........................] - ETA: 57s - loss: 7.5929 - accuracy: 0.5048
 2944/25000 [==>...........................] - ETA: 57s - loss: 7.5625 - accuracy: 0.5068
 2976/25000 [==>...........................] - ETA: 57s - loss: 7.5687 - accuracy: 0.5064
 3008/25000 [==>...........................] - ETA: 57s - loss: 7.5698 - accuracy: 0.5063
 3040/25000 [==>...........................] - ETA: 57s - loss: 7.5657 - accuracy: 0.5066
 3072/25000 [==>...........................] - ETA: 57s - loss: 7.5468 - accuracy: 0.5078
 3104/25000 [==>...........................] - ETA: 56s - loss: 7.5431 - accuracy: 0.5081
 3136/25000 [==>...........................] - ETA: 56s - loss: 7.5297 - accuracy: 0.5089
 3168/25000 [==>...........................] - ETA: 56s - loss: 7.5214 - accuracy: 0.5095
 3200/25000 [==>...........................] - ETA: 56s - loss: 7.4989 - accuracy: 0.5109
 3232/25000 [==>...........................] - ETA: 56s - loss: 7.5006 - accuracy: 0.5108
 3264/25000 [==>...........................] - ETA: 56s - loss: 7.5163 - accuracy: 0.5098
 3296/25000 [==>...........................] - ETA: 56s - loss: 7.5317 - accuracy: 0.5088
 3328/25000 [==>...........................] - ETA: 56s - loss: 7.5422 - accuracy: 0.5081
 3360/25000 [===>..........................] - ETA: 56s - loss: 7.5434 - accuracy: 0.5080
 3392/25000 [===>..........................] - ETA: 56s - loss: 7.5446 - accuracy: 0.5080
 3424/25000 [===>..........................] - ETA: 56s - loss: 7.5368 - accuracy: 0.5085
 3456/25000 [===>..........................] - ETA: 55s - loss: 7.5690 - accuracy: 0.5064
 3488/25000 [===>..........................] - ETA: 55s - loss: 7.5655 - accuracy: 0.5066
 3520/25000 [===>..........................] - ETA: 55s - loss: 7.5882 - accuracy: 0.5051
 3552/25000 [===>..........................] - ETA: 55s - loss: 7.5976 - accuracy: 0.5045
 3584/25000 [===>..........................] - ETA: 55s - loss: 7.6024 - accuracy: 0.5042
 3616/25000 [===>..........................] - ETA: 55s - loss: 7.5988 - accuracy: 0.5044
 3648/25000 [===>..........................] - ETA: 55s - loss: 7.5910 - accuracy: 0.5049
 3680/25000 [===>..........................] - ETA: 55s - loss: 7.6041 - accuracy: 0.5041
 3712/25000 [===>..........................] - ETA: 55s - loss: 7.6047 - accuracy: 0.5040
 3744/25000 [===>..........................] - ETA: 55s - loss: 7.6011 - accuracy: 0.5043
 3776/25000 [===>..........................] - ETA: 54s - loss: 7.5976 - accuracy: 0.5045
 3808/25000 [===>..........................] - ETA: 54s - loss: 7.6022 - accuracy: 0.5042
 3840/25000 [===>..........................] - ETA: 54s - loss: 7.6107 - accuracy: 0.5036
 3872/25000 [===>..........................] - ETA: 54s - loss: 7.6151 - accuracy: 0.5034
 3904/25000 [===>..........................] - ETA: 54s - loss: 7.6273 - accuracy: 0.5026
 3936/25000 [===>..........................] - ETA: 54s - loss: 7.6199 - accuracy: 0.5030
 3968/25000 [===>..........................] - ETA: 54s - loss: 7.6434 - accuracy: 0.5015
 4000/25000 [===>..........................] - ETA: 54s - loss: 7.6398 - accuracy: 0.5017
 4032/25000 [===>..........................] - ETA: 54s - loss: 7.6400 - accuracy: 0.5017
 4064/25000 [===>..........................] - ETA: 54s - loss: 7.6440 - accuracy: 0.5015
 4096/25000 [===>..........................] - ETA: 53s - loss: 7.6329 - accuracy: 0.5022
 4128/25000 [===>..........................] - ETA: 53s - loss: 7.6295 - accuracy: 0.5024
 4160/25000 [===>..........................] - ETA: 53s - loss: 7.6224 - accuracy: 0.5029
 4192/25000 [====>.........................] - ETA: 53s - loss: 7.6300 - accuracy: 0.5024
 4224/25000 [====>.........................] - ETA: 53s - loss: 7.6339 - accuracy: 0.5021
 4256/25000 [====>.........................] - ETA: 53s - loss: 7.6234 - accuracy: 0.5028
 4288/25000 [====>.........................] - ETA: 53s - loss: 7.6166 - accuracy: 0.5033
 4320/25000 [====>.........................] - ETA: 53s - loss: 7.6311 - accuracy: 0.5023
 4352/25000 [====>.........................] - ETA: 53s - loss: 7.6173 - accuracy: 0.5032
 4384/25000 [====>.........................] - ETA: 53s - loss: 7.6281 - accuracy: 0.5025
 4416/25000 [====>.........................] - ETA: 52s - loss: 7.6215 - accuracy: 0.5029
 4448/25000 [====>.........................] - ETA: 52s - loss: 7.6390 - accuracy: 0.5018
 4480/25000 [====>.........................] - ETA: 52s - loss: 7.6324 - accuracy: 0.5022
 4512/25000 [====>.........................] - ETA: 52s - loss: 7.6360 - accuracy: 0.5020
 4544/25000 [====>.........................] - ETA: 52s - loss: 7.6194 - accuracy: 0.5031
 4576/25000 [====>.........................] - ETA: 52s - loss: 7.6298 - accuracy: 0.5024
 4608/25000 [====>.........................] - ETA: 52s - loss: 7.6333 - accuracy: 0.5022
 4640/25000 [====>.........................] - ETA: 52s - loss: 7.6468 - accuracy: 0.5013
 4672/25000 [====>.........................] - ETA: 52s - loss: 7.6404 - accuracy: 0.5017
 4704/25000 [====>.........................] - ETA: 52s - loss: 7.6373 - accuracy: 0.5019
 4736/25000 [====>.........................] - ETA: 52s - loss: 7.6375 - accuracy: 0.5019
 4768/25000 [====>.........................] - ETA: 51s - loss: 7.6538 - accuracy: 0.5008
 4800/25000 [====>.........................] - ETA: 51s - loss: 7.6538 - accuracy: 0.5008
 4832/25000 [====>.........................] - ETA: 51s - loss: 7.6603 - accuracy: 0.5004
 4864/25000 [====>.........................] - ETA: 51s - loss: 7.6635 - accuracy: 0.5002
 4896/25000 [====>.........................] - ETA: 51s - loss: 7.6635 - accuracy: 0.5002
 4928/25000 [====>.........................] - ETA: 51s - loss: 7.6728 - accuracy: 0.4996
 4960/25000 [====>.........................] - ETA: 51s - loss: 7.6604 - accuracy: 0.5004
 4992/25000 [====>.........................] - ETA: 51s - loss: 7.6513 - accuracy: 0.5010
 5024/25000 [=====>........................] - ETA: 51s - loss: 7.6483 - accuracy: 0.5012
 5056/25000 [=====>........................] - ETA: 51s - loss: 7.6515 - accuracy: 0.5010
 5088/25000 [=====>........................] - ETA: 51s - loss: 7.6516 - accuracy: 0.5010
 5120/25000 [=====>........................] - ETA: 50s - loss: 7.6487 - accuracy: 0.5012
 5152/25000 [=====>........................] - ETA: 50s - loss: 7.6547 - accuracy: 0.5008
 5184/25000 [=====>........................] - ETA: 50s - loss: 7.6666 - accuracy: 0.5000
 5216/25000 [=====>........................] - ETA: 50s - loss: 7.6784 - accuracy: 0.4992
 5248/25000 [=====>........................] - ETA: 50s - loss: 7.6754 - accuracy: 0.4994
 5280/25000 [=====>........................] - ETA: 50s - loss: 7.6666 - accuracy: 0.5000
 5312/25000 [=====>........................] - ETA: 50s - loss: 7.6724 - accuracy: 0.4996
 5344/25000 [=====>........................] - ETA: 50s - loss: 7.6810 - accuracy: 0.4991
 5376/25000 [=====>........................] - ETA: 50s - loss: 7.6723 - accuracy: 0.4996
 5408/25000 [=====>........................] - ETA: 50s - loss: 7.6666 - accuracy: 0.5000
 5440/25000 [=====>........................] - ETA: 50s - loss: 7.6666 - accuracy: 0.5000
 5472/25000 [=====>........................] - ETA: 49s - loss: 7.6722 - accuracy: 0.4996
 5504/25000 [=====>........................] - ETA: 49s - loss: 7.6666 - accuracy: 0.5000
 5536/25000 [=====>........................] - ETA: 49s - loss: 7.6777 - accuracy: 0.4993
 5568/25000 [=====>........................] - ETA: 49s - loss: 7.6886 - accuracy: 0.4986
 5600/25000 [=====>........................] - ETA: 49s - loss: 7.6830 - accuracy: 0.4989
 5632/25000 [=====>........................] - ETA: 49s - loss: 7.6911 - accuracy: 0.4984
 5664/25000 [=====>........................] - ETA: 49s - loss: 7.7018 - accuracy: 0.4977
 5696/25000 [=====>........................] - ETA: 49s - loss: 7.6935 - accuracy: 0.4982
 5728/25000 [=====>........................] - ETA: 49s - loss: 7.6934 - accuracy: 0.4983
 5760/25000 [=====>........................] - ETA: 49s - loss: 7.6932 - accuracy: 0.4983
 5792/25000 [=====>........................] - ETA: 49s - loss: 7.6984 - accuracy: 0.4979
 5824/25000 [=====>........................] - ETA: 49s - loss: 7.6982 - accuracy: 0.4979
 5856/25000 [======>.......................] - ETA: 48s - loss: 7.7007 - accuracy: 0.4978
 5888/25000 [======>.......................] - ETA: 48s - loss: 7.7057 - accuracy: 0.4975
 5920/25000 [======>.......................] - ETA: 48s - loss: 7.7158 - accuracy: 0.4968
 5952/25000 [======>.......................] - ETA: 48s - loss: 7.7104 - accuracy: 0.4971
 5984/25000 [======>.......................] - ETA: 48s - loss: 7.6999 - accuracy: 0.4978
 6016/25000 [======>.......................] - ETA: 48s - loss: 7.7125 - accuracy: 0.4970
 6048/25000 [======>.......................] - ETA: 48s - loss: 7.7173 - accuracy: 0.4967
 6080/25000 [======>.......................] - ETA: 48s - loss: 7.7246 - accuracy: 0.4962
 6112/25000 [======>.......................] - ETA: 48s - loss: 7.7394 - accuracy: 0.4953
 6144/25000 [======>.......................] - ETA: 48s - loss: 7.7415 - accuracy: 0.4951
 6176/25000 [======>.......................] - ETA: 48s - loss: 7.7560 - accuracy: 0.4942
 6208/25000 [======>.......................] - ETA: 48s - loss: 7.7506 - accuracy: 0.4945
 6240/25000 [======>.......................] - ETA: 48s - loss: 7.7526 - accuracy: 0.4944
 6272/25000 [======>.......................] - ETA: 47s - loss: 7.7497 - accuracy: 0.4946
 6304/25000 [======>.......................] - ETA: 47s - loss: 7.7493 - accuracy: 0.4946
 6336/25000 [======>.......................] - ETA: 47s - loss: 7.7634 - accuracy: 0.4937
 6368/25000 [======>.......................] - ETA: 47s - loss: 7.7629 - accuracy: 0.4937
 6400/25000 [======>.......................] - ETA: 47s - loss: 7.7553 - accuracy: 0.4942
 6432/25000 [======>.......................] - ETA: 47s - loss: 7.7667 - accuracy: 0.4935
 6464/25000 [======>.......................] - ETA: 47s - loss: 7.7686 - accuracy: 0.4933
 6496/25000 [======>.......................] - ETA: 47s - loss: 7.7658 - accuracy: 0.4935
 6528/25000 [======>.......................] - ETA: 47s - loss: 7.7629 - accuracy: 0.4937
 6560/25000 [======>.......................] - ETA: 47s - loss: 7.7578 - accuracy: 0.4941
 6592/25000 [======>.......................] - ETA: 47s - loss: 7.7573 - accuracy: 0.4941
 6624/25000 [======>.......................] - ETA: 46s - loss: 7.7662 - accuracy: 0.4935
 6656/25000 [======>.......................] - ETA: 46s - loss: 7.7726 - accuracy: 0.4931
 6688/25000 [=======>......................] - ETA: 46s - loss: 7.7721 - accuracy: 0.4931
 6720/25000 [=======>......................] - ETA: 46s - loss: 7.7739 - accuracy: 0.4930
 6752/25000 [=======>......................] - ETA: 46s - loss: 7.7711 - accuracy: 0.4932
 6784/25000 [=======>......................] - ETA: 46s - loss: 7.7819 - accuracy: 0.4925
 6816/25000 [=======>......................] - ETA: 46s - loss: 7.7724 - accuracy: 0.4931
 6848/25000 [=======>......................] - ETA: 46s - loss: 7.7674 - accuracy: 0.4934
 6880/25000 [=======>......................] - ETA: 46s - loss: 7.7714 - accuracy: 0.4932
 6912/25000 [=======>......................] - ETA: 46s - loss: 7.7664 - accuracy: 0.4935
 6944/25000 [=======>......................] - ETA: 46s - loss: 7.7660 - accuracy: 0.4935
 6976/25000 [=======>......................] - ETA: 46s - loss: 7.7633 - accuracy: 0.4937
 7008/25000 [=======>......................] - ETA: 45s - loss: 7.7695 - accuracy: 0.4933
 7040/25000 [=======>......................] - ETA: 45s - loss: 7.7603 - accuracy: 0.4939
 7072/25000 [=======>......................] - ETA: 45s - loss: 7.7664 - accuracy: 0.4935
 7104/25000 [=======>......................] - ETA: 45s - loss: 7.7702 - accuracy: 0.4932
 7136/25000 [=======>......................] - ETA: 45s - loss: 7.7612 - accuracy: 0.4938
 7168/25000 [=======>......................] - ETA: 45s - loss: 7.7543 - accuracy: 0.4943
 7200/25000 [=======>......................] - ETA: 45s - loss: 7.7475 - accuracy: 0.4947
 7232/25000 [=======>......................] - ETA: 45s - loss: 7.7451 - accuracy: 0.4949
 7264/25000 [=======>......................] - ETA: 45s - loss: 7.7342 - accuracy: 0.4956
 7296/25000 [=======>......................] - ETA: 45s - loss: 7.7255 - accuracy: 0.4962
 7328/25000 [=======>......................] - ETA: 45s - loss: 7.7231 - accuracy: 0.4963
 7360/25000 [=======>......................] - ETA: 45s - loss: 7.7270 - accuracy: 0.4961
 7392/25000 [=======>......................] - ETA: 44s - loss: 7.7206 - accuracy: 0.4965
 7424/25000 [=======>......................] - ETA: 44s - loss: 7.7100 - accuracy: 0.4972
 7456/25000 [=======>......................] - ETA: 44s - loss: 7.7180 - accuracy: 0.4966
 7488/25000 [=======>......................] - ETA: 44s - loss: 7.7158 - accuracy: 0.4968
 7520/25000 [========>.....................] - ETA: 44s - loss: 7.7115 - accuracy: 0.4971
 7552/25000 [========>.....................] - ETA: 44s - loss: 7.7072 - accuracy: 0.4974
 7584/25000 [========>.....................] - ETA: 44s - loss: 7.7050 - accuracy: 0.4975
 7616/25000 [========>.....................] - ETA: 44s - loss: 7.7029 - accuracy: 0.4976
 7648/25000 [========>.....................] - ETA: 44s - loss: 7.7067 - accuracy: 0.4974
 7680/25000 [========>.....................] - ETA: 44s - loss: 7.7046 - accuracy: 0.4975
 7712/25000 [========>.....................] - ETA: 44s - loss: 7.7024 - accuracy: 0.4977
 7744/25000 [========>.....................] - ETA: 44s - loss: 7.7003 - accuracy: 0.4978
 7776/25000 [========>.....................] - ETA: 43s - loss: 7.6962 - accuracy: 0.4981
 7808/25000 [========>.....................] - ETA: 43s - loss: 7.6941 - accuracy: 0.4982
 7840/25000 [========>.....................] - ETA: 43s - loss: 7.6881 - accuracy: 0.4986
 7872/25000 [========>.....................] - ETA: 43s - loss: 7.6978 - accuracy: 0.4980
 7904/25000 [========>.....................] - ETA: 43s - loss: 7.7074 - accuracy: 0.4973
 7936/25000 [========>.....................] - ETA: 43s - loss: 7.7091 - accuracy: 0.4972
 7968/25000 [========>.....................] - ETA: 43s - loss: 7.7070 - accuracy: 0.4974
 8000/25000 [========>.....................] - ETA: 43s - loss: 7.7011 - accuracy: 0.4978
 8032/25000 [========>.....................] - ETA: 43s - loss: 7.6972 - accuracy: 0.4980
 8064/25000 [========>.....................] - ETA: 43s - loss: 7.6989 - accuracy: 0.4979
 8096/25000 [========>.....................] - ETA: 43s - loss: 7.6969 - accuracy: 0.4980
 8128/25000 [========>.....................] - ETA: 43s - loss: 7.7081 - accuracy: 0.4973
 8160/25000 [========>.....................] - ETA: 42s - loss: 7.7117 - accuracy: 0.4971
 8192/25000 [========>.....................] - ETA: 42s - loss: 7.7097 - accuracy: 0.4972
 8224/25000 [========>.....................] - ETA: 42s - loss: 7.7076 - accuracy: 0.4973
 8256/25000 [========>.....................] - ETA: 42s - loss: 7.7168 - accuracy: 0.4967
 8288/25000 [========>.....................] - ETA: 42s - loss: 7.7166 - accuracy: 0.4967
 8320/25000 [========>.....................] - ETA: 42s - loss: 7.7108 - accuracy: 0.4971
 8352/25000 [=========>....................] - ETA: 42s - loss: 7.7162 - accuracy: 0.4968
 8384/25000 [=========>....................] - ETA: 42s - loss: 7.7178 - accuracy: 0.4967
 8416/25000 [=========>....................] - ETA: 42s - loss: 7.7176 - accuracy: 0.4967
 8448/25000 [=========>....................] - ETA: 42s - loss: 7.7229 - accuracy: 0.4963
 8480/25000 [=========>....................] - ETA: 42s - loss: 7.7389 - accuracy: 0.4953
 8512/25000 [=========>....................] - ETA: 42s - loss: 7.7351 - accuracy: 0.4955
 8544/25000 [=========>....................] - ETA: 41s - loss: 7.7312 - accuracy: 0.4958
 8576/25000 [=========>....................] - ETA: 41s - loss: 7.7381 - accuracy: 0.4953
 8608/25000 [=========>....................] - ETA: 41s - loss: 7.7397 - accuracy: 0.4952
 8640/25000 [=========>....................] - ETA: 41s - loss: 7.7412 - accuracy: 0.4951
 8672/25000 [=========>....................] - ETA: 41s - loss: 7.7426 - accuracy: 0.4950
 8704/25000 [=========>....................] - ETA: 41s - loss: 7.7459 - accuracy: 0.4948
 8736/25000 [=========>....................] - ETA: 41s - loss: 7.7509 - accuracy: 0.4945
 8768/25000 [=========>....................] - ETA: 41s - loss: 7.7488 - accuracy: 0.4946
 8800/25000 [=========>....................] - ETA: 41s - loss: 7.7485 - accuracy: 0.4947
 8832/25000 [=========>....................] - ETA: 41s - loss: 7.7430 - accuracy: 0.4950
 8864/25000 [=========>....................] - ETA: 41s - loss: 7.7445 - accuracy: 0.4949
 8896/25000 [=========>....................] - ETA: 41s - loss: 7.7425 - accuracy: 0.4951
 8928/25000 [=========>....................] - ETA: 40s - loss: 7.7456 - accuracy: 0.4948
 8960/25000 [=========>....................] - ETA: 40s - loss: 7.7402 - accuracy: 0.4952
 8992/25000 [=========>....................] - ETA: 40s - loss: 7.7348 - accuracy: 0.4956
 9024/25000 [=========>....................] - ETA: 40s - loss: 7.7363 - accuracy: 0.4955
 9056/25000 [=========>....................] - ETA: 40s - loss: 7.7394 - accuracy: 0.4953
 9088/25000 [=========>....................] - ETA: 40s - loss: 7.7375 - accuracy: 0.4954
 9120/25000 [=========>....................] - ETA: 40s - loss: 7.7356 - accuracy: 0.4955
 9152/25000 [=========>....................] - ETA: 40s - loss: 7.7320 - accuracy: 0.4957
 9184/25000 [==========>...................] - ETA: 40s - loss: 7.7284 - accuracy: 0.4960
 9216/25000 [==========>...................] - ETA: 40s - loss: 7.7298 - accuracy: 0.4959
 9248/25000 [==========>...................] - ETA: 40s - loss: 7.7329 - accuracy: 0.4957
 9280/25000 [==========>...................] - ETA: 40s - loss: 7.7410 - accuracy: 0.4952
 9312/25000 [==========>...................] - ETA: 40s - loss: 7.7358 - accuracy: 0.4955
 9344/25000 [==========>...................] - ETA: 39s - loss: 7.7405 - accuracy: 0.4952
 9376/25000 [==========>...................] - ETA: 39s - loss: 7.7468 - accuracy: 0.4948
 9408/25000 [==========>...................] - ETA: 39s - loss: 7.7432 - accuracy: 0.4950
 9440/25000 [==========>...................] - ETA: 39s - loss: 7.7413 - accuracy: 0.4951
 9472/25000 [==========>...................] - ETA: 39s - loss: 7.7476 - accuracy: 0.4947
 9504/25000 [==========>...................] - ETA: 39s - loss: 7.7521 - accuracy: 0.4944
 9536/25000 [==========>...................] - ETA: 39s - loss: 7.7615 - accuracy: 0.4938
 9568/25000 [==========>...................] - ETA: 39s - loss: 7.7564 - accuracy: 0.4941
 9600/25000 [==========>...................] - ETA: 39s - loss: 7.7625 - accuracy: 0.4938
 9632/25000 [==========>...................] - ETA: 39s - loss: 7.7605 - accuracy: 0.4939
 9664/25000 [==========>...................] - ETA: 39s - loss: 7.7650 - accuracy: 0.4936
 9696/25000 [==========>...................] - ETA: 39s - loss: 7.7631 - accuracy: 0.4937
 9728/25000 [==========>...................] - ETA: 38s - loss: 7.7675 - accuracy: 0.4934
 9760/25000 [==========>...................] - ETA: 38s - loss: 7.7672 - accuracy: 0.4934
 9792/25000 [==========>...................] - ETA: 38s - loss: 7.7700 - accuracy: 0.4933
 9824/25000 [==========>...................] - ETA: 38s - loss: 7.7759 - accuracy: 0.4929
 9856/25000 [==========>...................] - ETA: 38s - loss: 7.7677 - accuracy: 0.4934
 9888/25000 [==========>...................] - ETA: 38s - loss: 7.7690 - accuracy: 0.4933
 9920/25000 [==========>...................] - ETA: 38s - loss: 7.7594 - accuracy: 0.4940
 9952/25000 [==========>...................] - ETA: 38s - loss: 7.7529 - accuracy: 0.4944
 9984/25000 [==========>...................] - ETA: 38s - loss: 7.7465 - accuracy: 0.4948
10016/25000 [===========>..................] - ETA: 38s - loss: 7.7508 - accuracy: 0.4945
10048/25000 [===========>..................] - ETA: 38s - loss: 7.7551 - accuracy: 0.4942
10080/25000 [===========>..................] - ETA: 38s - loss: 7.7518 - accuracy: 0.4944
10112/25000 [===========>..................] - ETA: 38s - loss: 7.7470 - accuracy: 0.4948
10144/25000 [===========>..................] - ETA: 37s - loss: 7.7498 - accuracy: 0.4946
10176/25000 [===========>..................] - ETA: 37s - loss: 7.7525 - accuracy: 0.4944
10208/25000 [===========>..................] - ETA: 37s - loss: 7.7522 - accuracy: 0.4944
10240/25000 [===========>..................] - ETA: 37s - loss: 7.7475 - accuracy: 0.4947
10272/25000 [===========>..................] - ETA: 37s - loss: 7.7427 - accuracy: 0.4950
10304/25000 [===========>..................] - ETA: 37s - loss: 7.7470 - accuracy: 0.4948
10336/25000 [===========>..................] - ETA: 37s - loss: 7.7438 - accuracy: 0.4950
10368/25000 [===========>..................] - ETA: 37s - loss: 7.7480 - accuracy: 0.4947
10400/25000 [===========>..................] - ETA: 37s - loss: 7.7536 - accuracy: 0.4943
10432/25000 [===========>..................] - ETA: 37s - loss: 7.7533 - accuracy: 0.4943
10464/25000 [===========>..................] - ETA: 37s - loss: 7.7487 - accuracy: 0.4946
10496/25000 [===========>..................] - ETA: 37s - loss: 7.7470 - accuracy: 0.4948
10528/25000 [===========>..................] - ETA: 36s - loss: 7.7438 - accuracy: 0.4950
10560/25000 [===========>..................] - ETA: 36s - loss: 7.7421 - accuracy: 0.4951
10592/25000 [===========>..................] - ETA: 36s - loss: 7.7419 - accuracy: 0.4951
10624/25000 [===========>..................] - ETA: 36s - loss: 7.7417 - accuracy: 0.4951
10656/25000 [===========>..................] - ETA: 36s - loss: 7.7414 - accuracy: 0.4951
10688/25000 [===========>..................] - ETA: 36s - loss: 7.7441 - accuracy: 0.4949
10720/25000 [===========>..................] - ETA: 36s - loss: 7.7467 - accuracy: 0.4948
10752/25000 [===========>..................] - ETA: 36s - loss: 7.7479 - accuracy: 0.4947
10784/25000 [===========>..................] - ETA: 36s - loss: 7.7477 - accuracy: 0.4947
10816/25000 [===========>..................] - ETA: 36s - loss: 7.7503 - accuracy: 0.4945
10848/25000 [============>.................] - ETA: 36s - loss: 7.7429 - accuracy: 0.4950
10880/25000 [============>.................] - ETA: 36s - loss: 7.7441 - accuracy: 0.4949
10912/25000 [============>.................] - ETA: 35s - loss: 7.7439 - accuracy: 0.4950
10944/25000 [============>.................] - ETA: 35s - loss: 7.7493 - accuracy: 0.4946
10976/25000 [============>.................] - ETA: 35s - loss: 7.7476 - accuracy: 0.4947
11008/25000 [============>.................] - ETA: 35s - loss: 7.7474 - accuracy: 0.4947
11040/25000 [============>.................] - ETA: 35s - loss: 7.7555 - accuracy: 0.4942
11072/25000 [============>.................] - ETA: 35s - loss: 7.7539 - accuracy: 0.4943
11104/25000 [============>.................] - ETA: 35s - loss: 7.7536 - accuracy: 0.4943
11136/25000 [============>.................] - ETA: 35s - loss: 7.7547 - accuracy: 0.4943
11168/25000 [============>.................] - ETA: 35s - loss: 7.7531 - accuracy: 0.4944
11200/25000 [============>.................] - ETA: 35s - loss: 7.7501 - accuracy: 0.4946
11232/25000 [============>.................] - ETA: 35s - loss: 7.7567 - accuracy: 0.4941
11264/25000 [============>.................] - ETA: 35s - loss: 7.7619 - accuracy: 0.4938
11296/25000 [============>.................] - ETA: 34s - loss: 7.7644 - accuracy: 0.4936
11328/25000 [============>.................] - ETA: 34s - loss: 7.7695 - accuracy: 0.4933
11360/25000 [============>.................] - ETA: 34s - loss: 7.7706 - accuracy: 0.4932
11392/25000 [============>.................] - ETA: 34s - loss: 7.7756 - accuracy: 0.4929
11424/25000 [============>.................] - ETA: 34s - loss: 7.7753 - accuracy: 0.4929
11456/25000 [============>.................] - ETA: 34s - loss: 7.7750 - accuracy: 0.4929
11488/25000 [============>.................] - ETA: 34s - loss: 7.7734 - accuracy: 0.4930
11520/25000 [============>.................] - ETA: 34s - loss: 7.7744 - accuracy: 0.4930
11552/25000 [============>.................] - ETA: 34s - loss: 7.7675 - accuracy: 0.4934
11584/25000 [============>.................] - ETA: 34s - loss: 7.7659 - accuracy: 0.4935
11616/25000 [============>.................] - ETA: 34s - loss: 7.7643 - accuracy: 0.4936
11648/25000 [============>.................] - ETA: 34s - loss: 7.7653 - accuracy: 0.4936
11680/25000 [=============>................] - ETA: 33s - loss: 7.7625 - accuracy: 0.4938
11712/25000 [=============>................] - ETA: 33s - loss: 7.7661 - accuracy: 0.4935
11744/25000 [=============>................] - ETA: 33s - loss: 7.7645 - accuracy: 0.4936
11776/25000 [=============>................] - ETA: 33s - loss: 7.7630 - accuracy: 0.4937
11808/25000 [=============>................] - ETA: 33s - loss: 7.7614 - accuracy: 0.4938
11840/25000 [=============>................] - ETA: 33s - loss: 7.7599 - accuracy: 0.4939
11872/25000 [=============>................] - ETA: 33s - loss: 7.7557 - accuracy: 0.4942
11904/25000 [=============>................] - ETA: 33s - loss: 7.7568 - accuracy: 0.4941
11936/25000 [=============>................] - ETA: 33s - loss: 7.7565 - accuracy: 0.4941
11968/25000 [=============>................] - ETA: 33s - loss: 7.7512 - accuracy: 0.4945
12000/25000 [=============>................] - ETA: 33s - loss: 7.7510 - accuracy: 0.4945
12032/25000 [=============>................] - ETA: 33s - loss: 7.7520 - accuracy: 0.4944
12064/25000 [=============>................] - ETA: 33s - loss: 7.7543 - accuracy: 0.4943
12096/25000 [=============>................] - ETA: 32s - loss: 7.7592 - accuracy: 0.4940
12128/25000 [=============>................] - ETA: 32s - loss: 7.7564 - accuracy: 0.4941
12160/25000 [=============>................] - ETA: 32s - loss: 7.7524 - accuracy: 0.4944
12192/25000 [=============>................] - ETA: 32s - loss: 7.7509 - accuracy: 0.4945
12224/25000 [=============>................] - ETA: 32s - loss: 7.7482 - accuracy: 0.4947
12256/25000 [=============>................] - ETA: 32s - loss: 7.7492 - accuracy: 0.4946
12288/25000 [=============>................] - ETA: 32s - loss: 7.7490 - accuracy: 0.4946
12320/25000 [=============>................] - ETA: 32s - loss: 7.7475 - accuracy: 0.4947
12352/25000 [=============>................] - ETA: 32s - loss: 7.7448 - accuracy: 0.4949
12384/25000 [=============>................] - ETA: 32s - loss: 7.7508 - accuracy: 0.4945
12416/25000 [=============>................] - ETA: 32s - loss: 7.7494 - accuracy: 0.4946
12448/25000 [=============>................] - ETA: 32s - loss: 7.7528 - accuracy: 0.4944
12480/25000 [=============>................] - ETA: 31s - loss: 7.7502 - accuracy: 0.4946
12512/25000 [==============>...............] - ETA: 31s - loss: 7.7561 - accuracy: 0.4942
12544/25000 [==============>...............] - ETA: 31s - loss: 7.7546 - accuracy: 0.4943
12576/25000 [==============>...............] - ETA: 31s - loss: 7.7544 - accuracy: 0.4943
12608/25000 [==============>...............] - ETA: 31s - loss: 7.7554 - accuracy: 0.4942
12640/25000 [==============>...............] - ETA: 31s - loss: 7.7600 - accuracy: 0.4939
12672/25000 [==============>...............] - ETA: 31s - loss: 7.7574 - accuracy: 0.4941
12704/25000 [==============>...............] - ETA: 31s - loss: 7.7596 - accuracy: 0.4939
12736/25000 [==============>...............] - ETA: 31s - loss: 7.7605 - accuracy: 0.4939
12768/25000 [==============>...............] - ETA: 31s - loss: 7.7555 - accuracy: 0.4942
12800/25000 [==============>...............] - ETA: 31s - loss: 7.7517 - accuracy: 0.4945
12832/25000 [==============>...............] - ETA: 31s - loss: 7.7515 - accuracy: 0.4945
12864/25000 [==============>...............] - ETA: 30s - loss: 7.7524 - accuracy: 0.4944
12896/25000 [==============>...............] - ETA: 30s - loss: 7.7510 - accuracy: 0.4945
12928/25000 [==============>...............] - ETA: 30s - loss: 7.7496 - accuracy: 0.4946
12960/25000 [==============>...............] - ETA: 30s - loss: 7.7459 - accuracy: 0.4948
12992/25000 [==============>...............] - ETA: 30s - loss: 7.7445 - accuracy: 0.4949
13024/25000 [==============>...............] - ETA: 30s - loss: 7.7431 - accuracy: 0.4950
13056/25000 [==============>...............] - ETA: 30s - loss: 7.7441 - accuracy: 0.4949
13088/25000 [==============>...............] - ETA: 30s - loss: 7.7498 - accuracy: 0.4946
13120/25000 [==============>...............] - ETA: 30s - loss: 7.7508 - accuracy: 0.4945
13152/25000 [==============>...............] - ETA: 30s - loss: 7.7529 - accuracy: 0.4944
13184/25000 [==============>...............] - ETA: 30s - loss: 7.7538 - accuracy: 0.4943
13216/25000 [==============>...............] - ETA: 30s - loss: 7.7525 - accuracy: 0.4944
13248/25000 [==============>...............] - ETA: 29s - loss: 7.7465 - accuracy: 0.4948
13280/25000 [==============>...............] - ETA: 29s - loss: 7.7474 - accuracy: 0.4947
13312/25000 [==============>...............] - ETA: 29s - loss: 7.7449 - accuracy: 0.4949
13344/25000 [===============>..............] - ETA: 29s - loss: 7.7471 - accuracy: 0.4948
13376/25000 [===============>..............] - ETA: 29s - loss: 7.7492 - accuracy: 0.4946
13408/25000 [===============>..............] - ETA: 29s - loss: 7.7467 - accuracy: 0.4948
13440/25000 [===============>..............] - ETA: 29s - loss: 7.7431 - accuracy: 0.4950
13472/25000 [===============>..............] - ETA: 29s - loss: 7.7406 - accuracy: 0.4952
13504/25000 [===============>..............] - ETA: 29s - loss: 7.7438 - accuracy: 0.4950
13536/25000 [===============>..............] - ETA: 29s - loss: 7.7402 - accuracy: 0.4952
13568/25000 [===============>..............] - ETA: 29s - loss: 7.7389 - accuracy: 0.4953
13600/25000 [===============>..............] - ETA: 29s - loss: 7.7444 - accuracy: 0.4949
13632/25000 [===============>..............] - ETA: 28s - loss: 7.7442 - accuracy: 0.4949
13664/25000 [===============>..............] - ETA: 28s - loss: 7.7384 - accuracy: 0.4953
13696/25000 [===============>..............] - ETA: 28s - loss: 7.7360 - accuracy: 0.4955
13728/25000 [===============>..............] - ETA: 28s - loss: 7.7348 - accuracy: 0.4956
13760/25000 [===============>..............] - ETA: 28s - loss: 7.7357 - accuracy: 0.4955
13792/25000 [===============>..............] - ETA: 28s - loss: 7.7355 - accuracy: 0.4955
13824/25000 [===============>..............] - ETA: 28s - loss: 7.7376 - accuracy: 0.4954
13856/25000 [===============>..............] - ETA: 28s - loss: 7.7374 - accuracy: 0.4954
13888/25000 [===============>..............] - ETA: 28s - loss: 7.7351 - accuracy: 0.4955
13920/25000 [===============>..............] - ETA: 28s - loss: 7.7305 - accuracy: 0.4958
13952/25000 [===============>..............] - ETA: 28s - loss: 7.7271 - accuracy: 0.4961
13984/25000 [===============>..............] - ETA: 28s - loss: 7.7291 - accuracy: 0.4959
14016/25000 [===============>..............] - ETA: 27s - loss: 7.7257 - accuracy: 0.4961
14048/25000 [===============>..............] - ETA: 27s - loss: 7.7245 - accuracy: 0.4962
14080/25000 [===============>..............] - ETA: 27s - loss: 7.7265 - accuracy: 0.4961
14112/25000 [===============>..............] - ETA: 27s - loss: 7.7199 - accuracy: 0.4965
14144/25000 [===============>..............] - ETA: 27s - loss: 7.7197 - accuracy: 0.4965
14176/25000 [================>.............] - ETA: 27s - loss: 7.7196 - accuracy: 0.4965
14208/25000 [================>.............] - ETA: 27s - loss: 7.7195 - accuracy: 0.4966
14240/25000 [================>.............] - ETA: 27s - loss: 7.7205 - accuracy: 0.4965
14272/25000 [================>.............] - ETA: 27s - loss: 7.7193 - accuracy: 0.4966
14304/25000 [================>.............] - ETA: 27s - loss: 7.7149 - accuracy: 0.4969
14336/25000 [================>.............] - ETA: 27s - loss: 7.7115 - accuracy: 0.4971
14368/25000 [================>.............] - ETA: 27s - loss: 7.7050 - accuracy: 0.4975
14400/25000 [================>.............] - ETA: 26s - loss: 7.7081 - accuracy: 0.4973
14432/25000 [================>.............] - ETA: 26s - loss: 7.7112 - accuracy: 0.4971
14464/25000 [================>.............] - ETA: 26s - loss: 7.7122 - accuracy: 0.4970
14496/25000 [================>.............] - ETA: 26s - loss: 7.7100 - accuracy: 0.4972
14528/25000 [================>.............] - ETA: 26s - loss: 7.7057 - accuracy: 0.4975
14560/25000 [================>.............] - ETA: 26s - loss: 7.7003 - accuracy: 0.4978
14592/25000 [================>.............] - ETA: 26s - loss: 7.7023 - accuracy: 0.4977
14624/25000 [================>.............] - ETA: 26s - loss: 7.7033 - accuracy: 0.4976
14656/25000 [================>.............] - ETA: 26s - loss: 7.7043 - accuracy: 0.4975
14688/25000 [================>.............] - ETA: 26s - loss: 7.7021 - accuracy: 0.4977
14720/25000 [================>.............] - ETA: 26s - loss: 7.6968 - accuracy: 0.4980
14752/25000 [================>.............] - ETA: 26s - loss: 7.6926 - accuracy: 0.4983
14784/25000 [================>.............] - ETA: 26s - loss: 7.6925 - accuracy: 0.4983
14816/25000 [================>.............] - ETA: 25s - loss: 7.6904 - accuracy: 0.4984
14848/25000 [================>.............] - ETA: 25s - loss: 7.6935 - accuracy: 0.4982
14880/25000 [================>.............] - ETA: 25s - loss: 7.6914 - accuracy: 0.4984
14912/25000 [================>.............] - ETA: 25s - loss: 7.6944 - accuracy: 0.4982
14944/25000 [================>.............] - ETA: 25s - loss: 7.6892 - accuracy: 0.4985
14976/25000 [================>.............] - ETA: 25s - loss: 7.6902 - accuracy: 0.4985
15008/25000 [=================>............] - ETA: 25s - loss: 7.6922 - accuracy: 0.4983
15040/25000 [=================>............] - ETA: 25s - loss: 7.6972 - accuracy: 0.4980
15072/25000 [=================>............] - ETA: 25s - loss: 7.6982 - accuracy: 0.4979
15104/25000 [=================>............] - ETA: 25s - loss: 7.7001 - accuracy: 0.4978
15136/25000 [=================>............] - ETA: 25s - loss: 7.6960 - accuracy: 0.4981
15168/25000 [=================>............] - ETA: 25s - loss: 7.6990 - accuracy: 0.4979
15200/25000 [=================>............] - ETA: 24s - loss: 7.6989 - accuracy: 0.4979
15232/25000 [=================>............] - ETA: 24s - loss: 7.7029 - accuracy: 0.4976
15264/25000 [=================>............] - ETA: 24s - loss: 7.7038 - accuracy: 0.4976
15296/25000 [=================>............] - ETA: 24s - loss: 7.7037 - accuracy: 0.4976
15328/25000 [=================>............] - ETA: 24s - loss: 7.7016 - accuracy: 0.4977
15360/25000 [=================>............] - ETA: 24s - loss: 7.7046 - accuracy: 0.4975
15392/25000 [=================>............] - ETA: 24s - loss: 7.7025 - accuracy: 0.4977
15424/25000 [=================>............] - ETA: 24s - loss: 7.7054 - accuracy: 0.4975
15456/25000 [=================>............] - ETA: 24s - loss: 7.7043 - accuracy: 0.4975
15488/25000 [=================>............] - ETA: 24s - loss: 7.7003 - accuracy: 0.4978
15520/25000 [=================>............] - ETA: 24s - loss: 7.6933 - accuracy: 0.4983
15552/25000 [=================>............] - ETA: 24s - loss: 7.6952 - accuracy: 0.4981
15584/25000 [=================>............] - ETA: 23s - loss: 7.6981 - accuracy: 0.4979
15616/25000 [=================>............] - ETA: 23s - loss: 7.6931 - accuracy: 0.4983
15648/25000 [=================>............] - ETA: 23s - loss: 7.6901 - accuracy: 0.4985
15680/25000 [=================>............] - ETA: 23s - loss: 7.6901 - accuracy: 0.4985
15712/25000 [=================>............] - ETA: 23s - loss: 7.6900 - accuracy: 0.4985
15744/25000 [=================>............] - ETA: 23s - loss: 7.6890 - accuracy: 0.4985
15776/25000 [=================>............] - ETA: 23s - loss: 7.6880 - accuracy: 0.4986
15808/25000 [=================>............] - ETA: 23s - loss: 7.6880 - accuracy: 0.4986
15840/25000 [==================>...........] - ETA: 23s - loss: 7.6869 - accuracy: 0.4987
15872/25000 [==================>...........] - ETA: 23s - loss: 7.6830 - accuracy: 0.4989
15904/25000 [==================>...........] - ETA: 23s - loss: 7.6820 - accuracy: 0.4990
15936/25000 [==================>...........] - ETA: 23s - loss: 7.6811 - accuracy: 0.4991
15968/25000 [==================>...........] - ETA: 22s - loss: 7.6820 - accuracy: 0.4990
16000/25000 [==================>...........] - ETA: 22s - loss: 7.6858 - accuracy: 0.4988
16032/25000 [==================>...........] - ETA: 22s - loss: 7.6857 - accuracy: 0.4988
16064/25000 [==================>...........] - ETA: 22s - loss: 7.6848 - accuracy: 0.4988
16096/25000 [==================>...........] - ETA: 22s - loss: 7.6857 - accuracy: 0.4988
16128/25000 [==================>...........] - ETA: 22s - loss: 7.6885 - accuracy: 0.4986
16160/25000 [==================>...........] - ETA: 22s - loss: 7.6856 - accuracy: 0.4988
16192/25000 [==================>...........] - ETA: 22s - loss: 7.6865 - accuracy: 0.4987
16224/25000 [==================>...........] - ETA: 22s - loss: 7.6836 - accuracy: 0.4989
16256/25000 [==================>...........] - ETA: 22s - loss: 7.6864 - accuracy: 0.4987
16288/25000 [==================>...........] - ETA: 22s - loss: 7.6864 - accuracy: 0.4987
16320/25000 [==================>...........] - ETA: 22s - loss: 7.6873 - accuracy: 0.4987
16352/25000 [==================>...........] - ETA: 22s - loss: 7.6919 - accuracy: 0.4983
16384/25000 [==================>...........] - ETA: 21s - loss: 7.6881 - accuracy: 0.4986
16416/25000 [==================>...........] - ETA: 21s - loss: 7.6862 - accuracy: 0.4987
16448/25000 [==================>...........] - ETA: 21s - loss: 7.6843 - accuracy: 0.4988
16480/25000 [==================>...........] - ETA: 21s - loss: 7.6843 - accuracy: 0.4988
16512/25000 [==================>...........] - ETA: 21s - loss: 7.6778 - accuracy: 0.4993
16544/25000 [==================>...........] - ETA: 21s - loss: 7.6777 - accuracy: 0.4993
16576/25000 [==================>...........] - ETA: 21s - loss: 7.6740 - accuracy: 0.4995
16608/25000 [==================>...........] - ETA: 21s - loss: 7.6722 - accuracy: 0.4996
16640/25000 [==================>...........] - ETA: 21s - loss: 7.6721 - accuracy: 0.4996
16672/25000 [===================>..........] - ETA: 21s - loss: 7.6694 - accuracy: 0.4998
16704/25000 [===================>..........] - ETA: 21s - loss: 7.6675 - accuracy: 0.4999
16736/25000 [===================>..........] - ETA: 21s - loss: 7.6703 - accuracy: 0.4998
16768/25000 [===================>..........] - ETA: 20s - loss: 7.6730 - accuracy: 0.4996
16800/25000 [===================>..........] - ETA: 20s - loss: 7.6721 - accuracy: 0.4996
16832/25000 [===================>..........] - ETA: 20s - loss: 7.6730 - accuracy: 0.4996
16864/25000 [===================>..........] - ETA: 20s - loss: 7.6730 - accuracy: 0.4996
16896/25000 [===================>..........] - ETA: 20s - loss: 7.6766 - accuracy: 0.4993
16928/25000 [===================>..........] - ETA: 20s - loss: 7.6775 - accuracy: 0.4993
16960/25000 [===================>..........] - ETA: 20s - loss: 7.6775 - accuracy: 0.4993
16992/25000 [===================>..........] - ETA: 20s - loss: 7.6774 - accuracy: 0.4993
17024/25000 [===================>..........] - ETA: 20s - loss: 7.6747 - accuracy: 0.4995
17056/25000 [===================>..........] - ETA: 20s - loss: 7.6783 - accuracy: 0.4992
17088/25000 [===================>..........] - ETA: 20s - loss: 7.6765 - accuracy: 0.4994
17120/25000 [===================>..........] - ETA: 20s - loss: 7.6729 - accuracy: 0.4996
17152/25000 [===================>..........] - ETA: 19s - loss: 7.6738 - accuracy: 0.4995
17184/25000 [===================>..........] - ETA: 19s - loss: 7.6764 - accuracy: 0.4994
17216/25000 [===================>..........] - ETA: 19s - loss: 7.6720 - accuracy: 0.4997
17248/25000 [===================>..........] - ETA: 19s - loss: 7.6764 - accuracy: 0.4994
17280/25000 [===================>..........] - ETA: 19s - loss: 7.6755 - accuracy: 0.4994
17312/25000 [===================>..........] - ETA: 19s - loss: 7.6781 - accuracy: 0.4992
17344/25000 [===================>..........] - ETA: 19s - loss: 7.6746 - accuracy: 0.4995
17376/25000 [===================>..........] - ETA: 19s - loss: 7.6719 - accuracy: 0.4997
17408/25000 [===================>..........] - ETA: 19s - loss: 7.6710 - accuracy: 0.4997
17440/25000 [===================>..........] - ETA: 19s - loss: 7.6684 - accuracy: 0.4999
17472/25000 [===================>..........] - ETA: 19s - loss: 7.6675 - accuracy: 0.4999
17504/25000 [====================>.........] - ETA: 19s - loss: 7.6657 - accuracy: 0.5001
17536/25000 [====================>.........] - ETA: 18s - loss: 7.6649 - accuracy: 0.5001
17568/25000 [====================>.........] - ETA: 18s - loss: 7.6675 - accuracy: 0.4999
17600/25000 [====================>.........] - ETA: 18s - loss: 7.6649 - accuracy: 0.5001
17632/25000 [====================>.........] - ETA: 18s - loss: 7.6649 - accuracy: 0.5001
17664/25000 [====================>.........] - ETA: 18s - loss: 7.6631 - accuracy: 0.5002
17696/25000 [====================>.........] - ETA: 18s - loss: 7.6632 - accuracy: 0.5002
17728/25000 [====================>.........] - ETA: 18s - loss: 7.6562 - accuracy: 0.5007
17760/25000 [====================>.........] - ETA: 18s - loss: 7.6545 - accuracy: 0.5008
17792/25000 [====================>.........] - ETA: 18s - loss: 7.6520 - accuracy: 0.5010
17824/25000 [====================>.........] - ETA: 18s - loss: 7.6537 - accuracy: 0.5008
17856/25000 [====================>.........] - ETA: 18s - loss: 7.6512 - accuracy: 0.5010
17888/25000 [====================>.........] - ETA: 18s - loss: 7.6563 - accuracy: 0.5007
17920/25000 [====================>.........] - ETA: 17s - loss: 7.6555 - accuracy: 0.5007
17952/25000 [====================>.........] - ETA: 17s - loss: 7.6521 - accuracy: 0.5009
17984/25000 [====================>.........] - ETA: 17s - loss: 7.6547 - accuracy: 0.5008
18016/25000 [====================>.........] - ETA: 17s - loss: 7.6581 - accuracy: 0.5006
18048/25000 [====================>.........] - ETA: 17s - loss: 7.6598 - accuracy: 0.5004
18080/25000 [====================>.........] - ETA: 17s - loss: 7.6590 - accuracy: 0.5005
18112/25000 [====================>.........] - ETA: 17s - loss: 7.6590 - accuracy: 0.5005
18144/25000 [====================>.........] - ETA: 17s - loss: 7.6607 - accuracy: 0.5004
18176/25000 [====================>.........] - ETA: 17s - loss: 7.6607 - accuracy: 0.5004
18208/25000 [====================>.........] - ETA: 17s - loss: 7.6607 - accuracy: 0.5004
18240/25000 [====================>.........] - ETA: 17s - loss: 7.6599 - accuracy: 0.5004
18272/25000 [====================>.........] - ETA: 17s - loss: 7.6557 - accuracy: 0.5007
18304/25000 [====================>.........] - ETA: 17s - loss: 7.6566 - accuracy: 0.5007
18336/25000 [=====================>........] - ETA: 16s - loss: 7.6583 - accuracy: 0.5005
18368/25000 [=====================>........] - ETA: 16s - loss: 7.6583 - accuracy: 0.5005
18400/25000 [=====================>........] - ETA: 16s - loss: 7.6583 - accuracy: 0.5005
18432/25000 [=====================>........] - ETA: 16s - loss: 7.6616 - accuracy: 0.5003
18464/25000 [=====================>........] - ETA: 16s - loss: 7.6658 - accuracy: 0.5001
18496/25000 [=====================>........] - ETA: 16s - loss: 7.6658 - accuracy: 0.5001
18528/25000 [=====================>........] - ETA: 16s - loss: 7.6666 - accuracy: 0.5000
18560/25000 [=====================>........] - ETA: 16s - loss: 7.6625 - accuracy: 0.5003
18592/25000 [=====================>........] - ETA: 16s - loss: 7.6650 - accuracy: 0.5001
18624/25000 [=====================>........] - ETA: 16s - loss: 7.6617 - accuracy: 0.5003
18656/25000 [=====================>........] - ETA: 16s - loss: 7.6576 - accuracy: 0.5006
18688/25000 [=====================>........] - ETA: 16s - loss: 7.6609 - accuracy: 0.5004
18720/25000 [=====================>........] - ETA: 15s - loss: 7.6601 - accuracy: 0.5004
18752/25000 [=====================>........] - ETA: 15s - loss: 7.6625 - accuracy: 0.5003
18784/25000 [=====================>........] - ETA: 15s - loss: 7.6674 - accuracy: 0.4999
18816/25000 [=====================>........] - ETA: 15s - loss: 7.6674 - accuracy: 0.4999
18848/25000 [=====================>........] - ETA: 15s - loss: 7.6650 - accuracy: 0.5001
18880/25000 [=====================>........] - ETA: 15s - loss: 7.6609 - accuracy: 0.5004
18912/25000 [=====================>........] - ETA: 15s - loss: 7.6593 - accuracy: 0.5005
18944/25000 [=====================>........] - ETA: 15s - loss: 7.6658 - accuracy: 0.5001
18976/25000 [=====================>........] - ETA: 15s - loss: 7.6690 - accuracy: 0.4998
19008/25000 [=====================>........] - ETA: 15s - loss: 7.6666 - accuracy: 0.5000
19040/25000 [=====================>........] - ETA: 15s - loss: 7.6650 - accuracy: 0.5001
19072/25000 [=====================>........] - ETA: 15s - loss: 7.6634 - accuracy: 0.5002
19104/25000 [=====================>........] - ETA: 14s - loss: 7.6610 - accuracy: 0.5004
19136/25000 [=====================>........] - ETA: 14s - loss: 7.6634 - accuracy: 0.5002
19168/25000 [======================>.......] - ETA: 14s - loss: 7.6610 - accuracy: 0.5004
19200/25000 [======================>.......] - ETA: 14s - loss: 7.6650 - accuracy: 0.5001
19232/25000 [======================>.......] - ETA: 14s - loss: 7.6618 - accuracy: 0.5003
19264/25000 [======================>.......] - ETA: 14s - loss: 7.6579 - accuracy: 0.5006
19296/25000 [======================>.......] - ETA: 14s - loss: 7.6579 - accuracy: 0.5006
19328/25000 [======================>.......] - ETA: 14s - loss: 7.6555 - accuracy: 0.5007
19360/25000 [======================>.......] - ETA: 14s - loss: 7.6539 - accuracy: 0.5008
19392/25000 [======================>.......] - ETA: 14s - loss: 7.6548 - accuracy: 0.5008
19424/25000 [======================>.......] - ETA: 14s - loss: 7.6579 - accuracy: 0.5006
19456/25000 [======================>.......] - ETA: 14s - loss: 7.6580 - accuracy: 0.5006
19488/25000 [======================>.......] - ETA: 13s - loss: 7.6572 - accuracy: 0.5006
19520/25000 [======================>.......] - ETA: 13s - loss: 7.6548 - accuracy: 0.5008
19552/25000 [======================>.......] - ETA: 13s - loss: 7.6564 - accuracy: 0.5007
19584/25000 [======================>.......] - ETA: 13s - loss: 7.6572 - accuracy: 0.5006
19616/25000 [======================>.......] - ETA: 13s - loss: 7.6565 - accuracy: 0.5007
19648/25000 [======================>.......] - ETA: 13s - loss: 7.6588 - accuracy: 0.5005
19680/25000 [======================>.......] - ETA: 13s - loss: 7.6580 - accuracy: 0.5006
19712/25000 [======================>.......] - ETA: 13s - loss: 7.6596 - accuracy: 0.5005
19744/25000 [======================>.......] - ETA: 13s - loss: 7.6596 - accuracy: 0.5005
19776/25000 [======================>.......] - ETA: 13s - loss: 7.6565 - accuracy: 0.5007
19808/25000 [======================>.......] - ETA: 13s - loss: 7.6597 - accuracy: 0.5005
19840/25000 [======================>.......] - ETA: 13s - loss: 7.6566 - accuracy: 0.5007
19872/25000 [======================>.......] - ETA: 13s - loss: 7.6558 - accuracy: 0.5007
19904/25000 [======================>.......] - ETA: 12s - loss: 7.6543 - accuracy: 0.5008
19936/25000 [======================>.......] - ETA: 12s - loss: 7.6520 - accuracy: 0.5010
19968/25000 [======================>.......] - ETA: 12s - loss: 7.6505 - accuracy: 0.5011
20000/25000 [=======================>......] - ETA: 12s - loss: 7.6513 - accuracy: 0.5010
20032/25000 [=======================>......] - ETA: 12s - loss: 7.6513 - accuracy: 0.5010
20064/25000 [=======================>......] - ETA: 12s - loss: 7.6529 - accuracy: 0.5009
20096/25000 [=======================>......] - ETA: 12s - loss: 7.6567 - accuracy: 0.5006
20128/25000 [=======================>......] - ETA: 12s - loss: 7.6560 - accuracy: 0.5007
20160/25000 [=======================>......] - ETA: 12s - loss: 7.6575 - accuracy: 0.5006
20192/25000 [=======================>......] - ETA: 12s - loss: 7.6567 - accuracy: 0.5006
20224/25000 [=======================>......] - ETA: 12s - loss: 7.6552 - accuracy: 0.5007
20256/25000 [=======================>......] - ETA: 12s - loss: 7.6553 - accuracy: 0.5007
20288/25000 [=======================>......] - ETA: 11s - loss: 7.6530 - accuracy: 0.5009
20320/25000 [=======================>......] - ETA: 11s - loss: 7.6545 - accuracy: 0.5008
20352/25000 [=======================>......] - ETA: 11s - loss: 7.6538 - accuracy: 0.5008
20384/25000 [=======================>......] - ETA: 11s - loss: 7.6523 - accuracy: 0.5009
20416/25000 [=======================>......] - ETA: 11s - loss: 7.6523 - accuracy: 0.5009
20448/25000 [=======================>......] - ETA: 11s - loss: 7.6554 - accuracy: 0.5007
20480/25000 [=======================>......] - ETA: 11s - loss: 7.6561 - accuracy: 0.5007
20512/25000 [=======================>......] - ETA: 11s - loss: 7.6621 - accuracy: 0.5003
20544/25000 [=======================>......] - ETA: 11s - loss: 7.6614 - accuracy: 0.5003
20576/25000 [=======================>......] - ETA: 11s - loss: 7.6562 - accuracy: 0.5007
20608/25000 [=======================>......] - ETA: 11s - loss: 7.6592 - accuracy: 0.5005
20640/25000 [=======================>......] - ETA: 11s - loss: 7.6577 - accuracy: 0.5006
20672/25000 [=======================>......] - ETA: 10s - loss: 7.6614 - accuracy: 0.5003
20704/25000 [=======================>......] - ETA: 10s - loss: 7.6614 - accuracy: 0.5003
20736/25000 [=======================>......] - ETA: 10s - loss: 7.6622 - accuracy: 0.5003
20768/25000 [=======================>......] - ETA: 10s - loss: 7.6659 - accuracy: 0.5000
20800/25000 [=======================>......] - ETA: 10s - loss: 7.6674 - accuracy: 0.5000
20832/25000 [=======================>......] - ETA: 10s - loss: 7.6674 - accuracy: 0.5000
20864/25000 [========================>.....] - ETA: 10s - loss: 7.6688 - accuracy: 0.4999
20896/25000 [========================>.....] - ETA: 10s - loss: 7.6703 - accuracy: 0.4998
20928/25000 [========================>.....] - ETA: 10s - loss: 7.6739 - accuracy: 0.4995
20960/25000 [========================>.....] - ETA: 10s - loss: 7.6739 - accuracy: 0.4995
20992/25000 [========================>.....] - ETA: 10s - loss: 7.6754 - accuracy: 0.4994
21024/25000 [========================>.....] - ETA: 10s - loss: 7.6783 - accuracy: 0.4992
21056/25000 [========================>.....] - ETA: 10s - loss: 7.6797 - accuracy: 0.4991
21088/25000 [========================>.....] - ETA: 9s - loss: 7.6775 - accuracy: 0.4993 
21120/25000 [========================>.....] - ETA: 9s - loss: 7.6782 - accuracy: 0.4992
21152/25000 [========================>.....] - ETA: 9s - loss: 7.6760 - accuracy: 0.4994
21184/25000 [========================>.....] - ETA: 9s - loss: 7.6753 - accuracy: 0.4994
21216/25000 [========================>.....] - ETA: 9s - loss: 7.6738 - accuracy: 0.4995
21248/25000 [========================>.....] - ETA: 9s - loss: 7.6731 - accuracy: 0.4996
21280/25000 [========================>.....] - ETA: 9s - loss: 7.6731 - accuracy: 0.4996
21312/25000 [========================>.....] - ETA: 9s - loss: 7.6760 - accuracy: 0.4994
21344/25000 [========================>.....] - ETA: 9s - loss: 7.6745 - accuracy: 0.4995
21376/25000 [========================>.....] - ETA: 9s - loss: 7.6795 - accuracy: 0.4992
21408/25000 [========================>.....] - ETA: 9s - loss: 7.6795 - accuracy: 0.4992
21440/25000 [========================>.....] - ETA: 9s - loss: 7.6809 - accuracy: 0.4991
21472/25000 [========================>.....] - ETA: 8s - loss: 7.6809 - accuracy: 0.4991
21504/25000 [========================>.....] - ETA: 8s - loss: 7.6830 - accuracy: 0.4989
21536/25000 [========================>.....] - ETA: 8s - loss: 7.6844 - accuracy: 0.4988
21568/25000 [========================>.....] - ETA: 8s - loss: 7.6858 - accuracy: 0.4987
21600/25000 [========================>.....] - ETA: 8s - loss: 7.6879 - accuracy: 0.4986
21632/25000 [========================>.....] - ETA: 8s - loss: 7.6858 - accuracy: 0.4988
21664/25000 [========================>.....] - ETA: 8s - loss: 7.6907 - accuracy: 0.4984
21696/25000 [=========================>....] - ETA: 8s - loss: 7.6914 - accuracy: 0.4984
21728/25000 [=========================>....] - ETA: 8s - loss: 7.6920 - accuracy: 0.4983
21760/25000 [=========================>....] - ETA: 8s - loss: 7.6913 - accuracy: 0.4984
21792/25000 [=========================>....] - ETA: 8s - loss: 7.6912 - accuracy: 0.4984
21824/25000 [=========================>....] - ETA: 8s - loss: 7.6898 - accuracy: 0.4985
21856/25000 [=========================>....] - ETA: 7s - loss: 7.6884 - accuracy: 0.4986
21888/25000 [=========================>....] - ETA: 7s - loss: 7.6897 - accuracy: 0.4985
21920/25000 [=========================>....] - ETA: 7s - loss: 7.6876 - accuracy: 0.4986
21952/25000 [=========================>....] - ETA: 7s - loss: 7.6876 - accuracy: 0.4986
21984/25000 [=========================>....] - ETA: 7s - loss: 7.6882 - accuracy: 0.4986
22016/25000 [=========================>....] - ETA: 7s - loss: 7.6868 - accuracy: 0.4987
22048/25000 [=========================>....] - ETA: 7s - loss: 7.6854 - accuracy: 0.4988
22080/25000 [=========================>....] - ETA: 7s - loss: 7.6847 - accuracy: 0.4988
22112/25000 [=========================>....] - ETA: 7s - loss: 7.6853 - accuracy: 0.4988
22144/25000 [=========================>....] - ETA: 7s - loss: 7.6853 - accuracy: 0.4988
22176/25000 [=========================>....] - ETA: 7s - loss: 7.6839 - accuracy: 0.4989
22208/25000 [=========================>....] - ETA: 7s - loss: 7.6853 - accuracy: 0.4988
22240/25000 [=========================>....] - ETA: 7s - loss: 7.6845 - accuracy: 0.4988
22272/25000 [=========================>....] - ETA: 6s - loss: 7.6852 - accuracy: 0.4988
22304/25000 [=========================>....] - ETA: 6s - loss: 7.6831 - accuracy: 0.4989
22336/25000 [=========================>....] - ETA: 6s - loss: 7.6810 - accuracy: 0.4991
22368/25000 [=========================>....] - ETA: 6s - loss: 7.6810 - accuracy: 0.4991
22400/25000 [=========================>....] - ETA: 6s - loss: 7.6789 - accuracy: 0.4992
22432/25000 [=========================>....] - ETA: 6s - loss: 7.6789 - accuracy: 0.4992
22464/25000 [=========================>....] - ETA: 6s - loss: 7.6789 - accuracy: 0.4992
22496/25000 [=========================>....] - ETA: 6s - loss: 7.6803 - accuracy: 0.4991
22528/25000 [==========================>...] - ETA: 6s - loss: 7.6809 - accuracy: 0.4991
22560/25000 [==========================>...] - ETA: 6s - loss: 7.6850 - accuracy: 0.4988
22592/25000 [==========================>...] - ETA: 6s - loss: 7.6849 - accuracy: 0.4988
22624/25000 [==========================>...] - ETA: 6s - loss: 7.6836 - accuracy: 0.4989
22656/25000 [==========================>...] - ETA: 5s - loss: 7.6842 - accuracy: 0.4989
22688/25000 [==========================>...] - ETA: 5s - loss: 7.6828 - accuracy: 0.4989
22720/25000 [==========================>...] - ETA: 5s - loss: 7.6835 - accuracy: 0.4989
22752/25000 [==========================>...] - ETA: 5s - loss: 7.6848 - accuracy: 0.4988
22784/25000 [==========================>...] - ETA: 5s - loss: 7.6834 - accuracy: 0.4989
22816/25000 [==========================>...] - ETA: 5s - loss: 7.6834 - accuracy: 0.4989
22848/25000 [==========================>...] - ETA: 5s - loss: 7.6787 - accuracy: 0.4992
22880/25000 [==========================>...] - ETA: 5s - loss: 7.6820 - accuracy: 0.4990
22912/25000 [==========================>...] - ETA: 5s - loss: 7.6834 - accuracy: 0.4989
22944/25000 [==========================>...] - ETA: 5s - loss: 7.6833 - accuracy: 0.4989
22976/25000 [==========================>...] - ETA: 5s - loss: 7.6800 - accuracy: 0.4991
23008/25000 [==========================>...] - ETA: 5s - loss: 7.6773 - accuracy: 0.4993
23040/25000 [==========================>...] - ETA: 4s - loss: 7.6786 - accuracy: 0.4992
23072/25000 [==========================>...] - ETA: 4s - loss: 7.6779 - accuracy: 0.4993
23104/25000 [==========================>...] - ETA: 4s - loss: 7.6812 - accuracy: 0.4990
23136/25000 [==========================>...] - ETA: 4s - loss: 7.6812 - accuracy: 0.4990
23168/25000 [==========================>...] - ETA: 4s - loss: 7.6792 - accuracy: 0.4992
23200/25000 [==========================>...] - ETA: 4s - loss: 7.6779 - accuracy: 0.4993
23232/25000 [==========================>...] - ETA: 4s - loss: 7.6778 - accuracy: 0.4993
23264/25000 [==========================>...] - ETA: 4s - loss: 7.6778 - accuracy: 0.4993
23296/25000 [==========================>...] - ETA: 4s - loss: 7.6745 - accuracy: 0.4995
23328/25000 [==========================>...] - ETA: 4s - loss: 7.6791 - accuracy: 0.4992
23360/25000 [===========================>..] - ETA: 4s - loss: 7.6824 - accuracy: 0.4990
23392/25000 [===========================>..] - ETA: 4s - loss: 7.6830 - accuracy: 0.4989
23424/25000 [===========================>..] - ETA: 4s - loss: 7.6836 - accuracy: 0.4989
23456/25000 [===========================>..] - ETA: 3s - loss: 7.6823 - accuracy: 0.4990
23488/25000 [===========================>..] - ETA: 3s - loss: 7.6810 - accuracy: 0.4991
23520/25000 [===========================>..] - ETA: 3s - loss: 7.6803 - accuracy: 0.4991
23552/25000 [===========================>..] - ETA: 3s - loss: 7.6803 - accuracy: 0.4991
23584/25000 [===========================>..] - ETA: 3s - loss: 7.6803 - accuracy: 0.4991
23616/25000 [===========================>..] - ETA: 3s - loss: 7.6777 - accuracy: 0.4993
23648/25000 [===========================>..] - ETA: 3s - loss: 7.6731 - accuracy: 0.4996
23680/25000 [===========================>..] - ETA: 3s - loss: 7.6686 - accuracy: 0.4999
23712/25000 [===========================>..] - ETA: 3s - loss: 7.6705 - accuracy: 0.4997
23744/25000 [===========================>..] - ETA: 3s - loss: 7.6686 - accuracy: 0.4999
23776/25000 [===========================>..] - ETA: 3s - loss: 7.6692 - accuracy: 0.4998
23808/25000 [===========================>..] - ETA: 3s - loss: 7.6698 - accuracy: 0.4998
23840/25000 [===========================>..] - ETA: 2s - loss: 7.6653 - accuracy: 0.5001
23872/25000 [===========================>..] - ETA: 2s - loss: 7.6634 - accuracy: 0.5002
23904/25000 [===========================>..] - ETA: 2s - loss: 7.6615 - accuracy: 0.5003
23936/25000 [===========================>..] - ETA: 2s - loss: 7.6628 - accuracy: 0.5003
23968/25000 [===========================>..] - ETA: 2s - loss: 7.6615 - accuracy: 0.5003
24000/25000 [===========================>..] - ETA: 2s - loss: 7.6615 - accuracy: 0.5003
24032/25000 [===========================>..] - ETA: 2s - loss: 7.6647 - accuracy: 0.5001
24064/25000 [===========================>..] - ETA: 2s - loss: 7.6647 - accuracy: 0.5001
24096/25000 [===========================>..] - ETA: 2s - loss: 7.6679 - accuracy: 0.4999
24128/25000 [===========================>..] - ETA: 2s - loss: 7.6692 - accuracy: 0.4998
24160/25000 [===========================>..] - ETA: 2s - loss: 7.6679 - accuracy: 0.4999
24192/25000 [============================>.] - ETA: 2s - loss: 7.6704 - accuracy: 0.4998
24224/25000 [============================>.] - ETA: 1s - loss: 7.6704 - accuracy: 0.4998
24256/25000 [============================>.] - ETA: 1s - loss: 7.6717 - accuracy: 0.4997
24288/25000 [============================>.] - ETA: 1s - loss: 7.6723 - accuracy: 0.4996
24320/25000 [============================>.] - ETA: 1s - loss: 7.6717 - accuracy: 0.4997
24352/25000 [============================>.] - ETA: 1s - loss: 7.6717 - accuracy: 0.4997
24384/25000 [============================>.] - ETA: 1s - loss: 7.6698 - accuracy: 0.4998
24416/25000 [============================>.] - ETA: 1s - loss: 7.6698 - accuracy: 0.4998
24448/25000 [============================>.] - ETA: 1s - loss: 7.6704 - accuracy: 0.4998
24480/25000 [============================>.] - ETA: 1s - loss: 7.6710 - accuracy: 0.4997
24512/25000 [============================>.] - ETA: 1s - loss: 7.6697 - accuracy: 0.4998
24544/25000 [============================>.] - ETA: 1s - loss: 7.6697 - accuracy: 0.4998
24576/25000 [============================>.] - ETA: 1s - loss: 7.6679 - accuracy: 0.4999
24608/25000 [============================>.] - ETA: 0s - loss: 7.6679 - accuracy: 0.4999
24640/25000 [============================>.] - ETA: 0s - loss: 7.6704 - accuracy: 0.4998
24672/25000 [============================>.] - ETA: 0s - loss: 7.6703 - accuracy: 0.4998
24704/25000 [============================>.] - ETA: 0s - loss: 7.6716 - accuracy: 0.4997
24736/25000 [============================>.] - ETA: 0s - loss: 7.6722 - accuracy: 0.4996
24768/25000 [============================>.] - ETA: 0s - loss: 7.6710 - accuracy: 0.4997
24800/25000 [============================>.] - ETA: 0s - loss: 7.6722 - accuracy: 0.4996
24832/25000 [============================>.] - ETA: 0s - loss: 7.6728 - accuracy: 0.4996
24864/25000 [============================>.] - ETA: 0s - loss: 7.6697 - accuracy: 0.4998
24896/25000 [============================>.] - ETA: 0s - loss: 7.6691 - accuracy: 0.4998
24928/25000 [============================>.] - ETA: 0s - loss: 7.6685 - accuracy: 0.4999
24960/25000 [============================>.] - ETA: 0s - loss: 7.6691 - accuracy: 0.4998
24992/25000 [============================>.] - ETA: 0s - loss: 7.6672 - accuracy: 0.5000
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

