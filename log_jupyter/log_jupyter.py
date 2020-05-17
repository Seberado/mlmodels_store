
  test_jupyter /home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json Namespace(config_file='/home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json', config_mode='test', do='test_jupyter', folder=None, log_file=None, save_folder='ztest/') 

  ml_test --do test_jupyter 





 ************************************************************************************************************************

 ******** TAG ::  {'github_repo_url': 'https://github.com/arita37/mlmodels/tree/76b7a81be9b27c2e92c4951280c0a8da664b997c', 'url_branch_file': 'https://github.com/arita37/mlmodels/blob/dev/', 'repo': 'arita37/mlmodels', 'branch': 'dev', 'sha': '76b7a81be9b27c2e92c4951280c0a8da664b997c', 'workflow': 'test_jupyter'}

 ******** GITHUB_WOKFLOW : https://github.com/arita37/mlmodels/actions?query=workflow%3Atest_jupyter

 ******** GITHUB_REPO_BRANCH : https://github.com/arita37/mlmodels/tree/dev/

 ******** GITHUB_REPO_URL : https://github.com/arita37/mlmodels/tree/76b7a81be9b27c2e92c4951280c0a8da664b997c

 ******** GITHUB_COMMIT_URL : https://github.com/arita37/mlmodels/commit/76b7a81be9b27c2e92c4951280c0a8da664b997c

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
	Data preprocessing and feature engineering runtime = 0.28s ...
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
Saving dataset/models/NeuralNetClassifier/trial_0_tabularNN.pkl
Finished Task with config: {'activation.choice': 0, 'dropout_prob': 0.1, 'embedding_size_factor': 1.0, 'layers.choice': 0, 'learning_rate': 0.0005, 'network_type.choice': 0, 'use_batchnorm.choice': 0, 'weight_decay': 1e-06} and reward: 0.3862
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\xb9\x99\x99\x99\x99\x99\x9aX\x15\x00\x00\x00embedding_size_factorq\x03G?\xf0\x00\x00\x00\x00\x00\x00X\r\x00\x00\x00layers.choiceq\x04K\x00X\r\x00\x00\x00learning_rateq\x05G?@bM\xd2\xf1\xa9\xfcX\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G>\xb0\xc6\xf7\xa0\xb5\xed\x8du.' and reward: 0.3862
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\xb9\x99\x99\x99\x99\x99\x9aX\x15\x00\x00\x00embedding_size_factorq\x03G?\xf0\x00\x00\x00\x00\x00\x00X\r\x00\x00\x00layers.choiceq\x04K\x00X\r\x00\x00\x00learning_rateq\x05G?@bM\xd2\xf1\xa9\xfcX\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G>\xb0\xc6\xf7\xa0\xb5\xed\x8du.' and reward: 0.3862
 40%|████      | 2/5 [00:55<01:23, 27.84s/it] 40%|████      | 2/5 [00:55<01:23, 27.84s/it]
Loading: dataset/models/NeuralNetClassifier/train_tabNNdataset.pkl
Loading: dataset/models/NeuralNetClassifier/validation_tabNNdataset.pkl
Saving dataset/models/NeuralNetClassifier/trial_1_tabularNN.pkl
Finished Task with config: {'activation.choice': 0, 'dropout_prob': 0.2650417233635454, 'embedding_size_factor': 1.2838689867252528, 'layers.choice': 2, 'learning_rate': 0.0002393638412400304, 'network_type.choice': 1, 'use_batchnorm.choice': 0, 'weight_decay': 7.631950819272812e-06} and reward: 0.3844
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\xd0\xf6q\x8f{\x00\x85X\x15\x00\x00\x00embedding_size_factorq\x03G?\xf4\x8a\xba4\xe5V\x81X\r\x00\x00\x00layers.choiceq\x04K\x02X\r\x00\x00\x00learning_rateq\x05G?/_\xb7\xbdl\xd2JX\x13\x00\x00\x00network_type.choiceq\x06K\x01X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G>\xe0\x01_Uc\x92\xf0u.' and reward: 0.3844
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\xd0\xf6q\x8f{\x00\x85X\x15\x00\x00\x00embedding_size_factorq\x03G?\xf4\x8a\xba4\xe5V\x81X\r\x00\x00\x00layers.choiceq\x04K\x02X\r\x00\x00\x00learning_rateq\x05G?/_\xb7\xbdl\xd2JX\x13\x00\x00\x00network_type.choiceq\x06K\x01X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G>\xe0\x01_Uc\x92\xf0u.' and reward: 0.3844
Please either provide filename or allow plot in get_training_curves
Time for Neural Network hyperparameter optimization: 114.01184129714966
Best hyperparameter configuration for Tabular Neural Network: 
{'activation.choice': 0, 'dropout_prob': 0.1, 'embedding_size_factor': 1.0, 'layers.choice': 0, 'learning_rate': 0.0005, 'network_type.choice': 0, 'use_batchnorm.choice': 0, 'weight_decay': 1e-06}
Saving dataset/models/trainer.pkl
Loading: dataset/models/NeuralNetClassifier/trial_0_tabularNN.pkl
Loading: dataset/models/NeuralNetClassifier/trial_1_tabularNN.pkl
Fitting model: weighted_ensemble_k0_l1 ... Training model for up to 119.72s of the 4.18s of remaining time.
Ensemble size: 69
Ensemble weights: 
[0.49275362 0.50724638]
	0.391	 = Validation accuracy score
	0.98s	 = Training runtime
	0.0s	 = Validation runtime
Saving dataset/models/weighted_ensemble_k0_l1/model.pkl
Saving dataset/models/trainer.pkl
Saving dataset/models/trainer.pkl
Saving dataset/models/trainer.pkl
AutoGluon training complete, total runtime = 117.02s ...
Loading: dataset/models/trainer.pkl
Loaded data from: https://autogluon.s3.amazonaws.com/datasets/Inc/test.csv | Columns = 15 / 15 | Rows = 9769 -> 9769
Loading: dataset/models/trainer.pkl
Loading: dataset/models/weighted_ensemble_k0_l1/model.pkl
Loading: dataset/models/NeuralNetClassifier/trial_0_tabularNN.pkl
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

  <mlmodels.model_tf.1_lstm.Model object at 0x7f7d6ff13ac8> 

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
 [ 0.03141199 -0.01018779 -0.01188385  0.1186894   0.02210121  0.05789975]
 [ 0.11257756  0.20386772 -0.19884248  0.04911641  0.02829061 -0.10141353]
 [-0.08608732 -0.24041751  0.11453547  0.23645425 -0.24964266 -0.05678106]
 [ 0.32068601  0.18445313  0.12633054 -0.00466641  0.01834493 -0.04575968]
 [ 0.38873377 -0.02575951  0.09600534  0.42739317 -0.24712606 -0.10560244]
 [-0.05108621  0.15388423  0.16738328  0.14452547 -0.17380294 -0.18453638]
 [ 0.37188429 -0.19222076 -0.06665063 -0.23552081  0.19647364 -0.0532699 ]
 [ 0.23269662 -0.12778313  0.05305666  0.22385307 -0.05909287  0.11435792]
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
{'loss': 0.3782574590295553, 'loss_history': []}

  #### Plot   ######################################################## 

  #### Save   ######################################################## 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/'}
Model saved in path: /home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm//model//model.ckpt

  #### Load   ######################################################## 
2020-05-17 15:16:42.144791: W tensorflow/core/framework/op_kernel.cc:1651] OP_REQUIRES failed at save_restore_v2_ops.cc:184 : Not found: Key Variable not found in checkpoint
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
{'loss': 0.43732018768787384, 'loss_history': []}

  #### Plot   ######################################################## 

  #### Save   ######################################################## 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/'}
Model saved in path: /home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm//model//model.ckpt

  #### Load   ######################################################## 
2020-05-17 15:16:43.390772: W tensorflow/core/framework/op_kernel.cc:1651] OP_REQUIRES failed at save_restore_v2_ops.cc:184 : Not found: Key Variable not found in checkpoint
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
 4235264/17464789 [======>.......................] - ETA: 0s
12083200/17464789 [===================>..........] - ETA: 0s
17465344/17464789 [==============================] - 0s 0us/step
Pad sequences (samples x time)...
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/math_grad.py:1424: where (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
2020-05-17 15:16:55.654831: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2020-05-17 15:16:55.659403: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2294680000 Hz
2020-05-17 15:16:55.659572: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x562658d5f0d0 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-17 15:16:55.659588: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py:422: The name tf.global_variables is deprecated. Please use tf.compat.v1.global_variables instead.

Train on 25000 samples, validate on 25000 samples
Epoch 1/1

   32/25000 [..............................] - ETA: 4:41 - loss: 9.1041 - accuracy: 0.4062
   64/25000 [..............................] - ETA: 3:02 - loss: 9.8229 - accuracy: 0.3594
   96/25000 [..............................] - ETA: 2:29 - loss: 8.7847 - accuracy: 0.4271
  128/25000 [..............................] - ETA: 2:13 - loss: 8.3854 - accuracy: 0.4531
  160/25000 [..............................] - ETA: 2:03 - loss: 8.4333 - accuracy: 0.4500
  192/25000 [..............................] - ETA: 1:56 - loss: 8.1458 - accuracy: 0.4688
  224/25000 [..............................] - ETA: 1:51 - loss: 8.2827 - accuracy: 0.4598
  256/25000 [..............................] - ETA: 1:48 - loss: 8.2656 - accuracy: 0.4609
  288/25000 [..............................] - ETA: 1:45 - loss: 8.3055 - accuracy: 0.4583
  320/25000 [..............................] - ETA: 1:43 - loss: 8.1458 - accuracy: 0.4688
  352/25000 [..............................] - ETA: 1:41 - loss: 8.2765 - accuracy: 0.4602
  384/25000 [..............................] - ETA: 1:39 - loss: 8.2656 - accuracy: 0.4609
  416/25000 [..............................] - ETA: 1:38 - loss: 8.1826 - accuracy: 0.4663
  448/25000 [..............................] - ETA: 1:37 - loss: 8.1800 - accuracy: 0.4665
  480/25000 [..............................] - ETA: 1:36 - loss: 8.0180 - accuracy: 0.4771
  512/25000 [..............................] - ETA: 1:35 - loss: 7.9960 - accuracy: 0.4785
  544/25000 [..............................] - ETA: 1:34 - loss: 7.9767 - accuracy: 0.4798
  576/25000 [..............................] - ETA: 1:34 - loss: 7.9861 - accuracy: 0.4792
  608/25000 [..............................] - ETA: 1:34 - loss: 7.9692 - accuracy: 0.4803
  640/25000 [..............................] - ETA: 1:33 - loss: 8.0500 - accuracy: 0.4750
  672/25000 [..............................] - ETA: 1:33 - loss: 7.9861 - accuracy: 0.4792
  704/25000 [..............................] - ETA: 1:33 - loss: 7.9715 - accuracy: 0.4801
  736/25000 [..............................] - ETA: 1:32 - loss: 7.9791 - accuracy: 0.4796
  768/25000 [..............................] - ETA: 1:32 - loss: 8.0260 - accuracy: 0.4766
  800/25000 [..............................] - ETA: 1:31 - loss: 8.0691 - accuracy: 0.4737
  832/25000 [..............................] - ETA: 1:31 - loss: 8.0536 - accuracy: 0.4748
  864/25000 [>.............................] - ETA: 1:30 - loss: 8.0748 - accuracy: 0.4734
  896/25000 [>.............................] - ETA: 1:30 - loss: 8.0602 - accuracy: 0.4743
  928/25000 [>.............................] - ETA: 1:30 - loss: 7.9806 - accuracy: 0.4795
  960/25000 [>.............................] - ETA: 1:30 - loss: 7.9701 - accuracy: 0.4802
  992/25000 [>.............................] - ETA: 1:30 - loss: 7.9603 - accuracy: 0.4808
 1024/25000 [>.............................] - ETA: 1:29 - loss: 7.9361 - accuracy: 0.4824
 1056/25000 [>.............................] - ETA: 1:29 - loss: 8.0006 - accuracy: 0.4782
 1088/25000 [>.............................] - ETA: 1:29 - loss: 7.9626 - accuracy: 0.4807
 1120/25000 [>.............................] - ETA: 1:29 - loss: 7.9130 - accuracy: 0.4839
 1152/25000 [>.............................] - ETA: 1:29 - loss: 7.9461 - accuracy: 0.4818
 1184/25000 [>.............................] - ETA: 1:29 - loss: 7.9515 - accuracy: 0.4814
 1216/25000 [>.............................] - ETA: 1:29 - loss: 7.8684 - accuracy: 0.4868
 1248/25000 [>.............................] - ETA: 1:28 - loss: 7.8263 - accuracy: 0.4896
 1280/25000 [>.............................] - ETA: 1:28 - loss: 7.7984 - accuracy: 0.4914
 1312/25000 [>.............................] - ETA: 1:28 - loss: 7.7952 - accuracy: 0.4916
 1344/25000 [>.............................] - ETA: 1:28 - loss: 7.8606 - accuracy: 0.4874
 1376/25000 [>.............................] - ETA: 1:27 - loss: 7.8672 - accuracy: 0.4869
 1408/25000 [>.............................] - ETA: 1:28 - loss: 7.8626 - accuracy: 0.4872
 1440/25000 [>.............................] - ETA: 1:27 - loss: 7.8263 - accuracy: 0.4896
 1472/25000 [>.............................] - ETA: 1:27 - loss: 7.7812 - accuracy: 0.4925
 1504/25000 [>.............................] - ETA: 1:27 - loss: 7.8603 - accuracy: 0.4874
 1536/25000 [>.............................] - ETA: 1:27 - loss: 7.8463 - accuracy: 0.4883
 1568/25000 [>.............................] - ETA: 1:27 - loss: 7.8524 - accuracy: 0.4879
 1600/25000 [>.............................] - ETA: 1:26 - loss: 7.8583 - accuracy: 0.4875
 1632/25000 [>.............................] - ETA: 1:26 - loss: 7.8733 - accuracy: 0.4865
 1664/25000 [>.............................] - ETA: 1:26 - loss: 7.9338 - accuracy: 0.4826
 1696/25000 [=>............................] - ETA: 1:26 - loss: 7.9288 - accuracy: 0.4829
 1728/25000 [=>............................] - ETA: 1:26 - loss: 7.8885 - accuracy: 0.4855
 1760/25000 [=>............................] - ETA: 1:25 - loss: 7.8757 - accuracy: 0.4864
 1792/25000 [=>............................] - ETA: 1:25 - loss: 7.8377 - accuracy: 0.4888
 1824/25000 [=>............................] - ETA: 1:25 - loss: 7.8095 - accuracy: 0.4907
 1856/25000 [=>............................] - ETA: 1:25 - loss: 7.8236 - accuracy: 0.4898
 1888/25000 [=>............................] - ETA: 1:25 - loss: 7.8372 - accuracy: 0.4889
 1920/25000 [=>............................] - ETA: 1:25 - loss: 7.8104 - accuracy: 0.4906
 1952/25000 [=>............................] - ETA: 1:25 - loss: 7.8002 - accuracy: 0.4913
 1984/25000 [=>............................] - ETA: 1:25 - loss: 7.8212 - accuracy: 0.4899
 2016/25000 [=>............................] - ETA: 1:24 - loss: 7.8339 - accuracy: 0.4891
 2048/25000 [=>............................] - ETA: 1:24 - loss: 7.8538 - accuracy: 0.4878
 2080/25000 [=>............................] - ETA: 1:24 - loss: 7.8362 - accuracy: 0.4889
 2112/25000 [=>............................] - ETA: 1:24 - loss: 7.8409 - accuracy: 0.4886
 2144/25000 [=>............................] - ETA: 1:23 - loss: 7.8383 - accuracy: 0.4888
 2176/25000 [=>............................] - ETA: 1:23 - loss: 7.8498 - accuracy: 0.4881
 2208/25000 [=>............................] - ETA: 1:23 - loss: 7.8819 - accuracy: 0.4860
 2240/25000 [=>............................] - ETA: 1:23 - loss: 7.8583 - accuracy: 0.4875
 2272/25000 [=>............................] - ETA: 1:23 - loss: 7.8758 - accuracy: 0.4864
 2304/25000 [=>............................] - ETA: 1:23 - loss: 7.8862 - accuracy: 0.4857
 2336/25000 [=>............................] - ETA: 1:22 - loss: 7.8504 - accuracy: 0.4880
 2368/25000 [=>............................] - ETA: 1:22 - loss: 7.8220 - accuracy: 0.4899
 2400/25000 [=>............................] - ETA: 1:22 - loss: 7.8327 - accuracy: 0.4892
 2432/25000 [=>............................] - ETA: 1:22 - loss: 7.7990 - accuracy: 0.4914
 2464/25000 [=>............................] - ETA: 1:22 - loss: 7.8097 - accuracy: 0.4907
 2496/25000 [=>............................] - ETA: 1:22 - loss: 7.8263 - accuracy: 0.4896
 2528/25000 [==>...........................] - ETA: 1:21 - loss: 7.8122 - accuracy: 0.4905
 2560/25000 [==>...........................] - ETA: 1:21 - loss: 7.8223 - accuracy: 0.4898
 2592/25000 [==>...........................] - ETA: 1:21 - loss: 7.8027 - accuracy: 0.4911
 2624/25000 [==>...........................] - ETA: 1:21 - loss: 7.7835 - accuracy: 0.4924
 2656/25000 [==>...........................] - ETA: 1:21 - loss: 7.7821 - accuracy: 0.4925
 2688/25000 [==>...........................] - ETA: 1:21 - loss: 7.7864 - accuracy: 0.4922
 2720/25000 [==>...........................] - ETA: 1:20 - loss: 7.7794 - accuracy: 0.4926
 2752/25000 [==>...........................] - ETA: 1:20 - loss: 7.7558 - accuracy: 0.4942
 2784/25000 [==>...........................] - ETA: 1:20 - loss: 7.7382 - accuracy: 0.4953
 2816/25000 [==>...........................] - ETA: 1:20 - loss: 7.7429 - accuracy: 0.4950
 2848/25000 [==>...........................] - ETA: 1:20 - loss: 7.7474 - accuracy: 0.4947
 2880/25000 [==>...........................] - ETA: 1:20 - loss: 7.7358 - accuracy: 0.4955
 2912/25000 [==>...........................] - ETA: 1:20 - loss: 7.7561 - accuracy: 0.4942
 2944/25000 [==>...........................] - ETA: 1:19 - loss: 7.7916 - accuracy: 0.4918
 2976/25000 [==>...........................] - ETA: 1:19 - loss: 7.7954 - accuracy: 0.4916
 3008/25000 [==>...........................] - ETA: 1:19 - loss: 7.7890 - accuracy: 0.4920
 3040/25000 [==>...........................] - ETA: 1:19 - loss: 7.8179 - accuracy: 0.4901
 3072/25000 [==>...........................] - ETA: 1:19 - loss: 7.8313 - accuracy: 0.4893
 3104/25000 [==>...........................] - ETA: 1:19 - loss: 7.8198 - accuracy: 0.4900
 3136/25000 [==>...........................] - ETA: 1:19 - loss: 7.8133 - accuracy: 0.4904
 3168/25000 [==>...........................] - ETA: 1:19 - loss: 7.7876 - accuracy: 0.4921
 3200/25000 [==>...........................] - ETA: 1:18 - loss: 7.7768 - accuracy: 0.4928
 3232/25000 [==>...........................] - ETA: 1:18 - loss: 7.7757 - accuracy: 0.4929
 3264/25000 [==>...........................] - ETA: 1:18 - loss: 7.7794 - accuracy: 0.4926
 3296/25000 [==>...........................] - ETA: 1:18 - loss: 7.7922 - accuracy: 0.4918
 3328/25000 [==>...........................] - ETA: 1:18 - loss: 7.8048 - accuracy: 0.4910
 3360/25000 [===>..........................] - ETA: 1:18 - loss: 7.7853 - accuracy: 0.4923
 3392/25000 [===>..........................] - ETA: 1:18 - loss: 7.8022 - accuracy: 0.4912
 3424/25000 [===>..........................] - ETA: 1:18 - loss: 7.7920 - accuracy: 0.4918
 3456/25000 [===>..........................] - ETA: 1:17 - loss: 7.7908 - accuracy: 0.4919
 3488/25000 [===>..........................] - ETA: 1:17 - loss: 7.8073 - accuracy: 0.4908
 3520/25000 [===>..........................] - ETA: 1:17 - loss: 7.7799 - accuracy: 0.4926
 3552/25000 [===>..........................] - ETA: 1:17 - loss: 7.8004 - accuracy: 0.4913
 3584/25000 [===>..........................] - ETA: 1:17 - loss: 7.8078 - accuracy: 0.4908
 3616/25000 [===>..........................] - ETA: 1:17 - loss: 7.8235 - accuracy: 0.4898
 3648/25000 [===>..........................] - ETA: 1:17 - loss: 7.8263 - accuracy: 0.4896
 3680/25000 [===>..........................] - ETA: 1:17 - loss: 7.8250 - accuracy: 0.4897
 3712/25000 [===>..........................] - ETA: 1:17 - loss: 7.8195 - accuracy: 0.4900
 3744/25000 [===>..........................] - ETA: 1:16 - loss: 7.8304 - accuracy: 0.4893
 3776/25000 [===>..........................] - ETA: 1:16 - loss: 7.8087 - accuracy: 0.4907
 3808/25000 [===>..........................] - ETA: 1:16 - loss: 7.7914 - accuracy: 0.4919
 3840/25000 [===>..........................] - ETA: 1:16 - loss: 7.7984 - accuracy: 0.4914
 3872/25000 [===>..........................] - ETA: 1:16 - loss: 7.7894 - accuracy: 0.4920
 3904/25000 [===>..........................] - ETA: 1:16 - loss: 7.7923 - accuracy: 0.4918
 3936/25000 [===>..........................] - ETA: 1:16 - loss: 7.7640 - accuracy: 0.4936
 3968/25000 [===>..........................] - ETA: 1:15 - loss: 7.7478 - accuracy: 0.4947
 4000/25000 [===>..........................] - ETA: 1:15 - loss: 7.7433 - accuracy: 0.4950
 4032/25000 [===>..........................] - ETA: 1:15 - loss: 7.7313 - accuracy: 0.4958
 4064/25000 [===>..........................] - ETA: 1:15 - loss: 7.7194 - accuracy: 0.4966
 4096/25000 [===>..........................] - ETA: 1:15 - loss: 7.7265 - accuracy: 0.4961
 4128/25000 [===>..........................] - ETA: 1:15 - loss: 7.7298 - accuracy: 0.4959
 4160/25000 [===>..........................] - ETA: 1:15 - loss: 7.7403 - accuracy: 0.4952
 4192/25000 [====>.........................] - ETA: 1:15 - loss: 7.7398 - accuracy: 0.4952
 4224/25000 [====>.........................] - ETA: 1:14 - loss: 7.7465 - accuracy: 0.4948
 4256/25000 [====>.........................] - ETA: 1:14 - loss: 7.7351 - accuracy: 0.4955
 4288/25000 [====>.........................] - ETA: 1:14 - loss: 7.7274 - accuracy: 0.4960
 4320/25000 [====>.........................] - ETA: 1:14 - loss: 7.7270 - accuracy: 0.4961
 4352/25000 [====>.........................] - ETA: 1:14 - loss: 7.7159 - accuracy: 0.4968
 4384/25000 [====>.........................] - ETA: 1:14 - loss: 7.7156 - accuracy: 0.4968
 4416/25000 [====>.........................] - ETA: 1:14 - loss: 7.7222 - accuracy: 0.4964
 4448/25000 [====>.........................] - ETA: 1:14 - loss: 7.7183 - accuracy: 0.4966
 4480/25000 [====>.........................] - ETA: 1:13 - loss: 7.7145 - accuracy: 0.4969
 4512/25000 [====>.........................] - ETA: 1:13 - loss: 7.7108 - accuracy: 0.4971
 4544/25000 [====>.........................] - ETA: 1:13 - loss: 7.7037 - accuracy: 0.4976
 4576/25000 [====>.........................] - ETA: 1:13 - loss: 7.7102 - accuracy: 0.4972
 4608/25000 [====>.........................] - ETA: 1:13 - loss: 7.7132 - accuracy: 0.4970
 4640/25000 [====>.........................] - ETA: 1:13 - loss: 7.7096 - accuracy: 0.4972
 4672/25000 [====>.........................] - ETA: 1:13 - loss: 7.7224 - accuracy: 0.4964
 4704/25000 [====>.........................] - ETA: 1:12 - loss: 7.7188 - accuracy: 0.4966
 4736/25000 [====>.........................] - ETA: 1:12 - loss: 7.7217 - accuracy: 0.4964
 4768/25000 [====>.........................] - ETA: 1:12 - loss: 7.7277 - accuracy: 0.4960
 4800/25000 [====>.........................] - ETA: 1:12 - loss: 7.7273 - accuracy: 0.4960
 4832/25000 [====>.........................] - ETA: 1:12 - loss: 7.7206 - accuracy: 0.4965
 4864/25000 [====>.........................] - ETA: 1:12 - loss: 7.7076 - accuracy: 0.4973
 4896/25000 [====>.........................] - ETA: 1:12 - loss: 7.6979 - accuracy: 0.4980
 4928/25000 [====>.........................] - ETA: 1:12 - loss: 7.6946 - accuracy: 0.4982
 4960/25000 [====>.........................] - ETA: 1:11 - loss: 7.6975 - accuracy: 0.4980
 4992/25000 [====>.........................] - ETA: 1:11 - loss: 7.7035 - accuracy: 0.4976
 5024/25000 [=====>........................] - ETA: 1:11 - loss: 7.7063 - accuracy: 0.4974
 5056/25000 [=====>........................] - ETA: 1:11 - loss: 7.7121 - accuracy: 0.4970
 5088/25000 [=====>........................] - ETA: 1:11 - loss: 7.6968 - accuracy: 0.4980
 5120/25000 [=====>........................] - ETA: 1:11 - loss: 7.7056 - accuracy: 0.4975
 5152/25000 [=====>........................] - ETA: 1:11 - loss: 7.7053 - accuracy: 0.4975
 5184/25000 [=====>........................] - ETA: 1:10 - loss: 7.7199 - accuracy: 0.4965
 5216/25000 [=====>........................] - ETA: 1:10 - loss: 7.7284 - accuracy: 0.4960
 5248/25000 [=====>........................] - ETA: 1:10 - loss: 7.7221 - accuracy: 0.4964
 5280/25000 [=====>........................] - ETA: 1:10 - loss: 7.7218 - accuracy: 0.4964
 5312/25000 [=====>........................] - ETA: 1:10 - loss: 7.7186 - accuracy: 0.4966
 5344/25000 [=====>........................] - ETA: 1:10 - loss: 7.7183 - accuracy: 0.4966
 5376/25000 [=====>........................] - ETA: 1:10 - loss: 7.7151 - accuracy: 0.4968
 5408/25000 [=====>........................] - ETA: 1:10 - loss: 7.7120 - accuracy: 0.4970
 5440/25000 [=====>........................] - ETA: 1:09 - loss: 7.7061 - accuracy: 0.4974
 5472/25000 [=====>........................] - ETA: 1:09 - loss: 7.7087 - accuracy: 0.4973
 5504/25000 [=====>........................] - ETA: 1:09 - loss: 7.7084 - accuracy: 0.4973
 5536/25000 [=====>........................] - ETA: 1:09 - loss: 7.7082 - accuracy: 0.4973
 5568/25000 [=====>........................] - ETA: 1:09 - loss: 7.7162 - accuracy: 0.4968
 5600/25000 [=====>........................] - ETA: 1:09 - loss: 7.7241 - accuracy: 0.4963
 5632/25000 [=====>........................] - ETA: 1:09 - loss: 7.7238 - accuracy: 0.4963
 5664/25000 [=====>........................] - ETA: 1:09 - loss: 7.7181 - accuracy: 0.4966
 5696/25000 [=====>........................] - ETA: 1:08 - loss: 7.7097 - accuracy: 0.4972
 5728/25000 [=====>........................] - ETA: 1:08 - loss: 7.7202 - accuracy: 0.4965
 5760/25000 [=====>........................] - ETA: 1:08 - loss: 7.7172 - accuracy: 0.4967
 5792/25000 [=====>........................] - ETA: 1:08 - loss: 7.7222 - accuracy: 0.4964
 5824/25000 [=====>........................] - ETA: 1:08 - loss: 7.7430 - accuracy: 0.4950
 5856/25000 [======>.......................] - ETA: 1:08 - loss: 7.7347 - accuracy: 0.4956
 5888/25000 [======>.......................] - ETA: 1:08 - loss: 7.7317 - accuracy: 0.4958
 5920/25000 [======>.......................] - ETA: 1:08 - loss: 7.7469 - accuracy: 0.4948
 5952/25000 [======>.......................] - ETA: 1:07 - loss: 7.7413 - accuracy: 0.4951
 5984/25000 [======>.......................] - ETA: 1:07 - loss: 7.7332 - accuracy: 0.4957
 6016/25000 [======>.......................] - ETA: 1:07 - loss: 7.7227 - accuracy: 0.4963
 6048/25000 [======>.......................] - ETA: 1:07 - loss: 7.7199 - accuracy: 0.4965
 6080/25000 [======>.......................] - ETA: 1:07 - loss: 7.7196 - accuracy: 0.4965
 6112/25000 [======>.......................] - ETA: 1:07 - loss: 7.7168 - accuracy: 0.4967
 6144/25000 [======>.......................] - ETA: 1:07 - loss: 7.7016 - accuracy: 0.4977
 6176/25000 [======>.......................] - ETA: 1:07 - loss: 7.6989 - accuracy: 0.4979
 6208/25000 [======>.......................] - ETA: 1:06 - loss: 7.6963 - accuracy: 0.4981
 6240/25000 [======>.......................] - ETA: 1:06 - loss: 7.6912 - accuracy: 0.4984
 6272/25000 [======>.......................] - ETA: 1:06 - loss: 7.6886 - accuracy: 0.4986
 6304/25000 [======>.......................] - ETA: 1:06 - loss: 7.7007 - accuracy: 0.4978
 6336/25000 [======>.......................] - ETA: 1:06 - loss: 7.7029 - accuracy: 0.4976
 6368/25000 [======>.......................] - ETA: 1:06 - loss: 7.6979 - accuracy: 0.4980
 6400/25000 [======>.......................] - ETA: 1:06 - loss: 7.6978 - accuracy: 0.4980
 6432/25000 [======>.......................] - ETA: 1:06 - loss: 7.6976 - accuracy: 0.4980
 6464/25000 [======>.......................] - ETA: 1:05 - loss: 7.6832 - accuracy: 0.4989
 6496/25000 [======>.......................] - ETA: 1:05 - loss: 7.6737 - accuracy: 0.4995
 6528/25000 [======>.......................] - ETA: 1:05 - loss: 7.6737 - accuracy: 0.4995
 6560/25000 [======>.......................] - ETA: 1:05 - loss: 7.6783 - accuracy: 0.4992
 6592/25000 [======>.......................] - ETA: 1:05 - loss: 7.6806 - accuracy: 0.4991
 6624/25000 [======>.......................] - ETA: 1:05 - loss: 7.6851 - accuracy: 0.4988
 6656/25000 [======>.......................] - ETA: 1:05 - loss: 7.6897 - accuracy: 0.4985
 6688/25000 [=======>......................] - ETA: 1:05 - loss: 7.6827 - accuracy: 0.4990
 6720/25000 [=======>......................] - ETA: 1:05 - loss: 7.6780 - accuracy: 0.4993
 6752/25000 [=======>......................] - ETA: 1:04 - loss: 7.6802 - accuracy: 0.4991
 6784/25000 [=======>......................] - ETA: 1:04 - loss: 7.6757 - accuracy: 0.4994
 6816/25000 [=======>......................] - ETA: 1:04 - loss: 7.6756 - accuracy: 0.4994
 6848/25000 [=======>......................] - ETA: 1:04 - loss: 7.6778 - accuracy: 0.4993
 6880/25000 [=======>......................] - ETA: 1:04 - loss: 7.6688 - accuracy: 0.4999
 6912/25000 [=======>......................] - ETA: 1:04 - loss: 7.6688 - accuracy: 0.4999
 6944/25000 [=======>......................] - ETA: 1:04 - loss: 7.6644 - accuracy: 0.5001
 6976/25000 [=======>......................] - ETA: 1:03 - loss: 7.6534 - accuracy: 0.5009
 7008/25000 [=======>......................] - ETA: 1:03 - loss: 7.6491 - accuracy: 0.5011
 7040/25000 [=======>......................] - ETA: 1:03 - loss: 7.6405 - accuracy: 0.5017
 7072/25000 [=======>......................] - ETA: 1:03 - loss: 7.6406 - accuracy: 0.5017
 7104/25000 [=======>......................] - ETA: 1:03 - loss: 7.6364 - accuracy: 0.5020
 7136/25000 [=======>......................] - ETA: 1:03 - loss: 7.6473 - accuracy: 0.5013
 7168/25000 [=======>......................] - ETA: 1:03 - loss: 7.6452 - accuracy: 0.5014
 7200/25000 [=======>......................] - ETA: 1:03 - loss: 7.6453 - accuracy: 0.5014
 7232/25000 [=======>......................] - ETA: 1:03 - loss: 7.6391 - accuracy: 0.5018
 7264/25000 [=======>......................] - ETA: 1:02 - loss: 7.6307 - accuracy: 0.5023
 7296/25000 [=======>......................] - ETA: 1:02 - loss: 7.6393 - accuracy: 0.5018
 7328/25000 [=======>......................] - ETA: 1:02 - loss: 7.6436 - accuracy: 0.5015
 7360/25000 [=======>......................] - ETA: 1:02 - loss: 7.6416 - accuracy: 0.5016
 7392/25000 [=======>......................] - ETA: 1:02 - loss: 7.6438 - accuracy: 0.5015
 7424/25000 [=======>......................] - ETA: 1:02 - loss: 7.6439 - accuracy: 0.5015
 7456/25000 [=======>......................] - ETA: 1:02 - loss: 7.6461 - accuracy: 0.5013
 7488/25000 [=======>......................] - ETA: 1:02 - loss: 7.6441 - accuracy: 0.5015
 7520/25000 [========>.....................] - ETA: 1:01 - loss: 7.6360 - accuracy: 0.5020
 7552/25000 [========>.....................] - ETA: 1:01 - loss: 7.6362 - accuracy: 0.5020
 7584/25000 [========>.....................] - ETA: 1:01 - loss: 7.6363 - accuracy: 0.5020
 7616/25000 [========>.....................] - ETA: 1:01 - loss: 7.6384 - accuracy: 0.5018
 7648/25000 [========>.....................] - ETA: 1:01 - loss: 7.6446 - accuracy: 0.5014
 7680/25000 [========>.....................] - ETA: 1:01 - loss: 7.6467 - accuracy: 0.5013
 7712/25000 [========>.....................] - ETA: 1:01 - loss: 7.6467 - accuracy: 0.5013
 7744/25000 [========>.....................] - ETA: 1:01 - loss: 7.6448 - accuracy: 0.5014
 7776/25000 [========>.....................] - ETA: 1:00 - loss: 7.6410 - accuracy: 0.5017
 7808/25000 [========>.....................] - ETA: 1:00 - loss: 7.6313 - accuracy: 0.5023
 7840/25000 [========>.....................] - ETA: 1:00 - loss: 7.6275 - accuracy: 0.5026
 7872/25000 [========>.....................] - ETA: 1:00 - loss: 7.6257 - accuracy: 0.5027
 7904/25000 [========>.....................] - ETA: 1:00 - loss: 7.6220 - accuracy: 0.5029
 7936/25000 [========>.....................] - ETA: 1:00 - loss: 7.6241 - accuracy: 0.5028
 7968/25000 [========>.....................] - ETA: 1:00 - loss: 7.6147 - accuracy: 0.5034
 8000/25000 [========>.....................] - ETA: 1:00 - loss: 7.6149 - accuracy: 0.5034
 8032/25000 [========>.....................] - ETA: 1:00 - loss: 7.6132 - accuracy: 0.5035
 8064/25000 [========>.....................] - ETA: 59s - loss: 7.6077 - accuracy: 0.5038 
 8096/25000 [========>.....................] - ETA: 59s - loss: 7.6060 - accuracy: 0.5040
 8128/25000 [========>.....................] - ETA: 59s - loss: 7.6081 - accuracy: 0.5038
 8160/25000 [========>.....................] - ETA: 59s - loss: 7.5952 - accuracy: 0.5047
 8192/25000 [========>.....................] - ETA: 59s - loss: 7.5955 - accuracy: 0.5046
 8224/25000 [========>.....................] - ETA: 59s - loss: 7.6014 - accuracy: 0.5043
 8256/25000 [========>.....................] - ETA: 59s - loss: 7.6090 - accuracy: 0.5038
 8288/25000 [========>.....................] - ETA: 59s - loss: 7.6037 - accuracy: 0.5041
 8320/25000 [========>.....................] - ETA: 58s - loss: 7.6040 - accuracy: 0.5041
 8352/25000 [=========>....................] - ETA: 58s - loss: 7.6042 - accuracy: 0.5041
 8384/25000 [=========>....................] - ETA: 58s - loss: 7.6099 - accuracy: 0.5037
 8416/25000 [=========>....................] - ETA: 58s - loss: 7.6029 - accuracy: 0.5042
 8448/25000 [=========>....................] - ETA: 58s - loss: 7.6158 - accuracy: 0.5033
 8480/25000 [=========>....................] - ETA: 58s - loss: 7.6232 - accuracy: 0.5028
 8512/25000 [=========>....................] - ETA: 58s - loss: 7.6252 - accuracy: 0.5027
 8544/25000 [=========>....................] - ETA: 58s - loss: 7.6200 - accuracy: 0.5030
 8576/25000 [=========>....................] - ETA: 58s - loss: 7.6183 - accuracy: 0.5031
 8608/25000 [=========>....................] - ETA: 57s - loss: 7.6150 - accuracy: 0.5034
 8640/25000 [=========>....................] - ETA: 57s - loss: 7.6098 - accuracy: 0.5037
 8672/25000 [=========>....................] - ETA: 57s - loss: 7.6118 - accuracy: 0.5036
 8704/25000 [=========>....................] - ETA: 57s - loss: 7.6120 - accuracy: 0.5036
 8736/25000 [=========>....................] - ETA: 57s - loss: 7.6069 - accuracy: 0.5039
 8768/25000 [=========>....................] - ETA: 57s - loss: 7.6019 - accuracy: 0.5042
 8800/25000 [=========>....................] - ETA: 57s - loss: 7.6004 - accuracy: 0.5043
 8832/25000 [=========>....................] - ETA: 57s - loss: 7.5972 - accuracy: 0.5045
 8864/25000 [=========>....................] - ETA: 57s - loss: 7.5836 - accuracy: 0.5054
 8896/25000 [=========>....................] - ETA: 56s - loss: 7.5891 - accuracy: 0.5051
 8928/25000 [=========>....................] - ETA: 56s - loss: 7.5859 - accuracy: 0.5053
 8960/25000 [=========>....................] - ETA: 56s - loss: 7.5845 - accuracy: 0.5054
 8992/25000 [=========>....................] - ETA: 56s - loss: 7.5848 - accuracy: 0.5053
 9024/25000 [=========>....................] - ETA: 56s - loss: 7.5851 - accuracy: 0.5053
 9056/25000 [=========>....................] - ETA: 56s - loss: 7.5853 - accuracy: 0.5053
 9088/25000 [=========>....................] - ETA: 56s - loss: 7.5924 - accuracy: 0.5048
 9120/25000 [=========>....................] - ETA: 56s - loss: 7.5910 - accuracy: 0.5049
 9152/25000 [=========>....................] - ETA: 56s - loss: 7.5879 - accuracy: 0.5051
 9184/25000 [==========>...................] - ETA: 55s - loss: 7.5932 - accuracy: 0.5048
 9216/25000 [==========>...................] - ETA: 55s - loss: 7.5901 - accuracy: 0.5050
 9248/25000 [==========>...................] - ETA: 55s - loss: 7.5870 - accuracy: 0.5052
 9280/25000 [==========>...................] - ETA: 55s - loss: 7.5857 - accuracy: 0.5053
 9312/25000 [==========>...................] - ETA: 55s - loss: 7.5876 - accuracy: 0.5052
 9344/25000 [==========>...................] - ETA: 55s - loss: 7.5895 - accuracy: 0.5050
 9376/25000 [==========>...................] - ETA: 55s - loss: 7.5865 - accuracy: 0.5052
 9408/25000 [==========>...................] - ETA: 55s - loss: 7.5884 - accuracy: 0.5051
 9440/25000 [==========>...................] - ETA: 54s - loss: 7.5887 - accuracy: 0.5051
 9472/25000 [==========>...................] - ETA: 54s - loss: 7.5922 - accuracy: 0.5049
 9504/25000 [==========>...................] - ETA: 54s - loss: 7.5892 - accuracy: 0.5051
 9536/25000 [==========>...................] - ETA: 54s - loss: 7.5927 - accuracy: 0.5048
 9568/25000 [==========>...................] - ETA: 54s - loss: 7.5913 - accuracy: 0.5049
 9600/25000 [==========>...................] - ETA: 54s - loss: 7.5884 - accuracy: 0.5051
 9632/25000 [==========>...................] - ETA: 54s - loss: 7.5854 - accuracy: 0.5053
 9664/25000 [==========>...................] - ETA: 54s - loss: 7.5873 - accuracy: 0.5052
 9696/25000 [==========>...................] - ETA: 54s - loss: 7.5923 - accuracy: 0.5048
 9728/25000 [==========>...................] - ETA: 53s - loss: 7.5878 - accuracy: 0.5051
 9760/25000 [==========>...................] - ETA: 53s - loss: 7.5818 - accuracy: 0.5055
 9792/25000 [==========>...................] - ETA: 53s - loss: 7.5836 - accuracy: 0.5054
 9824/25000 [==========>...................] - ETA: 53s - loss: 7.5855 - accuracy: 0.5053
 9856/25000 [==========>...................] - ETA: 53s - loss: 7.5904 - accuracy: 0.5050
 9888/25000 [==========>...................] - ETA: 53s - loss: 7.5906 - accuracy: 0.5050
 9920/25000 [==========>...................] - ETA: 53s - loss: 7.5955 - accuracy: 0.5046
 9952/25000 [==========>...................] - ETA: 53s - loss: 7.5973 - accuracy: 0.5045
 9984/25000 [==========>...................] - ETA: 53s - loss: 7.6021 - accuracy: 0.5042
10016/25000 [===========>..................] - ETA: 52s - loss: 7.6039 - accuracy: 0.5041
10048/25000 [===========>..................] - ETA: 52s - loss: 7.6025 - accuracy: 0.5042
10080/25000 [===========>..................] - ETA: 52s - loss: 7.6027 - accuracy: 0.5042
10112/25000 [===========>..................] - ETA: 52s - loss: 7.6075 - accuracy: 0.5039
10144/25000 [===========>..................] - ETA: 52s - loss: 7.6092 - accuracy: 0.5037
10176/25000 [===========>..................] - ETA: 52s - loss: 7.6139 - accuracy: 0.5034
10208/25000 [===========>..................] - ETA: 52s - loss: 7.6171 - accuracy: 0.5032
10240/25000 [===========>..................] - ETA: 52s - loss: 7.6217 - accuracy: 0.5029
10272/25000 [===========>..................] - ETA: 52s - loss: 7.6248 - accuracy: 0.5027
10304/25000 [===========>..................] - ETA: 51s - loss: 7.6250 - accuracy: 0.5027
10336/25000 [===========>..................] - ETA: 51s - loss: 7.6280 - accuracy: 0.5025
10368/25000 [===========>..................] - ETA: 51s - loss: 7.6341 - accuracy: 0.5021
10400/25000 [===========>..................] - ETA: 51s - loss: 7.6342 - accuracy: 0.5021
10432/25000 [===========>..................] - ETA: 51s - loss: 7.6387 - accuracy: 0.5018
10464/25000 [===========>..................] - ETA: 51s - loss: 7.6417 - accuracy: 0.5016
10496/25000 [===========>..................] - ETA: 51s - loss: 7.6389 - accuracy: 0.5018
10528/25000 [===========>..................] - ETA: 51s - loss: 7.6317 - accuracy: 0.5023
10560/25000 [===========>..................] - ETA: 51s - loss: 7.6318 - accuracy: 0.5023
10592/25000 [===========>..................] - ETA: 50s - loss: 7.6319 - accuracy: 0.5023
10624/25000 [===========>..................] - ETA: 50s - loss: 7.6349 - accuracy: 0.5021
10656/25000 [===========>..................] - ETA: 50s - loss: 7.6335 - accuracy: 0.5022
10688/25000 [===========>..................] - ETA: 50s - loss: 7.6351 - accuracy: 0.5021
10720/25000 [===========>..................] - ETA: 50s - loss: 7.6437 - accuracy: 0.5015
10752/25000 [===========>..................] - ETA: 50s - loss: 7.6452 - accuracy: 0.5014
10784/25000 [===========>..................] - ETA: 50s - loss: 7.6439 - accuracy: 0.5015
10816/25000 [===========>..................] - ETA: 50s - loss: 7.6397 - accuracy: 0.5018
10848/25000 [============>.................] - ETA: 49s - loss: 7.6398 - accuracy: 0.5018
10880/25000 [============>.................] - ETA: 49s - loss: 7.6370 - accuracy: 0.5019
10912/25000 [============>.................] - ETA: 49s - loss: 7.6441 - accuracy: 0.5015
10944/25000 [============>.................] - ETA: 49s - loss: 7.6414 - accuracy: 0.5016
10976/25000 [============>.................] - ETA: 49s - loss: 7.6485 - accuracy: 0.5012
11008/25000 [============>.................] - ETA: 49s - loss: 7.6485 - accuracy: 0.5012
11040/25000 [============>.................] - ETA: 49s - loss: 7.6458 - accuracy: 0.5014
11072/25000 [============>.................] - ETA: 49s - loss: 7.6486 - accuracy: 0.5012
11104/25000 [============>.................] - ETA: 49s - loss: 7.6487 - accuracy: 0.5012
11136/25000 [============>.................] - ETA: 48s - loss: 7.6473 - accuracy: 0.5013
11168/25000 [============>.................] - ETA: 48s - loss: 7.6447 - accuracy: 0.5014
11200/25000 [============>.................] - ETA: 48s - loss: 7.6420 - accuracy: 0.5016
11232/25000 [============>.................] - ETA: 48s - loss: 7.6489 - accuracy: 0.5012
11264/25000 [============>.................] - ETA: 48s - loss: 7.6503 - accuracy: 0.5011
11296/25000 [============>.................] - ETA: 48s - loss: 7.6558 - accuracy: 0.5007
11328/25000 [============>.................] - ETA: 48s - loss: 7.6517 - accuracy: 0.5010
11360/25000 [============>.................] - ETA: 48s - loss: 7.6531 - accuracy: 0.5009
11392/25000 [============>.................] - ETA: 48s - loss: 7.6518 - accuracy: 0.5010
11424/25000 [============>.................] - ETA: 47s - loss: 7.6572 - accuracy: 0.5006
11456/25000 [============>.................] - ETA: 47s - loss: 7.6599 - accuracy: 0.5004
11488/25000 [============>.................] - ETA: 47s - loss: 7.6586 - accuracy: 0.5005
11520/25000 [============>.................] - ETA: 47s - loss: 7.6586 - accuracy: 0.5005
11552/25000 [============>.................] - ETA: 47s - loss: 7.6494 - accuracy: 0.5011
11584/25000 [============>.................] - ETA: 47s - loss: 7.6481 - accuracy: 0.5012
11616/25000 [============>.................] - ETA: 47s - loss: 7.6455 - accuracy: 0.5014
11648/25000 [============>.................] - ETA: 47s - loss: 7.6482 - accuracy: 0.5012
11680/25000 [=============>................] - ETA: 46s - loss: 7.6535 - accuracy: 0.5009
11712/25000 [=============>................] - ETA: 46s - loss: 7.6561 - accuracy: 0.5007
11744/25000 [=============>................] - ETA: 46s - loss: 7.6523 - accuracy: 0.5009
11776/25000 [=============>................] - ETA: 46s - loss: 7.6523 - accuracy: 0.5009
11808/25000 [=============>................] - ETA: 46s - loss: 7.6575 - accuracy: 0.5006
11840/25000 [=============>................] - ETA: 46s - loss: 7.6614 - accuracy: 0.5003
11872/25000 [=============>................] - ETA: 46s - loss: 7.6627 - accuracy: 0.5003
11904/25000 [=============>................] - ETA: 46s - loss: 7.6640 - accuracy: 0.5002
11936/25000 [=============>................] - ETA: 46s - loss: 7.6628 - accuracy: 0.5003
11968/25000 [=============>................] - ETA: 45s - loss: 7.6589 - accuracy: 0.5005
12000/25000 [=============>................] - ETA: 45s - loss: 7.6602 - accuracy: 0.5004
12032/25000 [=============>................] - ETA: 45s - loss: 7.6602 - accuracy: 0.5004
12064/25000 [=============>................] - ETA: 45s - loss: 7.6603 - accuracy: 0.5004
12096/25000 [=============>................] - ETA: 45s - loss: 7.6615 - accuracy: 0.5003
12128/25000 [=============>................] - ETA: 45s - loss: 7.6654 - accuracy: 0.5001
12160/25000 [=============>................] - ETA: 45s - loss: 7.6654 - accuracy: 0.5001
12192/25000 [=============>................] - ETA: 45s - loss: 7.6666 - accuracy: 0.5000
12224/25000 [=============>................] - ETA: 45s - loss: 7.6641 - accuracy: 0.5002
12256/25000 [=============>................] - ETA: 44s - loss: 7.6691 - accuracy: 0.4998
12288/25000 [=============>................] - ETA: 44s - loss: 7.6654 - accuracy: 0.5001
12320/25000 [=============>................] - ETA: 44s - loss: 7.6666 - accuracy: 0.5000
12352/25000 [=============>................] - ETA: 44s - loss: 7.6666 - accuracy: 0.5000
12384/25000 [=============>................] - ETA: 44s - loss: 7.6666 - accuracy: 0.5000
12416/25000 [=============>................] - ETA: 44s - loss: 7.6728 - accuracy: 0.4996
12448/25000 [=============>................] - ETA: 44s - loss: 7.6728 - accuracy: 0.4996
12480/25000 [=============>................] - ETA: 44s - loss: 7.6678 - accuracy: 0.4999
12512/25000 [==============>...............] - ETA: 43s - loss: 7.6654 - accuracy: 0.5001
12544/25000 [==============>...............] - ETA: 43s - loss: 7.6605 - accuracy: 0.5004
12576/25000 [==============>...............] - ETA: 43s - loss: 7.6569 - accuracy: 0.5006
12608/25000 [==============>...............] - ETA: 43s - loss: 7.6557 - accuracy: 0.5007
12640/25000 [==============>...............] - ETA: 43s - loss: 7.6593 - accuracy: 0.5005
12672/25000 [==============>...............] - ETA: 43s - loss: 7.6569 - accuracy: 0.5006
12704/25000 [==============>...............] - ETA: 43s - loss: 7.6570 - accuracy: 0.5006
12736/25000 [==============>...............] - ETA: 43s - loss: 7.6570 - accuracy: 0.5006
12768/25000 [==============>...............] - ETA: 43s - loss: 7.6582 - accuracy: 0.5005
12800/25000 [==============>...............] - ETA: 42s - loss: 7.6570 - accuracy: 0.5006
12832/25000 [==============>...............] - ETA: 42s - loss: 7.6559 - accuracy: 0.5007
12864/25000 [==============>...............] - ETA: 42s - loss: 7.6559 - accuracy: 0.5007
12896/25000 [==============>...............] - ETA: 42s - loss: 7.6547 - accuracy: 0.5008
12928/25000 [==============>...............] - ETA: 42s - loss: 7.6536 - accuracy: 0.5009
12960/25000 [==============>...............] - ETA: 42s - loss: 7.6512 - accuracy: 0.5010
12992/25000 [==============>...............] - ETA: 42s - loss: 7.6525 - accuracy: 0.5009
13024/25000 [==============>...............] - ETA: 42s - loss: 7.6525 - accuracy: 0.5009
13056/25000 [==============>...............] - ETA: 42s - loss: 7.6525 - accuracy: 0.5009
13088/25000 [==============>...............] - ETA: 41s - loss: 7.6514 - accuracy: 0.5010
13120/25000 [==============>...............] - ETA: 41s - loss: 7.6421 - accuracy: 0.5016
13152/25000 [==============>...............] - ETA: 41s - loss: 7.6433 - accuracy: 0.5015
13184/25000 [==============>...............] - ETA: 41s - loss: 7.6434 - accuracy: 0.5015
13216/25000 [==============>...............] - ETA: 41s - loss: 7.6423 - accuracy: 0.5016
13248/25000 [==============>...............] - ETA: 41s - loss: 7.6493 - accuracy: 0.5011
13280/25000 [==============>...............] - ETA: 41s - loss: 7.6458 - accuracy: 0.5014
13312/25000 [==============>...............] - ETA: 41s - loss: 7.6516 - accuracy: 0.5010
13344/25000 [===============>..............] - ETA: 41s - loss: 7.6505 - accuracy: 0.5010
13376/25000 [===============>..............] - ETA: 40s - loss: 7.6529 - accuracy: 0.5009
13408/25000 [===============>..............] - ETA: 40s - loss: 7.6575 - accuracy: 0.5006
13440/25000 [===============>..............] - ETA: 40s - loss: 7.6564 - accuracy: 0.5007
13472/25000 [===============>..............] - ETA: 40s - loss: 7.6587 - accuracy: 0.5005
13504/25000 [===============>..............] - ETA: 40s - loss: 7.6598 - accuracy: 0.5004
13536/25000 [===============>..............] - ETA: 40s - loss: 7.6621 - accuracy: 0.5003
13568/25000 [===============>..............] - ETA: 40s - loss: 7.6564 - accuracy: 0.5007
13600/25000 [===============>..............] - ETA: 40s - loss: 7.6565 - accuracy: 0.5007
13632/25000 [===============>..............] - ETA: 40s - loss: 7.6565 - accuracy: 0.5007
13664/25000 [===============>..............] - ETA: 39s - loss: 7.6621 - accuracy: 0.5003
13696/25000 [===============>..............] - ETA: 39s - loss: 7.6655 - accuracy: 0.5001
13728/25000 [===============>..............] - ETA: 39s - loss: 7.6599 - accuracy: 0.5004
13760/25000 [===============>..............] - ETA: 39s - loss: 7.6566 - accuracy: 0.5007
13792/25000 [===============>..............] - ETA: 39s - loss: 7.6599 - accuracy: 0.5004
13824/25000 [===============>..............] - ETA: 39s - loss: 7.6611 - accuracy: 0.5004
13856/25000 [===============>..............] - ETA: 39s - loss: 7.6611 - accuracy: 0.5004
13888/25000 [===============>..............] - ETA: 39s - loss: 7.6666 - accuracy: 0.5000
13920/25000 [===============>..............] - ETA: 39s - loss: 7.6611 - accuracy: 0.5004
13952/25000 [===============>..............] - ETA: 38s - loss: 7.6545 - accuracy: 0.5008
13984/25000 [===============>..............] - ETA: 38s - loss: 7.6568 - accuracy: 0.5006
14016/25000 [===============>..............] - ETA: 38s - loss: 7.6557 - accuracy: 0.5007
14048/25000 [===============>..............] - ETA: 38s - loss: 7.6568 - accuracy: 0.5006
14080/25000 [===============>..............] - ETA: 38s - loss: 7.6557 - accuracy: 0.5007
14112/25000 [===============>..............] - ETA: 38s - loss: 7.6601 - accuracy: 0.5004
14144/25000 [===============>..............] - ETA: 38s - loss: 7.6612 - accuracy: 0.5004
14176/25000 [================>.............] - ETA: 38s - loss: 7.6569 - accuracy: 0.5006
14208/25000 [================>.............] - ETA: 38s - loss: 7.6591 - accuracy: 0.5005
14240/25000 [================>.............] - ETA: 37s - loss: 7.6548 - accuracy: 0.5008
14272/25000 [================>.............] - ETA: 37s - loss: 7.6580 - accuracy: 0.5006
14304/25000 [================>.............] - ETA: 37s - loss: 7.6591 - accuracy: 0.5005
14336/25000 [================>.............] - ETA: 37s - loss: 7.6559 - accuracy: 0.5007
14368/25000 [================>.............] - ETA: 37s - loss: 7.6581 - accuracy: 0.5006
14400/25000 [================>.............] - ETA: 37s - loss: 7.6560 - accuracy: 0.5007
14432/25000 [================>.............] - ETA: 37s - loss: 7.6539 - accuracy: 0.5008
14464/25000 [================>.............] - ETA: 37s - loss: 7.6550 - accuracy: 0.5008
14496/25000 [================>.............] - ETA: 37s - loss: 7.6592 - accuracy: 0.5005
14528/25000 [================>.............] - ETA: 36s - loss: 7.6603 - accuracy: 0.5004
14560/25000 [================>.............] - ETA: 36s - loss: 7.6582 - accuracy: 0.5005
14592/25000 [================>.............] - ETA: 36s - loss: 7.6582 - accuracy: 0.5005
14624/25000 [================>.............] - ETA: 36s - loss: 7.6540 - accuracy: 0.5008
14656/25000 [================>.............] - ETA: 36s - loss: 7.6572 - accuracy: 0.5006
14688/25000 [================>.............] - ETA: 36s - loss: 7.6551 - accuracy: 0.5007
14720/25000 [================>.............] - ETA: 36s - loss: 7.6541 - accuracy: 0.5008
14752/25000 [================>.............] - ETA: 36s - loss: 7.6521 - accuracy: 0.5009
14784/25000 [================>.............] - ETA: 36s - loss: 7.6521 - accuracy: 0.5009
14816/25000 [================>.............] - ETA: 35s - loss: 7.6480 - accuracy: 0.5012
14848/25000 [================>.............] - ETA: 35s - loss: 7.6460 - accuracy: 0.5013
14880/25000 [================>.............] - ETA: 35s - loss: 7.6429 - accuracy: 0.5015
14912/25000 [================>.............] - ETA: 35s - loss: 7.6471 - accuracy: 0.5013
14944/25000 [================>.............] - ETA: 35s - loss: 7.6461 - accuracy: 0.5013
14976/25000 [================>.............] - ETA: 35s - loss: 7.6482 - accuracy: 0.5012
15008/25000 [=================>............] - ETA: 35s - loss: 7.6472 - accuracy: 0.5013
15040/25000 [=================>............] - ETA: 35s - loss: 7.6452 - accuracy: 0.5014
15072/25000 [=================>............] - ETA: 35s - loss: 7.6371 - accuracy: 0.5019
15104/25000 [=================>............] - ETA: 34s - loss: 7.6443 - accuracy: 0.5015
15136/25000 [=================>............] - ETA: 34s - loss: 7.6464 - accuracy: 0.5013
15168/25000 [=================>............] - ETA: 34s - loss: 7.6434 - accuracy: 0.5015
15200/25000 [=================>............] - ETA: 34s - loss: 7.6404 - accuracy: 0.5017
15232/25000 [=================>............] - ETA: 34s - loss: 7.6404 - accuracy: 0.5017
15264/25000 [=================>............] - ETA: 34s - loss: 7.6445 - accuracy: 0.5014
15296/25000 [=================>............] - ETA: 34s - loss: 7.6386 - accuracy: 0.5018
15328/25000 [=================>............] - ETA: 34s - loss: 7.6376 - accuracy: 0.5019
15360/25000 [=================>............] - ETA: 34s - loss: 7.6377 - accuracy: 0.5019
15392/25000 [=================>............] - ETA: 33s - loss: 7.6357 - accuracy: 0.5020
15424/25000 [=================>............] - ETA: 33s - loss: 7.6348 - accuracy: 0.5021
15456/25000 [=================>............] - ETA: 33s - loss: 7.6339 - accuracy: 0.5021
15488/25000 [=================>............] - ETA: 33s - loss: 7.6349 - accuracy: 0.5021
15520/25000 [=================>............] - ETA: 33s - loss: 7.6380 - accuracy: 0.5019
15552/25000 [=================>............] - ETA: 33s - loss: 7.6351 - accuracy: 0.5021
15584/25000 [=================>............] - ETA: 33s - loss: 7.6401 - accuracy: 0.5017
15616/25000 [=================>............] - ETA: 33s - loss: 7.6440 - accuracy: 0.5015
15648/25000 [=================>............] - ETA: 32s - loss: 7.6421 - accuracy: 0.5016
15680/25000 [=================>............] - ETA: 32s - loss: 7.6441 - accuracy: 0.5015
15712/25000 [=================>............] - ETA: 32s - loss: 7.6500 - accuracy: 0.5011
15744/25000 [=================>............] - ETA: 32s - loss: 7.6520 - accuracy: 0.5010
15776/25000 [=================>............] - ETA: 32s - loss: 7.6501 - accuracy: 0.5011
15808/25000 [=================>............] - ETA: 32s - loss: 7.6501 - accuracy: 0.5011
15840/25000 [==================>...........] - ETA: 32s - loss: 7.6492 - accuracy: 0.5011
15872/25000 [==================>...........] - ETA: 32s - loss: 7.6512 - accuracy: 0.5010
15904/25000 [==================>...........] - ETA: 32s - loss: 7.6531 - accuracy: 0.5009
15936/25000 [==================>...........] - ETA: 31s - loss: 7.6599 - accuracy: 0.5004
15968/25000 [==================>...........] - ETA: 31s - loss: 7.6589 - accuracy: 0.5005
16000/25000 [==================>...........] - ETA: 31s - loss: 7.6628 - accuracy: 0.5002
16032/25000 [==================>...........] - ETA: 31s - loss: 7.6647 - accuracy: 0.5001
16064/25000 [==================>...........] - ETA: 31s - loss: 7.6647 - accuracy: 0.5001
16096/25000 [==================>...........] - ETA: 31s - loss: 7.6619 - accuracy: 0.5003
16128/25000 [==================>...........] - ETA: 31s - loss: 7.6590 - accuracy: 0.5005
16160/25000 [==================>...........] - ETA: 31s - loss: 7.6533 - accuracy: 0.5009
16192/25000 [==================>...........] - ETA: 31s - loss: 7.6553 - accuracy: 0.5007
16224/25000 [==================>...........] - ETA: 30s - loss: 7.6534 - accuracy: 0.5009
16256/25000 [==================>...........] - ETA: 30s - loss: 7.6562 - accuracy: 0.5007
16288/25000 [==================>...........] - ETA: 30s - loss: 7.6563 - accuracy: 0.5007
16320/25000 [==================>...........] - ETA: 30s - loss: 7.6572 - accuracy: 0.5006
16352/25000 [==================>...........] - ETA: 30s - loss: 7.6544 - accuracy: 0.5008
16384/25000 [==================>...........] - ETA: 30s - loss: 7.6526 - accuracy: 0.5009
16416/25000 [==================>...........] - ETA: 30s - loss: 7.6507 - accuracy: 0.5010
16448/25000 [==================>...........] - ETA: 30s - loss: 7.6470 - accuracy: 0.5013
16480/25000 [==================>...........] - ETA: 30s - loss: 7.6462 - accuracy: 0.5013
16512/25000 [==================>...........] - ETA: 29s - loss: 7.6490 - accuracy: 0.5012
16544/25000 [==================>...........] - ETA: 29s - loss: 7.6453 - accuracy: 0.5014
16576/25000 [==================>...........] - ETA: 29s - loss: 7.6444 - accuracy: 0.5014
16608/25000 [==================>...........] - ETA: 29s - loss: 7.6445 - accuracy: 0.5014
16640/25000 [==================>...........] - ETA: 29s - loss: 7.6473 - accuracy: 0.5013
16672/25000 [===================>..........] - ETA: 29s - loss: 7.6501 - accuracy: 0.5011
16704/25000 [===================>..........] - ETA: 29s - loss: 7.6492 - accuracy: 0.5011
16736/25000 [===================>..........] - ETA: 29s - loss: 7.6492 - accuracy: 0.5011
16768/25000 [===================>..........] - ETA: 29s - loss: 7.6502 - accuracy: 0.5011
16800/25000 [===================>..........] - ETA: 28s - loss: 7.6502 - accuracy: 0.5011
16832/25000 [===================>..........] - ETA: 28s - loss: 7.6493 - accuracy: 0.5011
16864/25000 [===================>..........] - ETA: 28s - loss: 7.6493 - accuracy: 0.5011
16896/25000 [===================>..........] - ETA: 28s - loss: 7.6485 - accuracy: 0.5012
16928/25000 [===================>..........] - ETA: 28s - loss: 7.6476 - accuracy: 0.5012
16960/25000 [===================>..........] - ETA: 28s - loss: 7.6476 - accuracy: 0.5012
16992/25000 [===================>..........] - ETA: 28s - loss: 7.6468 - accuracy: 0.5013
17024/25000 [===================>..........] - ETA: 28s - loss: 7.6486 - accuracy: 0.5012
17056/25000 [===================>..........] - ETA: 27s - loss: 7.6486 - accuracy: 0.5012
17088/25000 [===================>..........] - ETA: 27s - loss: 7.6469 - accuracy: 0.5013
17120/25000 [===================>..........] - ETA: 27s - loss: 7.6460 - accuracy: 0.5013
17152/25000 [===================>..........] - ETA: 27s - loss: 7.6452 - accuracy: 0.5014
17184/25000 [===================>..........] - ETA: 27s - loss: 7.6443 - accuracy: 0.5015
17216/25000 [===================>..........] - ETA: 27s - loss: 7.6426 - accuracy: 0.5016
17248/25000 [===================>..........] - ETA: 27s - loss: 7.6426 - accuracy: 0.5016
17280/25000 [===================>..........] - ETA: 27s - loss: 7.6418 - accuracy: 0.5016
17312/25000 [===================>..........] - ETA: 27s - loss: 7.6427 - accuracy: 0.5016
17344/25000 [===================>..........] - ETA: 26s - loss: 7.6410 - accuracy: 0.5017
17376/25000 [===================>..........] - ETA: 26s - loss: 7.6375 - accuracy: 0.5019
17408/25000 [===================>..........] - ETA: 26s - loss: 7.6384 - accuracy: 0.5018
17440/25000 [===================>..........] - ETA: 26s - loss: 7.6385 - accuracy: 0.5018
17472/25000 [===================>..........] - ETA: 26s - loss: 7.6385 - accuracy: 0.5018
17504/25000 [====================>.........] - ETA: 26s - loss: 7.6368 - accuracy: 0.5019
17536/25000 [====================>.........] - ETA: 26s - loss: 7.6369 - accuracy: 0.5019
17568/25000 [====================>.........] - ETA: 26s - loss: 7.6413 - accuracy: 0.5017
17600/25000 [====================>.........] - ETA: 26s - loss: 7.6457 - accuracy: 0.5014
17632/25000 [====================>.........] - ETA: 25s - loss: 7.6457 - accuracy: 0.5014
17664/25000 [====================>.........] - ETA: 25s - loss: 7.6449 - accuracy: 0.5014
17696/25000 [====================>.........] - ETA: 25s - loss: 7.6424 - accuracy: 0.5016
17728/25000 [====================>.........] - ETA: 25s - loss: 7.6415 - accuracy: 0.5016
17760/25000 [====================>.........] - ETA: 25s - loss: 7.6442 - accuracy: 0.5015
17792/25000 [====================>.........] - ETA: 25s - loss: 7.6442 - accuracy: 0.5015
17824/25000 [====================>.........] - ETA: 25s - loss: 7.6477 - accuracy: 0.5012
17856/25000 [====================>.........] - ETA: 25s - loss: 7.6512 - accuracy: 0.5010
17888/25000 [====================>.........] - ETA: 25s - loss: 7.6529 - accuracy: 0.5009
17920/25000 [====================>.........] - ETA: 24s - loss: 7.6538 - accuracy: 0.5008
17952/25000 [====================>.........] - ETA: 24s - loss: 7.6504 - accuracy: 0.5011
17984/25000 [====================>.........] - ETA: 24s - loss: 7.6530 - accuracy: 0.5009
18016/25000 [====================>.........] - ETA: 24s - loss: 7.6530 - accuracy: 0.5009
18048/25000 [====================>.........] - ETA: 24s - loss: 7.6547 - accuracy: 0.5008
18080/25000 [====================>.........] - ETA: 24s - loss: 7.6547 - accuracy: 0.5008
18112/25000 [====================>.........] - ETA: 24s - loss: 7.6531 - accuracy: 0.5009
18144/25000 [====================>.........] - ETA: 24s - loss: 7.6548 - accuracy: 0.5008
18176/25000 [====================>.........] - ETA: 24s - loss: 7.6565 - accuracy: 0.5007
18208/25000 [====================>.........] - ETA: 23s - loss: 7.6590 - accuracy: 0.5005
18240/25000 [====================>.........] - ETA: 23s - loss: 7.6591 - accuracy: 0.5005
18272/25000 [====================>.........] - ETA: 23s - loss: 7.6574 - accuracy: 0.5006
18304/25000 [====================>.........] - ETA: 23s - loss: 7.6591 - accuracy: 0.5005
18336/25000 [=====================>........] - ETA: 23s - loss: 7.6608 - accuracy: 0.5004
18368/25000 [=====================>........] - ETA: 23s - loss: 7.6624 - accuracy: 0.5003
18400/25000 [=====================>........] - ETA: 23s - loss: 7.6625 - accuracy: 0.5003
18432/25000 [=====================>........] - ETA: 23s - loss: 7.6616 - accuracy: 0.5003
18464/25000 [=====================>........] - ETA: 22s - loss: 7.6608 - accuracy: 0.5004
18496/25000 [=====================>........] - ETA: 22s - loss: 7.6600 - accuracy: 0.5004
18528/25000 [=====================>........] - ETA: 22s - loss: 7.6592 - accuracy: 0.5005
18560/25000 [=====================>........] - ETA: 22s - loss: 7.6633 - accuracy: 0.5002
18592/25000 [=====================>........] - ETA: 22s - loss: 7.6650 - accuracy: 0.5001
18624/25000 [=====================>........] - ETA: 22s - loss: 7.6666 - accuracy: 0.5000
18656/25000 [=====================>........] - ETA: 22s - loss: 7.6674 - accuracy: 0.4999
18688/25000 [=====================>........] - ETA: 22s - loss: 7.6666 - accuracy: 0.5000
18720/25000 [=====================>........] - ETA: 22s - loss: 7.6666 - accuracy: 0.5000
18752/25000 [=====================>........] - ETA: 21s - loss: 7.6674 - accuracy: 0.4999
18784/25000 [=====================>........] - ETA: 21s - loss: 7.6666 - accuracy: 0.5000
18816/25000 [=====================>........] - ETA: 21s - loss: 7.6666 - accuracy: 0.5000
18848/25000 [=====================>........] - ETA: 21s - loss: 7.6666 - accuracy: 0.5000
18880/25000 [=====================>........] - ETA: 21s - loss: 7.6658 - accuracy: 0.5001
18912/25000 [=====================>........] - ETA: 21s - loss: 7.6642 - accuracy: 0.5002
18944/25000 [=====================>........] - ETA: 21s - loss: 7.6658 - accuracy: 0.5001
18976/25000 [=====================>........] - ETA: 21s - loss: 7.6650 - accuracy: 0.5001
19008/25000 [=====================>........] - ETA: 21s - loss: 7.6610 - accuracy: 0.5004
19040/25000 [=====================>........] - ETA: 20s - loss: 7.6602 - accuracy: 0.5004
19072/25000 [=====================>........] - ETA: 20s - loss: 7.6594 - accuracy: 0.5005
19104/25000 [=====================>........] - ETA: 20s - loss: 7.6594 - accuracy: 0.5005
19136/25000 [=====================>........] - ETA: 20s - loss: 7.6602 - accuracy: 0.5004
19168/25000 [======================>.......] - ETA: 20s - loss: 7.6578 - accuracy: 0.5006
19200/25000 [======================>.......] - ETA: 20s - loss: 7.6570 - accuracy: 0.5006
19232/25000 [======================>.......] - ETA: 20s - loss: 7.6547 - accuracy: 0.5008
19264/25000 [======================>.......] - ETA: 20s - loss: 7.6539 - accuracy: 0.5008
19296/25000 [======================>.......] - ETA: 20s - loss: 7.6523 - accuracy: 0.5009
19328/25000 [======================>.......] - ETA: 19s - loss: 7.6531 - accuracy: 0.5009
19360/25000 [======================>.......] - ETA: 19s - loss: 7.6547 - accuracy: 0.5008
19392/25000 [======================>.......] - ETA: 19s - loss: 7.6563 - accuracy: 0.5007
19424/25000 [======================>.......] - ETA: 19s - loss: 7.6587 - accuracy: 0.5005
19456/25000 [======================>.......] - ETA: 19s - loss: 7.6595 - accuracy: 0.5005
19488/25000 [======================>.......] - ETA: 19s - loss: 7.6635 - accuracy: 0.5002
19520/25000 [======================>.......] - ETA: 19s - loss: 7.6643 - accuracy: 0.5002
19552/25000 [======================>.......] - ETA: 19s - loss: 7.6627 - accuracy: 0.5003
19584/25000 [======================>.......] - ETA: 19s - loss: 7.6596 - accuracy: 0.5005
19616/25000 [======================>.......] - ETA: 18s - loss: 7.6588 - accuracy: 0.5005
19648/25000 [======================>.......] - ETA: 18s - loss: 7.6604 - accuracy: 0.5004
19680/25000 [======================>.......] - ETA: 18s - loss: 7.6573 - accuracy: 0.5006
19712/25000 [======================>.......] - ETA: 18s - loss: 7.6542 - accuracy: 0.5008
19744/25000 [======================>.......] - ETA: 18s - loss: 7.6565 - accuracy: 0.5007
19776/25000 [======================>.......] - ETA: 18s - loss: 7.6620 - accuracy: 0.5003
19808/25000 [======================>.......] - ETA: 18s - loss: 7.6651 - accuracy: 0.5001
19840/25000 [======================>.......] - ETA: 18s - loss: 7.6620 - accuracy: 0.5003
19872/25000 [======================>.......] - ETA: 18s - loss: 7.6643 - accuracy: 0.5002
19904/25000 [======================>.......] - ETA: 17s - loss: 7.6658 - accuracy: 0.5001
19936/25000 [======================>.......] - ETA: 17s - loss: 7.6643 - accuracy: 0.5002
19968/25000 [======================>.......] - ETA: 17s - loss: 7.6597 - accuracy: 0.5005
20000/25000 [=======================>......] - ETA: 17s - loss: 7.6567 - accuracy: 0.5006
20032/25000 [=======================>......] - ETA: 17s - loss: 7.6528 - accuracy: 0.5009
20064/25000 [=======================>......] - ETA: 17s - loss: 7.6521 - accuracy: 0.5009
20096/25000 [=======================>......] - ETA: 17s - loss: 7.6521 - accuracy: 0.5009
20128/25000 [=======================>......] - ETA: 17s - loss: 7.6514 - accuracy: 0.5010
20160/25000 [=======================>......] - ETA: 17s - loss: 7.6468 - accuracy: 0.5013
20192/25000 [=======================>......] - ETA: 16s - loss: 7.6492 - accuracy: 0.5011
20224/25000 [=======================>......] - ETA: 16s - loss: 7.6492 - accuracy: 0.5011
20256/25000 [=======================>......] - ETA: 16s - loss: 7.6507 - accuracy: 0.5010
20288/25000 [=======================>......] - ETA: 16s - loss: 7.6515 - accuracy: 0.5010
20320/25000 [=======================>......] - ETA: 16s - loss: 7.6515 - accuracy: 0.5010
20352/25000 [=======================>......] - ETA: 16s - loss: 7.6516 - accuracy: 0.5010
20384/25000 [=======================>......] - ETA: 16s - loss: 7.6531 - accuracy: 0.5009
20416/25000 [=======================>......] - ETA: 16s - loss: 7.6523 - accuracy: 0.5009
20448/25000 [=======================>......] - ETA: 15s - loss: 7.6531 - accuracy: 0.5009
20480/25000 [=======================>......] - ETA: 15s - loss: 7.6561 - accuracy: 0.5007
20512/25000 [=======================>......] - ETA: 15s - loss: 7.6584 - accuracy: 0.5005
20544/25000 [=======================>......] - ETA: 15s - loss: 7.6569 - accuracy: 0.5006
20576/25000 [=======================>......] - ETA: 15s - loss: 7.6540 - accuracy: 0.5008
20608/25000 [=======================>......] - ETA: 15s - loss: 7.6555 - accuracy: 0.5007
20640/25000 [=======================>......] - ETA: 15s - loss: 7.6540 - accuracy: 0.5008
20672/25000 [=======================>......] - ETA: 15s - loss: 7.6555 - accuracy: 0.5007
20704/25000 [=======================>......] - ETA: 15s - loss: 7.6525 - accuracy: 0.5009
20736/25000 [=======================>......] - ETA: 14s - loss: 7.6540 - accuracy: 0.5008
20768/25000 [=======================>......] - ETA: 14s - loss: 7.6578 - accuracy: 0.5006
20800/25000 [=======================>......] - ETA: 14s - loss: 7.6548 - accuracy: 0.5008
20832/25000 [=======================>......] - ETA: 14s - loss: 7.6526 - accuracy: 0.5009
20864/25000 [========================>.....] - ETA: 14s - loss: 7.6512 - accuracy: 0.5010
20896/25000 [========================>.....] - ETA: 14s - loss: 7.6512 - accuracy: 0.5010
20928/25000 [========================>.....] - ETA: 14s - loss: 7.6527 - accuracy: 0.5009
20960/25000 [========================>.....] - ETA: 14s - loss: 7.6513 - accuracy: 0.5010
20992/25000 [========================>.....] - ETA: 14s - loss: 7.6505 - accuracy: 0.5010
21024/25000 [========================>.....] - ETA: 13s - loss: 7.6513 - accuracy: 0.5010
21056/25000 [========================>.....] - ETA: 13s - loss: 7.6477 - accuracy: 0.5012
21088/25000 [========================>.....] - ETA: 13s - loss: 7.6521 - accuracy: 0.5009
21120/25000 [========================>.....] - ETA: 13s - loss: 7.6492 - accuracy: 0.5011
21152/25000 [========================>.....] - ETA: 13s - loss: 7.6485 - accuracy: 0.5012
21184/25000 [========================>.....] - ETA: 13s - loss: 7.6471 - accuracy: 0.5013
21216/25000 [========================>.....] - ETA: 13s - loss: 7.6464 - accuracy: 0.5013
21248/25000 [========================>.....] - ETA: 13s - loss: 7.6479 - accuracy: 0.5012
21280/25000 [========================>.....] - ETA: 13s - loss: 7.6428 - accuracy: 0.5016
21312/25000 [========================>.....] - ETA: 12s - loss: 7.6414 - accuracy: 0.5016
21344/25000 [========================>.....] - ETA: 12s - loss: 7.6415 - accuracy: 0.5016
21376/25000 [========================>.....] - ETA: 12s - loss: 7.6429 - accuracy: 0.5015
21408/25000 [========================>.....] - ETA: 12s - loss: 7.6416 - accuracy: 0.5016
21440/25000 [========================>.....] - ETA: 12s - loss: 7.6409 - accuracy: 0.5017
21472/25000 [========================>.....] - ETA: 12s - loss: 7.6381 - accuracy: 0.5019
21504/25000 [========================>.....] - ETA: 12s - loss: 7.6374 - accuracy: 0.5019
21536/25000 [========================>.....] - ETA: 12s - loss: 7.6381 - accuracy: 0.5019
21568/25000 [========================>.....] - ETA: 12s - loss: 7.6375 - accuracy: 0.5019
21600/25000 [========================>.....] - ETA: 11s - loss: 7.6375 - accuracy: 0.5019
21632/25000 [========================>.....] - ETA: 11s - loss: 7.6368 - accuracy: 0.5019
21664/25000 [========================>.....] - ETA: 11s - loss: 7.6362 - accuracy: 0.5020
21696/25000 [=========================>....] - ETA: 11s - loss: 7.6355 - accuracy: 0.5020
21728/25000 [=========================>....] - ETA: 11s - loss: 7.6356 - accuracy: 0.5020
21760/25000 [=========================>....] - ETA: 11s - loss: 7.6377 - accuracy: 0.5019
21792/25000 [=========================>....] - ETA: 11s - loss: 7.6399 - accuracy: 0.5017
21824/25000 [=========================>....] - ETA: 11s - loss: 7.6385 - accuracy: 0.5018
21856/25000 [=========================>....] - ETA: 11s - loss: 7.6393 - accuracy: 0.5018
21888/25000 [=========================>....] - ETA: 10s - loss: 7.6393 - accuracy: 0.5018
21920/25000 [=========================>....] - ETA: 10s - loss: 7.6365 - accuracy: 0.5020
21952/25000 [=========================>....] - ETA: 10s - loss: 7.6387 - accuracy: 0.5018
21984/25000 [=========================>....] - ETA: 10s - loss: 7.6394 - accuracy: 0.5018
22016/25000 [=========================>....] - ETA: 10s - loss: 7.6388 - accuracy: 0.5018
22048/25000 [=========================>....] - ETA: 10s - loss: 7.6360 - accuracy: 0.5020
22080/25000 [=========================>....] - ETA: 10s - loss: 7.6368 - accuracy: 0.5019
22112/25000 [=========================>....] - ETA: 10s - loss: 7.6396 - accuracy: 0.5018
22144/25000 [=========================>....] - ETA: 10s - loss: 7.6382 - accuracy: 0.5019
22176/25000 [=========================>....] - ETA: 9s - loss: 7.6390 - accuracy: 0.5018 
22208/25000 [=========================>....] - ETA: 9s - loss: 7.6383 - accuracy: 0.5018
22240/25000 [=========================>....] - ETA: 9s - loss: 7.6377 - accuracy: 0.5019
22272/25000 [=========================>....] - ETA: 9s - loss: 7.6370 - accuracy: 0.5019
22304/25000 [=========================>....] - ETA: 9s - loss: 7.6371 - accuracy: 0.5019
22336/25000 [=========================>....] - ETA: 9s - loss: 7.6371 - accuracy: 0.5019
22368/25000 [=========================>....] - ETA: 9s - loss: 7.6385 - accuracy: 0.5018
22400/25000 [=========================>....] - ETA: 9s - loss: 7.6358 - accuracy: 0.5020
22432/25000 [=========================>....] - ETA: 9s - loss: 7.6406 - accuracy: 0.5017
22464/25000 [=========================>....] - ETA: 8s - loss: 7.6441 - accuracy: 0.5015
22496/25000 [=========================>....] - ETA: 8s - loss: 7.6428 - accuracy: 0.5016
22528/25000 [==========================>...] - ETA: 8s - loss: 7.6421 - accuracy: 0.5016
22560/25000 [==========================>...] - ETA: 8s - loss: 7.6360 - accuracy: 0.5020
22592/25000 [==========================>...] - ETA: 8s - loss: 7.6334 - accuracy: 0.5022
22624/25000 [==========================>...] - ETA: 8s - loss: 7.6327 - accuracy: 0.5022
22656/25000 [==========================>...] - ETA: 8s - loss: 7.6348 - accuracy: 0.5021
22688/25000 [==========================>...] - ETA: 8s - loss: 7.6322 - accuracy: 0.5022
22720/25000 [==========================>...] - ETA: 8s - loss: 7.6302 - accuracy: 0.5024
22752/25000 [==========================>...] - ETA: 7s - loss: 7.6343 - accuracy: 0.5021
22784/25000 [==========================>...] - ETA: 7s - loss: 7.6357 - accuracy: 0.5020
22816/25000 [==========================>...] - ETA: 7s - loss: 7.6377 - accuracy: 0.5019
22848/25000 [==========================>...] - ETA: 7s - loss: 7.6378 - accuracy: 0.5019
22880/25000 [==========================>...] - ETA: 7s - loss: 7.6385 - accuracy: 0.5018
22912/25000 [==========================>...] - ETA: 7s - loss: 7.6392 - accuracy: 0.5018
22944/25000 [==========================>...] - ETA: 7s - loss: 7.6412 - accuracy: 0.5017
22976/25000 [==========================>...] - ETA: 7s - loss: 7.6439 - accuracy: 0.5015
23008/25000 [==========================>...] - ETA: 7s - loss: 7.6446 - accuracy: 0.5014
23040/25000 [==========================>...] - ETA: 6s - loss: 7.6453 - accuracy: 0.5014
23072/25000 [==========================>...] - ETA: 6s - loss: 7.6454 - accuracy: 0.5014
23104/25000 [==========================>...] - ETA: 6s - loss: 7.6441 - accuracy: 0.5015
23136/25000 [==========================>...] - ETA: 6s - loss: 7.6441 - accuracy: 0.5015
23168/25000 [==========================>...] - ETA: 6s - loss: 7.6454 - accuracy: 0.5014
23200/25000 [==========================>...] - ETA: 6s - loss: 7.6475 - accuracy: 0.5013
23232/25000 [==========================>...] - ETA: 6s - loss: 7.6462 - accuracy: 0.5013
23264/25000 [==========================>...] - ETA: 6s - loss: 7.6436 - accuracy: 0.5015
23296/25000 [==========================>...] - ETA: 5s - loss: 7.6469 - accuracy: 0.5013
23328/25000 [==========================>...] - ETA: 5s - loss: 7.6469 - accuracy: 0.5013
23360/25000 [===========================>..] - ETA: 5s - loss: 7.6443 - accuracy: 0.5015
23392/25000 [===========================>..] - ETA: 5s - loss: 7.6483 - accuracy: 0.5012
23424/25000 [===========================>..] - ETA: 5s - loss: 7.6509 - accuracy: 0.5010
23456/25000 [===========================>..] - ETA: 5s - loss: 7.6509 - accuracy: 0.5010
23488/25000 [===========================>..] - ETA: 5s - loss: 7.6536 - accuracy: 0.5009
23520/25000 [===========================>..] - ETA: 5s - loss: 7.6516 - accuracy: 0.5010
23552/25000 [===========================>..] - ETA: 5s - loss: 7.6529 - accuracy: 0.5009
23584/25000 [===========================>..] - ETA: 4s - loss: 7.6536 - accuracy: 0.5008
23616/25000 [===========================>..] - ETA: 4s - loss: 7.6530 - accuracy: 0.5009
23648/25000 [===========================>..] - ETA: 4s - loss: 7.6524 - accuracy: 0.5009
23680/25000 [===========================>..] - ETA: 4s - loss: 7.6511 - accuracy: 0.5010
23712/25000 [===========================>..] - ETA: 4s - loss: 7.6543 - accuracy: 0.5008
23744/25000 [===========================>..] - ETA: 4s - loss: 7.6537 - accuracy: 0.5008
23776/25000 [===========================>..] - ETA: 4s - loss: 7.6544 - accuracy: 0.5008
23808/25000 [===========================>..] - ETA: 4s - loss: 7.6531 - accuracy: 0.5009
23840/25000 [===========================>..] - ETA: 4s - loss: 7.6525 - accuracy: 0.5009
23872/25000 [===========================>..] - ETA: 3s - loss: 7.6531 - accuracy: 0.5009
23904/25000 [===========================>..] - ETA: 3s - loss: 7.6544 - accuracy: 0.5008
23936/25000 [===========================>..] - ETA: 3s - loss: 7.6532 - accuracy: 0.5009
23968/25000 [===========================>..] - ETA: 3s - loss: 7.6538 - accuracy: 0.5008
24000/25000 [===========================>..] - ETA: 3s - loss: 7.6526 - accuracy: 0.5009
24032/25000 [===========================>..] - ETA: 3s - loss: 7.6545 - accuracy: 0.5008
24064/25000 [===========================>..] - ETA: 3s - loss: 7.6564 - accuracy: 0.5007
24096/25000 [===========================>..] - ETA: 3s - loss: 7.6577 - accuracy: 0.5006
24128/25000 [===========================>..] - ETA: 3s - loss: 7.6603 - accuracy: 0.5004
24160/25000 [===========================>..] - ETA: 2s - loss: 7.6577 - accuracy: 0.5006
24192/25000 [============================>.] - ETA: 2s - loss: 7.6590 - accuracy: 0.5005
24224/25000 [============================>.] - ETA: 2s - loss: 7.6597 - accuracy: 0.5005
24256/25000 [============================>.] - ETA: 2s - loss: 7.6571 - accuracy: 0.5006
24288/25000 [============================>.] - ETA: 2s - loss: 7.6559 - accuracy: 0.5007
24320/25000 [============================>.] - ETA: 2s - loss: 7.6534 - accuracy: 0.5009
24352/25000 [============================>.] - ETA: 2s - loss: 7.6515 - accuracy: 0.5010
24384/25000 [============================>.] - ETA: 2s - loss: 7.6540 - accuracy: 0.5008
24416/25000 [============================>.] - ETA: 2s - loss: 7.6541 - accuracy: 0.5008
24448/25000 [============================>.] - ETA: 1s - loss: 7.6547 - accuracy: 0.5008
24480/25000 [============================>.] - ETA: 1s - loss: 7.6547 - accuracy: 0.5008
24512/25000 [============================>.] - ETA: 1s - loss: 7.6547 - accuracy: 0.5008
24544/25000 [============================>.] - ETA: 1s - loss: 7.6572 - accuracy: 0.5006
24576/25000 [============================>.] - ETA: 1s - loss: 7.6548 - accuracy: 0.5008
24608/25000 [============================>.] - ETA: 1s - loss: 7.6548 - accuracy: 0.5008
24640/25000 [============================>.] - ETA: 1s - loss: 7.6567 - accuracy: 0.5006
24672/25000 [============================>.] - ETA: 1s - loss: 7.6561 - accuracy: 0.5007
24704/25000 [============================>.] - ETA: 1s - loss: 7.6592 - accuracy: 0.5005
24736/25000 [============================>.] - ETA: 0s - loss: 7.6579 - accuracy: 0.5006
24768/25000 [============================>.] - ETA: 0s - loss: 7.6573 - accuracy: 0.5006
24800/25000 [============================>.] - ETA: 0s - loss: 7.6604 - accuracy: 0.5004
24832/25000 [============================>.] - ETA: 0s - loss: 7.6617 - accuracy: 0.5003
24864/25000 [============================>.] - ETA: 0s - loss: 7.6635 - accuracy: 0.5002
24896/25000 [============================>.] - ETA: 0s - loss: 7.6623 - accuracy: 0.5003
24928/25000 [============================>.] - ETA: 0s - loss: 7.6648 - accuracy: 0.5001
24960/25000 [============================>.] - ETA: 0s - loss: 7.6660 - accuracy: 0.5000
24992/25000 [============================>.] - ETA: 0s - loss: 7.6678 - accuracy: 0.4999
25000/25000 [==============================] - 106s 4ms/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000
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

[0;31m---------------------------------------------------------------------------[0m
[0;31mFileNotFoundError[0m                         Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example/benchmark_timeseries_m5.py[0m in [0;36m<module>[0;34m[0m
[1;32m     84[0m [0;34m[0m[0m
[1;32m     85[0m """
[0;32m---> 86[0;31m [0mcalendar[0m               [0;34m=[0m [0mpd[0m[0;34m.[0m[0mread_csv[0m[0;34m([0m[0;34mf'{m5_input_path}/calendar.csv'[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     87[0m [0msales_train_val[0m        [0;34m=[0m [0mpd[0m[0;34m.[0m[0mread_csv[0m[0;34m([0m[0;34mf'{m5_input_path}/sales_train_val.csv'[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[1;32m     88[0m [0msample_submission[0m      [0;34m=[0m [0mpd[0m[0;34m.[0m[0mread_csv[0m[0;34m([0m[0;34mf'{m5_input_path}/sample_submission.csv'[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/pandas/io/parsers.py[0m in [0;36mparser_f[0;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, dialect, error_bad_lines, warn_bad_lines, delim_whitespace, low_memory, memory_map, float_precision)[0m
[1;32m    683[0m         )
[1;32m    684[0m [0;34m[0m[0m
[0;32m--> 685[0;31m         [0;32mreturn[0m [0m_read[0m[0;34m([0m[0mfilepath_or_buffer[0m[0;34m,[0m [0mkwds[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m    686[0m [0;34m[0m[0m
[1;32m    687[0m     [0mparser_f[0m[0;34m.[0m[0m__name__[0m [0;34m=[0m [0mname[0m[0;34m[0m[0;34m[0m[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/pandas/io/parsers.py[0m in [0;36m_read[0;34m(filepath_or_buffer, kwds)[0m
[1;32m    455[0m [0;34m[0m[0m
[1;32m    456[0m     [0;31m# Create the parser.[0m[0;34m[0m[0;34m[0m[0;34m[0m[0m
[0;32m--> 457[0;31m     [0mparser[0m [0;34m=[0m [0mTextFileReader[0m[0;34m([0m[0mfp_or_buf[0m[0;34m,[0m [0;34m**[0m[0mkwds[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m    458[0m [0;34m[0m[0m
[1;32m    459[0m     [0;32mif[0m [0mchunksize[0m [0;32mor[0m [0miterator[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/pandas/io/parsers.py[0m in [0;36m__init__[0;34m(self, f, engine, **kwds)[0m
[1;32m    893[0m             [0mself[0m[0;34m.[0m[0moptions[0m[0;34m[[0m[0;34m"has_index_names"[0m[0;34m][0m [0;34m=[0m [0mkwds[0m[0;34m[[0m[0;34m"has_index_names"[0m[0;34m][0m[0;34m[0m[0;34m[0m[0m
[1;32m    894[0m [0;34m[0m[0m
[0;32m--> 895[0;31m         [0mself[0m[0;34m.[0m[0m_make_engine[0m[0;34m([0m[0mself[0m[0;34m.[0m[0mengine[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m    896[0m [0;34m[0m[0m
[1;32m    897[0m     [0;32mdef[0m [0mclose[0m[0;34m([0m[0mself[0m[0;34m)[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/pandas/io/parsers.py[0m in [0;36m_make_engine[0;34m(self, engine)[0m
[1;32m   1133[0m     [0;32mdef[0m [0m_make_engine[0m[0;34m([0m[0mself[0m[0;34m,[0m [0mengine[0m[0;34m=[0m[0;34m"c"[0m[0;34m)[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
[1;32m   1134[0m         [0;32mif[0m [0mengine[0m [0;34m==[0m [0;34m"c"[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
[0;32m-> 1135[0;31m             [0mself[0m[0;34m.[0m[0m_engine[0m [0;34m=[0m [0mCParserWrapper[0m[0;34m([0m[0mself[0m[0;34m.[0m[0mf[0m[0;34m,[0m [0;34m**[0m[0mself[0m[0;34m.[0m[0moptions[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m   1136[0m         [0;32melse[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
[1;32m   1137[0m             [0;32mif[0m [0mengine[0m [0;34m==[0m [0;34m"python"[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/pandas/io/parsers.py[0m in [0;36m__init__[0;34m(self, src, **kwds)[0m
[1;32m   1915[0m         [0mkwds[0m[0;34m[[0m[0;34m"usecols"[0m[0;34m][0m [0;34m=[0m [0mself[0m[0;34m.[0m[0musecols[0m[0;34m[0m[0;34m[0m[0m
[1;32m   1916[0m [0;34m[0m[0m
[0;32m-> 1917[0;31m         [0mself[0m[0;34m.[0m[0m_reader[0m [0;34m=[0m [0mparsers[0m[0;34m.[0m[0mTextReader[0m[0;34m([0m[0msrc[0m[0;34m,[0m [0;34m**[0m[0mkwds[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m   1918[0m         [0mself[0m[0;34m.[0m[0munnamed_cols[0m [0;34m=[0m [0mself[0m[0;34m.[0m[0m_reader[0m[0;34m.[0m[0munnamed_cols[0m[0;34m[0m[0;34m[0m[0m
[1;32m   1919[0m [0;34m[0m[0m

[0;32mpandas/_libs/parsers.pyx[0m in [0;36mpandas._libs.parsers.TextReader.__cinit__[0;34m()[0m

[0;32mpandas/_libs/parsers.pyx[0m in [0;36mpandas._libs.parsers.TextReader._setup_parser_source[0;34m()[0m

[0;31mFileNotFoundError[0m: [Errno 2] File b'./m5-forecasting-accuracy/calendar.csv' does not exist: b'./m5-forecasting-accuracy/calendar.csv'





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

[0;31m---------------------------------------------------------------------------[0m
[0;31mFileNotFoundError[0m                         Traceback (most recent call last)
[0;32m~/work/mlmodels/mlmodels/mlmodels/example/benchmark_timeseries_m5.py[0m in [0;36m<module>[0;34m[0m
[1;32m     84[0m [0;34m[0m[0m
[1;32m     85[0m """
[0;32m---> 86[0;31m [0mcalendar[0m               [0;34m=[0m [0mpd[0m[0;34m.[0m[0mread_csv[0m[0;34m([0m[0;34mf'{m5_input_path}/calendar.csv'[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m     87[0m [0msales_train_val[0m        [0;34m=[0m [0mpd[0m[0;34m.[0m[0mread_csv[0m[0;34m([0m[0;34mf'{m5_input_path}/sales_train_val.csv'[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[1;32m     88[0m [0msample_submission[0m      [0;34m=[0m [0mpd[0m[0;34m.[0m[0mread_csv[0m[0;34m([0m[0;34mf'{m5_input_path}/sample_submission.csv'[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/pandas/io/parsers.py[0m in [0;36mparser_f[0;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, dialect, error_bad_lines, warn_bad_lines, delim_whitespace, low_memory, memory_map, float_precision)[0m
[1;32m    683[0m         )
[1;32m    684[0m [0;34m[0m[0m
[0;32m--> 685[0;31m         [0;32mreturn[0m [0m_read[0m[0;34m([0m[0mfilepath_or_buffer[0m[0;34m,[0m [0mkwds[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m    686[0m [0;34m[0m[0m
[1;32m    687[0m     [0mparser_f[0m[0;34m.[0m[0m__name__[0m [0;34m=[0m [0mname[0m[0;34m[0m[0;34m[0m[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/pandas/io/parsers.py[0m in [0;36m_read[0;34m(filepath_or_buffer, kwds)[0m
[1;32m    455[0m [0;34m[0m[0m
[1;32m    456[0m     [0;31m# Create the parser.[0m[0;34m[0m[0;34m[0m[0;34m[0m[0m
[0;32m--> 457[0;31m     [0mparser[0m [0;34m=[0m [0mTextFileReader[0m[0;34m([0m[0mfp_or_buf[0m[0;34m,[0m [0;34m**[0m[0mkwds[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m    458[0m [0;34m[0m[0m
[1;32m    459[0m     [0;32mif[0m [0mchunksize[0m [0;32mor[0m [0miterator[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/pandas/io/parsers.py[0m in [0;36m__init__[0;34m(self, f, engine, **kwds)[0m
[1;32m    893[0m             [0mself[0m[0;34m.[0m[0moptions[0m[0;34m[[0m[0;34m"has_index_names"[0m[0;34m][0m [0;34m=[0m [0mkwds[0m[0;34m[[0m[0;34m"has_index_names"[0m[0;34m][0m[0;34m[0m[0;34m[0m[0m
[1;32m    894[0m [0;34m[0m[0m
[0;32m--> 895[0;31m         [0mself[0m[0;34m.[0m[0m_make_engine[0m[0;34m([0m[0mself[0m[0;34m.[0m[0mengine[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m    896[0m [0;34m[0m[0m
[1;32m    897[0m     [0;32mdef[0m [0mclose[0m[0;34m([0m[0mself[0m[0;34m)[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/pandas/io/parsers.py[0m in [0;36m_make_engine[0;34m(self, engine)[0m
[1;32m   1133[0m     [0;32mdef[0m [0m_make_engine[0m[0;34m([0m[0mself[0m[0;34m,[0m [0mengine[0m[0;34m=[0m[0;34m"c"[0m[0;34m)[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
[1;32m   1134[0m         [0;32mif[0m [0mengine[0m [0;34m==[0m [0;34m"c"[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
[0;32m-> 1135[0;31m             [0mself[0m[0;34m.[0m[0m_engine[0m [0;34m=[0m [0mCParserWrapper[0m[0;34m([0m[0mself[0m[0;34m.[0m[0mf[0m[0;34m,[0m [0;34m**[0m[0mself[0m[0;34m.[0m[0moptions[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m   1136[0m         [0;32melse[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m
[1;32m   1137[0m             [0;32mif[0m [0mengine[0m [0;34m==[0m [0;34m"python"[0m[0;34m:[0m[0;34m[0m[0;34m[0m[0m

[0;32m/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/pandas/io/parsers.py[0m in [0;36m__init__[0;34m(self, src, **kwds)[0m
[1;32m   1915[0m         [0mkwds[0m[0;34m[[0m[0;34m"usecols"[0m[0;34m][0m [0;34m=[0m [0mself[0m[0;34m.[0m[0musecols[0m[0;34m[0m[0;34m[0m[0m
[1;32m   1916[0m [0;34m[0m[0m
[0;32m-> 1917[0;31m         [0mself[0m[0;34m.[0m[0m_reader[0m [0;34m=[0m [0mparsers[0m[0;34m.[0m[0mTextReader[0m[0;34m([0m[0msrc[0m[0;34m,[0m [0;34m**[0m[0mkwds[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
[0m[1;32m   1918[0m         [0mself[0m[0;34m.[0m[0munnamed_cols[0m [0;34m=[0m [0mself[0m[0;34m.[0m[0m_reader[0m[0;34m.[0m[0munnamed_cols[0m[0;34m[0m[0;34m[0m[0m
[1;32m   1919[0m [0;34m[0m[0m

[0;32mpandas/_libs/parsers.pyx[0m in [0;36mpandas._libs.parsers.TextReader.__cinit__[0;34m()[0m

[0;32mpandas/_libs/parsers.pyx[0m in [0;36mpandas._libs.parsers.TextReader._setup_parser_source[0;34m()[0m

[0;31mFileNotFoundError[0m: [Errno 2] File b'./m5-forecasting-accuracy/calendar.csv' does not exist: b'./m5-forecasting-accuracy/calendar.csv'
