
  test_dataloader /home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json Namespace(config_file='/home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json', config_mode='test', do='test_dataloader', folder=None, log_file=None, name='ml_store', save_folder='ztest/') 

  ml_test --do test_dataloader 





 ********************************************************************************************************************************************

 ******** TAG ::  {'github_repo_url': 'https://github.com/arita37/mlmodels/tree/bd7dfc233939710e05244f8e6a394a7ce12a3485', 'url_branch_file': 'https://github.com/arita37/mlmodels/blob/dev/', 'repo': 'arita37/mlmodels', 'branch': 'dev', 'sha': 'bd7dfc233939710e05244f8e6a394a7ce12a3485', 'workflow': 'test_dataloader'}

 ******** GITHUB_WOKFLOW : https://github.com/arita37/mlmodels/actions?query=workflow%3Atest_dataloader

 ******** GITHUB_REPO_BRANCH : https://github.com/arita37/mlmodels/tree/dev/

 ******** GITHUB_REPO_URL : https://github.com/arita37/mlmodels/tree/bd7dfc233939710e05244f8e6a394a7ce12a3485

 ******** GITHUB_COMMIT_URL : https://github.com/arita37/mlmodels/commit/bd7dfc233939710e05244f8e6a394a7ce12a3485

 ******** Click here for Online DEBUGGER : https://gitpod.io/#https://github.com/arita37/mlmodels/tree/bd7dfc233939710e05244f8e6a394a7ce12a3485

 ************************************************************************************************************************

  ############Check model ################################ 





 ********************************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/dataloader.py --do test  

  




 #################################################################################################### 

  /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/charcnn.json 
 

  #####  Load JSON data_pars 

  {
  "data_info":{
    "dataset":"mlmodels\/dataset\/text\/ag_news_csv",
    "train":true,
    "alphabet_size":69,
    "alphabet":"abcdefghijklmnopqrstuvwxyz0123456789-,;.!?:'\"\/\\|_@#$%^&*~`+-=<>()[]{}",
    "input_size":1014,
    "num_of_classes":4
  },
  "preprocessors":[
    {
      "name":"loader",
      "uri":"mlmodels.preprocess.generic:pandasDataset",
      "args":{
        "colX":[
          "colX"
        ],
        "coly":[
          "coly"
        ],
        "encoding":"'ISO-8859-1'",
        "read_csv_parm":{
          "usecols":[
            0,
            1
          ],
          "names":[
            "coly",
            "colX"
          ]
        }
      }
    },
    {
      "name":"tokenizer",
      "uri":"mlmodels.model_keras.raw.char_cnn.data_utils:Data",
      "args":{
        "data_source":"",
        "alphabet":"abcdefghijklmnopqrstuvwxyz0123456789-,;.!?:'\"\/\\|_@#$%^&*~`+-=<>()[]{}",
        "input_size":1014,
        "num_of_classes":4
      }
    }
  ]
} 

  
 #####  Load DataLoader  

  
 #####  compute DataLoader  

  URL:  mlmodels.preprocess.generic:pandasDataset {'colX': ['colX'], 'coly': ['coly'], 'encoding': "'ISO-8859-1'", 'read_csv_parm': {'usecols': [0, 1], 'names': ['coly', 'colX']}} 

  
###### load_callable_from_uri LOADED <class 'mlmodels.preprocess.generic.pandasDataset'> 
cls_name : pandasDataset
Error /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/charcnn.json [Errno 2] File b'mlmodels/dataset/text/ag_news_csv/train/mlmodels/dataset/text/ag_news_csv.csv' does not exist: b'mlmodels/dataset/text/ag_news_csv/train/mlmodels/dataset/text/ag_news_csv.csv'

  




 #################################################################################################### 

  /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/charcnn_zhang.json 
 

  #####  Load JSON data_pars 

  {
  "data_info":{
    "dataset":"mlmodels\/dataset\/text\/ag_news_csv",
    "train":true,
    "alphabet_size":69,
    "alphabet":"abcdefghijklmnopqrstuvwxyz0123456789-,;.!?:'\"\/\\|_@#$%^&*~`+-=<>()[]{}",
    "input_size":1014,
    "num_of_classes":4
  },
  "preprocessors":[
    {
      "name":"loader",
      "uri":"mlmodels.preprocess.generic:pandasDataset",
      "args":{
        "colX":[
          "colX"
        ],
        "coly":[
          "coly"
        ],
        "encoding":"'ISO-8859-1'",
        "read_csv_parm":{
          "usecols":[
            0,
            1
          ],
          "names":[
            "coly",
            "colX"
          ]
        }
      }
    },
    {
      "name":"tokenizer",
      "uri":"mlmodels.model_keras.raw.char_cnn.data_utils:Data",
      "args":{
        "data_source":"",
        "alphabet":"abcdefghijklmnopqrstuvwxyz0123456789-,;.!?:'\"\/\\|_@#$%^&*~`+-=<>()[]{}",
        "input_size":1014,
        "num_of_classes":4
      }
    }
  ]
} 

  
 #####  Load DataLoader  

  
 #####  compute DataLoader  

  URL:  mlmodels.preprocess.generic:pandasDataset {'colX': ['colX'], 'coly': ['coly'], 'encoding': "'ISO-8859-1'", 'read_csv_parm': {'usecols': [0, 1], 'names': ['coly', 'colX']}} 

  
###### load_callable_from_uri LOADED <class 'mlmodels.preprocess.generic.pandasDataset'> 
cls_name : pandasDataset
Error /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/charcnn_zhang.json [Errno 2] File b'mlmodels/dataset/text/ag_news_csv/train/mlmodels/dataset/text/ag_news_csv.csv' does not exist: b'mlmodels/dataset/text/ag_news_csv/train/mlmodels/dataset/text/ag_news_csv.csv'

  




 #################################################################################################### 

  /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/textcnn.json 
 

  #####  Load JSON data_pars 

  {
  "data_info":{
    "dataset":"mlmodels\/dataset\/text\/imdb",
    "pass_data_pars":false,
    "train":true,
    "maxlen":40,
    "max_features":5
  },
  "preprocessors":[
    {
      "name":"loader",
      "uri":"mlmodels.preprocess.generic:NumpyDataset",
      "args":{
        "numpy_loader_args":{
          "allow_pickle":true
        },
        "encoding":"'ISO-8859-1'"
      }
    },
    {
      "name":"imdb_process",
      "uri":"mlmodels.preprocess.text_keras:IMDBDataset",
      "args":{
        "num_words":5
      }
    }
  ]
} 

  
 #####  Load DataLoader  

  
 #####  compute DataLoader  

  URL:  mlmodels.preprocess.generic:NumpyDataset {'numpy_loader_args': {'allow_pickle': True}, 'encoding': "'ISO-8859-1'"} 

  
###### load_callable_from_uri LOADED <class 'mlmodels.preprocess.generic.NumpyDataset'> 
cls_name : NumpyDataset
Dataset File path :  train/mlmodels/dataset/text/imdb.npz
Error /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/textcnn.json [Errno 2] No such file or directory: 'train/mlmodels/dataset/text/imdb.npz'

  




 #################################################################################################### 

  /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/namentity_crm_bilstm.json 
 

  #####  Load JSON data_pars 

  {
  "data_info":{
    "data_path":"dataset\/text\/",
    "dataset":"ner_dataset.csv",
    "pass_data_pars":false,
    "train":true
  },
  "preprocessors":[
    {
      "name":"loader",
      "uri":"mlmodels.preprocess.generic:pandasDataset",
      "args":{
        "read_csv_parm":{
          "encoding":"ISO-8859-1"
        },
        "colX":[

        ],
        "coly":[

        ]
      }
    },
    {
      "uri":"mlmodels.preprocess.text_keras:Preprocess_namentity",
      "args":{
        "max_len":75
      },
      "internal_states":[
        "word_count"
      ]
    },
    {
      "name":"split_xy",
      "uri":"mlmodels.dataloader:split_xy_from_dict",
      "args":{
        "col_Xinput":[
          "X"
        ],
        "col_yinput":[
          "y"
        ]
      }
    },
    {
      "name":"split_train_test",
      "uri":"sklearn.model_selection:train_test_split",
      "args":{
        "test_size":0.5
      }
    },
    {
      "name":"saver",
      "uri":"mlmodels.dataloader:pickle_dump",
      "args":{
        "path":"mlmodels\/ztest\/ml_keras\/namentity_crm_bilstm\/data.pkl"
      }
    }
  ],
  "output":{
    "shape":[
      [
        75
      ],
      [
        75,
        18
      ]
    ],
    "max_len":75
  }
} 

  
 #####  Load DataLoader  

  
 #####  compute DataLoader  

  URL:  mlmodels.preprocess.generic:pandasDataset {'read_csv_parm': {'encoding': 'ISO-8859-1'}, 'colX': [], 'coly': []} 

  
###### load_callable_from_uri LOADED <class 'mlmodels.preprocess.generic.pandasDataset'> 
cls_name : pandasDataset

  URL:  mlmodels.preprocess.text_keras:Preprocess_namentity {'max_len': 75} 

  
###### load_callable_from_uri LOADED <class 'mlmodels.preprocess.text_keras.Preprocess_namentity'> 
cls_name : Preprocess_namentity

  
 Object Creation 

  
 Object Compute 

  
 Object get_data 

  URL:  mlmodels.dataloader:split_xy_from_dict {'col_Xinput': ['X'], 'col_yinput': ['y']} 

  
###### load_callable_from_uri LOADED <function split_xy_from_dict at 0x7f383e845e18> 

  
 ######### postional parameters :  ['out'] 

  
 ######### Execute : preprocessor_func <function split_xy_from_dict at 0x7f383e845e18> 

  URL:  sklearn.model_selection:train_test_split {'test_size': 0.5} 

  
###### load_callable_from_uri LOADED <function train_test_split at 0x7f38a9dfc048> 

  
 ######### postional parameters :  [] 

  
 ######### Execute : preprocessor_func <function train_test_split at 0x7f38a9dfc048> 

  URL:  mlmodels.dataloader:pickle_dump {'path': 'mlmodels/ztest/ml_keras/namentity_crm_bilstm/data.pkl'} 

  
###### load_callable_from_uri LOADED <function pickle_dump at 0x7f38c3b2ae18> 

  
 ######### postional parameters :  ['t'] 

  
 ######### Execute : preprocessor_func <function pickle_dump at 0x7f38c3b2ae18> 
Error /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/namentity_crm_bilstm.json [Errno 2] No such file or directory: 'mlmodels/ztest/ml_keras/namentity_crm_bilstm/data.pkl'

  




 #################################################################################################### 

  /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor/torchhub_cnn_dataloader.json 
 

  #####  Load JSON data_pars 

  {
  "data_info":{
    "data_path":"dataset\/vision\/MNIST",
    "dataset":"MNIST",
    "data_type":"tch_dataset",
    "batch_size":10,
    "train":true
  },
  "preprocessors":[
    {
      "name":"tch_dataset_start",
      "uri":"mlmodels.preprocess.generic:get_dataset_torch",
      "args":{
        "dataloader":"torchvision.datasets:MNIST",
        "to_image":true,
        "transform":{
          "uri":"mlmodels.preprocess.image:torch_transform_mnist",
          "pass_data_pars":false,
          "arg":{
            "fixed_size":256,
            "path":"dataset\/vision\/MNIST\/"
          }
        },
        "shuffle":true,
        "download":true
      }
    }
  ]
} 

  
 #####  Load DataLoader  

  
 #####  compute DataLoader  

  URL:  mlmodels.preprocess.generic:get_dataset_torch {'dataloader': 'torchvision.datasets:MNIST', 'to_image': True, 'transform': {'uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'pass_data_pars': False, 'arg': {'fixed_size': 256, 'path': 'dataset/vision/MNIST/'}}, 'shuffle': True, 'download': True} 

  
###### load_callable_from_uri LOADED <function get_dataset_torch at 0x7f385767b8c8> 

  
 ######### postional parameters :  ['data_info'] 

  
 ######### Execute : preprocessor_func <function get_dataset_torch at 0x7f385767b8c8> 

  function with postional parmater data_info <function get_dataset_torch at 0x7f385767b8c8> , (data_info, **args) 

  #### If transformer URI is Provided {'uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'pass_data_pars': False, 'arg': {'fixed_size': 256, 'path': 'dataset/vision/MNIST/'}} 

  #### Loading dataloader URI 

  dataset :  <class 'torchvision.datasets.mnist.MNIST'> 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/dataloader.py", line 452, in test_json_list
    loader.compute()
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/dataloader.py", line 258, in compute
    obj_preprocessor = preprocessor_func(**args, data_info=self.data_info)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/preprocess/generic.py", line 502, in __init__
    df = pd.read_csv(file_path, **args.get("read_csv_parm",{}))
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/pandas/io/parsers.py", line 685, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/pandas/io/parsers.py", line 457, in _read
    parser = TextFileReader(fp_or_buf, **kwds)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/pandas/io/parsers.py", line 895, in __init__
    self._make_engine(self.engine)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/pandas/io/parsers.py", line 1135, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/pandas/io/parsers.py", line 1917, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas/_libs/parsers.pyx", line 382, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas/_libs/parsers.pyx", line 689, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: [Errno 2] File b'mlmodels/dataset/text/ag_news_csv/train/mlmodels/dataset/text/ag_news_csv.csv' does not exist: b'mlmodels/dataset/text/ag_news_csv/train/mlmodels/dataset/text/ag_news_csv.csv'
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/dataloader.py", line 452, in test_json_list
    loader.compute()
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/dataloader.py", line 258, in compute
    obj_preprocessor = preprocessor_func(**args, data_info=self.data_info)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/preprocess/generic.py", line 502, in __init__
    df = pd.read_csv(file_path, **args.get("read_csv_parm",{}))
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/pandas/io/parsers.py", line 685, in parser_f
    return _read(filepath_or_buffer, kwds)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/pandas/io/parsers.py", line 457, in _read
    parser = TextFileReader(fp_or_buf, **kwds)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/pandas/io/parsers.py", line 895, in __init__
    self._make_engine(self.engine)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/pandas/io/parsers.py", line 1135, in _make_engine
    self._engine = CParserWrapper(self.f, **self.options)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/pandas/io/parsers.py", line 1917, in __init__
    self._reader = parsers.TextReader(src, **kwds)
  File "pandas/_libs/parsers.pyx", line 382, in pandas._libs.parsers.TextReader.__cinit__
  File "pandas/_libs/parsers.pyx", line 689, in pandas._libs.parsers.TextReader._setup_parser_source
FileNotFoundError: [Errno 2] File b'mlmodels/dataset/text/ag_news_csv/train/mlmodels/dataset/text/ag_news_csv.csv' does not exist: b'mlmodels/dataset/text/ag_news_csv/train/mlmodels/dataset/text/ag_news_csv.csv'
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/dataloader.py", line 452, in test_json_list
    loader.compute()
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/dataloader.py", line 258, in compute
    obj_preprocessor = preprocessor_func(**args, data_info=self.data_info)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/preprocess/generic.py", line 607, in __init__
    data            = np.load( file_path,**args.get("numpy_loader_args", {}))
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/numpy/lib/npyio.py", line 428, in load
    fid = open(os_fspath(file), "rb")
FileNotFoundError: [Errno 2] No such file or directory: 'train/mlmodels/dataset/text/imdb.npz'
Using TensorFlow backend.
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/dataloader.py", line 452, in test_json_list
    loader.compute()
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/dataloader.py", line 301, in compute
    out_tmp = preprocessor_func(input_tmp, **args)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/dataloader.py", line 93, in pickle_dump
    with open(kwargs["path"], "wb") as fi:
FileNotFoundError: [Errno 2] No such file or directory: 'mlmodels/ztest/ml_keras/namentity_crm_bilstm/data.pkl'
0it [00:00, ?it/s]  0%|          | 0/9912422 [00:00<?, ?it/s] 31%|███▏      | 3121152/9912422 [00:00<00:00, 30443476.74it/s]9920512it [00:00, 36841896.50it/s]                             
0it [00:00, ?it/s]32768it [00:00, 496666.17it/s]
0it [00:00, ?it/s]  3%|▎         | 49152/1648877 [00:00<00:03, 465875.81it/s]1654784it [00:00, 11633273.92it/s]                         
0it [00:00, ?it/s]8192it [00:00, 177126.66it/s]Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz to dataset/vision/MNIST/MNIST/raw/train-images-idx3-ubyte.gz
Extracting dataset/vision/MNIST/MNIST/raw/train-images-idx3-ubyte.gz to dataset/vision/MNIST/MNIST/raw
Downloading http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz to dataset/vision/MNIST/MNIST/raw/train-labels-idx1-ubyte.gz
Extracting dataset/vision/MNIST/MNIST/raw/train-labels-idx1-ubyte.gz to dataset/vision/MNIST/MNIST/raw
Downloading http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz to dataset/vision/MNIST/MNIST/raw/t10k-images-idx3-ubyte.gz
Extracting dataset/vision/MNIST/MNIST/raw/t10k-images-idx3-ubyte.gz to dataset/vision/MNIST/MNIST/raw
Downloading http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz to dataset/vision/MNIST/MNIST/raw/t10k-labels-idx1-ubyte.gz
Extracting dataset/vision/MNIST/MNIST/raw/t10k-labels-idx1-ubyte.gz to dataset/vision/MNIST/MNIST/raw
Processing...
Done!

  
 #####  get_Data DataLoader  

  ((<mlmodels.preprocess.generic.Custom_DataLoader object at 0x7f3854be9550>, <mlmodels.preprocess.generic.Custom_DataLoader object at 0x7f38566419e8>), {}) 

  




 #################################################################################################### 

  /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor/model_list_CIFAR.json 
 

  #####  Load JSON data_pars 

  {
  "data_info":{
    "data_path":"dataset\/vision\/cifar10\/",
    "dataset":"CIFAR10",
    "data_type":"tf_dataset",
    "batch_size":10,
    "train":true
  },
  "preprocessors":[
    {
      "name":"tf_dataset_start",
      "uri":"mlmodels.preprocess.generic:tf_dataset_download",
      "arg":{
        "train_samples":2000,
        "test_samples":500,
        "shuffle":true,
        "download":true
      }
    },
    {
      "uri":"mlmodels.preprocess.generic:get_dataset_torch",
      "args":{
        "dataloader":"mlmodels.preprocess.generic:NumpyDataset",
        "to_image":true,
        "transform":{
          "uri":"mlmodels.preprocess.image:torch_transform_generic",
          "pass_data_pars":false,
          "arg":{
            "fixed_size":256
          }
        },
        "shuffle":true,
        "download":true
      }
    }
  ]
} 

  
 #####  Load DataLoader  

  
 #####  compute DataLoader  

  URL:  mlmodels.preprocess.generic:tf_dataset_download {} 

  
###### load_callable_from_uri LOADED <function tf_dataset_download at 0x7f385767b510> 

  
 ######### postional parameters :  ['data_info'] 

  
 ######### Execute : preprocessor_func <function tf_dataset_download at 0x7f385767b510> 

  function with postional parmater data_info <function tf_dataset_download at 0x7f385767b510> , (data_info, **args) 

  CIFAR10 

  Dataset Name is :  cifar10 

Dl Completed...: 0 url [00:00, ? url/s]
Dl Size...: 0 MiB [00:00, ? MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...: 0 MiB [00:00, ? MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[A/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/urllib3/connectionpool.py:986: InsecureRequestWarning: Unverified HTTPS request is being made to host 'www.cs.toronto.edu'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  InsecureRequestWarning,
Dl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:   0%|          | 0/162 [00:00<?, ? MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[A
Dl Size...:   1%|          | 1/162 [00:00<01:01,  2.62 MiB/s][ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:   1%|          | 1/162 [00:00<01:01,  2.62 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:   1%|          | 2/162 [00:00<01:00,  2.62 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:   2%|▏         | 3/162 [00:00<01:00,  2.62 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:   2%|▏         | 4/162 [00:00<01:00,  2.62 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:   3%|▎         | 5/162 [00:00<00:59,  2.62 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:   4%|▎         | 6/162 [00:00<00:59,  2.62 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:   4%|▍         | 7/162 [00:00<00:59,  2.62 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[A
Dl Size...:   5%|▍         | 8/162 [00:00<00:41,  3.68 MiB/s][ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:   5%|▍         | 8/162 [00:00<00:41,  3.68 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:   6%|▌         | 9/162 [00:00<00:41,  3.68 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:   6%|▌         | 10/162 [00:00<00:41,  3.68 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:   7%|▋         | 11/162 [00:00<00:41,  3.68 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:   7%|▋         | 12/162 [00:00<00:40,  3.68 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:   8%|▊         | 13/162 [00:00<00:40,  3.68 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:   9%|▊         | 14/162 [00:00<00:40,  3.68 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:   9%|▉         | 15/162 [00:00<00:39,  3.68 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  10%|▉         | 16/162 [00:00<00:39,  3.68 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[A
Dl Size...:  10%|█         | 17/162 [00:00<00:28,  5.16 MiB/s][ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  10%|█         | 17/162 [00:00<00:28,  5.16 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  11%|█         | 18/162 [00:00<00:27,  5.16 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  12%|█▏        | 19/162 [00:00<00:27,  5.16 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  12%|█▏        | 20/162 [00:00<00:27,  5.16 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  13%|█▎        | 21/162 [00:00<00:27,  5.16 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  14%|█▎        | 22/162 [00:00<00:27,  5.16 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  14%|█▍        | 23/162 [00:00<00:26,  5.16 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  15%|█▍        | 24/162 [00:00<00:26,  5.16 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[A
Dl Size...:  15%|█▌        | 25/162 [00:00<00:19,  7.17 MiB/s][ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  15%|█▌        | 25/162 [00:00<00:19,  7.17 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  16%|█▌        | 26/162 [00:00<00:18,  7.17 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  17%|█▋        | 27/162 [00:00<00:18,  7.17 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  17%|█▋        | 28/162 [00:00<00:18,  7.17 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  18%|█▊        | 29/162 [00:00<00:18,  7.17 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  19%|█▊        | 30/162 [00:00<00:18,  7.17 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  19%|█▉        | 31/162 [00:00<00:18,  7.17 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  20%|█▉        | 32/162 [00:00<00:18,  7.17 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  20%|██        | 33/162 [00:00<00:17,  7.17 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[A
Dl Size...:  21%|██        | 34/162 [00:00<00:12,  9.87 MiB/s][ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  21%|██        | 34/162 [00:00<00:12,  9.87 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  22%|██▏       | 35/162 [00:00<00:12,  9.87 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  22%|██▏       | 36/162 [00:00<00:12,  9.87 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  23%|██▎       | 37/162 [00:00<00:12,  9.87 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  23%|██▎       | 38/162 [00:00<00:12,  9.87 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  24%|██▍       | 39/162 [00:00<00:12,  9.87 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  25%|██▍       | 40/162 [00:00<00:12,  9.87 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  25%|██▌       | 41/162 [00:00<00:12,  9.87 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  26%|██▌       | 42/162 [00:00<00:12,  9.87 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[A
Dl Size...:  27%|██▋       | 43/162 [00:00<00:08, 13.36 MiB/s][ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  27%|██▋       | 43/162 [00:00<00:08, 13.36 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  27%|██▋       | 44/162 [00:00<00:08, 13.36 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  28%|██▊       | 45/162 [00:00<00:08, 13.36 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  28%|██▊       | 46/162 [00:00<00:08, 13.36 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  29%|██▉       | 47/162 [00:00<00:08, 13.36 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:00<?, ? url/s]
Dl Size...:  30%|██▉       | 48/162 [00:00<00:08, 13.36 MiB/s][A

Extraction completed...: 0 file [00:00, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  30%|███       | 49/162 [00:01<00:08, 13.36 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  31%|███       | 50/162 [00:01<00:08, 13.36 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  31%|███▏      | 51/162 [00:01<00:08, 13.36 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[A
Dl Size...:  32%|███▏      | 52/162 [00:01<00:06, 17.86 MiB/s][ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  32%|███▏      | 52/162 [00:01<00:06, 17.86 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  33%|███▎      | 53/162 [00:01<00:06, 17.86 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  33%|███▎      | 54/162 [00:01<00:06, 17.86 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  34%|███▍      | 55/162 [00:01<00:05, 17.86 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  35%|███▍      | 56/162 [00:01<00:05, 17.86 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  35%|███▌      | 57/162 [00:01<00:05, 17.86 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  36%|███▌      | 58/162 [00:01<00:05, 17.86 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  36%|███▋      | 59/162 [00:01<00:05, 17.86 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[A
Dl Size...:  37%|███▋      | 60/162 [00:01<00:04, 23.29 MiB/s][ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  37%|███▋      | 60/162 [00:01<00:04, 23.29 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  38%|███▊      | 61/162 [00:01<00:04, 23.29 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  38%|███▊      | 62/162 [00:01<00:04, 23.29 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  39%|███▉      | 63/162 [00:01<00:04, 23.29 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  40%|███▉      | 64/162 [00:01<00:04, 23.29 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  40%|████      | 65/162 [00:01<00:04, 23.29 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  41%|████      | 66/162 [00:01<00:04, 23.29 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  41%|████▏     | 67/162 [00:01<00:04, 23.29 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[A
Dl Size...:  42%|████▏     | 68/162 [00:01<00:03, 29.45 MiB/s][ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  42%|████▏     | 68/162 [00:01<00:03, 29.45 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  43%|████▎     | 69/162 [00:01<00:03, 29.45 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  43%|████▎     | 70/162 [00:01<00:03, 29.45 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  44%|████▍     | 71/162 [00:01<00:03, 29.45 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  44%|████▍     | 72/162 [00:01<00:03, 29.45 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  45%|████▌     | 73/162 [00:01<00:03, 29.45 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  46%|████▌     | 74/162 [00:01<00:02, 29.45 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  46%|████▋     | 75/162 [00:01<00:02, 29.45 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  47%|████▋     | 76/162 [00:01<00:02, 29.45 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[A
Dl Size...:  48%|████▊     | 77/162 [00:01<00:02, 36.50 MiB/s][ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  48%|████▊     | 77/162 [00:01<00:02, 36.50 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  48%|████▊     | 78/162 [00:01<00:02, 36.50 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  49%|████▉     | 79/162 [00:01<00:02, 36.50 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  49%|████▉     | 80/162 [00:01<00:02, 36.50 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  50%|█████     | 81/162 [00:01<00:02, 36.50 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  51%|█████     | 82/162 [00:01<00:02, 36.50 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  51%|█████     | 83/162 [00:01<00:02, 36.50 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  52%|█████▏    | 84/162 [00:01<00:02, 36.50 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[A
Dl Size...:  52%|█████▏    | 85/162 [00:01<00:01, 43.24 MiB/s][ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  52%|█████▏    | 85/162 [00:01<00:01, 43.24 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  53%|█████▎    | 86/162 [00:01<00:01, 43.24 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  54%|█████▎    | 87/162 [00:01<00:01, 43.24 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  54%|█████▍    | 88/162 [00:01<00:01, 43.24 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  55%|█████▍    | 89/162 [00:01<00:01, 43.24 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  56%|█████▌    | 90/162 [00:01<00:01, 43.24 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  56%|█████▌    | 91/162 [00:01<00:01, 43.24 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  57%|█████▋    | 92/162 [00:01<00:01, 43.24 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  57%|█████▋    | 93/162 [00:01<00:01, 43.24 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[A
Dl Size...:  58%|█████▊    | 94/162 [00:01<00:01, 50.48 MiB/s][ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  58%|█████▊    | 94/162 [00:01<00:01, 50.48 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  59%|█████▊    | 95/162 [00:01<00:01, 50.48 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  59%|█████▉    | 96/162 [00:01<00:01, 50.48 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  60%|█████▉    | 97/162 [00:01<00:01, 50.48 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  60%|██████    | 98/162 [00:01<00:01, 50.48 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  61%|██████    | 99/162 [00:01<00:01, 50.48 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  62%|██████▏   | 100/162 [00:01<00:01, 50.48 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  62%|██████▏   | 101/162 [00:01<00:01, 50.48 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  63%|██████▎   | 102/162 [00:01<00:01, 50.48 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[A
Dl Size...:  64%|██████▎   | 103/162 [00:01<00:01, 56.62 MiB/s][ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  64%|██████▎   | 103/162 [00:01<00:01, 56.62 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  64%|██████▍   | 104/162 [00:01<00:01, 56.62 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  65%|██████▍   | 105/162 [00:01<00:01, 56.62 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  65%|██████▌   | 106/162 [00:01<00:00, 56.62 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  66%|██████▌   | 107/162 [00:01<00:00, 56.62 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  67%|██████▋   | 108/162 [00:01<00:00, 56.62 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  67%|██████▋   | 109/162 [00:01<00:00, 56.62 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  68%|██████▊   | 110/162 [00:01<00:00, 56.62 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  69%|██████▊   | 111/162 [00:01<00:00, 56.62 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[A
Dl Size...:  69%|██████▉   | 112/162 [00:01<00:00, 62.48 MiB/s][ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  69%|██████▉   | 112/162 [00:01<00:00, 62.48 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  70%|██████▉   | 113/162 [00:01<00:00, 62.48 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  70%|███████   | 114/162 [00:01<00:00, 62.48 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  71%|███████   | 115/162 [00:01<00:00, 62.48 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  72%|███████▏  | 116/162 [00:01<00:00, 62.48 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  72%|███████▏  | 117/162 [00:01<00:00, 62.48 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  73%|███████▎  | 118/162 [00:01<00:00, 62.48 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  73%|███████▎  | 119/162 [00:01<00:00, 62.48 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  74%|███████▍  | 120/162 [00:01<00:00, 62.48 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[A
Dl Size...:  75%|███████▍  | 121/162 [00:01<00:00, 66.76 MiB/s][ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  75%|███████▍  | 121/162 [00:01<00:00, 66.76 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  75%|███████▌  | 122/162 [00:01<00:00, 66.76 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  76%|███████▌  | 123/162 [00:01<00:00, 66.76 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  77%|███████▋  | 124/162 [00:01<00:00, 66.76 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  77%|███████▋  | 125/162 [00:01<00:00, 66.76 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  78%|███████▊  | 126/162 [00:01<00:00, 66.76 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  78%|███████▊  | 127/162 [00:01<00:00, 66.76 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:01<?, ? url/s]
Dl Size...:  79%|███████▉  | 128/162 [00:01<00:00, 66.76 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  80%|███████▉  | 129/162 [00:01<00:00, 66.76 MiB/s][A

Extraction completed...: 0 file [00:01, ? file/s][A[A
Dl Size...:  80%|████████  | 130/162 [00:02<00:00, 71.03 MiB/s][ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  80%|████████  | 130/162 [00:02<00:00, 71.03 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  81%|████████  | 131/162 [00:02<00:00, 71.03 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  81%|████████▏ | 132/162 [00:02<00:00, 71.03 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  82%|████████▏ | 133/162 [00:02<00:00, 71.03 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  83%|████████▎ | 134/162 [00:02<00:00, 71.03 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  83%|████████▎ | 135/162 [00:02<00:00, 71.03 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  84%|████████▍ | 136/162 [00:02<00:00, 71.03 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  85%|████████▍ | 137/162 [00:02<00:00, 71.03 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  85%|████████▌ | 138/162 [00:02<00:00, 71.03 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[A
Dl Size...:  86%|████████▌ | 139/162 [00:02<00:00, 73.03 MiB/s][ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  86%|████████▌ | 139/162 [00:02<00:00, 73.03 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  86%|████████▋ | 140/162 [00:02<00:00, 73.03 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  87%|████████▋ | 141/162 [00:02<00:00, 73.03 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  88%|████████▊ | 142/162 [00:02<00:00, 73.03 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  88%|████████▊ | 143/162 [00:02<00:00, 73.03 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  89%|████████▉ | 144/162 [00:02<00:00, 73.03 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  90%|████████▉ | 145/162 [00:02<00:00, 73.03 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  90%|█████████ | 146/162 [00:02<00:00, 73.03 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  91%|█████████ | 147/162 [00:02<00:00, 73.03 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[A
Dl Size...:  91%|█████████▏| 148/162 [00:02<00:00, 76.25 MiB/s][ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  91%|█████████▏| 148/162 [00:02<00:00, 76.25 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  92%|█████████▏| 149/162 [00:02<00:00, 76.25 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  93%|█████████▎| 150/162 [00:02<00:00, 76.25 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  93%|█████████▎| 151/162 [00:02<00:00, 76.25 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  94%|█████████▍| 152/162 [00:02<00:00, 76.25 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  94%|█████████▍| 153/162 [00:02<00:00, 76.25 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  95%|█████████▌| 154/162 [00:02<00:00, 76.25 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  96%|█████████▌| 155/162 [00:02<00:00, 76.25 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  96%|█████████▋| 156/162 [00:02<00:00, 76.25 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[A
Dl Size...:  97%|█████████▋| 157/162 [00:02<00:00, 77.38 MiB/s][ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  97%|█████████▋| 157/162 [00:02<00:00, 77.38 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  98%|█████████▊| 158/162 [00:02<00:00, 77.38 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  98%|█████████▊| 159/162 [00:02<00:00, 77.38 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  99%|█████████▉| 160/162 [00:02<00:00, 77.38 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...:  99%|█████████▉| 161/162 [00:02<00:00, 77.38 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...:   0%|          | 0/1 [00:02<?, ? url/s]
Dl Size...: 100%|██████████| 162/162 [00:02<00:00, 77.38 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...: 100%|██████████| 1/1 [00:02<00:00,  2.40s/ url]Dl Completed...: 100%|██████████| 1/1 [00:02<00:00,  2.40s/ url]
Dl Size...: 100%|██████████| 162/162 [00:02<00:00, 77.38 MiB/s][A

Extraction completed...: 0 file [00:02, ? file/s][A[ADl Completed...: 100%|██████████| 1/1 [00:02<00:00,  2.40s/ url]
Dl Size...: 100%|██████████| 162/162 [00:02<00:00, 77.38 MiB/s][A

Extraction completed...:   0%|          | 0/1 [00:02<?, ? file/s][A[A

Extraction completed...: 100%|██████████| 1/1 [00:04<00:00,  4.48s/ file][A[ADl Completed...: 100%|██████████| 1/1 [00:04<00:00,  2.40s/ url]
Dl Size...: 100%|██████████| 162/162 [00:04<00:00, 77.38 MiB/s][A

Extraction completed...: 100%|██████████| 1/1 [00:04<00:00,  4.48s/ file][A[AExtraction completed...: 100%|██████████| 1/1 [00:04<00:00,  4.48s/ file]
Dl Size...: 100%|██████████| 162/162 [00:04<00:00, 36.14 MiB/s]
Dl Completed...: 100%|██████████| 1/1 [00:04<00:00,  4.48s/ url]
0 examples [00:00, ? examples/s]2020-06-19 00:09:25.878502: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 AVX512F FMA
2020-06-19 00:09:25.892637: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2095074999 Hz
2020-06-19 00:09:25.894414: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x55e001e4f550 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-06-19 00:09:25.894444: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
1 examples [00:00,  2.23 examples/s]111 examples [00:00,  3.18 examples/s]220 examples [00:00,  4.54 examples/s]329 examples [00:00,  6.47 examples/s]440 examples [00:00,  9.22 examples/s]551 examples [00:00, 13.13 examples/s]662 examples [00:01, 18.66 examples/s]770 examples [00:01, 26.46 examples/s]881 examples [00:01, 37.41 examples/s]992 examples [00:01, 52.68 examples/s]1104 examples [00:01, 73.76 examples/s]1213 examples [00:01, 102.40 examples/s]1323 examples [00:01, 140.67 examples/s]1434 examples [00:01, 190.58 examples/s]1545 examples [00:01, 253.53 examples/s]1655 examples [00:01, 328.85 examples/s]1764 examples [00:02, 415.60 examples/s]1873 examples [00:02, 508.63 examples/s]1983 examples [00:02, 606.36 examples/s]2093 examples [00:02, 700.37 examples/s]2204 examples [00:02, 787.00 examples/s]2314 examples [00:02, 845.96 examples/s]2422 examples [00:02, 883.14 examples/s]2527 examples [00:02, 900.67 examples/s]2629 examples [00:02, 923.52 examples/s]2739 examples [00:02, 969.68 examples/s]2847 examples [00:03, 998.94 examples/s]2957 examples [00:03, 1026.76 examples/s]3069 examples [00:03, 1050.89 examples/s]3181 examples [00:03, 1069.29 examples/s]3291 examples [00:03, 1078.28 examples/s]3401 examples [00:03, 1074.56 examples/s]3510 examples [00:03, 1075.18 examples/s]3620 examples [00:03, 1079.70 examples/s]3729 examples [00:03, 1081.93 examples/s]3838 examples [00:04, 1066.13 examples/s]3949 examples [00:04, 1078.68 examples/s]4058 examples [00:04, 1080.25 examples/s]4169 examples [00:04, 1087.40 examples/s]4280 examples [00:04, 1091.91 examples/s]4391 examples [00:04, 1095.80 examples/s]4502 examples [00:04, 1098.29 examples/s]4612 examples [00:04, 1095.88 examples/s]4722 examples [00:04, 1094.11 examples/s]4832 examples [00:04, 1095.64 examples/s]4943 examples [00:05, 1098.75 examples/s]5054 examples [00:05, 1101.25 examples/s]5165 examples [00:05, 1099.20 examples/s]5275 examples [00:05, 1087.98 examples/s]5384 examples [00:05, 1085.46 examples/s]5494 examples [00:05, 1088.15 examples/s]5603 examples [00:05, 1059.08 examples/s]5710 examples [00:05, 1059.95 examples/s]5819 examples [00:05, 1068.45 examples/s]5929 examples [00:05, 1075.05 examples/s]6037 examples [00:06, 1048.28 examples/s]6146 examples [00:06, 1058.53 examples/s]6253 examples [00:06, 1051.74 examples/s]6362 examples [00:06, 1062.56 examples/s]6470 examples [00:06, 1065.66 examples/s]6578 examples [00:06, 1068.89 examples/s]6686 examples [00:06, 1071.62 examples/s]6794 examples [00:06, 1070.90 examples/s]6902 examples [00:06, 1065.86 examples/s]7009 examples [00:06, 1061.29 examples/s]7117 examples [00:07, 1065.36 examples/s]7224 examples [00:07, 1063.59 examples/s]7331 examples [00:07, 1049.06 examples/s]7436 examples [00:07, 1033.82 examples/s]7540 examples [00:07, 1034.42 examples/s]7647 examples [00:07, 1042.51 examples/s]7752 examples [00:07, 1037.91 examples/s]7859 examples [00:07, 1045.50 examples/s]7964 examples [00:07, 1040.86 examples/s]8073 examples [00:07, 1054.85 examples/s]8183 examples [00:08, 1066.09 examples/s]8291 examples [00:08, 1070.21 examples/s]8399 examples [00:08, 1068.73 examples/s]8509 examples [00:08, 1076.17 examples/s]8618 examples [00:08, 1077.99 examples/s]8728 examples [00:08, 1082.82 examples/s]8837 examples [00:08, 1079.53 examples/s]8945 examples [00:08, 1077.15 examples/s]9053 examples [00:08, 1077.92 examples/s]9163 examples [00:08, 1081.99 examples/s]9272 examples [00:09, 1040.85 examples/s]9380 examples [00:09, 1050.87 examples/s]9487 examples [00:09, 1055.71 examples/s]9597 examples [00:09, 1067.48 examples/s]9705 examples [00:09, 1068.38 examples/s]9813 examples [00:09, 1070.60 examples/s]9921 examples [00:09, 1068.81 examples/s]10028 examples [00:09, 1000.67 examples/s]10136 examples [00:09, 1021.08 examples/s]10239 examples [00:10, 999.07 examples/s] 10348 examples [00:10, 1022.45 examples/s]10454 examples [00:10, 1032.97 examples/s]10563 examples [00:10, 1048.87 examples/s]10673 examples [00:10, 1061.65 examples/s]10783 examples [00:10, 1070.98 examples/s]10892 examples [00:10, 1076.51 examples/s]11000 examples [00:10, 1073.59 examples/s]11108 examples [00:10, 1008.61 examples/s]11218 examples [00:10, 1033.97 examples/s]11327 examples [00:11, 1050.07 examples/s]11438 examples [00:11, 1064.70 examples/s]11545 examples [00:11, 1063.47 examples/s]11655 examples [00:11, 1073.26 examples/s]11767 examples [00:11, 1085.03 examples/s]11878 examples [00:11, 1091.38 examples/s]11988 examples [00:11, 1087.24 examples/s]12097 examples [00:11, 1075.34 examples/s]12206 examples [00:11, 1077.90 examples/s]12314 examples [00:11, 1077.63 examples/s]12425 examples [00:12, 1087.07 examples/s]12537 examples [00:12, 1092.37 examples/s]12647 examples [00:12, 1066.94 examples/s]12756 examples [00:12, 1073.03 examples/s]12866 examples [00:12, 1079.41 examples/s]12978 examples [00:12, 1089.25 examples/s]13088 examples [00:12, 1081.37 examples/s]13197 examples [00:12, 1082.91 examples/s]13306 examples [00:12, 1069.61 examples/s]13414 examples [00:12, 1064.37 examples/s]13526 examples [00:13, 1078.85 examples/s]13637 examples [00:13, 1086.46 examples/s]13746 examples [00:13, 1083.33 examples/s]13855 examples [00:13, 1070.99 examples/s]13965 examples [00:13, 1077.12 examples/s]14078 examples [00:13, 1090.46 examples/s]14188 examples [00:13, 1091.76 examples/s]14298 examples [00:13, 1050.44 examples/s]14408 examples [00:13, 1062.09 examples/s]14518 examples [00:14, 1072.01 examples/s]14626 examples [00:14, 1069.37 examples/s]14734 examples [00:14, 1071.64 examples/s]14843 examples [00:14, 1076.40 examples/s]14953 examples [00:14, 1082.27 examples/s]15065 examples [00:14, 1090.78 examples/s]15176 examples [00:14, 1094.20 examples/s]15287 examples [00:14, 1096.01 examples/s]15398 examples [00:14, 1097.42 examples/s]15508 examples [00:14, 1087.79 examples/s]15618 examples [00:15, 1088.64 examples/s]15727 examples [00:15, 1086.52 examples/s]15838 examples [00:15, 1093.21 examples/s]15948 examples [00:15, 1057.25 examples/s]16054 examples [00:15, 1056.84 examples/s]16164 examples [00:15, 1067.02 examples/s]16275 examples [00:15, 1076.90 examples/s]16385 examples [00:15, 1080.11 examples/s]16494 examples [00:15, 1078.17 examples/s]16603 examples [00:15, 1081.15 examples/s]16715 examples [00:16, 1090.30 examples/s]16825 examples [00:16, 1079.02 examples/s]16934 examples [00:16, 1081.56 examples/s]17046 examples [00:16, 1091.01 examples/s]17156 examples [00:16, 1086.31 examples/s]17267 examples [00:16, 1091.04 examples/s]17377 examples [00:16, 1085.49 examples/s]17488 examples [00:16, 1090.63 examples/s]17598 examples [00:16, 1089.38 examples/s]17707 examples [00:16, 1086.27 examples/s]17818 examples [00:17, 1093.27 examples/s]17928 examples [00:17, 1086.68 examples/s]18037 examples [00:17, 1053.56 examples/s]18143 examples [00:17, 1036.59 examples/s]18252 examples [00:17, 1050.07 examples/s]18358 examples [00:17, 1050.81 examples/s]18464 examples [00:17, 1048.71 examples/s]18574 examples [00:17, 1060.95 examples/s]18681 examples [00:17, 1048.68 examples/s]18788 examples [00:17, 1054.01 examples/s]18898 examples [00:18, 1064.95 examples/s]19005 examples [00:18, 1053.28 examples/s]19114 examples [00:18, 1061.29 examples/s]19221 examples [00:18, 1034.77 examples/s]19325 examples [00:18, 1029.29 examples/s]19435 examples [00:18, 1047.23 examples/s]19545 examples [00:18, 1060.77 examples/s]19655 examples [00:18, 1070.93 examples/s]19763 examples [00:18, 1070.85 examples/s]19871 examples [00:18, 1063.68 examples/s]19980 examples [00:19, 1071.31 examples/s]20088 examples [00:19, 1013.54 examples/s]20191 examples [00:19, 1009.64 examples/s]20297 examples [00:19, 1024.05 examples/s]20404 examples [00:19, 1035.67 examples/s]20512 examples [00:19, 1046.26 examples/s]20622 examples [00:19, 1060.43 examples/s]20732 examples [00:19, 1070.05 examples/s]20840 examples [00:19, 1067.21 examples/s]20947 examples [00:20, 1066.99 examples/s]21057 examples [00:20, 1075.83 examples/s]21167 examples [00:20, 1080.52 examples/s]21277 examples [00:20, 1085.04 examples/s]21386 examples [00:20, 1081.80 examples/s]21497 examples [00:20, 1087.44 examples/s]21609 examples [00:20, 1096.46 examples/s]21719 examples [00:20, 1095.61 examples/s]21829 examples [00:20, 1095.08 examples/s]21939 examples [00:20, 1089.46 examples/s]22048 examples [00:21, 1087.35 examples/s]22158 examples [00:21, 1089.75 examples/s]22268 examples [00:21, 1091.27 examples/s]22379 examples [00:21, 1096.23 examples/s]22489 examples [00:21, 1059.41 examples/s]22600 examples [00:21, 1071.41 examples/s]22710 examples [00:21, 1079.71 examples/s]22819 examples [00:21, 1082.74 examples/s]22930 examples [00:21, 1090.15 examples/s]23040 examples [00:21, 1067.02 examples/s]23147 examples [00:22, 1066.62 examples/s]23257 examples [00:22, 1074.36 examples/s]23366 examples [00:22, 1077.45 examples/s]23477 examples [00:22, 1084.49 examples/s]23586 examples [00:22, 1075.53 examples/s]23694 examples [00:22, 1073.21 examples/s]23803 examples [00:22, 1076.27 examples/s]23914 examples [00:22, 1084.88 examples/s]24023 examples [00:22, 1075.83 examples/s]24131 examples [00:22, 1040.64 examples/s]24240 examples [00:23, 1053.64 examples/s]24350 examples [00:23, 1064.32 examples/s]24458 examples [00:23, 1066.78 examples/s]24566 examples [00:23, 1070.12 examples/s]24674 examples [00:23, 1070.07 examples/s]24782 examples [00:23, 1044.36 examples/s]24891 examples [00:23, 1055.85 examples/s]25000 examples [00:23, 1065.64 examples/s]25107 examples [00:23, 1066.49 examples/s]25214 examples [00:23, 1065.50 examples/s]25321 examples [00:24, 1063.54 examples/s]25428 examples [00:24, 1038.06 examples/s]25537 examples [00:24, 1051.80 examples/s]25646 examples [00:24, 1062.35 examples/s]25753 examples [00:24, 1017.08 examples/s]25863 examples [00:24, 1039.41 examples/s]25974 examples [00:24, 1058.26 examples/s]26084 examples [00:24, 1068.10 examples/s]26193 examples [00:24, 1071.68 examples/s]26302 examples [00:25, 1074.89 examples/s]26411 examples [00:25, 1077.33 examples/s]26520 examples [00:25, 1080.81 examples/s]26629 examples [00:25, 1083.02 examples/s]26740 examples [00:25, 1089.02 examples/s]26849 examples [00:25, 1085.05 examples/s]26958 examples [00:25, 1079.16 examples/s]27066 examples [00:25, 1061.18 examples/s]27175 examples [00:25, 1069.50 examples/s]27284 examples [00:25, 1073.10 examples/s]27392 examples [00:26, 1071.66 examples/s]27502 examples [00:26, 1077.47 examples/s]27612 examples [00:26, 1083.62 examples/s]27721 examples [00:26, 1076.78 examples/s]27829 examples [00:26, 1076.47 examples/s]27937 examples [00:26, 1042.98 examples/s]28046 examples [00:26, 1054.62 examples/s]28156 examples [00:26, 1065.75 examples/s]28266 examples [00:26, 1075.70 examples/s]28375 examples [00:26, 1078.46 examples/s]28483 examples [00:27, 1053.65 examples/s]28592 examples [00:27, 1061.80 examples/s]28699 examples [00:27, 1063.22 examples/s]28807 examples [00:27, 1068.07 examples/s]28914 examples [00:27, 1068.53 examples/s]29021 examples [00:27, 1013.86 examples/s]29128 examples [00:27, 1029.47 examples/s]29233 examples [00:27, 1035.03 examples/s]29337 examples [00:27, 1034.90 examples/s]29444 examples [00:27, 1045.05 examples/s]29550 examples [00:28, 1048.67 examples/s]29659 examples [00:28, 1059.85 examples/s]29768 examples [00:28, 1068.24 examples/s]29878 examples [00:28, 1076.03 examples/s]29986 examples [00:28, 1039.56 examples/s]30091 examples [00:28, 991.81 examples/s] 30198 examples [00:28, 1013.53 examples/s]30307 examples [00:28, 1032.54 examples/s]30416 examples [00:28, 1047.01 examples/s]30522 examples [00:29, 1047.76 examples/s]30628 examples [00:29, 1040.73 examples/s]30736 examples [00:29, 1051.80 examples/s]30845 examples [00:29, 1061.77 examples/s]30953 examples [00:29, 1065.52 examples/s]31060 examples [00:29, 1062.10 examples/s]31167 examples [00:29, 1044.91 examples/s]31272 examples [00:29, 1045.07 examples/s]31381 examples [00:29, 1054.73 examples/s]31491 examples [00:29, 1065.83 examples/s]31598 examples [00:30, 1065.89 examples/s]31706 examples [00:30, 1067.83 examples/s]31816 examples [00:30, 1075.64 examples/s]31924 examples [00:30, 1072.27 examples/s]32032 examples [00:30, 1026.64 examples/s]32136 examples [00:30, 1005.33 examples/s]32237 examples [00:30, 996.61 examples/s] 32346 examples [00:30, 1020.64 examples/s]32455 examples [00:30, 1039.90 examples/s]32566 examples [00:30, 1059.77 examples/s]32673 examples [00:31, 1061.58 examples/s]32781 examples [00:31, 1064.57 examples/s]32889 examples [00:31, 1069.03 examples/s]32998 examples [00:31, 1075.01 examples/s]33106 examples [00:31, 1072.78 examples/s]33215 examples [00:31, 1076.47 examples/s]33323 examples [00:31, 1076.56 examples/s]33433 examples [00:31, 1081.84 examples/s]33543 examples [00:31, 1085.58 examples/s]33652 examples [00:31, 1059.95 examples/s]33761 examples [00:32, 1068.43 examples/s]33868 examples [00:32, 1067.54 examples/s]33977 examples [00:32, 1073.08 examples/s]34087 examples [00:32, 1079.98 examples/s]34196 examples [00:32, 1081.28 examples/s]34305 examples [00:32, 1081.42 examples/s]34414 examples [00:32, 1076.70 examples/s]34522 examples [00:32, 1062.70 examples/s]34629 examples [00:32, 1038.73 examples/s]34734 examples [00:32, 1025.26 examples/s]34842 examples [00:33, 1038.88 examples/s]34949 examples [00:33, 1046.68 examples/s]35059 examples [00:33, 1061.08 examples/s]35168 examples [00:33, 1067.49 examples/s]35277 examples [00:33, 1073.64 examples/s]35385 examples [00:33, 1031.29 examples/s]35489 examples [00:33, 1032.28 examples/s]35597 examples [00:33, 1045.56 examples/s]35704 examples [00:33, 1052.47 examples/s]35812 examples [00:34, 1059.57 examples/s]35921 examples [00:34, 1065.79 examples/s]36028 examples [00:34, 1064.57 examples/s]36138 examples [00:34, 1072.91 examples/s]36248 examples [00:34, 1080.08 examples/s]36357 examples [00:34, 1082.94 examples/s]36466 examples [00:34, 1082.21 examples/s]36575 examples [00:34, 1080.81 examples/s]36684 examples [00:34, 1078.02 examples/s]36792 examples [00:34, 1046.23 examples/s]36897 examples [00:35, 1041.62 examples/s]37002 examples [00:35, 1040.86 examples/s]37107 examples [00:35, 1037.55 examples/s]37214 examples [00:35, 1044.14 examples/s]37323 examples [00:35, 1055.46 examples/s]37431 examples [00:35, 1060.15 examples/s]37539 examples [00:35, 1064.99 examples/s]37646 examples [00:35, 1059.29 examples/s]37755 examples [00:35, 1066.65 examples/s]37865 examples [00:35, 1075.37 examples/s]37974 examples [00:36, 1079.17 examples/s]38084 examples [00:36, 1083.63 examples/s]38193 examples [00:36, 1074.14 examples/s]38302 examples [00:36, 1077.53 examples/s]38412 examples [00:36, 1081.55 examples/s]38521 examples [00:36, 1065.74 examples/s]38628 examples [00:36, 1044.84 examples/s]38733 examples [00:36, 1046.25 examples/s]38843 examples [00:36, 1061.20 examples/s]38953 examples [00:36, 1070.05 examples/s]39063 examples [00:37, 1076.42 examples/s]39171 examples [00:37, 1075.63 examples/s]39279 examples [00:37, 1058.75 examples/s]39389 examples [00:37, 1068.51 examples/s]39498 examples [00:37, 1072.61 examples/s]39607 examples [00:37, 1075.52 examples/s]39716 examples [00:37, 1078.44 examples/s]39824 examples [00:37, 1066.42 examples/s]39931 examples [00:37, 1057.31 examples/s]40037 examples [00:37, 1009.51 examples/s]40146 examples [00:38, 1031.69 examples/s]40255 examples [00:38, 1046.35 examples/s]40361 examples [00:38, 1045.29 examples/s]40467 examples [00:38, 1048.59 examples/s]40574 examples [00:38, 1053.96 examples/s]40682 examples [00:38, 1060.32 examples/s]40789 examples [00:38, 1034.85 examples/s]40895 examples [00:38, 1041.70 examples/s]41002 examples [00:38, 1047.23 examples/s]41110 examples [00:39, 1054.68 examples/s]41220 examples [00:39, 1065.57 examples/s]41328 examples [00:39, 1068.79 examples/s]41435 examples [00:39, 1063.67 examples/s]41542 examples [00:39, 1058.64 examples/s]41650 examples [00:39, 1063.36 examples/s]41760 examples [00:39, 1073.23 examples/s]41868 examples [00:39, 1041.89 examples/s]41974 examples [00:39, 1047.10 examples/s]42080 examples [00:39, 1049.59 examples/s]42186 examples [00:40, 1052.52 examples/s]42292 examples [00:40, 1053.65 examples/s]42400 examples [00:40, 1058.98 examples/s]42506 examples [00:40, 1058.79 examples/s]42612 examples [00:40, 1058.13 examples/s]42721 examples [00:40, 1066.08 examples/s]42830 examples [00:40, 1071.64 examples/s]42939 examples [00:40, 1075.23 examples/s]43047 examples [00:40, 1062.88 examples/s]43157 examples [00:40, 1071.45 examples/s]43267 examples [00:41, 1078.15 examples/s]43376 examples [00:41, 1079.69 examples/s]43485 examples [00:41, 1079.89 examples/s]43594 examples [00:41, 1073.12 examples/s]43702 examples [00:41, 1074.24 examples/s]43810 examples [00:41, 1069.56 examples/s]43917 examples [00:41, 1065.89 examples/s]44024 examples [00:41, 1050.13 examples/s]44131 examples [00:41, 1055.97 examples/s]44240 examples [00:41, 1065.64 examples/s]44349 examples [00:42, 1071.84 examples/s]44460 examples [00:42, 1080.73 examples/s]44569 examples [00:42, 1082.89 examples/s]44678 examples [00:42, 1079.01 examples/s]44787 examples [00:42, 1079.79 examples/s]44898 examples [00:42, 1086.41 examples/s]45008 examples [00:42, 1090.20 examples/s]45118 examples [00:42, 1055.23 examples/s]45224 examples [00:42, 1036.13 examples/s]45334 examples [00:42, 1052.60 examples/s]45440 examples [00:43, 1038.62 examples/s]45550 examples [00:43, 1055.54 examples/s]45658 examples [00:43, 1062.18 examples/s]45765 examples [00:43, 1055.52 examples/s]45874 examples [00:43, 1065.32 examples/s]45981 examples [00:43, 1056.83 examples/s]46089 examples [00:43, 1061.74 examples/s]46196 examples [00:43, 1063.08 examples/s]46304 examples [00:43, 1066.73 examples/s]46413 examples [00:43, 1072.59 examples/s]46523 examples [00:44, 1078.84 examples/s]46631 examples [00:44, 1059.59 examples/s]46739 examples [00:44, 1064.97 examples/s]46846 examples [00:44, 1066.37 examples/s]46956 examples [00:44, 1074.34 examples/s]47066 examples [00:44, 1080.02 examples/s]47175 examples [00:44, 1082.22 examples/s]47284 examples [00:44, 1082.56 examples/s]47393 examples [00:44, 1076.57 examples/s]47501 examples [00:44, 1077.28 examples/s]47609 examples [00:45, 1034.20 examples/s]47718 examples [00:45, 1049.32 examples/s]47827 examples [00:45, 1058.03 examples/s]47936 examples [00:45, 1064.79 examples/s]48047 examples [00:45, 1077.39 examples/s]48155 examples [00:45, 1062.02 examples/s]48264 examples [00:45, 1068.99 examples/s]48372 examples [00:45, 1023.11 examples/s]48477 examples [00:45, 1028.23 examples/s]48581 examples [00:46, 1015.17 examples/s]48691 examples [00:46, 1037.30 examples/s]48802 examples [00:46, 1056.03 examples/s]48912 examples [00:46, 1068.76 examples/s]49020 examples [00:46, 1066.11 examples/s]49131 examples [00:46, 1076.99 examples/s]49241 examples [00:46, 1082.39 examples/s]49352 examples [00:46, 1089.04 examples/s]49461 examples [00:46, 1084.47 examples/s]49570 examples [00:46, 1078.29 examples/s]49681 examples [00:47, 1085.85 examples/s]49794 examples [00:47, 1096.25 examples/s]49904 examples [00:47, 1091.86 examples/s]                                            0%|          | 0/50000 [00:00<?, ? examples/s] 14%|█▍        | 6942/50000 [00:00<00:00, 69414.94 examples/s] 40%|████      | 20223/50000 [00:00<00:00, 81015.72 examples/s] 66%|██████▋   | 33140/50000 [00:00<00:00, 91217.15 examples/s] 94%|█████████▍| 46896/50000 [00:00<00:00, 101471.71 examples/s]                                                                0 examples [00:00, ? examples/s]89 examples [00:00, 882.75 examples/s]200 examples [00:00, 939.68 examples/s]312 examples [00:00, 987.19 examples/s]425 examples [00:00, 1025.14 examples/s]537 examples [00:00, 1049.31 examples/s]650 examples [00:00, 1069.62 examples/s]758 examples [00:00, 1069.57 examples/s]867 examples [00:00, 1074.44 examples/s]974 examples [00:00, 1073.01 examples/s]1082 examples [00:01, 1074.98 examples/s]1188 examples [00:01, 1041.53 examples/s]1294 examples [00:01, 1045.93 examples/s]1404 examples [00:01, 1060.33 examples/s]1515 examples [00:01, 1073.91 examples/s]1627 examples [00:01, 1086.32 examples/s]1738 examples [00:01, 1092.17 examples/s]1848 examples [00:01, 1087.16 examples/s]1959 examples [00:01, 1091.33 examples/s]2070 examples [00:01, 1095.33 examples/s]2180 examples [00:02, 1095.59 examples/s]2292 examples [00:02, 1100.03 examples/s]2402 examples [00:02, 1061.15 examples/s]2511 examples [00:02, 1068.58 examples/s]2619 examples [00:02, 1064.25 examples/s]2728 examples [00:02, 1069.01 examples/s]2838 examples [00:02, 1077.52 examples/s]2946 examples [00:02, 1076.02 examples/s]3056 examples [00:02, 1080.76 examples/s]3165 examples [00:02, 1044.16 examples/s]3273 examples [00:03, 1052.62 examples/s]3382 examples [00:03, 1061.26 examples/s]3489 examples [00:03, 1062.43 examples/s]3600 examples [00:03, 1074.49 examples/s]3708 examples [00:03, 1070.59 examples/s]3817 examples [00:03, 1073.74 examples/s]3925 examples [00:03, 977.28 examples/s] 4034 examples [00:03, 1008.02 examples/s]4143 examples [00:03, 1029.90 examples/s]4253 examples [00:03, 1048.86 examples/s]4362 examples [00:04, 1060.84 examples/s]4469 examples [00:04, 1041.37 examples/s]4576 examples [00:04, 1049.64 examples/s]4685 examples [00:04, 1061.31 examples/s]4795 examples [00:04, 1071.79 examples/s]4905 examples [00:04, 1078.15 examples/s]5016 examples [00:04, 1086.56 examples/s]5125 examples [00:04, 1082.66 examples/s]5234 examples [00:04, 1081.37 examples/s]5344 examples [00:05, 1084.86 examples/s]5453 examples [00:05, 1077.83 examples/s]5564 examples [00:05, 1084.41 examples/s]5673 examples [00:05, 1081.13 examples/s]5783 examples [00:05, 1084.85 examples/s]5892 examples [00:05, 1084.16 examples/s]6001 examples [00:05, 1085.40 examples/s]6110 examples [00:05, 1082.01 examples/s]6219 examples [00:05, 1075.39 examples/s]6327 examples [00:05, 1074.42 examples/s]6435 examples [00:06, 1074.90 examples/s]6543 examples [00:06, 1074.24 examples/s]6653 examples [00:06, 1080.71 examples/s]6762 examples [00:06, 1077.89 examples/s]6873 examples [00:06, 1085.76 examples/s]6982 examples [00:06, 1083.05 examples/s]7091 examples [00:06, 1083.79 examples/s]7202 examples [00:06, 1087.01 examples/s]7313 examples [00:06, 1091.76 examples/s]7425 examples [00:06, 1099.10 examples/s]7536 examples [00:07, 1100.53 examples/s]7648 examples [00:07, 1105.94 examples/s]7759 examples [00:07, 1057.30 examples/s]7870 examples [00:07, 1070.89 examples/s]7981 examples [00:07, 1081.81 examples/s]8091 examples [00:07, 1084.77 examples/s]8203 examples [00:07, 1092.56 examples/s]8314 examples [00:07, 1095.40 examples/s]8425 examples [00:07, 1098.47 examples/s]8537 examples [00:07, 1103.65 examples/s]8649 examples [00:08, 1106.77 examples/s]8760 examples [00:08, 1106.40 examples/s]8871 examples [00:08, 1093.14 examples/s]8981 examples [00:08, 1093.53 examples/s]9091 examples [00:08, 1095.03 examples/s]9203 examples [00:08, 1100.41 examples/s]9314 examples [00:08, 1082.33 examples/s]9423 examples [00:08, 1082.75 examples/s]9532 examples [00:08, 1083.01 examples/s]9644 examples [00:08, 1090.97 examples/s]9755 examples [00:09, 1095.49 examples/s]9865 examples [00:09, 1096.16 examples/s]9975 examples [00:09, 1092.95 examples/s]                                           0%|          | 0/10000 [00:00<?, ? examples/s]                                                [1mDownloading and preparing dataset cifar10/3.0.2 (download: 162.17 MiB, generated: 132.40 MiB, total: 294.58 MiB) to /home/runner/tensorflow_datasets/cifar10/3.0.2...[0m



Shuffling and writing examples to /home/runner/tensorflow_datasets/cifar10/3.0.2.incompleteWIIX9G/cifar10-train.tfrecord
Shuffling and writing examples to /home/runner/tensorflow_datasets/cifar10/3.0.2.incompleteWIIX9G/cifar10-test.tfrecord
[1mDataset cifar10 downloaded and prepared to /home/runner/tensorflow_datasets/cifar10/3.0.2. Subsequent calls will reuse this data.[0m

  ############## Saving train dataset ############################### 

  ############## Saving test dataset ############################### 

  Saved /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/cifar10/ ['test', 'train'] 

  URL:  mlmodels.preprocess.generic:get_dataset_torch {'dataloader': 'mlmodels.preprocess.generic:NumpyDataset', 'to_image': True, 'transform': {'uri': 'mlmodels.preprocess.image:torch_transform_generic', 'pass_data_pars': False, 'arg': {'fixed_size': 256}}, 'shuffle': True, 'download': True} 

  
###### load_callable_from_uri LOADED <function get_dataset_torch at 0x7f385767b8c8> 

  
 ######### postional parameters :  ['data_info'] 

  
 ######### Execute : preprocessor_func <function get_dataset_torch at 0x7f385767b8c8> 

  function with postional parmater data_info <function get_dataset_torch at 0x7f385767b8c8> , (data_info, **args) 

  #### If transformer URI is Provided {'uri': 'mlmodels.preprocess.image:torch_transform_generic', 'pass_data_pars': False, 'arg': {'fixed_size': 256}} 

  #### Loading dataloader URI 

  dataset :  <class 'mlmodels.preprocess.generic.NumpyDataset'> 
Dataset File path :  /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/cifar10/train/cifar10.npz
Dataset File path :  /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/cifar10/test/cifar10.npz

  
 #####  get_Data DataLoader  

  ((<mlmodels.preprocess.generic.Custom_DataLoader object at 0x7f37dcb1bbe0>, <mlmodels.preprocess.generic.Custom_DataLoader object at 0x7f37dcad6c50>), {}) 

  




 #################################################################################################### 

  /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor/resnet34_benchmark_mnist.json 
 

  #####  Load JSON data_pars 

  {
  "data_info":{
    "data_path":"dataset\/vision\/MNIST\/",
    "dataset":"MNIST",
    "data_type":"tch_dataset",
    "batch_size":10,
    "train":true
  },
  "preprocessors":[
    {
      "name":"tch_dataset_start",
      "uri":"mlmodels.preprocess.generic:get_dataset_torch",
      "args":{
        "dataloader":"torchvision.datasets:MNIST",
        "to_image":true,
        "transform":{
          "uri":"mlmodels.preprocess.image:torch_transform_mnist",
          "pass_data_pars":false,
          "arg":{

          }
        },
        "shuffle":true,
        "download":true
      }
    }
  ]
} 

  
 #####  Load DataLoader  

  
 #####  compute DataLoader  

  URL:  mlmodels.preprocess.generic:get_dataset_torch {'dataloader': 'torchvision.datasets:MNIST', 'to_image': True, 'transform': {'uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'pass_data_pars': False, 'arg': {}}, 'shuffle': True, 'download': True} 

  
###### load_callable_from_uri LOADED <function get_dataset_torch at 0x7f385767b8c8> 

  
 ######### postional parameters :  ['data_info'] 

  
 ######### Execute : preprocessor_func <function get_dataset_torch at 0x7f385767b8c8> 

  function with postional parmater data_info <function get_dataset_torch at 0x7f385767b8c8> , (data_info, **args) 

  #### If transformer URI is Provided {'uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'pass_data_pars': False, 'arg': {}} 

  #### Loading dataloader URI 

  dataset :  <class 'torchvision.datasets.mnist.MNIST'> 

  
 #####  get_Data DataLoader  

  ((<mlmodels.preprocess.generic.Custom_DataLoader object at 0x7f38567b9be0>, <mlmodels.preprocess.generic.Custom_DataLoader object at 0x7f3856641ef0>), {}) 

  




 #################################################################################################### 

  /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor/textcnn.json 
 

  #####  Load JSON data_pars 

  {
  "data_info":{
    "data_path":"dataset\/recommender\/",
    "dataset":"IMDB_sample.txt",
    "data_type":"csv_dataset",
    "batch_size":64,
    "train":true
  },
  "preprocessors":[
    {
      "uri":"mlmodels.model_tch.textcnn:split_train_valid",
      "args":{
        "frac":0.99
      }
    },
    {
      "uri":"mlmodels.model_tch.textcnn:create_tabular_dataset",
      "args":{
        "lang":"en",
        "pretrained_emb":"glove.6B.300d"
      }
    }
  ]
} 

  
 #####  Load DataLoader  

  
 #####  compute DataLoader  

  URL:  mlmodels.model_tch.textcnn:split_train_valid {'frac': 0.99} 

  
###### load_callable_from_uri LOADED <function split_train_valid at 0x7f37cf1af378> 

  
 ######### postional parameters :  ['data_info'] 

  
 ######### Execute : preprocessor_func <function split_train_valid at 0x7f37cf1af378> 

  function with postional parmater data_info <function split_train_valid at 0x7f37cf1af378> , (data_info, **args) 
Spliting original file to train/valid set...

  URL:  mlmodels.model_tch.textcnn:create_tabular_dataset {'lang': 'en', 'pretrained_emb': 'glove.6B.300d'} 

  
###### load_callable_from_uri LOADED <function create_tabular_dataset at 0x7f37cf1af488> 

  
 ######### postional parameters :  ['data_info'] 

  
 ######### Execute : preprocessor_func <function create_tabular_dataset at 0x7f37cf1af488> 

  function with postional parmater data_info <function create_tabular_dataset at 0x7f37cf1af488> , (data_info, **args) 

  Download en 
Collecting en_core_web_sm==2.3.0
  Downloading https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.0/en_core_web_sm-2.3.0.tar.gz (12.0 MB)
Requirement already satisfied: spacy<2.4.0,>=2.3.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from en_core_web_sm==2.3.0) (2.3.0)
Requirement already satisfied: plac<1.2.0,>=0.9.6 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy<2.4.0,>=2.3.0->en_core_web_sm==2.3.0) (1.1.3)
Requirement already satisfied: blis<0.5.0,>=0.4.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy<2.4.0,>=2.3.0->en_core_web_sm==2.3.0) (0.4.1)
Requirement already satisfied: preshed<3.1.0,>=3.0.2 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy<2.4.0,>=2.3.0->en_core_web_sm==2.3.0) (3.0.2)
Requirement already satisfied: setuptools in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy<2.4.0,>=2.3.0->en_core_web_sm==2.3.0) (45.2.0)
Requirement already satisfied: srsly<1.1.0,>=1.0.2 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy<2.4.0,>=2.3.0->en_core_web_sm==2.3.0) (1.0.2)
Requirement already satisfied: tqdm<5.0.0,>=4.38.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy<2.4.0,>=2.3.0->en_core_web_sm==2.3.0) (4.46.1)
Requirement already satisfied: requests<3.0.0,>=2.13.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy<2.4.0,>=2.3.0->en_core_web_sm==2.3.0) (2.24.0)
Requirement already satisfied: wasabi<1.1.0,>=0.4.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy<2.4.0,>=2.3.0->en_core_web_sm==2.3.0) (0.6.0)
Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy<2.4.0,>=2.3.0->en_core_web_sm==2.3.0) (1.0.2)
Requirement already satisfied: thinc==7.4.1 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy<2.4.0,>=2.3.0->en_core_web_sm==2.3.0) (7.4.1)
Requirement already satisfied: numpy>=1.15.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy<2.4.0,>=2.3.0->en_core_web_sm==2.3.0) (1.18.5)
Requirement already satisfied: cymem<2.1.0,>=2.0.2 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy<2.4.0,>=2.3.0->en_core_web_sm==2.3.0) (2.0.3)
Requirement already satisfied: catalogue<1.1.0,>=0.0.7 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy<2.4.0,>=2.3.0->en_core_web_sm==2.3.0) (1.0.0)
Requirement already satisfied: certifi>=2017.4.17 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from requests<3.0.0,>=2.13.0->spacy<2.4.0,>=2.3.0->en_core_web_sm==2.3.0) (2020.4.5.2)
Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from requests<3.0.0,>=2.13.0->spacy<2.4.0,>=2.3.0->en_core_web_sm==2.3.0) (1.25.9)
Requirement already satisfied: chardet<4,>=3.0.2 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from requests<3.0.0,>=2.13.0->spacy<2.4.0,>=2.3.0->en_core_web_sm==2.3.0) (3.0.4)
Requirement already satisfied: idna<3,>=2.5 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from requests<3.0.0,>=2.13.0->spacy<2.4.0,>=2.3.0->en_core_web_sm==2.3.0) (2.9)
Requirement already satisfied: importlib-metadata>=0.20; python_version < "3.8" in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from catalogue<1.1.0,>=0.0.7->spacy<2.4.0,>=2.3.0->en_core_web_sm==2.3.0) (1.6.1)
Requirement already satisfied: zipp>=0.5 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from importlib-metadata>=0.20; python_version < "3.8"->catalogue<1.1.0,>=0.0.7->spacy<2.4.0,>=2.3.0->en_core_web_sm==2.3.0) (3.1.0)
Building wheels for collected packages: en-core-web-sm
  Building wheel for en-core-web-sm (setup.py): started
  Building wheel for en-core-web-sm (setup.py): finished with status 'done'
  Created wheel for en-core-web-sm: filename=en_core_web_sm-2.3.0-py3-none-any.whl size=12048606 sha256=431061b2607edee161bf166c6a57b1e4673a51df0974423d6f563451deeae345
  Stored in directory: /tmp/pip-ephem-wheel-cache-vbs0vqjv/wheels/4a/db/07/94eee4f3a60150464a04160bd0dfe9c8752ab981fe92f16aea
Successfully built en-core-web-sm
Installing collected packages: en-core-web-sm
Successfully installed en-core-web-sm-2.3.0
[38;5;2m✔ Download and installation successful[0m
You can now load the model via spacy.load('en_core_web_sm')
[38;5;2m✔ Linking successful[0m
/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/en_core_web_sm
-->
/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/spacy/data/en
You can now load the model via spacy.load('en')
.vector_cache/glove.6B.zip: 0.00B [00:00, ?B/s].vector_cache/glove.6B.zip:   0%|          | 8.19k/862M [00:00<20:44:13, 11.5kB/s].vector_cache/glove.6B.zip:   0%|          | 49.2k/862M [00:00<14:45:12, 16.2kB/s].vector_cache/glove.6B.zip:   0%|          | 221k/862M [00:00<10:22:55, 23.1kB/s] .vector_cache/glove.6B.zip:   0%|          | 901k/862M [00:01<7:16:33, 32.9kB/s] .vector_cache/glove.6B.zip:   0%|          | 3.65M/862M [00:01<5:04:49, 46.9kB/s].vector_cache/glove.6B.zip:   1%|          | 8.09M/862M [00:01<3:32:22, 67.0kB/s].vector_cache/glove.6B.zip:   1%|▏         | 12.3M/862M [00:01<2:28:02, 95.7kB/s].vector_cache/glove.6B.zip:   2%|▏         | 16.8M/862M [00:01<1:43:10, 137kB/s] .vector_cache/glove.6B.zip:   2%|▏         | 20.8M/862M [00:01<1:11:59, 195kB/s].vector_cache/glove.6B.zip:   3%|▎         | 25.5M/862M [00:01<50:12, 278kB/s]  .vector_cache/glove.6B.zip:   3%|▎         | 29.3M/862M [00:01<35:09, 395kB/s].vector_cache/glove.6B.zip:   4%|▍         | 33.9M/862M [00:02<24:33, 562kB/s].vector_cache/glove.6B.zip:   4%|▍         | 38.4M/862M [00:02<17:11, 799kB/s].vector_cache/glove.6B.zip:   5%|▍         | 42.1M/862M [00:02<12:05, 1.13MB/s].vector_cache/glove.6B.zip:   5%|▌         | 46.6M/862M [00:02<08:30, 1.60MB/s].vector_cache/glove.6B.zip:   6%|▌         | 50.4M/862M [00:02<06:02, 2.24MB/s].vector_cache/glove.6B.zip:   6%|▌         | 51.8M/862M [00:02<05:00, 2.70MB/s].vector_cache/glove.6B.zip:   6%|▋         | 55.9M/862M [00:04<05:24, 2.49MB/s].vector_cache/glove.6B.zip:   7%|▋         | 56.1M/862M [00:04<06:49, 1.97MB/s].vector_cache/glove.6B.zip:   7%|▋         | 56.8M/862M [00:04<05:31, 2.43MB/s].vector_cache/glove.6B.zip:   7%|▋         | 59.7M/862M [00:05<04:02, 3.31MB/s].vector_cache/glove.6B.zip:   7%|▋         | 60.1M/862M [00:06<18:58, 705kB/s] .vector_cache/glove.6B.zip:   7%|▋         | 60.5M/862M [00:06<14:46, 904kB/s].vector_cache/glove.6B.zip:   7%|▋         | 61.9M/862M [00:06<10:40, 1.25MB/s].vector_cache/glove.6B.zip:   7%|▋         | 64.3M/862M [00:08<10:20, 1.28MB/s].vector_cache/glove.6B.zip:   7%|▋         | 64.5M/862M [00:08<10:15, 1.30MB/s].vector_cache/glove.6B.zip:   8%|▊         | 65.2M/862M [00:08<07:49, 1.70MB/s].vector_cache/glove.6B.zip:   8%|▊         | 66.5M/862M [00:09<05:46, 2.30MB/s].vector_cache/glove.6B.zip:   8%|▊         | 68.0M/862M [00:09<04:18, 3.07MB/s].vector_cache/glove.6B.zip:   8%|▊         | 68.5M/862M [00:10<17:01, 777kB/s] .vector_cache/glove.6B.zip:   8%|▊         | 68.5M/862M [00:10<17:55, 738kB/s].vector_cache/glove.6B.zip:   8%|▊         | 68.9M/862M [00:10<13:51, 954kB/s].vector_cache/glove.6B.zip:   8%|▊         | 70.0M/862M [00:11<10:03, 1.31MB/s].vector_cache/glove.6B.zip:   8%|▊         | 71.3M/862M [00:11<07:20, 1.80MB/s].vector_cache/glove.6B.zip:   8%|▊         | 72.6M/862M [00:12<09:40, 1.36MB/s].vector_cache/glove.6B.zip:   8%|▊         | 72.7M/862M [00:12<12:43, 1.03MB/s].vector_cache/glove.6B.zip:   8%|▊         | 73.0M/862M [00:12<10:09, 1.30MB/s].vector_cache/glove.6B.zip:   9%|▊         | 73.9M/862M [00:12<07:34, 1.73MB/s].vector_cache/glove.6B.zip:   9%|▊         | 75.4M/862M [00:13<05:33, 2.36MB/s].vector_cache/glove.6B.zip:   9%|▉         | 76.4M/862M [00:13<05:27, 2.40MB/s].vector_cache/glove.6B.zip:   9%|▉         | 76.4M/862M [00:14<7:46:02, 28.1kB/s].vector_cache/glove.6B.zip:   9%|▉         | 76.8M/862M [00:14<5:27:29, 40.0kB/s].vector_cache/glove.6B.zip:   9%|▉         | 78.2M/862M [00:14<3:49:10, 57.0kB/s].vector_cache/glove.6B.zip:   9%|▉         | 80.3M/862M [00:14<2:40:15, 81.3kB/s].vector_cache/glove.6B.zip:   9%|▉         | 80.5M/862M [00:16<2:14:58, 96.5kB/s].vector_cache/glove.6B.zip:   9%|▉         | 80.6M/862M [00:16<1:40:23, 130kB/s] .vector_cache/glove.6B.zip:   9%|▉         | 81.0M/862M [00:16<1:11:38, 182kB/s].vector_cache/glove.6B.zip:  10%|▉         | 82.5M/862M [00:16<50:24, 258kB/s]  .vector_cache/glove.6B.zip:  10%|▉         | 84.3M/862M [00:16<35:30, 365kB/s].vector_cache/glove.6B.zip:  10%|▉         | 84.7M/862M [00:18<38:25, 337kB/s].vector_cache/glove.6B.zip:  10%|▉         | 84.7M/862M [00:18<34:56, 371kB/s].vector_cache/glove.6B.zip:  10%|▉         | 85.0M/862M [00:18<26:20, 492kB/s].vector_cache/glove.6B.zip:  10%|▉         | 86.1M/862M [00:18<18:53, 685kB/s].vector_cache/glove.6B.zip:  10%|█         | 87.6M/862M [00:18<13:32, 953kB/s].vector_cache/glove.6B.zip:  10%|█         | 88.8M/862M [00:20<14:07, 913kB/s].vector_cache/glove.6B.zip:  10%|█         | 89.0M/862M [00:20<13:26, 958kB/s].vector_cache/glove.6B.zip:  10%|█         | 89.5M/862M [00:20<10:20, 1.25MB/s].vector_cache/glove.6B.zip:  11%|█         | 91.0M/862M [00:20<07:34, 1.70MB/s].vector_cache/glove.6B.zip:  11%|█         | 92.6M/862M [00:20<05:37, 2.28MB/s].vector_cache/glove.6B.zip:  11%|█         | 93.0M/862M [00:22<18:54, 678kB/s] .vector_cache/glove.6B.zip:  11%|█         | 93.0M/862M [00:22<20:17, 632kB/s].vector_cache/glove.6B.zip:  11%|█         | 93.3M/862M [00:22<15:44, 814kB/s].vector_cache/glove.6B.zip:  11%|█         | 94.4M/862M [00:22<11:27, 1.12MB/s].vector_cache/glove.6B.zip:  11%|█         | 95.9M/862M [00:22<08:15, 1.55MB/s].vector_cache/glove.6B.zip:  11%|█         | 96.8M/862M [00:22<06:12, 2.06MB/s].vector_cache/glove.6B.zip:  11%|█▏        | 97.1M/862M [00:24<25:13, 505kB/s] .vector_cache/glove.6B.zip:  11%|█▏        | 97.3M/862M [00:24<21:00, 607kB/s].vector_cache/glove.6B.zip:  11%|█▏        | 97.9M/862M [00:24<15:24, 827kB/s].vector_cache/glove.6B.zip:  11%|█▏        | 99.1M/862M [00:24<11:04, 1.15MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 100M/862M [00:24<08:05, 1.57MB/s] .vector_cache/glove.6B.zip:  12%|█▏        | 101M/862M [00:26<11:09, 1.14MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 101M/862M [00:26<14:50, 855kB/s] .vector_cache/glove.6B.zip:  12%|█▏        | 102M/862M [00:26<12:01, 1.05MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 103M/862M [00:26<08:47, 1.44MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 104M/862M [00:26<06:24, 1.97MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 105M/862M [00:26<04:51, 2.60MB/s].vector_cache/glove.6B.zip:  12%|█▏        | 105M/862M [00:28<49:00, 257kB/s] .vector_cache/glove.6B.zip:  12%|█▏        | 106M/862M [00:28<37:35, 335kB/s].vector_cache/glove.6B.zip:  12%|█▏        | 106M/862M [00:28<27:06, 465kB/s].vector_cache/glove.6B.zip:  12%|█▏        | 108M/862M [00:28<19:16, 652kB/s].vector_cache/glove.6B.zip:  13%|█▎        | 109M/862M [00:28<13:45, 912kB/s].vector_cache/glove.6B.zip:  13%|█▎        | 110M/862M [00:30<42:41, 294kB/s].vector_cache/glove.6B.zip:  13%|█▎        | 110M/862M [00:30<36:04, 348kB/s].vector_cache/glove.6B.zip:  13%|█▎        | 110M/862M [00:30<26:54, 466kB/s].vector_cache/glove.6B.zip:  13%|█▎        | 111M/862M [00:30<19:15, 650kB/s].vector_cache/glove.6B.zip:  13%|█▎        | 113M/862M [00:30<13:45, 908kB/s].vector_cache/glove.6B.zip:  13%|█▎        | 114M/862M [00:32<15:24, 810kB/s].vector_cache/glove.6B.zip:  13%|█▎        | 114M/862M [00:32<17:40, 706kB/s].vector_cache/glove.6B.zip:  13%|█▎        | 114M/862M [00:32<13:55, 896kB/s].vector_cache/glove.6B.zip:  13%|█▎        | 115M/862M [00:32<10:05, 1.23MB/s].vector_cache/glove.6B.zip:  13%|█▎        | 116M/862M [00:32<07:43, 1.61MB/s].vector_cache/glove.6B.zip:  14%|█▎        | 118M/862M [00:34<08:34, 1.45MB/s].vector_cache/glove.6B.zip:  14%|█▎        | 118M/862M [00:34<10:22, 1.19MB/s].vector_cache/glove.6B.zip:  14%|█▎        | 118M/862M [00:34<08:23, 1.48MB/s].vector_cache/glove.6B.zip:  14%|█▍        | 120M/862M [00:34<06:17, 1.97MB/s].vector_cache/glove.6B.zip:  14%|█▍        | 121M/862M [00:34<04:45, 2.59MB/s].vector_cache/glove.6B.zip:  14%|█▍        | 122M/862M [00:36<08:09, 1.51MB/s].vector_cache/glove.6B.zip:  14%|█▍        | 122M/862M [00:36<14:27, 853kB/s] .vector_cache/glove.6B.zip:  14%|█▍        | 122M/862M [00:36<14:31, 850kB/s].vector_cache/glove.6B.zip:  14%|█▍        | 123M/862M [00:36<11:24, 1.08MB/s].vector_cache/glove.6B.zip:  14%|█▍        | 123M/862M [00:36<09:43, 1.27MB/s].vector_cache/glove.6B.zip:  14%|█▍        | 123M/862M [00:36<08:33, 1.44MB/s].vector_cache/glove.6B.zip:  14%|█▍        | 123M/862M [00:36<07:38, 1.61MB/s].vector_cache/glove.6B.zip:  14%|█▍        | 124M/862M [00:37<06:59, 1.76MB/s].vector_cache/glove.6B.zip:  14%|█▍        | 124M/862M [00:37<06:31, 1.88MB/s].vector_cache/glove.6B.zip:  14%|█▍        | 124M/862M [00:37<06:10, 1.99MB/s].vector_cache/glove.6B.zip:  14%|█▍        | 125M/862M [00:37<05:48, 2.12MB/s].vector_cache/glove.6B.zip:  14%|█▍        | 125M/862M [00:37<05:37, 2.18MB/s].vector_cache/glove.6B.zip:  15%|█▍        | 125M/862M [00:37<05:30, 2.23MB/s].vector_cache/glove.6B.zip:  15%|█▍        | 125M/862M [00:37<05:49, 2.11MB/s].vector_cache/glove.6B.zip:  15%|█▍        | 126M/862M [00:37<05:22, 2.28MB/s].vector_cache/glove.6B.zip:  15%|█▍        | 126M/862M [00:38<05:38, 2.18MB/s].vector_cache/glove.6B.zip:  15%|█▍        | 126M/862M [00:38<05:25, 2.26MB/s].vector_cache/glove.6B.zip:  15%|█▍        | 127M/862M [00:38<05:18, 2.31MB/s].vector_cache/glove.6B.zip:  15%|█▍        | 127M/862M [00:38<05:14, 2.34MB/s].vector_cache/glove.6B.zip:  15%|█▍        | 127M/862M [00:38<05:00, 2.44MB/s].vector_cache/glove.6B.zip:  15%|█▍        | 127M/862M [00:38<05:19, 2.30MB/s].vector_cache/glove.6B.zip:  15%|█▍        | 128M/862M [00:38<04:59, 2.45MB/s].vector_cache/glove.6B.zip:  15%|█▍        | 128M/862M [00:38<05:13, 2.34MB/s].vector_cache/glove.6B.zip:  15%|█▍        | 128M/862M [00:39<05:13, 2.34MB/s].vector_cache/glove.6B.zip:  15%|█▍        | 128M/862M [00:39<05:44, 2.13MB/s].vector_cache/glove.6B.zip:  15%|█▍        | 129M/862M [00:39<06:02, 2.03MB/s].vector_cache/glove.6B.zip:  15%|█▍        | 129M/862M [00:39<06:11, 1.97MB/s].vector_cache/glove.6B.zip:  15%|█▍        | 129M/862M [00:39<06:13, 1.96MB/s].vector_cache/glove.6B.zip:  15%|█▌        | 130M/862M [00:39<06:11, 1.97MB/s].vector_cache/glove.6B.zip:  15%|█▌        | 130M/862M [00:39<06:10, 1.97MB/s].vector_cache/glove.6B.zip:  15%|█▌        | 130M/862M [00:40<06:53, 1.77MB/s].vector_cache/glove.6B.zip:  15%|█▌        | 130M/862M [00:40<06:32, 1.86MB/s].vector_cache/glove.6B.zip:  15%|█▌        | 131M/862M [00:40<06:16, 1.95MB/s].vector_cache/glove.6B.zip:  15%|█▌        | 131M/862M [00:40<05:54, 2.06MB/s].vector_cache/glove.6B.zip:  15%|█▌        | 131M/862M [00:40<05:53, 2.07MB/s].vector_cache/glove.6B.zip:  15%|█▌        | 132M/862M [00:40<05:33, 2.19MB/s].vector_cache/glove.6B.zip:  15%|█▌        | 132M/862M [00:40<05:28, 2.22MB/s].vector_cache/glove.6B.zip:  15%|█▌        | 132M/862M [00:40<05:23, 2.26MB/s].vector_cache/glove.6B.zip:  15%|█▌        | 132M/862M [00:41<05:18, 2.29MB/s].vector_cache/glove.6B.zip:  15%|█▌        | 133M/862M [00:41<05:14, 2.32MB/s].vector_cache/glove.6B.zip:  15%|█▌        | 133M/862M [00:41<05:12, 2.33MB/s].vector_cache/glove.6B.zip:  15%|█▌        | 133M/862M [00:41<05:08, 2.36MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 134M/862M [00:41<04:52, 2.49MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 134M/862M [00:41<05:13, 2.33MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 134M/862M [00:41<08:35, 1.41MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 134M/862M [00:42<07:30, 1.61MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 135M/862M [00:42<06:43, 1.80MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 135M/862M [00:42<06:10, 1.96MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 135M/862M [00:42<05:46, 2.09MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 136M/862M [00:42<05:30, 2.20MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 136M/862M [00:42<05:18, 2.28MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 136M/862M [00:42<05:09, 2.34MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 137M/862M [00:43<05:04, 2.39MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 137M/862M [00:43<05:00, 2.41MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 138M/862M [00:43<04:57, 2.43MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 138M/862M [00:43<04:56, 2.44MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 138M/862M [00:43<04:55, 2.45MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 138M/862M [00:43<16:00, 754kB/s] .vector_cache/glove.6B.zip:  16%|█▌        | 139M/862M [00:44<13:20, 904kB/s].vector_cache/glove.6B.zip:  16%|█▌        | 139M/862M [00:44<10:49, 1.11MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 139M/862M [00:44<09:02, 1.33MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 140M/862M [00:44<07:29, 1.61MB/s].vector_cache/glove.6B.zip:  16%|█▌        | 140M/862M [00:44<06:42, 1.80MB/s].vector_cache/glove.6B.zip:  16%|█▋        | 140M/862M [00:44<05:49, 2.07MB/s].vector_cache/glove.6B.zip:  16%|█▋        | 140M/862M [00:44<05:57, 2.02MB/s].vector_cache/glove.6B.zip:  16%|█▋        | 141M/862M [00:44<05:41, 2.11MB/s].vector_cache/glove.6B.zip:  16%|█▋        | 141M/862M [00:45<05:16, 2.28MB/s].vector_cache/glove.6B.zip:  16%|█▋        | 141M/862M [00:45<05:13, 2.30MB/s].vector_cache/glove.6B.zip:  16%|█▋        | 141M/862M [00:45<04:55, 2.44MB/s].vector_cache/glove.6B.zip:  16%|█▋        | 142M/862M [00:45<04:56, 2.43MB/s].vector_cache/glove.6B.zip:  16%|█▋        | 142M/862M [00:45<04:45, 2.52MB/s].vector_cache/glove.6B.zip:  16%|█▋        | 142M/862M [00:45<04:49, 2.49MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 142M/862M [00:45<10:11, 1.18MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 143M/862M [00:46<09:15, 1.29MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 143M/862M [00:46<07:49, 1.53MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 143M/862M [00:46<06:35, 1.82MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 144M/862M [00:46<05:40, 2.11MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 144M/862M [00:46<05:57, 2.01MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 144M/862M [00:46<05:28, 2.19MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 145M/862M [00:46<04:53, 2.45MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 145M/862M [00:46<04:34, 2.61MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 145M/862M [00:47<04:57, 2.41MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 146M/862M [00:47<04:30, 2.64MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 146M/862M [00:47<04:20, 2.75MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 146M/862M [00:47<04:21, 2.74MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 147M/862M [00:47<09:33, 1.25MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 147M/862M [00:48<08:35, 1.39MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 147M/862M [00:48<07:23, 1.61MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 148M/862M [00:48<06:24, 1.86MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 148M/862M [00:48<05:41, 2.09MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 148M/862M [00:48<05:05, 2.34MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 149M/862M [00:48<04:44, 2.51MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 149M/862M [00:48<04:29, 2.65MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 150M/862M [00:48<04:17, 2.76MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 150M/862M [00:49<04:10, 2.84MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 150M/862M [00:49<04:02, 2.93MB/s].vector_cache/glove.6B.zip:  17%|█▋        | 151M/862M [00:49<11:49, 1.00MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 151M/862M [00:49<10:00, 1.19MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 151M/862M [00:50<08:13, 1.44MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 152M/862M [00:50<06:39, 1.78MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 152M/862M [00:50<05:31, 2.14MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 152M/862M [00:50<05:05, 2.32MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 153M/862M [00:50<04:22, 2.71MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 153M/862M [00:50<04:18, 2.74MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 154M/862M [00:50<03:45, 3.14MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 154M/862M [00:50<03:55, 3.01MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 154M/862M [00:50<03:26, 3.42MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 155M/862M [00:51<13:04, 901kB/s] .vector_cache/glove.6B.zip:  18%|█▊        | 155M/862M [00:51<11:29, 1.03MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 155M/862M [00:52<08:53, 1.33MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 156M/862M [00:52<06:52, 1.71MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 156M/862M [00:52<05:55, 1.99MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 157M/862M [00:52<04:47, 2.45MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 157M/862M [00:52<04:20, 2.71MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 158M/862M [00:52<03:39, 3.21MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 158M/862M [00:52<08:31, 1.38MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 159M/862M [00:52<06:29, 1.81MB/s].vector_cache/glove.6B.zip:  18%|█▊        | 159M/862M [00:53<16:30, 710kB/s] .vector_cache/glove.6B.zip:  18%|█▊        | 159M/862M [00:53<17:23, 674kB/s].vector_cache/glove.6B.zip:  18%|█▊        | 159M/862M [00:54<13:20, 878kB/s].vector_cache/glove.6B.zip:  19%|█▊        | 160M/862M [00:54<10:18, 1.14MB/s].vector_cache/glove.6B.zip:  19%|█▊        | 160M/862M [00:54<08:17, 1.41MB/s].vector_cache/glove.6B.zip:  19%|█▊        | 161M/862M [00:54<06:33, 1.78MB/s].vector_cache/glove.6B.zip:  19%|█▊        | 161M/862M [00:54<05:37, 2.07MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 162M/862M [00:54<04:40, 2.50MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 162M/862M [00:54<03:55, 2.98MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 163M/862M [00:54<03:59, 2.92MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 163M/862M [00:55<13:15, 879kB/s] .vector_cache/glove.6B.zip:  19%|█▉        | 163M/862M [00:55<11:35, 1.01MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 164M/862M [00:56<09:03, 1.28MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 164M/862M [00:56<07:10, 1.62MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 165M/862M [00:56<05:42, 2.03MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 165M/862M [00:56<04:37, 2.51MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 166M/862M [00:56<04:19, 2.68MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 166M/862M [00:56<03:43, 3.11MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 167M/862M [00:56<04:00, 2.89MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 167M/862M [00:56<03:44, 3.10MB/s].vector_cache/glove.6B.zip:  19%|█▉        | 167M/862M [00:57<15:50, 732kB/s] .vector_cache/glove.6B.zip:  19%|█▉        | 167M/862M [00:57<16:48, 689kB/s].vector_cache/glove.6B.zip:  19%|█▉        | 168M/862M [00:57<13:13, 875kB/s].vector_cache/glove.6B.zip:  19%|█▉        | 168M/862M [00:58<10:18, 1.12MB/s].vector_cache/glove.6B.zip:  20%|█▉        | 168M/862M [00:58<08:10, 1.41MB/s].vector_cache/glove.6B.zip:  20%|█▉        | 169M/862M [00:58<06:47, 1.70MB/s].vector_cache/glove.6B.zip:  20%|█▉        | 169M/862M [00:58<05:41, 2.03MB/s].vector_cache/glove.6B.zip:  20%|█▉        | 170M/862M [00:58<04:58, 2.32MB/s].vector_cache/glove.6B.zip:  20%|█▉        | 170M/862M [00:58<04:28, 2.58MB/s].vector_cache/glove.6B.zip:  20%|█▉        | 171M/862M [00:58<04:06, 2.81MB/s].vector_cache/glove.6B.zip:  20%|█▉        | 171M/862M [00:59<08:38, 1.33MB/s].vector_cache/glove.6B.zip:  20%|█▉        | 171M/862M [00:59<08:31, 1.35MB/s].vector_cache/glove.6B.zip:  20%|█▉        | 172M/862M [00:59<07:00, 1.64MB/s].vector_cache/glove.6B.zip:  20%|█▉        | 172M/862M [01:00<05:44, 2.00MB/s].vector_cache/glove.6B.zip:  20%|██        | 173M/862M [01:00<05:04, 2.27MB/s].vector_cache/glove.6B.zip:  20%|██        | 173M/862M [01:00<04:28, 2.56MB/s].vector_cache/glove.6B.zip:  20%|██        | 174M/862M [01:00<03:56, 2.91MB/s].vector_cache/glove.6B.zip:  20%|██        | 174M/862M [01:00<03:40, 3.11MB/s].vector_cache/glove.6B.zip:  20%|██        | 175M/862M [01:00<03:30, 3.27MB/s].vector_cache/glove.6B.zip:  20%|██        | 175M/862M [01:01<08:38, 1.32MB/s].vector_cache/glove.6B.zip:  20%|██        | 176M/862M [01:01<08:31, 1.34MB/s].vector_cache/glove.6B.zip:  20%|██        | 176M/862M [01:01<06:58, 1.64MB/s].vector_cache/glove.6B.zip:  20%|██        | 177M/862M [01:02<05:40, 2.01MB/s].vector_cache/glove.6B.zip:  21%|██        | 177M/862M [01:02<04:52, 2.34MB/s].vector_cache/glove.6B.zip:  21%|██        | 178M/862M [01:02<04:19, 2.64MB/s].vector_cache/glove.6B.zip:  21%|██        | 178M/862M [01:02<03:55, 2.90MB/s].vector_cache/glove.6B.zip:  21%|██        | 179M/862M [01:02<03:39, 3.12MB/s].vector_cache/glove.6B.zip:  21%|██        | 179M/862M [01:02<03:28, 3.28MB/s].vector_cache/glove.6B.zip:  21%|██        | 180M/862M [01:03<09:31, 1.19MB/s].vector_cache/glove.6B.zip:  21%|██        | 180M/862M [01:03<09:06, 1.25MB/s].vector_cache/glove.6B.zip:  21%|██        | 180M/862M [01:03<07:22, 1.54MB/s].vector_cache/glove.6B.zip:  21%|██        | 181M/862M [01:04<05:55, 1.92MB/s].vector_cache/glove.6B.zip:  21%|██        | 181M/862M [01:04<05:03, 2.25MB/s].vector_cache/glove.6B.zip:  21%|██        | 182M/862M [01:04<04:18, 2.64MB/s].vector_cache/glove.6B.zip:  21%|██        | 182M/862M [01:04<04:07, 2.75MB/s].vector_cache/glove.6B.zip:  21%|██        | 182M/862M [01:04<03:38, 3.11MB/s].vector_cache/glove.6B.zip:  21%|██        | 183M/862M [01:04<03:38, 3.12MB/s].vector_cache/glove.6B.zip:  21%|██        | 183M/862M [01:04<03:22, 3.35MB/s].vector_cache/glove.6B.zip:  21%|██▏       | 183M/862M [01:05<09:41, 1.17MB/s].vector_cache/glove.6B.zip:  21%|██▏       | 183M/862M [01:05<3:06:28, 60.7kB/s].vector_cache/glove.6B.zip:  21%|██▏       | 184M/862M [01:05<2:11:10, 86.2kB/s].vector_cache/glove.6B.zip:  21%|██▏       | 184M/862M [01:05<1:32:38, 122kB/s] .vector_cache/glove.6B.zip:  21%|██▏       | 185M/862M [01:05<1:05:40, 172kB/s].vector_cache/glove.6B.zip:  22%|██▏       | 186M/862M [01:06<46:48, 241kB/s]  .vector_cache/glove.6B.zip:  22%|██▏       | 186M/862M [01:06<33:44, 334kB/s].vector_cache/glove.6B.zip:  22%|██▏       | 186M/862M [01:06<24:48, 454kB/s].vector_cache/glove.6B.zip:  22%|██▏       | 187M/862M [01:06<18:44, 601kB/s].vector_cache/glove.6B.zip:  22%|██▏       | 187M/862M [01:06<14:45, 762kB/s].vector_cache/glove.6B.zip:  22%|██▏       | 187M/862M [01:06<11:57, 940kB/s].vector_cache/glove.6B.zip:  22%|██▏       | 187M/862M [01:07<17:57, 626kB/s].vector_cache/glove.6B.zip:  22%|██▏       | 188M/862M [01:07<16:50, 668kB/s].vector_cache/glove.6B.zip:  22%|██▏       | 188M/862M [01:07<13:25, 837kB/s].vector_cache/glove.6B.zip:  22%|██▏       | 188M/862M [01:07<10:38, 1.06MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 188M/862M [01:07<08:44, 1.28MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 189M/862M [01:07<08:00, 1.40MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 189M/862M [01:08<07:16, 1.54MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 189M/862M [01:08<06:19, 1.77MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 190M/862M [01:08<05:53, 1.90MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 190M/862M [01:08<05:33, 2.02MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 190M/862M [01:08<05:18, 2.11MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 190M/862M [01:08<05:08, 2.18MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 191M/862M [01:08<04:59, 2.24MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 191M/862M [01:09<04:35, 2.43MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 191M/862M [01:09<05:03, 2.21MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 192M/862M [01:09<04:51, 2.30MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 192M/862M [01:09<28:52, 387kB/s] .vector_cache/glove.6B.zip:  22%|██▏       | 192M/862M [01:09<21:35, 517kB/s].vector_cache/glove.6B.zip:  22%|██▏       | 192M/862M [01:09<16:21, 683kB/s].vector_cache/glove.6B.zip:  22%|██▏       | 193M/862M [01:09<12:48, 871kB/s].vector_cache/glove.6B.zip:  22%|██▏       | 193M/862M [01:09<10:25, 1.07MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 193M/862M [01:10<08:33, 1.30MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 194M/862M [01:10<07:21, 1.51MB/s].vector_cache/glove.6B.zip:  22%|██▏       | 194M/862M [01:10<06:29, 1.72MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 194M/862M [01:10<05:53, 1.89MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 195M/862M [01:10<05:27, 2.04MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 195M/862M [01:10<05:08, 2.16MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 195M/862M [01:10<04:54, 2.26MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 196M/862M [01:10<04:43, 2.35MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 196M/862M [01:11<15:20, 724kB/s] .vector_cache/glove.6B.zip:  23%|██▎       | 196M/862M [01:11<12:26, 893kB/s].vector_cache/glove.6B.zip:  23%|██▎       | 196M/862M [01:11<10:00, 1.11MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 197M/862M [01:11<08:27, 1.31MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 197M/862M [01:11<06:58, 1.59MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 197M/862M [01:11<05:53, 1.88MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 198M/862M [01:12<05:40, 1.95MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 198M/862M [01:12<04:56, 2.24MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 198M/862M [01:12<05:09, 2.14MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 198M/862M [01:12<04:39, 2.38MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 199M/862M [01:12<04:57, 2.23MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 199M/862M [01:12<04:28, 2.47MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 199M/862M [01:12<04:13, 2.62MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 200M/862M [01:12<04:12, 2.62MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 200M/862M [01:13<09:54, 1.11MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 200M/862M [01:13<08:49, 1.25MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 200M/862M [01:13<07:12, 1.53MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 201M/862M [01:13<06:05, 1.81MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 201M/862M [01:13<05:16, 2.09MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 202M/862M [01:13<04:44, 2.32MB/s].vector_cache/glove.6B.zip:  23%|██▎       | 202M/862M [01:14<04:21, 2.53MB/s].vector_cache/glove.6B.zip:  24%|██▎       | 203M/862M [01:14<04:04, 2.70MB/s].vector_cache/glove.6B.zip:  24%|██▎       | 203M/862M [01:14<03:53, 2.83MB/s].vector_cache/glove.6B.zip:  24%|██▎       | 203M/862M [01:14<03:44, 2.93MB/s].vector_cache/glove.6B.zip:  24%|██▎       | 204M/862M [01:14<03:37, 3.02MB/s].vector_cache/glove.6B.zip:  24%|██▎       | 204M/862M [01:15<4:10:48, 43.7kB/s].vector_cache/glove.6B.zip:  24%|██▎       | 204M/862M [01:15<2:58:24, 61.5kB/s].vector_cache/glove.6B.zip:  24%|██▎       | 204M/862M [01:15<2:06:01, 87.0kB/s].vector_cache/glove.6B.zip:  24%|██▍       | 205M/862M [01:15<1:29:15, 123kB/s] .vector_cache/glove.6B.zip:  24%|██▍       | 205M/862M [01:15<1:03:30, 172kB/s].vector_cache/glove.6B.zip:  24%|██▍       | 206M/862M [01:15<45:28, 241kB/s]  .vector_cache/glove.6B.zip:  24%|██▍       | 206M/862M [01:16<32:39, 335kB/s].vector_cache/glove.6B.zip:  24%|██▍       | 206M/862M [01:16<23:57, 456kB/s].vector_cache/glove.6B.zip:  24%|██▍       | 207M/862M [01:16<17:45, 615kB/s].vector_cache/glove.6B.zip:  24%|██▍       | 207M/862M [01:16<13:32, 807kB/s].vector_cache/glove.6B.zip:  24%|██▍       | 207M/862M [01:16<10:26, 1.05MB/s].vector_cache/glove.6B.zip:  24%|██▍       | 208M/862M [01:16<08:25, 1.30MB/s].vector_cache/glove.6B.zip:  24%|██▍       | 208M/862M [01:17<12:13, 892kB/s] .vector_cache/glove.6B.zip:  24%|██▍       | 208M/862M [01:17<11:15, 968kB/s].vector_cache/glove.6B.zip:  24%|██▍       | 209M/862M [01:17<09:04, 1.20MB/s].vector_cache/glove.6B.zip:  24%|██▍       | 209M/862M [01:17<07:12, 1.51MB/s].vector_cache/glove.6B.zip:  24%|██▍       | 209M/862M [01:17<05:44, 1.89MB/s].vector_cache/glove.6B.zip:  24%|██▍       | 210M/862M [01:17<05:25, 2.01MB/s].vector_cache/glove.6B.zip:  24%|██▍       | 210M/862M [01:17<04:33, 2.38MB/s].vector_cache/glove.6B.zip:  24%|██▍       | 210M/862M [01:18<04:34, 2.37MB/s].vector_cache/glove.6B.zip:  24%|██▍       | 211M/862M [01:18<03:59, 2.72MB/s].vector_cache/glove.6B.zip:  24%|██▍       | 211M/862M [01:18<04:18, 2.52MB/s].vector_cache/glove.6B.zip:  25%|██▍       | 211M/862M [01:18<04:36, 2.35MB/s].vector_cache/glove.6B.zip:  25%|██▍       | 212M/862M [01:18<04:12, 2.58MB/s].vector_cache/glove.6B.zip:  25%|██▍       | 212M/862M [01:18<04:36, 2.36MB/s].vector_cache/glove.6B.zip:  25%|██▍       | 212M/862M [01:19<11:32, 938kB/s] .vector_cache/glove.6B.zip:  25%|██▍       | 212M/862M [01:19<09:52, 1.10MB/s].vector_cache/glove.6B.zip:  25%|██▍       | 213M/862M [01:19<08:01, 1.35MB/s].vector_cache/glove.6B.zip:  25%|██▍       | 213M/862M [01:19<06:42, 1.61MB/s].vector_cache/glove.6B.zip:  25%|██▍       | 214M/862M [01:19<05:44, 1.88MB/s].vector_cache/glove.6B.zip:  25%|██▍       | 214M/862M [01:19<05:03, 2.14MB/s].vector_cache/glove.6B.zip:  25%|██▍       | 215M/862M [01:20<04:32, 2.37MB/s].vector_cache/glove.6B.zip:  25%|██▍       | 215M/862M [01:20<04:11, 2.57MB/s].vector_cache/glove.6B.zip:  25%|██▍       | 215M/862M [01:20<03:54, 2.76MB/s].vector_cache/glove.6B.zip:  25%|██▌       | 216M/862M [01:20<03:41, 2.91MB/s].vector_cache/glove.6B.zip:  25%|██▌       | 216M/862M [01:21<08:00, 1.34MB/s].vector_cache/glove.6B.zip:  25%|██▌       | 216M/862M [01:21<08:08, 1.32MB/s].vector_cache/glove.6B.zip:  25%|██▌       | 217M/862M [01:21<06:47, 1.58MB/s].vector_cache/glove.6B.zip:  25%|██▌       | 217M/862M [01:21<05:42, 1.88MB/s].vector_cache/glove.6B.zip:  25%|██▌       | 218M/862M [01:21<04:53, 2.20MB/s].vector_cache/glove.6B.zip:  25%|██▌       | 218M/862M [01:21<04:20, 2.47MB/s].vector_cache/glove.6B.zip:  25%|██▌       | 219M/862M [01:21<03:56, 2.72MB/s].vector_cache/glove.6B.zip:  25%|██▌       | 219M/862M [01:22<03:38, 2.94MB/s].vector_cache/glove.6B.zip:  25%|██▌       | 220M/862M [01:22<03:22, 3.17MB/s].vector_cache/glove.6B.zip:  26%|██▌       | 220M/862M [01:22<03:17, 3.24MB/s].vector_cache/glove.6B.zip:  26%|██▌       | 220M/862M [01:23<15:34, 687kB/s] .vector_cache/glove.6B.zip:  26%|██▌       | 221M/862M [01:23<13:18, 803kB/s].vector_cache/glove.6B.zip:  26%|██▌       | 221M/862M [01:23<10:10, 1.05MB/s].vector_cache/glove.6B.zip:  26%|██▌       | 222M/862M [01:23<08:07, 1.31MB/s].vector_cache/glove.6B.zip:  26%|██▌       | 222M/862M [01:23<06:25, 1.66MB/s].vector_cache/glove.6B.zip:  26%|██▌       | 223M/862M [01:23<05:29, 1.94MB/s].vector_cache/glove.6B.zip:  26%|██▌       | 223M/862M [01:23<04:33, 2.33MB/s].vector_cache/glove.6B.zip:  26%|██▌       | 224M/862M [01:24<04:03, 2.62MB/s].vector_cache/glove.6B.zip:  26%|██▌       | 224M/862M [01:24<03:31, 3.02MB/s].vector_cache/glove.6B.zip:  26%|██▌       | 224M/862M [01:24<03:36, 2.95MB/s].vector_cache/glove.6B.zip:  26%|██▌       | 225M/862M [01:25<12:24, 857kB/s] .vector_cache/glove.6B.zip:  26%|██▌       | 225M/862M [01:25<10:57, 969kB/s].vector_cache/glove.6B.zip:  26%|██▌       | 225M/862M [01:25<08:35, 1.24MB/s].vector_cache/glove.6B.zip:  26%|██▌       | 226M/862M [01:25<06:48, 1.56MB/s].vector_cache/glove.6B.zip:  26%|██▌       | 226M/862M [01:25<05:41, 1.86MB/s].vector_cache/glove.6B.zip:  26%|██▋       | 227M/862M [01:25<04:49, 2.20MB/s].vector_cache/glove.6B.zip:  26%|██▋       | 227M/862M [01:25<04:14, 2.49MB/s].vector_cache/glove.6B.zip:  26%|██▋       | 228M/862M [01:26<04:12, 2.52MB/s].vector_cache/glove.6B.zip:  26%|██▋       | 228M/862M [01:26<03:37, 2.91MB/s].vector_cache/glove.6B.zip:  26%|██▋       | 228M/862M [01:26<03:42, 2.85MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 229M/862M [01:27<14:17, 738kB/s] .vector_cache/glove.6B.zip:  27%|██▋       | 229M/862M [01:27<13:05, 806kB/s].vector_cache/glove.6B.zip:  27%|██▋       | 229M/862M [01:27<10:19, 1.02MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 230M/862M [01:27<08:17, 1.27MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 230M/862M [01:27<06:40, 1.58MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 230M/862M [01:27<05:41, 1.85MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 231M/862M [01:27<04:47, 2.19MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 231M/862M [01:27<04:39, 2.26MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 231M/862M [01:28<04:09, 2.53MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 232M/862M [01:28<03:58, 2.64MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 232M/862M [01:28<03:46, 2.78MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 232M/862M [01:28<03:33, 2.95MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 233M/862M [01:28<03:37, 2.89MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 233M/862M [01:29<16:07, 651kB/s] .vector_cache/glove.6B.zip:  27%|██▋       | 233M/862M [01:29<13:44, 763kB/s].vector_cache/glove.6B.zip:  27%|██▋       | 233M/862M [01:29<10:37, 986kB/s].vector_cache/glove.6B.zip:  27%|██▋       | 234M/862M [01:29<08:20, 1.26MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 234M/862M [01:29<06:43, 1.56MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 235M/862M [01:29<05:29, 1.90MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 235M/862M [01:29<04:48, 2.17MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 236M/862M [01:29<04:14, 2.46MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 236M/862M [01:30<03:50, 2.72MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 237M/862M [01:30<03:32, 2.94MB/s].vector_cache/glove.6B.zip:  27%|██▋       | 237M/862M [01:30<17:28, 596kB/s] .vector_cache/glove.6B.zip:  27%|██▋       | 237M/862M [01:31<14:34, 715kB/s].vector_cache/glove.6B.zip:  28%|██▊       | 238M/862M [01:31<11:10, 932kB/s].vector_cache/glove.6B.zip:  28%|██▊       | 238M/862M [01:31<08:40, 1.20MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 239M/862M [01:31<06:54, 1.50MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 239M/862M [01:31<05:40, 1.83MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 239M/862M [01:31<04:37, 2.24MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 240M/862M [01:31<04:20, 2.39MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 240M/862M [01:31<03:42, 2.79MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 241M/862M [01:32<03:44, 2.77MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 241M/862M [01:32<03:16, 3.17MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 241M/862M [01:32<1:41:05, 102kB/s].vector_cache/glove.6B.zip:  28%|██▊       | 241M/862M [01:33<1:12:58, 142kB/s].vector_cache/glove.6B.zip:  28%|██▊       | 242M/862M [01:33<51:51, 199kB/s]  .vector_cache/glove.6B.zip:  28%|██▊       | 242M/862M [01:33<36:58, 280kB/s].vector_cache/glove.6B.zip:  28%|██▊       | 242M/862M [01:33<27:06, 381kB/s].vector_cache/glove.6B.zip:  28%|██▊       | 243M/862M [01:33<19:47, 521kB/s].vector_cache/glove.6B.zip:  28%|██▊       | 243M/862M [01:33<14:33, 708kB/s].vector_cache/glove.6B.zip:  28%|██▊       | 244M/862M [01:33<10:54, 945kB/s].vector_cache/glove.6B.zip:  28%|██▊       | 244M/862M [01:33<08:36, 1.20MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 245M/862M [01:33<06:45, 1.52MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 245M/862M [01:34<06:34, 1.56MB/s].vector_cache/glove.6B.zip:  28%|██▊       | 245M/862M [01:34<11:59, 857kB/s] .vector_cache/glove.6B.zip:  28%|██▊       | 245M/862M [01:35<11:48, 871kB/s].vector_cache/glove.6B.zip:  28%|██▊       | 246M/862M [01:35<09:28, 1.09MB/s].vector_cache/glove.6B.zip:  29%|██▊       | 246M/862M [01:35<07:35, 1.35MB/s].vector_cache/glove.6B.zip:  29%|██▊       | 246M/862M [01:35<06:12, 1.65MB/s].vector_cache/glove.6B.zip:  29%|██▊       | 247M/862M [01:35<06:01, 1.70MB/s].vector_cache/glove.6B.zip:  29%|██▊       | 247M/862M [01:35<05:07, 2.00MB/s].vector_cache/glove.6B.zip:  29%|██▊       | 247M/862M [01:35<04:26, 2.31MB/s].vector_cache/glove.6B.zip:  29%|██▊       | 248M/862M [01:35<04:24, 2.32MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 248M/862M [01:35<03:56, 2.60MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 248M/862M [01:36<03:59, 2.56MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 249M/862M [01:36<03:37, 2.82MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 249M/862M [01:36<03:41, 2.76MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 249M/862M [01:36<04:05, 2.50MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 249M/862M [01:36<13:43, 745kB/s] .vector_cache/glove.6B.zip:  29%|██▉       | 250M/862M [01:37<11:24, 895kB/s].vector_cache/glove.6B.zip:  29%|██▉       | 250M/862M [01:37<09:16, 1.10MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 250M/862M [01:37<07:44, 1.32MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 250M/862M [01:37<06:41, 1.52MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 251M/862M [01:37<05:44, 1.77MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 251M/862M [01:37<05:23, 1.89MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 252M/862M [01:37<04:48, 2.12MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 252M/862M [01:37<04:33, 2.23MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 252M/862M [01:38<04:21, 2.34MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 253M/862M [01:38<04:12, 2.41MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 253M/862M [01:38<03:51, 2.63MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 253M/862M [01:38<04:14, 2.40MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 253M/862M [01:38<07:15, 1.40MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 254M/862M [01:38<06:45, 1.50MB/s].vector_cache/glove.6B.zip:  29%|██▉       | 254M/862M [01:39<05:52, 1.72MB/s].vector_cache/glove.6B.zip:  30%|██▉       | 254M/862M [01:39<05:04, 2.00MB/s].vector_cache/glove.6B.zip:  30%|██▉       | 255M/862M [01:39<04:39, 2.17MB/s].vector_cache/glove.6B.zip:  30%|██▉       | 255M/862M [01:39<04:22, 2.31MB/s].vector_cache/glove.6B.zip:  30%|██▉       | 255M/862M [01:39<04:11, 2.41MB/s].vector_cache/glove.6B.zip:  30%|██▉       | 256M/862M [01:39<04:01, 2.51MB/s].vector_cache/glove.6B.zip:  30%|██▉       | 256M/862M [01:39<03:55, 2.57MB/s].vector_cache/glove.6B.zip:  30%|██▉       | 257M/862M [01:40<03:34, 2.82MB/s].vector_cache/glove.6B.zip:  30%|██▉       | 257M/862M [01:40<04:04, 2.48MB/s].vector_cache/glove.6B.zip:  30%|██▉       | 257M/862M [01:40<03:41, 2.73MB/s].vector_cache/glove.6B.zip:  30%|██▉       | 257M/862M [01:40<04:10, 2.41MB/s].vector_cache/glove.6B.zip:  30%|██▉       | 258M/862M [01:40<11:11, 900kB/s] .vector_cache/glove.6B.zip:  30%|██▉       | 258M/862M [01:40<09:29, 1.06MB/s].vector_cache/glove.6B.zip:  30%|██▉       | 258M/862M [01:41<07:35, 1.33MB/s].vector_cache/glove.6B.zip:  30%|██▉       | 259M/862M [01:41<06:32, 1.54MB/s].vector_cache/glove.6B.zip:  30%|███       | 259M/862M [01:41<05:29, 1.83MB/s].vector_cache/glove.6B.zip:  30%|███       | 259M/862M [01:41<04:56, 2.03MB/s].vector_cache/glove.6B.zip:  30%|███       | 259M/862M [01:41<05:37, 1.79MB/s].vector_cache/glove.6B.zip:  30%|███       | 260M/862M [01:41<05:24, 1.86MB/s].vector_cache/glove.6B.zip:  30%|███       | 260M/862M [01:41<04:59, 2.01MB/s].vector_cache/glove.6B.zip:  30%|███       | 260M/862M [01:41<04:38, 2.16MB/s].vector_cache/glove.6B.zip:  30%|███       | 260M/862M [01:42<04:59, 2.01MB/s].vector_cache/glove.6B.zip:  30%|███       | 261M/862M [01:42<04:32, 2.21MB/s].vector_cache/glove.6B.zip:  30%|███       | 261M/862M [01:42<04:53, 2.05MB/s].vector_cache/glove.6B.zip:  30%|███       | 261M/862M [01:42<04:28, 2.24MB/s].vector_cache/glove.6B.zip:  30%|███       | 261M/862M [01:42<04:43, 2.12MB/s].vector_cache/glove.6B.zip:  30%|███       | 262M/862M [01:42<04:16, 2.34MB/s].vector_cache/glove.6B.zip:  30%|███       | 262M/862M [01:42<34:00, 294kB/s] .vector_cache/glove.6B.zip:  30%|███       | 262M/862M [01:42<25:00, 400kB/s].vector_cache/glove.6B.zip:  30%|███       | 262M/862M [01:43<18:40, 535kB/s].vector_cache/glove.6B.zip:  30%|███       | 263M/862M [01:43<14:12, 703kB/s].vector_cache/glove.6B.zip:  31%|███       | 263M/862M [01:43<11:05, 900kB/s].vector_cache/glove.6B.zip:  31%|███       | 263M/862M [01:43<08:54, 1.12MB/s].vector_cache/glove.6B.zip:  31%|███       | 264M/862M [01:43<07:22, 1.35MB/s].vector_cache/glove.6B.zip:  31%|███       | 264M/862M [01:43<06:32, 1.53MB/s].vector_cache/glove.6B.zip:  31%|███       | 264M/862M [01:43<06:06, 1.63MB/s].vector_cache/glove.6B.zip:  31%|███       | 265M/862M [01:43<05:41, 1.75MB/s].vector_cache/glove.6B.zip:  31%|███       | 265M/862M [01:44<05:29, 1.81MB/s].vector_cache/glove.6B.zip:  31%|███       | 265M/862M [01:44<05:27, 1.82MB/s].vector_cache/glove.6B.zip:  31%|███       | 265M/862M [01:44<05:15, 1.89MB/s].vector_cache/glove.6B.zip:  31%|███       | 266M/862M [01:44<05:05, 1.95MB/s].vector_cache/glove.6B.zip:  31%|███       | 266M/862M [01:44<09:43, 1.02MB/s].vector_cache/glove.6B.zip:  31%|███       | 266M/862M [01:44<08:13, 1.21MB/s].vector_cache/glove.6B.zip:  31%|███       | 266M/862M [01:45<07:06, 1.40MB/s].vector_cache/glove.6B.zip:  31%|███       | 267M/862M [01:45<06:20, 1.57MB/s].vector_cache/glove.6B.zip:  31%|███       | 267M/862M [01:45<05:48, 1.71MB/s].vector_cache/glove.6B.zip:  31%|███       | 267M/862M [01:45<05:24, 1.83MB/s].vector_cache/glove.6B.zip:  31%|███       | 268M/862M [01:45<05:00, 1.98MB/s].vector_cache/glove.6B.zip:  31%|███       | 268M/862M [01:45<04:50, 2.05MB/s].vector_cache/glove.6B.zip:  31%|███       | 268M/862M [01:45<04:48, 2.06MB/s].vector_cache/glove.6B.zip:  31%|███       | 268M/862M [01:45<05:15, 1.88MB/s].vector_cache/glove.6B.zip:  31%|███       | 269M/862M [01:46<05:33, 1.78MB/s].vector_cache/glove.6B.zip:  31%|███       | 269M/862M [01:46<05:45, 1.72MB/s].vector_cache/glove.6B.zip:  31%|███       | 269M/862M [01:46<05:46, 1.71MB/s].vector_cache/glove.6B.zip:  31%|███       | 269M/862M [01:46<05:47, 1.71MB/s].vector_cache/glove.6B.zip:  31%|███▏      | 269M/862M [01:46<05:44, 1.72MB/s].vector_cache/glove.6B.zip:  31%|███▏      | 270M/862M [01:46<05:46, 1.71MB/s].vector_cache/glove.6B.zip:  31%|███▏      | 270M/862M [01:46<05:41, 1.73MB/s].vector_cache/glove.6B.zip:  31%|███▏      | 270M/862M [01:47<05:40, 1.74MB/s].vector_cache/glove.6B.zip:  31%|███▏      | 270M/862M [01:47<05:35, 1.76MB/s].vector_cache/glove.6B.zip:  31%|███▏      | 271M/862M [01:47<05:32, 1.78MB/s].vector_cache/glove.6B.zip:  31%|███▏      | 271M/862M [01:47<05:26, 1.81MB/s].vector_cache/glove.6B.zip:  31%|███▏      | 271M/862M [01:47<05:25, 1.81MB/s].vector_cache/glove.6B.zip:  31%|███▏      | 271M/862M [01:47<05:22, 1.83MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 272M/862M [01:47<05:21, 1.84MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 272M/862M [01:47<05:19, 1.85MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 272M/862M [01:48<05:21, 1.83MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 272M/862M [01:48<05:56, 1.66MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 273M/862M [01:48<06:16, 1.56MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 273M/862M [01:48<06:21, 1.55MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 273M/862M [01:48<06:28, 1.52MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 273M/862M [01:48<06:24, 1.53MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 273M/862M [01:48<05:55, 1.66MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 273M/862M [01:49<06:45, 1.45MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 274M/862M [01:49<06:10, 1.59MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 274M/862M [01:49<06:37, 1.48MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 274M/862M [01:49<06:04, 1.61MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 274M/862M [01:49<06:25, 1.53MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 274M/862M [01:49<06:03, 1.62MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 275M/862M [01:49<06:00, 1.63MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 275M/862M [01:49<05:41, 1.72MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 275M/862M [01:49<05:49, 1.68MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 275M/862M [01:49<05:28, 1.79MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 275M/862M [01:50<05:46, 1.69MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 275M/862M [01:50<05:22, 1.82MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 276M/862M [01:50<05:49, 1.68MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 276M/862M [01:50<05:18, 1.84MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 276M/862M [01:50<05:54, 1.65MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 276M/862M [01:50<05:42, 1.71MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 276M/862M [01:50<05:16, 1.85MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 277M/862M [01:50<05:42, 1.71MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 277M/862M [01:50<05:16, 1.85MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 277M/862M [01:50<05:39, 1.73MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 277M/862M [01:51<05:30, 1.77MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 277M/862M [01:51<05:02, 1.93MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 278M/862M [01:51<05:42, 1.71MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 278M/862M [01:51<05:16, 1.85MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 278M/862M [01:51<05:36, 1.73MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 278M/862M [01:51<05:12, 1.87MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 278M/862M [01:51<05:32, 1.75MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 279M/862M [01:51<05:09, 1.89MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 279M/862M [01:51<05:33, 1.75MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 279M/862M [01:52<05:09, 1.88MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 279M/862M [01:52<05:21, 1.81MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 279M/862M [01:52<05:01, 1.93MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 280M/862M [01:52<05:13, 1.86MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 280M/862M [01:52<04:59, 1.94MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 280M/862M [01:52<05:08, 1.89MB/s].vector_cache/glove.6B.zip:  32%|███▏      | 280M/862M [01:52<05:05, 1.91MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 280M/862M [01:52<05:04, 1.91MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 281M/862M [01:52<04:49, 2.01MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 281M/862M [01:52<04:47, 2.02MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 281M/862M [01:53<04:35, 2.11MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 281M/862M [01:53<04:48, 2.02MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 282M/862M [01:53<04:32, 2.13MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 282M/862M [01:53<04:43, 2.05MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 282M/862M [01:53<04:44, 2.04MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 282M/862M [01:53<04:31, 2.13MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 283M/862M [01:53<04:29, 2.15MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 283M/862M [01:53<04:23, 2.20MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 283M/862M [01:53<04:30, 2.14MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 283M/862M [01:54<04:24, 2.19MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 283M/862M [01:54<04:23, 2.19MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 284M/862M [01:54<04:20, 2.22MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 284M/862M [01:54<04:18, 2.24MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 284M/862M [01:54<04:12, 2.29MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 284M/862M [01:54<04:14, 2.27MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 285M/862M [01:54<04:11, 2.30MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 285M/862M [01:54<04:11, 2.29MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 285M/862M [01:54<04:07, 2.33MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 285M/862M [01:54<04:09, 2.31MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 286M/862M [01:55<04:01, 2.39MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 286M/862M [01:55<04:07, 2.32MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 286M/862M [01:55<03:57, 2.42MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 286M/862M [01:55<04:04, 2.36MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 287M/862M [01:55<04:01, 2.39MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 287M/862M [01:55<04:39, 2.06MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 287M/862M [01:55<04:37, 2.07MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 287M/862M [01:55<05:01, 1.91MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 287M/862M [01:55<04:51, 1.98MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 287M/862M [01:55<05:09, 1.86MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 288M/862M [01:56<04:48, 1.99MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 288M/862M [01:56<05:01, 1.90MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 288M/862M [01:56<04:52, 1.96MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 288M/862M [01:56<04:40, 2.05MB/s].vector_cache/glove.6B.zip:  33%|███▎      | 289M/862M [01:56<04:45, 2.01MB/s].vector_cache/glove.6B.zip:  34%|███▎      | 289M/862M [01:56<04:30, 2.12MB/s].vector_cache/glove.6B.zip:  34%|███▎      | 289M/862M [01:56<04:40, 2.05MB/s].vector_cache/glove.6B.zip:  34%|███▎      | 289M/862M [01:56<04:24, 2.17MB/s].vector_cache/glove.6B.zip:  34%|███▎      | 289M/862M [01:56<04:30, 2.11MB/s].vector_cache/glove.6B.zip:  34%|███▎      | 290M/862M [01:57<04:17, 2.22MB/s].vector_cache/glove.6B.zip:  34%|███▎      | 290M/862M [01:57<04:15, 2.24MB/s].vector_cache/glove.6B.zip:  34%|███▎      | 290M/862M [01:57<04:10, 2.28MB/s].vector_cache/glove.6B.zip:  34%|███▎      | 290M/862M [01:57<04:10, 2.28MB/s].vector_cache/glove.6B.zip:  34%|███▎      | 291M/862M [01:57<04:04, 2.33MB/s].vector_cache/glove.6B.zip:  34%|███▎      | 291M/862M [01:57<04:08, 2.30MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 291M/862M [01:57<03:58, 2.39MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 291M/862M [01:57<04:05, 2.33MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 292M/862M [01:57<04:06, 2.32MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 292M/862M [01:57<03:56, 2.41MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 292M/862M [01:58<04:00, 2.37MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 293M/862M [01:58<03:53, 2.44MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 293M/862M [01:58<03:57, 2.40MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 293M/862M [01:58<03:49, 2.48MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 293M/862M [01:58<03:57, 2.39MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 294M/862M [01:58<03:50, 2.47MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 294M/862M [01:58<03:55, 2.41MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 294M/862M [01:58<03:48, 2.49MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 294M/862M [01:58<03:49, 2.47MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 294M/862M [01:58<04:30, 2.10MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 295M/862M [01:59<04:18, 2.19MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 295M/862M [01:59<04:08, 2.29MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 295M/862M [01:59<04:02, 2.34MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 296M/862M [01:59<03:58, 2.38MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 296M/862M [01:59<03:53, 2.42MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 296M/862M [01:59<03:51, 2.44MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 297M/862M [01:59<03:49, 2.46MB/s].vector_cache/glove.6B.zip:  34%|███▍      | 297M/862M [02:00<03:48, 2.47MB/s].vector_cache/glove.6B.zip:  35%|███▍      | 297M/862M [02:00<03:44, 2.51MB/s].vector_cache/glove.6B.zip:  35%|███▍      | 298M/862M [02:00<03:45, 2.50MB/s].vector_cache/glove.6B.zip:  35%|███▍      | 298M/862M [02:00<03:44, 2.52MB/s].vector_cache/glove.6B.zip:  35%|███▍      | 299M/862M [02:00<03:42, 2.54MB/s].vector_cache/glove.6B.zip:  35%|███▍      | 299M/862M [02:00<26:23, 356kB/s] .vector_cache/glove.6B.zip:  35%|███▍      | 299M/862M [02:01<20:11, 465kB/s].vector_cache/glove.6B.zip:  35%|███▍      | 299M/862M [02:01<15:16, 615kB/s].vector_cache/glove.6B.zip:  35%|███▍      | 299M/862M [02:01<11:45, 797kB/s].vector_cache/glove.6B.zip:  35%|███▍      | 300M/862M [02:01<09:17, 1.01MB/s].vector_cache/glove.6B.zip:  35%|███▍      | 300M/862M [02:01<07:33, 1.24MB/s].vector_cache/glove.6B.zip:  35%|███▍      | 301M/862M [02:01<06:10, 1.52MB/s].vector_cache/glove.6B.zip:  35%|███▍      | 301M/862M [02:01<05:21, 1.75MB/s].vector_cache/glove.6B.zip:  35%|███▍      | 301M/862M [02:02<04:46, 1.96MB/s].vector_cache/glove.6B.zip:  35%|███▍      | 302M/862M [02:02<04:30, 2.07MB/s].vector_cache/glove.6B.zip:  35%|███▌      | 302M/862M [02:02<04:09, 2.25MB/s].vector_cache/glove.6B.zip:  35%|███▌      | 302M/862M [02:02<03:44, 2.49MB/s].vector_cache/glove.6B.zip:  35%|███▌      | 303M/862M [02:02<07:55, 1.18MB/s].vector_cache/glove.6B.zip:  35%|███▌      | 303M/862M [02:03<07:09, 1.30MB/s].vector_cache/glove.6B.zip:  35%|███▌      | 303M/862M [02:03<06:01, 1.55MB/s].vector_cache/glove.6B.zip:  35%|███▌      | 304M/862M [02:03<05:06, 1.82MB/s].vector_cache/glove.6B.zip:  35%|███▌      | 304M/862M [02:03<04:33, 2.04MB/s].vector_cache/glove.6B.zip:  35%|███▌      | 304M/862M [02:03<04:09, 2.24MB/s].vector_cache/glove.6B.zip:  35%|███▌      | 305M/862M [02:03<03:56, 2.36MB/s].vector_cache/glove.6B.zip:  35%|███▌      | 305M/862M [02:03<03:37, 2.56MB/s].vector_cache/glove.6B.zip:  35%|███▌      | 306M/862M [02:03<03:28, 2.67MB/s].vector_cache/glove.6B.zip:  35%|███▌      | 306M/862M [02:04<03:22, 2.75MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 306M/862M [02:04<03:15, 2.84MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 307M/862M [02:04<07:31, 1.23MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 307M/862M [02:05<06:44, 1.37MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 307M/862M [02:05<05:39, 1.63MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 308M/862M [02:05<04:50, 1.91MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 308M/862M [02:05<04:08, 2.23MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 309M/862M [02:05<03:46, 2.45MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 309M/862M [02:05<03:31, 2.62MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 309M/862M [02:05<04:04, 2.27MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 310M/862M [02:05<03:28, 2.65MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 310M/862M [02:05<03:36, 2.54MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 310M/862M [02:06<03:42, 2.48MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 310M/862M [02:06<03:42, 2.48MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 311M/862M [02:06<03:45, 2.45MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 311M/862M [02:06<03:45, 2.45MB/s].vector_cache/glove.6B.zip:  36%|███▌      | 311M/862M [02:06<1:21:05, 113kB/s].vector_cache/glove.6B.zip:  36%|███▌      | 311M/862M [02:06<58:18, 157kB/s]  .vector_cache/glove.6B.zip:  36%|███▌      | 312M/862M [02:07<41:52, 219kB/s].vector_cache/glove.6B.zip:  36%|███▌      | 312M/862M [02:07<30:19, 303kB/s].vector_cache/glove.6B.zip:  36%|███▌      | 312M/862M [02:07<22:12, 413kB/s].vector_cache/glove.6B.zip:  36%|███▋      | 313M/862M [02:07<16:31, 554kB/s].vector_cache/glove.6B.zip:  36%|███▋      | 313M/862M [02:07<12:25, 737kB/s].vector_cache/glove.6B.zip:  36%|███▋      | 313M/862M [02:08<11:20, 807kB/s].vector_cache/glove.6B.zip:  36%|███▋      | 314M/862M [02:08<08:21, 1.09MB/s].vector_cache/glove.6B.zip:  36%|███▋      | 315M/862M [02:08<06:40, 1.37MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 315M/862M [02:08<05:34, 1.63MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 315M/862M [02:08<48:54, 186kB/s] .vector_cache/glove.6B.zip:  37%|███▋      | 315M/862M [02:08<35:34, 256kB/s].vector_cache/glove.6B.zip:  37%|███▋      | 316M/862M [02:09<25:49, 353kB/s].vector_cache/glove.6B.zip:  37%|███▋      | 316M/862M [02:09<18:57, 480kB/s].vector_cache/glove.6B.zip:  37%|███▋      | 317M/862M [02:09<14:07, 644kB/s].vector_cache/glove.6B.zip:  37%|███▋      | 317M/862M [02:09<10:44, 846kB/s].vector_cache/glove.6B.zip:  37%|███▋      | 317M/862M [02:09<08:31, 1.07MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 318M/862M [02:09<07:00, 1.29MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 318M/862M [02:09<06:03, 1.50MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 318M/862M [02:10<05:25, 1.67MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 319M/862M [02:10<04:48, 1.89MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 319M/862M [02:10<04:50, 1.87MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 319M/862M [02:10<04:21, 2.08MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 319M/862M [02:10<31:01, 292kB/s] .vector_cache/glove.6B.zip:  37%|███▋      | 319M/862M [02:10<23:14, 389kB/s].vector_cache/glove.6B.zip:  37%|███▋      | 320M/862M [02:11<17:21, 521kB/s].vector_cache/glove.6B.zip:  37%|███▋      | 320M/862M [02:11<13:12, 684kB/s].vector_cache/glove.6B.zip:  37%|███▋      | 320M/862M [02:11<10:16, 879kB/s].vector_cache/glove.6B.zip:  37%|███▋      | 321M/862M [02:11<08:13, 1.10MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 321M/862M [02:11<06:47, 1.33MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 321M/862M [02:11<05:40, 1.59MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 322M/862M [02:11<05:00, 1.80MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 322M/862M [02:11<04:30, 2.00MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 322M/862M [02:12<04:11, 2.15MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 323M/862M [02:12<04:01, 2.23MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 323M/862M [02:12<03:43, 2.41MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 323M/862M [02:12<03:33, 2.53MB/s].vector_cache/glove.6B.zip:  37%|███▋      | 323M/862M [02:12<20:58, 428kB/s] .vector_cache/glove.6B.zip:  38%|███▊      | 324M/862M [02:12<16:06, 557kB/s].vector_cache/glove.6B.zip:  38%|███▊      | 324M/862M [02:13<12:10, 737kB/s].vector_cache/glove.6B.zip:  38%|███▊      | 324M/862M [02:13<09:36, 933kB/s].vector_cache/glove.6B.zip:  38%|███▊      | 325M/862M [02:13<07:42, 1.16MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 325M/862M [02:13<06:22, 1.40MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 325M/862M [02:13<05:26, 1.64MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 326M/862M [02:13<04:40, 1.91MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 326M/862M [02:13<04:15, 2.10MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 326M/862M [02:13<03:57, 2.26MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 327M/862M [02:14<03:43, 2.39MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 327M/862M [02:14<03:33, 2.50MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 327M/862M [02:14<10:11, 875kB/s] .vector_cache/glove.6B.zip:  38%|███▊      | 328M/862M [02:14<08:31, 1.05MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 328M/862M [02:14<06:55, 1.29MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 328M/862M [02:15<05:45, 1.55MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 329M/862M [02:15<04:56, 1.80MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 329M/862M [02:15<04:21, 2.04MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 330M/862M [02:15<03:51, 2.31MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 330M/862M [02:15<03:34, 2.49MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 330M/862M [02:15<03:29, 2.54MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 331M/862M [02:15<03:12, 2.75MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 331M/862M [02:16<03:07, 2.83MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 332M/862M [02:16<08:33, 1.03MB/s].vector_cache/glove.6B.zip:  38%|███▊      | 332M/862M [02:16<08:19, 1.06MB/s].vector_cache/glove.6B.zip:  39%|███▊      | 332M/862M [02:16<06:47, 1.30MB/s].vector_cache/glove.6B.zip:  39%|███▊      | 332M/862M [02:17<05:28, 1.61MB/s].vector_cache/glove.6B.zip:  39%|███▊      | 333M/862M [02:17<04:42, 1.87MB/s].vector_cache/glove.6B.zip:  39%|███▊      | 333M/862M [02:17<04:18, 2.05MB/s].vector_cache/glove.6B.zip:  39%|███▊      | 334M/862M [02:17<03:42, 2.38MB/s].vector_cache/glove.6B.zip:  39%|███▊      | 334M/862M [02:17<03:29, 2.52MB/s].vector_cache/glove.6B.zip:  39%|███▉      | 334M/862M [02:17<03:23, 2.60MB/s].vector_cache/glove.6B.zip:  39%|███▉      | 335M/862M [02:17<03:11, 2.75MB/s].vector_cache/glove.6B.zip:  39%|███▉      | 335M/862M [02:17<02:53, 3.05MB/s].vector_cache/glove.6B.zip:  39%|███▉      | 335M/862M [02:17<02:57, 2.98MB/s].vector_cache/glove.6B.zip:  39%|███▉      | 336M/862M [02:18<07:42, 1.14MB/s].vector_cache/glove.6B.zip:  39%|███▉      | 336M/862M [02:18<07:10, 1.22MB/s].vector_cache/glove.6B.zip:  39%|███▉      | 336M/862M [02:18<05:51, 1.50MB/s].vector_cache/glove.6B.zip:  39%|███▉      | 336M/862M [02:18<04:58, 1.76MB/s].vector_cache/glove.6B.zip:  39%|███▉      | 337M/862M [02:19<04:18, 2.04MB/s].vector_cache/glove.6B.zip:  39%|███▉      | 337M/862M [02:19<03:57, 2.21MB/s].vector_cache/glove.6B.zip:  39%|███▉      | 338M/862M [02:19<03:24, 2.57MB/s].vector_cache/glove.6B.zip:  39%|███▉      | 338M/862M [02:19<03:20, 2.62MB/s].vector_cache/glove.6B.zip:  39%|███▉      | 338M/862M [02:19<02:58, 2.93MB/s].vector_cache/glove.6B.zip:  39%|███▉      | 339M/862M [02:19<03:01, 2.88MB/s].vector_cache/glove.6B.zip:  39%|███▉      | 339M/862M [02:19<02:46, 3.15MB/s].vector_cache/glove.6B.zip:  39%|███▉      | 339M/862M [02:19<02:51, 3.04MB/s].vector_cache/glove.6B.zip:  39%|███▉      | 340M/862M [02:19<02:45, 3.16MB/s].vector_cache/glove.6B.zip:  39%|███▉      | 340M/862M [02:20<13:34, 641kB/s] .vector_cache/glove.6B.zip:  39%|███▉      | 340M/862M [02:20<11:27, 759kB/s].vector_cache/glove.6B.zip:  39%|███▉      | 340M/862M [02:20<08:41, 1.00MB/s].vector_cache/glove.6B.zip:  40%|███▉      | 341M/862M [02:20<06:49, 1.27MB/s].vector_cache/glove.6B.zip:  40%|███▉      | 341M/862M [02:21<05:31, 1.57MB/s].vector_cache/glove.6B.zip:  40%|███▉      | 341M/862M [02:21<04:37, 1.87MB/s].vector_cache/glove.6B.zip:  40%|███▉      | 342M/862M [02:21<03:55, 2.21MB/s].vector_cache/glove.6B.zip:  40%|███▉      | 342M/862M [02:21<03:29, 2.48MB/s].vector_cache/glove.6B.zip:  40%|███▉      | 343M/862M [02:21<03:07, 2.77MB/s].vector_cache/glove.6B.zip:  40%|███▉      | 343M/862M [02:21<02:54, 2.98MB/s].vector_cache/glove.6B.zip:  40%|███▉      | 343M/862M [02:21<02:41, 3.20MB/s].vector_cache/glove.6B.zip:  40%|███▉      | 344M/862M [02:21<02:36, 3.31MB/s].vector_cache/glove.6B.zip:  40%|███▉      | 344M/862M [02:22<12:00, 719kB/s] .vector_cache/glove.6B.zip:  40%|███▉      | 344M/862M [02:22<10:07, 852kB/s].vector_cache/glove.6B.zip:  40%|███▉      | 345M/862M [02:22<07:50, 1.10MB/s].vector_cache/glove.6B.zip:  40%|████      | 345M/862M [02:22<06:05, 1.41MB/s].vector_cache/glove.6B.zip:  40%|████      | 346M/862M [02:23<04:47, 1.80MB/s].vector_cache/glove.6B.zip:  40%|████      | 346M/862M [02:23<03:55, 2.19MB/s].vector_cache/glove.6B.zip:  40%|████      | 347M/862M [02:23<03:18, 2.60MB/s].vector_cache/glove.6B.zip:  40%|████      | 348M/862M [02:23<02:52, 2.99MB/s].vector_cache/glove.6B.zip:  40%|████      | 348M/862M [02:24<07:55, 1.08MB/s].vector_cache/glove.6B.zip:  40%|████      | 348M/862M [02:24<08:22, 1.02MB/s].vector_cache/glove.6B.zip:  40%|████      | 349M/862M [02:24<06:33, 1.31MB/s].vector_cache/glove.6B.zip:  40%|████      | 349M/862M [02:24<05:35, 1.53MB/s].vector_cache/glove.6B.zip:  41%|████      | 350M/862M [02:25<04:17, 1.99MB/s].vector_cache/glove.6B.zip:  41%|████      | 350M/862M [02:25<03:42, 2.31MB/s].vector_cache/glove.6B.zip:  41%|████      | 350M/862M [02:25<03:16, 2.61MB/s].vector_cache/glove.6B.zip:  41%|████      | 351M/862M [02:25<03:00, 2.83MB/s].vector_cache/glove.6B.zip:  41%|████      | 351M/862M [02:25<03:06, 2.74MB/s].vector_cache/glove.6B.zip:  41%|████      | 351M/862M [02:25<03:08, 2.70MB/s].vector_cache/glove.6B.zip:  41%|████      | 352M/862M [02:25<03:06, 2.74MB/s].vector_cache/glove.6B.zip:  41%|████      | 352M/862M [02:25<03:06, 2.73MB/s].vector_cache/glove.6B.zip:  41%|████      | 352M/862M [02:26<10:07, 839kB/s] .vector_cache/glove.6B.zip:  41%|████      | 352M/862M [02:26<09:25, 902kB/s].vector_cache/glove.6B.zip:  41%|████      | 353M/862M [02:26<07:25, 1.14MB/s].vector_cache/glove.6B.zip:  41%|████      | 353M/862M [02:26<06:08, 1.38MB/s].vector_cache/glove.6B.zip:  41%|████      | 353M/862M [02:27<05:09, 1.64MB/s].vector_cache/glove.6B.zip:  41%|████      | 354M/862M [02:27<04:42, 1.80MB/s].vector_cache/glove.6B.zip:  41%|████      | 354M/862M [02:27<04:00, 2.11MB/s].vector_cache/glove.6B.zip:  41%|████      | 354M/862M [02:27<03:50, 2.21MB/s].vector_cache/glove.6B.zip:  41%|████      | 355M/862M [02:27<04:14, 1.99MB/s].vector_cache/glove.6B.zip:  41%|████      | 355M/862M [02:27<03:59, 2.12MB/s].vector_cache/glove.6B.zip:  41%|████      | 355M/862M [02:27<03:47, 2.23MB/s].vector_cache/glove.6B.zip:  41%|████      | 355M/862M [02:27<04:04, 2.07MB/s].vector_cache/glove.6B.zip:  41%|████▏     | 356M/862M [02:28<03:57, 2.14MB/s].vector_cache/glove.6B.zip:  41%|████▏     | 356M/862M [02:28<03:43, 2.27MB/s].vector_cache/glove.6B.zip:  41%|████▏     | 356M/862M [02:28<06:14, 1.35MB/s].vector_cache/glove.6B.zip:  41%|████▏     | 357M/862M [02:28<05:24, 1.56MB/s].vector_cache/glove.6B.zip:  41%|████▏     | 357M/862M [02:28<04:39, 1.81MB/s].vector_cache/glove.6B.zip:  41%|████▏     | 357M/862M [02:28<04:25, 1.90MB/s].vector_cache/glove.6B.zip:  41%|████▏     | 358M/862M [02:29<04:07, 2.04MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 358M/862M [02:29<03:54, 2.15MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 358M/862M [02:29<03:34, 2.35MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 359M/862M [02:29<03:26, 2.44MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 359M/862M [02:29<03:28, 2.42MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 359M/862M [02:29<03:22, 2.49MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 359M/862M [02:29<05:58, 1.40MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 360M/862M [02:29<04:52, 1.72MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 360M/862M [02:29<04:44, 1.77MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 360M/862M [02:30<04:54, 1.70MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 360M/862M [02:30<04:33, 1.84MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 360M/862M [02:30<04:32, 1.84MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 360M/862M [02:30<23:30, 356kB/s] .vector_cache/glove.6B.zip:  42%|████▏     | 361M/862M [02:30<17:42, 472kB/s].vector_cache/glove.6B.zip:  42%|████▏     | 361M/862M [02:30<13:28, 620kB/s].vector_cache/glove.6B.zip:  42%|████▏     | 361M/862M [02:30<10:51, 770kB/s].vector_cache/glove.6B.zip:  42%|████▏     | 361M/862M [02:30<09:02, 923kB/s].vector_cache/glove.6B.zip:  42%|████▏     | 362M/862M [02:31<07:36, 1.10MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 362M/862M [02:31<06:32, 1.28MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 362M/862M [02:31<05:47, 1.44MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 362M/862M [02:31<05:14, 1.59MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 363M/862M [02:31<04:50, 1.72MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 363M/862M [02:31<04:34, 1.82MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 363M/862M [02:31<04:22, 1.90MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 364M/862M [02:32<04:13, 1.97MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 364M/862M [02:32<04:07, 2.02MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 364M/862M [02:32<04:02, 2.05MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 364M/862M [02:32<03:58, 2.08MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 365M/862M [02:32<03:56, 2.11MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 365M/862M [02:32<03:51, 2.14MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 365M/862M [02:32<03:49, 2.17MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 366M/862M [02:33<03:47, 2.18MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 366M/862M [02:33<03:44, 2.21MB/s].vector_cache/glove.6B.zip:  42%|████▏     | 366M/862M [02:33<03:42, 2.23MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 367M/862M [02:33<03:39, 2.26MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 367M/862M [02:33<03:36, 2.28MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 367M/862M [02:33<03:34, 2.30MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 368M/862M [02:33<03:36, 2.29MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 368M/862M [02:33<03:32, 2.32MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 368M/862M [02:34<03:28, 2.37MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 368M/862M [02:34<05:41, 1.45MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 369M/862M [02:34<04:58, 1.65MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 369M/862M [02:34<04:23, 1.87MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 369M/862M [02:34<04:02, 2.03MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 370M/862M [02:34<03:53, 2.11MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 370M/862M [02:34<03:36, 2.27MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 370M/862M [02:35<03:28, 2.36MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 371M/862M [02:35<03:22, 2.43MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 371M/862M [02:35<03:18, 2.47MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 372M/862M [02:35<03:14, 2.52MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 372M/862M [02:35<03:12, 2.55MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 372M/862M [02:35<03:08, 2.60MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 373M/862M [02:36<06:33, 1.24MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 373M/862M [02:36<05:54, 1.38MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 373M/862M [02:36<05:03, 1.61MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 374M/862M [02:36<04:25, 1.84MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 374M/862M [02:36<03:58, 2.05MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 374M/862M [02:36<03:39, 2.22MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 375M/862M [02:37<03:25, 2.37MB/s].vector_cache/glove.6B.zip:  43%|████▎     | 375M/862M [02:37<03:09, 2.57MB/s].vector_cache/glove.6B.zip:  44%|████▎     | 375M/862M [02:37<03:03, 2.66MB/s].vector_cache/glove.6B.zip:  44%|████▎     | 376M/862M [02:37<02:46, 2.91MB/s].vector_cache/glove.6B.zip:  44%|████▎     | 376M/862M [02:37<03:08, 2.58MB/s].vector_cache/glove.6B.zip:  44%|████▎     | 376M/862M [02:37<02:48, 2.88MB/s].vector_cache/glove.6B.zip:  44%|████▎     | 377M/862M [02:37<03:11, 2.54MB/s].vector_cache/glove.6B.zip:  44%|████▎     | 377M/862M [02:38<50:17, 161kB/s] .vector_cache/glove.6B.zip:  44%|████▎     | 377M/862M [02:38<36:29, 222kB/s].vector_cache/glove.6B.zip:  44%|████▍     | 377M/862M [02:38<26:14, 308kB/s].vector_cache/glove.6B.zip:  44%|████▍     | 378M/862M [02:38<19:15, 419kB/s].vector_cache/glove.6B.zip:  44%|████▍     | 378M/862M [02:38<14:17, 564kB/s].vector_cache/glove.6B.zip:  44%|████▍     | 379M/862M [02:38<10:47, 748kB/s].vector_cache/glove.6B.zip:  44%|████▍     | 379M/862M [02:39<08:29, 949kB/s].vector_cache/glove.6B.zip:  44%|████▍     | 379M/862M [02:39<06:33, 1.23MB/s].vector_cache/glove.6B.zip:  44%|████▍     | 380M/862M [02:39<06:52, 1.17MB/s].vector_cache/glove.6B.zip:  44%|████▍     | 380M/862M [02:39<05:13, 1.54MB/s].vector_cache/glove.6B.zip:  44%|████▍     | 381M/862M [02:39<04:17, 1.87MB/s].vector_cache/glove.6B.zip:  44%|████▍     | 381M/862M [02:40<11:01, 728kB/s] .vector_cache/glove.6B.zip:  44%|████▍     | 381M/862M [02:40<08:47, 913kB/s].vector_cache/glove.6B.zip:  44%|████▍     | 382M/862M [02:40<06:51, 1.17MB/s].vector_cache/glove.6B.zip:  44%|████▍     | 382M/862M [02:40<05:24, 1.48MB/s].vector_cache/glove.6B.zip:  44%|████▍     | 382M/862M [02:40<04:31, 1.77MB/s].vector_cache/glove.6B.zip:  44%|████▍     | 383M/862M [02:40<03:43, 2.14MB/s].vector_cache/glove.6B.zip:  44%|████▍     | 383M/862M [02:41<03:49, 2.09MB/s].vector_cache/glove.6B.zip:  45%|████▍     | 384M/862M [02:41<03:09, 2.53MB/s].vector_cache/glove.6B.zip:  45%|████▍     | 384M/862M [02:41<03:05, 2.58MB/s].vector_cache/glove.6B.zip:  45%|████▍     | 385M/862M [02:41<03:00, 2.65MB/s].vector_cache/glove.6B.zip:  45%|████▍     | 385M/862M [02:42<09:01, 882kB/s] .vector_cache/glove.6B.zip:  45%|████▍     | 385M/862M [02:42<08:30, 935kB/s].vector_cache/glove.6B.zip:  45%|████▍     | 385M/862M [02:42<06:38, 1.20MB/s].vector_cache/glove.6B.zip:  45%|████▍     | 386M/862M [02:42<05:16, 1.51MB/s].vector_cache/glove.6B.zip:  45%|████▍     | 386M/862M [02:42<04:39, 1.71MB/s].vector_cache/glove.6B.zip:  45%|████▍     | 386M/862M [02:42<03:57, 2.00MB/s].vector_cache/glove.6B.zip:  45%|████▍     | 387M/862M [02:42<03:32, 2.24MB/s].vector_cache/glove.6B.zip:  45%|████▍     | 387M/862M [02:42<03:10, 2.50MB/s].vector_cache/glove.6B.zip:  45%|████▍     | 387M/862M [02:43<02:58, 2.65MB/s].vector_cache/glove.6B.zip:  45%|████▍     | 388M/862M [02:43<02:45, 2.86MB/s].vector_cache/glove.6B.zip:  45%|████▍     | 388M/862M [02:43<03:57, 2.00MB/s].vector_cache/glove.6B.zip:  45%|████▌     | 388M/862M [02:43<03:16, 2.42MB/s].vector_cache/glove.6B.zip:  45%|████▌     | 389M/862M [02:43<03:20, 2.37MB/s].vector_cache/glove.6B.zip:  45%|████▌     | 389M/862M [02:43<03:13, 2.45MB/s].vector_cache/glove.6B.zip:  45%|████▌     | 389M/862M [02:44<09:47, 806kB/s] .vector_cache/glove.6B.zip:  45%|████▌     | 389M/862M [02:44<08:08, 967kB/s].vector_cache/glove.6B.zip:  45%|████▌     | 390M/862M [02:44<06:38, 1.19MB/s].vector_cache/glove.6B.zip:  45%|████▌     | 390M/862M [02:44<05:23, 1.46MB/s].vector_cache/glove.6B.zip:  45%|████▌     | 390M/862M [02:44<04:27, 1.77MB/s].vector_cache/glove.6B.zip:  45%|████▌     | 390M/862M [02:44<04:22, 1.80MB/s].vector_cache/glove.6B.zip:  45%|████▌     | 391M/862M [02:44<03:56, 2.00MB/s].vector_cache/glove.6B.zip:  45%|████▌     | 391M/862M [02:44<03:36, 2.17MB/s].vector_cache/glove.6B.zip:  45%|████▌     | 392M/862M [02:45<03:22, 2.33MB/s].vector_cache/glove.6B.zip:  45%|████▌     | 392M/862M [02:45<03:12, 2.45MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 392M/862M [02:45<02:51, 2.73MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 393M/862M [02:45<03:14, 2.42MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 393M/862M [02:45<03:05, 2.53MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 393M/862M [02:46<08:24, 929kB/s] .vector_cache/glove.6B.zip:  46%|████▌     | 393M/862M [02:46<07:06, 1.10MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 394M/862M [02:46<05:46, 1.35MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 394M/862M [02:46<04:51, 1.60MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 395M/862M [02:46<04:06, 1.90MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 395M/862M [02:46<03:40, 2.12MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 395M/862M [02:46<03:22, 2.31MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 396M/862M [02:47<03:09, 2.46MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 396M/862M [02:47<03:00, 2.58MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 397M/862M [02:47<02:55, 2.65MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 397M/862M [02:47<02:39, 2.93MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 397M/862M [02:47<03:01, 2.57MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 397M/862M [02:48<10:59, 705kB/s] .vector_cache/glove.6B.zip:  46%|████▌     | 398M/862M [02:48<08:54, 870kB/s].vector_cache/glove.6B.zip:  46%|████▌     | 398M/862M [02:48<07:04, 1.09MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 398M/862M [02:48<05:44, 1.35MB/s].vector_cache/glove.6B.zip:  46%|████▌     | 399M/862M [02:48<04:47, 1.61MB/s].vector_cache/glove.6B.zip:  46%|████▋     | 399M/862M [02:48<04:06, 1.88MB/s].vector_cache/glove.6B.zip:  46%|████▋     | 400M/862M [02:48<03:35, 2.15MB/s].vector_cache/glove.6B.zip:  46%|████▋     | 400M/862M [02:49<03:19, 2.32MB/s].vector_cache/glove.6B.zip:  46%|████▋     | 400M/862M [02:49<03:01, 2.54MB/s].vector_cache/glove.6B.zip:  46%|████▋     | 401M/862M [02:49<02:51, 2.68MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 401M/862M [02:49<02:44, 2.81MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 401M/862M [02:50<09:11, 835kB/s] .vector_cache/glove.6B.zip:  47%|████▋     | 402M/862M [02:50<08:26, 909kB/s].vector_cache/glove.6B.zip:  47%|████▋     | 402M/862M [02:50<06:44, 1.14MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 402M/862M [02:50<05:19, 1.44MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 403M/862M [02:50<04:26, 1.72MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 403M/862M [02:50<03:40, 2.09MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 403M/862M [02:50<03:31, 2.17MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 404M/862M [02:50<03:03, 2.50MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 404M/862M [02:50<03:11, 2.39MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 405M/862M [02:51<02:56, 2.60MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 405M/862M [02:51<02:38, 2.89MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 405M/862M [02:51<03:03, 2.49MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 405M/862M [02:51<06:44, 1.13MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 406M/862M [02:52<07:23, 1.03MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 406M/862M [02:52<06:09, 1.23MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 406M/862M [02:52<05:15, 1.45MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 407M/862M [02:52<04:36, 1.65MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 407M/862M [02:52<04:01, 1.89MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 407M/862M [02:52<03:41, 2.05MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 408M/862M [02:52<03:25, 2.21MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 408M/862M [02:53<03:14, 2.34MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 408M/862M [02:53<03:04, 2.45MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 409M/862M [02:53<02:57, 2.55MB/s].vector_cache/glove.6B.zip:  47%|████▋     | 409M/862M [02:53<02:50, 2.65MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 410M/862M [02:53<02:45, 2.74MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 410M/862M [02:53<21:13, 355kB/s] .vector_cache/glove.6B.zip:  48%|████▊     | 410M/862M [02:54<15:57, 473kB/s].vector_cache/glove.6B.zip:  48%|████▊     | 410M/862M [02:54<11:53, 633kB/s].vector_cache/glove.6B.zip:  48%|████▊     | 411M/862M [02:54<09:03, 831kB/s].vector_cache/glove.6B.zip:  48%|████▊     | 411M/862M [02:54<07:04, 1.06MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 412M/862M [02:54<05:39, 1.33MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 412M/862M [02:54<04:34, 1.64MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 412M/862M [02:54<04:00, 1.87MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 413M/862M [02:55<03:30, 2.14MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 413M/862M [02:55<03:03, 2.45MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 414M/862M [02:55<06:00, 1.24MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 414M/862M [02:56<06:04, 1.23MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 414M/862M [02:56<05:03, 1.47MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 415M/862M [02:56<04:14, 1.76MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 415M/862M [02:56<03:33, 2.09MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 416M/862M [02:56<03:01, 2.46MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 416M/862M [02:56<03:10, 2.34MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 416M/862M [02:56<02:53, 2.57MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 417M/862M [02:56<02:36, 2.85MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 417M/862M [02:57<02:23, 3.10MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 417M/862M [02:57<02:36, 2.84MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 418M/862M [02:57<02:29, 2.98MB/s].vector_cache/glove.6B.zip:  48%|████▊     | 418M/862M [02:57<1:25:08, 87.0kB/s].vector_cache/glove.6B.zip:  48%|████▊     | 418M/862M [02:58<1:01:19, 121kB/s] .vector_cache/glove.6B.zip:  49%|████▊     | 418M/862M [02:58<43:35, 170kB/s]  .vector_cache/glove.6B.zip:  49%|████▊     | 419M/862M [02:58<31:17, 236kB/s].vector_cache/glove.6B.zip:  49%|████▊     | 419M/862M [02:58<22:32, 327kB/s].vector_cache/glove.6B.zip:  49%|████▊     | 420M/862M [02:58<16:25, 449kB/s].vector_cache/glove.6B.zip:  49%|████▊     | 420M/862M [02:58<12:02, 611kB/s].vector_cache/glove.6B.zip:  49%|████▉     | 421M/862M [02:58<09:02, 814kB/s].vector_cache/glove.6B.zip:  49%|████▉     | 421M/862M [02:58<07:01, 1.05MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 421M/862M [02:58<05:37, 1.31MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 422M/862M [02:59<04:34, 1.61MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 422M/862M [02:59<03:53, 1.89MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 422M/862M [02:59<13:17, 552kB/s] .vector_cache/glove.6B.zip:  49%|████▉     | 422M/862M [02:59<10:48, 678kB/s].vector_cache/glove.6B.zip:  49%|████▉     | 422M/862M [03:00<08:24, 871kB/s].vector_cache/glove.6B.zip:  49%|████▉     | 423M/862M [03:00<06:40, 1.10MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 423M/862M [03:00<05:13, 1.40MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 424M/862M [03:00<04:12, 1.74MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 424M/862M [03:00<03:44, 1.95MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 424M/862M [03:00<03:13, 2.27MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 425M/862M [03:00<02:58, 2.45MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 425M/862M [03:00<02:40, 2.73MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 425M/862M [03:00<02:35, 2.81MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 426M/862M [03:01<02:23, 3.04MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 426M/862M [03:01<06:58, 1.04MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 426M/862M [03:01<06:37, 1.10MB/s].vector_cache/glove.6B.zip:  49%|████▉     | 427M/862M [03:02<05:19, 1.36MB/s].vector_cache/glove.6B.zip:  50%|████▉     | 427M/862M [03:02<04:22, 1.66MB/s].vector_cache/glove.6B.zip:  50%|████▉     | 428M/862M [03:02<03:41, 1.96MB/s].vector_cache/glove.6B.zip:  50%|████▉     | 428M/862M [03:02<03:08, 2.31MB/s].vector_cache/glove.6B.zip:  50%|████▉     | 429M/862M [03:02<02:49, 2.56MB/s].vector_cache/glove.6B.zip:  50%|████▉     | 429M/862M [03:02<02:26, 2.95MB/s].vector_cache/glove.6B.zip:  50%|████▉     | 429M/862M [03:02<02:35, 2.79MB/s].vector_cache/glove.6B.zip:  50%|████▉     | 430M/862M [03:02<02:21, 3.07MB/s].vector_cache/glove.6B.zip:  50%|████▉     | 430M/862M [03:03<02:20, 3.07MB/s].vector_cache/glove.6B.zip:  50%|████▉     | 430M/862M [03:03<08:19, 865kB/s] .vector_cache/glove.6B.zip:  50%|████▉     | 430M/862M [03:03<07:10, 1.00MB/s].vector_cache/glove.6B.zip:  50%|████▉     | 431M/862M [03:04<05:43, 1.25MB/s].vector_cache/glove.6B.zip:  50%|█████     | 431M/862M [03:04<04:30, 1.59MB/s].vector_cache/glove.6B.zip:  50%|█████     | 432M/862M [03:04<03:52, 1.85MB/s].vector_cache/glove.6B.zip:  50%|█████     | 432M/862M [03:04<03:34, 2.01MB/s].vector_cache/glove.6B.zip:  50%|█████     | 432M/862M [03:04<02:58, 2.41MB/s].vector_cache/glove.6B.zip:  50%|█████     | 433M/862M [03:04<02:43, 2.62MB/s].vector_cache/glove.6B.zip:  50%|█████     | 433M/862M [03:04<02:24, 2.97MB/s].vector_cache/glove.6B.zip:  50%|█████     | 433M/862M [03:04<02:20, 3.05MB/s].vector_cache/glove.6B.zip:  50%|█████     | 434M/862M [03:04<02:06, 3.37MB/s].vector_cache/glove.6B.zip:  50%|█████     | 434M/862M [03:04<02:03, 3.46MB/s].vector_cache/glove.6B.zip:  50%|█████     | 434M/862M [03:05<18:30, 385kB/s] .vector_cache/glove.6B.zip:  50%|█████     | 435M/862M [03:05<14:22, 496kB/s].vector_cache/glove.6B.zip:  50%|█████     | 435M/862M [03:06<10:38, 669kB/s].vector_cache/glove.6B.zip:  51%|█████     | 436M/862M [03:06<07:52, 902kB/s].vector_cache/glove.6B.zip:  51%|█████     | 436M/862M [03:06<06:00, 1.18MB/s].vector_cache/glove.6B.zip:  51%|█████     | 437M/862M [03:06<04:41, 1.51MB/s].vector_cache/glove.6B.zip:  51%|█████     | 437M/862M [03:06<03:38, 1.94MB/s].vector_cache/glove.6B.zip:  51%|█████     | 438M/862M [03:06<03:14, 2.18MB/s].vector_cache/glove.6B.zip:  51%|█████     | 438M/862M [03:06<02:37, 2.70MB/s].vector_cache/glove.6B.zip:  51%|█████     | 438M/862M [03:07<13:06, 539kB/s] .vector_cache/glove.6B.zip:  51%|█████     | 439M/862M [03:07<11:40, 605kB/s].vector_cache/glove.6B.zip:  51%|█████     | 439M/862M [03:07<08:48, 802kB/s].vector_cache/glove.6B.zip:  51%|█████     | 440M/862M [03:08<06:37, 1.06MB/s].vector_cache/glove.6B.zip:  51%|█████     | 440M/862M [03:08<05:02, 1.39MB/s].vector_cache/glove.6B.zip:  51%|█████     | 441M/862M [03:08<03:56, 1.78MB/s].vector_cache/glove.6B.zip:  51%|█████     | 442M/862M [03:08<03:03, 2.29MB/s].vector_cache/glove.6B.zip:  51%|█████▏    | 442M/862M [03:08<02:43, 2.58MB/s].vector_cache/glove.6B.zip:  51%|█████▏    | 443M/862M [03:09<05:53, 1.19MB/s].vector_cache/glove.6B.zip:  51%|█████▏    | 443M/862M [03:09<06:17, 1.11MB/s].vector_cache/glove.6B.zip:  51%|█████▏    | 443M/862M [03:09<04:57, 1.41MB/s].vector_cache/glove.6B.zip:  51%|█████▏    | 444M/862M [03:10<03:51, 1.80MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 445M/862M [03:10<03:03, 2.28MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 446M/862M [03:10<02:26, 2.85MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 446M/862M [03:10<02:02, 3.41MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 447M/862M [03:11<09:40, 716kB/s] .vector_cache/glove.6B.zip:  52%|█████▏    | 447M/862M [03:11<10:11, 679kB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 447M/862M [03:11<07:59, 866kB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 448M/862M [03:12<05:54, 1.17MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 449M/862M [03:12<04:25, 1.56MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 450M/862M [03:12<03:20, 2.06MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 450M/862M [03:12<02:39, 2.58MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 451M/862M [03:12<02:25, 2.82MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 451M/862M [03:13<14:10, 484kB/s] .vector_cache/glove.6B.zip:  52%|█████▏    | 451M/862M [03:13<14:46, 464kB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 451M/862M [03:13<11:58, 572kB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 451M/862M [03:14<10:04, 680kB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 451M/862M [03:14<08:27, 809kB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 452M/862M [03:14<07:43, 886kB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 452M/862M [03:14<06:45, 1.01MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 452M/862M [03:14<06:25, 1.06MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 452M/862M [03:14<05:47, 1.18MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 452M/862M [03:14<05:11, 1.31MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 452M/862M [03:14<05:59, 1.14MB/s].vector_cache/glove.6B.zip:  52%|█████▏    | 453M/862M [03:15<05:26, 1.26MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 453M/862M [03:15<04:56, 1.38MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 453M/862M [03:15<05:26, 1.26MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 453M/862M [03:15<04:53, 1.39MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 453M/862M [03:15<05:25, 1.26MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 453M/862M [03:15<04:53, 1.39MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 453M/862M [03:15<05:23, 1.26MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 454M/862M [03:15<04:54, 1.39MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 454M/862M [03:15<05:07, 1.33MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 454M/862M [03:15<04:46, 1.42MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 454M/862M [03:16<04:45, 1.43MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 454M/862M [03:16<04:28, 1.52MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 454M/862M [03:16<04:43, 1.44MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 455M/862M [03:16<04:23, 1.55MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 455M/862M [03:16<04:34, 1.48MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 455M/862M [03:16<04:19, 1.57MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 455M/862M [03:16<04:28, 1.52MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 455M/862M [03:16<04:10, 1.63MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 455M/862M [03:16<04:24, 1.54MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 456M/862M [03:16<04:05, 1.65MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 456M/862M [03:17<04:20, 1.56MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 456M/862M [03:17<04:02, 1.68MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 456M/862M [03:17<04:14, 1.60MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 456M/862M [03:17<03:58, 1.70MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 456M/862M [03:17<04:11, 1.62MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 457M/862M [03:17<03:54, 1.73MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 457M/862M [03:17<04:04, 1.66MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 457M/862M [03:17<03:48, 1.77MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 457M/862M [03:17<04:00, 1.68MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 457M/862M [03:17<03:43, 1.81MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 458M/862M [03:18<03:52, 1.74MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 458M/862M [03:18<03:33, 1.89MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 458M/862M [03:18<03:54, 1.72MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 458M/862M [03:18<03:32, 1.90MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 458M/862M [03:18<03:57, 1.70MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 459M/862M [03:18<03:48, 1.77MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 459M/862M [03:18<03:27, 1.95MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 459M/862M [03:18<03:43, 1.80MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 459M/862M [03:18<03:24, 1.97MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 459M/862M [03:19<03:40, 1.82MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 460M/862M [03:19<03:22, 1.98MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 460M/862M [03:19<03:39, 1.83MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 460M/862M [03:19<03:26, 1.95MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 460M/862M [03:19<03:30, 1.91MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 461M/862M [03:19<03:17, 2.03MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 461M/862M [03:19<03:22, 1.98MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 461M/862M [03:19<03:11, 2.10MB/s].vector_cache/glove.6B.zip:  53%|█████▎    | 461M/862M [03:19<03:19, 2.01MB/s].vector_cache/glove.6B.zip:  54%|█████▎    | 461M/862M [03:19<03:07, 2.13MB/s].vector_cache/glove.6B.zip:  54%|█████▎    | 462M/862M [03:20<03:13, 2.07MB/s].vector_cache/glove.6B.zip:  54%|█████▎    | 462M/862M [03:20<03:05, 2.16MB/s].vector_cache/glove.6B.zip:  54%|█████▎    | 462M/862M [03:20<03:08, 2.12MB/s].vector_cache/glove.6B.zip:  54%|█████▎    | 462M/862M [03:20<03:00, 2.22MB/s].vector_cache/glove.6B.zip:  54%|█████▎    | 463M/862M [03:20<03:08, 2.12MB/s].vector_cache/glove.6B.zip:  54%|█████▎    | 463M/862M [03:20<02:57, 2.25MB/s].vector_cache/glove.6B.zip:  54%|█████▎    | 463M/862M [03:20<03:03, 2.17MB/s].vector_cache/glove.6B.zip:  54%|█████▎    | 463M/862M [03:20<02:53, 2.30MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 463M/862M [03:20<03:03, 2.17MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 464M/862M [03:20<02:51, 2.32MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 464M/862M [03:21<03:00, 2.21MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 464M/862M [03:21<02:55, 2.27MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 464M/862M [03:21<03:30, 1.89MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 465M/862M [03:21<03:23, 1.95MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 465M/862M [03:21<03:50, 1.72MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 465M/862M [03:21<03:35, 1.84MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 465M/862M [03:21<03:53, 1.70MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 465M/862M [03:21<03:35, 1.84MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 465M/862M [03:21<03:45, 1.76MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 466M/862M [03:21<03:30, 1.89MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 466M/862M [03:22<03:40, 1.80MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 466M/862M [03:22<03:40, 1.80MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 466M/862M [03:22<03:33, 1.85MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 467M/862M [03:22<03:27, 1.91MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 467M/862M [03:22<03:11, 2.06MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 467M/862M [03:22<03:39, 1.80MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 467M/862M [03:22<03:26, 1.91MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 468M/862M [03:22<03:07, 2.11MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 468M/862M [03:23<03:57, 1.66MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 468M/862M [03:23<03:46, 1.74MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 468M/862M [03:23<03:33, 1.84MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 468M/862M [03:23<03:21, 1.95MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 469M/862M [03:23<03:03, 2.14MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 469M/862M [03:23<03:21, 1.95MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 469M/862M [03:23<04:06, 1.60MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 469M/862M [03:23<03:42, 1.77MB/s].vector_cache/glove.6B.zip:  54%|█████▍    | 470M/862M [03:24<03:25, 1.91MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 470M/862M [03:24<03:20, 1.95MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 470M/862M [03:24<03:25, 1.90MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 470M/862M [03:24<03:24, 1.91MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 471M/862M [03:24<03:12, 2.03MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 471M/862M [03:24<02:52, 2.26MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 471M/862M [03:24<03:25, 1.90MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 471M/862M [03:24<03:17, 1.98MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 472M/862M [03:24<03:09, 2.06MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 472M/862M [03:25<02:51, 2.28MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 472M/862M [03:25<03:06, 2.09MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 472M/862M [03:25<02:52, 2.26MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 473M/862M [03:25<02:59, 2.17MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 473M/862M [03:25<02:50, 2.29MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 473M/862M [03:25<02:53, 2.24MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 473M/862M [03:25<02:49, 2.30MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 474M/862M [03:25<02:50, 2.27MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 474M/862M [03:25<02:45, 2.34MB/s].vector_cache/glove.6B.zip:  55%|█████▍    | 474M/862M [03:25<02:49, 2.29MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 474M/862M [03:26<02:43, 2.38MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 475M/862M [03:26<02:46, 2.33MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 475M/862M [03:26<02:43, 2.36MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 475M/862M [03:26<02:43, 2.36MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 475M/862M [03:26<02:40, 2.41MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 476M/862M [03:26<02:40, 2.41MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 476M/862M [03:26<02:33, 2.51MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 476M/862M [03:26<02:40, 2.41MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 476M/862M [03:26<02:38, 2.43MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 477M/862M [03:27<02:38, 2.43MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 477M/862M [03:27<02:35, 2.48MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 477M/862M [03:27<02:29, 2.58MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 477M/862M [03:27<02:36, 2.46MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 478M/862M [03:27<02:42, 2.37MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 478M/862M [03:27<02:42, 2.37MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 478M/862M [03:27<02:42, 2.37MB/s].vector_cache/glove.6B.zip:  55%|█████▌    | 478M/862M [03:27<02:36, 2.45MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 479M/862M [03:27<02:32, 2.52MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 479M/862M [03:27<02:33, 2.49MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 479M/862M [03:28<02:28, 2.58MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 479M/862M [03:28<02:30, 2.54MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 480M/862M [03:28<02:26, 2.61MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 480M/862M [03:28<02:26, 2.61MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 480M/862M [03:28<02:24, 2.64MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 481M/862M [03:28<02:26, 2.61MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 481M/862M [03:28<02:18, 2.76MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 481M/862M [03:28<02:22, 2.68MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 482M/862M [03:28<02:15, 2.82MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 482M/862M [03:29<02:23, 2.65MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 482M/862M [03:29<02:14, 2.82MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 482M/862M [03:29<02:20, 2.71MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 483M/862M [03:29<02:12, 2.86MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 483M/862M [03:29<02:17, 2.75MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 483M/862M [03:29<02:11, 2.88MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 484M/862M [03:29<02:13, 2.84MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 484M/862M [03:29<02:07, 2.98MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 484M/862M [03:29<02:12, 2.86MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 485M/862M [03:29<02:04, 3.02MB/s].vector_cache/glove.6B.zip:  56%|█████▌    | 485M/862M [03:30<02:10, 2.89MB/s].vector_cache/glove.6B.zip:  56%|█████▋    | 485M/862M [03:30<02:03, 3.05MB/s].vector_cache/glove.6B.zip:  56%|█████▋    | 485M/862M [03:30<02:07, 2.96MB/s].vector_cache/glove.6B.zip:  56%|█████▋    | 486M/862M [03:30<02:02, 3.07MB/s].vector_cache/glove.6B.zip:  56%|█████▋    | 486M/862M [03:30<02:05, 3.00MB/s].vector_cache/glove.6B.zip:  56%|█████▋    | 486M/862M [03:30<06:52, 912kB/s] .vector_cache/glove.6B.zip:  56%|█████▋    | 487M/862M [03:30<05:21, 1.17MB/s].vector_cache/glove.6B.zip:  56%|█████▋    | 487M/862M [03:30<04:17, 1.46MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 488M/862M [03:31<03:32, 1.77MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 488M/862M [03:31<03:00, 2.08MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 489M/862M [03:31<02:36, 2.39MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 489M/862M [03:31<02:18, 2.70MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 490M/862M [03:31<02:05, 2.98MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 490M/862M [03:31<01:55, 3.22MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 490M/862M [03:32<13:04, 474kB/s] .vector_cache/glove.6B.zip:  57%|█████▋    | 490M/862M [03:32<11:32, 537kB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 491M/862M [03:32<08:47, 704kB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 491M/862M [03:33<06:35, 937kB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 492M/862M [03:33<05:19, 1.16MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 492M/862M [03:33<04:05, 1.51MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 493M/862M [03:33<03:21, 1.83MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 493M/862M [03:33<02:51, 2.15MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 493M/862M [03:33<02:35, 2.37MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 494M/862M [03:33<02:20, 2.63MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 494M/862M [03:33<02:09, 2.84MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 494M/862M [03:34<07:36, 806kB/s] .vector_cache/glove.6B.zip:  57%|█████▋    | 495M/862M [03:34<06:41, 915kB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 495M/862M [03:34<05:08, 1.19MB/s].vector_cache/glove.6B.zip:  57%|█████▋    | 496M/862M [03:35<04:09, 1.47MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 496M/862M [03:35<03:18, 1.84MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 496M/862M [03:35<02:46, 2.20MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 497M/862M [03:35<02:25, 2.52MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 497M/862M [03:35<02:07, 2.85MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 498M/862M [03:35<02:01, 3.00MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 498M/862M [03:35<01:58, 3.06MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 499M/862M [03:35<01:46, 3.40MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 499M/862M [03:36<3:01:11, 33.5kB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 499M/862M [03:36<2:07:58, 47.3kB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 499M/862M [03:36<1:29:54, 67.3kB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 500M/862M [03:36<1:03:15, 95.5kB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 500M/862M [03:37<44:41, 135kB/s]   .vector_cache/glove.6B.zip:  58%|█████▊    | 501M/862M [03:37<31:37, 191kB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 501M/862M [03:37<22:34, 267kB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 501M/862M [03:37<16:10, 372kB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 502M/862M [03:37<11:44, 512kB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 502M/862M [03:37<08:35, 698kB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 503M/862M [03:38<11:21, 528kB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 503M/862M [03:38<10:03, 596kB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 503M/862M [03:38<07:34, 790kB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 504M/862M [03:38<05:42, 1.05MB/s].vector_cache/glove.6B.zip:  58%|█████▊    | 504M/862M [03:39<04:23, 1.36MB/s].vector_cache/glove.6B.zip:  59%|█████▊    | 505M/862M [03:39<03:29, 1.70MB/s].vector_cache/glove.6B.zip:  59%|█████▊    | 505M/862M [03:39<02:48, 2.12MB/s].vector_cache/glove.6B.zip:  59%|█████▊    | 506M/862M [03:39<02:24, 2.47MB/s].vector_cache/glove.6B.zip:  59%|█████▊    | 506M/862M [03:39<02:01, 2.93MB/s].vector_cache/glove.6B.zip:  59%|█████▊    | 506M/862M [03:39<01:58, 3.00MB/s].vector_cache/glove.6B.zip:  59%|█████▉    | 507M/862M [03:40<07:24, 799kB/s] .vector_cache/glove.6B.zip:  59%|█████▉    | 507M/862M [03:40<07:17, 812kB/s].vector_cache/glove.6B.zip:  59%|█████▉    | 507M/862M [03:40<05:37, 1.05MB/s].vector_cache/glove.6B.zip:  59%|█████▉    | 508M/862M [03:40<04:15, 1.39MB/s].vector_cache/glove.6B.zip:  59%|█████▉    | 508M/862M [03:40<03:35, 1.64MB/s].vector_cache/glove.6B.zip:  59%|█████▉    | 509M/862M [03:41<02:50, 2.07MB/s].vector_cache/glove.6B.zip:  59%|█████▉    | 509M/862M [03:41<02:17, 2.57MB/s].vector_cache/glove.6B.zip:  59%|█████▉    | 510M/862M [03:41<02:13, 2.64MB/s].vector_cache/glove.6B.zip:  59%|█████▉    | 510M/862M [03:41<01:52, 3.12MB/s].vector_cache/glove.6B.zip:  59%|█████▉    | 511M/862M [03:41<01:41, 3.46MB/s].vector_cache/glove.6B.zip:  59%|█████▉    | 511M/862M [03:42<19:29, 300kB/s] .vector_cache/glove.6B.zip:  59%|█████▉    | 511M/862M [03:42<15:43, 372kB/s].vector_cache/glove.6B.zip:  59%|█████▉    | 511M/862M [03:42<11:29, 508kB/s].vector_cache/glove.6B.zip:  59%|█████▉    | 512M/862M [03:42<08:25, 693kB/s].vector_cache/glove.6B.zip:  59%|█████▉    | 513M/862M [03:43<06:15, 931kB/s].vector_cache/glove.6B.zip:  60%|█████▉    | 513M/862M [03:43<04:39, 1.25MB/s].vector_cache/glove.6B.zip:  60%|█████▉    | 514M/862M [03:43<03:46, 1.54MB/s].vector_cache/glove.6B.zip:  60%|█████▉    | 514M/862M [03:43<02:56, 1.97MB/s].vector_cache/glove.6B.zip:  60%|█████▉    | 515M/862M [03:43<02:39, 2.18MB/s].vector_cache/glove.6B.zip:  60%|█████▉    | 515M/862M [03:44<05:38, 1.03MB/s].vector_cache/glove.6B.zip:  60%|█████▉    | 515M/862M [03:44<05:59, 966kB/s] .vector_cache/glove.6B.zip:  60%|█████▉    | 516M/862M [03:44<04:46, 1.21MB/s].vector_cache/glove.6B.zip:  60%|█████▉    | 516M/862M [03:44<03:43, 1.55MB/s].vector_cache/glove.6B.zip:  60%|█████▉    | 517M/862M [03:44<02:56, 1.96MB/s].vector_cache/glove.6B.zip:  60%|█████▉    | 517M/862M [03:45<02:21, 2.43MB/s].vector_cache/glove.6B.zip:  60%|██████    | 518M/862M [03:45<02:08, 2.68MB/s].vector_cache/glove.6B.zip:  60%|██████    | 518M/862M [03:45<01:48, 3.18MB/s].vector_cache/glove.6B.zip:  60%|██████    | 519M/862M [03:45<01:44, 3.28MB/s].vector_cache/glove.6B.zip:  60%|██████    | 519M/862M [03:45<01:32, 3.70MB/s].vector_cache/glove.6B.zip:  60%|██████    | 519M/862M [03:46<1:06:17, 86.2kB/s].vector_cache/glove.6B.zip:  60%|██████    | 519M/862M [03:46<48:24, 118kB/s]   .vector_cache/glove.6B.zip:  60%|██████    | 520M/862M [03:46<34:26, 166kB/s].vector_cache/glove.6B.zip:  60%|██████    | 520M/862M [03:46<24:27, 233kB/s].vector_cache/glove.6B.zip:  60%|██████    | 521M/862M [03:46<17:27, 326kB/s].vector_cache/glove.6B.zip:  60%|██████    | 522M/862M [03:47<12:33, 452kB/s].vector_cache/glove.6B.zip:  61%|██████    | 522M/862M [03:47<09:06, 622kB/s].vector_cache/glove.6B.zip:  61%|██████    | 523M/862M [03:47<06:43, 842kB/s].vector_cache/glove.6B.zip:  61%|██████    | 523M/862M [03:48<08:15, 684kB/s].vector_cache/glove.6B.zip:  61%|██████    | 523M/862M [03:48<07:38, 739kB/s].vector_cache/glove.6B.zip:  61%|██████    | 524M/862M [03:48<05:54, 953kB/s].vector_cache/glove.6B.zip:  61%|██████    | 524M/862M [03:48<04:28, 1.26MB/s].vector_cache/glove.6B.zip:  61%|██████    | 525M/862M [03:48<03:30, 1.60MB/s].vector_cache/glove.6B.zip:  61%|██████    | 526M/862M [03:49<02:46, 2.02MB/s].vector_cache/glove.6B.zip:  61%|██████    | 526M/862M [03:49<02:17, 2.45MB/s].vector_cache/glove.6B.zip:  61%|██████    | 527M/862M [03:49<01:56, 2.88MB/s].vector_cache/glove.6B.zip:  61%|██████    | 527M/862M [03:50<05:50, 956kB/s] .vector_cache/glove.6B.zip:  61%|██████    | 528M/862M [03:50<05:55, 940kB/s].vector_cache/glove.6B.zip:  61%|██████    | 528M/862M [03:50<04:40, 1.19MB/s].vector_cache/glove.6B.zip:  61%|██████▏   | 529M/862M [03:50<03:37, 1.54MB/s].vector_cache/glove.6B.zip:  61%|██████▏   | 529M/862M [03:50<02:51, 1.94MB/s].vector_cache/glove.6B.zip:  61%|██████▏   | 530M/862M [03:51<02:19, 2.39MB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 531M/862M [03:51<01:56, 2.85MB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 531M/862M [03:51<01:37, 3.39MB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 532M/862M [03:52<14:13, 388kB/s] .vector_cache/glove.6B.zip:  62%|██████▏   | 532M/862M [03:52<11:40, 472kB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 532M/862M [03:52<08:35, 641kB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 533M/862M [03:52<06:18, 870kB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 534M/862M [03:52<04:45, 1.15MB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 534M/862M [03:52<03:33, 1.53MB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 535M/862M [03:53<02:42, 2.01MB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 536M/862M [03:53<02:17, 2.37MB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 536M/862M [03:54<13:09, 414kB/s] .vector_cache/glove.6B.zip:  62%|██████▏   | 536M/862M [03:54<10:42, 508kB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 536M/862M [03:54<07:56, 684kB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 537M/862M [03:54<05:49, 929kB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 538M/862M [03:54<04:22, 1.24MB/s].vector_cache/glove.6B.zip:  62%|██████▏   | 539M/862M [03:54<03:18, 1.63MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 540M/862M [03:55<02:32, 2.12MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 540M/862M [03:56<08:57, 600kB/s] .vector_cache/glove.6B.zip:  63%|██████▎   | 540M/862M [03:56<08:11, 656kB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 540M/862M [03:56<06:07, 875kB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 541M/862M [03:56<04:34, 1.17MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 541M/862M [03:56<03:35, 1.49MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 542M/862M [03:56<02:47, 1.91MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 542M/862M [03:56<03:12, 1.67MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 543M/862M [03:57<02:28, 2.16MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 543M/862M [03:57<02:05, 2.54MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 544M/862M [03:57<01:59, 2.67MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 544M/862M [03:58<05:59, 885kB/s] .vector_cache/glove.6B.zip:  63%|██████▎   | 544M/862M [03:58<06:23, 830kB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 544M/862M [03:58<05:03, 1.05MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 545M/862M [03:58<03:57, 1.34MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 545M/862M [03:58<03:10, 1.67MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 546M/862M [03:58<02:33, 2.06MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 546M/862M [03:59<02:10, 2.41MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 547M/862M [03:59<01:50, 2.84MB/s].vector_cache/glove.6B.zip:  63%|██████▎   | 547M/862M [03:59<01:47, 2.94MB/s].vector_cache/glove.6B.zip:  64%|██████▎   | 548M/862M [03:59<01:35, 3.29MB/s].vector_cache/glove.6B.zip:  64%|██████▎   | 548M/862M [04:00<06:10, 848kB/s] .vector_cache/glove.6B.zip:  64%|██████▎   | 548M/862M [04:00<05:10, 1.01MB/s].vector_cache/glove.6B.zip:  64%|██████▎   | 549M/862M [04:00<04:05, 1.28MB/s].vector_cache/glove.6B.zip:  64%|██████▎   | 549M/862M [04:00<03:10, 1.64MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 550M/862M [04:00<02:35, 2.01MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 550M/862M [04:00<02:06, 2.46MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 551M/862M [04:00<01:57, 2.66MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 551M/862M [04:01<01:41, 3.08MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 551M/862M [04:01<01:51, 2.79MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 552M/862M [04:01<01:48, 2.86MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 552M/862M [04:02<06:18, 820kB/s] .vector_cache/glove.6B.zip:  64%|██████▍   | 552M/862M [04:02<05:45, 897kB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 553M/862M [04:02<04:27, 1.16MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 553M/862M [04:02<03:36, 1.43MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 554M/862M [04:02<03:04, 1.68MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 554M/862M [04:02<02:32, 2.01MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 555M/862M [04:02<02:14, 2.28MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 555M/862M [04:03<02:02, 2.52MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 555M/862M [04:03<01:51, 2.74MB/s].vector_cache/glove.6B.zip:  64%|██████▍   | 556M/862M [04:03<01:38, 3.12MB/s].vector_cache/glove.6B.zip:  65%|██████▍   | 556M/862M [04:03<01:48, 2.82MB/s].vector_cache/glove.6B.zip:  65%|██████▍   | 556M/862M [04:04<07:26, 686kB/s] .vector_cache/glove.6B.zip:  65%|██████▍   | 556M/862M [04:04<06:24, 795kB/s].vector_cache/glove.6B.zip:  65%|██████▍   | 557M/862M [04:04<04:58, 1.02MB/s].vector_cache/glove.6B.zip:  65%|██████▍   | 557M/862M [04:04<03:55, 1.29MB/s].vector_cache/glove.6B.zip:  65%|██████▍   | 558M/862M [04:04<03:06, 1.63MB/s].vector_cache/glove.6B.zip:  65%|██████▍   | 558M/862M [04:04<02:31, 2.01MB/s].vector_cache/glove.6B.zip:  65%|██████▍   | 559M/862M [04:04<02:19, 2.18MB/s].vector_cache/glove.6B.zip:  65%|██████▍   | 559M/862M [04:04<01:58, 2.56MB/s].vector_cache/glove.6B.zip:  65%|██████▍   | 559M/862M [04:05<02:01, 2.49MB/s].vector_cache/glove.6B.zip:  65%|██████▍   | 560M/862M [04:05<01:50, 2.74MB/s].vector_cache/glove.6B.zip:  65%|██████▍   | 560M/862M [04:05<01:38, 3.07MB/s].vector_cache/glove.6B.zip:  65%|██████▍   | 560M/862M [04:06<07:33, 665kB/s] .vector_cache/glove.6B.zip:  65%|██████▌   | 561M/862M [04:06<06:25, 782kB/s].vector_cache/glove.6B.zip:  65%|██████▌   | 561M/862M [04:06<04:57, 1.01MB/s].vector_cache/glove.6B.zip:  65%|██████▌   | 562M/862M [04:06<03:53, 1.29MB/s].vector_cache/glove.6B.zip:  65%|██████▌   | 562M/862M [04:06<03:08, 1.59MB/s].vector_cache/glove.6B.zip:  65%|██████▌   | 562M/862M [04:06<02:34, 1.94MB/s].vector_cache/glove.6B.zip:  65%|██████▌   | 563M/862M [04:06<02:15, 2.21MB/s].vector_cache/glove.6B.zip:  65%|██████▌   | 563M/862M [04:07<01:56, 2.56MB/s].vector_cache/glove.6B.zip:  65%|██████▌   | 564M/862M [04:07<01:49, 2.73MB/s].vector_cache/glove.6B.zip:  65%|██████▌   | 564M/862M [04:07<01:38, 3.03MB/s].vector_cache/glove.6B.zip:  65%|██████▌   | 565M/862M [04:08<11:46, 421kB/s] .vector_cache/glove.6B.zip:  65%|██████▌   | 565M/862M [04:08<09:21, 530kB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 565M/862M [04:08<06:59, 707kB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 566M/862M [04:08<05:18, 930kB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 566M/862M [04:08<04:07, 1.19MB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 567M/862M [04:08<03:15, 1.51MB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 567M/862M [04:08<02:42, 1.82MB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 568M/862M [04:08<02:16, 2.16MB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 568M/862M [04:09<01:58, 2.47MB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 569M/862M [04:09<01:46, 2.75MB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 569M/862M [04:10<20:38, 237kB/s] .vector_cache/glove.6B.zip:  66%|██████▌   | 569M/862M [04:10<15:20, 319kB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 569M/862M [04:10<11:10, 437kB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 570M/862M [04:10<08:20, 584kB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 570M/862M [04:10<06:09, 791kB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 570M/862M [04:10<04:39, 1.04MB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 571M/862M [04:10<03:40, 1.32MB/s].vector_cache/glove.6B.zip:  66%|██████▌   | 571M/862M [04:10<02:57, 1.64MB/s].vector_cache/glove.6B.zip:  66%|██████▋   | 572M/862M [04:10<02:26, 1.99MB/s].vector_cache/glove.6B.zip:  66%|██████▋   | 572M/862M [04:10<02:04, 2.32MB/s].vector_cache/glove.6B.zip:  66%|██████▋   | 572M/862M [04:11<01:50, 2.63MB/s].vector_cache/glove.6B.zip:  66%|██████▋   | 573M/862M [04:11<01:38, 2.94MB/s].vector_cache/glove.6B.zip:  66%|██████▋   | 573M/862M [04:11<36:45, 131kB/s] .vector_cache/glove.6B.zip:  66%|██████▋   | 573M/862M [04:12<27:44, 174kB/s].vector_cache/glove.6B.zip:  66%|██████▋   | 573M/862M [04:12<19:52, 242kB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 574M/862M [04:12<14:15, 337kB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 574M/862M [04:12<10:19, 464kB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 575M/862M [04:12<07:29, 639kB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 575M/862M [04:12<05:45, 831kB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 576M/862M [04:12<04:17, 1.11MB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 576M/862M [04:12<03:31, 1.35MB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 576M/862M [04:13<02:45, 1.73MB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 577M/862M [04:13<02:22, 2.00MB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 577M/862M [04:13<07:31, 632kB/s] .vector_cache/glove.6B.zip:  67%|██████▋   | 577M/862M [04:14<06:12, 765kB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 578M/862M [04:14<04:44, 1.00MB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 578M/862M [04:14<03:37, 1.30MB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 579M/862M [04:14<02:52, 1.64MB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 579M/862M [04:14<02:21, 2.00MB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 580M/862M [04:14<01:59, 2.37MB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 580M/862M [04:14<01:53, 2.48MB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 581M/862M [04:15<01:37, 2.89MB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 581M/862M [04:15<06:25, 728kB/s] .vector_cache/glove.6B.zip:  67%|██████▋   | 581M/862M [04:16<07:05, 661kB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 581M/862M [04:16<05:34, 840kB/s].vector_cache/glove.6B.zip:  67%|██████▋   | 582M/862M [04:16<04:19, 1.08MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 582M/862M [04:16<03:26, 1.36MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 583M/862M [04:16<02:48, 1.66MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 583M/862M [04:16<02:21, 1.97MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 584M/862M [04:16<02:02, 2.28MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 584M/862M [04:17<01:48, 2.57MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 585M/862M [04:17<01:37, 2.83MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 585M/862M [04:17<03:42, 1.25MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 585M/862M [04:18<03:34, 1.29MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 586M/862M [04:18<02:50, 1.62MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 586M/862M [04:18<02:16, 2.02MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 587M/862M [04:18<02:08, 2.15MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 587M/862M [04:18<01:47, 2.56MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 588M/862M [04:18<01:32, 2.96MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 588M/862M [04:18<01:53, 2.42MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 588M/862M [04:18<01:44, 2.63MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 589M/862M [04:18<01:37, 2.79MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 589M/862M [04:19<01:41, 2.69MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 589M/862M [04:19<01:34, 2.88MB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 589M/862M [04:19<07:31, 604kB/s] .vector_cache/glove.6B.zip:  68%|██████▊   | 589M/862M [04:19<06:27, 704kB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 590M/862M [04:20<04:59, 910kB/s].vector_cache/glove.6B.zip:  68%|██████▊   | 590M/862M [04:20<03:53, 1.17MB/s].vector_cache/glove.6B.zip:  69%|██████▊   | 591M/862M [04:20<03:09, 1.43MB/s].vector_cache/glove.6B.zip:  69%|██████▊   | 591M/862M [04:20<02:38, 1.71MB/s].vector_cache/glove.6B.zip:  69%|██████▊   | 591M/862M [04:20<02:15, 1.99MB/s].vector_cache/glove.6B.zip:  69%|██████▊   | 592M/862M [04:20<02:00, 2.25MB/s].vector_cache/glove.6B.zip:  69%|██████▊   | 592M/862M [04:20<01:48, 2.48MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 593M/862M [04:21<01:40, 2.68MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 593M/862M [04:21<01:32, 2.90MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 593M/862M [04:21<05:06, 877kB/s] .vector_cache/glove.6B.zip:  69%|██████▉   | 594M/862M [04:21<04:32, 985kB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 594M/862M [04:22<03:33, 1.26MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 594M/862M [04:22<03:00, 1.49MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 595M/862M [04:22<02:25, 1.83MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 595M/862M [04:22<02:18, 1.93MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 595M/862M [04:22<01:57, 2.28MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 596M/862M [04:22<01:41, 2.63MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 596M/862M [04:22<01:42, 2.59MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 596M/862M [04:22<01:50, 2.41MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 597M/862M [04:22<01:49, 2.43MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 597M/862M [04:23<01:41, 2.62MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 597M/862M [04:23<01:45, 2.50MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 597M/862M [04:23<02:28, 1.79MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 598M/862M [04:23<05:59, 735kB/s] .vector_cache/glove.6B.zip:  69%|██████▉   | 598M/862M [04:23<05:14, 841kB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 598M/862M [04:24<04:23, 1.00MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 598M/862M [04:24<03:41, 1.19MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 598M/862M [04:24<03:16, 1.34MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 599M/862M [04:24<02:58, 1.48MB/s].vector_cache/glove.6B.zip:  69%|██████▉   | 599M/862M [04:24<02:45, 1.59MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 599M/862M [04:24<02:35, 1.69MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 599M/862M [04:24<02:20, 1.87MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 600M/862M [04:24<02:41, 1.62MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 600M/862M [04:25<02:26, 1.79MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 600M/862M [04:25<02:17, 1.91MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 600M/862M [04:25<02:20, 1.86MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 601M/862M [04:25<02:15, 1.93MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 601M/862M [04:25<02:15, 1.92MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 601M/862M [04:25<02:10, 2.00MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 601M/862M [04:25<02:22, 1.83MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 601M/862M [04:25<02:12, 1.97MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 602M/862M [04:25<02:07, 2.04MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 602M/862M [04:26<02:10, 2.00MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 602M/862M [04:26<02:06, 2.06MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 602M/862M [04:26<02:08, 2.03MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 602M/862M [04:26<02:03, 2.10MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 603M/862M [04:26<02:05, 2.06MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 603M/862M [04:26<01:59, 2.16MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 603M/862M [04:26<02:04, 2.08MB/s].vector_cache/glove.6B.zip:  70%|██████▉   | 603M/862M [04:26<01:59, 2.16MB/s].vector_cache/glove.6B.zip:  70%|███████   | 604M/862M [04:26<02:02, 2.10MB/s].vector_cache/glove.6B.zip:  70%|███████   | 604M/862M [04:26<01:56, 2.21MB/s].vector_cache/glove.6B.zip:  70%|███████   | 604M/862M [04:27<02:00, 2.15MB/s].vector_cache/glove.6B.zip:  70%|███████   | 604M/862M [04:27<01:56, 2.21MB/s].vector_cache/glove.6B.zip:  70%|███████   | 604M/862M [04:27<01:58, 2.18MB/s].vector_cache/glove.6B.zip:  70%|███████   | 605M/862M [04:27<01:53, 2.27MB/s].vector_cache/glove.6B.zip:  70%|███████   | 605M/862M [04:27<01:58, 2.17MB/s].vector_cache/glove.6B.zip:  70%|███████   | 605M/862M [04:27<02:14, 1.92MB/s].vector_cache/glove.6B.zip:  70%|███████   | 605M/862M [04:27<02:06, 2.03MB/s].vector_cache/glove.6B.zip:  70%|███████   | 606M/862M [04:27<02:00, 2.12MB/s].vector_cache/glove.6B.zip:  70%|███████   | 606M/862M [04:27<01:56, 2.19MB/s].vector_cache/glove.6B.zip:  70%|███████   | 606M/862M [04:28<01:53, 2.26MB/s].vector_cache/glove.6B.zip:  70%|███████   | 607M/862M [04:28<01:50, 2.31MB/s].vector_cache/glove.6B.zip:  70%|███████   | 607M/862M [04:28<01:47, 2.37MB/s].vector_cache/glove.6B.zip:  70%|███████   | 607M/862M [04:28<01:46, 2.38MB/s].vector_cache/glove.6B.zip:  70%|███████   | 608M/862M [04:28<01:45, 2.42MB/s].vector_cache/glove.6B.zip:  71%|███████   | 608M/862M [04:28<01:43, 2.45MB/s].vector_cache/glove.6B.zip:  71%|███████   | 608M/862M [04:28<01:43, 2.46MB/s].vector_cache/glove.6B.zip:  71%|███████   | 609M/862M [04:29<01:42, 2.48MB/s].vector_cache/glove.6B.zip:  71%|███████   | 609M/862M [04:29<02:17, 1.84MB/s].vector_cache/glove.6B.zip:  71%|███████   | 609M/862M [04:29<02:01, 2.08MB/s].vector_cache/glove.6B.zip:  71%|███████   | 610M/862M [04:29<01:54, 2.21MB/s].vector_cache/glove.6B.zip:  71%|███████   | 610M/862M [04:29<01:48, 2.32MB/s].vector_cache/glove.6B.zip:  71%|███████   | 610M/862M [04:29<01:38, 2.56MB/s].vector_cache/glove.6B.zip:  71%|███████   | 611M/862M [04:29<01:47, 2.35MB/s].vector_cache/glove.6B.zip:  71%|███████   | 611M/862M [04:29<01:39, 2.52MB/s].vector_cache/glove.6B.zip:  71%|███████   | 611M/862M [04:30<01:42, 2.46MB/s].vector_cache/glove.6B.zip:  71%|███████   | 611M/862M [04:30<01:37, 2.58MB/s].vector_cache/glove.6B.zip:  71%|███████   | 612M/862M [04:30<01:37, 2.58MB/s].vector_cache/glove.6B.zip:  71%|███████   | 612M/862M [04:30<01:33, 2.66MB/s].vector_cache/glove.6B.zip:  71%|███████   | 612M/862M [04:30<01:35, 2.63MB/s].vector_cache/glove.6B.zip:  71%|███████   | 613M/862M [04:30<01:39, 2.52MB/s].vector_cache/glove.6B.zip:  71%|███████   | 613M/862M [04:30<01:32, 2.71MB/s].vector_cache/glove.6B.zip:  71%|███████   | 613M/862M [04:30<01:35, 2.62MB/s].vector_cache/glove.6B.zip:  71%|███████   | 613M/862M [04:31<11:06, 373kB/s] .vector_cache/glove.6B.zip:  71%|███████   | 613M/862M [04:31<08:27, 490kB/s].vector_cache/glove.6B.zip:  71%|███████   | 614M/862M [04:31<06:21, 651kB/s].vector_cache/glove.6B.zip:  71%|███████   | 614M/862M [04:31<04:52, 849kB/s].vector_cache/glove.6B.zip:  71%|███████▏  | 615M/862M [04:31<03:49, 1.08MB/s].vector_cache/glove.6B.zip:  71%|███████▏  | 615M/862M [04:31<03:05, 1.33MB/s].vector_cache/glove.6B.zip:  71%|███████▏  | 615M/862M [04:32<02:35, 1.59MB/s].vector_cache/glove.6B.zip:  71%|███████▏  | 616M/862M [04:32<02:11, 1.87MB/s].vector_cache/glove.6B.zip:  71%|███████▏  | 616M/862M [04:32<01:59, 2.07MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 617M/862M [04:32<01:45, 2.33MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 617M/862M [04:32<01:37, 2.52MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 617M/862M [04:33<03:43, 1.10MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 618M/862M [04:33<03:13, 1.27MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 618M/862M [04:33<02:38, 1.54MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 618M/862M [04:33<02:12, 1.84MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 619M/862M [04:33<01:53, 2.15MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 619M/862M [04:33<01:36, 2.50MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 620M/862M [04:34<01:27, 2.77MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 620M/862M [04:34<01:15, 3.21MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 621M/862M [04:34<01:18, 3.06MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 621M/862M [04:34<01:08, 3.51MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 621M/862M [04:35<06:19, 635kB/s] .vector_cache/glove.6B.zip:  72%|███████▏  | 622M/862M [04:35<05:11, 773kB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 622M/862M [04:35<03:59, 1.00MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 623M/862M [04:35<03:04, 1.30MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 623M/862M [04:35<02:24, 1.66MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 624M/862M [04:35<01:55, 2.06MB/s].vector_cache/glove.6B.zip:  72%|███████▏  | 625M/862M [04:35<01:33, 2.53MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 625M/862M [04:36<01:20, 2.94MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 626M/862M [04:37<05:32, 712kB/s] .vector_cache/glove.6B.zip:  73%|███████▎  | 626M/862M [04:37<05:06, 772kB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 626M/862M [04:37<03:54, 1.01MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 627M/862M [04:37<02:55, 1.34MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 628M/862M [04:37<02:14, 1.74MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 628M/862M [04:37<01:47, 2.17MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 629M/862M [04:37<01:27, 2.67MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 629M/862M [04:38<01:24, 2.76MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 630M/862M [04:39<03:52, 1.00MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 630M/862M [04:39<04:11, 925kB/s] .vector_cache/glove.6B.zip:  73%|███████▎  | 630M/862M [04:39<03:13, 1.20MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 631M/862M [04:39<02:29, 1.54MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 631M/862M [04:39<01:56, 1.97MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 632M/862M [04:39<01:39, 2.33MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 632M/862M [04:39<01:20, 2.85MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 633M/862M [04:39<01:13, 3.11MB/s].vector_cache/glove.6B.zip:  73%|███████▎  | 633M/862M [04:40<01:02, 3.69MB/s].vector_cache/glove.6B.zip:  74%|███████▎  | 634M/862M [04:41<04:59, 762kB/s] .vector_cache/glove.6B.zip:  74%|███████▎  | 634M/862M [04:41<04:40, 815kB/s].vector_cache/glove.6B.zip:  74%|███████▎  | 634M/862M [04:41<03:35, 1.06MB/s].vector_cache/glove.6B.zip:  74%|███████▎  | 635M/862M [04:41<02:44, 1.38MB/s].vector_cache/glove.6B.zip:  74%|███████▎  | 636M/862M [04:41<02:07, 1.78MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 636M/862M [04:41<01:39, 2.26MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 637M/862M [04:41<01:19, 2.81MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 638M/862M [04:41<01:11, 3.15MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 638M/862M [04:43<05:08, 726kB/s] .vector_cache/glove.6B.zip:  74%|███████▍  | 638M/862M [04:43<04:37, 807kB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 639M/862M [04:43<03:29, 1.07MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 639M/862M [04:43<02:38, 1.41MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 640M/862M [04:43<01:59, 1.86MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 640M/862M [04:43<01:39, 2.22MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 641M/862M [04:43<01:18, 2.81MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 642M/862M [04:43<01:10, 3.13MB/s].vector_cache/glove.6B.zip:  74%|███████▍  | 642M/862M [04:45<04:06, 894kB/s] .vector_cache/glove.6B.zip:  74%|███████▍  | 642M/862M [04:45<05:08, 714kB/s].vector_cache/glove.6B.zip:  75%|███████▍  | 642M/862M [04:45<04:05, 895kB/s].vector_cache/glove.6B.zip:  75%|███████▍  | 643M/862M [04:45<03:03, 1.19MB/s].vector_cache/glove.6B.zip:  75%|███████▍  | 644M/862M [04:45<02:19, 1.57MB/s].vector_cache/glove.6B.zip:  75%|███████▍  | 645M/862M [04:45<01:47, 2.03MB/s].vector_cache/glove.6B.zip:  75%|███████▍  | 646M/862M [04:45<01:25, 2.53MB/s].vector_cache/glove.6B.zip:  75%|███████▍  | 646M/862M [04:46<02:55, 1.23MB/s].vector_cache/glove.6B.zip:  75%|███████▍  | 646M/862M [04:47<03:02, 1.18MB/s].vector_cache/glove.6B.zip:  75%|███████▌  | 647M/862M [04:47<02:20, 1.53MB/s].vector_cache/glove.6B.zip:  75%|███████▌  | 648M/862M [04:47<01:46, 2.01MB/s].vector_cache/glove.6B.zip:  75%|███████▌  | 648M/862M [04:47<01:33, 2.30MB/s].vector_cache/glove.6B.zip:  75%|███████▌  | 649M/862M [04:47<01:14, 2.85MB/s].vector_cache/glove.6B.zip:  75%|███████▌  | 650M/862M [04:47<01:03, 3.34MB/s].vector_cache/glove.6B.zip:  75%|███████▌  | 650M/862M [04:48<02:49, 1.25MB/s].vector_cache/glove.6B.zip:  75%|███████▌  | 650M/862M [04:49<03:56, 897kB/s] .vector_cache/glove.6B.zip:  75%|███████▌  | 651M/862M [04:49<03:12, 1.10MB/s].vector_cache/glove.6B.zip:  76%|███████▌  | 651M/862M [04:49<02:26, 1.44MB/s].vector_cache/glove.6B.zip:  76%|███████▌  | 652M/862M [04:49<01:52, 1.87MB/s].vector_cache/glove.6B.zip:  76%|███████▌  | 653M/862M [04:49<01:28, 2.36MB/s].vector_cache/glove.6B.zip:  76%|███████▌  | 654M/862M [04:49<01:10, 2.94MB/s].vector_cache/glove.6B.zip:  76%|███████▌  | 654M/862M [04:50<02:58, 1.16MB/s].vector_cache/glove.6B.zip:  76%|███████▌  | 655M/862M [04:51<03:02, 1.14MB/s].vector_cache/glove.6B.zip:  76%|███████▌  | 655M/862M [04:51<02:23, 1.44MB/s].vector_cache/glove.6B.zip:  76%|███████▌  | 656M/862M [04:51<01:49, 1.88MB/s].vector_cache/glove.6B.zip:  76%|███████▌  | 657M/862M [04:51<01:26, 2.37MB/s].vector_cache/glove.6B.zip:  76%|███████▋  | 657M/862M [04:51<01:10, 2.89MB/s].vector_cache/glove.6B.zip:  76%|███████▋  | 658M/862M [04:51<00:59, 3.43MB/s].vector_cache/glove.6B.zip:  76%|███████▋  | 659M/862M [04:52<05:33, 610kB/s] .vector_cache/glove.6B.zip:  76%|███████▋  | 659M/862M [04:53<05:46, 588kB/s].vector_cache/glove.6B.zip:  76%|███████▋  | 659M/862M [04:53<04:28, 757kB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 660M/862M [04:53<03:18, 1.02MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 660M/862M [04:53<02:28, 1.36MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 661M/862M [04:53<01:53, 1.77MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 662M/862M [04:53<01:29, 2.24MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 663M/862M [04:54<03:04, 1.08MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 663M/862M [04:54<03:01, 1.10MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 663M/862M [04:55<02:19, 1.42MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 664M/862M [04:55<01:46, 1.87MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 664M/862M [04:55<01:28, 2.24MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 665M/862M [04:55<01:10, 2.81MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 666M/862M [04:55<01:00, 3.26MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 666M/862M [04:55<00:51, 3.81MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 667M/862M [04:55<00:56, 3.45MB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 667M/862M [04:56<12:20, 264kB/s] .vector_cache/glove.6B.zip:  77%|███████▋  | 667M/862M [04:56<09:52, 330kB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 667M/862M [04:57<07:09, 454kB/s].vector_cache/glove.6B.zip:  77%|███████▋  | 668M/862M [04:57<05:11, 625kB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 668M/862M [04:57<03:51, 837kB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 669M/862M [04:57<02:52, 1.12MB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 669M/862M [04:57<02:14, 1.44MB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 670M/862M [04:57<01:43, 1.85MB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 670M/862M [04:57<01:26, 2.22MB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 671M/862M [04:57<01:10, 2.72MB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 671M/862M [04:58<09:14, 345kB/s] .vector_cache/glove.6B.zip:  78%|███████▊  | 671M/862M [04:58<07:31, 424kB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 672M/862M [04:59<05:29, 578kB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 672M/862M [04:59<04:00, 790kB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 673M/862M [04:59<02:59, 1.05MB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 673M/862M [04:59<02:14, 1.40MB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 674M/862M [04:59<01:45, 1.78MB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 674M/862M [04:59<01:23, 2.26MB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 675M/862M [04:59<01:09, 2.69MB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 675M/862M [05:00<04:37, 675kB/s] .vector_cache/glove.6B.zip:  78%|███████▊  | 675M/862M [05:00<04:09, 751kB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 676M/862M [05:01<03:07, 997kB/s].vector_cache/glove.6B.zip:  78%|███████▊  | 676M/862M [05:01<02:20, 1.32MB/s].vector_cache/glove.6B.zip:  79%|███████▊  | 677M/862M [05:01<01:49, 1.69MB/s].vector_cache/glove.6B.zip:  79%|███████▊  | 678M/862M [05:01<01:24, 2.19MB/s].vector_cache/glove.6B.zip:  79%|███████▊  | 679M/862M [05:01<01:06, 2.74MB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 679M/862M [05:01<00:58, 3.15MB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 679M/862M [05:02<31:39, 96.3kB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 679M/862M [05:02<22:59, 133kB/s] .vector_cache/glove.6B.zip:  79%|███████▉  | 680M/862M [05:02<16:15, 187kB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 681M/862M [05:03<11:27, 264kB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 681M/862M [05:03<08:13, 367kB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 682M/862M [05:03<05:51, 513kB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 682M/862M [05:03<04:15, 703kB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 683M/862M [05:03<03:06, 961kB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 683M/862M [05:04<04:37, 645kB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 683M/862M [05:04<04:43, 631kB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 684M/862M [05:04<03:41, 804kB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 684M/862M [05:05<02:44, 1.08MB/s].vector_cache/glove.6B.zip:  79%|███████▉  | 685M/862M [05:05<02:01, 1.45MB/s].vector_cache/glove.6B.zip:  80%|███████▉  | 686M/862M [05:05<01:39, 1.78MB/s].vector_cache/glove.6B.zip:  80%|███████▉  | 686M/862M [05:05<01:16, 2.29MB/s].vector_cache/glove.6B.zip:  80%|███████▉  | 687M/862M [05:05<01:00, 2.92MB/s].vector_cache/glove.6B.zip:  80%|███████▉  | 687M/862M [05:06<04:05, 713kB/s] .vector_cache/glove.6B.zip:  80%|███████▉  | 688M/862M [05:06<03:39, 796kB/s].vector_cache/glove.6B.zip:  80%|███████▉  | 688M/862M [05:06<02:46, 1.04MB/s].vector_cache/glove.6B.zip:  80%|███████▉  | 689M/862M [05:07<02:04, 1.39MB/s].vector_cache/glove.6B.zip:  80%|███████▉  | 690M/862M [05:07<01:35, 1.81MB/s].vector_cache/glove.6B.zip:  80%|████████  | 691M/862M [05:07<01:15, 2.27MB/s].vector_cache/glove.6B.zip:  80%|████████  | 691M/862M [05:07<01:00, 2.83MB/s].vector_cache/glove.6B.zip:  80%|████████  | 692M/862M [05:08<05:45, 494kB/s] .vector_cache/glove.6B.zip:  80%|████████  | 692M/862M [05:08<05:36, 507kB/s].vector_cache/glove.6B.zip:  80%|████████  | 692M/862M [05:08<04:17, 661kB/s].vector_cache/glove.6B.zip:  80%|████████  | 693M/862M [05:09<03:08, 897kB/s].vector_cache/glove.6B.zip:  80%|████████  | 694M/862M [05:09<02:19, 1.21MB/s].vector_cache/glove.6B.zip:  81%|████████  | 694M/862M [05:09<01:44, 1.60MB/s].vector_cache/glove.6B.zip:  81%|████████  | 695M/862M [05:09<01:19, 2.09MB/s].vector_cache/glove.6B.zip:  81%|████████  | 695M/862M [05:09<01:15, 2.21MB/s].vector_cache/glove.6B.zip:  81%|████████  | 696M/862M [05:10<03:49, 725kB/s] .vector_cache/glove.6B.zip:  81%|████████  | 696M/862M [05:10<04:57, 559kB/s].vector_cache/glove.6B.zip:  81%|████████  | 696M/862M [05:10<04:01, 689kB/s].vector_cache/glove.6B.zip:  81%|████████  | 697M/862M [05:11<02:59, 921kB/s].vector_cache/glove.6B.zip:  81%|████████  | 697M/862M [05:11<02:14, 1.23MB/s].vector_cache/glove.6B.zip:  81%|████████  | 698M/862M [05:11<01:41, 1.62MB/s].vector_cache/glove.6B.zip:  81%|████████  | 698M/862M [05:11<01:25, 1.92MB/s].vector_cache/glove.6B.zip:  81%|████████  | 699M/862M [05:11<01:08, 2.39MB/s].vector_cache/glove.6B.zip:  81%|████████  | 699M/862M [05:11<00:59, 2.75MB/s].vector_cache/glove.6B.zip:  81%|████████  | 700M/862M [05:11<00:49, 3.27MB/s].vector_cache/glove.6B.zip:  81%|████████  | 700M/862M [05:12<03:21, 806kB/s] .vector_cache/glove.6B.zip:  81%|████████  | 700M/862M [05:12<03:10, 848kB/s].vector_cache/glove.6B.zip:  81%|████████▏ | 701M/862M [05:12<02:27, 1.09MB/s].vector_cache/glove.6B.zip:  81%|████████▏ | 701M/862M [05:13<01:52, 1.43MB/s].vector_cache/glove.6B.zip:  81%|████████▏ | 702M/862M [05:13<01:27, 1.83MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 703M/862M [05:13<01:09, 2.30MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 704M/862M [05:13<00:56, 2.80MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 704M/862M [05:14<02:03, 1.28MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 704M/862M [05:14<03:04, 855kB/s] .vector_cache/glove.6B.zip:  82%|████████▏ | 704M/862M [05:14<02:32, 1.03MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 705M/862M [05:15<01:56, 1.35MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 706M/862M [05:15<01:34, 1.65MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 706M/862M [05:15<01:13, 2.11MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 707M/862M [05:15<01:01, 2.51MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 707M/862M [05:15<00:56, 2.77MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 708M/862M [05:15<00:49, 3.15MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 708M/862M [05:15<00:46, 3.29MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 708M/862M [05:16<02:38, 973kB/s] .vector_cache/glove.6B.zip:  82%|████████▏ | 708M/862M [05:16<02:48, 911kB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 709M/862M [05:16<02:13, 1.15MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 709M/862M [05:17<01:43, 1.48MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 710M/862M [05:17<01:21, 1.88MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 711M/862M [05:17<01:06, 2.27MB/s].vector_cache/glove.6B.zip:  82%|████████▏ | 711M/862M [05:17<00:56, 2.66MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 712M/862M [05:17<00:49, 3.03MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 712M/862M [05:18<01:52, 1.33MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 713M/862M [05:18<02:11, 1.14MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 713M/862M [05:18<01:43, 1.44MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 714M/862M [05:18<01:22, 1.81MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 714M/862M [05:19<01:05, 2.27MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 715M/862M [05:19<00:57, 2.57MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 715M/862M [05:19<00:47, 3.08MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 715M/862M [05:19<00:45, 3.25MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 716M/862M [05:19<00:38, 3.76MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 716M/862M [05:19<00:39, 3.69MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 717M/862M [05:20<07:05, 342kB/s] .vector_cache/glove.6B.zip:  83%|████████▎ | 717M/862M [05:20<05:46, 420kB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 717M/862M [05:20<04:15, 568kB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 718M/862M [05:20<03:07, 770kB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 718M/862M [05:21<02:19, 1.03MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 719M/862M [05:21<01:45, 1.36MB/s].vector_cache/glove.6B.zip:  83%|████████▎ | 720M/862M [05:21<01:20, 1.77MB/s].vector_cache/glove.6B.zip:  84%|████████▎ | 720M/862M [05:21<01:07, 2.10MB/s].vector_cache/glove.6B.zip:  84%|████████▎ | 721M/862M [05:21<00:54, 2.62MB/s].vector_cache/glove.6B.zip:  84%|████████▎ | 721M/862M [05:22<11:26, 206kB/s] .vector_cache/glove.6B.zip:  84%|████████▎ | 721M/862M [05:22<08:47, 268kB/s].vector_cache/glove.6B.zip:  84%|████████▎ | 721M/862M [05:22<06:20, 370kB/s].vector_cache/glove.6B.zip:  84%|████████▎ | 722M/862M [05:22<04:33, 513kB/s].vector_cache/glove.6B.zip:  84%|████████▍ | 723M/862M [05:23<03:20, 698kB/s].vector_cache/glove.6B.zip:  84%|████████▍ | 723M/862M [05:23<02:28, 939kB/s].vector_cache/glove.6B.zip:  84%|████████▍ | 724M/862M [05:23<01:51, 1.25MB/s].vector_cache/glove.6B.zip:  84%|████████▍ | 724M/862M [05:23<01:26, 1.60MB/s].vector_cache/glove.6B.zip:  84%|████████▍ | 725M/862M [05:24<03:09, 725kB/s] .vector_cache/glove.6B.zip:  84%|████████▍ | 725M/862M [05:24<02:57, 772kB/s].vector_cache/glove.6B.zip:  84%|████████▍ | 725M/862M [05:24<02:16, 999kB/s].vector_cache/glove.6B.zip:  84%|████████▍ | 726M/862M [05:24<01:44, 1.31MB/s].vector_cache/glove.6B.zip:  84%|████████▍ | 727M/862M [05:25<01:21, 1.67MB/s].vector_cache/glove.6B.zip:  84%|████████▍ | 727M/862M [05:25<01:04, 2.08MB/s].vector_cache/glove.6B.zip:  84%|████████▍ | 728M/862M [05:25<00:52, 2.55MB/s].vector_cache/glove.6B.zip:  85%|████████▍ | 729M/862M [05:25<00:45, 2.97MB/s].vector_cache/glove.6B.zip:  85%|████████▍ | 729M/862M [05:26<02:34, 863kB/s] .vector_cache/glove.6B.zip:  85%|████████▍ | 729M/862M [05:26<02:35, 859kB/s].vector_cache/glove.6B.zip:  85%|████████▍ | 729M/862M [05:26<02:00, 1.10MB/s].vector_cache/glove.6B.zip:  85%|████████▍ | 730M/862M [05:26<01:32, 1.43MB/s].vector_cache/glove.6B.zip:  85%|████████▍ | 731M/862M [05:26<01:11, 1.83MB/s].vector_cache/glove.6B.zip:  85%|████████▍ | 731M/862M [05:27<00:58, 2.24MB/s].vector_cache/glove.6B.zip:  85%|████████▍ | 732M/862M [05:27<00:48, 2.68MB/s].vector_cache/glove.6B.zip:  85%|████████▍ | 733M/862M [05:27<00:41, 3.09MB/s].vector_cache/glove.6B.zip:  85%|████████▌ | 733M/862M [05:28<02:31, 854kB/s] .vector_cache/glove.6B.zip:  85%|████████▌ | 733M/862M [05:28<02:28, 869kB/s].vector_cache/glove.6B.zip:  85%|████████▌ | 734M/862M [05:28<01:55, 1.11MB/s].vector_cache/glove.6B.zip:  85%|████████▌ | 734M/862M [05:28<01:28, 1.45MB/s].vector_cache/glove.6B.zip:  85%|████████▌ | 735M/862M [05:28<01:08, 1.87MB/s].vector_cache/glove.6B.zip:  85%|████████▌ | 736M/862M [05:29<00:55, 2.30MB/s].vector_cache/glove.6B.zip:  85%|████████▌ | 736M/862M [05:29<00:46, 2.73MB/s].vector_cache/glove.6B.zip:  85%|████████▌ | 737M/862M [05:29<00:37, 3.31MB/s].vector_cache/glove.6B.zip:  85%|████████▌ | 737M/862M [05:30<03:05, 675kB/s] .vector_cache/glove.6B.zip:  86%|████████▌ | 737M/862M [05:30<02:48, 742kB/s].vector_cache/glove.6B.zip:  86%|████████▌ | 738M/862M [05:30<02:09, 963kB/s].vector_cache/glove.6B.zip:  86%|████████▌ | 738M/862M [05:30<01:37, 1.27MB/s].vector_cache/glove.6B.zip:  86%|████████▌ | 739M/862M [05:30<01:14, 1.66MB/s].vector_cache/glove.6B.zip:  86%|████████▌ | 740M/862M [05:31<00:58, 2.09MB/s].vector_cache/glove.6B.zip:  86%|████████▌ | 740M/862M [05:31<00:47, 2.54MB/s].vector_cache/glove.6B.zip:  86%|████████▌ | 741M/862M [05:31<00:41, 2.94MB/s].vector_cache/glove.6B.zip:  86%|████████▌ | 741M/862M [05:32<06:44, 299kB/s] .vector_cache/glove.6B.zip:  86%|████████▌ | 741M/862M [05:32<05:20, 377kB/s].vector_cache/glove.6B.zip:  86%|████████▌ | 742M/862M [05:32<03:53, 516kB/s].vector_cache/glove.6B.zip:  86%|████████▌ | 743M/862M [05:32<02:50, 703kB/s].vector_cache/glove.6B.zip:  86%|████████▌ | 743M/862M [05:32<02:04, 952kB/s].vector_cache/glove.6B.zip:  86%|████████▋ | 744M/862M [05:33<01:33, 1.27MB/s].vector_cache/glove.6B.zip:  86%|████████▋ | 745M/862M [05:33<01:10, 1.66MB/s].vector_cache/glove.6B.zip:  86%|████████▋ | 745M/862M [05:34<01:55, 1.01MB/s].vector_cache/glove.6B.zip:  86%|████████▋ | 746M/862M [05:34<01:54, 1.01MB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 746M/862M [05:34<01:29, 1.29MB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 747M/862M [05:34<01:08, 1.68MB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 748M/862M [05:34<00:53, 2.14MB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 748M/862M [05:35<00:42, 2.65MB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 749M/862M [05:35<00:35, 3.20MB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 750M/862M [05:36<02:40, 701kB/s] .vector_cache/glove.6B.zip:  87%|████████▋ | 750M/862M [05:36<02:54, 645kB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 750M/862M [05:36<02:16, 823kB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 751M/862M [05:36<01:40, 1.11MB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 751M/862M [05:36<01:15, 1.47MB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 752M/862M [05:36<00:56, 1.95MB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 753M/862M [05:37<00:45, 2.40MB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 754M/862M [05:37<00:36, 3.01MB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 754M/862M [05:38<04:39, 389kB/s] .vector_cache/glove.6B.zip:  87%|████████▋ | 754M/862M [05:38<04:04, 443kB/s].vector_cache/glove.6B.zip:  87%|████████▋ | 754M/862M [05:38<03:03, 588kB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 755M/862M [05:38<02:12, 812kB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 756M/862M [05:38<01:35, 1.11MB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 757M/862M [05:38<01:09, 1.51MB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 757M/862M [05:39<00:54, 1.91MB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 758M/862M [05:40<02:28, 703kB/s] .vector_cache/glove.6B.zip:  88%|████████▊ | 758M/862M [05:40<02:26, 709kB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 758M/862M [05:40<01:53, 918kB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 759M/862M [05:40<01:22, 1.24MB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 760M/862M [05:40<01:01, 1.67MB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 762M/862M [05:40<00:45, 2.20MB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 762M/862M [05:42<02:05, 800kB/s] .vector_cache/glove.6B.zip:  88%|████████▊ | 762M/862M [05:42<02:03, 814kB/s].vector_cache/glove.6B.zip:  88%|████████▊ | 763M/862M [05:42<01:34, 1.05MB/s].vector_cache/glove.6B.zip:  89%|████████▊ | 764M/862M [05:42<01:09, 1.41MB/s].vector_cache/glove.6B.zip:  89%|████████▊ | 765M/862M [05:42<00:51, 1.89MB/s].vector_cache/glove.6B.zip:  89%|████████▉ | 766M/862M [05:42<00:38, 2.49MB/s].vector_cache/glove.6B.zip:  89%|████████▉ | 766M/862M [05:44<09:56, 161kB/s] .vector_cache/glove.6B.zip:  89%|████████▉ | 766M/862M [05:44<07:28, 214kB/s].vector_cache/glove.6B.zip:  89%|████████▉ | 767M/862M [05:44<05:20, 298kB/s].vector_cache/glove.6B.zip:  89%|████████▉ | 768M/862M [05:44<03:44, 419kB/s].vector_cache/glove.6B.zip:  89%|████████▉ | 769M/862M [05:44<02:37, 589kB/s].vector_cache/glove.6B.zip:  89%|████████▉ | 770M/862M [05:46<02:27, 623kB/s].vector_cache/glove.6B.zip:  89%|████████▉ | 770M/862M [05:46<02:09, 706kB/s].vector_cache/glove.6B.zip:  89%|████████▉ | 771M/862M [05:46<01:36, 948kB/s].vector_cache/glove.6B.zip:  90%|████████▉ | 772M/862M [05:46<01:08, 1.31MB/s].vector_cache/glove.6B.zip:  90%|████████▉ | 773M/862M [05:46<00:51, 1.74MB/s].vector_cache/glove.6B.zip:  90%|████████▉ | 774M/862M [05:46<00:37, 2.35MB/s].vector_cache/glove.6B.zip:  90%|████████▉ | 774M/862M [05:48<02:49, 518kB/s] .vector_cache/glove.6B.zip:  90%|████████▉ | 774M/862M [05:48<02:46, 527kB/s].vector_cache/glove.6B.zip:  90%|████████▉ | 775M/862M [05:48<02:06, 691kB/s].vector_cache/glove.6B.zip:  90%|████████▉ | 776M/862M [05:48<01:30, 959kB/s].vector_cache/glove.6B.zip:  90%|█████████ | 777M/862M [05:48<01:05, 1.31MB/s].vector_cache/glove.6B.zip:  90%|█████████ | 778M/862M [05:48<00:46, 1.79MB/s].vector_cache/glove.6B.zip:  90%|█████████ | 779M/862M [05:50<01:42, 815kB/s] .vector_cache/glove.6B.zip:  90%|█████████ | 779M/862M [05:50<01:31, 912kB/s].vector_cache/glove.6B.zip:  90%|█████████ | 779M/862M [05:50<01:08, 1.22MB/s].vector_cache/glove.6B.zip:  91%|█████████ | 781M/862M [05:50<00:49, 1.66MB/s].vector_cache/glove.6B.zip:  91%|█████████ | 783M/862M [05:50<00:35, 2.27MB/s].vector_cache/glove.6B.zip:  91%|█████████ | 783M/862M [05:52<04:01, 330kB/s] .vector_cache/glove.6B.zip:  91%|█████████ | 783M/862M [05:52<03:24, 388kB/s].vector_cache/glove.6B.zip:  91%|█████████ | 783M/862M [05:52<02:31, 522kB/s].vector_cache/glove.6B.zip:  91%|█████████ | 784M/862M [05:52<01:46, 730kB/s].vector_cache/glove.6B.zip:  91%|█████████ | 786M/862M [05:52<01:14, 1.02MB/s].vector_cache/glove.6B.zip:  91%|█████████▏| 787M/862M [05:54<01:27, 857kB/s] .vector_cache/glove.6B.zip:  91%|█████████▏| 787M/862M [05:54<01:30, 832kB/s].vector_cache/glove.6B.zip:  91%|█████████▏| 787M/862M [05:54<01:10, 1.06MB/s].vector_cache/glove.6B.zip:  91%|█████████▏| 789M/862M [05:54<00:50, 1.46MB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 790M/862M [05:54<00:36, 1.97MB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 791M/862M [05:56<00:51, 1.38MB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 791M/862M [05:56<01:01, 1.16MB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 792M/862M [05:56<00:48, 1.46MB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 793M/862M [05:56<00:35, 1.97MB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 794M/862M [05:56<00:25, 2.66MB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 795M/862M [05:58<00:47, 1.40MB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 795M/862M [05:58<00:55, 1.20MB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 796M/862M [05:58<00:44, 1.51MB/s].vector_cache/glove.6B.zip:  92%|█████████▏| 797M/862M [05:58<00:31, 2.05MB/s].vector_cache/glove.6B.zip:  93%|█████████▎| 799M/862M [06:00<00:37, 1.68MB/s].vector_cache/glove.6B.zip:  93%|█████████▎| 799M/862M [06:00<00:45, 1.38MB/s].vector_cache/glove.6B.zip:  93%|█████████▎| 800M/862M [06:00<00:35, 1.74MB/s].vector_cache/glove.6B.zip:  93%|█████████▎| 801M/862M [06:00<00:25, 2.36MB/s].vector_cache/glove.6B.zip:  93%|█████████▎| 803M/862M [06:00<00:18, 3.15MB/s].vector_cache/glove.6B.zip:  93%|█████████▎| 803M/862M [06:01<00:56, 1.04MB/s].vector_cache/glove.6B.zip:  93%|█████████▎| 804M/862M [06:02<01:01, 948kB/s] .vector_cache/glove.6B.zip:  93%|█████████▎| 804M/862M [06:02<00:47, 1.22MB/s].vector_cache/glove.6B.zip:  93%|█████████▎| 805M/862M [06:02<00:34, 1.66MB/s].vector_cache/glove.6B.zip:  94%|█████████▎| 807M/862M [06:02<00:24, 2.29MB/s].vector_cache/glove.6B.zip:  94%|█████████▎| 808M/862M [06:03<00:56, 960kB/s] .vector_cache/glove.6B.zip:  94%|█████████▎| 808M/862M [06:04<00:56, 963kB/s].vector_cache/glove.6B.zip:  94%|█████████▎| 808M/862M [06:04<00:43, 1.25MB/s].vector_cache/glove.6B.zip:  94%|█████████▍| 810M/862M [06:04<00:30, 1.72MB/s].vector_cache/glove.6B.zip:  94%|█████████▍| 812M/862M [06:05<00:35, 1.43MB/s].vector_cache/glove.6B.zip:  94%|█████████▍| 812M/862M [06:06<00:37, 1.36MB/s].vector_cache/glove.6B.zip:  94%|█████████▍| 813M/862M [06:06<00:28, 1.75MB/s].vector_cache/glove.6B.zip:  94%|█████████▍| 814M/862M [06:06<00:20, 2.39MB/s].vector_cache/glove.6B.zip:  95%|█████████▍| 816M/862M [06:07<00:26, 1.77MB/s].vector_cache/glove.6B.zip:  95%|█████████▍| 816M/862M [06:08<00:30, 1.52MB/s].vector_cache/glove.6B.zip:  95%|█████████▍| 817M/862M [06:08<00:23, 1.93MB/s].vector_cache/glove.6B.zip:  95%|█████████▍| 818M/862M [06:08<00:16, 2.61MB/s].vector_cache/glove.6B.zip:  95%|█████████▌| 820M/862M [06:09<00:21, 1.91MB/s].vector_cache/glove.6B.zip:  95%|█████████▌| 820M/862M [06:10<00:24, 1.72MB/s].vector_cache/glove.6B.zip:  95%|█████████▌| 821M/862M [06:10<00:22, 1.86MB/s].vector_cache/glove.6B.zip:  95%|█████████▌| 822M/862M [06:10<00:16, 2.46MB/s].vector_cache/glove.6B.zip:  95%|█████████▌| 823M/862M [06:10<00:13, 2.99MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 823M/862M [06:10<00:10, 3.53MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 824M/862M [06:11<00:25, 1.49MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 824M/862M [06:12<00:38, 977kB/s] .vector_cache/glove.6B.zip:  96%|█████████▌| 825M/862M [06:12<00:31, 1.18MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 825M/862M [06:12<00:23, 1.58MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 826M/862M [06:12<00:17, 2.08MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 827M/862M [06:12<00:13, 2.53MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 828M/862M [06:12<00:10, 3.22MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 828M/862M [06:12<00:09, 3.62MB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 828M/862M [06:13<01:23, 406kB/s] .vector_cache/glove.6B.zip:  96%|█████████▌| 828M/862M [06:14<01:13, 459kB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 829M/862M [06:14<00:54, 608kB/s].vector_cache/glove.6B.zip:  96%|█████████▌| 829M/862M [06:14<00:40, 803kB/s].vector_cache/glove.6B.zip:  96%|█████████▋| 830M/862M [06:14<00:28, 1.11MB/s].vector_cache/glove.6B.zip:  96%|█████████▋| 831M/862M [06:14<00:21, 1.47MB/s].vector_cache/glove.6B.zip:  96%|█████████▋| 831M/862M [06:14<00:17, 1.78MB/s].vector_cache/glove.6B.zip:  96%|█████████▋| 832M/862M [06:14<00:13, 2.27MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 832M/862M [06:14<00:11, 2.57MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 833M/862M [06:15<00:55, 538kB/s] .vector_cache/glove.6B.zip:  97%|█████████▋| 833M/862M [06:15<00:47, 621kB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 833M/862M [06:16<00:35, 825kB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 834M/862M [06:16<00:25, 1.10MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 835M/862M [06:16<00:19, 1.45MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 835M/862M [06:16<00:14, 1.88MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 836M/862M [06:16<00:11, 2.38MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 836M/862M [06:16<00:09, 2.68MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 837M/862M [06:17<00:36, 700kB/s] .vector_cache/glove.6B.zip:  97%|█████████▋| 837M/862M [06:17<00:33, 763kB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 837M/862M [06:18<00:24, 1.00MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 838M/862M [06:18<00:18, 1.33MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 839M/862M [06:18<00:13, 1.73MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 840M/862M [06:18<00:10, 2.18MB/s].vector_cache/glove.6B.zip:  97%|█████████▋| 840M/862M [06:18<00:08, 2.57MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 841M/862M [06:18<00:07, 2.94MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 841M/862M [06:19<02:19, 153kB/s] .vector_cache/glove.6B.zip:  98%|█████████▊| 841M/862M [06:19<01:46, 201kB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 841M/862M [06:20<01:14, 279kB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 842M/862M [06:20<00:52, 387kB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 842M/862M [06:20<00:36, 536kB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 843M/862M [06:20<00:26, 731kB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 843M/862M [06:20<00:19, 963kB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 844M/862M [06:20<00:14, 1.27MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 844M/862M [06:20<00:11, 1.59MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 845M/862M [06:20<00:09, 1.94MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 845M/862M [06:21<00:21, 802kB/s] .vector_cache/glove.6B.zip:  98%|█████████▊| 845M/862M [06:21<00:20, 818kB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 845M/862M [06:22<00:15, 1.05MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 846M/862M [06:22<00:11, 1.36MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 847M/862M [06:22<00:08, 1.74MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 847M/862M [06:22<00:07, 1.97MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 848M/862M [06:22<00:06, 2.40MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 848M/862M [06:22<00:05, 2.68MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 849M/862M [06:22<00:04, 2.85MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 849M/862M [06:23<00:12, 1.09MB/s].vector_cache/glove.6B.zip:  98%|█████████▊| 849M/862M [06:23<00:11, 1.14MB/s].vector_cache/glove.6B.zip:  99%|█████████▊| 850M/862M [06:24<00:08, 1.42MB/s].vector_cache/glove.6B.zip:  99%|█████████▊| 850M/862M [06:24<00:06, 1.73MB/s].vector_cache/glove.6B.zip:  99%|█████████▊| 851M/862M [06:24<00:05, 2.07MB/s].vector_cache/glove.6B.zip:  99%|█████████▊| 851M/862M [06:24<00:04, 2.38MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 852M/862M [06:24<00:03, 2.65MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 852M/862M [06:24<00:03, 2.90MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 853M/862M [06:24<00:03, 3.10MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 853M/862M [06:24<00:02, 3.28MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 853M/862M [06:25<00:51, 174kB/s] .vector_cache/glove.6B.zip:  99%|█████████▉| 853M/862M [06:25<00:37, 237kB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 854M/862M [06:25<00:25, 329kB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 854M/862M [06:26<00:17, 453kB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 855M/862M [06:26<00:11, 614kB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 855M/862M [06:26<00:08, 822kB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 856M/862M [06:26<00:05, 1.08MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 856M/862M [06:26<00:04, 1.39MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 857M/862M [06:26<00:03, 1.72MB/s].vector_cache/glove.6B.zip:  99%|█████████▉| 857M/862M [06:27<00:05, 829kB/s] .vector_cache/glove.6B.zip:  99%|█████████▉| 857M/862M [06:27<00:04, 976kB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 858M/862M [06:27<00:03, 1.22MB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 858M/862M [06:28<00:02, 1.57MB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 859M/862M [06:28<00:01, 1.91MB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 860M/862M [06:28<00:01, 2.26MB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 860M/862M [06:28<00:00, 2.71MB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 860M/862M [06:28<00:00, 2.60MB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 861M/862M [06:28<00:00, 3.02MB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 861M/862M [06:28<00:00, 3.25MB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 861M/862M [06:29<00:01, 477kB/s] .vector_cache/glove.6B.zip: 100%|█████████▉| 862M/862M [06:29<00:01, 532kB/s].vector_cache/glove.6B.zip: 100%|█████████▉| 862M/862M [06:29<00:00, 708kB/s].vector_cache/glove.6B.zip: 862MB [06:29, 2.21MB/s]                          
  0%|          | 0/400000 [00:00<?, ?it/s]  0%|          | 1/400000 [00:00<14:37:59,  7.59it/s]  0%|          | 852/400000 [00:00<10:13:31, 10.84it/s]  0%|          | 1724/400000 [00:00<7:08:45, 15.48it/s]  1%|          | 2583/400000 [00:00<4:59:42, 22.10it/s]  1%|          | 3441/400000 [00:00<3:29:34, 31.54it/s]  1%|          | 4312/400000 [00:00<2:26:36, 44.98it/s]  1%|▏         | 5177/400000 [00:00<1:42:37, 64.12it/s]  2%|▏         | 6044/400000 [00:00<1:11:54, 91.31it/s]  2%|▏         | 6905/400000 [00:00<50:27, 129.85it/s]   2%|▏         | 7763/400000 [00:01<35:28, 184.30it/s]  2%|▏         | 8627/400000 [00:01<25:00, 260.90it/s]  2%|▏         | 9490/400000 [00:01<17:41, 367.94it/s]  3%|▎         | 10344/400000 [00:01<12:35, 516.09it/s]  3%|▎         | 11198/400000 [00:01<09:01, 718.65it/s]  3%|▎         | 12052/400000 [00:01<06:31, 990.86it/s]  3%|▎         | 12903/400000 [00:01<04:48, 1340.26it/s]  3%|▎         | 13754/400000 [00:01<03:35, 1793.58it/s]  4%|▎         | 14610/400000 [00:01<02:43, 2350.99it/s]  4%|▍         | 15449/400000 [00:01<02:08, 2998.19it/s]  4%|▍         | 16298/400000 [00:02<01:43, 3719.97it/s]  4%|▍         | 17154/400000 [00:02<01:25, 4479.11it/s]  5%|▍         | 18034/400000 [00:02<01:12, 5251.86it/s]  5%|▍         | 18904/400000 [00:02<01:03, 5959.28it/s]  5%|▍         | 19775/400000 [00:02<00:57, 6582.57it/s]  5%|▌         | 20642/400000 [00:02<00:53, 7094.29it/s]  5%|▌         | 21508/400000 [00:02<00:50, 7499.72it/s]  6%|▌         | 22386/400000 [00:02<00:48, 7842.24it/s]  6%|▌         | 23256/400000 [00:02<00:46, 8080.59it/s]  6%|▌         | 24141/400000 [00:02<00:45, 8295.74it/s]  6%|▋         | 25015/400000 [00:03<00:44, 8392.82it/s]  6%|▋         | 25890/400000 [00:03<00:44, 8495.01it/s]  7%|▋         | 26762/400000 [00:03<00:43, 8549.36it/s]  7%|▋         | 27636/400000 [00:03<00:43, 8603.45it/s]  7%|▋         | 28508/400000 [00:03<00:43, 8627.58it/s]  7%|▋         | 29379/400000 [00:03<00:43, 8596.12it/s]  8%|▊         | 30245/400000 [00:03<00:43, 8545.81it/s]  8%|▊         | 31109/400000 [00:03<00:43, 8571.50it/s]  8%|▊         | 31975/400000 [00:03<00:42, 8595.95it/s]  8%|▊         | 32837/400000 [00:03<00:42, 8603.01it/s]  8%|▊         | 33699/400000 [00:04<00:42, 8567.79it/s]  9%|▊         | 34565/400000 [00:04<00:42, 8592.11it/s]  9%|▉         | 35428/400000 [00:04<00:42, 8602.37it/s]  9%|▉         | 36310/400000 [00:04<00:41, 8663.90it/s]  9%|▉         | 37186/400000 [00:04<00:41, 8691.03it/s] 10%|▉         | 38075/400000 [00:04<00:41, 8749.22it/s] 10%|▉         | 38951/400000 [00:04<00:41, 8640.94it/s] 10%|▉         | 39823/400000 [00:04<00:41, 8663.00it/s] 10%|█         | 40703/400000 [00:04<00:41, 8701.78it/s] 10%|█         | 41580/400000 [00:04<00:41, 8717.60it/s] 11%|█         | 42453/400000 [00:05<00:41, 8720.53it/s] 11%|█         | 43326/400000 [00:05<00:41, 8653.07it/s] 11%|█         | 44192/400000 [00:05<00:41, 8644.98it/s] 11%|█▏        | 45057/400000 [00:05<00:41, 8643.12it/s] 11%|█▏        | 45922/400000 [00:05<00:40, 8640.29it/s] 12%|█▏        | 46787/400000 [00:05<00:41, 8592.72it/s] 12%|█▏        | 47647/400000 [00:05<00:41, 8572.35it/s] 12%|█▏        | 48505/400000 [00:05<00:41, 8545.98it/s] 12%|█▏        | 49369/400000 [00:05<00:40, 8573.33it/s] 13%|█▎        | 50235/400000 [00:05<00:40, 8598.45it/s] 13%|█▎        | 51100/400000 [00:06<00:40, 8612.75it/s] 13%|█▎        | 51962/400000 [00:06<00:40, 8547.08it/s] 13%|█▎        | 52834/400000 [00:06<00:40, 8596.11it/s] 13%|█▎        | 53719/400000 [00:06<00:39, 8669.50it/s] 14%|█▎        | 54587/400000 [00:06<00:39, 8637.98it/s] 14%|█▍        | 55462/400000 [00:06<00:39, 8671.23it/s] 14%|█▍        | 56330/400000 [00:06<00:39, 8643.68it/s] 14%|█▍        | 57195/400000 [00:06<00:39, 8613.61it/s] 15%|█▍        | 58075/400000 [00:06<00:39, 8667.45it/s] 15%|█▍        | 58942/400000 [00:06<00:39, 8620.84it/s] 15%|█▍        | 59813/400000 [00:07<00:39, 8644.73it/s] 15%|█▌        | 60678/400000 [00:07<00:39, 8598.82it/s] 15%|█▌        | 61539/400000 [00:07<00:39, 8550.65it/s] 16%|█▌        | 62395/400000 [00:07<00:39, 8543.29it/s] 16%|█▌        | 63258/400000 [00:07<00:39, 8567.96it/s] 16%|█▌        | 64128/400000 [00:07<00:39, 8605.96it/s] 16%|█▌        | 64989/400000 [00:07<00:39, 8561.25it/s] 16%|█▋        | 65846/400000 [00:07<00:39, 8557.55it/s] 17%|█▋        | 66708/400000 [00:07<00:38, 8573.46it/s] 17%|█▋        | 67578/400000 [00:07<00:38, 8610.40it/s] 17%|█▋        | 68452/400000 [00:08<00:38, 8648.65it/s] 17%|█▋        | 69317/400000 [00:08<00:38, 8578.88it/s] 18%|█▊        | 70176/400000 [00:08<00:38, 8557.18it/s] 18%|█▊        | 71040/400000 [00:08<00:38, 8581.13it/s] 18%|█▊        | 71904/400000 [00:08<00:38, 8596.72it/s] 18%|█▊        | 72764/400000 [00:08<00:38, 8584.05it/s] 18%|█▊        | 73623/400000 [00:08<00:38, 8552.78it/s] 19%|█▊        | 74482/400000 [00:08<00:38, 8563.09it/s] 19%|█▉        | 75345/400000 [00:08<00:37, 8580.76it/s] 19%|█▉        | 76206/400000 [00:08<00:37, 8589.46it/s] 19%|█▉        | 77065/400000 [00:09<00:37, 8543.87it/s] 19%|█▉        | 77920/400000 [00:09<00:37, 8497.04it/s] 20%|█▉        | 78791/400000 [00:09<00:37, 8557.95it/s] 20%|█▉        | 79647/400000 [00:09<00:37, 8497.18it/s] 20%|██        | 80498/400000 [00:09<00:37, 8499.92it/s] 20%|██        | 81371/400000 [00:09<00:37, 8565.47it/s] 21%|██        | 82228/400000 [00:09<00:37, 8566.07it/s] 21%|██        | 83099/400000 [00:09<00:36, 8607.58it/s] 21%|██        | 83967/400000 [00:09<00:36, 8628.36it/s] 21%|██        | 84830/400000 [00:09<00:36, 8590.48it/s] 21%|██▏       | 85690/400000 [00:10<00:36, 8551.97it/s] 22%|██▏       | 86546/400000 [00:10<00:36, 8483.99it/s] 22%|██▏       | 87402/400000 [00:10<00:36, 8505.35it/s] 22%|██▏       | 88262/400000 [00:10<00:36, 8531.84it/s] 22%|██▏       | 89122/400000 [00:10<00:36, 8551.27it/s] 22%|██▏       | 89978/400000 [00:10<00:36, 8507.77it/s] 23%|██▎       | 90829/400000 [00:10<00:36, 8455.58it/s] 23%|██▎       | 91696/400000 [00:10<00:36, 8518.49it/s] 23%|██▎       | 92563/400000 [00:10<00:35, 8563.26it/s] 23%|██▎       | 93433/400000 [00:11<00:35, 8602.35it/s] 24%|██▎       | 94306/400000 [00:11<00:35, 8637.36it/s] 24%|██▍       | 95176/400000 [00:11<00:35, 8654.09it/s] 24%|██▍       | 96042/400000 [00:11<00:35, 8653.34it/s] 24%|██▍       | 96908/400000 [00:11<00:35, 8619.48it/s] 24%|██▍       | 97780/400000 [00:11<00:34, 8648.67it/s] 25%|██▍       | 98647/400000 [00:11<00:34, 8653.54it/s] 25%|██▍       | 99513/400000 [00:11<00:34, 8614.99it/s] 25%|██▌       | 100375/400000 [00:11<00:34, 8604.46it/s] 25%|██▌       | 101236/400000 [00:11<00:34, 8559.26it/s] 26%|██▌       | 102093/400000 [00:12<00:35, 8510.11it/s] 26%|██▌       | 102963/400000 [00:12<00:34, 8565.94it/s] 26%|██▌       | 103820/400000 [00:12<00:34, 8557.03it/s] 26%|██▌       | 104702/400000 [00:12<00:34, 8633.21it/s] 26%|██▋       | 105575/400000 [00:12<00:33, 8661.31it/s] 27%|██▋       | 106447/400000 [00:12<00:33, 8677.41it/s] 27%|██▋       | 107315/400000 [00:12<00:33, 8624.12it/s] 27%|██▋       | 108178/400000 [00:12<00:33, 8602.69it/s] 27%|██▋       | 109052/400000 [00:12<00:33, 8641.85it/s] 27%|██▋       | 109917/400000 [00:12<00:33, 8622.88it/s] 28%|██▊       | 110785/400000 [00:13<00:33, 8637.49it/s] 28%|██▊       | 111666/400000 [00:13<00:33, 8685.39it/s] 28%|██▊       | 112535/400000 [00:13<00:33, 8669.25it/s] 28%|██▊       | 113403/400000 [00:13<00:33, 8590.33it/s] 29%|██▊       | 114269/400000 [00:13<00:33, 8608.22it/s] 29%|██▉       | 115132/400000 [00:13<00:33, 8613.18it/s] 29%|██▉       | 116003/400000 [00:13<00:32, 8641.03it/s] 29%|██▉       | 116868/400000 [00:13<00:32, 8616.95it/s] 29%|██▉       | 117740/400000 [00:13<00:32, 8644.98it/s] 30%|██▉       | 118619/400000 [00:13<00:32, 8686.11it/s] 30%|██▉       | 119488/400000 [00:14<00:33, 8465.94it/s] 30%|███       | 120367/400000 [00:14<00:32, 8550.85it/s] 30%|███       | 121231/400000 [00:14<00:32, 8577.27it/s] 31%|███       | 122096/400000 [00:14<00:32, 8598.90it/s] 31%|███       | 122957/400000 [00:14<00:32, 8568.28it/s] 31%|███       | 123824/400000 [00:14<00:32, 8597.48it/s] 31%|███       | 124704/400000 [00:14<00:31, 8656.16it/s] 31%|███▏      | 125570/400000 [00:14<00:32, 8563.80it/s] 32%|███▏      | 126434/400000 [00:14<00:31, 8584.16it/s] 32%|███▏      | 127300/400000 [00:14<00:31, 8604.49it/s] 32%|███▏      | 128161/400000 [00:15<00:31, 8604.51it/s] 32%|███▏      | 129027/400000 [00:15<00:31, 8618.73it/s] 32%|███▏      | 129889/400000 [00:15<00:31, 8539.09it/s] 33%|███▎      | 130744/400000 [00:15<00:31, 8508.39it/s] 33%|███▎      | 131603/400000 [00:15<00:31, 8531.20it/s] 33%|███▎      | 132463/400000 [00:15<00:31, 8551.11it/s] 33%|███▎      | 133332/400000 [00:15<00:31, 8591.99it/s] 34%|███▎      | 134193/400000 [00:15<00:30, 8594.66it/s] 34%|███▍      | 135053/400000 [00:15<00:31, 8529.01it/s] 34%|███▍      | 135922/400000 [00:15<00:30, 8574.68it/s] 34%|███▍      | 136785/400000 [00:16<00:30, 8590.70it/s] 34%|███▍      | 137657/400000 [00:16<00:30, 8628.87it/s] 35%|███▍      | 138528/400000 [00:16<00:30, 8651.98it/s] 35%|███▍      | 139394/400000 [00:16<00:30, 8642.52it/s] 35%|███▌      | 140270/400000 [00:16<00:29, 8677.11it/s] 35%|███▌      | 141138/400000 [00:16<00:29, 8671.62it/s] 36%|███▌      | 142006/400000 [00:16<00:29, 8667.29it/s] 36%|███▌      | 142884/400000 [00:16<00:29, 8698.85it/s] 36%|███▌      | 143765/400000 [00:16<00:29, 8729.88it/s] 36%|███▌      | 144639/400000 [00:16<00:29, 8721.52it/s] 36%|███▋      | 145512/400000 [00:17<00:29, 8710.81it/s] 37%|███▋      | 146388/400000 [00:17<00:29, 8725.19it/s] 37%|███▋      | 147261/400000 [00:17<00:29, 8705.17it/s] 37%|███▋      | 148132/400000 [00:17<00:29, 8660.20it/s] 37%|███▋      | 148999/400000 [00:17<00:29, 8644.36it/s] 37%|███▋      | 149864/400000 [00:17<00:29, 8610.35it/s] 38%|███▊      | 150757/400000 [00:17<00:28, 8701.31it/s] 38%|███▊      | 151656/400000 [00:17<00:28, 8783.24it/s] 38%|███▊      | 152535/400000 [00:17<00:28, 8769.61it/s] 38%|███▊      | 153413/400000 [00:17<00:28, 8752.73it/s] 39%|███▊      | 154305/400000 [00:18<00:27, 8801.15it/s] 39%|███▉      | 155190/400000 [00:18<00:27, 8813.85it/s] 39%|███▉      | 156072/400000 [00:18<00:27, 8780.59it/s] 39%|███▉      | 156951/400000 [00:18<00:27, 8736.38it/s] 39%|███▉      | 157828/400000 [00:18<00:27, 8743.99it/s] 40%|███▉      | 158703/400000 [00:18<00:27, 8733.22it/s] 40%|███▉      | 159577/400000 [00:18<00:27, 8726.58it/s] 40%|████      | 160450/400000 [00:18<00:27, 8706.57it/s] 40%|████      | 161321/400000 [00:18<00:27, 8643.98it/s] 41%|████      | 162186/400000 [00:18<00:27, 8622.54it/s] 41%|████      | 163056/400000 [00:19<00:27, 8643.90it/s] 41%|████      | 163929/400000 [00:19<00:27, 8668.51it/s] 41%|████      | 164801/400000 [00:19<00:27, 8681.78it/s] 41%|████▏     | 165670/400000 [00:19<00:27, 8654.53it/s] 42%|████▏     | 166536/400000 [00:19<00:27, 8645.55it/s] 42%|████▏     | 167401/400000 [00:19<00:27, 8590.39it/s] 42%|████▏     | 168261/400000 [00:19<00:27, 8430.32it/s] 42%|████▏     | 169105/400000 [00:19<00:27, 8387.51it/s] 42%|████▏     | 169958/400000 [00:19<00:27, 8427.61it/s] 43%|████▎     | 170816/400000 [00:19<00:27, 8471.99it/s] 43%|████▎     | 171681/400000 [00:20<00:26, 8522.65it/s] 43%|████▎     | 172544/400000 [00:20<00:26, 8552.45it/s] 43%|████▎     | 173410/400000 [00:20<00:26, 8581.99it/s] 44%|████▎     | 174269/400000 [00:20<00:26, 8580.36it/s] 44%|████▍     | 175130/400000 [00:20<00:26, 8588.83it/s] 44%|████▍     | 176000/400000 [00:20<00:25, 8620.34it/s] 44%|████▍     | 176865/400000 [00:20<00:25, 8628.35it/s] 44%|████▍     | 177730/400000 [00:20<00:25, 8632.03it/s] 45%|████▍     | 178594/400000 [00:20<00:25, 8598.31it/s] 45%|████▍     | 179468/400000 [00:20<00:25, 8637.70it/s] 45%|████▌     | 180344/400000 [00:21<00:25, 8673.47it/s] 45%|████▌     | 181216/400000 [00:21<00:25, 8687.29it/s] 46%|████▌     | 182098/400000 [00:21<00:24, 8723.86it/s] 46%|████▌     | 182971/400000 [00:21<00:25, 8676.48it/s] 46%|████▌     | 183839/400000 [00:21<00:24, 8659.38it/s] 46%|████▌     | 184706/400000 [00:21<00:24, 8657.82it/s] 46%|████▋     | 185579/400000 [00:21<00:24, 8676.52it/s] 47%|████▋     | 186447/400000 [00:21<00:24, 8666.05it/s] 47%|████▋     | 187314/400000 [00:21<00:24, 8651.74it/s] 47%|████▋     | 188180/400000 [00:21<00:24, 8619.18it/s] 47%|████▋     | 189051/400000 [00:22<00:24, 8645.82it/s] 47%|████▋     | 189931/400000 [00:22<00:24, 8689.77it/s] 48%|████▊     | 190801/400000 [00:22<00:24, 8683.49it/s] 48%|████▊     | 191670/400000 [00:22<00:24, 8556.82it/s] 48%|████▊     | 192535/400000 [00:22<00:24, 8583.38it/s] 48%|████▊     | 193402/400000 [00:22<00:24, 8606.92it/s] 49%|████▊     | 194272/400000 [00:22<00:23, 8632.19it/s] 49%|████▉     | 195141/400000 [00:22<00:23, 8647.69it/s] 49%|████▉     | 196011/400000 [00:22<00:23, 8662.49it/s] 49%|████▉     | 196878/400000 [00:22<00:23, 8660.96it/s] 49%|████▉     | 197747/400000 [00:23<00:23, 8669.27it/s] 50%|████▉     | 198633/400000 [00:23<00:23, 8724.64it/s] 50%|████▉     | 199523/400000 [00:23<00:22, 8775.25it/s] 50%|█████     | 200401/400000 [00:23<00:22, 8774.23it/s] 50%|█████     | 201279/400000 [00:23<00:22, 8760.28it/s] 51%|█████     | 202156/400000 [00:23<00:22, 8735.04it/s] 51%|█████     | 203034/400000 [00:23<00:22, 8745.92it/s] 51%|█████     | 203911/400000 [00:23<00:22, 8752.55it/s] 51%|█████     | 204792/400000 [00:23<00:22, 8769.06it/s] 51%|█████▏    | 205670/400000 [00:23<00:22, 8769.79it/s] 52%|█████▏    | 206548/400000 [00:24<00:22, 8761.77it/s] 52%|█████▏    | 207425/400000 [00:24<00:22, 8739.96it/s] 52%|█████▏    | 208305/400000 [00:24<00:21, 8755.64it/s] 52%|█████▏    | 209181/400000 [00:24<00:22, 8660.57it/s] 53%|█████▎    | 210048/400000 [00:24<00:21, 8658.47it/s] 53%|█████▎    | 210924/400000 [00:24<00:21, 8686.18it/s] 53%|█████▎    | 211804/400000 [00:24<00:21, 8718.29it/s] 53%|█████▎    | 212685/400000 [00:24<00:21, 8744.76it/s] 53%|█████▎    | 213561/400000 [00:24<00:21, 8746.35it/s] 54%|█████▎    | 214436/400000 [00:24<00:21, 8730.57it/s] 54%|█████▍    | 215321/400000 [00:25<00:21, 8763.89it/s] 54%|█████▍    | 216198/400000 [00:25<00:20, 8755.17it/s] 54%|█████▍    | 217074/400000 [00:25<00:20, 8748.04it/s] 54%|█████▍    | 217949/400000 [00:25<00:21, 8652.81it/s] 55%|█████▍    | 218815/400000 [00:25<00:21, 8617.68it/s] 55%|█████▍    | 219684/400000 [00:25<00:20, 8638.86it/s] 55%|█████▌    | 220549/400000 [00:25<00:20, 8639.35it/s] 55%|█████▌    | 221420/400000 [00:25<00:20, 8657.99it/s] 56%|█████▌    | 222286/400000 [00:25<00:20, 8621.21it/s] 56%|█████▌    | 223149/400000 [00:26<00:20, 8552.43it/s] 56%|█████▌    | 224019/400000 [00:26<00:20, 8593.51it/s] 56%|█████▌    | 224887/400000 [00:26<00:20, 8617.30it/s] 56%|█████▋    | 225763/400000 [00:26<00:20, 8658.81it/s] 57%|█████▋    | 226630/400000 [00:26<00:20, 8656.72it/s] 57%|█████▋    | 227496/400000 [00:26<00:20, 8586.77it/s] 57%|█████▋    | 228368/400000 [00:26<00:19, 8626.02it/s] 57%|█████▋    | 229240/400000 [00:26<00:19, 8653.29it/s] 58%|█████▊    | 230107/400000 [00:26<00:19, 8655.61it/s] 58%|█████▊    | 230975/400000 [00:26<00:19, 8662.25it/s] 58%|█████▊    | 231842/400000 [00:27<00:19, 8652.79it/s] 58%|█████▊    | 232725/400000 [00:27<00:19, 8702.90it/s] 58%|█████▊    | 233596/400000 [00:27<00:19, 8696.35it/s] 59%|█████▊    | 234467/400000 [00:27<00:19, 8699.56it/s] 59%|█████▉    | 235338/400000 [00:27<00:19, 8606.26it/s] 59%|█████▉    | 236199/400000 [00:27<00:19, 8482.72it/s] 59%|█████▉    | 237048/400000 [00:27<00:20, 8079.82it/s] 59%|█████▉    | 237924/400000 [00:27<00:19, 8269.93it/s] 60%|█████▉    | 238789/400000 [00:27<00:19, 8378.61it/s] 60%|█████▉    | 239661/400000 [00:27<00:18, 8476.20it/s] 60%|██████    | 240525/400000 [00:28<00:18, 8524.26it/s] 60%|██████    | 241407/400000 [00:28<00:18, 8608.88it/s] 61%|██████    | 242282/400000 [00:28<00:18, 8649.87it/s] 61%|██████    | 243159/400000 [00:28<00:18, 8685.26it/s] 61%|██████    | 244029/400000 [00:28<00:18, 8649.43it/s] 61%|██████    | 244895/400000 [00:28<00:18, 8594.19it/s] 61%|██████▏   | 245758/400000 [00:28<00:17, 8604.55it/s] 62%|██████▏   | 246619/400000 [00:28<00:17, 8606.03it/s] 62%|██████▏   | 247495/400000 [00:28<00:17, 8650.98it/s] 62%|██████▏   | 248367/400000 [00:28<00:17, 8670.27it/s] 62%|██████▏   | 249235/400000 [00:29<00:17, 8663.72it/s] 63%|██████▎   | 250105/400000 [00:29<00:17, 8672.78it/s] 63%|██████▎   | 251002/400000 [00:29<00:17, 8757.49it/s] 63%|██████▎   | 251879/400000 [00:29<00:16, 8723.02it/s] 63%|██████▎   | 252752/400000 [00:29<00:16, 8664.91it/s] 63%|██████▎   | 253619/400000 [00:29<00:16, 8634.33it/s] 64%|██████▎   | 254483/400000 [00:29<00:16, 8620.68it/s] 64%|██████▍   | 255350/400000 [00:29<00:16, 8633.37it/s] 64%|██████▍   | 256221/400000 [00:29<00:16, 8656.05it/s] 64%|██████▍   | 257097/400000 [00:29<00:16, 8686.06it/s] 64%|██████▍   | 257966/400000 [00:30<00:16, 8642.61it/s] 65%|██████▍   | 258842/400000 [00:30<00:16, 8675.14it/s] 65%|██████▍   | 259710/400000 [00:30<00:16, 8669.45it/s] 65%|██████▌   | 260578/400000 [00:30<00:16, 8664.19it/s] 65%|██████▌   | 261445/400000 [00:30<00:15, 8660.45it/s] 66%|██████▌   | 262312/400000 [00:30<00:15, 8605.97it/s] 66%|██████▌   | 263173/400000 [00:30<00:15, 8603.27it/s] 66%|██████▌   | 264034/400000 [00:30<00:15, 8582.41it/s] 66%|██████▌   | 264897/400000 [00:30<00:15, 8596.45it/s] 66%|██████▋   | 265764/400000 [00:30<00:15, 8616.76it/s] 67%|██████▋   | 266628/400000 [00:31<00:15, 8621.65it/s] 67%|██████▋   | 267495/400000 [00:31<00:15, 8634.48it/s] 67%|██████▋   | 268359/400000 [00:31<00:15, 8584.67it/s] 67%|██████▋   | 269218/400000 [00:31<00:15, 8578.44it/s] 68%|██████▊   | 270086/400000 [00:31<00:15, 8607.04it/s] 68%|██████▊   | 270947/400000 [00:31<00:15, 8515.67it/s] 68%|██████▊   | 271821/400000 [00:31<00:14, 8579.64it/s] 68%|██████▊   | 272690/400000 [00:31<00:14, 8609.85it/s] 68%|██████▊   | 273552/400000 [00:31<00:14, 8587.95it/s] 69%|██████▊   | 274418/400000 [00:31<00:14, 8607.66it/s] 69%|██████▉   | 275279/400000 [00:32<00:14, 8372.09it/s] 69%|██████▉   | 276139/400000 [00:32<00:14, 8438.68it/s] 69%|██████▉   | 276985/400000 [00:32<00:14, 8423.39it/s] 69%|██████▉   | 277832/400000 [00:32<00:14, 8435.70it/s] 70%|██████▉   | 278689/400000 [00:32<00:14, 8475.15it/s] 70%|██████▉   | 279542/400000 [00:32<00:14, 8490.45it/s] 70%|███████   | 280396/400000 [00:32<00:14, 8504.83it/s] 70%|███████   | 281257/400000 [00:32<00:13, 8534.07it/s] 71%|███████   | 282121/400000 [00:32<00:13, 8563.19it/s] 71%|███████   | 282978/400000 [00:32<00:13, 8559.39it/s] 71%|███████   | 283835/400000 [00:33<00:13, 8523.70it/s] 71%|███████   | 284721/400000 [00:33<00:13, 8619.35it/s] 71%|███████▏  | 285604/400000 [00:33<00:13, 8679.15it/s] 72%|███████▏  | 286473/400000 [00:33<00:13, 8647.11it/s] 72%|███████▏  | 287338/400000 [00:33<00:13, 8583.37it/s] 72%|███████▏  | 288197/400000 [00:33<00:13, 8558.69it/s] 72%|███████▏  | 289054/400000 [00:33<00:13, 8528.04it/s] 72%|███████▏  | 289907/400000 [00:33<00:13, 8267.84it/s] 73%|███████▎  | 290773/400000 [00:33<00:13, 8381.57it/s] 73%|███████▎  | 291655/400000 [00:33<00:12, 8506.01it/s] 73%|███████▎  | 292534/400000 [00:34<00:12, 8588.76it/s] 73%|███████▎  | 293395/400000 [00:34<00:12, 8522.21it/s] 74%|███████▎  | 294249/400000 [00:34<00:12, 8409.77it/s] 74%|███████▍  | 295122/400000 [00:34<00:12, 8502.21it/s] 74%|███████▍  | 295996/400000 [00:34<00:12, 8572.04it/s] 74%|███████▍  | 296865/400000 [00:34<00:11, 8604.68it/s] 74%|███████▍  | 297727/400000 [00:34<00:11, 8608.64it/s] 75%|███████▍  | 298594/400000 [00:34<00:11, 8626.64it/s] 75%|███████▍  | 299468/400000 [00:34<00:11, 8660.07it/s] 75%|███████▌  | 300349/400000 [00:34<00:11, 8701.71it/s] 75%|███████▌  | 301224/400000 [00:35<00:11, 8715.12it/s] 76%|███████▌  | 302096/400000 [00:35<00:11, 8679.94it/s] 76%|███████▌  | 302975/400000 [00:35<00:11, 8712.60it/s] 76%|███████▌  | 303857/400000 [00:35<00:10, 8742.83it/s] 76%|███████▌  | 304734/400000 [00:35<00:10, 8748.90it/s] 76%|███████▋  | 305609/400000 [00:35<00:10, 8728.98it/s] 77%|███████▋  | 306482/400000 [00:35<00:10, 8675.61it/s] 77%|███████▋  | 307350/400000 [00:35<00:10, 8633.77it/s] 77%|███████▋  | 308214/400000 [00:35<00:10, 8624.49it/s] 77%|███████▋  | 309089/400000 [00:36<00:10, 8661.52it/s] 77%|███████▋  | 309956/400000 [00:36<00:10, 8658.35it/s] 78%|███████▊  | 310822/400000 [00:36<00:10, 8639.82it/s] 78%|███████▊  | 311689/400000 [00:36<00:10, 8648.72it/s] 78%|███████▊  | 312554/400000 [00:36<00:10, 8609.98it/s] 78%|███████▊  | 313423/400000 [00:36<00:10, 8632.66it/s] 79%|███████▊  | 314287/400000 [00:36<00:09, 8596.80it/s] 79%|███████▉  | 315158/400000 [00:36<00:09, 8629.19it/s] 79%|███████▉  | 316027/400000 [00:36<00:09, 8644.33it/s] 79%|███████▉  | 316910/400000 [00:36<00:09, 8699.04it/s] 79%|███████▉  | 317789/400000 [00:37<00:09, 8723.22it/s] 80%|███████▉  | 318662/400000 [00:37<00:09, 8722.06it/s] 80%|███████▉  | 319535/400000 [00:37<00:09, 8670.05it/s] 80%|████████  | 320403/400000 [00:37<00:09, 8648.09it/s] 80%|████████  | 321292/400000 [00:37<00:09, 8718.78it/s] 81%|████████  | 322169/400000 [00:37<00:08, 8733.16it/s] 81%|████████  | 323048/400000 [00:37<00:08, 8750.03it/s] 81%|████████  | 323924/400000 [00:37<00:08, 8715.21it/s] 81%|████████  | 324796/400000 [00:37<00:08, 8657.86it/s] 81%|████████▏ | 325675/400000 [00:37<00:08, 8696.26it/s] 82%|████████▏ | 326545/400000 [00:38<00:08, 8582.09it/s] 82%|████████▏ | 327404/400000 [00:38<00:08, 8569.76it/s] 82%|████████▏ | 328262/400000 [00:38<00:08, 8555.32it/s] 82%|████████▏ | 329118/400000 [00:38<00:08, 8490.14it/s] 82%|████████▏ | 329993/400000 [00:38<00:08, 8564.28it/s] 83%|████████▎ | 330878/400000 [00:38<00:07, 8646.14it/s] 83%|████████▎ | 331750/400000 [00:38<00:07, 8666.40it/s] 83%|████████▎ | 332617/400000 [00:38<00:07, 8557.64it/s] 83%|████████▎ | 333482/400000 [00:38<00:07, 8583.65it/s] 84%|████████▎ | 334356/400000 [00:38<00:07, 8627.01it/s] 84%|████████▍ | 335237/400000 [00:39<00:07, 8680.75it/s] 84%|████████▍ | 336122/400000 [00:39<00:07, 8730.48it/s] 84%|████████▍ | 336996/400000 [00:39<00:07, 8585.07it/s] 84%|████████▍ | 337856/400000 [00:39<00:07, 8560.33it/s] 85%|████████▍ | 338720/400000 [00:39<00:07, 8582.40it/s] 85%|████████▍ | 339579/400000 [00:39<00:07, 8573.33it/s] 85%|████████▌ | 340444/400000 [00:39<00:06, 8594.87it/s] 85%|████████▌ | 341304/400000 [00:39<00:06, 8542.42it/s] 86%|████████▌ | 342159/400000 [00:39<00:06, 8539.58it/s] 86%|████████▌ | 343026/400000 [00:39<00:06, 8576.89it/s] 86%|████████▌ | 343890/400000 [00:40<00:06, 8593.98it/s] 86%|████████▌ | 344753/400000 [00:40<00:06, 8604.07it/s] 86%|████████▋ | 345614/400000 [00:40<00:06, 8589.70it/s] 87%|████████▋ | 346474/400000 [00:40<00:06, 8584.53it/s] 87%|████████▋ | 347343/400000 [00:40<00:06, 8615.12it/s] 87%|████████▋ | 348213/400000 [00:40<00:05, 8640.15it/s] 87%|████████▋ | 349081/400000 [00:40<00:05, 8649.68it/s] 87%|████████▋ | 349947/400000 [00:40<00:05, 8531.05it/s] 88%|████████▊ | 350807/400000 [00:40<00:05, 8550.97it/s] 88%|████████▊ | 351675/400000 [00:40<00:05, 8586.64it/s] 88%|████████▊ | 352534/400000 [00:41<00:05, 8556.95it/s] 88%|████████▊ | 353394/400000 [00:41<00:05, 8568.51it/s] 89%|████████▊ | 354254/400000 [00:41<00:05, 8577.81it/s] 89%|████████▉ | 355116/400000 [00:41<00:05, 8588.50it/s] 89%|████████▉ | 355975/400000 [00:41<00:05, 8579.05it/s] 89%|████████▉ | 356833/400000 [00:41<00:05, 8537.01it/s] 89%|████████▉ | 357700/400000 [00:41<00:04, 8576.27it/s] 90%|████████▉ | 358558/400000 [00:41<00:04, 8558.65it/s] 90%|████████▉ | 359414/400000 [00:41<00:04, 8520.91it/s] 90%|█████████ | 360277/400000 [00:41<00:04, 8550.92it/s] 90%|█████████ | 361139/400000 [00:42<00:04, 8569.32it/s] 91%|█████████ | 362002/400000 [00:42<00:04, 8586.60it/s] 91%|█████████ | 362861/400000 [00:42<00:04, 8560.65it/s] 91%|█████████ | 363728/400000 [00:42<00:04, 8590.97it/s] 91%|█████████ | 364590/400000 [00:42<00:04, 8598.13it/s] 91%|█████████▏| 365455/400000 [00:42<00:04, 8611.13it/s] 92%|█████████▏| 366318/400000 [00:42<00:03, 8614.32it/s] 92%|█████████▏| 367180/400000 [00:42<00:03, 8508.93it/s] 92%|█████████▏| 368032/400000 [00:42<00:03, 8486.08it/s] 92%|█████████▏| 368896/400000 [00:42<00:03, 8529.39it/s] 92%|█████████▏| 369761/400000 [00:43<00:03, 8564.65it/s] 93%|█████████▎| 370622/400000 [00:43<00:03, 8576.61it/s] 93%|█████████▎| 371480/400000 [00:43<00:03, 8533.29it/s] 93%|█████████▎| 372338/400000 [00:43<00:03, 8545.74it/s] 93%|█████████▎| 373202/400000 [00:43<00:03, 8573.76it/s] 94%|█████████▎| 374075/400000 [00:43<00:03, 8617.81it/s] 94%|█████████▎| 374948/400000 [00:43<00:02, 8648.86it/s] 94%|█████████▍| 375813/400000 [00:43<00:02, 8586.86it/s] 94%|█████████▍| 376672/400000 [00:43<00:02, 8575.13it/s] 94%|█████████▍| 377530/400000 [00:43<00:02, 8548.23it/s] 95%|█████████▍| 378390/400000 [00:44<00:02, 8561.00it/s] 95%|█████████▍| 379254/400000 [00:44<00:02, 8583.76it/s] 95%|█████████▌| 380113/400000 [00:44<00:02, 8562.11it/s] 95%|█████████▌| 380989/400000 [00:44<00:02, 8619.06it/s] 95%|█████████▌| 381853/400000 [00:44<00:02, 8624.58it/s] 96%|█████████▌| 382716/400000 [00:44<00:02, 8620.40it/s] 96%|█████████▌| 383590/400000 [00:44<00:01, 8655.53it/s] 96%|█████████▌| 384461/400000 [00:44<00:01, 8669.66it/s] 96%|█████████▋| 385329/400000 [00:44<00:01, 8572.29it/s] 97%|█████████▋| 386189/400000 [00:44<00:01, 8578.10it/s] 97%|█████████▋| 387076/400000 [00:45<00:01, 8661.26it/s] 97%|█████████▋| 387945/400000 [00:45<00:01, 8667.00it/s] 97%|█████████▋| 388812/400000 [00:45<00:01, 8571.85it/s] 97%|█████████▋| 389672/400000 [00:45<00:01, 8578.61it/s] 98%|█████████▊| 390540/400000 [00:45<00:01, 8606.65it/s] 98%|█████████▊| 391413/400000 [00:45<00:00, 8641.98it/s] 98%|█████████▊| 392297/400000 [00:45<00:00, 8700.17it/s] 98%|█████████▊| 393168/400000 [00:45<00:00, 8664.77it/s] 99%|█████████▊| 394035/400000 [00:45<00:00, 8615.22it/s] 99%|█████████▊| 394918/400000 [00:45<00:00, 8677.87it/s] 99%|█████████▉| 395788/400000 [00:46<00:00, 8684.16it/s] 99%|█████████▉| 396658/400000 [00:46<00:00, 8686.07it/s] 99%|█████████▉| 397527/400000 [00:46<00:00, 8675.66it/s]100%|█████████▉| 398395/400000 [00:46<00:00, 8653.88it/s]100%|█████████▉| 399261/400000 [00:46<00:00, 8650.95it/s]100%|█████████▉| 399999/400000 [00:46<00:00, 8590.64it/s]Preprocessing the text...
Creating tabular datasets...It might take a while to finish!
Building vocaulary...

  
 #####  get_Data DataLoader  

  ((<torchtext.data.dataset.TabularDataset object at 0x7f37cf1e1c18>, <torchtext.data.dataset.TabularDataset object at 0x7f37d8065128>, <torchtext.vocab.Vocab object at 0x7f37cf1e1c50>), {}) 

  




 #################################################################################################### 

  /home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/transformer_sentence.json 
 

  #####  Load JSON data_pars 

  {
  "data_info":{

  },
  "preprocessors":[
    {
      "name":"DataReader",
      "uri":"mlmodels.model_tch.util_transformer:TransformerDataReader",
      "args":{
        "train":{
          "uri":"sentence_transformers.readers:NLIDataReader",
          "dataset":"dataset\/text\/AllNLI\/train"
        },
        "test":{
          "uri":"sentence_transformers.readers:STSBenchmarkDataReader",
          "dataset":"dataset\/text\/stsbenchmark\/val"
        }
      }
    }
  ]
} 

  
 #####  Load DataLoader  

  
 #####  compute DataLoader  

  URL:  mlmodels.model_tch.util_transformer:TransformerDataReader {'train': {'uri': 'sentence_transformers.readers:NLIDataReader', 'dataset': 'dataset/text/AllNLI/train'}, 'test': {'uri': 'sentence_transformers.readers:STSBenchmarkDataReader', 'dataset': 'dataset/text/stsbenchmark/val'}} 

  
###### load_callable_from_uri LOADED <class 'mlmodels.model_tch.util_transformer.TransformerDataReader'> 
cls_name : TransformerDataReader

  
 Object Creation 

  
 Object Compute 
Error /home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/transformer_sentence.json Module ['sentence_transformers.readers', 'STSBenchmarkDataReader'] notfound, module 'sentence_transformers.readers' has no attribute 'STSBenchmarkDataReader', tuple index out of range

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 672, in load_function_uri
    return  getattr(importlib.import_module(package), name)
AttributeError: module 'sentence_transformers.readers' has no attribute 'STSBenchmarkDataReader'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 683, in load_function_uri
    package_name = str(Path(package).parts[-2]) + "." + str(model_name)
IndexError: tuple index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/dataloader.py", line 452, in test_json_list
    loader.compute()
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/dataloader.py", line 275, in compute
    obj_preprocessor.compute(input_tmp)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch/util_transformer.py", line 275, in compute
    test_func = load_function(self.test_reader)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 688, in load_function_uri
    raise NameError(f"Module {pkg} notfound, {e1}, {e2}")
NameError: Module ['sentence_transformers.readers', 'STSBenchmarkDataReader'] notfound, module 'sentence_transformers.readers' has no attribute 'STSBenchmarkDataReader', tuple index out of range





 ********************************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/preprocess/generic.py --do test  

  #### Test unit Dataloader/Dataset   #################################### 

  


 #################### tf_dataset_download 

  tf_dataset_download mlmodels/preprocess/generic:tf_dataset_download {'train_samples': 500, 'test_samples': 500} 

  MNIST 

  Dataset Name is :  mnist 
WARNING:absl:Dataset mnist is hosted on GCS. It will automatically be downloaded to your
local data directory. If you'd instead prefer to read directly from our public
GCS bucket (recommended if you're running on GCP), you can instead set
data_dir=gs://tfds-data/datasets.

Dl Completed...:   0%|          | 0/4 [00:00<?, ? file/s]Dl Completed...:  25%|██▌       | 1/4 [00:00<00:00, 24.93 file/s]Dl Completed...:  50%|█████     | 2/4 [00:00<00:00, 45.51 file/s]Dl Completed...:  75%|███████▌  | 3/4 [00:00<00:00, 26.67 file/s]Dl Completed...:  75%|███████▌  | 3/4 [00:00<00:00, 26.67 file/s]Dl Completed...: 100%|██████████| 4/4 [00:00<00:00,  3.91 file/s]Dl Completed...: 100%|██████████| 4/4 [00:00<00:00,  3.91 file/s]Dl Completed...: 100%|██████████| 4/4 [00:00<00:00,  4.55 file/s]2020-06-19 00:18:30.173305: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 AVX512F FMA
2020-06-19 00:18:30.177794: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2095074999 Hz
2020-06-19 00:18:30.177979: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x55ff908ea260 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-06-19 00:18:30.177993: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
[1mDownloading and preparing dataset mnist/3.0.1 (download: 11.06 MiB, generated: 21.00 MiB, total: 32.06 MiB) to /home/runner/tensorflow_datasets/mnist/3.0.1...[0m

[1mDataset mnist downloaded and prepared to /home/runner/tensorflow_datasets/mnist/3.0.1. Subsequent calls will reuse this data.[0m

  ############## Saving train dataset ############################### 

  ############## Saving test dataset ############################### 

  Saved /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/ ['mnist_dataset_small.npy', 'cifar10', 'test', 'train', 'mnist2', 'fashion-mnist_small.npy'] 

  


 #################### get_dataset_torch 

  get_dataset_torch mlmodels/preprocess/generic:get_dataset_torch {'dataloader': 'torchvision.datasets:MNIST', 'to_image': True, 'transform': {'uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'pass_data_pars': False, 'arg': {}}, 'shuffle': True, 'download': True} 

  #### If transformer URI is Provided {'uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'pass_data_pars': False, 'arg': {}} 

  #### Loading dataloader URI 

  dataset :  <class 'torchvision.datasets.mnist.MNIST'> 

0it [00:00, ?it/s]  0%|          | 0/9912422 [00:00<?, ?it/s] 38%|███▊      | 3768320/9912422 [00:00<00:00, 37505913.79it/s]9920512it [00:00, 32726880.52it/s]                             
0it [00:00, ?it/s]32768it [00:00, 614082.15it/s]
0it [00:00, ?it/s]  3%|▎         | 49152/1648877 [00:00<00:03, 467476.25it/s]1654784it [00:00, 11755056.22it/s]                         
0it [00:00, ?it/s]8192it [00:00, 186474.21it/s]Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz to dataset/vision/MNIST/raw/train-images-idx3-ubyte.gz
Extracting dataset/vision/MNIST/raw/train-images-idx3-ubyte.gz to dataset/vision/MNIST/raw
Downloading http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz to dataset/vision/MNIST/raw/train-labels-idx1-ubyte.gz
Extracting dataset/vision/MNIST/raw/train-labels-idx1-ubyte.gz to dataset/vision/MNIST/raw
Downloading http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz to dataset/vision/MNIST/raw/t10k-images-idx3-ubyte.gz
Extracting dataset/vision/MNIST/raw/t10k-images-idx3-ubyte.gz to dataset/vision/MNIST/raw
Downloading http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz to dataset/vision/MNIST/raw/t10k-labels-idx1-ubyte.gz
Extracting dataset/vision/MNIST/raw/t10k-labels-idx1-ubyte.gz to dataset/vision/MNIST/raw
Processing...
Done!

  


 #################### PandasDataset 

  PandasDataset mlmodels/preprocess/generic:pandasDataset {'colX': ['colX'], 'coly': ['coly'], 'encoding': 'ISO-8859-1', 'read_csv_parm': {'usecols': [0, 1], 'names': ['coly', 'colX'], 'encoding': 'ISO-8859-1'}} 

  


 #################### NumpyDataset 

  NumpyDataset mlmodels/preprocess/generic:NumpyDataset {'to_image': True, 'transform': {'uri': 'mlmodels.preprocess.image:torch_transform_generic', 'pass_data_pars': False, 'arg': {'fixed_size': 256}}, 'numpy_loader_args': {}} 

Dataset File path :  /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/train/mnist.npz
