
  test_all /home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json Namespace(config_file='/home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json', config_mode='test', do='test_all', folder=None, log_file=None, save_folder='ztest/') 

  ml_test --do test_all 





 ************************************************************************************************************************

 ******** TAG ::  {'github_repo_url': 'https://github.com/arita37/mlmodels/tree/73f54da32a5da4768415eb9105ad096255137679', 'url_branch_file': 'https://github.com/arita37/mlmodels/blob/dev/', 'repo': 'arita37/mlmodels', 'branch': 'dev', 'sha': '73f54da32a5da4768415eb9105ad096255137679', 'workflow': 'test_all'}

 ******** GITHUB_WOKFLOW : https://github.com/arita37/mlmodels/actions?query=workflow%3Atest_all

 ******** GITHUB_REPO_BRANCH : https://github.com/arita37/mlmodels/tree/dev/

 ******** GITHUB_REPO_URL : https://github.com/arita37/mlmodels/tree/73f54da32a5da4768415eb9105ad096255137679

 ******** GITHUB_COMMIT_URL : https://github.com/arita37/mlmodels/commit/73f54da32a5da4768415eb9105ad096255137679

 ******** Click here for Online DEBUGGER : https://gitpod.io/#https://github.com/arita37/mlmodels/tree/73f54da32a5da4768415eb9105ad096255137679

 ************************************************************************************************************************

  ############Check model ################################ 

  ['model_keras.keras_gan', 'model_keras.textcnn_dataloader', 'model_keras.nbeats', 'model_keras.01_deepctr', 'model_keras.textvae', 'model_keras.namentity_crm_bilstm_dataloader', 'model_keras.Autokeras', 'model_keras.charcnn_zhang', 'model_keras.charcnn', 'model_keras.namentity_crm_bilstm', 'model_keras.textcnn', 'model_keras.armdn', 'model_keras.02_cnn', 'model_tf.1_lstm', 'model_tf.temporal_fusion_google', 'model_gluon.gluon_automl', 'model_gluon.fb_prophet', 'model_gluon.gluonts_model', 'model_sklearn.model_sklearn', 'model_sklearn.model_lightgbm', 'model_tch.nbeats', 'model_tch.transformer_classifier', 'model_tch.matchzoo_models', 'model_tch.torchhub', 'model_tch.03_nbeats_dataloader', 'model_tch.transformer_sentence', 'model_tch.pytorch_vae', 'model_tch.pplm', 'model_tch.textcnn', 'model_tch.mlp'] 

  Used ['model_keras.keras_gan', 'model_keras.textcnn_dataloader', 'model_keras.nbeats', 'model_keras.01_deepctr', 'model_keras.textvae', 'model_keras.namentity_crm_bilstm_dataloader', 'model_keras.Autokeras', 'model_keras.charcnn_zhang', 'model_keras.charcnn', 'model_keras.namentity_crm_bilstm', 'model_keras.textcnn', 'model_keras.armdn', 'model_keras.02_cnn', 'model_tf.1_lstm', 'model_tf.temporal_fusion_google', 'model_gluon.gluon_automl', 'model_gluon.fb_prophet', 'model_gluon.gluonts_model', 'model_sklearn.model_sklearn', 'model_sklearn.model_lightgbm', 'model_tch.nbeats', 'model_tch.transformer_classifier', 'model_tch.matchzoo_models', 'model_tch.torchhub', 'model_tch.03_nbeats_dataloader', 'model_tch.transformer_sentence', 'model_tch.pytorch_vae', 'model_tch.pplm', 'model_tch.textcnn', 'model_tch.mlp'] 





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//keras_gan.py 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//keras_gan.py", line 31, in <module>
    'AAE' : kg.aae.aae,
AttributeError: module 'mlmodels.model_keras.raw.keras_gan' has no attribute 'aae'

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Warning: Permanently added the RSA host key for IP address '140.82.114.4' to the list of known hosts.
Already up to date.
[master 6a8ee2e] ml_store
 2 files changed, 64 insertions(+), 11276 deletions(-)
 rewrite log_testall/log_testall.py (99%)
To github.com:arita37/mlmodels_store.git
   f88e918..6a8ee2e  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//textcnn_dataloader.py 

  #### Module init   ############################################ 

  <module 'mlmodels.model_keras.textcnn_dataloader' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/textcnn_dataloader.py'> 

  #### Loading params   ############################################## 
Using TensorFlow backend.
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//textcnn_dataloader.py", line 275, in <module>
    test_module(model_uri = MODEL_URI, param_pars= param_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 257, in test_module
    model_pars, data_pars, compute_pars, out_pars = module.get_params(param_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/textcnn_dataloader.py", line 182, in get_params
    cf = json.load(open(data_path, mode='r'))
FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor/textcnn_keras.json'

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Already up to date.
[master 3736ae6] ml_store
 1 file changed, 48 insertions(+)
To github.com:arita37/mlmodels_store.git
   6a8ee2e..3736ae6  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//nbeats.py 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Loading dataset   ############################################# 
Using TensorFlow backend.
Loading data...
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//nbeats.py", line 315, in <module>
    test(pars_choice="test01")
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//nbeats.py", line 278, in test
    Xtuple = get_dataset(data_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//nbeats.py", line 172, in get_dataset
    train_data = Data(data_source= path_norm( data_pars["train_data_source"]) ,
NameError: name 'Data' is not defined

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Already up to date.
[master 615a634] ml_store
 1 file changed, 48 insertions(+)
To github.com:arita37/mlmodels_store.git
   3736ae6..615a634  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//01_deepctr.py 

  #### Loading params   ############################################## 

  #### Path params   ################################################# 

  #### Model params   ################################################ 
{'model_name': 'AFM', 'optimization': 'adam', 'cost': 'mse'} {'dataset_type': 'synthesis', 'sample_size': 8, 'test_size': 0.2, 'dataset_name': 'AFM', 'sparse_feature_num': 3, 'dense_feature_num': 0} {'batch_size': 100, 'epochs': 1, 'validation_split': 0.5} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/deepctr/model_AFM.h5'}

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 
Using TensorFlow backend.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/keras/initializers.py:143: calling RandomNormal.__init__ (from tensorflow.python.ops.init_ops) with dtype is deprecated and will be removed in a future version.
Instructions for updating:
Call initializer instance with the dtype argument instead of passing it to the constructor
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/resource_variable_ops.py:1630: calling BaseResourceVariable.__init__ (from tensorflow.python.ops.resource_variable_ops) with constraint is deprecated and will be removed in a future version.
Instructions for updating:
If using Keras pass *_constraint arguments to layers.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/deepctr/layers/sequence.py:159: where (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/deepctr/layers/utils.py:199: calling softmax (from tensorflow.python.ops.nn_ops) with dim is deprecated and will be removed in a future version.
Instructions for updating:
dim is deprecated, use axis instead
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/deepctr/layers/utils.py:163: calling reduce_sum_v1 (from tensorflow.python.ops.math_ops) with keep_dims is deprecated and will be removed in a future version.
Instructions for updating:
keep_dims is deprecated, use keepdims instead
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/deepctr/layers/utils.py:193: div (from tensorflow.python.ops.math_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Deprecated in favor of operator or tf.math.divide.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/deepctr/layers/utils.py:180: calling reduce_max_v1 (from tensorflow.python.ops.math_ops) with keep_dims is deprecated and will be removed in a future version.
Instructions for updating:
keep_dims is deprecated, use keepdims instead
Model: "model"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
weighted_seq (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
weighted_seq_seq_length (InputL [(None, 1)]          0                                            
__________________________________________________________________________________________________
weight (InputLayer)             [(None, 3, 1)]       0                                            
__________________________________________________________________________________________________
sequence_sum (InputLayer)       [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 9)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_1 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_2 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_1 (Weig (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         9           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         4           sequence_max[0][0]               
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         1           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_4 (Seque (None, 1, 1)         0           weighted_sequence_layer_1[0][0]  
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_5 (Seque (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_6 (Seque (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_7 (Seque (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
no_mask (NoMask)                (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_4[0][0]   
                                                                 sequence_pooling_layer_5[0][0]   
                                                                 sequence_pooling_layer_6[0][0]   
                                                                 sequence_pooling_layer_7[0][0]   
__________________________________________________________________________________________________
weighted_sequence_layer (Weight (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 6, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 2, 4)         36          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 9, 4)         16          sequence_max[0][0]               
__________________________________________________________________________________________________
concatenate (Concatenate)       (None, 1, 7)         0           no_mask[0][0]                    
                                                                 no_mask[1][0]                    
                                                                 no_mask[2][0]                    
                                                                 no_mask[3][0]                    
                                                                 no_mask[4][0]                    
                                                                 no_mask[5][0]                    
                                                                 no_mask[6][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         4           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         12          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         32          sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer (Sequenc (None, 1, 4)         0           weighted_sequence_layer[0][0]    2020-05-19 04:12:11.144587: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 AVX512F FMA
2020-05-19 04:12:11.161668: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2095074999 Hz
2020-05-19 04:12:11.161901: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x55e400f7f460 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-19 04:12:11.161917: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version

                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_1 (Seque (None, 1, 4)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_2 (Seque (None, 1, 4)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_3 (Seque (None, 1, 4)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
linear (Linear)                 (None, 1, 1)         0           concatenate[0][0]                
__________________________________________________________________________________________________
afm_layer (AFMLayer)            (None, 1)            52          sparse_emb_sparse_feature_0[0][0]
                                                                 sparse_emb_sparse_feature_1[0][0]
                                                                 sparse_emb_sparse_feature_2[0][0]
                                                                 sequence_pooling_layer[0][0]     
                                                                 sequence_pooling_layer_1[0][0]   
                                                                 sequence_pooling_layer_2[0][0]   
                                                                 sequence_pooling_layer_3[0][0]   
__________________________________________________________________________________________________
no_mask_1 (NoMask)              (None, 1, 1)         0           linear[0][0]                     
__________________________________________________________________________________________________
add (Add)                       (None, 1)            0           afm_layer[0][0]                  
__________________________________________________________________________________________________
add_1 (Add)                     (None, 1, 1)         0           no_mask_1[0][0]                  
                                                                 add[0][0]                        
__________________________________________________________________________________________________
prediction_layer (PredictionLay (None, 1)            1           add_1[0][0]                      
==================================================================================================
Total params: 228
Trainable params: 228
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 2s - loss: 0.2500 - binary_crossentropy: 0.6932500/500 [==============================] - 1s 2ms/sample - loss: 0.2502 - binary_crossentropy: 0.6935 - val_loss: 0.2501 - val_binary_crossentropy: 0.6933

  #### metrics   #################################################### 
{'MSE': 0.24993084398218782}

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
Model: "model"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
weighted_seq (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
weighted_seq_seq_length (InputL [(None, 1)]          0                                            
__________________________________________________________________________________________________
weight (InputLayer)             [(None, 3, 1)]       0                                            
__________________________________________________________________________________________________
sequence_sum (InputLayer)       [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 9)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_1 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_2 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_1 (Weig (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         9           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         4           sequence_max[0][0]               
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         1           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_4 (Seque (None, 1, 1)         0           weighted_sequence_layer_1[0][0]  
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_5 (Seque (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_6 (Seque (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_7 (Seque (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
no_mask (NoMask)                (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_4[0][0]   
                                                                 sequence_pooling_layer_5[0][0]   
                                                                 sequence_pooling_layer_6[0][0]   
                                                                 sequence_pooling_layer_7[0][0]   
__________________________________________________________________________________________________
weighted_sequence_layer (Weight (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 6, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 2, 4)         36          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 9, 4)         16          sequence_max[0][0]               
__________________________________________________________________________________________________
concatenate (Concatenate)       (None, 1, 7)         0           no_mask[0][0]                    
                                                                 no_mask[1][0]                    
                                                                 no_mask[2][0]                    
                                                                 no_mask[3][0]                    
                                                                 no_mask[4][0]                    
                                                                 no_mask[5][0]                    
                                                                 no_mask[6][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         4           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         12          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         32          sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer (Sequenc (None, 1, 4)         0           weighted_sequence_layer[0][0]    
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_1 (Seque (None, 1, 4)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_2 (Seque (None, 1, 4)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_3 (Seque (None, 1, 4)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
linear (Linear)                 (None, 1, 1)         0           concatenate[0][0]                
__________________________________________________________________________________________________
afm_layer (AFMLayer)            (None, 1)            52          sparse_emb_sparse_feature_0[0][0]
                                                                 sparse_emb_sparse_feature_1[0][0]
                                                                 sparse_emb_sparse_feature_2[0][0]
                                                                 sequence_pooling_layer[0][0]     
                                                                 sequence_pooling_layer_1[0][0]   
                                                                 sequence_pooling_layer_2[0][0]   
                                                                 sequence_pooling_layer_3[0][0]   
__________________________________________________________________________________________________
no_mask_1 (NoMask)              (None, 1, 1)         0           linear[0][0]                     
__________________________________________________________________________________________________
add (Add)                       (None, 1)            0           afm_layer[0][0]                  
__________________________________________________________________________________________________
add_1 (Add)                     (None, 1, 1)         0           no_mask_1[0][0]                  
                                                                 add[0][0]                        
__________________________________________________________________________________________________
prediction_layer (PredictionLay (None, 1)            1           add_1[0][0]                      
==================================================================================================
Total params: 228
Trainable params: 228
Non-trainable params: 0
__________________________________________________________________________________________________

  #### Loading params   ############################################## 

  #### Path params   ################################################# 

  #### Model params   ################################################ 
{'model_name': 'AutoInt', 'optimization': 'adam', 'cost': 'mse'} {'dataset_type': 'synthesis', 'sample_size': 8, 'test_size': 0.2, 'dataset_name': 'AutoInt', 'sparse_feature_num': 1, 'dense_feature_num': 1} {'batch_size': 100, 'epochs': 1, 'validation_split': 0.5} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/deepctr/model_AutoInt.h5'}

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/deepctr/layers/interaction.py:565: The name tf.keras.initializers.TruncatedNormal is deprecated. Please use tf.compat.v1.keras.initializers.TruncatedNormal instead.

WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/keras/initializers.py:94: calling TruncatedNormal.__init__ (from tensorflow.python.ops.init_ops) with dtype is deprecated and will be removed in a future version.
Instructions for updating:
Call initializer instance with the dtype argument instead of passing it to the constructor
Model: "model_1"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
weighted_seq (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
weighted_seq_seq_length (InputL [(None, 1)]          0                                            
__________________________________________________________________________________________________
weight (InputLayer)             [(None, 3, 1)]       0                                            
__________________________________________________________________________________________________
sequence_sum (InputLayer)       [(None, 4)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 8)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_3 (Weig (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 4, 4)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 6, 4)         12          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 8, 4)         12          sequence_max[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         32          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_12 (Sequ (None, 1, 4)         0           weighted_sequence_layer_3[0][0]  
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_13 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_14 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_15 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
weighted_sequence_layer_4 (Weig (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 4, 1)         2           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         3           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 8, 1)         3           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_5 (NoMask)              (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_12[0][0]  
                                                                 sequence_pooling_layer_13[0][0]  
                                                                 sequence_pooling_layer_14[0][0]  
                                                                 sequence_pooling_layer_15[0][0]  
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_16 (Sequ (None, 1, 1)         0           weighted_sequence_layer_4[0][0]  
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_17 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_18 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_19 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
concatenate_2 (Concatenate)     (None, 5, 4)         0           no_mask_5[0][0]                  
                                                                 no_mask_5[1][0]                  
                                                                 no_mask_5[2][0]                  
                                                                 no_mask_5[3][0]                  
                                                                 no_mask_5[4][0]                  
__________________________________________________________________________________________________
no_mask_2 (NoMask)              (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_16[0][0]  
                                                                 sequence_pooling_layer_17[0][0]  
                                                                 sequence_pooling_layer_18[0][0]  
                                                                 sequence_pooling_layer_19[0][0]  
__________________________________________________________________________________________________
dense_feature_0 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
interacting_layer (InteractingL (None, 5, 16)        256         concatenate_2[0][0]              
__________________________________________________________________________________________________
concatenate_1 (Concatenate)     (None, 1, 5)         0           no_mask_2[0][0]                  
                                                                 no_mask_2[1][0]                  
                                                                 no_mask_2[2][0]                  
                                                                 no_mask_2[3][0]                  
                                                                 no_mask_2[4][0]                  
__________________________________________________________________________________________________
no_mask_3 (NoMask)              (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
flatten (Flatten)               (None, 80)           0           interacting_layer[0][0]          
__________________________________________________________________________________________________
linear_1 (Linear)               (None, 1)            1           concatenate_1[0][0]              
                                                                 no_mask_3[0][0]                  
__________________________________________________________________________________________________
dense (Dense)                   (None, 1)            80          flatten[0][0]                    
__________________________________________________________________________________________________
no_mask_4 (NoMask)              (None, 1)            0           linear_1[0][0]                   
__________________________________________________________________________________________________
add_4 (Add)                     (None, 1)            0           dense[0][0]                      
                                                                 no_mask_4[0][0]                  
__________________________________________________________________________________________________
prediction_layer_1 (PredictionL (None, 1)            1           add_4[0][0]                      
==================================================================================================
Total params: 428
Trainable params: 428
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 1s - loss: 0.2485 - binary_crossentropy: 0.6900500/500 [==============================] - 1s 2ms/sample - loss: 0.2552 - binary_crossentropy: 0.7038 - val_loss: 0.2538 - val_binary_crossentropy: 0.7010

  #### metrics   #################################################### 
{'MSE': 0.25401544084459277}

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/init_ops.py:97: calling GlorotUniform.__init__ (from tensorflow.python.ops.init_ops) with dtype is deprecated and will be removed in a future version.
Instructions for updating:
Call initializer instance with the dtype argument instead of passing it to the constructor
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/init_ops.py:97: calling Zeros.__init__ (from tensorflow.python.ops.init_ops) with dtype is deprecated and will be removed in a future version.
Instructions for updating:
Call initializer instance with the dtype argument instead of passing it to the constructor
Model: "model_1"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
weighted_seq (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
weighted_seq_seq_length (InputL [(None, 1)]          0                                            
__________________________________________________________________________________________________
weight (InputLayer)             [(None, 3, 1)]       0                                            
__________________________________________________________________________________________________
sequence_sum (InputLayer)       [(None, 4)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 8)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_3 (Weig (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 4, 4)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 6, 4)         12          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 8, 4)         12          sequence_max[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         32          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_12 (Sequ (None, 1, 4)         0           weighted_sequence_layer_3[0][0]  
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_13 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_14 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_15 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
weighted_sequence_layer_4 (Weig (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 4, 1)         2           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         3           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 8, 1)         3           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_5 (NoMask)              (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_12[0][0]  
                                                                 sequence_pooling_layer_13[0][0]  
                                                                 sequence_pooling_layer_14[0][0]  
                                                                 sequence_pooling_layer_15[0][0]  
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_16 (Sequ (None, 1, 1)         0           weighted_sequence_layer_4[0][0]  
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_17 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_18 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_19 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
concatenate_2 (Concatenate)     (None, 5, 4)         0           no_mask_5[0][0]                  
                                                                 no_mask_5[1][0]                  
                                                                 no_mask_5[2][0]                  
                                                                 no_mask_5[3][0]                  
                                                                 no_mask_5[4][0]                  
__________________________________________________________________________________________________
no_mask_2 (NoMask)              (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_16[0][0]  
                                                                 sequence_pooling_layer_17[0][0]  
                                                                 sequence_pooling_layer_18[0][0]  
                                                                 sequence_pooling_layer_19[0][0]  
__________________________________________________________________________________________________
dense_feature_0 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
interacting_layer (InteractingL (None, 5, 16)        256         concatenate_2[0][0]              
__________________________________________________________________________________________________
concatenate_1 (Concatenate)     (None, 1, 5)         0           no_mask_2[0][0]                  
                                                                 no_mask_2[1][0]                  
                                                                 no_mask_2[2][0]                  
                                                                 no_mask_2[3][0]                  
                                                                 no_mask_2[4][0]                  
__________________________________________________________________________________________________
no_mask_3 (NoMask)              (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
flatten (Flatten)               (None, 80)           0           interacting_layer[0][0]          
__________________________________________________________________________________________________
linear_1 (Linear)               (None, 1)            1           concatenate_1[0][0]              
                                                                 no_mask_3[0][0]                  
__________________________________________________________________________________________________
dense (Dense)                   (None, 1)            80          flatten[0][0]                    
__________________________________________________________________________________________________
no_mask_4 (NoMask)              (None, 1)            0           linear_1[0][0]                   
__________________________________________________________________________________________________
add_4 (Add)                     (None, 1)            0           dense[0][0]                      
                                                                 no_mask_4[0][0]                  
__________________________________________________________________________________________________
prediction_layer_1 (PredictionL (None, 1)            1           add_4[0][0]                      
==================================================================================================
Total params: 428
Trainable params: 428
Non-trainable params: 0
__________________________________________________________________________________________________

  #### Loading params   ############################################## 

  #### Path params   ################################################# 

  #### Model params   ################################################ 
{'model_name': 'CCPM', 'optimization': 'adam', 'cost': 'mse'} {'dataset_type': 'synthesis', 'sample_size': 8, 'test_size': 0.2, 'dataset_name': 'CCPM', 'sparse_feature_num': 3, 'dense_feature_num': 0} {'batch_size': 100, 'epochs': 1, 'validation_split': 0.5} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/deepctr/model_CCPM.h5'}

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 
Model: "model_2"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
weighted_seq (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
weighted_seq_seq_length (InputL [(None, 1)]          0                                            
__________________________________________________________________________________________________
weight (InputLayer)             [(None, 3, 1)]       0                                            
__________________________________________________________________________________________________
sequence_sum (InputLayer)       [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 3)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 5)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_1 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_2 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_6 (Weig (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 9, 4)         36          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 3, 4)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 5, 4)         36          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         28          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         32          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         12          sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_24 (Sequ (None, 1, 4)         0           weighted_sequence_layer_6[0][0]  
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_25 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_26 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_27 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
no_mask_11 (NoMask)             (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sparse_emb_sparse_feature_1[0][0]
                                                                 sparse_emb_sparse_feature_2[0][0]
                                                                 sequence_pooling_layer_24[0][0]  
                                                                 sequence_pooling_layer_25[0][0]  
                                                                 sequence_pooling_layer_26[0][0]  
                                                                 sequence_pooling_layer_27[0][0]  
__________________________________________________________________________________________________
concatenate_6 (Concatenate)     (None, 7, 4)         0           no_mask_11[0][0]                 
                                                                 no_mask_11[1][0]                 
                                                                 no_mask_11[2][0]                 
                                                                 no_mask_11[3][0]                 
                                                                 no_mask_11[4][0]                 
                                                                 no_mask_11[5][0]                 
                                                                 no_mask_11[6][0]                 
__________________________________________________________________________________________________
lambda_2 (Lambda)               (None, 7, 4, 1)      0           concatenate_6[0][0]              
__________________________________________________________________________________________________
conv2d (Conv2D)                 (None, 7, 4, 2)      8           lambda_2[0][0]                   
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
k_max_pooling (KMaxPooling)     (None, 3, 4, 2)      0           conv2d[0][0]                     
__________________________________________________________________________________________________
weighted_sequence_layer_7 (Weig (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         9           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         1           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         9           sequence_max[0][0]               
__________________________________________________________________________________________________
conv2d_1 (Conv2D)               (None, 3, 4, 1)      5           k_max_pooling[0][0]              
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_28 (Sequ (None, 1, 1)         0           weighted_sequence_layer_7[0][0]  
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_29 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_30 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_31 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
k_max_pooling_1 (KMaxPooling)   (None, 3, 4, 1)      0           conv2d_1[0][0]                   
__________________________________________________________________________________________________
no_mask_9 (NoMask)              (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_28[0][0]  
                                                                 sequence_pooling_layer_29[0][0]  
                                                                 sequence_pooling_layer_30[0][0]  
                                                                 sequence_pooling_layer_31[0][0]  
__________________________________________________________________________________________________
flatten_3 (Flatten)             (None, 12)           0           k_max_pooling_1[0][0]            
__________________________________________________________________________________________________
concatenate_5 (Concatenate)     (None, 1, 7)         0           no_mask_9[0][0]                  
                                                                 no_mask_9[1][0]                  
                                                                 no_mask_9[2][0]                  
                                                                 no_mask_9[3][0]                  
                                                                 no_mask_9[4][0]                  
                                                                 no_mask_9[5][0]                  
                                                                 no_mask_9[6][0]                  
__________________________________________________________________________________________________
dnn (DNN)                       (None, 32)           416         flatten_3[0][0]                  
__________________________________________________________________________________________________
linear_2 (Linear)               (None, 1, 1)         0           concatenate_5[0][0]              
__________________________________________________________________________________________________
dense_1 (Dense)                 (None, 1)            32          dnn[0][0]                        
__________________________________________________________________________________________________
no_mask_10 (NoMask)             (None, 1, 1)         0           linear_2[0][0]                   
__________________________________________________________________________________________________
add_7 (Add)                     (None, 1, 1)         0           dense_1[0][0]                    
                                                                 no_mask_10[0][0]                 
__________________________________________________________________________________________________
prediction_layer_2 (PredictionL (None, 1)            1           add_7[0][0]                      
==================================================================================================
Total params: 657
Trainable params: 657
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 2s - loss: 0.2500 - binary_crossentropy: 0.6931500/500 [==============================] - 1s 2ms/sample - loss: 0.2501 - binary_crossentropy: 0.6933 - val_loss: 0.2497 - val_binary_crossentropy: 0.6926

  #### metrics   #################################################### 
{'MSE': 0.2496953783341129}

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
Model: "model_2"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
weighted_seq (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
weighted_seq_seq_length (InputL [(None, 1)]          0                                            
__________________________________________________________________________________________________
weight (InputLayer)             [(None, 3, 1)]       0                                            
__________________________________________________________________________________________________
sequence_sum (InputLayer)       [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 3)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 5)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_1 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_2 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_6 (Weig (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 9, 4)         36          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 3, 4)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 5, 4)         36          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         28          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         32          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         12          sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_24 (Sequ (None, 1, 4)         0           weighted_sequence_layer_6[0][0]  
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_25 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_26 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_27 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
no_mask_11 (NoMask)             (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sparse_emb_sparse_feature_1[0][0]
                                                                 sparse_emb_sparse_feature_2[0][0]
                                                                 sequence_pooling_layer_24[0][0]  
                                                                 sequence_pooling_layer_25[0][0]  
                                                                 sequence_pooling_layer_26[0][0]  
                                                                 sequence_pooling_layer_27[0][0]  
__________________________________________________________________________________________________
concatenate_6 (Concatenate)     (None, 7, 4)         0           no_mask_11[0][0]                 
                                                                 no_mask_11[1][0]                 
                                                                 no_mask_11[2][0]                 
                                                                 no_mask_11[3][0]                 
                                                                 no_mask_11[4][0]                 
                                                                 no_mask_11[5][0]                 
                                                                 no_mask_11[6][0]                 
__________________________________________________________________________________________________
lambda_2 (Lambda)               (None, 7, 4, 1)      0           concatenate_6[0][0]              
__________________________________________________________________________________________________
conv2d (Conv2D)                 (None, 7, 4, 2)      8           lambda_2[0][0]                   
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
k_max_pooling (KMaxPooling)     (None, 3, 4, 2)      0           conv2d[0][0]                     
__________________________________________________________________________________________________
weighted_sequence_layer_7 (Weig (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         9           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         1           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         9           sequence_max[0][0]               
__________________________________________________________________________________________________
conv2d_1 (Conv2D)               (None, 3, 4, 1)      5           k_max_pooling[0][0]              
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_28 (Sequ (None, 1, 1)         0           weighted_sequence_layer_7[0][0]  
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_29 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_30 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_31 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
k_max_pooling_1 (KMaxPooling)   (None, 3, 4, 1)      0           conv2d_1[0][0]                   
__________________________________________________________________________________________________
no_mask_9 (NoMask)              (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_28[0][0]  
                                                                 sequence_pooling_layer_29[0][0]  
                                                                 sequence_pooling_layer_30[0][0]  
                                                                 sequence_pooling_layer_31[0][0]  
__________________________________________________________________________________________________
flatten_3 (Flatten)             (None, 12)           0           k_max_pooling_1[0][0]            
__________________________________________________________________________________________________
concatenate_5 (Concatenate)     (None, 1, 7)         0           no_mask_9[0][0]                  
                                                                 no_mask_9[1][0]                  
                                                                 no_mask_9[2][0]                  
                                                                 no_mask_9[3][0]                  
                                                                 no_mask_9[4][0]                  
                                                                 no_mask_9[5][0]                  
                                                                 no_mask_9[6][0]                  
__________________________________________________________________________________________________
dnn (DNN)                       (None, 32)           416         flatten_3[0][0]                  
__________________________________________________________________________________________________
linear_2 (Linear)               (None, 1, 1)         0           concatenate_5[0][0]              
__________________________________________________________________________________________________
dense_1 (Dense)                 (None, 1)            32          dnn[0][0]                        
__________________________________________________________________________________________________
no_mask_10 (NoMask)             (None, 1, 1)         0           linear_2[0][0]                   
__________________________________________________________________________________________________
add_7 (Add)                     (None, 1, 1)         0           dense_1[0][0]                    
                                                                 no_mask_10[0][0]                 
__________________________________________________________________________________________________
prediction_layer_2 (PredictionL (None, 1)            1           add_7[0][0]                      
==================================================================================================
Total params: 657
Trainable params: 657
Non-trainable params: 0
__________________________________________________________________________________________________

  #### Loading params   ############################################## 

  #### Path params   ################################################# 

  #### Model params   ################################################ 
{'model_name': 'DCN', 'optimization': 'adam', 'cost': 'mse'} {'dataset_type': 'synthesis', 'sample_size': 8, 'test_size': 0.2, 'dataset_name': 'DCN', 'sparse_feature_num': 3, 'dense_feature_num': 3} {'batch_size': 100, 'epochs': 1, 'validation_split': 0.5} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/deepctr/model_DCN.h5'}

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 
Model: "model_3"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
weighted_seq (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
weighted_seq_seq_length (InputL [(None, 1)]          0                                            
__________________________________________________________________________________________________
weight (InputLayer)             [(None, 3, 1)]       0                                            
__________________________________________________________________________________________________
sequence_sum (InputLayer)       [(None, 1)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_1 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_2 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_9 (Weig (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 1, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 5, 4)         16          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 3, 4)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         20          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         36          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         24          sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_36 (Sequ (None, 1, 4)         0           weighted_sequence_layer_9[0][0]  
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_37 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_38 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_39 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
dense_feature_0 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
dense_feature_1 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
dense_feature_2 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
no_mask_15 (NoMask)             (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sparse_emb_sparse_feature_1[0][0]
                                                                 sparse_emb_sparse_feature_2[0][0]
                                                                 sequence_pooling_layer_36[0][0]  
                                                                 sequence_pooling_layer_37[0][0]  
                                                                 sequence_pooling_layer_38[0][0]  
                                                                 sequence_pooling_layer_39[0][0]  
__________________________________________________________________________________________________
no_mask_16 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
                                                                 dense_feature_1[0][0]            
                                                                 dense_feature_2[0][0]            
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
concatenate_9 (Concatenate)     (None, 1, 28)        0           no_mask_15[0][0]                 
                                                                 no_mask_15[1][0]                 
                                                                 no_mask_15[2][0]                 
                                                                 no_mask_15[3][0]                 
                                                                 no_mask_15[4][0]                 
                                                                 no_mask_15[5][0]                 
                                                                 no_mask_15[6][0]                 
__________________________________________________________________________________________________
concatenate_10 (Concatenate)    (None, 3)            0           no_mask_16[0][0]                 
                                                                 no_mask_16[1][0]                 
                                                                 no_mask_16[2][0]                 
__________________________________________________________________________________________________
weighted_sequence_layer_10 (Wei (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         2           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_4 (Flatten)             (None, 28)           0           concatenate_9[0][0]              
__________________________________________________________________________________________________
flatten_5 (Flatten)             (None, 3)            0           concatenate_10[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         9           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_40 (Sequ (None, 1, 1)         0           weighted_sequence_layer_10[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_41 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_42 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_43 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
no_mask_17 (NoMask)             multiple             0           flatten_4[0][0]                  
                                                                 flatten_5[0][0]                  
__________________________________________________________________________________________________
no_mask_12 (NoMask)             (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_40[0][0]  
                                                                 sequence_pooling_layer_41[0][0]  
                                                                 sequence_pooling_layer_42[0][0]  
                                                                 sequence_pooling_layer_43[0][0]  
__________________________________________________________________________________________________
no_mask_13 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
                                                                 dense_feature_1[0][0]            
                                                                 dense_feature_2[0][0]            
__________________________________________________________________________________________________
concatenate_11 (Concatenate)    (None, 31)           0           no_mask_17[0][0]                 
                                                                 no_mask_17[1][0]                 
__________________________________________________________________________________________________
concatenate_7 (Concatenate)     (None, 1, 7)         0           no_mask_12[0][0]                 
                                                                 no_mask_12[1][0]                 
                                                                 no_mask_12[2][0]                 
                                                                 no_mask_12[3][0]                 
                                                                 no_mask_12[4][0]                 
                                                                 no_mask_12[5][0]                 
                                                                 no_mask_12[6][0]                 
__________________________________________________________________________________________________
concatenate_8 (Concatenate)     (None, 3)            0           no_mask_13[0][0]                 
                                                                 no_mask_13[1][0]                 
                                                                 no_mask_13[2][0]                 
__________________________________________________________________________________________________
dnn_1 (DNN)                     (None, 8)            256         concatenate_11[0][0]             
__________________________________________________________________________________________________
linear_3 (Linear)               (None, 1)            3           concatenate_7[0][0]              
                                                                 concatenate_8[0][0]              
__________________________________________________________________________________________________
dense_2 (Dense)                 (None, 1)            8           dnn_1[0][0]                      
__________________________________________________________________________________________________
no_mask_14 (NoMask)             (None, 1)            0           linear_3[0][0]                   
__________________________________________________________________________________________________
add_10 (Add)                    (None, 1)            0           dense_2[0][0]                    
                                                                 no_mask_14[0][0]                 
__________________________________________________________________________________________________
prediction_layer_3 (PredictionL (None, 1)            1           add_10[0][0]                     
==================================================================================================
Total params: 448
Trainable params: 448
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 2s - loss: 0.3430 - binary_crossentropy: 1.6839500/500 [==============================] - 1s 3ms/sample - loss: 0.3222 - binary_crossentropy: 1.8992 - val_loss: 0.3117 - val_binary_crossentropy: 1.7386

  #### metrics   #################################################### 
{'MSE': 0.3134412010596837}

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
Model: "model_3"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
weighted_seq (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
weighted_seq_seq_length (InputL [(None, 1)]          0                                            
__________________________________________________________________________________________________
weight (InputLayer)             [(None, 3, 1)]       0                                            
__________________________________________________________________________________________________
sequence_sum (InputLayer)       [(None, 1)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_1 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_2 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_9 (Weig (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 1, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 5, 4)         16          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 3, 4)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         20          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         36          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         24          sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_36 (Sequ (None, 1, 4)         0           weighted_sequence_layer_9[0][0]  
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_37 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_38 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_39 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
dense_feature_0 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
dense_feature_1 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
dense_feature_2 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
no_mask_15 (NoMask)             (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sparse_emb_sparse_feature_1[0][0]
                                                                 sparse_emb_sparse_feature_2[0][0]
                                                                 sequence_pooling_layer_36[0][0]  
                                                                 sequence_pooling_layer_37[0][0]  
                                                                 sequence_pooling_layer_38[0][0]  
                                                                 sequence_pooling_layer_39[0][0]  
__________________________________________________________________________________________________
no_mask_16 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
                                                                 dense_feature_1[0][0]            
                                                                 dense_feature_2[0][0]            
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
concatenate_9 (Concatenate)     (None, 1, 28)        0           no_mask_15[0][0]                 
                                                                 no_mask_15[1][0]                 
                                                                 no_mask_15[2][0]                 
                                                                 no_mask_15[3][0]                 
                                                                 no_mask_15[4][0]                 
                                                                 no_mask_15[5][0]                 
                                                                 no_mask_15[6][0]                 
__________________________________________________________________________________________________
concatenate_10 (Concatenate)    (None, 3)            0           no_mask_16[0][0]                 
                                                                 no_mask_16[1][0]                 
                                                                 no_mask_16[2][0]                 
__________________________________________________________________________________________________
weighted_sequence_layer_10 (Wei (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         2           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_4 (Flatten)             (None, 28)           0           concatenate_9[0][0]              
__________________________________________________________________________________________________
flatten_5 (Flatten)             (None, 3)            0           concatenate_10[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         9           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_40 (Sequ (None, 1, 1)         0           weighted_sequence_layer_10[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_41 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_42 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_43 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
no_mask_17 (NoMask)             multiple             0           flatten_4[0][0]                  
                                                                 flatten_5[0][0]                  
__________________________________________________________________________________________________
no_mask_12 (NoMask)             (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_40[0][0]  
                                                                 sequence_pooling_layer_41[0][0]  
                                                                 sequence_pooling_layer_42[0][0]  
                                                                 sequence_pooling_layer_43[0][0]  
__________________________________________________________________________________________________
no_mask_13 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
                                                                 dense_feature_1[0][0]            
                                                                 dense_feature_2[0][0]            
__________________________________________________________________________________________________
concatenate_11 (Concatenate)    (None, 31)           0           no_mask_17[0][0]                 
                                                                 no_mask_17[1][0]                 
__________________________________________________________________________________________________
concatenate_7 (Concatenate)     (None, 1, 7)         0           no_mask_12[0][0]                 
                                                                 no_mask_12[1][0]                 
                                                                 no_mask_12[2][0]                 
                                                                 no_mask_12[3][0]                 
                                                                 no_mask_12[4][0]                 
                                                                 no_mask_12[5][0]                 
                                                                 no_mask_12[6][0]                 
__________________________________________________________________________________________________
concatenate_8 (Concatenate)     (None, 3)            0           no_mask_13[0][0]                 
                                                                 no_mask_13[1][0]                 
                                                                 no_mask_13[2][0]                 
__________________________________________________________________________________________________
dnn_1 (DNN)                     (None, 8)            256         concatenate_11[0][0]             
__________________________________________________________________________________________________
linear_3 (Linear)               (None, 1)            3           concatenate_7[0][0]              
                                                                 concatenate_8[0][0]              
__________________________________________________________________________________________________
dense_2 (Dense)                 (None, 1)            8           dnn_1[0][0]                      
__________________________________________________________________________________________________
no_mask_14 (NoMask)             (None, 1)            0           linear_3[0][0]                   
__________________________________________________________________________________________________
add_10 (Add)                    (None, 1)            0           dense_2[0][0]                    
                                                                 no_mask_14[0][0]                 
__________________________________________________________________________________________________
prediction_layer_3 (PredictionL (None, 1)            1           add_10[0][0]                     
==================================================================================================
Total params: 448
Trainable params: 448
Non-trainable params: 0
__________________________________________________________________________________________________

  #### Loading params   ############################################## 

  #### Path params   ################################################# 

  #### Model params   ################################################ 
{'model_name': 'DeepFM', 'optimization': 'adam', 'cost': 'mse'} {'dataset_type': 'synthesis', 'sample_size': 8, 'test_size': 0.2, 'dataset_name': 'DeepFM', 'sparse_feature_num': 1, 'dense_feature_num': 1} {'batch_size': 100, 'epochs': 1, 'validation_split': 0.5} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/deepctr/model_DeepFM.h5'}

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 
Model: "model_4"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
weighted_seq (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
weighted_seq_seq_length (InputL [(None, 1)]          0                                            
__________________________________________________________________________________________________
weight (InputLayer)             [(None, 3, 1)]       0                                            
__________________________________________________________________________________________________
sequence_sum (InputLayer)       [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 9)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_12 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 6, 4)         16          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 2, 4)         20          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 9, 4)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         32          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_48 (Sequ (None, 1, 4)         0           weighted_sequence_layer_12[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_49 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_50 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_51 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
dense_feature_0 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
no_mask_22 (NoMask)             (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_48[0][0]  
                                                                 sequence_pooling_layer_49[0][0]  
                                                                 sequence_pooling_layer_50[0][0]  
                                                                 sequence_pooling_layer_51[0][0]  
__________________________________________________________________________________________________
weighted_sequence_layer_13 (Wei (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         5           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         2           sequence_max[0][0]               
__________________________________________________________________________________________________
concatenate_14 (Concatenate)    (None, 1, 20)        0           no_mask_22[0][0]                 
                                                                 no_mask_22[1][0]                 
                                                                 no_mask_22[2][0]                 
                                                                 no_mask_22[3][0]                 
                                                                 no_mask_22[4][0]                 
__________________________________________________________________________________________________
no_mask_23 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_52 (Sequ (None, 1, 1)         0           weighted_sequence_layer_13[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_53 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_54 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_55 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
flatten_6 (Flatten)             (None, 20)           0           concatenate_14[0][0]             
__________________________________________________________________________________________________
flatten_7 (Flatten)             (None, 1)            0           no_mask_23[0][0]                 
__________________________________________________________________________________________________
no_mask_18 (NoMask)             (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_52[0][0]  
                                                                 sequence_pooling_layer_53[0][0]  
                                                                 sequence_pooling_layer_54[0][0]  
                                                                 sequence_pooling_layer_55[0][0]  
__________________________________________________________________________________________________
no_mask_21 (NoMask)             (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_48[0][0]  
                                                                 sequence_pooling_layer_49[0][0]  
                                                                 sequence_pooling_layer_50[0][0]  
                                                                 sequence_pooling_layer_51[0][0]  
__________________________________________________________________________________________________
no_mask_24 (NoMask)             multiple             0           flatten_6[0][0]                  
                                                                 flatten_7[0][0]                  
__________________________________________________________________________________________________
concatenate_12 (Concatenate)    (None, 1, 5)         0           no_mask_18[0][0]                 
                                                                 no_mask_18[1][0]                 
                                                                 no_mask_18[2][0]                 
                                                                 no_mask_18[3][0]                 
                                                                 no_mask_18[4][0]                 
__________________________________________________________________________________________________
no_mask_19 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
concatenate_13 (Concatenate)    (None, 5, 4)         0           no_mask_21[0][0]                 
                                                                 no_mask_21[1][0]                 
                                                                 no_mask_21[2][0]                 
                                                                 no_mask_21[3][0]                 
                                                                 no_mask_21[4][0]                 
__________________________________________________________________________________________________
concatenate_15 (Concatenate)    (None, 21)           0           no_mask_24[0][0]                 
                                                                 no_mask_24[1][0]                 
__________________________________________________________________________________________________
linear_4 (Linear)               (None, 1)            1           concatenate_12[0][0]             
                                                                 no_mask_19[0][0]                 
__________________________________________________________________________________________________
fm (FM)                         (None, 1)            0           concatenate_13[0][0]             
__________________________________________________________________________________________________
dnn_2 (DNN)                     (None, 2)            44          concatenate_15[0][0]             
__________________________________________________________________________________________________
no_mask_20 (NoMask)             (None, 1)            0           linear_4[0][0]                   
__________________________________________________________________________________________________
add_13 (Add)                    (None, 1)            0           fm[0][0]                         
__________________________________________________________________________________________________
dense_3 (Dense)                 (None, 1)            2           dnn_2[0][0]                      
__________________________________________________________________________________________________
add_14 (Add)                    (None, 1)            0           no_mask_20[0][0]                 
                                                                 add_13[0][0]                     
                                                                 dense_3[0][0]                    
__________________________________________________________________________________________________
prediction_layer_4 (PredictionL (None, 1)            1           add_14[0][0]                     
==================================================================================================
Total params: 153
Trainable params: 153
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 2s - loss: 0.3062 - binary_crossentropy: 0.8208500/500 [==============================] - 2s 3ms/sample - loss: 0.2911 - binary_crossentropy: 0.8104 - val_loss: 0.2652 - val_binary_crossentropy: 0.7270

  #### metrics   #################################################### 
{'MSE': 0.27420950442226094}

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
Model: "model_4"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
weighted_seq (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
weighted_seq_seq_length (InputL [(None, 1)]          0                                            
__________________________________________________________________________________________________
weight (InputLayer)             [(None, 3, 1)]       0                                            
__________________________________________________________________________________________________
sequence_sum (InputLayer)       [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 9)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_12 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 6, 4)         16          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 2, 4)         20          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 9, 4)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         32          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_48 (Sequ (None, 1, 4)         0           weighted_sequence_layer_12[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_49 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_50 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_51 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
dense_feature_0 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
no_mask_22 (NoMask)             (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_48[0][0]  
                                                                 sequence_pooling_layer_49[0][0]  
                                                                 sequence_pooling_layer_50[0][0]  
                                                                 sequence_pooling_layer_51[0][0]  
__________________________________________________________________________________________________
weighted_sequence_layer_13 (Wei (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         5           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         2           sequence_max[0][0]               
__________________________________________________________________________________________________
concatenate_14 (Concatenate)    (None, 1, 20)        0           no_mask_22[0][0]                 
                                                                 no_mask_22[1][0]                 
                                                                 no_mask_22[2][0]                 
                                                                 no_mask_22[3][0]                 
                                                                 no_mask_22[4][0]                 
__________________________________________________________________________________________________
no_mask_23 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_52 (Sequ (None, 1, 1)         0           weighted_sequence_layer_13[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_53 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_54 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_55 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
flatten_6 (Flatten)             (None, 20)           0           concatenate_14[0][0]             
__________________________________________________________________________________________________
flatten_7 (Flatten)             (None, 1)            0           no_mask_23[0][0]                 
__________________________________________________________________________________________________
no_mask_18 (NoMask)             (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_52[0][0]  
                                                                 sequence_pooling_layer_53[0][0]  
                                                                 sequence_pooling_layer_54[0][0]  
                                                                 sequence_pooling_layer_55[0][0]  
__________________________________________________________________________________________________
no_mask_21 (NoMask)             (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_48[0][0]  
                                                                 sequence_pooling_layer_49[0][0]  
                                                                 sequence_pooling_layer_50[0][0]  
                                                                 sequence_pooling_layer_51[0][0]  
__________________________________________________________________________________________________
no_mask_24 (NoMask)             multiple             0           flatten_6[0][0]                  
                                                                 flatten_7[0][0]                  
__________________________________________________________________________________________________
concatenate_12 (Concatenate)    (None, 1, 5)         0           no_mask_18[0][0]                 
                                                                 no_mask_18[1][0]                 
                                                                 no_mask_18[2][0]                 
                                                                 no_mask_18[3][0]                 
                                                                 no_mask_18[4][0]                 
__________________________________________________________________________________________________
no_mask_19 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
concatenate_13 (Concatenate)    (None, 5, 4)         0           no_mask_21[0][0]                 
                                                                 no_mask_21[1][0]                 
                                                                 no_mask_21[2][0]                 
                                                                 no_mask_21[3][0]                 
                                                                 no_mask_21[4][0]                 
__________________________________________________________________________________________________
concatenate_15 (Concatenate)    (None, 21)           0           no_mask_24[0][0]                 
                                                                 no_mask_24[1][0]                 
__________________________________________________________________________________________________
linear_4 (Linear)               (None, 1)            1           concatenate_12[0][0]             
                                                                 no_mask_19[0][0]                 
__________________________________________________________________________________________________
fm (FM)                         (None, 1)            0           concatenate_13[0][0]             
__________________________________________________________________________________________________
dnn_2 (DNN)                     (None, 2)            44          concatenate_15[0][0]             
__________________________________________________________________________________________________
no_mask_20 (NoMask)             (None, 1)            0           linear_4[0][0]                   
__________________________________________________________________________________________________
add_13 (Add)                    (None, 1)            0           fm[0][0]                         
__________________________________________________________________________________________________
dense_3 (Dense)                 (None, 1)            2           dnn_2[0][0]                      
__________________________________________________________________________________________________
add_14 (Add)                    (None, 1)            0           no_mask_20[0][0]                 
                                                                 add_13[0][0]                     
                                                                 dense_3[0][0]                    
__________________________________________________________________________________________________
prediction_layer_4 (PredictionL (None, 1)            1           add_14[0][0]                     
==================================================================================================
Total params: 153
Trainable params: 153
Non-trainable params: 0
__________________________________________________________________________________________________

  #### Loading params   ############################################## 

  #### Path params   ################################################# 

  #### Model params   ################################################ 
{'model_name': 'DIEN', 'optimization': 'adam', 'cost': 'mse'} {'dataset_type': 'synthesis', 'sample_size': 8, 'test_size': 0.2, 'dataset_name': 'DIEN'} {'batch_size': 100, 'epochs': 1, 'validation_split': 0.5} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/deepctr/model_DIEN.h5'}

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/deepctr/layers/sequence.py:724: GRUCell.__init__ (from tensorflow.python.ops.rnn_cell_impl) is deprecated and will be removed in a future version.
Instructions for updating:
This class is equivalent as tf.keras.layers.GRUCell, and will be replaced by that in Tensorflow 2.0.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/autograph/converters/directives.py:119: The name tf.AUTO_REUSE is deprecated. Please use tf.compat.v1.AUTO_REUSE instead.

WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/deepctr/contrib/rnn.py:798: to_int32 (from tensorflow.python.ops.math_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use `tf.cast` instead.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/rnn_cell_impl.py:559: Layer.add_variable (from tensorflow.python.keras.engine.base_layer) is deprecated and will be removed in a future version.
Instructions for updating:
Please use `layer.add_weight` method instead.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/rnn_cell_impl.py:565: calling Constant.__init__ (from tensorflow.python.ops.init_ops) with dtype is deprecated and will be removed in a future version.
Instructions for updating:
Call initializer instance with the dtype argument instead of passing it to the constructor
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/deepctr/models/dien.py:282: The name tf.keras.backend.get_session is deprecated. Please use tf.compat.v1.keras.backend.get_session instead.

WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/deepctr/models/dien.py:282: The name tf.global_variables_initializer is deprecated. Please use tf.compat.v1.global_variables_initializer instead.

Model: "model_5"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
item (InputLayer)               [(None, 1)]          0                                            
__________________________________________________________________________________________________
item_gender (InputLayer)        [(None, 1)]          0                                            
__________________________________________________________________________________________________
hist_item (InputLayer)          [(None, 4)]          0                                            
__________________________________________________________________________________________________
hist_item_gender (InputLayer)   [(None, 4)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_hist_item (Embed multiple             32          item[0][0]                       
                                                                 hist_item[0][0]                  
                                                                 item[0][0]                       
__________________________________________________________________________________________________
sparse_seq_emb_hist_item_gender multiple             12          item_gender[0][0]                
                                                                 hist_item_gender[0][0]           
                                                                 item_gender[0][0]                
__________________________________________________________________________________________________
no_mask_25 (NoMask)             multiple             0           sparse_seq_emb_hist_item[1][0]   
                                                                 sparse_seq_emb_hist_item_gender[1
__________________________________________________________________________________________________
user (InputLayer)               [(None, 1)]          0                                            
__________________________________________________________________________________________________
gender (InputLayer)             [(None, 1)]          0                                            
__________________________________________________________________________________________________
concatenate_16 (Concatenate)    (None, 4, 12)        0           no_mask_25[0][0]                 
                                                                 no_mask_25[1][0]                 
__________________________________________________________________________________________________
seq_length (InputLayer)         [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_emb_user (Embedding)     (None, 1, 1)         3           user[0][0]                       
__________________________________________________________________________________________________
sparse_emb_gender (Embedding)   (None, 1, 1)         2           gender[0][0]                     
__________________________________________________________________________________________________
no_mask_27 (NoMask)             multiple             0           sparse_seq_emb_hist_item[0][0]   
                                                                 sparse_seq_emb_hist_item_gender[0
__________________________________________________________________________________________________
gru1 (DynamicGRU)               (None, 4, 12)        900         concatenate_16[0][0]             
                                                                 seq_length[0][0]                 
__________________________________________________________________________________________________
no_mask_26 (NoMask)             multiple             0           sparse_emb_user[0][0]            
                                                                 sparse_emb_gender[0][0]          
                                                                 sparse_seq_emb_hist_item[2][0]   
                                                                 sparse_seq_emb_hist_item_gender[2
__________________________________________________________________________________________________
concatenate_18 (Concatenate)    (None, 1, 12)        0           no_mask_27[0][0]                 
                                                                 no_mask_27[1][0]                 
__________________________________________________________________________________________________
gru2 (DynamicGRU)               (None, 4, 12)        900         gru1[0][0]                       
                                                                 seq_length[0][0]                 
__________________________________________________________________________________________________
concatenate_17 (Concatenate)    (None, 1, 14)        0           no_mask_26[0][0]                 
                                                                 no_mask_26[1][0]                 
                                                                 no_mask_26[2][0]                 
                                                                 no_mask_26[3][0]                 
__________________________________________________________________________________________________
attention_sequence_pooling_laye (None, 1, 12)        4433        concatenate_18[0][0]             
                                                                 gru2[0][0]                       
                                                                 seq_length[0][0]                 
__________________________________________________________________________________________________
concatenate_19 (Concatenate)    (None, 1, 26)        0           concatenate_17[0][0]             
                                                                 attention_sequence_pooling_layer[
__________________________________________________________________________________________________
flatten_8 (Flatten)             (None, 26)           0           concatenate_19[0][0]             
__________________________________________________________________________________________________
score (InputLayer)              [(None, 1)]          0                                            
__________________________________________________________________________________________________
no_mask_28 (NoMask)             (None, 26)           0           flatten_8[0][0]                  
__________________________________________________________________________________________________
no_mask_29 (NoMask)             (None, 1)            0           score[0][0]                      
__________________________________________________________________________________________________
flatten_9 (Flatten)             (None, 26)           0           no_mask_28[0][0]                 
__________________________________________________________________________________________________
flatten_10 (Flatten)            (None, 1)            0           no_mask_29[0][0]                 
__________________________________________________________________________________________________
no_mask_30 (NoMask)             multiple             0           flatten_9[0][0]                  
                                                                 flatten_10[0][0]                 
__________________________________________________________________________________________________
concatenate_20 (Concatenate)    (None, 27)           0           no_mask_30[0][0]                 
                                                                 no_mask_30[1][0]                 
__________________________________________________________________________________________________
dnn_4 (DNN)                     (None, 4)            152         concatenate_20[0][0]             2020-05-19 04:13:31.655294: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 04:13:31.657371: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 04:13:31.663122: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-19 04:13:31.673602: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-19 04:13:31.675376: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-19 04:13:31.677043: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 04:13:31.678525: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

__________________________________________________________________________________________________
dense_4 (Dense)                 (None, 1)            4           dnn_4[0][0]                      
__________________________________________________________________________________________________
prediction_layer_5 (PredictionL (None, 1)            1           dense_4[0][0]                    
==================================================================================================
Total params: 6,439
Trainable params: 6,279
Non-trainable params: 160
__________________________________________________________________________________________________
Train on 1 samples, validate on 2 samples
1/1 [==============================] - 3s 3s/sample - loss: 0.2500 - binary_crossentropy: 0.6931 - val_loss: 0.2504 - val_binary_crossentropy: 0.6940
2020-05-19 04:13:32.960395: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 04:13:32.962146: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 04:13:32.966557: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-19 04:13:32.975475: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-19 04:13:32.977016: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-19 04:13:32.978411: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 04:13:32.979701: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

  #### metrics   #################################################### 
{'MSE': 0.25045907065863116}

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
Model: "model_5"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
item (InputLayer)               [(None, 1)]          0                                            
__________________________________________________________________________________________________
item_gender (InputLayer)        [(None, 1)]          0                                            
__________________________________________________________________________________________________
hist_item (InputLayer)          [(None, 4)]          0                                            
__________________________________________________________________________________________________
hist_item_gender (InputLayer)   [(None, 4)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_hist_item (Embed multiple             32          item[0][0]                       
                                                                 hist_item[0][0]                  
                                                                 item[0][0]                       
__________________________________________________________________________________________________
sparse_seq_emb_hist_item_gender multiple             12          item_gender[0][0]                
                                                                 hist_item_gender[0][0]           
                                                                 item_gender[0][0]                
__________________________________________________________________________________________________
no_mask_25 (NoMask)             multiple             0           sparse_seq_emb_hist_item[1][0]   
                                                                 sparse_seq_emb_hist_item_gender[1
__________________________________________________________________________________________________
user (InputLayer)               [(None, 1)]          0                                            
__________________________________________________________________________________________________
gender (InputLayer)             [(None, 1)]          0                                            
__________________________________________________________________________________________________
concatenate_16 (Concatenate)    (None, 4, 12)        0           no_mask_25[0][0]                 
                                                                 no_mask_25[1][0]                 
__________________________________________________________________________________________________
seq_length (InputLayer)         [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_emb_user (Embedding)     (None, 1, 1)         3           user[0][0]                       
__________________________________________________________________________________________________
sparse_emb_gender (Embedding)   (None, 1, 1)         2           gender[0][0]                     
__________________________________________________________________________________________________
no_mask_27 (NoMask)             multiple             0           sparse_seq_emb_hist_item[0][0]   
                                                                 sparse_seq_emb_hist_item_gender[0
__________________________________________________________________________________________________
gru1 (DynamicGRU)               (None, 4, 12)        900         concatenate_16[0][0]             
                                                                 seq_length[0][0]                 
__________________________________________________________________________________________________
no_mask_26 (NoMask)             multiple             0           sparse_emb_user[0][0]            
                                                                 sparse_emb_gender[0][0]          
                                                                 sparse_seq_emb_hist_item[2][0]   
                                                                 sparse_seq_emb_hist_item_gender[2
__________________________________________________________________________________________________
concatenate_18 (Concatenate)    (None, 1, 12)        0           no_mask_27[0][0]                 
                                                                 no_mask_27[1][0]                 
__________________________________________________________________________________________________
gru2 (DynamicGRU)               (None, 4, 12)        900         gru1[0][0]                       
                                                                 seq_length[0][0]                 
__________________________________________________________________________________________________
concatenate_17 (Concatenate)    (None, 1, 14)        0           no_mask_26[0][0]                 
                                                                 no_mask_26[1][0]                 
                                                                 no_mask_26[2][0]                 
                                                                 no_mask_26[3][0]                 
__________________________________________________________________________________________________
attention_sequence_pooling_laye (None, 1, 12)        4433        concatenate_18[0][0]             
                                                                 gru2[0][0]                       
                                                                 seq_length[0][0]                 
__________________________________________________________________________________________________
concatenate_19 (Concatenate)    (None, 1, 26)        0           concatenate_17[0][0]             
                                                                 attention_sequence_pooling_layer[
__________________________________________________________________________________________________
flatten_8 (Flatten)             (None, 26)           0           concatenate_19[0][0]             
__________________________________________________________________________________________________
score (InputLayer)              [(None, 1)]          0                                            
__________________________________________________________________________________________________
no_mask_28 (NoMask)             (None, 26)           0           flatten_8[0][0]                  
__________________________________________________________________________________________________
no_mask_29 (NoMask)             (None, 1)            0           score[0][0]                      
__________________________________________________________________________________________________
flatten_9 (Flatten)             (None, 26)           0           no_mask_28[0][0]                 
__________________________________________________________________________________________________
flatten_10 (Flatten)            (None, 1)            0           no_mask_29[0][0]                 
__________________________________________________________________________________________________
no_mask_30 (NoMask)             multiple             0           flatten_9[0][0]                  
                                                                 flatten_10[0][0]                 
__________________________________________________________________________________________________
concatenate_20 (Concatenate)    (None, 27)           0           no_mask_30[0][0]                 
                                                                 no_mask_30[1][0]                 
__________________________________________________________________________________________________
dnn_4 (DNN)                     (None, 4)            152         concatenate_20[0][0]             
__________________________________________________________________________________________________
dense_4 (Dense)                 (None, 1)            4           dnn_4[0][0]                      
__________________________________________________________________________________________________
prediction_layer_5 (PredictionL (None, 1)            1           dense_4[0][0]                    
==================================================================================================
Total params: 6,439
Trainable params: 6,279
Non-trainable params: 160
__________________________________________________________________________________________________

  #### Loading params   ############################################## 

  #### Path params   ################################################# 

  #### Model params   ################################################ 
{'model_name': 'DIN', 'optimization': 'adam', 'cost': 'mse'} {'dataset_type': 'synthesis', 'sample_size': 8, 'test_size': 0.2, 'dataset_name': 'DIN'} {'batch_size': 100, 'epochs': 1, 'validation_split': 0.5} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/deepctr/model_DIN.h5'}

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 
2020-05-19 04:13:56.306768: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 04:13:56.308134: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 04:13:56.311799: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-19 04:13:56.317969: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-19 04:13:56.319000: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-19 04:13:56.319964: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 04:13:56.320875: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
Model: "model_6"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
user (InputLayer)               [(None, 1)]          0                                            
__________________________________________________________________________________________________
gender (InputLayer)             [(None, 1)]          0                                            
__________________________________________________________________________________________________
item (InputLayer)               [(None, 1)]          0                                            
__________________________________________________________________________________________________
item_gender (InputLayer)        [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_emb_user (Embedding)     (None, 1, 4)         12          user[0][0]                       
__________________________________________________________________________________________________
sparse_emb_gender (Embedding)   (None, 1, 4)         8           gender[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_hist_item (Embed multiple             32          item[0][0]                       
                                                                 hist_item[0][0]                  
                                                                 item[0][0]                       
__________________________________________________________________________________________________
sparse_seq_emb_hist_item_gender multiple             12          item_gender[0][0]                
                                                                 hist_item_gender[0][0]           
                                                                 item_gender[0][0]                
__________________________________________________________________________________________________
hist_item (InputLayer)          [(None, 4)]          0                                            
__________________________________________________________________________________________________
hist_item_gender (InputLayer)   [(None, 4)]          0                                            
__________________________________________________________________________________________________
no_mask_31 (NoMask)             multiple             0           sparse_emb_user[0][0]            
                                                                 sparse_emb_gender[0][0]          
                                                                 sparse_seq_emb_hist_item[2][0]   
                                                                 sparse_seq_emb_hist_item_gender[2
__________________________________________________________________________________________________
concatenate_22 (Concatenate)    (None, 1, 20)        0           no_mask_31[0][0]                 
                                                                 no_mask_31[1][0]                 
                                                                 no_mask_31[2][0]                 
                                                                 no_mask_31[3][0]                 
__________________________________________________________________________________________________
concatenate_23 (Concatenate)    (None, 1, 12)        0           sparse_seq_emb_hist_item[0][0]   
                                                                 sparse_seq_emb_hist_item_gender[0
__________________________________________________________________________________________________
concatenate_21 (Concatenate)    (None, 4, 12)        0           sparse_seq_emb_hist_item[1][0]   
                                                                 sparse_seq_emb_hist_item_gender[1
__________________________________________________________________________________________________
no_mask_32 (NoMask)             (None, 1, 20)        0           concatenate_22[0][0]             
__________________________________________________________________________________________________
attention_sequence_pooling_laye (None, 1, 12)        7561        concatenate_23[0][0]             
                                                                 concatenate_21[0][0]             
__________________________________________________________________________________________________
concatenate_24 (Concatenate)    (None, 1, 32)        0           no_mask_32[0][0]                 
                                                                 attention_sequence_pooling_layer_
__________________________________________________________________________________________________
flatten_11 (Flatten)            (None, 32)           0           concatenate_24[0][0]             
__________________________________________________________________________________________________
score (InputLayer)              [(None, 1)]          0                                            
__________________________________________________________________________________________________
no_mask_33 (NoMask)             (None, 32)           0           flatten_11[0][0]                 
__________________________________________________________________________________________________
no_mask_34 (NoMask)             (None, 1)            0           score[0][0]                      
__________________________________________________________________________________________________
flatten_12 (Flatten)            (None, 32)           0           no_mask_33[0][0]                 
__________________________________________________________________________________________________
flatten_13 (Flatten)            (None, 1)            0           no_mask_34[0][0]                 
__________________________________________________________________________________________________
no_mask_35 (NoMask)             multiple             0           flatten_12[0][0]                 
                                                                 flatten_13[0][0]                 
__________________________________________________________________________________________________
concatenate_25 (Concatenate)    (None, 33)           0           no_mask_35[0][0]                 
                                                                 no_mask_35[1][0]                 
__________________________________________________________________________________________________
dnn_7 (DNN)                     (None, 4)            176         concatenate_25[0][0]             
__________________________________________________________________________________________________
dense_5 (Dense)                 (None, 1)            4           dnn_7[0][0]                      
__________________________________________________________________________________________________
prediction_layer_6 (PredictionL (None, 1)            1           dense_5[0][0]                    
==================================================================================================
Total params: 7,806
Trainable params: 7,566
Non-trainable params: 240
__________________________________________________________________________________________________
Train on 1 samples, validate on 2 samples
1/1 [==============================] - 3s 3s/sample - loss: 0.2500 - binary_crossentropy: 0.6931 - val_loss: 0.2515 - val_binary_crossentropy: 0.6962
2020-05-19 04:13:57.848295: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 04:13:57.849543: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 04:13:57.852122: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-19 04:13:57.857321: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-19 04:13:57.858209: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-19 04:13:57.859015: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 04:13:57.859768: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

  #### metrics   #################################################### 
{'MSE': 0.25193721517516615}

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
Model: "model_6"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
user (InputLayer)               [(None, 1)]          0                                            
__________________________________________________________________________________________________
gender (InputLayer)             [(None, 1)]          0                                            
__________________________________________________________________________________________________
item (InputLayer)               [(None, 1)]          0                                            
__________________________________________________________________________________________________
item_gender (InputLayer)        [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_emb_user (Embedding)     (None, 1, 4)         12          user[0][0]                       
__________________________________________________________________________________________________
sparse_emb_gender (Embedding)   (None, 1, 4)         8           gender[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_hist_item (Embed multiple             32          item[0][0]                       
                                                                 hist_item[0][0]                  
                                                                 item[0][0]                       
__________________________________________________________________________________________________
sparse_seq_emb_hist_item_gender multiple             12          item_gender[0][0]                
                                                                 hist_item_gender[0][0]           
                                                                 item_gender[0][0]                
__________________________________________________________________________________________________
hist_item (InputLayer)          [(None, 4)]          0                                            
__________________________________________________________________________________________________
hist_item_gender (InputLayer)   [(None, 4)]          0                                            
__________________________________________________________________________________________________
no_mask_31 (NoMask)             multiple             0           sparse_emb_user[0][0]            
                                                                 sparse_emb_gender[0][0]          
                                                                 sparse_seq_emb_hist_item[2][0]   
                                                                 sparse_seq_emb_hist_item_gender[2
__________________________________________________________________________________________________
concatenate_22 (Concatenate)    (None, 1, 20)        0           no_mask_31[0][0]                 
                                                                 no_mask_31[1][0]                 
                                                                 no_mask_31[2][0]                 
                                                                 no_mask_31[3][0]                 
__________________________________________________________________________________________________
concatenate_23 (Concatenate)    (None, 1, 12)        0           sparse_seq_emb_hist_item[0][0]   
                                                                 sparse_seq_emb_hist_item_gender[0
__________________________________________________________________________________________________
concatenate_21 (Concatenate)    (None, 4, 12)        0           sparse_seq_emb_hist_item[1][0]   
                                                                 sparse_seq_emb_hist_item_gender[1
__________________________________________________________________________________________________
no_mask_32 (NoMask)             (None, 1, 20)        0           concatenate_22[0][0]             
__________________________________________________________________________________________________
attention_sequence_pooling_laye (None, 1, 12)        7561        concatenate_23[0][0]             
                                                                 concatenate_21[0][0]             
__________________________________________________________________________________________________
concatenate_24 (Concatenate)    (None, 1, 32)        0           no_mask_32[0][0]                 
                                                                 attention_sequence_pooling_layer_
__________________________________________________________________________________________________
flatten_11 (Flatten)            (None, 32)           0           concatenate_24[0][0]             
__________________________________________________________________________________________________
score (InputLayer)              [(None, 1)]          0                                            
__________________________________________________________________________________________________
no_mask_33 (NoMask)             (None, 32)           0           flatten_11[0][0]                 
__________________________________________________________________________________________________
no_mask_34 (NoMask)             (None, 1)            0           score[0][0]                      
__________________________________________________________________________________________________
flatten_12 (Flatten)            (None, 32)           0           no_mask_33[0][0]                 
__________________________________________________________________________________________________
flatten_13 (Flatten)            (None, 1)            0           no_mask_34[0][0]                 
__________________________________________________________________________________________________
no_mask_35 (NoMask)             multiple             0           flatten_12[0][0]                 
                                                                 flatten_13[0][0]                 
__________________________________________________________________________________________________
concatenate_25 (Concatenate)    (None, 33)           0           no_mask_35[0][0]                 
                                                                 no_mask_35[1][0]                 
__________________________________________________________________________________________________
dnn_7 (DNN)                     (None, 4)            176         concatenate_25[0][0]             
__________________________________________________________________________________________________
dense_5 (Dense)                 (None, 1)            4           dnn_7[0][0]                      
__________________________________________________________________________________________________
prediction_layer_6 (PredictionL (None, 1)            1           dense_5[0][0]                    
==================================================================================================
Total params: 7,806
Trainable params: 7,566
Non-trainable params: 240
__________________________________________________________________________________________________

  #### Loading params   ############################################## 

  #### Path params   ################################################# 

  #### Model params   ################################################ 
{'model_name': 'DSIN', 'optimization': 'adam', 'cost': 'mse'} {'dataset_type': 'synthesis', 'sample_size': 8, 'test_size': 0.2, 'dataset_name': 'DSIN'} {'batch_size': 100, 'epochs': 1, 'validation_split': 0.5} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/deepctr/model_DSIN.h5'}

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/autograph/converters/directives.py:119: The name tf.string_to_hash_bucket_fast is deprecated. Please use tf.strings.to_hash_bucket_fast instead.

WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/autograph/converters/directives.py:119: The name tf.matrix_set_diag is deprecated. Please use tf.linalg.set_diag instead.

Model: "model_7"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
item (InputLayer)               [(None, 1)]          0                                            
__________________________________________________________________________________________________
item_gender (InputLayer)        [(None, 1)]          0                                            
__________________________________________________________________________________________________
sess_0_item (InputLayer)        [(None, 4)]          0                                            
__________________________________________________________________________________________________
sess_0_item_gender (InputLayer) [(None, 4)]          0                                            
__________________________________________________________________________________________________
sess_1_item (InputLayer)        [(None, 4)]          0                                            
__________________________________________________________________________________________________
sess_1_item_gender (InputLayer) [(None, 4)]          0                                            
__________________________________________________________________________________________________
hash_4 (Hash)                   (None, 1)            0           item[0][0]                       
__________________________________________________________________________________________________
hash_5 (Hash)                   (None, 1)            0           item_gender[0][0]                
__________________________________________________________________________________________________
hash (Hash)                     (None, 1)            0           item[0][0]                       
__________________________________________________________________________________________________
hash_1 (Hash)                   (None, 1)            0           item_gender[0][0]                
__________________________________________________________________________________________________
hash_6 (Hash)                   (None, 4)            0           sess_0_item[0][0]                
__________________________________________________________________________________________________
hash_7 (Hash)                   (None, 4)            0           sess_0_item_gender[0][0]         
__________________________________________________________________________________________________
hash_8 (Hash)                   (None, 4)            0           sess_1_item[0][0]                
__________________________________________________________________________________________________
hash_9 (Hash)                   (None, 4)            0           sess_1_item_gender[0][0]         
__________________________________________________________________________________________________
sparse_emb_2-item (Embedding)   multiple             16          hash[0][0]                       
                                                                 hash_4[0][0]                     
                                                                 hash_6[0][0]                     
                                                                 hash_8[0][0]                     
__________________________________________________________________________________________________
sparse_emb_3-item_gender (Embed multiple             12          hash_1[0][0]                     
                                                                 hash_5[0][0]                     
                                                                 hash_7[0][0]                     
                                                                 hash_9[0][0]                     
__________________________________________________________________________________________________
concatenate_28 (Concatenate)    (None, 4, 8)         0           sparse_emb_2-item[2][0]          
                                                                 sparse_emb_3-item_gender[2][0]   
__________________________________________________________________________________________________
concatenate_29 (Concatenate)    (None, 4, 8)         0           sparse_emb_2-item[3][0]          
                                                                 sparse_emb_3-item_gender[3][0]   
__________________________________________________________________________________________________
user (InputLayer)               [(None, 1)]          0                                            
__________________________________________________________________________________________________
gender (InputLayer)             [(None, 1)]          0                                            
__________________________________________________________________________________________________
transformer (Transformer)       (None, 1, 8)         704         concatenate_28[0][0]             
                                                                 concatenate_28[0][0]             
                                                                 concatenate_29[0][0]             
                                                                 concatenate_29[0][0]             
__________________________________________________________________________________________________
hash_2 (Hash)                   (None, 1)            0           user[0][0]                       
__________________________________________________________________________________________________
hash_3 (Hash)                   (None, 1)            0           gender[0][0]                     
__________________________________________________________________________________________________
no_mask_37 (NoMask)             (None, 1, 8)         0           transformer[0][0]                
                                                                 transformer[1][0]                
__________________________________________________________________________________________________
sparse_emb_0-user (Embedding)   (None, 1, 4)         12          hash_2[0][0]                     
__________________________________________________________________________________________________
sparse_emb_1-gender (Embedding) (None, 1, 4)         8           hash_3[0][0]                     
__________________________________________________________________________________________________
concatenate_30 (Concatenate)    (None, 2, 8)         0           no_mask_37[0][0]                 
                                                                 no_mask_37[1][0]                 
__________________________________________________________________________________________________
no_mask_36 (NoMask)             (None, 1, 4)         0           sparse_emb_0-user[0][0]          
                                                                 sparse_emb_1-gender[0][0]        
                                                                 sparse_emb_2-item[1][0]          
                                                                 sparse_emb_3-item_gender[1][0]   
__________________________________________________________________________________________________
concatenate_26 (Concatenate)    (None, 1, 8)         0           sparse_emb_2-item[0][0]          
                                                                 sparse_emb_3-item_gender[0][0]   
__________________________________________________________________________________________________
sess_length (InputLayer)        [(None, 1)]          0                                            
__________________________________________________________________________________________________
bi_lstm (BiLSTM)                (None, 2, 8)         2176        concatenate_30[0][0]             
__________________________________________________________________________________________________
concatenate_27 (Concatenate)    (None, 1, 16)        0           no_mask_36[0][0]                 2020-05-19 04:14:31.236727: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 04:14:31.241963: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 04:14:31.257611: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-19 04:14:31.284845: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-19 04:14:31.289547: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-19 04:14:31.293977: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 04:14:31.298284: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

                                                                 no_mask_36[1][0]                 
                                                                 no_mask_36[2][0]                 
                                                                 no_mask_36[3][0]                 
__________________________________________________________________________________________________
attention_sequence_pooling_laye (None, 1, 8)         3169        concatenate_26[0][0]             
                                                                 concatenate_30[0][0]             
                                                                 sess_length[0][0]                
__________________________________________________________________________________________________
attention_sequence_pooling_laye (None, 1, 8)         3169        concatenate_26[0][0]             
                                                                 bi_lstm[0][0]                    
                                                                 sess_length[0][0]                
__________________________________________________________________________________________________
flatten_14 (Flatten)            (None, 16)           0           concatenate_27[0][0]             
__________________________________________________________________________________________________
flatten_15 (Flatten)            (None, 8)            0           attention_sequence_pooling_layer_
__________________________________________________________________________________________________
flatten_16 (Flatten)            (None, 8)            0           attention_sequence_pooling_layer_
__________________________________________________________________________________________________
concatenate_31 (Concatenate)    (None, 32)           0           flatten_14[0][0]                 
                                                                 flatten_15[0][0]                 
                                                                 flatten_16[0][0]                 
__________________________________________________________________________________________________
score (InputLayer)              [(None, 1)]          0                                            
__________________________________________________________________________________________________
no_mask_38 (NoMask)             (None, 32)           0           concatenate_31[0][0]             
__________________________________________________________________________________________________
no_mask_39 (NoMask)             (None, 1)            0           score[0][0]                      
__________________________________________________________________________________________________
flatten_17 (Flatten)            (None, 32)           0           no_mask_38[0][0]                 
__________________________________________________________________________________________________
flatten_18 (Flatten)            (None, 1)            0           no_mask_39[0][0]                 
__________________________________________________________________________________________________
no_mask_40 (NoMask)             multiple             0           flatten_17[0][0]                 
                                                                 flatten_18[0][0]                 
__________________________________________________________________________________________________
concatenate_32 (Concatenate)    (None, 33)           0           no_mask_40[0][0]                 
                                                                 no_mask_40[1][0]                 
__________________________________________________________________________________________________
dnn_11 (DNN)                    (None, 4)            176         concatenate_32[0][0]             
__________________________________________________________________________________________________
dense_6 (Dense)                 (None, 1)            4           dnn_11[0][0]                     
__________________________________________________________________________________________________
prediction_layer_7 (PredictionL (None, 1)            1           dense_6[0][0]                    
==================================================================================================
Total params: 9,447
Trainable params: 9,447
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 1 samples, validate on 2 samples
1/1 [==============================] - 5s 5s/sample - loss: 0.0574 - binary_crossentropy: 0.2739 - val_loss: 0.2998 - val_binary_crossentropy: 0.8041
2020-05-19 04:14:33.580431: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 04:14:33.585356: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 04:14:33.598048: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-19 04:14:33.623633: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-19 04:14:33.628048: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-19 04:14:33.632191: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 04:14:33.636182: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

  #### metrics   #################################################### 
{'MSE': 0.22540222832724174}

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
Model: "model_7"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
item (InputLayer)               [(None, 1)]          0                                            
__________________________________________________________________________________________________
item_gender (InputLayer)        [(None, 1)]          0                                            
__________________________________________________________________________________________________
sess_0_item (InputLayer)        [(None, 4)]          0                                            
__________________________________________________________________________________________________
sess_0_item_gender (InputLayer) [(None, 4)]          0                                            
__________________________________________________________________________________________________
sess_1_item (InputLayer)        [(None, 4)]          0                                            
__________________________________________________________________________________________________
sess_1_item_gender (InputLayer) [(None, 4)]          0                                            
__________________________________________________________________________________________________
hash_4 (Hash)                   (None, 1)            0           item[0][0]                       
__________________________________________________________________________________________________
hash_5 (Hash)                   (None, 1)            0           item_gender[0][0]                
__________________________________________________________________________________________________
hash (Hash)                     (None, 1)            0           item[0][0]                       
__________________________________________________________________________________________________
hash_1 (Hash)                   (None, 1)            0           item_gender[0][0]                
__________________________________________________________________________________________________
hash_6 (Hash)                   (None, 4)            0           sess_0_item[0][0]                
__________________________________________________________________________________________________
hash_7 (Hash)                   (None, 4)            0           sess_0_item_gender[0][0]         
__________________________________________________________________________________________________
hash_8 (Hash)                   (None, 4)            0           sess_1_item[0][0]                
__________________________________________________________________________________________________
hash_9 (Hash)                   (None, 4)            0           sess_1_item_gender[0][0]         
__________________________________________________________________________________________________
sparse_emb_2-item (Embedding)   multiple             16          hash[0][0]                       
                                                                 hash_4[0][0]                     
                                                                 hash_6[0][0]                     
                                                                 hash_8[0][0]                     
__________________________________________________________________________________________________
sparse_emb_3-item_gender (Embed multiple             12          hash_1[0][0]                     
                                                                 hash_5[0][0]                     
                                                                 hash_7[0][0]                     
                                                                 hash_9[0][0]                     
__________________________________________________________________________________________________
concatenate_28 (Concatenate)    (None, 4, 8)         0           sparse_emb_2-item[2][0]          
                                                                 sparse_emb_3-item_gender[2][0]   
__________________________________________________________________________________________________
concatenate_29 (Concatenate)    (None, 4, 8)         0           sparse_emb_2-item[3][0]          
                                                                 sparse_emb_3-item_gender[3][0]   
__________________________________________________________________________________________________
user (InputLayer)               [(None, 1)]          0                                            
__________________________________________________________________________________________________
gender (InputLayer)             [(None, 1)]          0                                            
__________________________________________________________________________________________________
transformer (Transformer)       (None, 1, 8)         704         concatenate_28[0][0]             
                                                                 concatenate_28[0][0]             
                                                                 concatenate_29[0][0]             
                                                                 concatenate_29[0][0]             
__________________________________________________________________________________________________
hash_2 (Hash)                   (None, 1)            0           user[0][0]                       
__________________________________________________________________________________________________
hash_3 (Hash)                   (None, 1)            0           gender[0][0]                     
__________________________________________________________________________________________________
no_mask_37 (NoMask)             (None, 1, 8)         0           transformer[0][0]                
                                                                 transformer[1][0]                
__________________________________________________________________________________________________
sparse_emb_0-user (Embedding)   (None, 1, 4)         12          hash_2[0][0]                     
__________________________________________________________________________________________________
sparse_emb_1-gender (Embedding) (None, 1, 4)         8           hash_3[0][0]                     
__________________________________________________________________________________________________
concatenate_30 (Concatenate)    (None, 2, 8)         0           no_mask_37[0][0]                 
                                                                 no_mask_37[1][0]                 
__________________________________________________________________________________________________
no_mask_36 (NoMask)             (None, 1, 4)         0           sparse_emb_0-user[0][0]          
                                                                 sparse_emb_1-gender[0][0]        
                                                                 sparse_emb_2-item[1][0]          
                                                                 sparse_emb_3-item_gender[1][0]   
__________________________________________________________________________________________________
concatenate_26 (Concatenate)    (None, 1, 8)         0           sparse_emb_2-item[0][0]          
                                                                 sparse_emb_3-item_gender[0][0]   
__________________________________________________________________________________________________
sess_length (InputLayer)        [(None, 1)]          0                                            
__________________________________________________________________________________________________
bi_lstm (BiLSTM)                (None, 2, 8)         2176        concatenate_30[0][0]             
__________________________________________________________________________________________________
concatenate_27 (Concatenate)    (None, 1, 16)        0           no_mask_36[0][0]                 
                                                                 no_mask_36[1][0]                 
                                                                 no_mask_36[2][0]                 
                                                                 no_mask_36[3][0]                 
__________________________________________________________________________________________________
attention_sequence_pooling_laye (None, 1, 8)         3169        concatenate_26[0][0]             
                                                                 concatenate_30[0][0]             
                                                                 sess_length[0][0]                
__________________________________________________________________________________________________
attention_sequence_pooling_laye (None, 1, 8)         3169        concatenate_26[0][0]             
                                                                 bi_lstm[0][0]                    
                                                                 sess_length[0][0]                
__________________________________________________________________________________________________
flatten_14 (Flatten)            (None, 16)           0           concatenate_27[0][0]             
__________________________________________________________________________________________________
flatten_15 (Flatten)            (None, 8)            0           attention_sequence_pooling_layer_
__________________________________________________________________________________________________
flatten_16 (Flatten)            (None, 8)            0           attention_sequence_pooling_layer_
__________________________________________________________________________________________________
concatenate_31 (Concatenate)    (None, 32)           0           flatten_14[0][0]                 
                                                                 flatten_15[0][0]                 
                                                                 flatten_16[0][0]                 
__________________________________________________________________________________________________
score (InputLayer)              [(None, 1)]          0                                            
__________________________________________________________________________________________________
no_mask_38 (NoMask)             (None, 32)           0           concatenate_31[0][0]             
__________________________________________________________________________________________________
no_mask_39 (NoMask)             (None, 1)            0           score[0][0]                      
__________________________________________________________________________________________________
flatten_17 (Flatten)            (None, 32)           0           no_mask_38[0][0]                 
__________________________________________________________________________________________________
flatten_18 (Flatten)            (None, 1)            0           no_mask_39[0][0]                 
__________________________________________________________________________________________________
no_mask_40 (NoMask)             multiple             0           flatten_17[0][0]                 
                                                                 flatten_18[0][0]                 
__________________________________________________________________________________________________
concatenate_32 (Concatenate)    (None, 33)           0           no_mask_40[0][0]                 
                                                                 no_mask_40[1][0]                 
__________________________________________________________________________________________________
dnn_11 (DNN)                    (None, 4)            176         concatenate_32[0][0]             
__________________________________________________________________________________________________
dense_6 (Dense)                 (None, 1)            4           dnn_11[0][0]                     
__________________________________________________________________________________________________
prediction_layer_7 (PredictionL (None, 1)            1           dense_6[0][0]                    
==================================================================================================
Total params: 9,447
Trainable params: 9,447
Non-trainable params: 0
__________________________________________________________________________________________________

  #### Loading params   ############################################## 

  #### Path params   ################################################# 

  #### Model params   ################################################ 
{'model_name': 'FiBiNET', 'optimization': 'adam', 'cost': 'mse'} {'dataset_type': 'synthesis', 'sample_size': 8, 'test_size': 0.2, 'dataset_name': 'FiBiNET', 'sparse_feature_num': 2, 'dense_feature_num': 2} {'batch_size': 100, 'epochs': 1, 'validation_split': 0.5} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/deepctr/model_FiBiNET.h5'}

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 
Model: "model_8"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
weighted_seq (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
weighted_seq_seq_length (InputL [(None, 1)]          0                                            
__________________________________________________________________________________________________
weight (InputLayer)             [(None, 3, 1)]       0                                            
__________________________________________________________________________________________________
sequence_sum (InputLayer)       [(None, 8)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 7)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 6)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_1 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_15 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 8, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 7, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 6, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         24          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         32          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_60 (Sequ (None, 1, 4)         0           weighted_sequence_layer_15[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_61 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_62 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_63 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
senet_layer (SENETLayer)        [(None, 1, 4), (None 24          sparse_emb_sparse_feature_0[0][0]
                                                                 sparse_emb_sparse_feature_1[0][0]
                                                                 sequence_pooling_layer_60[0][0]  
                                                                 sequence_pooling_layer_61[0][0]  
                                                                 sequence_pooling_layer_62[0][0]  
                                                                 sequence_pooling_layer_63[0][0]  
__________________________________________________________________________________________________
bilinear_interaction (BilinearI (None, 1, 60)        16          senet_layer[0][0]                
                                                                 senet_layer[0][1]                
                                                                 senet_layer[0][2]                
                                                                 senet_layer[0][3]                
                                                                 senet_layer[0][4]                
                                                                 senet_layer[0][5]                
__________________________________________________________________________________________________
bilinear_interaction_1 (Bilinea (None, 1, 60)        16          sparse_emb_sparse_feature_0[0][0]
                                                                 sparse_emb_sparse_feature_1[0][0]
                                                                 sequence_pooling_layer_60[0][0]  
                                                                 sequence_pooling_layer_61[0][0]  
                                                                 sequence_pooling_layer_62[0][0]  
                                                                 sequence_pooling_layer_63[0][0]  
__________________________________________________________________________________________________
no_mask_47 (NoMask)             (None, 1, 60)        0           bilinear_interaction[0][0]       
                                                                 bilinear_interaction_1[0][0]     
__________________________________________________________________________________________________
dense_feature_0 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
dense_feature_1 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
concatenate_38 (Concatenate)    (None, 1, 120)       0           no_mask_47[0][0]                 
                                                                 no_mask_47[1][0]                 
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
flatten_19 (Flatten)            (None, 120)          0           concatenate_38[0][0]             
__________________________________________________________________________________________________
no_mask_49 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
                                                                 dense_feature_1[0][0]            
__________________________________________________________________________________________________
weighted_sequence_layer_16 (Wei (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 8, 1)         7           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 7, 1)         7           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_48 (NoMask)             (None, 120)          0           flatten_19[0][0]                 
__________________________________________________________________________________________________
concatenate_39 (Concatenate)    (None, 2)            0           no_mask_49[0][0]                 
                                                                 no_mask_49[1][0]                 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_64 (Sequ (None, 1, 1)         0           weighted_sequence_layer_16[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_65 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_66 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_67 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
flatten_20 (Flatten)            (None, 120)          0           no_mask_48[0][0]                 
__________________________________________________________________________________________________
flatten_21 (Flatten)            (None, 2)            0           concatenate_39[0][0]             
__________________________________________________________________________________________________
no_mask_44 (NoMask)             (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_64[0][0]  
                                                                 sequence_pooling_layer_65[0][0]  
                                                                 sequence_pooling_layer_66[0][0]  
                                                                 sequence_pooling_layer_67[0][0]  
__________________________________________________________________________________________________
no_mask_45 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
                                                                 dense_feature_1[0][0]            
__________________________________________________________________________________________________
no_mask_50 (NoMask)             multiple             0           flatten_20[0][0]                 
                                                                 flatten_21[0][0]                 
__________________________________________________________________________________________________
concatenate_36 (Concatenate)    (None, 1, 6)         0           no_mask_44[0][0]                 
                                                                 no_mask_44[1][0]                 
                                                                 no_mask_44[2][0]                 
                                                                 no_mask_44[3][0]                 
                                                                 no_mask_44[4][0]                 
                                                                 no_mask_44[5][0]                 
__________________________________________________________________________________________________
concatenate_37 (Concatenate)    (None, 2)            0           no_mask_45[0][0]                 
                                                                 no_mask_45[1][0]                 
__________________________________________________________________________________________________
concatenate_40 (Concatenate)    (None, 122)          0           no_mask_50[0][0]                 
                                                                 no_mask_50[1][0]                 
__________________________________________________________________________________________________
linear_5 (Linear)               (None, 1)            2           concatenate_36[0][0]             
                                                                 concatenate_37[0][0]             
__________________________________________________________________________________________________
dnn_14 (DNN)                    (None, 4)            492         concatenate_40[0][0]             
__________________________________________________________________________________________________
no_mask_46 (NoMask)             (None, 1)            0           linear_5[0][0]                   
__________________________________________________________________________________________________
dense_7 (Dense)                 (None, 1)            4           dnn_14[0][0]                     
__________________________________________________________________________________________________
add_17 (Add)                    (None, 1)            0           no_mask_46[0][0]                 
                                                                 dense_7[0][0]                    
__________________________________________________________________________________________________
prediction_layer_8 (PredictionL (None, 1)            1           add_17[0][0]                     
==================================================================================================
Total params: 745
Trainable params: 745
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 6s - loss: 0.2555 - binary_crossentropy: 0.7043500/500 [==============================] - 4s 8ms/sample - loss: 0.2515 - binary_crossentropy: 0.6964 - val_loss: 0.2525 - val_binary_crossentropy: 0.6983

  #### metrics   #################################################### 
{'MSE': 0.2517399937720843}

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
Model: "model_8"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
weighted_seq (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
weighted_seq_seq_length (InputL [(None, 1)]          0                                            
__________________________________________________________________________________________________
weight (InputLayer)             [(None, 3, 1)]       0                                            
__________________________________________________________________________________________________
sequence_sum (InputLayer)       [(None, 8)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 7)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 6)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_1 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_15 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 8, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 7, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 6, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         24          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         32          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_60 (Sequ (None, 1, 4)         0           weighted_sequence_layer_15[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_61 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_62 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_63 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
senet_layer (SENETLayer)        [(None, 1, 4), (None 24          sparse_emb_sparse_feature_0[0][0]
                                                                 sparse_emb_sparse_feature_1[0][0]
                                                                 sequence_pooling_layer_60[0][0]  
                                                                 sequence_pooling_layer_61[0][0]  
                                                                 sequence_pooling_layer_62[0][0]  
                                                                 sequence_pooling_layer_63[0][0]  
__________________________________________________________________________________________________
bilinear_interaction (BilinearI (None, 1, 60)        16          senet_layer[0][0]                
                                                                 senet_layer[0][1]                
                                                                 senet_layer[0][2]                
                                                                 senet_layer[0][3]                
                                                                 senet_layer[0][4]                
                                                                 senet_layer[0][5]                
__________________________________________________________________________________________________
bilinear_interaction_1 (Bilinea (None, 1, 60)        16          sparse_emb_sparse_feature_0[0][0]
                                                                 sparse_emb_sparse_feature_1[0][0]
                                                                 sequence_pooling_layer_60[0][0]  
                                                                 sequence_pooling_layer_61[0][0]  
                                                                 sequence_pooling_layer_62[0][0]  
                                                                 sequence_pooling_layer_63[0][0]  
__________________________________________________________________________________________________
no_mask_47 (NoMask)             (None, 1, 60)        0           bilinear_interaction[0][0]       
                                                                 bilinear_interaction_1[0][0]     
__________________________________________________________________________________________________
dense_feature_0 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
dense_feature_1 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
concatenate_38 (Concatenate)    (None, 1, 120)       0           no_mask_47[0][0]                 
                                                                 no_mask_47[1][0]                 
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
flatten_19 (Flatten)            (None, 120)          0           concatenate_38[0][0]             
__________________________________________________________________________________________________
no_mask_49 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
                                                                 dense_feature_1[0][0]            
__________________________________________________________________________________________________
weighted_sequence_layer_16 (Wei (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 8, 1)         7           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 7, 1)         7           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_48 (NoMask)             (None, 120)          0           flatten_19[0][0]                 
__________________________________________________________________________________________________
concatenate_39 (Concatenate)    (None, 2)            0           no_mask_49[0][0]                 
                                                                 no_mask_49[1][0]                 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_64 (Sequ (None, 1, 1)         0           weighted_sequence_layer_16[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_65 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_66 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_67 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
flatten_20 (Flatten)            (None, 120)          0           no_mask_48[0][0]                 
__________________________________________________________________________________________________
flatten_21 (Flatten)            (None, 2)            0           concatenate_39[0][0]             
__________________________________________________________________________________________________
no_mask_44 (NoMask)             (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_64[0][0]  
                                                                 sequence_pooling_layer_65[0][0]  
                                                                 sequence_pooling_layer_66[0][0]  
                                                                 sequence_pooling_layer_67[0][0]  
__________________________________________________________________________________________________
no_mask_45 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
                                                                 dense_feature_1[0][0]            
__________________________________________________________________________________________________
no_mask_50 (NoMask)             multiple             0           flatten_20[0][0]                 
                                                                 flatten_21[0][0]                 
__________________________________________________________________________________________________
concatenate_36 (Concatenate)    (None, 1, 6)         0           no_mask_44[0][0]                 
                                                                 no_mask_44[1][0]                 
                                                                 no_mask_44[2][0]                 
                                                                 no_mask_44[3][0]                 
                                                                 no_mask_44[4][0]                 
                                                                 no_mask_44[5][0]                 
__________________________________________________________________________________________________
concatenate_37 (Concatenate)    (None, 2)            0           no_mask_45[0][0]                 
                                                                 no_mask_45[1][0]                 
__________________________________________________________________________________________________
concatenate_40 (Concatenate)    (None, 122)          0           no_mask_50[0][0]                 
                                                                 no_mask_50[1][0]                 
__________________________________________________________________________________________________
linear_5 (Linear)               (None, 1)            2           concatenate_36[0][0]             
                                                                 concatenate_37[0][0]             
__________________________________________________________________________________________________
dnn_14 (DNN)                    (None, 4)            492         concatenate_40[0][0]             
__________________________________________________________________________________________________
no_mask_46 (NoMask)             (None, 1)            0           linear_5[0][0]                   
__________________________________________________________________________________________________
dense_7 (Dense)                 (None, 1)            4           dnn_14[0][0]                     
__________________________________________________________________________________________________
add_17 (Add)                    (None, 1)            0           no_mask_46[0][0]                 
                                                                 dense_7[0][0]                    
__________________________________________________________________________________________________
prediction_layer_8 (PredictionL (None, 1)            1           add_17[0][0]                     
==================================================================================================
Total params: 745
Trainable params: 745
Non-trainable params: 0
__________________________________________________________________________________________________

  #### Loading params   ############################################## 

  #### Path params   ################################################# 

  #### Model params   ################################################ 
{'model_name': 'FLEN', 'optimization': 'adam', 'cost': 'mse'} {'dataset_type': 'synthesis', 'sample_size': 8, 'test_size': 0.2, 'dataset_name': 'FLEN', 'embedding_size': 2, 'sparse_feature_num': 6, 'dense_feature_num': 6, 'use_group': True} {'batch_size': 100, 'epochs': 1, 'validation_split': 0.5} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/deepctr/model_FLEN.h5'}

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 
Model: "model_9"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
weighted_seq (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
weighted_seq_seq_length (InputL [(None, 1)]          0                                            
__________________________________________________________________________________________________
weight (InputLayer)             [(None, 3, 1)]       0                                            
__________________________________________________________________________________________________
sequence_sum (InputLayer)       [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 9)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 2)         4           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_3 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_1 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_4 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_2 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_5 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_18 (Wei (None, 3, 2)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 5, 2)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 6, 2)         16          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 9, 2)         2           sequence_max[0][0]               
__________________________________________________________________________________________________
dense_feature_0 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
dense_feature_1 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
dense_feature_2 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
dense_feature_3 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
dense_feature_4 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
dense_feature_5 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 2)         12          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_3 (Em (None, 1, 2)         16          sparse_feature_3[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 2)         12          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_4 (Em (None, 1, 2)         16          sparse_feature_4[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 2)         10          sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_5 (Em (None, 1, 2)         6           sparse_feature_5[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_72 (Sequ (None, 1, 2)         0           weighted_sequence_layer_18[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_73 (Sequ (None, 1, 2)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_74 (Sequ (None, 1, 2)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_75 (Sequ (None, 1, 2)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
no_mask_61 (NoMask)             (None, 1, 2)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sparse_emb_sparse_feature_3[0][0]
                                                                 sparse_emb_sparse_feature_1[0][0]
                                                                 sparse_emb_sparse_feature_4[0][0]
                                                                 sparse_emb_sparse_feature_2[0][0]
                                                                 sparse_emb_sparse_feature_5[0][0]
                                                                 sequence_pooling_layer_72[0][0]  
                                                                 sequence_pooling_layer_73[0][0]  
                                                                 sequence_pooling_layer_74[0][0]  
                                                                 sequence_pooling_layer_75[0][0]  
__________________________________________________________________________________________________
no_mask_62 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
                                                                 dense_feature_1[0][0]            
                                                                 dense_feature_2[0][0]            
                                                                 dense_feature_3[0][0]            
                                                                 dense_feature_4[0][0]            
                                                                 dense_feature_5[0][0]            
__________________________________________________________________________________________________
concatenate_50 (Concatenate)    (None, 1, 20)        0           no_mask_61[0][0]                 
                                                                 no_mask_61[1][0]                 
                                                                 no_mask_61[2][0]                 
                                                                 no_mask_61[3][0]                 
                                                                 no_mask_61[4][0]                 
                                                                 no_mask_61[5][0]                 
                                                                 no_mask_61[6][0]                 
                                                                 no_mask_61[7][0]                 
                                                                 no_mask_61[8][0]                 
                                                                 no_mask_61[9][0]                 
__________________________________________________________________________________________________
concatenate_51 (Concatenate)    (None, 6)            0           no_mask_62[0][0]                 
                                                                 no_mask_62[1][0]                 
                                                                 no_mask_62[2][0]                 
                                                                 no_mask_62[3][0]                 
                                                                 no_mask_62[4][0]                 
                                                                 no_mask_62[5][0]                 
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
flatten_22 (Flatten)            (None, 20)           0           concatenate_50[0][0]             
__________________________________________________________________________________________________
flatten_23 (Flatten)            (None, 6)            0           concatenate_51[0][0]             
__________________________________________________________________________________________________
weighted_sequence_layer_19 (Wei (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         2           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         8           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         1           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_57 (NoMask)             (None, 1, 2)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sparse_emb_sparse_feature_3[0][0]
__________________________________________________________________________________________________
no_mask_58 (NoMask)             (None, 1, 2)         0           sparse_emb_sparse_feature_1[0][0]
                                                                 sparse_emb_sparse_feature_4[0][0]
__________________________________________________________________________________________________
no_mask_59 (NoMask)             (None, 1, 2)         0           sparse_emb_sparse_feature_2[0][0]
                                                                 sparse_emb_sparse_feature_5[0][0]
__________________________________________________________________________________________________
no_mask_60 (NoMask)             (None, 1, 2)         0           sequence_pooling_layer_72[0][0]  
                                                                 sequence_pooling_layer_73[0][0]  
                                                                 sequence_pooling_layer_74[0][0]  
                                                                 sequence_pooling_layer_75[0][0]  
__________________________________________________________________________________________________
no_mask_63 (NoMask)             multiple             0           flatten_22[0][0]                 
                                                                 flatten_23[0][0]                 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_3[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_4[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_5[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_76 (Sequ (None, 1, 1)         0           weighted_sequence_layer_19[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_77 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_78 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_79 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
concatenate_46 (Concatenate)    (None, 2, 2)         0           no_mask_57[0][0]                 
                                                                 no_mask_57[1][0]                 
__________________________________________________________________________________________________
concatenate_47 (Concatenate)    (None, 2, 2)         0           no_mask_58[0][0]                 
                                                                 no_mask_58[1][0]                 
__________________________________________________________________________________________________
concatenate_48 (Concatenate)    (None, 2, 2)         0           no_mask_59[0][0]                 
                                                                 no_mask_59[1][0]                 
__________________________________________________________________________________________________
concatenate_49 (Concatenate)    (None, 4, 2)         0           no_mask_60[0][0]                 
                                                                 no_mask_60[1][0]                 
                                                                 no_mask_60[2][0]                 
                                                                 no_mask_60[3][0]                 
__________________________________________________________________________________________________
concatenate_52 (Concatenate)    (None, 26)           0           no_mask_63[0][0]                 
                                                                 no_mask_63[1][0]                 
__________________________________________________________________________________________________
no_mask_54 (NoMask)             (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_76[0][0]  
                                                                 sequence_pooling_layer_77[0][0]  
                                                                 sequence_pooling_layer_78[0][0]  
                                                                 sequence_pooling_layer_79[0][0]  
__________________________________________________________________________________________________
no_mask_55 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
                                                                 dense_feature_1[0][0]            
                                                                 dense_feature_2[0][0]            
                                                                 dense_feature_3[0][0]            
                                                                 dense_feature_4[0][0]            
                                                                 dense_feature_5[0][0]            
__________________________________________________________________________________________________
field_wise_bi_interaction (Fiel (None, 2)            14          concatenate_46[0][0]             
                                                                 concatenate_47[0][0]             
                                                                 concatenate_48[0][0]             
                                                                 concatenate_49[0][0]             
__________________________________________________________________________________________________
dnn_15 (DNN)                    (None, 3)            81          concatenate_52[0][0]             
__________________________________________________________________________________________________
concatenate_44 (Concatenate)    (None, 1, 10)        0           no_mask_54[0][0]                 
                                                                 no_mask_54[1][0]                 
                                                                 no_mask_54[2][0]                 
                                                                 no_mask_54[3][0]                 
                                                                 no_mask_54[4][0]                 
                                                                 no_mask_54[5][0]                 
                                                                 no_mask_54[6][0]                 
                                                                 no_mask_54[7][0]                 
                                                                 no_mask_54[8][0]                 
                                                                 no_mask_54[9][0]                 
__________________________________________________________________________________________________
concatenate_45 (Concatenate)    (None, 6)            0           no_mask_55[0][0]                 
                                                                 no_mask_55[1][0]                 
                                                                 no_mask_55[2][0]                 
                                                                 no_mask_55[3][0]                 
                                                                 no_mask_55[4][0]                 
                                                                 no_mask_55[5][0]                 
__________________________________________________________________________________________________
no_mask_64 (NoMask)             multiple             0           field_wise_bi_interaction[0][0]  
                                                                 dnn_15[0][0]                     
__________________________________________________________________________________________________
linear_6 (Linear)               (None, 1)            6           concatenate_44[0][0]             
                                                                 concatenate_45[0][0]             
__________________________________________________________________________________________________
concatenate_53 (Concatenate)    (None, 5)            0           no_mask_64[0][0]                 
                                                                 no_mask_64[1][0]                 
__________________________________________________________________________________________________
no_mask_56 (NoMask)             (None, 1)            0           linear_6[0][0]                   
__________________________________________________________________________________________________
dense_8 (Dense)                 (None, 1)            5           concatenate_53[0][0]             
__________________________________________________________________________________________________
add_20 (Add)                    (None, 1)            0           no_mask_56[0][0]                 
                                                                 dense_8[0][0]                    
__________________________________________________________________________________________________
prediction_layer_9 (PredictionL (None, 1)            1           add_20[0][0]                     
==================================================================================================
Total params: 254
Trainable params: 254
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 6s - loss: 0.5600 - binary_crossentropy: 8.6380500/500 [==============================] - 4s 9ms/sample - loss: 0.5040 - binary_crossentropy: 7.7742 - val_loss: 0.5560 - val_binary_crossentropy: 8.5763

  #### metrics   #################################################### 
{'MSE': 0.53}

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
Model: "model_9"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
weighted_seq (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
weighted_seq_seq_length (InputL [(None, 1)]          0                                            
__________________________________________________________________________________________________
weight (InputLayer)             [(None, 3, 1)]       0                                            
__________________________________________________________________________________________________
sequence_sum (InputLayer)       [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 9)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 2)         4           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_3 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_1 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_4 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_2 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_5 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_18 (Wei (None, 3, 2)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 5, 2)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 6, 2)         16          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 9, 2)         2           sequence_max[0][0]               
__________________________________________________________________________________________________
dense_feature_0 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
dense_feature_1 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
dense_feature_2 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
dense_feature_3 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
dense_feature_4 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
dense_feature_5 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 2)         12          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_3 (Em (None, 1, 2)         16          sparse_feature_3[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 2)         12          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_4 (Em (None, 1, 2)         16          sparse_feature_4[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 2)         10          sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_5 (Em (None, 1, 2)         6           sparse_feature_5[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_72 (Sequ (None, 1, 2)         0           weighted_sequence_layer_18[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_73 (Sequ (None, 1, 2)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_74 (Sequ (None, 1, 2)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_75 (Sequ (None, 1, 2)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
no_mask_61 (NoMask)             (None, 1, 2)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sparse_emb_sparse_feature_3[0][0]
                                                                 sparse_emb_sparse_feature_1[0][0]
                                                                 sparse_emb_sparse_feature_4[0][0]
                                                                 sparse_emb_sparse_feature_2[0][0]
                                                                 sparse_emb_sparse_feature_5[0][0]
                                                                 sequence_pooling_layer_72[0][0]  
                                                                 sequence_pooling_layer_73[0][0]  
                                                                 sequence_pooling_layer_74[0][0]  
                                                                 sequence_pooling_layer_75[0][0]  
__________________________________________________________________________________________________
no_mask_62 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
                                                                 dense_feature_1[0][0]            
                                                                 dense_feature_2[0][0]            
                                                                 dense_feature_3[0][0]            
                                                                 dense_feature_4[0][0]            
                                                                 dense_feature_5[0][0]            
__________________________________________________________________________________________________
concatenate_50 (Concatenate)    (None, 1, 20)        0           no_mask_61[0][0]                 
                                                                 no_mask_61[1][0]                 
                                                                 no_mask_61[2][0]                 
                                                                 no_mask_61[3][0]                 
                                                                 no_mask_61[4][0]                 
                                                                 no_mask_61[5][0]                 
                                                                 no_mask_61[6][0]                 
                                                                 no_mask_61[7][0]                 
                                                                 no_mask_61[8][0]                 
                                                                 no_mask_61[9][0]                 
__________________________________________________________________________________________________
concatenate_51 (Concatenate)    (None, 6)            0           no_mask_62[0][0]                 
                                                                 no_mask_62[1][0]                 
                                                                 no_mask_62[2][0]                 
                                                                 no_mask_62[3][0]                 
                                                                 no_mask_62[4][0]                 
                                                                 no_mask_62[5][0]                 
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
flatten_22 (Flatten)            (None, 20)           0           concatenate_50[0][0]             
__________________________________________________________________________________________________
flatten_23 (Flatten)            (None, 6)            0           concatenate_51[0][0]             
__________________________________________________________________________________________________
weighted_sequence_layer_19 (Wei (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         2           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         8           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         1           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_57 (NoMask)             (None, 1, 2)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sparse_emb_sparse_feature_3[0][0]
__________________________________________________________________________________________________
no_mask_58 (NoMask)             (None, 1, 2)         0           sparse_emb_sparse_feature_1[0][0]
                                                                 sparse_emb_sparse_feature_4[0][0]
__________________________________________________________________________________________________
no_mask_59 (NoMask)             (None, 1, 2)         0           sparse_emb_sparse_feature_2[0][0]
                                                                 sparse_emb_sparse_feature_5[0][0]
__________________________________________________________________________________________________
no_mask_60 (NoMask)             (None, 1, 2)         0           sequence_pooling_layer_72[0][0]  
                                                                 sequence_pooling_layer_73[0][0]  
                                                                 sequence_pooling_layer_74[0][0]  
                                                                 sequence_pooling_layer_75[0][0]  
__________________________________________________________________________________________________
no_mask_63 (NoMask)             multiple             0           flatten_22[0][0]                 
                                                                 flatten_23[0][0]                 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_3[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_4[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_5[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_76 (Sequ (None, 1, 1)         0           weighted_sequence_layer_19[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_77 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_78 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_79 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
concatenate_46 (Concatenate)    (None, 2, 2)         0           no_mask_57[0][0]                 
                                                                 no_mask_57[1][0]                 
__________________________________________________________________________________________________
concatenate_47 (Concatenate)    (None, 2, 2)         0           no_mask_58[0][0]                 
                                                                 no_mask_58[1][0]                 
__________________________________________________________________________________________________
concatenate_48 (Concatenate)    (None, 2, 2)         0           no_mask_59[0][0]                 
                                                                 no_mask_59[1][0]                 
__________________________________________________________________________________________________
concatenate_49 (Concatenate)    (None, 4, 2)         0           no_mask_60[0][0]                 
                                                                 no_mask_60[1][0]                 
                                                                 no_mask_60[2][0]                 
                                                                 no_mask_60[3][0]                 
__________________________________________________________________________________________________
concatenate_52 (Concatenate)    (None, 26)           0           no_mask_63[0][0]                 
                                                                 no_mask_63[1][0]                 
__________________________________________________________________________________________________
no_mask_54 (NoMask)             (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_76[0][0]  
                                                                 sequence_pooling_layer_77[0][0]  
                                                                 sequence_pooling_layer_78[0][0]  
                                                                 sequence_pooling_layer_79[0][0]  
__________________________________________________________________________________________________
no_mask_55 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
                                                                 dense_feature_1[0][0]            
                                                                 dense_feature_2[0][0]            
                                                                 dense_feature_3[0][0]            
                                                                 dense_feature_4[0][0]            
                                                                 dense_feature_5[0][0]            
__________________________________________________________________________________________________
field_wise_bi_interaction (Fiel (None, 2)            14          concatenate_46[0][0]             
                                                                 concatenate_47[0][0]             
                                                                 concatenate_48[0][0]             
                                                                 concatenate_49[0][0]             
__________________________________________________________________________________________________
dnn_15 (DNN)                    (None, 3)            81          concatenate_52[0][0]             
__________________________________________________________________________________________________
concatenate_44 (Concatenate)    (None, 1, 10)        0           no_mask_54[0][0]                 
                                                                 no_mask_54[1][0]                 
                                                                 no_mask_54[2][0]                 
                                                                 no_mask_54[3][0]                 
                                                                 no_mask_54[4][0]                 
                                                                 no_mask_54[5][0]                 
                                                                 no_mask_54[6][0]                 
                                                                 no_mask_54[7][0]                 
                                                                 no_mask_54[8][0]                 
                                                                 no_mask_54[9][0]                 
__________________________________________________________________________________________________
concatenate_45 (Concatenate)    (None, 6)            0           no_mask_55[0][0]                 
                                                                 no_mask_55[1][0]                 
                                                                 no_mask_55[2][0]                 
                                                                 no_mask_55[3][0]                 
                                                                 no_mask_55[4][0]                 
                                                                 no_mask_55[5][0]                 
__________________________________________________________________________________________________
no_mask_64 (NoMask)             multiple             0           field_wise_bi_interaction[0][0]  
                                                                 dnn_15[0][0]                     
__________________________________________________________________________________________________
linear_6 (Linear)               (None, 1)            6           concatenate_44[0][0]             
                                                                 concatenate_45[0][0]             
__________________________________________________________________________________________________
concatenate_53 (Concatenate)    (None, 5)            0           no_mask_64[0][0]                 
                                                                 no_mask_64[1][0]                 
__________________________________________________________________________________________________
no_mask_56 (NoMask)             (None, 1)            0           linear_6[0][0]                   
__________________________________________________________________________________________________
dense_8 (Dense)                 (None, 1)            5           concatenate_53[0][0]             
__________________________________________________________________________________________________
add_20 (Add)                    (None, 1)            0           no_mask_56[0][0]                 
                                                                 dense_8[0][0]                    
__________________________________________________________________________________________________
prediction_layer_9 (PredictionL (None, 1)            1           add_20[0][0]                     
==================================================================================================
Total params: 254
Trainable params: 254
Non-trainable params: 0
__________________________________________________________________________________________________

  #### Loading params   ############################################## 

  #### Path params   ################################################# 

  #### Model params   ################################################ 
{'model_name': 'FNN', 'optimization': 'adam', 'cost': 'mse'} {'dataset_type': 'synthesis', 'sample_size': 8, 'test_size': 0.2, 'dataset_name': 'FNN', 'sparse_feature_num': 1, 'dense_feature_num': 1} {'batch_size': 100, 'epochs': 1, 'validation_split': 0.5} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/deepctr/model_FNN.h5'}

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 
Model: "model_10"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
weighted_seq (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
weighted_seq_seq_length (InputL [(None, 1)]          0                                            
__________________________________________________________________________________________________
weight (InputLayer)             [(None, 3, 1)]       0                                            
__________________________________________________________________________________________________
sequence_sum (InputLayer)       [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 4)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_21 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 5, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 2, 4)         36          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 4, 4)         36          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         4           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_84 (Sequ (None, 1, 4)         0           weighted_sequence_layer_21[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_85 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_86 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_87 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
no_mask_68 (NoMask)             (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_84[0][0]  
                                                                 sequence_pooling_layer_85[0][0]  
                                                                 sequence_pooling_layer_86[0][0]  
                                                                 sequence_pooling_layer_87[0][0]  
__________________________________________________________________________________________________
dense_feature_0 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
concatenate_55 (Concatenate)    (None, 1, 20)        0           no_mask_68[0][0]                 
                                                                 no_mask_68[1][0]                 
                                                                 no_mask_68[2][0]                 
                                                                 no_mask_68[3][0]                 
                                                                 no_mask_68[4][0]                 
__________________________________________________________________________________________________
no_mask_69 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
weighted_sequence_layer_22 (Wei (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         9           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 4, 1)         9           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_24 (Flatten)            (None, 20)           0           concatenate_55[0][0]             
__________________________________________________________________________________________________
flatten_25 (Flatten)            (None, 1)            0           no_mask_69[0][0]                 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         1           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_88 (Sequ (None, 1, 1)         0           weighted_sequence_layer_22[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_89 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_90 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_91 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
no_mask_70 (NoMask)             multiple             0           flatten_24[0][0]                 
                                                                 flatten_25[0][0]                 
__________________________________________________________________________________________________
no_mask_65 (NoMask)             (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_88[0][0]  
                                                                 sequence_pooling_layer_89[0][0]  
                                                                 sequence_pooling_layer_90[0][0]  
                                                                 sequence_pooling_layer_91[0][0]  
__________________________________________________________________________________________________
concatenate_56 (Concatenate)    (None, 21)           0           no_mask_70[0][0]                 
                                                                 no_mask_70[1][0]                 
__________________________________________________________________________________________________
concatenate_54 (Concatenate)    (None, 1, 5)         0           no_mask_65[0][0]                 
                                                                 no_mask_65[1][0]                 
                                                                 no_mask_65[2][0]                 
                                                                 no_mask_65[3][0]                 
                                                                 no_mask_65[4][0]                 
__________________________________________________________________________________________________
no_mask_66 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
dnn_16 (DNN)                    (None, 32)           1760        concatenate_56[0][0]             
__________________________________________________________________________________________________
linear_7 (Linear)               (None, 1)            1           concatenate_54[0][0]             
                                                                 no_mask_66[0][0]                 
__________________________________________________________________________________________________
dense_9 (Dense)                 (None, 1)            32          dnn_16[0][0]                     
__________________________________________________________________________________________________
no_mask_67 (NoMask)             (None, 1)            0           linear_7[0][0]                   
__________________________________________________________________________________________________
add_23 (Add)                    (None, 1)            0           dense_9[0][0]                    
                                                                 no_mask_67[0][0]                 
__________________________________________________________________________________________________
prediction_layer_10 (Prediction (None, 1)            1           add_23[0][0]                     
==================================================================================================
Total params: 1,939
Trainable params: 1,939
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 6s - loss: 0.2658 - binary_crossentropy: 0.7322500/500 [==============================] - 4s 9ms/sample - loss: 0.2724 - binary_crossentropy: 0.7460 - val_loss: 0.2807 - val_binary_crossentropy: 0.7617

  #### metrics   #################################################### 
{'MSE': 0.2768647551335268}

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
Model: "model_10"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
weighted_seq (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
weighted_seq_seq_length (InputL [(None, 1)]          0                                            
__________________________________________________________________________________________________
weight (InputLayer)             [(None, 3, 1)]       0                                            
__________________________________________________________________________________________________
sequence_sum (InputLayer)       [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 4)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_21 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 5, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 2, 4)         36          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 4, 4)         36          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         4           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_84 (Sequ (None, 1, 4)         0           weighted_sequence_layer_21[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_85 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_86 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_87 (Sequ (None, 1, 4)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
no_mask_68 (NoMask)             (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_84[0][0]  
                                                                 sequence_pooling_layer_85[0][0]  
                                                                 sequence_pooling_layer_86[0][0]  
                                                                 sequence_pooling_layer_87[0][0]  
__________________________________________________________________________________________________
dense_feature_0 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
concatenate_55 (Concatenate)    (None, 1, 20)        0           no_mask_68[0][0]                 
                                                                 no_mask_68[1][0]                 
                                                                 no_mask_68[2][0]                 
                                                                 no_mask_68[3][0]                 
                                                                 no_mask_68[4][0]                 
__________________________________________________________________________________________________
no_mask_69 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
weighted_sequence_layer_22 (Wei (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         9           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 4, 1)         9           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_24 (Flatten)            (None, 20)           0           concatenate_55[0][0]             
__________________________________________________________________________________________________
flatten_25 (Flatten)            (None, 1)            0           no_mask_69[0][0]                 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         1           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_88 (Sequ (None, 1, 1)         0           weighted_sequence_layer_22[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_89 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_90 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_91 (Sequ (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
no_mask_70 (NoMask)             multiple             0           flatten_24[0][0]                 
                                                                 flatten_25[0][0]                 
__________________________________________________________________________________________________
no_mask_65 (NoMask)             (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_88[0][0]  
                                                                 sequence_pooling_layer_89[0][0]  
                                                                 sequence_pooling_layer_90[0][0]  
                                                                 sequence_pooling_layer_91[0][0]  
__________________________________________________________________________________________________
concatenate_56 (Concatenate)    (None, 21)           0           no_mask_70[0][0]                 
                                                                 no_mask_70[1][0]                 
__________________________________________________________________________________________________
concatenate_54 (Concatenate)    (None, 1, 5)         0           no_mask_65[0][0]                 
                                                                 no_mask_65[1][0]                 
                                                                 no_mask_65[2][0]                 
                                                                 no_mask_65[3][0]                 
                                                                 no_mask_65[4][0]                 
__________________________________________________________________________________________________
no_mask_66 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
dnn_16 (DNN)                    (None, 32)           1760        concatenate_56[0][0]             
__________________________________________________________________________________________________
linear_7 (Linear)               (None, 1)            1           concatenate_54[0][0]             
                                                                 no_mask_66[0][0]                 
__________________________________________________________________________________________________
dense_9 (Dense)                 (None, 1)            32          dnn_16[0][0]                     
__________________________________________________________________________________________________
no_mask_67 (NoMask)             (None, 1)            0           linear_7[0][0]                   
__________________________________________________________________________________________________
add_23 (Add)                    (None, 1)            0           dense_9[0][0]                    
                                                                 no_mask_67[0][0]                 
__________________________________________________________________________________________________
prediction_layer_10 (Prediction (None, 1)            1           add_23[0][0]                     
==================================================================================================
Total params: 1,939
Trainable params: 1,939
Non-trainable params: 0
__________________________________________________________________________________________________

  #### Loading params   ############################################## 

  #### Path params   ################################################# 

  #### Model params   ################################################ 
{'model_name': 'MLR', 'optimization': 'adam', 'cost': 'mse'} {'dataset_type': 'synthesis', 'sample_size': 8, 'test_size': 0.2, 'dataset_name': 'MLR', 'sparse_feature_num': 0, 'dense_feature_num': 2, 'prefix': 'region'} {'batch_size': 100, 'epochs': 1, 'validation_split': 0.5} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/deepctr/model_MLR.h5'}

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 
Model: "model_11"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
regionweighted_seq (InputLayer) [(None, 3)]          0                                            
__________________________________________________________________________________________________
region_10sparse_seq_emb_regionw (None, 3, 1)         2           regionweighted_seq[0][0]         
__________________________________________________________________________________________________
regionweighted_seq_seq_length ( [(None, 1)]          0                                            
__________________________________________________________________________________________________
regionweight (InputLayer)       [(None, 3, 1)]       0                                            
__________________________________________________________________________________________________
regionsequence_sum (InputLayer) [(None, 5)]          0                                            
__________________________________________________________________________________________________
regionsequence_mean (InputLayer [(None, 7)]          0                                            
__________________________________________________________________________________________________
regionsequence_max (InputLayer) [(None, 9)]          0                                            
__________________________________________________________________________________________________
region_20sparse_seq_emb_regionw (None, 3, 1)         2           regionweighted_seq[0][0]         
__________________________________________________________________________________________________
region_30sparse_seq_emb_regionw (None, 3, 1)         2           regionweighted_seq[0][0]         
__________________________________________________________________________________________________
region_40sparse_seq_emb_regionw (None, 3, 1)         2           regionweighted_seq[0][0]         
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 3, 1)         2           regionweighted_seq[0][0]         
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 3, 1)         2           regionweighted_seq[0][0]         
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 3, 1)         2           regionweighted_seq[0][0]         
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 3, 1)         2           regionweighted_seq[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_24 (Wei (None, 3, 1)         0           region_10sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 5, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 9, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_26 (Wei (None, 3, 1)         0           region_20sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 5, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 9, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_28 (Wei (None, 3, 1)         0           region_30sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 5, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 9, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_30 (Wei (None, 3, 1)         0           region_40sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 5, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 9, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_32 (Wei (None, 3, 1)         0           learner_10sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 5, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 9, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_34 (Wei (None, 3, 1)         0           learner_20sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 5, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 9, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_36 (Wei (None, 3, 1)         0           learner_30sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 5, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 9, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_38 (Wei (None, 3, 1)         0           learner_40sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 5, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 9, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
sequence_pooling_layer_96 (Sequ (None, 1, 1)         0           weighted_sequence_layer_24[0][0] 
                                                                 regionweighted_seq_seq_length[0][
__________________________________________________________________________________________________
sequence_pooling_layer_97 (Sequ (None, 1, 1)         0           region_10sparse_seq_emb_regionseq
__________________________________________________________________________________________________
sequence_pooling_layer_98 (Sequ (None, 1, 1)         0           region_10sparse_seq_emb_regionseq
__________________________________________________________________________________________________
sequence_pooling_layer_99 (Sequ (None, 1, 1)         0           region_10sparse_seq_emb_regionseq
__________________________________________________________________________________________________
regiondense_feature_0 (InputLay [(None, 1)]          0                                            
__________________________________________________________________________________________________
regiondense_feature_1 (InputLay [(None, 1)]          0                                            
__________________________________________________________________________________________________
sequence_pooling_layer_104 (Seq (None, 1, 1)         0           weighted_sequence_layer_26[0][0] 
                                                                 regionweighted_seq_seq_length[0][
__________________________________________________________________________________________________
sequence_pooling_layer_105 (Seq (None, 1, 1)         0           region_20sparse_seq_emb_regionseq
__________________________________________________________________________________________________
sequence_pooling_layer_106 (Seq (None, 1, 1)         0           region_20sparse_seq_emb_regionseq
__________________________________________________________________________________________________
sequence_pooling_layer_107 (Seq (None, 1, 1)         0           region_20sparse_seq_emb_regionseq
__________________________________________________________________________________________________
sequence_pooling_layer_112 (Seq (None, 1, 1)         0           weighted_sequence_layer_28[0][0] 
                                                                 regionweighted_seq_seq_length[0][
__________________________________________________________________________________________________
sequence_pooling_layer_113 (Seq (None, 1, 1)         0           region_30sparse_seq_emb_regionseq
__________________________________________________________________________________________________
sequence_pooling_layer_114 (Seq (None, 1, 1)         0           region_30sparse_seq_emb_regionseq
__________________________________________________________________________________________________
sequence_pooling_layer_115 (Seq (None, 1, 1)         0           region_30sparse_seq_emb_regionseq
__________________________________________________________________________________________________
sequence_pooling_layer_120 (Seq (None, 1, 1)         0           weighted_sequence_layer_30[0][0] 
                                                                 regionweighted_seq_seq_length[0][
__________________________________________________________________________________________________
sequence_pooling_layer_121 (Seq (None, 1, 1)         0           region_40sparse_seq_emb_regionseq
__________________________________________________________________________________________________
sequence_pooling_layer_122 (Seq (None, 1, 1)         0           region_40sparse_seq_emb_regionseq
__________________________________________________________________________________________________
sequence_pooling_layer_123 (Seq (None, 1, 1)         0           region_40sparse_seq_emb_regionseq
__________________________________________________________________________________________________
sequence_pooling_layer_128 (Seq (None, 1, 1)         0           weighted_sequence_layer_32[0][0] 
                                                                 regionweighted_seq_seq_length[0][
__________________________________________________________________________________________________
sequence_pooling_layer_129 (Seq (None, 1, 1)         0           learner_10sparse_seq_emb_regionse
__________________________________________________________________________________________________
sequence_pooling_layer_130 (Seq (None, 1, 1)         0           learner_10sparse_seq_emb_regionse
__________________________________________________________________________________________________
sequence_pooling_layer_131 (Seq (None, 1, 1)         0           learner_10sparse_seq_emb_regionse
__________________________________________________________________________________________________
sequence_pooling_layer_136 (Seq (None, 1, 1)         0           weighted_sequence_layer_34[0][0] 
                                                                 regionweighted_seq_seq_length[0][
__________________________________________________________________________________________________
sequence_pooling_layer_137 (Seq (None, 1, 1)         0           learner_20sparse_seq_emb_regionse
__________________________________________________________________________________________________
sequence_pooling_layer_138 (Seq (None, 1, 1)         0           learner_20sparse_seq_emb_regionse
__________________________________________________________________________________________________
sequence_pooling_layer_139 (Seq (None, 1, 1)         0           learner_20sparse_seq_emb_regionse
__________________________________________________________________________________________________
sequence_pooling_layer_144 (Seq (None, 1, 1)         0           weighted_sequence_layer_36[0][0] 
                                                                 regionweighted_seq_seq_length[0][
__________________________________________________________________________________________________
sequence_pooling_layer_145 (Seq (None, 1, 1)         0           learner_30sparse_seq_emb_regionse
__________________________________________________________________________________________________
sequence_pooling_layer_146 (Seq (None, 1, 1)         0           learner_30sparse_seq_emb_regionse
__________________________________________________________________________________________________
sequence_pooling_layer_147 (Seq (None, 1, 1)         0           learner_30sparse_seq_emb_regionse
__________________________________________________________________________________________________
sequence_pooling_layer_152 (Seq (None, 1, 1)         0           weighted_sequence_layer_38[0][0] 
                                                                 regionweighted_seq_seq_length[0][
__________________________________________________________________________________________________
sequence_pooling_layer_153 (Seq (None, 1, 1)         0           learner_40sparse_seq_emb_regionse
__________________________________________________________________________________________________
sequence_pooling_layer_154 (Seq (None, 1, 1)         0           learner_40sparse_seq_emb_regionse
__________________________________________________________________________________________________
sequence_pooling_layer_155 (Seq (None, 1, 1)         0           learner_40sparse_seq_emb_regionse
__________________________________________________________________________________________________
no_mask_71 (NoMask)             (None, 1, 1)         0           sequence_pooling_layer_96[0][0]  
                                                                 sequence_pooling_layer_97[0][0]  
                                                                 sequence_pooling_layer_98[0][0]  
                                                                 sequence_pooling_layer_99[0][0]  
__________________________________________________________________________________________________
no_mask_72 (NoMask)             (None, 1)            0           regiondense_feature_0[0][0]      
                                                                 regiondense_feature_1[0][0]      
__________________________________________________________________________________________________
no_mask_74 (NoMask)             (None, 1, 1)         0           sequence_pooling_layer_104[0][0] 
                                                                 sequence_pooling_layer_105[0][0] 
                                                                 sequence_pooling_layer_106[0][0] 
                                                                 sequence_pooling_layer_107[0][0] 
__________________________________________________________________________________________________
no_mask_75 (NoMask)             (None, 1)            0           regiondense_feature_0[0][0]      
                                                                 regiondense_feature_1[0][0]      
__________________________________________________________________________________________________
no_mask_77 (NoMask)             (None, 1, 1)         0           sequence_pooling_layer_112[0][0] 
                                                                 sequence_pooling_layer_113[0][0] 
                                                                 sequence_pooling_layer_114[0][0] 
                                                                 sequence_pooling_layer_115[0][0] 
__________________________________________________________________________________________________
no_mask_78 (NoMask)             (None, 1)            0           regiondense_feature_0[0][0]      
                                                                 regiondense_feature_1[0][0]      
__________________________________________________________________________________________________
no_mask_80 (NoMask)             (None, 1, 1)         0           sequence_pooling_layer_120[0][0] 
                                                                 sequence_pooling_layer_121[0][0] 
                                                                 sequence_pooling_layer_122[0][0] 
                                                                 sequence_pooling_layer_123[0][0] 
__________________________________________________________________________________________________
no_mask_81 (NoMask)             (None, 1)            0           regiondense_feature_0[0][0]      
                                                                 regiondense_feature_1[0][0]      
__________________________________________________________________________________________________
no_mask_84 (NoMask)             (None, 1, 1)         0           sequence_pooling_layer_128[0][0] 
                                                                 sequence_pooling_layer_129[0][0] 
                                                                 sequence_pooling_layer_130[0][0] 
                                                                 sequence_pooling_layer_131[0][0] 
__________________________________________________________________________________________________
no_mask_85 (NoMask)             (None, 1)            0           regiondense_feature_0[0][0]      
                                                                 regiondense_feature_1[0][0]      
__________________________________________________________________________________________________
no_mask_87 (NoMask)             (None, 1, 1)         0           sequence_pooling_layer_136[0][0] 
                                                                 sequence_pooling_layer_137[0][0] 
                                                                 sequence_pooling_layer_138[0][0] 
                                                                 sequence_pooling_layer_139[0][0] 
__________________________________________________________________________________________________
no_mask_88 (NoMask)             (None, 1)            0           regiondense_feature_0[0][0]      
                                                                 regiondense_feature_1[0][0]      
__________________________________________________________________________________________________
no_mask_90 (NoMask)             (None, 1, 1)         0           sequence_pooling_layer_144[0][0] 
                                                                 sequence_pooling_layer_145[0][0] 
                                                                 sequence_pooling_layer_146[0][0] 
                                                                 sequence_pooling_layer_147[0][0] 
__________________________________________________________________________________________________
no_mask_91 (NoMask)             (None, 1)            0           regiondense_feature_0[0][0]      
                                                                 regiondense_feature_1[0][0]      
__________________________________________________________________________________________________
no_mask_93 (NoMask)             (None, 1, 1)         0           sequence_pooling_layer_152[0][0] 
                                                                 sequence_pooling_layer_153[0][0] 
                                                                 sequence_pooling_layer_154[0][0] 
                                                                 sequence_pooling_layer_155[0][0] 
__________________________________________________________________________________________________
no_mask_94 (NoMask)             (None, 1)            0           regiondense_feature_0[0][0]      
                                                                 regiondense_feature_1[0][0]      
__________________________________________________________________________________________________
concatenate_57 (Concatenate)    (None, 1, 4)         0           no_mask_71[0][0]                 
                                                                 no_mask_71[1][0]                 
                                                                 no_mask_71[2][0]                 
                                                                 no_mask_71[3][0]                 
__________________________________________________________________________________________________
concatenate_58 (Concatenate)    (None, 2)            0           no_mask_72[0][0]                 
                                                                 no_mask_72[1][0]                 
__________________________________________________________________________________________________
concatenate_59 (Concatenate)    (None, 1, 4)         0           no_mask_74[0][0]                 
                                                                 no_mask_74[1][0]                 
                                                                 no_mask_74[2][0]                 
                                                                 no_mask_74[3][0]                 
__________________________________________________________________________________________________
concatenate_60 (Concatenate)    (None, 2)            0           no_mask_75[0][0]                 
                                                                 no_mask_75[1][0]                 
__________________________________________________________________________________________________
concatenate_61 (Concatenate)    (None, 1, 4)         0           no_mask_77[0][0]                 
                                                                 no_mask_77[1][0]                 
                                                                 no_mask_77[2][0]                 
                                                                 no_mask_77[3][0]                 
__________________________________________________________________________________________________
concatenate_62 (Concatenate)    (None, 2)            0           no_mask_78[0][0]                 
                                                                 no_mask_78[1][0]                 
__________________________________________________________________________________________________
concatenate_63 (Concatenate)    (None, 1, 4)         0           no_mask_80[0][0]                 
                                                                 no_mask_80[1][0]                 
                                                                 no_mask_80[2][0]                 
                                                                 no_mask_80[3][0]                 
__________________________________________________________________________________________________
concatenate_64 (Concatenate)    (None, 2)            0           no_mask_81[0][0]                 
                                                                 no_mask_81[1][0]                 
__________________________________________________________________________________________________
concatenate_66 (Concatenate)    (None, 1, 4)         0           no_mask_84[0][0]                 
                                                                 no_mask_84[1][0]                 
                                                                 no_mask_84[2][0]                 
                                                                 no_mask_84[3][0]                 
__________________________________________________________________________________________________
concatenate_67 (Concatenate)    (None, 2)            0           no_mask_85[0][0]                 
                                                                 no_mask_85[1][0]                 
__________________________________________________________________________________________________
concatenate_68 (Concatenate)    (None, 1, 4)         0           no_mask_87[0][0]                 
                                                                 no_mask_87[1][0]                 
                                                                 no_mask_87[2][0]                 
                                                                 no_mask_87[3][0]                 
__________________________________________________________________________________________________
concatenate_69 (Concatenate)    (None, 2)            0           no_mask_88[0][0]                 
                                                                 no_mask_88[1][0]                 
__________________________________________________________________________________________________
concatenate_70 (Concatenate)    (None, 1, 4)         0           no_mask_90[0][0]                 
                                                                 no_mask_90[1][0]                 
                                                                 no_mask_90[2][0]                 
                                                                 no_mask_90[3][0]                 
__________________________________________________________________________________________________
concatenate_71 (Concatenate)    (None, 2)            0           no_mask_91[0][0]                 
                                                                 no_mask_91[1][0]                 
__________________________________________________________________________________________________
concatenate_72 (Concatenate)    (None, 1, 4)         0           no_mask_93[0][0]                 
                                                                 no_mask_93[1][0]                 
                                                                 no_mask_93[2][0]                 
                                                                 no_mask_93[3][0]                 
__________________________________________________________________________________________________
concatenate_73 (Concatenate)    (None, 2)            0           no_mask_94[0][0]                 
                                                                 no_mask_94[1][0]                 
__________________________________________________________________________________________________
linear_8 (Linear)               (None, 1)            2           concatenate_57[0][0]             
                                                                 concatenate_58[0][0]             
__________________________________________________________________________________________________
linear_9 (Linear)               (None, 1)            2           concatenate_59[0][0]             
                                                                 concatenate_60[0][0]             
__________________________________________________________________________________________________
linear_10 (Linear)              (None, 1)            2           concatenate_61[0][0]             
                                                                 concatenate_62[0][0]             
__________________________________________________________________________________________________
linear_11 (Linear)              (None, 1)            2           concatenate_63[0][0]             
                                                                 concatenate_64[0][0]             
__________________________________________________________________________________________________
linear_12 (Linear)              (None, 1)            2           concatenate_66[0][0]             
                                                                 concatenate_67[0][0]             
__________________________________________________________________________________________________
linear_13 (Linear)              (None, 1)            2           concatenate_68[0][0]             
                                                                 concatenate_69[0][0]             
__________________________________________________________________________________________________
linear_14 (Linear)              (None, 1)            2           concatenate_70[0][0]             
                                                                 concatenate_71[0][0]             
__________________________________________________________________________________________________
linear_15 (Linear)              (None, 1)            2           concatenate_72[0][0]             
                                                                 concatenate_73[0][0]             
__________________________________________________________________________________________________
no_mask_73 (NoMask)             (None, 1)            0           linear_8[0][0]                   
__________________________________________________________________________________________________
no_mask_76 (NoMask)             (None, 1)            0           linear_9[0][0]                   
__________________________________________________________________________________________________
no_mask_79 (NoMask)             (None, 1)            0           linear_10[0][0]                  
__________________________________________________________________________________________________
no_mask_82 (NoMask)             (None, 1)            0           linear_11[0][0]                  
__________________________________________________________________________________________________
no_mask_86 (NoMask)             (None, 1)            0           linear_12[0][0]                  
__________________________________________________________________________________________________
no_mask_89 (NoMask)             (None, 1)            0           linear_13[0][0]                  
__________________________________________________________________________________________________
no_mask_92 (NoMask)             (None, 1)            0           linear_14[0][0]                  
__________________________________________________________________________________________________
no_mask_95 (NoMask)             (None, 1)            0           linear_15[0][0]                  
__________________________________________________________________________________________________
no_mask_83 (NoMask)             (None, 1)            0           no_mask_73[0][0]                 
                                                                 no_mask_76[0][0]                 
                                                                 no_mask_79[0][0]                 
                                                                 no_mask_82[0][0]                 
__________________________________________________________________________________________________
prediction_layer_11 (Prediction (None, 1)            0           no_mask_86[0][0]                 
__________________________________________________________________________________________________
prediction_layer_12 (Prediction (None, 1)            0           no_mask_89[0][0]                 
__________________________________________________________________________________________________
prediction_layer_13 (Prediction (None, 1)            0           no_mask_92[0][0]                 
__________________________________________________________________________________________________
prediction_layer_14 (Prediction (None, 1)            0           no_mask_95[0][0]                 
__________________________________________________________________________________________________
concatenate_65 (Concatenate)    (None, 4)            0           no_mask_83[0][0]                 
                                                                 no_mask_83[1][0]                 
                                                                 no_mask_83[2][0]                 
                                                                 no_mask_83[3][0]                 
__________________________________________________________________________________________________
no_mask_96 (NoMask)             (None, 1)            0           prediction_layer_11[0][0]        
                                                                 prediction_layer_12[0][0]        
                                                                 prediction_layer_13[0][0]        
                                                                 prediction_layer_14[0][0]        
__________________________________________________________________________________________________
activation_40 (Activation)      (None, 4)            0           concatenate_65[0][0]             
__________________________________________________________________________________________________
concatenate_74 (Concatenate)    (None, 4)            0           no_mask_96[0][0]                 
                                                                 no_mask_96[1][0]                 
                                                                 no_mask_96[2][0]                 
                                                                 no_mask_96[3][0]                 
__________________________________________________________________________________________________
dot (Dot)                       (None, 1)            0           activation_40[0][0]              
                                                                 concatenate_74[0][0]             
==================================================================================================
Total params: 144
Trainable params: 144
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 8s - loss: 0.2551 - binary_crossentropy: 0.7032500/500 [==============================] - 6s 12ms/sample - loss: 0.2524 - binary_crossentropy: 0.6979 - val_loss: 0.2510 - val_binary_crossentropy: 0.7478

  #### metrics   #################################################### 
{'MSE': 0.25117893146530423}

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
Model: "model_11"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
regionweighted_seq (InputLayer) [(None, 3)]          0                                            
__________________________________________________________________________________________________
region_10sparse_seq_emb_regionw (None, 3, 1)         2           regionweighted_seq[0][0]         
__________________________________________________________________________________________________
regionweighted_seq_seq_length ( [(None, 1)]          0                                            
__________________________________________________________________________________________________
regionweight (InputLayer)       [(None, 3, 1)]       0                                            
__________________________________________________________________________________________________
regionsequence_sum (InputLayer) [(None, 5)]          0                                            
__________________________________________________________________________________________________
regionsequence_mean (InputLayer [(None, 7)]          0                                            
__________________________________________________________________________________________________
regionsequence_max (InputLayer) [(None, 9)]          0                                            
__________________________________________________________________________________________________
region_20sparse_seq_emb_regionw (None, 3, 1)         2           regionweighted_seq[0][0]         
__________________________________________________________________________________________________
region_30sparse_seq_emb_regionw (None, 3, 1)         2           regionweighted_seq[0][0]         
__________________________________________________________________________________________________
region_40sparse_seq_emb_regionw (None, 3, 1)         2           regionweighted_seq[0][0]         
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 3, 1)         2           regionweighted_seq[0][0]         
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 3, 1)         2           regionweighted_seq[0][0]         
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 3, 1)         2           regionweighted_seq[0][0]         
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 3, 1)         2           regionweighted_seq[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_24 (Wei (None, 3, 1)         0           region_10sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 5, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 9, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_26 (Wei (None, 3, 1)         0           region_20sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 5, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 9, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_28 (Wei (None, 3, 1)         0           region_30sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 5, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 9, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_30 (Wei (None, 3, 1)         0           region_40sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 5, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 9, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_32 (Wei (None, 3, 1)         0           learner_10sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 5, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 9, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_34 (Wei (None, 3, 1)         0           learner_20sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 5, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 9, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_36 (Wei (None, 3, 1)         0           learner_30sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 5, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 9, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_38 (Wei (None, 3, 1)         0           learner_40sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 5, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 9, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
sequence_pooling_layer_96 (Sequ (None, 1, 1)         0           weighted_sequence_layer_24[0][0] 
                                                                 regionweighted_seq_seq_length[0][
__________________________________________________________________________________________________
sequence_pooling_layer_97 (Sequ (None, 1, 1)         0           region_10sparse_seq_emb_regionseq
__________________________________________________________________________________________________
sequence_pooling_layer_98 (Sequ (None, 1, 1)         0           region_10sparse_seq_emb_regionseq
__________________________________________________________________________________________________
sequence_pooling_layer_99 (Sequ (None, 1, 1)         0           region_10sparse_seq_emb_regionseq
__________________________________________________________________________________________________
regiondense_feature_0 (InputLay [(None, 1)]          0                                            
__________________________________________________________________________________________________
regiondense_feature_1 (InputLay [(None, 1)]          0                                            
__________________________________________________________________________________________________
sequence_pooling_layer_104 (Seq (None, 1, 1)         0           weighted_sequence_layer_26[0][0] 
                                                                 regionweighted_seq_seq_length[0][
__________________________________________________________________________________________________
sequence_pooling_layer_105 (Seq (None, 1, 1)         0           region_20sparse_seq_emb_regionseq
__________________________________________________________________________________________________
sequence_pooling_layer_106 (Seq (None, 1, 1)         0           region_20sparse_seq_emb_regionseq
__________________________________________________________________________________________________
sequence_pooling_layer_107 (Seq (None, 1, 1)         0           region_20sparse_seq_emb_regionseq
__________________________________________________________________________________________________
sequence_pooling_layer_112 (Seq (None, 1, 1)         0           weighted_sequence_layer_28[0][0] 
                                                                 regionweighted_seq_seq_length[0][
__________________________________________________________________________________________________
sequence_pooling_layer_113 (Seq (None, 1, 1)         0           region_30sparse_seq_emb_regionseq
__________________________________________________________________________________________________
sequence_pooling_layer_114 (Seq (None, 1, 1)         0           region_30sparse_seq_emb_regionseq
__________________________________________________________________________________________________
sequence_pooling_layer_115 (Seq (None, 1, 1)         0           region_30sparse_seq_emb_regionseq
__________________________________________________________________________________________________
sequence_pooling_layer_120 (Seq (None, 1, 1)         0           weighted_sequence_layer_30[0][0] 
                                                                 regionweighted_seq_seq_length[0][
__________________________________________________________________________________________________
sequence_pooling_layer_121 (Seq (None, 1, 1)         0           region_40sparse_seq_emb_regionseq
__________________________________________________________________________________________________
sequence_pooling_layer_122 (Seq (None, 1, 1)         0           region_40sparse_seq_emb_regionseq
__________________________________________________________________________________________________
sequence_pooling_layer_123 (Seq (None, 1, 1)         0           region_40sparse_seq_emb_regionseq
__________________________________________________________________________________________________
sequence_pooling_layer_128 (Seq (None, 1, 1)         0           weighted_sequence_layer_32[0][0] 
                                                                 regionweighted_seq_seq_length[0][
__________________________________________________________________________________________________
sequence_pooling_layer_129 (Seq (None, 1, 1)         0           learner_10sparse_seq_emb_regionse
__________________________________________________________________________________________________
sequence_pooling_layer_130 (Seq (None, 1, 1)         0           learner_10sparse_seq_emb_regionse
__________________________________________________________________________________________________
sequence_pooling_layer_131 (Seq (None, 1, 1)         0           learner_10sparse_seq_emb_regionse
__________________________________________________________________________________________________
sequence_pooling_layer_136 (Seq (None, 1, 1)         0           weighted_sequence_layer_34[0][0] 
                                                                 regionweighted_seq_seq_length[0][
__________________________________________________________________________________________________
sequence_pooling_layer_137 (Seq (None, 1, 1)         0           learner_20sparse_seq_emb_regionse
__________________________________________________________________________________________________
sequence_pooling_layer_138 (Seq (None, 1, 1)         0           learner_20sparse_seq_emb_regionse
__________________________________________________________________________________________________
sequence_pooling_layer_139 (Seq (None, 1, 1)         0           learner_20sparse_seq_emb_regionse
__________________________________________________________________________________________________
sequence_pooling_layer_144 (Seq (None, 1, 1)         0           weighted_sequence_layer_36[0][0] 
                                                                 regionweighted_seq_seq_length[0][
__________________________________________________________________________________________________
sequence_pooling_layer_145 (Seq (None, 1, 1)         0           learner_30sparse_seq_emb_regionse
__________________________________________________________________________________________________
sequence_pooling_layer_146 (Seq (None, 1, 1)         0           learner_30sparse_seq_emb_regionse
__________________________________________________________________________________________________
sequence_pooling_layer_147 (Seq (None, 1, 1)         0           learner_30sparse_seq_emb_regionse
__________________________________________________________________________________________________
sequence_pooling_layer_152 (Seq (None, 1, 1)         0           weighted_sequence_layer_38[0][0] 
                                                                 regionweighted_seq_seq_length[0][
__________________________________________________________________________________________________
sequence_pooling_layer_153 (Seq (None, 1, 1)         0           learner_40sparse_seq_emb_regionse
__________________________________________________________________________________________________
sequence_pooling_layer_154 (Seq (None, 1, 1)         0           learner_40sparse_seq_emb_regionse
__________________________________________________________________________________________________
sequence_pooling_layer_155 (Seq (None, 1, 1)         0           learner_40sparse_seq_emb_regionse
__________________________________________________________________________________________________
no_mask_71 (NoMask)             (None, 1, 1)         0           sequence_pooling_layer_96[0][0]  
                                                                 sequence_pooling_layer_97[0][0]  
                                                                 sequence_pooling_layer_98[0][0]  
                                                                 sequence_pooling_layer_99[0][0]  
__________________________________________________________________________________________________
no_mask_72 (NoMask)             (None, 1)            0           regiondense_feature_0[0][0]      
                                                                 regiondense_feature_1[0][0]      
__________________________________________________________________________________________________
no_mask_74 (NoMask)             (None, 1, 1)         0           sequence_pooling_layer_104[0][0] 
                                                                 sequence_pooling_layer_105[0][0] 
                                                                 sequence_pooling_layer_106[0][0] 
                                                                 sequence_pooling_layer_107[0][0] 
__________________________________________________________________________________________________
no_mask_75 (NoMask)             (None, 1)            0           regiondense_feature_0[0][0]      
                                                                 regiondense_feature_1[0][0]      
__________________________________________________________________________________________________
no_mask_77 (NoMask)             (None, 1, 1)         0           sequence_pooling_layer_112[0][0] 
                                                                 sequence_pooling_layer_113[0][0] 
                                                                 sequence_pooling_layer_114[0][0] 
                                                                 sequence_pooling_layer_115[0][0] 
__________________________________________________________________________________________________
no_mask_78 (NoMask)             (None, 1)            0           regiondense_feature_0[0][0]      
                                                                 regiondense_feature_1[0][0]      
__________________________________________________________________________________________________
no_mask_80 (NoMask)             (None, 1, 1)         0           sequence_pooling_layer_120[0][0] 
                                                                 sequence_pooling_layer_121[0][0] 
                                                                 sequence_pooling_layer_122[0][0] 
                                                                 sequence_pooling_layer_123[0][0] 
__________________________________________________________________________________________________
no_mask_81 (NoMask)             (None, 1)            0           regiondense_feature_0[0][0]      
                                                                 regiondense_feature_1[0][0]      
__________________________________________________________________________________________________
no_mask_84 (NoMask)             (None, 1, 1)         0           sequence_pooling_layer_128[0][0] 
                                                                 sequence_pooling_layer_129[0][0] 
                                                                 sequence_pooling_layer_130[0][0] 
                                                                 sequence_pooling_layer_131[0][0] 
__________________________________________________________________________________________________
no_mask_85 (NoMask)             (None, 1)            0           regiondense_feature_0[0][0]      
                                                                 regiondense_feature_1[0][0]      
__________________________________________________________________________________________________
no_mask_87 (NoMask)             (None, 1, 1)         0           sequence_pooling_layer_136[0][0] 
                                                                 sequence_pooling_layer_137[0][0] 
                                                                 sequence_pooling_layer_138[0][0] 
                                                                 sequence_pooling_layer_139[0][0] 
__________________________________________________________________________________________________
no_mask_88 (NoMask)             (None, 1)            0           regiondense_feature_0[0][0]      
                                                                 regiondense_feature_1[0][0]      
__________________________________________________________________________________________________
no_mask_90 (NoMask)             (None, 1, 1)         0           sequence_pooling_layer_144[0][0] 
                                                                 sequence_pooling_layer_145[0][0] 
                                                                 sequence_pooling_layer_146[0][0] 
                                                                 sequence_pooling_layer_147[0][0] 
__________________________________________________________________________________________________
no_mask_91 (NoMask)             (None, 1)            0           regiondense_feature_0[0][0]      
                                                                 regiondense_feature_1[0][0]      
__________________________________________________________________________________________________
no_mask_93 (NoMask)             (None, 1, 1)         0           sequence_pooling_layer_152[0][0] 
                                                                 sequence_pooling_layer_153[0][0] 
                                                                 sequence_pooling_layer_154[0][0] 
                                                                 sequence_pooling_layer_155[0][0] 
__________________________________________________________________________________________________
no_mask_94 (NoMask)             (None, 1)            0           regiondense_feature_0[0][0]      
                                                                 regiondense_feature_1[0][0]      
__________________________________________________________________________________________________
concatenate_57 (Concatenate)    (None, 1, 4)         0           no_mask_71[0][0]                 
                                                                 no_mask_71[1][0]                 
                                                                 no_mask_71[2][0]                 
                                                                 no_mask_71[3][0]                 
__________________________________________________________________________________________________
concatenate_58 (Concatenate)    (None, 2)            0           no_mask_72[0][0]                 
                                                                 no_mask_72[1][0]                 
__________________________________________________________________________________________________
concatenate_59 (Concatenate)    (None, 1, 4)         0           no_mask_74[0][0]                 
                                                                 no_mask_74[1][0]                 
                                                                 no_mask_74[2][0]                 
                                                                 no_mask_74[3][0]                 
__________________________________________________________________________________________________
concatenate_60 (Concatenate)    (None, 2)            0           no_mask_75[0][0]                 
                                                                 no_mask_75[1][0]                 
__________________________________________________________________________________________________
concatenate_61 (Concatenate)    (None, 1, 4)         0           no_mask_77[0][0]                 
                                                                 no_mask_77[1][0]                 
                                                                 no_mask_77[2][0]                 
                                                                 no_mask_77[3][0]                 
__________________________________________________________________________________________________
concatenate_62 (Concatenate)    (None, 2)            0           no_mask_78[0][0]                 
                                                                 no_mask_78[1][0]                 
__________________________________________________________________________________________________
concatenate_63 (Concatenate)    (None, 1, 4)         0           no_mask_80[0][0]                 
                                                                 no_mask_80[1][0]                 
                                                                 no_mask_80[2][0]                 
                                                                 no_mask_80[3][0]                 
__________________________________________________________________________________________________
concatenate_64 (Concatenate)    (None, 2)            0           no_mask_81[0][0]                 
                                                                 no_mask_81[1][0]                 
__________________________________________________________________________________________________
concatenate_66 (Concatenate)    (None, 1, 4)         0           no_mask_84[0][0]                 
                                                                 no_mask_84[1][0]                 
                                                                 no_mask_84[2][0]                 
                                                                 no_mask_84[3][0]                 
__________________________________________________________________________________________________
concatenate_67 (Concatenate)    (None, 2)            0           no_mask_85[0][0]                 
                                                                 no_mask_85[1][0]                 
__________________________________________________________________________________________________
concatenate_68 (Concatenate)    (None, 1, 4)         0           no_mask_87[0][0]                 
                                                                 no_mask_87[1][0]                 
                                                                 no_mask_87[2][0]                 
                                                                 no_mask_87[3][0]                 
__________________________________________________________________________________________________
concatenate_69 (Concatenate)    (None, 2)            0           no_mask_88[0][0]                 
                                                                 no_mask_88[1][0]                 
__________________________________________________________________________________________________
concatenate_70 (Concatenate)    (None, 1, 4)         0           no_mask_90[0][0]                 
                                                                 no_mask_90[1][0]                 
                                                                 no_mask_90[2][0]                 
                                                                 no_mask_90[3][0]                 
__________________________________________________________________________________________________
concatenate_71 (Concatenate)    (None, 2)            0           no_mask_91[0][0]                 
                                                                 no_mask_91[1][0]                 
__________________________________________________________________________________________________
concatenate_72 (Concatenate)    (None, 1, 4)         0           no_mask_93[0][0]                 
                                                                 no_mask_93[1][0]                 
                                                                 no_mask_93[2][0]                 
                                                                 no_mask_93[3][0]                 
__________________________________________________________________________________________________
concatenate_73 (Concatenate)    (None, 2)            0           no_mask_94[0][0]                 
                                                                 no_mask_94[1][0]                 
__________________________________________________________________________________________________
linear_8 (Linear)               (None, 1)            2           concatenate_57[0][0]             
                                                                 concatenate_58[0][0]             
__________________________________________________________________________________________________
linear_9 (Linear)               (None, 1)            2           concatenate_59[0][0]             
                                                                 concatenate_60[0][0]             
__________________________________________________________________________________________________
linear_10 (Linear)              (None, 1)            2           concatenate_61[0][0]             
                                                                 concatenate_62[0][0]             
__________________________________________________________________________________________________
linear_11 (Linear)              (None, 1)            2           concatenate_63[0][0]             
                                                                 concatenate_64[0][0]             
__________________________________________________________________________________________________
linear_12 (Linear)              (None, 1)            2           concatenate_66[0][0]             
                                                                 concatenate_67[0][0]             
__________________________________________________________________________________________________
linear_13 (Linear)              (None, 1)            2           concatenate_68[0][0]             
                                                                 concatenate_69[0][0]             
__________________________________________________________________________________________________
linear_14 (Linear)              (None, 1)            2           concatenate_70[0][0]             
                                                                 concatenate_71[0][0]             
__________________________________________________________________________________________________
linear_15 (Linear)              (None, 1)            2           concatenate_72[0][0]             
                                                                 concatenate_73[0][0]             
__________________________________________________________________________________________________
no_mask_73 (NoMask)             (None, 1)            0           linear_8[0][0]                   
__________________________________________________________________________________________________
no_mask_76 (NoMask)             (None, 1)            0           linear_9[0][0]                   
__________________________________________________________________________________________________
no_mask_79 (NoMask)             (None, 1)            0           linear_10[0][0]                  
__________________________________________________________________________________________________
no_mask_82 (NoMask)             (None, 1)            0           linear_11[0][0]                  
__________________________________________________________________________________________________
no_mask_86 (NoMask)             (None, 1)            0           linear_12[0][0]                  
__________________________________________________________________________________________________
no_mask_89 (NoMask)             (None, 1)            0           linear_13[0][0]                  
__________________________________________________________________________________________________
no_mask_92 (NoMask)             (None, 1)            0           linear_14[0][0]                  
__________________________________________________________________________________________________
no_mask_95 (NoMask)             (None, 1)            0           linear_15[0][0]                  
__________________________________________________________________________________________________
no_mask_83 (NoMask)             (None, 1)            0           no_mask_73[0][0]                 
                                                                 no_mask_76[0][0]                 
                                                                 no_mask_79[0][0]                 
                                                                 no_mask_82[0][0]                 
__________________________________________________________________________________________________
prediction_layer_11 (Prediction (None, 1)            0           no_mask_86[0][0]                 
__________________________________________________________________________________________________
prediction_layer_12 (Prediction (None, 1)            0           no_mask_89[0][0]                 
__________________________________________________________________________________________________
prediction_layer_13 (Prediction (None, 1)            0           no_mask_92[0][0]                 
__________________________________________________________________________________________________
prediction_layer_14 (Prediction (None, 1)            0           no_mask_95[0][0]                 
__________________________________________________________________________________________________
concatenate_65 (Concatenate)    (None, 4)            0           no_mask_83[0][0]                 
                                                                 no_mask_83[1][0]                 
                                                                 no_mask_83[2][0]                 
                                                                 no_mask_83[3][0]                 
__________________________________________________________________________________________________
no_mask_96 (NoMask)             (None, 1)            0           prediction_layer_11[0][0]        
                                                                 prediction_layer_12[0][0]        
                                                                 prediction_layer_13[0][0]        
                                                                 prediction_layer_14[0][0]        
__________________________________________________________________________________________________
activation_40 (Activation)      (None, 4)            0           concatenate_65[0][0]             
__________________________________________________________________________________________________
concatenate_74 (Concatenate)    (None, 4)            0           no_mask_96[0][0]                 
                                                                 no_mask_96[1][0]                 
                                                                 no_mask_96[2][0]                 
                                                                 no_mask_96[3][0]                 
__________________________________________________________________________________________________
dot (Dot)                       (None, 1)            0           activation_40[0][0]              
                                                                 concatenate_74[0][0]             
==================================================================================================
Total params: 144
Trainable params: 144
Non-trainable params: 0
__________________________________________________________________________________________________

  #### Loading params   ############################################## 

  #### Path params   ################################################# 

  #### Model params   ################################################ 
{'model_name': 'NFM', 'optimization': 'adam', 'cost': 'mse'} {'dataset_type': 'synthesis', 'sample_size': 8, 'test_size': 0.2, 'dataset_name': 'NFM', 'sparse_feature_num': 1, 'dense_feature_num': 1} {'batch_size': 100, 'epochs': 1, 'validation_split': 0.5} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/deepctr/model_NFM.h5'}

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 
Model: "model_12"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
weighted_seq (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
weighted_seq_seq_length (InputL [(None, 1)]          0                                            
__________________________________________________________________________________________________
weight (InputLayer)             [(None, 3, 1)]       0                                            
__________________________________________________________________________________________________
sequence_sum (InputLayer)       [(None, 1)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 9)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_40 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 1, 4)         36          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 5, 4)         20          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 9, 4)         20          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         32          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_160 (Seq (None, 1, 4)         0           weighted_sequence_layer_40[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_161 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_162 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_163 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
no_mask_100 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_160[0][0] 
                                                                 sequence_pooling_layer_161[0][0] 
                                                                 sequence_pooling_layer_162[0][0] 
                                                                 sequence_pooling_layer_163[0][0] 
__________________________________________________________________________________________________
concatenate_76 (Concatenate)    (None, 5, 4)         0           no_mask_100[0][0]                
                                                                 no_mask_100[1][0]                
                                                                 no_mask_100[2][0]                
                                                                 no_mask_100[3][0]                
                                                                 no_mask_100[4][0]                
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
dense_feature_0 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
bi_interaction_pooling (BiInter (None, 1, 4)         0           concatenate_76[0][0]             
__________________________________________________________________________________________________
weighted_sequence_layer_41 (Wei (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         9           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         5           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         5           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_101 (NoMask)            (None, 1, 4)         0           bi_interaction_pooling[0][0]     
__________________________________________________________________________________________________
no_mask_102 (NoMask)            (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_164 (Seq (None, 1, 1)         0           weighted_sequence_layer_41[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_165 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_166 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_167 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
flatten_26 (Flatten)            (None, 4)            0           no_mask_101[0][0]                
__________________________________________________________________________________________________
flatten_27 (Flatten)            (None, 1)            0           no_mask_102[0][0]                
__________________________________________________________________________________________________
no_mask_97 (NoMask)             (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_164[0][0] 
                                                                 sequence_pooling_layer_165[0][0] 
                                                                 sequence_pooling_layer_166[0][0] 
                                                                 sequence_pooling_layer_167[0][0] 
__________________________________________________________________________________________________
no_mask_103 (NoMask)            multiple             0           flatten_26[0][0]                 
                                                                 flatten_27[0][0]                 
__________________________________________________________________________________________________
concatenate_75 (Concatenate)    (None, 1, 5)         0           no_mask_97[0][0]                 
                                                                 no_mask_97[1][0]                 
                                                                 no_mask_97[2][0]                 
                                                                 no_mask_97[3][0]                 
                                                                 no_mask_97[4][0]                 
__________________________________________________________________________________________________
no_mask_98 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
concatenate_77 (Concatenate)    (None, 5)            0           no_mask_103[0][0]                
                                                                 no_mask_103[1][0]                
__________________________________________________________________________________________________
linear_16 (Linear)              (None, 1)            1           concatenate_75[0][0]             
                                                                 no_mask_98[0][0]                 
__________________________________________________________________________________________________
dnn_17 (DNN)                    (None, 32)           1248        concatenate_77[0][0]             
__________________________________________________________________________________________________
no_mask_99 (NoMask)             (None, 1)            0           linear_16[0][0]                  
__________________________________________________________________________________________________
dense_10 (Dense)                (None, 1)            32          dnn_17[0][0]                     
__________________________________________________________________________________________________
add_26 (Add)                    (None, 1)            0           no_mask_99[0][0]                 
                                                                 dense_10[0][0]                   
__________________________________________________________________________________________________
prediction_layer_15 (Prediction (None, 1)            1           add_26[0][0]                     
==================================================================================================
Total params: 1,427
Trainable params: 1,427
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 7s - loss: 0.2531 - binary_crossentropy: 0.6992500/500 [==============================] - 6s 11ms/sample - loss: 0.2497 - binary_crossentropy: 0.6926 - val_loss: 0.2515 - val_binary_crossentropy: 0.6962

  #### metrics   #################################################### 
{'MSE': 0.2508028579490546}

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
Model: "model_12"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
weighted_seq (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
weighted_seq_seq_length (InputL [(None, 1)]          0                                            
__________________________________________________________________________________________________
weight (InputLayer)             [(None, 3, 1)]       0                                            
__________________________________________________________________________________________________
sequence_sum (InputLayer)       [(None, 1)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 9)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_40 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 1, 4)         36          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 5, 4)         20          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 9, 4)         20          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         32          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_160 (Seq (None, 1, 4)         0           weighted_sequence_layer_40[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_161 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_162 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_163 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
no_mask_100 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_160[0][0] 
                                                                 sequence_pooling_layer_161[0][0] 
                                                                 sequence_pooling_layer_162[0][0] 
                                                                 sequence_pooling_layer_163[0][0] 
__________________________________________________________________________________________________
concatenate_76 (Concatenate)    (None, 5, 4)         0           no_mask_100[0][0]                
                                                                 no_mask_100[1][0]                
                                                                 no_mask_100[2][0]                
                                                                 no_mask_100[3][0]                
                                                                 no_mask_100[4][0]                
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
dense_feature_0 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
bi_interaction_pooling (BiInter (None, 1, 4)         0           concatenate_76[0][0]             
__________________________________________________________________________________________________
weighted_sequence_layer_41 (Wei (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         9           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         5           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         5           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_101 (NoMask)            (None, 1, 4)         0           bi_interaction_pooling[0][0]     
__________________________________________________________________________________________________
no_mask_102 (NoMask)            (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_164 (Seq (None, 1, 1)         0           weighted_sequence_layer_41[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_165 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_166 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_167 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
flatten_26 (Flatten)            (None, 4)            0           no_mask_101[0][0]                
__________________________________________________________________________________________________
flatten_27 (Flatten)            (None, 1)            0           no_mask_102[0][0]                
__________________________________________________________________________________________________
no_mask_97 (NoMask)             (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_164[0][0] 
                                                                 sequence_pooling_layer_165[0][0] 
                                                                 sequence_pooling_layer_166[0][0] 
                                                                 sequence_pooling_layer_167[0][0] 
__________________________________________________________________________________________________
no_mask_103 (NoMask)            multiple             0           flatten_26[0][0]                 
                                                                 flatten_27[0][0]                 
__________________________________________________________________________________________________
concatenate_75 (Concatenate)    (None, 1, 5)         0           no_mask_97[0][0]                 
                                                                 no_mask_97[1][0]                 
                                                                 no_mask_97[2][0]                 
                                                                 no_mask_97[3][0]                 
                                                                 no_mask_97[4][0]                 
__________________________________________________________________________________________________
no_mask_98 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
concatenate_77 (Concatenate)    (None, 5)            0           no_mask_103[0][0]                
                                                                 no_mask_103[1][0]                
__________________________________________________________________________________________________
linear_16 (Linear)              (None, 1)            1           concatenate_75[0][0]             
                                                                 no_mask_98[0][0]                 
__________________________________________________________________________________________________
dnn_17 (DNN)                    (None, 32)           1248        concatenate_77[0][0]             
__________________________________________________________________________________________________
no_mask_99 (NoMask)             (None, 1)            0           linear_16[0][0]                  
__________________________________________________________________________________________________
dense_10 (Dense)                (None, 1)            32          dnn_17[0][0]                     
__________________________________________________________________________________________________
add_26 (Add)                    (None, 1)            0           no_mask_99[0][0]                 
                                                                 dense_10[0][0]                   
__________________________________________________________________________________________________
prediction_layer_15 (Prediction (None, 1)            1           add_26[0][0]                     
==================================================================================================
Total params: 1,427
Trainable params: 1,427
Non-trainable params: 0
__________________________________________________________________________________________________

  #### Loading params   ############################################## 

  #### Path params   ################################################# 

  #### Model params   ################################################ 
{'model_name': 'ONN', 'optimization': 'adam', 'cost': 'mse'} {'dataset_type': 'synthesis', 'sample_size': 8, 'test_size': 0.2, 'dataset_name': 'ONN', 'sparse_feature_num': 2, 'dense_feature_num': 2, 'sequence_feature': ('sum', 'mean', 'max'), 'hash_flag': True} {'batch_size': 100, 'epochs': 1, 'validation_split': 0.5} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/deepctr/model_ONN.h5'}

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 
Model: "model_13"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_1 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
hash_14 (Hash)                  (None, 1)            0           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
hash_15 (Hash)                  (None, 1)            0           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
hash_16 (Hash)                  (None, 1)            0           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_sum (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
hash_17 (Hash)                  (None, 1)            0           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 4)]          0                                            
__________________________________________________________________________________________________
hash_18 (Hash)                  (None, 1)            0           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 1)]          0                                            
__________________________________________________________________________________________________
hash_19 (Hash)                  (None, 1)            0           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
hash_20 (Hash)                  (None, 1)            0           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
hash_21 (Hash)                  (None, 1)            0           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_spa (None, 1, 4)         12          hash_14[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_spa (None, 1, 4)         4           hash_15[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         12          hash_16[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 3, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         12          hash_17[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 4, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         12          hash_18[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 1, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         4           hash_19[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 3, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         4           hash_20[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 4, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         4           hash_21[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 1, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 3, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 4, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 3, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_max_sequenc (None, 1, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 4, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sequence_max_sequenc (None, 1, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_107 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_0_spars
__________________________________________________________________________________________________
no_mask_108 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_1_spars
__________________________________________________________________________________________________
no_mask_109 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_0_seque
__________________________________________________________________________________________________
sequence_pooling_layer_178 (Seq (None, 1, 4)         0           sparse_emb_sequence_sum_sparse_fe
__________________________________________________________________________________________________
no_mask_110 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_0_seque
__________________________________________________________________________________________________
sequence_pooling_layer_179 (Seq (None, 1, 4)         0           sparse_emb_sequence_mean_sparse_f
__________________________________________________________________________________________________
no_mask_111 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_0_seque
__________________________________________________________________________________________________
sequence_pooling_layer_180 (Seq (None, 1, 4)         0           sparse_emb_sequence_max_sparse_fe
__________________________________________________________________________________________________
no_mask_112 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_1_seque
__________________________________________________________________________________________________
sequence_pooling_layer_181 (Seq (None, 1, 4)         0           sparse_emb_sequence_sum_sparse_fe
__________________________________________________________________________________________________
no_mask_113 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_1_seque
__________________________________________________________________________________________________
sequence_pooling_layer_182 (Seq (None, 1, 4)         0           sparse_emb_sequence_mean_sparse_f
__________________________________________________________________________________________________
no_mask_114 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_1_seque
__________________________________________________________________________________________________
sequence_pooling_layer_183 (Seq (None, 1, 4)         0           sparse_emb_sequence_max_sparse_fe
__________________________________________________________________________________________________
sequence_pooling_layer_184 (Seq (None, 1, 4)         0           sparse_emb_sequence_sum_sequence_
__________________________________________________________________________________________________
sequence_pooling_layer_185 (Seq (None, 1, 4)         0           sparse_emb_sequence_mean_sequence
__________________________________________________________________________________________________
sequence_pooling_layer_186 (Seq (None, 1, 4)         0           sparse_emb_sequence_sum_sequence_
__________________________________________________________________________________________________
sequence_pooling_layer_187 (Seq (None, 1, 4)         0           sparse_emb_sequence_max_sequence_
__________________________________________________________________________________________________
sequence_pooling_layer_188 (Seq (None, 1, 4)         0           sparse_emb_sequence_mean_sequence
__________________________________________________________________________________________________
sequence_pooling_layer_189 (Seq (None, 1, 4)         0           sparse_emb_sequence_max_sequence_
__________________________________________________________________________________________________
multiply (Multiply)             (None, 1, 4)         0           no_mask_107[0][0]                
                                                                 no_mask_108[0][0]                
__________________________________________________________________________________________________
multiply_1 (Multiply)           (None, 1, 4)         0           no_mask_109[0][0]                
                                                                 sequence_pooling_layer_178[0][0] 
__________________________________________________________________________________________________
multiply_2 (Multiply)           (None, 1, 4)         0           no_mask_110[0][0]                
                                                                 sequence_pooling_layer_179[0][0] 
__________________________________________________________________________________________________
multiply_3 (Multiply)           (None, 1, 4)         0           no_mask_111[0][0]                
                                                                 sequence_pooling_layer_180[0][0] 
__________________________________________________________________________________________________
multiply_4 (Multiply)           (None, 1, 4)         0           no_mask_112[0][0]                
                                                                 sequence_pooling_layer_181[0][0] 
__________________________________________________________________________________________________
multiply_5 (Multiply)           (None, 1, 4)         0           no_mask_113[0][0]                
                                                                 sequence_pooling_layer_182[0][0] 
__________________________________________________________________________________________________
multiply_6 (Multiply)           (None, 1, 4)         0           no_mask_114[0][0]                
                                                                 sequence_pooling_layer_183[0][0] 
__________________________________________________________________________________________________
multiply_7 (Multiply)           (None, 1, 4)         0           sequence_pooling_layer_184[0][0] 
                                                                 sequence_pooling_layer_185[0][0] 
__________________________________________________________________________________________________
multiply_8 (Multiply)           (None, 1, 4)         0           sequence_pooling_layer_186[0][0] 
                                                                 sequence_pooling_layer_187[0][0] 
__________________________________________________________________________________________________
multiply_9 (Multiply)           (None, 1, 4)         0           sequence_pooling_layer_188[0][0] 
                                                                 sequence_pooling_layer_189[0][0] 
__________________________________________________________________________________________________
no_mask_115 (NoMask)            (None, 1, 4)         0           multiply[0][0]                   
                                                                 multiply_1[0][0]                 
                                                                 multiply_2[0][0]                 
                                                                 multiply_3[0][0]                 
                                                                 multiply_4[0][0]                 
                                                                 multiply_5[0][0]                 
                                                                 multiply_6[0][0]                 
                                                                 multiply_7[0][0]                 
                                                                 multiply_8[0][0]                 
                                                                 multiply_9[0][0]                 
__________________________________________________________________________________________________
concatenate_80 (Concatenate)    (None, 10, 4)        0           no_mask_115[0][0]                
                                                                 no_mask_115[1][0]                
                                                                 no_mask_115[2][0]                
                                                                 no_mask_115[3][0]                
                                                                 no_mask_115[4][0]                
                                                                 no_mask_115[5][0]                
                                                                 no_mask_115[6][0]                
                                                                 no_mask_115[7][0]                
                                                                 no_mask_115[8][0]                
                                                                 no_mask_115[9][0]                
__________________________________________________________________________________________________
flatten_28 (Flatten)            (None, 40)           0           concatenate_80[0][0]             
__________________________________________________________________________________________________
dense_feature_0 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
dense_feature_1 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
batch_normalization_8 (BatchNor (None, 40)           160         flatten_28[0][0]                 
__________________________________________________________________________________________________
no_mask_117 (NoMask)            (None, 1)            0           dense_feature_0[0][0]            
                                                                 dense_feature_1[0][0]            
__________________________________________________________________________________________________
no_mask_116 (NoMask)            (None, 40)           0           batch_normalization_8[0][0]      
__________________________________________________________________________________________________
concatenate_81 (Concatenate)    (None, 2)            0           no_mask_117[0][0]                
                                                                 no_mask_117[1][0]                
__________________________________________________________________________________________________
hash_10 (Hash)                  (None, 1)            0           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
hash_11 (Hash)                  (None, 1)            0           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         7           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 4, 1)         7           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_29 (Flatten)            (None, 40)           0           no_mask_116[0][0]                
__________________________________________________________________________________________________
flatten_30 (Flatten)            (None, 2)            0           concatenate_81[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           hash_10[0][0]                    
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         1           hash_11[0][0]                    
__________________________________________________________________________________________________
sequence_pooling_layer_172 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_173 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_174 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
no_mask_118 (NoMask)            multiple             0           flatten_29[0][0]                 
                                                                 flatten_30[0][0]                 
__________________________________________________________________________________________________
no_mask_104 (NoMask)            (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_172[0][0] 
                                                                 sequence_pooling_layer_173[0][0] 
                                                                 sequence_pooling_layer_174[0][0] 
__________________________________________________________________________________________________
no_mask_105 (NoMask)            (None, 1)            0           dense_feature_0[0][0]            
                                                                 dense_feature_1[0][0]            
__________________________________________________________________________________________________
concatenate_82 (Concatenate)    (None, 42)           0           no_mask_118[0][0]                
                                                                 no_mask_118[1][0]                
__________________________________________________________________________________________________
concatenate_78 (Concatenate)    (None, 1, 5)         0           no_mask_104[0][0]                
                                                                 no_mask_104[1][0]                
                                                                 no_mask_104[2][0]                
                                                                 no_mask_104[3][0]                
                                                                 no_mask_104[4][0]                
__________________________________________________________________________________________________
concatenate_79 (Concatenate)    (None, 2)            0           no_mask_105[0][0]                
                                                                 no_mask_105[1][0]                
__________________________________________________________________________________________________
dnn_18 (DNN)                    (None, 32)           2432        concatenate_82[0][0]             
__________________________________________________________________________________________________
linear_17 (Linear)              (None, 1)            2           concatenate_78[0][0]             
                                                                 concatenate_79[0][0]             
__________________________________________________________________________________________________
dense_11 (Dense)                (None, 1)            32          dnn_18[0][0]                     
__________________________________________________________________________________________________
no_mask_106 (NoMask)            (None, 1)            0           linear_17[0][0]                  
__________________________________________________________________________________________________
add_29 (Add)                    (None, 1)            0           dense_11[0][0]                   
                                                                 no_mask_106[0][0]                
__________________________________________________________________________________________________
prediction_layer_16 (Prediction (None, 1)            1           add_29[0][0]                     
==================================================================================================
Total params: 3,069
Trainable params: 2,989
Non-trainable params: 80
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 8s - loss: 0.2984 - binary_crossentropy: 1.5740500/500 [==============================] - 6s 13ms/sample - loss: 0.2987 - binary_crossentropy: 1.6541 - val_loss: 0.2867 - val_binary_crossentropy: 1.6550

  #### metrics   #################################################### 
{'MSE': 0.28838763272032336}

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/init_ops.py:97: calling Ones.__init__ (from tensorflow.python.ops.init_ops) with dtype is deprecated and will be removed in a future version.
Instructions for updating:
Call initializer instance with the dtype argument instead of passing it to the constructor
Model: "model_13"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_1 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
hash_14 (Hash)                  (None, 1)            0           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
hash_15 (Hash)                  (None, 1)            0           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
hash_16 (Hash)                  (None, 1)            0           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_sum (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
hash_17 (Hash)                  (None, 1)            0           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 4)]          0                                            
__________________________________________________________________________________________________
hash_18 (Hash)                  (None, 1)            0           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 1)]          0                                            
__________________________________________________________________________________________________
hash_19 (Hash)                  (None, 1)            0           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
hash_20 (Hash)                  (None, 1)            0           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
hash_21 (Hash)                  (None, 1)            0           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_spa (None, 1, 4)         12          hash_14[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_spa (None, 1, 4)         4           hash_15[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         12          hash_16[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 3, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         12          hash_17[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 4, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         12          hash_18[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 1, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         4           hash_19[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 3, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         4           hash_20[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 4, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         4           hash_21[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 1, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 3, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 4, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 3, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_max_sequenc (None, 1, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 4, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sequence_max_sequenc (None, 1, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_107 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_0_spars
__________________________________________________________________________________________________
no_mask_108 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_1_spars
__________________________________________________________________________________________________
no_mask_109 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_0_seque
__________________________________________________________________________________________________
sequence_pooling_layer_178 (Seq (None, 1, 4)         0           sparse_emb_sequence_sum_sparse_fe
__________________________________________________________________________________________________
no_mask_110 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_0_seque
__________________________________________________________________________________________________
sequence_pooling_layer_179 (Seq (None, 1, 4)         0           sparse_emb_sequence_mean_sparse_f
__________________________________________________________________________________________________
no_mask_111 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_0_seque
__________________________________________________________________________________________________
sequence_pooling_layer_180 (Seq (None, 1, 4)         0           sparse_emb_sequence_max_sparse_fe
__________________________________________________________________________________________________
no_mask_112 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_1_seque
__________________________________________________________________________________________________
sequence_pooling_layer_181 (Seq (None, 1, 4)         0           sparse_emb_sequence_sum_sparse_fe
__________________________________________________________________________________________________
no_mask_113 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_1_seque
__________________________________________________________________________________________________
sequence_pooling_layer_182 (Seq (None, 1, 4)         0           sparse_emb_sequence_mean_sparse_f
__________________________________________________________________________________________________
no_mask_114 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_1_seque
__________________________________________________________________________________________________
sequence_pooling_layer_183 (Seq (None, 1, 4)         0           sparse_emb_sequence_max_sparse_fe
__________________________________________________________________________________________________
sequence_pooling_layer_184 (Seq (None, 1, 4)         0           sparse_emb_sequence_sum_sequence_
__________________________________________________________________________________________________
sequence_pooling_layer_185 (Seq (None, 1, 4)         0           sparse_emb_sequence_mean_sequence
__________________________________________________________________________________________________
sequence_pooling_layer_186 (Seq (None, 1, 4)         0           sparse_emb_sequence_sum_sequence_
__________________________________________________________________________________________________
sequence_pooling_layer_187 (Seq (None, 1, 4)         0           sparse_emb_sequence_max_sequence_
__________________________________________________________________________________________________
sequence_pooling_layer_188 (Seq (None, 1, 4)         0           sparse_emb_sequence_mean_sequence
__________________________________________________________________________________________________
sequence_pooling_layer_189 (Seq (None, 1, 4)         0           sparse_emb_sequence_max_sequence_
__________________________________________________________________________________________________
multiply (Multiply)             (None, 1, 4)         0           no_mask_107[0][0]                
                                                                 no_mask_108[0][0]                
__________________________________________________________________________________________________
multiply_1 (Multiply)           (None, 1, 4)         0           no_mask_109[0][0]                
                                                                 sequence_pooling_layer_178[0][0] 
__________________________________________________________________________________________________
multiply_2 (Multiply)           (None, 1, 4)         0           no_mask_110[0][0]                
                                                                 sequence_pooling_layer_179[0][0] 
__________________________________________________________________________________________________
multiply_3 (Multiply)           (None, 1, 4)         0           no_mask_111[0][0]                
                                                                 sequence_pooling_layer_180[0][0] 
__________________________________________________________________________________________________
multiply_4 (Multiply)           (None, 1, 4)         0           no_mask_112[0][0]                
                                                                 sequence_pooling_layer_181[0][0] 
__________________________________________________________________________________________________
multiply_5 (Multiply)           (None, 1, 4)         0           no_mask_113[0][0]                
                                                                 sequence_pooling_layer_182[0][0] 
__________________________________________________________________________________________________
multiply_6 (Multiply)           (None, 1, 4)         0           no_mask_114[0][0]                
                                                                 sequence_pooling_layer_183[0][0] 
__________________________________________________________________________________________________
multiply_7 (Multiply)           (None, 1, 4)         0           sequence_pooling_layer_184[0][0] 
                                                                 sequence_pooling_layer_185[0][0] 
__________________________________________________________________________________________________
multiply_8 (Multiply)           (None, 1, 4)         0           sequence_pooling_layer_186[0][0] 
                                                                 sequence_pooling_layer_187[0][0] 
__________________________________________________________________________________________________
multiply_9 (Multiply)           (None, 1, 4)         0           sequence_pooling_layer_188[0][0] 
                                                                 sequence_pooling_layer_189[0][0] 
__________________________________________________________________________________________________
no_mask_115 (NoMask)            (None, 1, 4)         0           multiply[0][0]                   
                                                                 multiply_1[0][0]                 
                                                                 multiply_2[0][0]                 
                                                                 multiply_3[0][0]                 
                                                                 multiply_4[0][0]                 
                                                                 multiply_5[0][0]                 
                                                                 multiply_6[0][0]                 
                                                                 multiply_7[0][0]                 
                                                                 multiply_8[0][0]                 
                                                                 multiply_9[0][0]                 
__________________________________________________________________________________________________
concatenate_80 (Concatenate)    (None, 10, 4)        0           no_mask_115[0][0]                
                                                                 no_mask_115[1][0]                
                                                                 no_mask_115[2][0]                
                                                                 no_mask_115[3][0]                
                                                                 no_mask_115[4][0]                
                                                                 no_mask_115[5][0]                
                                                                 no_mask_115[6][0]                
                                                                 no_mask_115[7][0]                
                                                                 no_mask_115[8][0]                
                                                                 no_mask_115[9][0]                
__________________________________________________________________________________________________
flatten_28 (Flatten)            (None, 40)           0           concatenate_80[0][0]             
__________________________________________________________________________________________________
dense_feature_0 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
dense_feature_1 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
batch_normalization_8 (BatchNor (None, 40)           160         flatten_28[0][0]                 
__________________________________________________________________________________________________
no_mask_117 (NoMask)            (None, 1)            0           dense_feature_0[0][0]            
                                                                 dense_feature_1[0][0]            
__________________________________________________________________________________________________
no_mask_116 (NoMask)            (None, 40)           0           batch_normalization_8[0][0]      
__________________________________________________________________________________________________
concatenate_81 (Concatenate)    (None, 2)            0           no_mask_117[0][0]                
                                                                 no_mask_117[1][0]                
__________________________________________________________________________________________________
hash_10 (Hash)                  (None, 1)            0           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
hash_11 (Hash)                  (None, 1)            0           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         7           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 4, 1)         7           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_29 (Flatten)            (None, 40)           0           no_mask_116[0][0]                
__________________________________________________________________________________________________
flatten_30 (Flatten)            (None, 2)            0           concatenate_81[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           hash_10[0][0]                    
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         1           hash_11[0][0]                    
__________________________________________________________________________________________________
sequence_pooling_layer_172 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_173 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_174 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
no_mask_118 (NoMask)            multiple             0           flatten_29[0][0]                 
                                                                 flatten_30[0][0]                 
__________________________________________________________________________________________________
no_mask_104 (NoMask)            (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_172[0][0] 
                                                                 sequence_pooling_layer_173[0][0] 
                                                                 sequence_pooling_layer_174[0][0] 
__________________________________________________________________________________________________
no_mask_105 (NoMask)            (None, 1)            0           dense_feature_0[0][0]            
                                                                 dense_feature_1[0][0]            
__________________________________________________________________________________________________
concatenate_82 (Concatenate)    (None, 42)           0           no_mask_118[0][0]                
                                                                 no_mask_118[1][0]                
__________________________________________________________________________________________________
concatenate_78 (Concatenate)    (None, 1, 5)         0           no_mask_104[0][0]                
                                                                 no_mask_104[1][0]                
                                                                 no_mask_104[2][0]                
                                                                 no_mask_104[3][0]                
                                                                 no_mask_104[4][0]                
__________________________________________________________________________________________________
concatenate_79 (Concatenate)    (None, 2)            0           no_mask_105[0][0]                
                                                                 no_mask_105[1][0]                
__________________________________________________________________________________________________
dnn_18 (DNN)                    (None, 32)           2432        concatenate_82[0][0]             
__________________________________________________________________________________________________
linear_17 (Linear)              (None, 1)            2           concatenate_78[0][0]             
                                                                 concatenate_79[0][0]             
__________________________________________________________________________________________________
dense_11 (Dense)                (None, 1)            32          dnn_18[0][0]                     
__________________________________________________________________________________________________
no_mask_106 (NoMask)            (None, 1)            0           linear_17[0][0]                  
__________________________________________________________________________________________________
add_29 (Add)                    (None, 1)            0           dense_11[0][0]                   
                                                                 no_mask_106[0][0]                
__________________________________________________________________________________________________
prediction_layer_16 (Prediction (None, 1)            1           add_29[0][0]                     
==================================================================================================
Total params: 3,069
Trainable params: 2,989
Non-trainable params: 80
__________________________________________________________________________________________________

  #### Loading params   ############################################## 

  #### Path params   ################################################# 

  #### Model params   ################################################ 
{'model_name': 'PNN', 'optimization': 'adam', 'cost': 'mse'} {'dataset_type': 'synthesis', 'sample_size': 8, 'test_size': 0.2, 'dataset_name': 'PNN', 'sparse_feature_num': 1, 'dense_feature_num': 1} {'batch_size': 100, 'epochs': 1, 'validation_split': 0.5} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/deepctr/model_PNN.h5'}

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//01_deepctr.py", line 541, in <module>
    test(pars_choice=5, **{"model_name": model_name})
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//01_deepctr.py", line 517, in test
    module, model = module_load_full("model_keras.01_deepctr", model_pars, data_pars, compute_pars, dataset=dataset)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 101, in module_load_full
    model = module.Model(model_pars=model_pars, data_pars=data_pars, compute_pars=compute_pars, **kwarg)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/01_deepctr.py", line 155, in __init__
    self.model = modeli(feature_columns, **MODEL_PARAMS[model_name])
TypeError: PNN() got an unexpected keyword argument 'embedding_size'

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
From github.com:arita37/mlmodels_store
   615a634..3741dff  master     -> origin/master
Updating 615a634..3741dff
Fast-forward
 error_list/20200519/list_log_testall_20200519.md   | 790 +--------------------
 ...-10_73f54da32a5da4768415eb9105ad096255137679.py | 627 ++++++++++++++++
 2 files changed, 629 insertions(+), 788 deletions(-)
 create mode 100644 log_pullrequest/log_pr_2020-05-19-04-10_73f54da32a5da4768415eb9105ad096255137679.py
[master 33036ec] ml_store
 1 file changed, 4954 insertions(+)
To github.com:arita37/mlmodels_store.git
   3741dff..33036ec  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//textvae.py 

  #### Loading params   ############################################## 

  #### Path params   ################################################### 

  #### Model params   ################################################# 

  #### Loading dataset   ############################################# 
Using TensorFlow backend.
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//textvae.py", line 356, in <module>
    test(pars_choice="test01")
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//textvae.py", line 327, in test
    xtuple = get_dataset(data_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//textvae.py", line 269, in get_dataset
    with codecs.open(data_pars["train_data_path"], encoding='utf-8') as f:
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/codecs.py", line 897, in open
    file = builtins.open(filename, mode, buffering)
FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/text/quora/train.csv'

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Already up to date.
[master 0feb5cf] ml_store
 1 file changed, 51 insertions(+)
To github.com:arita37/mlmodels_store.git
   33036ec..0feb5cf  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//namentity_crm_bilstm_dataloader.py 

  #### Module init   ############################################ 

  <module 'mlmodels.model_keras.namentity_crm_bilstm_dataloader' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/namentity_crm_bilstm_dataloader.py'> 

  #### Loading params   ############################################## 
Using TensorFlow backend.
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//namentity_crm_bilstm_dataloader.py", line 306, in <module>
    test_module(model_uri=MODEL_URI, param_pars=param_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/models.py", line 257, in test_module
    model_pars, data_pars, compute_pars, out_pars = module.get_params(param_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/namentity_crm_bilstm_dataloader.py", line 197, in get_params
    cf = json.load(open(data_path, mode="r"))
FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/json/refactor/namentity_crm_bilstm_dataloader.json'

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Already up to date.
[master b9cbe05] ml_store
 1 file changed, 47 insertions(+)
To github.com:arita37/mlmodels_store.git
   0feb5cf..b9cbe05  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//Autokeras.py 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//Autokeras.py", line 12, in <module>
    import autokeras as ak
ModuleNotFoundError: No module named 'autokeras'

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Already up to date.
[master 8c92817] ml_store
 1 file changed, 36 insertions(+)
To github.com:arita37/mlmodels_store.git
   b9cbe05..8c92817  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//charcnn_zhang.py 
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset

  #### Loading params   ############################################## 

  #### Loading daaset   ############################################# 
Loading data...
Data loaded from /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/text/ag_news_csv/train.csv
Data loaded from /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/text/ag_news_csv/test.csv

  #### Model init, fit   ############################################# 
Using TensorFlow backend.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/resource_variable_ops.py:1630: calling BaseResourceVariable.__init__ (from tensorflow.python.ops.resource_variable_ops) with constraint is deprecated and will be removed in a future version.
Instructions for updating:
If using Keras pass *_constraint arguments to layers.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py:4070: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.

2020-05-19 04:23:20.048851: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 AVX512F FMA
2020-05-19 04:23:20.054450: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2095074999 Hz
2020-05-19 04:23:20.054603: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x5605f75d2980 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-19 04:23:20.054617: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py:422: The name tf.global_variables is deprecated. Please use tf.compat.v1.global_variables instead.

CharCNNZhang model built: 
Model: "model_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
sent_input (InputLayer)      (None, 1014)              0         
_________________________________________________________________
embedding_1 (Embedding)      (None, 1014, 128)         8960      
_________________________________________________________________
conv1d_1 (Conv1D)            (None, 1008, 256)         229632    
_________________________________________________________________
thresholded_re_lu_1 (Thresho (None, 1008, 256)         0         
_________________________________________________________________
max_pooling1d_1 (MaxPooling1 (None, 336, 256)          0         
_________________________________________________________________
conv1d_2 (Conv1D)            (None, 330, 256)          459008    
_________________________________________________________________
thresholded_re_lu_2 (Thresho (None, 330, 256)          0         
_________________________________________________________________
max_pooling1d_2 (MaxPooling1 (None, 110, 256)          0         
_________________________________________________________________
conv1d_3 (Conv1D)            (None, 108, 256)          196864    
_________________________________________________________________
thresholded_re_lu_3 (Thresho (None, 108, 256)          0         
_________________________________________________________________
conv1d_4 (Conv1D)            (None, 106, 256)          196864    
_________________________________________________________________
thresholded_re_lu_4 (Thresho (None, 106, 256)          0         
_________________________________________________________________
conv1d_5 (Conv1D)            (None, 104, 256)          196864    
_________________________________________________________________
thresholded_re_lu_5 (Thresho (None, 104, 256)          0         
_________________________________________________________________
conv1d_6 (Conv1D)            (None, 102, 256)          196864    
_________________________________________________________________
thresholded_re_lu_6 (Thresho (None, 102, 256)          0         
_________________________________________________________________
max_pooling1d_3 (MaxPooling1 (None, 34, 256)           0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 8704)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 1024)              8913920   
_________________________________________________________________
thresholded_re_lu_7 (Thresho (None, 1024)              0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 1024)              0         
_________________________________________________________________
dense_2 (Dense)              (None, 1024)              1049600   
_________________________________________________________________
thresholded_re_lu_8 (Thresho (None, 1024)              0         
_________________________________________________________________
dropout_2 (Dropout)          (None, 1024)              0         
_________________________________________________________________
dense_3 (Dense)              (None, 4)                 4100      
=================================================================
Total params: 11,452,676
Trainable params: 11,452,676
Non-trainable params: 0
_________________________________________________________________
Loading data...
Data loaded from /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/text/ag_news_csv/train.csv
Data loaded from /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/text/ag_news_csv/test.csv
Train on 354 samples, validate on 236 samples
Epoch 1/1

128/354 [=========>....................] - ETA: 5s - loss: 1.3844
256/354 [====================>.........] - ETA: 2s - loss: 1.2571
354/354 [==============================] - 10s 27ms/step - loss: 1.2793 - val_loss: 1.9834

  #### Predict   ##################################################### 
Data loaded from /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/text/ag_news_csv/test.csv

  #### metrics   ##################################################### 
{}

  #### Plot   ######################################################## 

  #### Save/Load   ################################################### 
/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/keras/callbacks/callbacks.py:846: RuntimeWarning: Early stopping conditioned on metric `val_acc` which is not available. Available metrics are: val_loss,loss
  (self.monitor, ','.join(list(logs.keys()))), RuntimeWarning
{'path': 'ztest/ml_keras/charcnn_zhang/', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6]}
{'path': 'ztest/ml_keras/charcnn_zhang/', 'data_type': 'pandas', 'size': [0, 0, 6], 'output_size': [0, 6]}
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//charcnn_zhang.py", line 284, in <module>
    test(pars_choice="json", data_path= f"{root_path}/model_keras/charcnn_zhang.json")
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//charcnn_zhang.py", line 268, in test
    model2 = load(out_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//charcnn_zhang.py", line 118, in load
    model = load_keras(load_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 602, in load_keras
    model.model = load_model(path_file)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/keras/saving/save.py", line 146, in load_model
    loader_impl.parse_saved_model(filepath)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/saved_model/loader_impl.py", line 83, in parse_saved_model
    constants.SAVED_MODEL_FILENAME_PB))
OSError: SavedModel file does not exist at: ztest/ml_keras/charcnn_zhang//model.h5/{saved_model.pbtxt|saved_model.pb}

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Already up to date.
[master ef2b3ef] ml_store
 1 file changed, 150 insertions(+)
To github.com:arita37/mlmodels_store.git
   8c92817..ef2b3ef  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//charcnn.py 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Loading dataset   ############################################# 
Using TensorFlow backend.
Loading data...
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//charcnn.py", line 357, in <module>
    test(pars_choice="test01")
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//charcnn.py", line 320, in test
    Xtuple = get_dataset(data_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//charcnn.py", line 216, in get_dataset
    if data_pars['type'] == "npz":
KeyError: 'type'

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Already up to date.
[master 401c54d] ml_store
 1 file changed, 48 insertions(+)
To github.com:arita37/mlmodels_store.git
   ef2b3ef..401c54d  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//namentity_crm_bilstm.py 

  #### Loading params   ############################################## 

  #### Loading dataset   ############################################# 
Using TensorFlow backend.
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//namentity_crm_bilstm.py", line 348, in <module>
    test(pars_choice="json", data_path=f"model_keras/namentity_crm_bilstm.json")
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//namentity_crm_bilstm.py", line 311, in test
    Xtuple = get_dataset(data_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//namentity_crm_bilstm.py", line 193, in get_dataset
    raise Exception(f"Not support dataset yet")
Exception: Not support dataset yet

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Warning: Permanently added the RSA host key for IP address '140.82.118.4' to the list of known hosts.
Already up to date.
[master 5ac6c42] ml_store
 1 file changed, 46 insertions(+)
To github.com:arita37/mlmodels_store.git
   401c54d..5ac6c42  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//textcnn.py 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Loading dataset   ############################################# 
Loading data...
Downloading data from https://s3.amazonaws.com/text-datasets/imdb.npz

    8192/17464789 [..............................] - ETA: 0s
 1818624/17464789 [==>...........................] - ETA: 0s
 6815744/17464789 [==========>...................] - ETA: 0s
16310272/17464789 [===========================>..] - ETA: 0s
17465344/17464789 [==============================] - 0s 0us/step
Pad sequences (samples x time)...

  #### Model init, fit   ############################################# 
Using TensorFlow backend.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/resource_variable_ops.py:1630: calling BaseResourceVariable.__init__ (from tensorflow.python.ops.resource_variable_ops) with constraint is deprecated and will be removed in a future version.
Instructions for updating:
If using Keras pass *_constraint arguments to layers.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/math_grad.py:1424: where (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
2020-05-19 04:24:20.249892: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 AVX512F FMA
2020-05-19 04:24:20.254396: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2095074999 Hz
2020-05-19 04:24:20.254533: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x56376572d310 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-19 04:24:20.254547: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py:422: The name tf.global_variables is deprecated. Please use tf.compat.v1.global_variables instead.

Model: "model_1"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
input_1 (InputLayer)            (None, 40)           0                                            
__________________________________________________________________________________________________
embedding_1 (Embedding)         (None, 40, 50)       250         input_1[0][0]                    
__________________________________________________________________________________________________
conv1d_1 (Conv1D)               (None, 38, 128)      19328       embedding_1[0][0]                
__________________________________________________________________________________________________
conv1d_2 (Conv1D)               (None, 37, 128)      25728       embedding_1[0][0]                
__________________________________________________________________________________________________
conv1d_3 (Conv1D)               (None, 36, 128)      32128       embedding_1[0][0]                
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
Total params: 77,819
Trainable params: 77,819
Non-trainable params: 0
__________________________________________________________________________________________________
Loading data...
Pad sequences (samples x time)...
Train on 25000 samples, validate on 25000 samples
Epoch 1/1

 1000/25000 [>.............................] - ETA: 12s - loss: 7.7740 - accuracy: 0.4930
 2000/25000 [=>............................] - ETA: 8s - loss: 7.6666 - accuracy: 0.5000 
 3000/25000 [==>...........................] - ETA: 7s - loss: 7.6564 - accuracy: 0.5007
 4000/25000 [===>..........................] - ETA: 6s - loss: 7.7088 - accuracy: 0.4972
 5000/25000 [=====>........................] - ETA: 5s - loss: 7.6513 - accuracy: 0.5010
 6000/25000 [======>.......................] - ETA: 5s - loss: 7.6922 - accuracy: 0.4983
 7000/25000 [=======>......................] - ETA: 4s - loss: 7.6666 - accuracy: 0.5000
 8000/25000 [========>.....................] - ETA: 4s - loss: 7.7241 - accuracy: 0.4963
 9000/25000 [=========>....................] - ETA: 4s - loss: 7.7143 - accuracy: 0.4969
10000/25000 [===========>..................] - ETA: 3s - loss: 7.6804 - accuracy: 0.4991
11000/25000 [============>.................] - ETA: 3s - loss: 7.7001 - accuracy: 0.4978
12000/25000 [=============>................] - ETA: 3s - loss: 7.7024 - accuracy: 0.4977
13000/25000 [==============>...............] - ETA: 2s - loss: 7.7327 - accuracy: 0.4957
14000/25000 [===============>..............] - ETA: 2s - loss: 7.7050 - accuracy: 0.4975
15000/25000 [=================>............] - ETA: 2s - loss: 7.6932 - accuracy: 0.4983
16000/25000 [==================>...........] - ETA: 2s - loss: 7.6714 - accuracy: 0.4997
17000/25000 [===================>..........] - ETA: 1s - loss: 7.6747 - accuracy: 0.4995
18000/25000 [====================>.........] - ETA: 1s - loss: 7.6751 - accuracy: 0.4994
19000/25000 [=====================>........] - ETA: 1s - loss: 7.6707 - accuracy: 0.4997
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6820 - accuracy: 0.4990
21000/25000 [========================>.....] - ETA: 0s - loss: 7.6856 - accuracy: 0.4988
22000/25000 [=========================>....] - ETA: 0s - loss: 7.6757 - accuracy: 0.4994
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6840 - accuracy: 0.4989
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6871 - accuracy: 0.4987
25000/25000 [==============================] - 7s 280us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000

  #### save the trained model  ####################################### 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/textcnn/model.h5', 'model_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/textcnn/model.h5'}

  #### Predict   ##################################################### 
Loading data...

  #### metrics   ##################################################### 
{}

  #### Plot   ######################################################## 

  #### Save/Load   ################################################### 
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/keras/initializers.py:119: calling RandomUniform.__init__ (from tensorflow.python.ops.init_ops) with dtype is deprecated and will be removed in a future version.
Instructions for updating:
Call initializer instance with the dtype argument instead of passing it to the constructor
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/textcnn/model.h5', 'model_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/textcnn/model.h5'}
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/textcnn/model.h5', 'model_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/textcnn/model.h5'}
(<mlmodels.util.Model_empty object at 0x7f5cf2142898>, None)

  #### Module init   ############################################ 

  <module 'mlmodels.model_keras.textcnn' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/textcnn.py'> 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Model init   ############################################ 
Model: "model_2"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
input_2 (InputLayer)            (None, 40)           0                                            
__________________________________________________________________________________________________
embedding_2 (Embedding)         (None, 40, 50)       250         input_2[0][0]                    
__________________________________________________________________________________________________
conv1d_4 (Conv1D)               (None, 38, 128)      19328       embedding_2[0][0]                
__________________________________________________________________________________________________
conv1d_5 (Conv1D)               (None, 37, 128)      25728       embedding_2[0][0]                
__________________________________________________________________________________________________
conv1d_6 (Conv1D)               (None, 36, 128)      32128       embedding_2[0][0]                
__________________________________________________________________________________________________
global_max_pooling1d_4 (GlobalM (None, 128)          0           conv1d_4[0][0]                   
__________________________________________________________________________________________________
global_max_pooling1d_5 (GlobalM (None, 128)          0           conv1d_5[0][0]                   
__________________________________________________________________________________________________
global_max_pooling1d_6 (GlobalM (None, 128)          0           conv1d_6[0][0]                   
__________________________________________________________________________________________________
concatenate_2 (Concatenate)     (None, 384)          0           global_max_pooling1d_4[0][0]     
                                                                 global_max_pooling1d_5[0][0]     
                                                                 global_max_pooling1d_6[0][0]     
__________________________________________________________________________________________________
dense_2 (Dense)                 (None, 1)            385         concatenate_2[0][0]              
==================================================================================================
Total params: 77,819
Trainable params: 77,819
Non-trainable params: 0
__________________________________________________________________________________________________

  <mlmodels.model_keras.textcnn.Model object at 0x7f5cf0d45be0> 

  #### Fit   ######################################################## 
Loading data...
Pad sequences (samples x time)...
Train on 25000 samples, validate on 25000 samples
Epoch 1/1

 1000/25000 [>.............................] - ETA: 10s - loss: 7.5286 - accuracy: 0.5090
 2000/25000 [=>............................] - ETA: 7s - loss: 7.4750 - accuracy: 0.5125 
 3000/25000 [==>...........................] - ETA: 6s - loss: 7.6717 - accuracy: 0.4997
 4000/25000 [===>..........................] - ETA: 5s - loss: 7.6283 - accuracy: 0.5025
 5000/25000 [=====>........................] - ETA: 5s - loss: 7.5992 - accuracy: 0.5044
 6000/25000 [======>.......................] - ETA: 5s - loss: 7.6385 - accuracy: 0.5018
 7000/25000 [=======>......................] - ETA: 4s - loss: 7.6754 - accuracy: 0.4994
 8000/25000 [========>.....................] - ETA: 4s - loss: 7.6858 - accuracy: 0.4988
 9000/25000 [=========>....................] - ETA: 4s - loss: 7.7211 - accuracy: 0.4964
10000/25000 [===========>..................] - ETA: 3s - loss: 7.7556 - accuracy: 0.4942
11000/25000 [============>.................] - ETA: 3s - loss: 7.7600 - accuracy: 0.4939
12000/25000 [=============>................] - ETA: 3s - loss: 7.7139 - accuracy: 0.4969
13000/25000 [==============>...............] - ETA: 2s - loss: 7.6938 - accuracy: 0.4982
14000/25000 [===============>..............] - ETA: 2s - loss: 7.6699 - accuracy: 0.4998
15000/25000 [=================>............] - ETA: 2s - loss: 7.6441 - accuracy: 0.5015
16000/25000 [==================>...........] - ETA: 2s - loss: 7.6091 - accuracy: 0.5038
17000/25000 [===================>..........] - ETA: 1s - loss: 7.6134 - accuracy: 0.5035
18000/25000 [====================>.........] - ETA: 1s - loss: 7.5959 - accuracy: 0.5046
19000/25000 [=====================>........] - ETA: 1s - loss: 7.6093 - accuracy: 0.5037
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6475 - accuracy: 0.5013
21000/25000 [========================>.....] - ETA: 0s - loss: 7.6528 - accuracy: 0.5009
22000/25000 [=========================>....] - ETA: 0s - loss: 7.6764 - accuracy: 0.4994
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6740 - accuracy: 0.4995
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6628 - accuracy: 0.5002
25000/25000 [==============================] - 7s 277us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000

  #### Predict   #################################################### 
Loading data...
(array([[1.],
       [1.],
       [1.],
       ...,
       [1.],
       [1.],
       [1.]], dtype=float32), None)

  #### Get  metrics   ################################################ 

  #### Save   ######################################################## 

  #### Load   ######################################################## 

  ############ Model preparation   ################################## 

  #### Module init   ############################################ 

  <module 'mlmodels.model_keras.textcnn' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/textcnn.py'> 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Model init   ############################################ 
Model: "model_3"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
input_3 (InputLayer)            (None, 40)           0                                            
__________________________________________________________________________________________________
embedding_3 (Embedding)         (None, 40, 50)       250         input_3[0][0]                    
__________________________________________________________________________________________________
conv1d_7 (Conv1D)               (None, 38, 128)      19328       embedding_3[0][0]                
__________________________________________________________________________________________________
conv1d_8 (Conv1D)               (None, 37, 128)      25728       embedding_3[0][0]                
__________________________________________________________________________________________________
conv1d_9 (Conv1D)               (None, 36, 128)      32128       embedding_3[0][0]                
__________________________________________________________________________________________________
global_max_pooling1d_7 (GlobalM (None, 128)          0           conv1d_7[0][0]                   
__________________________________________________________________________________________________
global_max_pooling1d_8 (GlobalM (None, 128)          0           conv1d_8[0][0]                   
__________________________________________________________________________________________________
global_max_pooling1d_9 (GlobalM (None, 128)          0           conv1d_9[0][0]                   
__________________________________________________________________________________________________
concatenate_3 (Concatenate)     (None, 384)          0           global_max_pooling1d_7[0][0]     
                                                                 global_max_pooling1d_8[0][0]     
                                                                 global_max_pooling1d_9[0][0]     
__________________________________________________________________________________________________
dense_3 (Dense)                 (None, 1)            385         concatenate_3[0][0]              
==================================================================================================
Total params: 77,819
Trainable params: 77,819
Non-trainable params: 0
__________________________________________________________________________________________________

  ############ Model fit   ########################################## 
Loading data...
Pad sequences (samples x time)...
Train on 25000 samples, validate on 25000 samples
Epoch 1/1

 1000/25000 [>.............................] - ETA: 11s - loss: 7.7893 - accuracy: 0.4920
 2000/25000 [=>............................] - ETA: 8s - loss: 7.6283 - accuracy: 0.5025 
 3000/25000 [==>...........................] - ETA: 6s - loss: 7.5542 - accuracy: 0.5073
 4000/25000 [===>..........................] - ETA: 6s - loss: 7.6398 - accuracy: 0.5017
 5000/25000 [=====>........................] - ETA: 5s - loss: 7.6176 - accuracy: 0.5032
 6000/25000 [======>.......................] - ETA: 5s - loss: 7.6947 - accuracy: 0.4982
 7000/25000 [=======>......................] - ETA: 4s - loss: 7.6820 - accuracy: 0.4990
 8000/25000 [========>.....................] - ETA: 4s - loss: 7.6724 - accuracy: 0.4996
 9000/25000 [=========>....................] - ETA: 4s - loss: 7.7297 - accuracy: 0.4959
10000/25000 [===========>..................] - ETA: 3s - loss: 7.7142 - accuracy: 0.4969
11000/25000 [============>.................] - ETA: 3s - loss: 7.6806 - accuracy: 0.4991
12000/25000 [=============>................] - ETA: 3s - loss: 7.6602 - accuracy: 0.5004
13000/25000 [==============>...............] - ETA: 2s - loss: 7.6371 - accuracy: 0.5019
14000/25000 [===============>..............] - ETA: 2s - loss: 7.6381 - accuracy: 0.5019
15000/25000 [=================>............] - ETA: 2s - loss: 7.6360 - accuracy: 0.5020
16000/25000 [==================>...........] - ETA: 2s - loss: 7.6369 - accuracy: 0.5019
17000/25000 [===================>..........] - ETA: 1s - loss: 7.6405 - accuracy: 0.5017
18000/25000 [====================>.........] - ETA: 1s - loss: 7.6215 - accuracy: 0.5029
19000/25000 [=====================>........] - ETA: 1s - loss: 7.6279 - accuracy: 0.5025
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6275 - accuracy: 0.5026
21000/25000 [========================>.....] - ETA: 0s - loss: 7.6235 - accuracy: 0.5028
22000/25000 [=========================>....] - ETA: 0s - loss: 7.6429 - accuracy: 0.5015
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6513 - accuracy: 0.5010
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6596 - accuracy: 0.5005
25000/25000 [==============================] - 7s 279us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000
fit success None

  ############ Prediction############################################ 
Loading data...
(array([[1.],
       [1.],
       [1.],
       ...,
       [1.],
       [1.],
       [1.]], dtype=float32), None)

  ############ Save/ Load ############################################ 

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Warning: Permanently added the RSA host key for IP address '140.82.114.3' to the list of known hosts.
From github.com:arita37/mlmodels_store
   5ac6c42..ec570d3  master     -> origin/master
Updating 5ac6c42..ec570d3
Fast-forward
 error_list/20200519/list_log_testall_20200519.md | 104 +++++++++++++++++++++++
 1 file changed, 104 insertions(+)
[master b73a2b3] ml_store
 1 file changed, 324 insertions(+)
To github.com:arita37/mlmodels_store.git
   ec570d3..b73a2b3  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//armdn.py 

  #### Loading params   ############################################## 

  #### Model init   ################################################## 
Using TensorFlow backend.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/resource_variable_ops.py:1630: calling BaseResourceVariable.__init__ (from tensorflow.python.ops.resource_variable_ops) with constraint is deprecated and will be removed in a future version.
Instructions for updating:
If using Keras pass *_constraint arguments to layers.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_probability/python/distributions/mixture.py:154: Categorical.event_size (from tensorflow_probability.python.distributions.categorical) is deprecated and will be removed after 2019-05-19.
Instructions for updating:
The `event_size` property is deprecated.  Use `num_categories` instead.  They have the same value, but `event_size` is misnamed.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/math_ops.py:2509: where (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
Model: "sequential_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
LSTM_1 (LSTM)                (None, 12, 300)           362400    
_________________________________________________________________
LSTM_2 (LSTM)                (None, 12, 200)           400800    
_________________________________________________________________
LSTM_3 (LSTM)                (None, 12, 24)            21600     
_________________________________________________________________
LSTM_4 (LSTM)                (None, 12)                1776      
_________________________________________________________________
dense_1 (Dense)              (None, 10)                130       
_________________________________________________________________
mdn_1 (MDN)                  (None, 75)                825       
=================================================================
Total params: 787,531
Trainable params: 787,531
Non-trainable params: 0
_________________________________________________________________

  ### Model Fit ###################################################### 

  #### Loading dataset   ############################################# 
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py:422: The name tf.global_variables is deprecated. Please use tf.compat.v1.global_variables instead.

Epoch 1/10

13/13 [==============================] - 2s 132ms/step - loss: nan
Epoch 2/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 3/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 4/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 5/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 6/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 7/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 8/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 9/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 10/10

13/13 [==============================] - 0s 4ms/step - loss: nan

  fitted metrics {'loss': [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan]} 

  #### Predict   ##################################################### 
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/mdn/__init__.py:209: The name tf.logging.info is deprecated. Please use tf.compat.v1.logging.info instead.

[[nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
  nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
  nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
  nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
  nan nan nan]]
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//armdn.py", line 380, in <module>
    test(pars_choice="json", data_path= "model_keras/armdn.json")
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//armdn.py", line 354, in test
    y_pred, y_test = predict(model=model, model_pars=model_pars, data_pars=data_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//armdn.py", line 170, in predict
    model.model_pars["n_mixes"], temp=1.0)
  File "<__array_function__ internals>", line 6, in apply_along_axis
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/numpy/lib/shape_base.py", line 379, in apply_along_axis
    res = asanyarray(func1d(inarr_view[ind0], *args, **kwargs))
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/mdn/__init__.py", line 237, in sample_from_output
    cov_matrix = np.identity(output_dim) * sig_vector
ValueError: operands could not be broadcast together with shapes (12,12) (0,) 

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Already up to date.
[master 4b31bc3] ml_store
 1 file changed, 126 insertions(+)
To github.com:arita37/mlmodels_store.git
   b73a2b3..4b31bc3  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//02_cnn.py 

  ('#### Loading params   ##############################################',) 

  ('#### Path params   ################################################',) 

  ('/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/charcnn/',) 

  ('#### Model params   ################################################',) 

  ('#### Loading dataset   #############################################',) 

  ('#### Path params   ################################################',) 

  ('/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/', '/home/runner/work/mlmodels/mlmodels/keras_deepAR/') 
Downloading data from https://s3.amazonaws.com/img-datasets/mnist.npz

    8192/11490434 [..............................] - ETA: 0s
 1081344/11490434 [=>............................] - ETA: 0s
 2334720/11490434 [=====>........................] - ETA: 0s
 4997120/11490434 [============>.................] - ETA: 0s
 8814592/11490434 [======================>.......] - ETA: 0s
11493376/11490434 [==============================] - 0s 0us/step

  ('#### Model init, fit   #############################################',) 
Using TensorFlow backend.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/resource_variable_ops.py:1630: calling BaseResourceVariable.__init__ (from tensorflow.python.ops.resource_variable_ops) with constraint is deprecated and will be removed in a future version.
Instructions for updating:
If using Keras pass *_constraint arguments to layers.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py:4070: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.


  ('#### Path params   ################################################',) 

  ('/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/', '/home/runner/work/mlmodels/mlmodels/keras_deepAR/') 
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/keras/backend/tensorflow_backend.py:422: The name tf.global_variables is deprecated. Please use tf.compat.v1.global_variables instead.

Train on 60000 samples, validate on 10000 samples
Epoch 1/1

   32/60000 [..............................] - ETA: 8:13 - loss: 2.3403 - categorical_accuracy: 0.0625
   96/60000 [..............................] - ETA: 3:48 - loss: 2.2951 - categorical_accuracy: 0.1354
  128/60000 [..............................] - ETA: 3:14 - loss: 2.2647 - categorical_accuracy: 0.1562
  192/60000 [..............................] - ETA: 2:38 - loss: 2.2274 - categorical_accuracy: 0.1875
  256/60000 [..............................] - ETA: 2:19 - loss: 2.1734 - categorical_accuracy: 0.2266
  320/60000 [..............................] - ETA: 2:08 - loss: 2.1013 - categorical_accuracy: 0.2594
  384/60000 [..............................] - ETA: 2:00 - loss: 2.0557 - categorical_accuracy: 0.2812
  448/60000 [..............................] - ETA: 1:55 - loss: 1.9680 - categorical_accuracy: 0.3103
  512/60000 [..............................] - ETA: 1:52 - loss: 1.9011 - categorical_accuracy: 0.3379
  544/60000 [..............................] - ETA: 1:51 - loss: 1.8553 - categorical_accuracy: 0.3548
  608/60000 [..............................] - ETA: 1:49 - loss: 1.8084 - categorical_accuracy: 0.3766
  672/60000 [..............................] - ETA: 1:46 - loss: 1.7690 - categorical_accuracy: 0.3869
  736/60000 [..............................] - ETA: 1:44 - loss: 1.7320 - categorical_accuracy: 0.3967
  800/60000 [..............................] - ETA: 1:43 - loss: 1.6885 - categorical_accuracy: 0.4175
  864/60000 [..............................] - ETA: 1:41 - loss: 1.6413 - categorical_accuracy: 0.4375
  928/60000 [..............................] - ETA: 1:39 - loss: 1.6235 - categorical_accuracy: 0.4440
  992/60000 [..............................] - ETA: 1:38 - loss: 1.5952 - categorical_accuracy: 0.4526
 1056/60000 [..............................] - ETA: 1:37 - loss: 1.5619 - categorical_accuracy: 0.4659
 1120/60000 [..............................] - ETA: 1:36 - loss: 1.5379 - categorical_accuracy: 0.4759
 1184/60000 [..............................] - ETA: 1:36 - loss: 1.5227 - categorical_accuracy: 0.4823
 1248/60000 [..............................] - ETA: 1:35 - loss: 1.4984 - categorical_accuracy: 0.4872
 1312/60000 [..............................] - ETA: 1:34 - loss: 1.4711 - categorical_accuracy: 0.4992
 1376/60000 [..............................] - ETA: 1:33 - loss: 1.4513 - categorical_accuracy: 0.5073
 1440/60000 [..............................] - ETA: 1:33 - loss: 1.4203 - categorical_accuracy: 0.5201
 1504/60000 [..............................] - ETA: 1:32 - loss: 1.4046 - categorical_accuracy: 0.5259
 1568/60000 [..............................] - ETA: 1:32 - loss: 1.3783 - categorical_accuracy: 0.5344
 1632/60000 [..............................] - ETA: 1:31 - loss: 1.3587 - categorical_accuracy: 0.5404
 1696/60000 [..............................] - ETA: 1:31 - loss: 1.3248 - categorical_accuracy: 0.5525
 1760/60000 [..............................] - ETA: 1:31 - loss: 1.3010 - categorical_accuracy: 0.5591
 1824/60000 [..............................] - ETA: 1:30 - loss: 1.2762 - categorical_accuracy: 0.5702
 1888/60000 [..............................] - ETA: 1:30 - loss: 1.2521 - categorical_accuracy: 0.5784
 1952/60000 [..............................] - ETA: 1:30 - loss: 1.2272 - categorical_accuracy: 0.5871
 2016/60000 [>.............................] - ETA: 1:30 - loss: 1.2098 - categorical_accuracy: 0.5938
 2080/60000 [>.............................] - ETA: 1:29 - loss: 1.1943 - categorical_accuracy: 0.6000
 2144/60000 [>.............................] - ETA: 1:29 - loss: 1.1692 - categorical_accuracy: 0.6087
 2208/60000 [>.............................] - ETA: 1:29 - loss: 1.1572 - categorical_accuracy: 0.6119
 2240/60000 [>.............................] - ETA: 1:29 - loss: 1.1505 - categorical_accuracy: 0.6138
 2304/60000 [>.............................] - ETA: 1:29 - loss: 1.1305 - categorical_accuracy: 0.6211
 2368/60000 [>.............................] - ETA: 1:28 - loss: 1.1136 - categorical_accuracy: 0.6280
 2432/60000 [>.............................] - ETA: 1:28 - loss: 1.0973 - categorical_accuracy: 0.6324
 2496/60000 [>.............................] - ETA: 1:28 - loss: 1.0776 - categorical_accuracy: 0.6402
 2560/60000 [>.............................] - ETA: 1:27 - loss: 1.0595 - categorical_accuracy: 0.6465
 2592/60000 [>.............................] - ETA: 1:27 - loss: 1.0488 - categorical_accuracy: 0.6505
 2656/60000 [>.............................] - ETA: 1:27 - loss: 1.0297 - categorical_accuracy: 0.6574
 2720/60000 [>.............................] - ETA: 1:27 - loss: 1.0147 - categorical_accuracy: 0.6625
 2752/60000 [>.............................] - ETA: 1:27 - loss: 1.0108 - categorical_accuracy: 0.6639
 2816/60000 [>.............................] - ETA: 1:27 - loss: 0.9937 - categorical_accuracy: 0.6694
 2880/60000 [>.............................] - ETA: 1:27 - loss: 0.9768 - categorical_accuracy: 0.6753
 2944/60000 [>.............................] - ETA: 1:26 - loss: 0.9668 - categorical_accuracy: 0.6783
 3008/60000 [>.............................] - ETA: 1:26 - loss: 0.9584 - categorical_accuracy: 0.6818
 3072/60000 [>.............................] - ETA: 1:26 - loss: 0.9496 - categorical_accuracy: 0.6855
 3136/60000 [>.............................] - ETA: 1:26 - loss: 0.9374 - categorical_accuracy: 0.6904
 3200/60000 [>.............................] - ETA: 1:26 - loss: 0.9281 - categorical_accuracy: 0.6947
 3232/60000 [>.............................] - ETA: 1:26 - loss: 0.9235 - categorical_accuracy: 0.6971
 3296/60000 [>.............................] - ETA: 1:26 - loss: 0.9113 - categorical_accuracy: 0.7005
 3360/60000 [>.............................] - ETA: 1:25 - loss: 0.8985 - categorical_accuracy: 0.7048
 3424/60000 [>.............................] - ETA: 1:25 - loss: 0.8866 - categorical_accuracy: 0.7094
 3488/60000 [>.............................] - ETA: 1:25 - loss: 0.8761 - categorical_accuracy: 0.7130
 3552/60000 [>.............................] - ETA: 1:25 - loss: 0.8633 - categorical_accuracy: 0.7171
 3616/60000 [>.............................] - ETA: 1:25 - loss: 0.8559 - categorical_accuracy: 0.7204
 3680/60000 [>.............................] - ETA: 1:24 - loss: 0.8469 - categorical_accuracy: 0.7242
 3744/60000 [>.............................] - ETA: 1:24 - loss: 0.8409 - categorical_accuracy: 0.7265
 3808/60000 [>.............................] - ETA: 1:24 - loss: 0.8313 - categorical_accuracy: 0.7295
 3872/60000 [>.............................] - ETA: 1:24 - loss: 0.8224 - categorical_accuracy: 0.7327
 3936/60000 [>.............................] - ETA: 1:24 - loss: 0.8142 - categorical_accuracy: 0.7353
 4000/60000 [=>............................] - ETA: 1:24 - loss: 0.8070 - categorical_accuracy: 0.7377
 4064/60000 [=>............................] - ETA: 1:23 - loss: 0.8005 - categorical_accuracy: 0.7397
 4128/60000 [=>............................] - ETA: 1:23 - loss: 0.7928 - categorical_accuracy: 0.7427
 4192/60000 [=>............................] - ETA: 1:23 - loss: 0.7846 - categorical_accuracy: 0.7455
 4256/60000 [=>............................] - ETA: 1:23 - loss: 0.7767 - categorical_accuracy: 0.7479
 4320/60000 [=>............................] - ETA: 1:23 - loss: 0.7683 - categorical_accuracy: 0.7507
 4384/60000 [=>............................] - ETA: 1:23 - loss: 0.7615 - categorical_accuracy: 0.7530
 4448/60000 [=>............................] - ETA: 1:23 - loss: 0.7561 - categorical_accuracy: 0.7552
 4512/60000 [=>............................] - ETA: 1:22 - loss: 0.7501 - categorical_accuracy: 0.7569
 4576/60000 [=>............................] - ETA: 1:22 - loss: 0.7420 - categorical_accuracy: 0.7598
 4640/60000 [=>............................] - ETA: 1:22 - loss: 0.7385 - categorical_accuracy: 0.7616
 4704/60000 [=>............................] - ETA: 1:22 - loss: 0.7305 - categorical_accuracy: 0.7645
 4768/60000 [=>............................] - ETA: 1:22 - loss: 0.7244 - categorical_accuracy: 0.7666
 4832/60000 [=>............................] - ETA: 1:22 - loss: 0.7181 - categorical_accuracy: 0.7690
 4896/60000 [=>............................] - ETA: 1:22 - loss: 0.7144 - categorical_accuracy: 0.7702
 4960/60000 [=>............................] - ETA: 1:21 - loss: 0.7080 - categorical_accuracy: 0.7722
 5024/60000 [=>............................] - ETA: 1:21 - loss: 0.7037 - categorical_accuracy: 0.7729
 5088/60000 [=>............................] - ETA: 1:21 - loss: 0.6980 - categorical_accuracy: 0.7746
 5152/60000 [=>............................] - ETA: 1:21 - loss: 0.6952 - categorical_accuracy: 0.7760
 5216/60000 [=>............................] - ETA: 1:21 - loss: 0.6910 - categorical_accuracy: 0.7778
 5280/60000 [=>............................] - ETA: 1:21 - loss: 0.6845 - categorical_accuracy: 0.7799
 5344/60000 [=>............................] - ETA: 1:21 - loss: 0.6784 - categorical_accuracy: 0.7820
 5408/60000 [=>............................] - ETA: 1:20 - loss: 0.6728 - categorical_accuracy: 0.7835
 5472/60000 [=>............................] - ETA: 1:20 - loss: 0.6713 - categorical_accuracy: 0.7844
 5536/60000 [=>............................] - ETA: 1:20 - loss: 0.6673 - categorical_accuracy: 0.7859
 5600/60000 [=>............................] - ETA: 1:20 - loss: 0.6632 - categorical_accuracy: 0.7871
 5664/60000 [=>............................] - ETA: 1:20 - loss: 0.6583 - categorical_accuracy: 0.7890
 5728/60000 [=>............................] - ETA: 1:20 - loss: 0.6558 - categorical_accuracy: 0.7902
 5792/60000 [=>............................] - ETA: 1:20 - loss: 0.6505 - categorical_accuracy: 0.7921
 5856/60000 [=>............................] - ETA: 1:19 - loss: 0.6466 - categorical_accuracy: 0.7935
 5920/60000 [=>............................] - ETA: 1:19 - loss: 0.6440 - categorical_accuracy: 0.7941
 5984/60000 [=>............................] - ETA: 1:19 - loss: 0.6399 - categorical_accuracy: 0.7956
 6048/60000 [==>...........................] - ETA: 1:19 - loss: 0.6352 - categorical_accuracy: 0.7975
 6112/60000 [==>...........................] - ETA: 1:19 - loss: 0.6314 - categorical_accuracy: 0.7983
 6176/60000 [==>...........................] - ETA: 1:19 - loss: 0.6269 - categorical_accuracy: 0.7997
 6240/60000 [==>...........................] - ETA: 1:19 - loss: 0.6234 - categorical_accuracy: 0.8006
 6304/60000 [==>...........................] - ETA: 1:19 - loss: 0.6230 - categorical_accuracy: 0.8011
 6368/60000 [==>...........................] - ETA: 1:18 - loss: 0.6185 - categorical_accuracy: 0.8028
 6432/60000 [==>...........................] - ETA: 1:18 - loss: 0.6150 - categorical_accuracy: 0.8041
 6496/60000 [==>...........................] - ETA: 1:18 - loss: 0.6101 - categorical_accuracy: 0.8056
 6528/60000 [==>...........................] - ETA: 1:18 - loss: 0.6082 - categorical_accuracy: 0.8062
 6560/60000 [==>...........................] - ETA: 1:18 - loss: 0.6068 - categorical_accuracy: 0.8067
 6624/60000 [==>...........................] - ETA: 1:18 - loss: 0.6024 - categorical_accuracy: 0.8080
 6688/60000 [==>...........................] - ETA: 1:18 - loss: 0.5987 - categorical_accuracy: 0.8092
 6752/60000 [==>...........................] - ETA: 1:18 - loss: 0.5968 - categorical_accuracy: 0.8101
 6784/60000 [==>...........................] - ETA: 1:18 - loss: 0.5944 - categorical_accuracy: 0.8109
 6848/60000 [==>...........................] - ETA: 1:18 - loss: 0.5926 - categorical_accuracy: 0.8119
 6912/60000 [==>...........................] - ETA: 1:18 - loss: 0.5887 - categorical_accuracy: 0.8132
 6976/60000 [==>...........................] - ETA: 1:17 - loss: 0.5847 - categorical_accuracy: 0.8147
 7040/60000 [==>...........................] - ETA: 1:17 - loss: 0.5821 - categorical_accuracy: 0.8155
 7104/60000 [==>...........................] - ETA: 1:17 - loss: 0.5797 - categorical_accuracy: 0.8162
 7168/60000 [==>...........................] - ETA: 1:17 - loss: 0.5787 - categorical_accuracy: 0.8165
 7232/60000 [==>...........................] - ETA: 1:17 - loss: 0.5752 - categorical_accuracy: 0.8178
 7296/60000 [==>...........................] - ETA: 1:17 - loss: 0.5719 - categorical_accuracy: 0.8188
 7360/60000 [==>...........................] - ETA: 1:17 - loss: 0.5697 - categorical_accuracy: 0.8198
 7424/60000 [==>...........................] - ETA: 1:17 - loss: 0.5661 - categorical_accuracy: 0.8211
 7488/60000 [==>...........................] - ETA: 1:16 - loss: 0.5625 - categorical_accuracy: 0.8222
 7552/60000 [==>...........................] - ETA: 1:16 - loss: 0.5592 - categorical_accuracy: 0.8232
 7616/60000 [==>...........................] - ETA: 1:16 - loss: 0.5566 - categorical_accuracy: 0.8241
 7680/60000 [==>...........................] - ETA: 1:16 - loss: 0.5538 - categorical_accuracy: 0.8246
 7744/60000 [==>...........................] - ETA: 1:16 - loss: 0.5528 - categorical_accuracy: 0.8252
 7808/60000 [==>...........................] - ETA: 1:16 - loss: 0.5512 - categorical_accuracy: 0.8257
 7872/60000 [==>...........................] - ETA: 1:16 - loss: 0.5486 - categorical_accuracy: 0.8263
 7936/60000 [==>...........................] - ETA: 1:16 - loss: 0.5462 - categorical_accuracy: 0.8271
 8000/60000 [===>..........................] - ETA: 1:16 - loss: 0.5438 - categorical_accuracy: 0.8279
 8064/60000 [===>..........................] - ETA: 1:15 - loss: 0.5414 - categorical_accuracy: 0.8285
 8128/60000 [===>..........................] - ETA: 1:15 - loss: 0.5401 - categorical_accuracy: 0.8290
 8192/60000 [===>..........................] - ETA: 1:15 - loss: 0.5376 - categorical_accuracy: 0.8300
 8256/60000 [===>..........................] - ETA: 1:15 - loss: 0.5351 - categorical_accuracy: 0.8308
 8320/60000 [===>..........................] - ETA: 1:15 - loss: 0.5330 - categorical_accuracy: 0.8315
 8384/60000 [===>..........................] - ETA: 1:15 - loss: 0.5315 - categorical_accuracy: 0.8322
 8448/60000 [===>..........................] - ETA: 1:15 - loss: 0.5290 - categorical_accuracy: 0.8329
 8512/60000 [===>..........................] - ETA: 1:15 - loss: 0.5255 - categorical_accuracy: 0.8339
 8576/60000 [===>..........................] - ETA: 1:14 - loss: 0.5241 - categorical_accuracy: 0.8345
 8640/60000 [===>..........................] - ETA: 1:14 - loss: 0.5221 - categorical_accuracy: 0.8353
 8704/60000 [===>..........................] - ETA: 1:14 - loss: 0.5209 - categorical_accuracy: 0.8357
 8768/60000 [===>..........................] - ETA: 1:14 - loss: 0.5194 - categorical_accuracy: 0.8359
 8800/60000 [===>..........................] - ETA: 1:14 - loss: 0.5187 - categorical_accuracy: 0.8363
 8864/60000 [===>..........................] - ETA: 1:14 - loss: 0.5173 - categorical_accuracy: 0.8366
 8928/60000 [===>..........................] - ETA: 1:14 - loss: 0.5151 - categorical_accuracy: 0.8371
 8992/60000 [===>..........................] - ETA: 1:14 - loss: 0.5128 - categorical_accuracy: 0.8379
 9024/60000 [===>..........................] - ETA: 1:14 - loss: 0.5116 - categorical_accuracy: 0.8383
 9088/60000 [===>..........................] - ETA: 1:14 - loss: 0.5111 - categorical_accuracy: 0.8387
 9152/60000 [===>..........................] - ETA: 1:14 - loss: 0.5084 - categorical_accuracy: 0.8394
 9216/60000 [===>..........................] - ETA: 1:13 - loss: 0.5056 - categorical_accuracy: 0.8401
 9280/60000 [===>..........................] - ETA: 1:13 - loss: 0.5029 - categorical_accuracy: 0.8411
 9344/60000 [===>..........................] - ETA: 1:13 - loss: 0.5022 - categorical_accuracy: 0.8413
 9408/60000 [===>..........................] - ETA: 1:13 - loss: 0.5006 - categorical_accuracy: 0.8417
 9472/60000 [===>..........................] - ETA: 1:13 - loss: 0.4989 - categorical_accuracy: 0.8423
 9536/60000 [===>..........................] - ETA: 1:13 - loss: 0.4970 - categorical_accuracy: 0.8430
 9600/60000 [===>..........................] - ETA: 1:13 - loss: 0.4966 - categorical_accuracy: 0.8433
 9664/60000 [===>..........................] - ETA: 1:13 - loss: 0.4951 - categorical_accuracy: 0.8436
 9728/60000 [===>..........................] - ETA: 1:13 - loss: 0.4936 - categorical_accuracy: 0.8442
 9792/60000 [===>..........................] - ETA: 1:12 - loss: 0.4911 - categorical_accuracy: 0.8450
 9856/60000 [===>..........................] - ETA: 1:12 - loss: 0.4888 - categorical_accuracy: 0.8458
 9920/60000 [===>..........................] - ETA: 1:12 - loss: 0.4885 - categorical_accuracy: 0.8459
 9984/60000 [===>..........................] - ETA: 1:12 - loss: 0.4877 - categorical_accuracy: 0.8462
10048/60000 [====>.........................] - ETA: 1:12 - loss: 0.4865 - categorical_accuracy: 0.8467
10112/60000 [====>.........................] - ETA: 1:12 - loss: 0.4849 - categorical_accuracy: 0.8473
10176/60000 [====>.........................] - ETA: 1:12 - loss: 0.4827 - categorical_accuracy: 0.8481
10240/60000 [====>.........................] - ETA: 1:12 - loss: 0.4810 - categorical_accuracy: 0.8487
10304/60000 [====>.........................] - ETA: 1:12 - loss: 0.4801 - categorical_accuracy: 0.8491
10368/60000 [====>.........................] - ETA: 1:12 - loss: 0.4776 - categorical_accuracy: 0.8500
10432/60000 [====>.........................] - ETA: 1:11 - loss: 0.4756 - categorical_accuracy: 0.8508
10496/60000 [====>.........................] - ETA: 1:11 - loss: 0.4741 - categorical_accuracy: 0.8514
10560/60000 [====>.........................] - ETA: 1:11 - loss: 0.4728 - categorical_accuracy: 0.8521
10624/60000 [====>.........................] - ETA: 1:11 - loss: 0.4725 - categorical_accuracy: 0.8524
10688/60000 [====>.........................] - ETA: 1:11 - loss: 0.4716 - categorical_accuracy: 0.8526
10752/60000 [====>.........................] - ETA: 1:11 - loss: 0.4701 - categorical_accuracy: 0.8531
10816/60000 [====>.........................] - ETA: 1:11 - loss: 0.4699 - categorical_accuracy: 0.8536
10848/60000 [====>.........................] - ETA: 1:11 - loss: 0.4691 - categorical_accuracy: 0.8537
10912/60000 [====>.........................] - ETA: 1:11 - loss: 0.4678 - categorical_accuracy: 0.8541
10976/60000 [====>.........................] - ETA: 1:11 - loss: 0.4661 - categorical_accuracy: 0.8546
11040/60000 [====>.........................] - ETA: 1:11 - loss: 0.4640 - categorical_accuracy: 0.8553
11104/60000 [====>.........................] - ETA: 1:10 - loss: 0.4618 - categorical_accuracy: 0.8559
11168/60000 [====>.........................] - ETA: 1:10 - loss: 0.4604 - categorical_accuracy: 0.8564
11232/60000 [====>.........................] - ETA: 1:10 - loss: 0.4581 - categorical_accuracy: 0.8570
11296/60000 [====>.........................] - ETA: 1:10 - loss: 0.4568 - categorical_accuracy: 0.8574
11360/60000 [====>.........................] - ETA: 1:10 - loss: 0.4559 - categorical_accuracy: 0.8577
11424/60000 [====>.........................] - ETA: 1:10 - loss: 0.4546 - categorical_accuracy: 0.8580
11488/60000 [====>.........................] - ETA: 1:10 - loss: 0.4536 - categorical_accuracy: 0.8582
11552/60000 [====>.........................] - ETA: 1:10 - loss: 0.4526 - categorical_accuracy: 0.8588
11616/60000 [====>.........................] - ETA: 1:10 - loss: 0.4513 - categorical_accuracy: 0.8592
11680/60000 [====>.........................] - ETA: 1:10 - loss: 0.4496 - categorical_accuracy: 0.8598
11744/60000 [====>.........................] - ETA: 1:09 - loss: 0.4477 - categorical_accuracy: 0.8604
11808/60000 [====>.........................] - ETA: 1:09 - loss: 0.4465 - categorical_accuracy: 0.8608
11872/60000 [====>.........................] - ETA: 1:09 - loss: 0.4448 - categorical_accuracy: 0.8611
11936/60000 [====>.........................] - ETA: 1:09 - loss: 0.4431 - categorical_accuracy: 0.8616
12000/60000 [=====>........................] - ETA: 1:09 - loss: 0.4423 - categorical_accuracy: 0.8618
12064/60000 [=====>........................] - ETA: 1:09 - loss: 0.4419 - categorical_accuracy: 0.8620
12128/60000 [=====>........................] - ETA: 1:09 - loss: 0.4405 - categorical_accuracy: 0.8625
12192/60000 [=====>........................] - ETA: 1:09 - loss: 0.4391 - categorical_accuracy: 0.8629
12256/60000 [=====>........................] - ETA: 1:09 - loss: 0.4377 - categorical_accuracy: 0.8635
12288/60000 [=====>........................] - ETA: 1:09 - loss: 0.4367 - categorical_accuracy: 0.8638
12352/60000 [=====>........................] - ETA: 1:09 - loss: 0.4357 - categorical_accuracy: 0.8642
12416/60000 [=====>........................] - ETA: 1:08 - loss: 0.4349 - categorical_accuracy: 0.8644
12480/60000 [=====>........................] - ETA: 1:08 - loss: 0.4335 - categorical_accuracy: 0.8649
12544/60000 [=====>........................] - ETA: 1:08 - loss: 0.4321 - categorical_accuracy: 0.8654
12608/60000 [=====>........................] - ETA: 1:08 - loss: 0.4316 - categorical_accuracy: 0.8657
12672/60000 [=====>........................] - ETA: 1:08 - loss: 0.4307 - categorical_accuracy: 0.8659
12736/60000 [=====>........................] - ETA: 1:08 - loss: 0.4290 - categorical_accuracy: 0.8665
12800/60000 [=====>........................] - ETA: 1:08 - loss: 0.4276 - categorical_accuracy: 0.8670
12864/60000 [=====>........................] - ETA: 1:08 - loss: 0.4260 - categorical_accuracy: 0.8675
12928/60000 [=====>........................] - ETA: 1:08 - loss: 0.4245 - categorical_accuracy: 0.8680
12960/60000 [=====>........................] - ETA: 1:08 - loss: 0.4241 - categorical_accuracy: 0.8681
13024/60000 [=====>........................] - ETA: 1:08 - loss: 0.4243 - categorical_accuracy: 0.8682
13088/60000 [=====>........................] - ETA: 1:08 - loss: 0.4230 - categorical_accuracy: 0.8684
13120/60000 [=====>........................] - ETA: 1:07 - loss: 0.4224 - categorical_accuracy: 0.8686
13184/60000 [=====>........................] - ETA: 1:07 - loss: 0.4209 - categorical_accuracy: 0.8692
13216/60000 [=====>........................] - ETA: 1:07 - loss: 0.4202 - categorical_accuracy: 0.8694
13280/60000 [=====>........................] - ETA: 1:07 - loss: 0.4189 - categorical_accuracy: 0.8697
13344/60000 [=====>........................] - ETA: 1:07 - loss: 0.4179 - categorical_accuracy: 0.8700
13408/60000 [=====>........................] - ETA: 1:07 - loss: 0.4172 - categorical_accuracy: 0.8703
13472/60000 [=====>........................] - ETA: 1:07 - loss: 0.4158 - categorical_accuracy: 0.8706
13536/60000 [=====>........................] - ETA: 1:07 - loss: 0.4142 - categorical_accuracy: 0.8711
13600/60000 [=====>........................] - ETA: 1:07 - loss: 0.4134 - categorical_accuracy: 0.8713
13664/60000 [=====>........................] - ETA: 1:07 - loss: 0.4129 - categorical_accuracy: 0.8713
13728/60000 [=====>........................] - ETA: 1:07 - loss: 0.4119 - categorical_accuracy: 0.8715
13792/60000 [=====>........................] - ETA: 1:06 - loss: 0.4108 - categorical_accuracy: 0.8719
13856/60000 [=====>........................] - ETA: 1:06 - loss: 0.4093 - categorical_accuracy: 0.8723
13920/60000 [=====>........................] - ETA: 1:06 - loss: 0.4081 - categorical_accuracy: 0.8726
13984/60000 [=====>........................] - ETA: 1:06 - loss: 0.4072 - categorical_accuracy: 0.8731
14048/60000 [======>.......................] - ETA: 1:06 - loss: 0.4066 - categorical_accuracy: 0.8733
14112/60000 [======>.......................] - ETA: 1:06 - loss: 0.4053 - categorical_accuracy: 0.8737
14176/60000 [======>.......................] - ETA: 1:06 - loss: 0.4039 - categorical_accuracy: 0.8740
14240/60000 [======>.......................] - ETA: 1:06 - loss: 0.4031 - categorical_accuracy: 0.8742
14304/60000 [======>.......................] - ETA: 1:06 - loss: 0.4018 - categorical_accuracy: 0.8747
14368/60000 [======>.......................] - ETA: 1:06 - loss: 0.4003 - categorical_accuracy: 0.8752
14432/60000 [======>.......................] - ETA: 1:05 - loss: 0.3995 - categorical_accuracy: 0.8755
14496/60000 [======>.......................] - ETA: 1:05 - loss: 0.3993 - categorical_accuracy: 0.8754
14560/60000 [======>.......................] - ETA: 1:05 - loss: 0.3987 - categorical_accuracy: 0.8758
14624/60000 [======>.......................] - ETA: 1:05 - loss: 0.3981 - categorical_accuracy: 0.8760
14688/60000 [======>.......................] - ETA: 1:05 - loss: 0.3969 - categorical_accuracy: 0.8764
14752/60000 [======>.......................] - ETA: 1:05 - loss: 0.3960 - categorical_accuracy: 0.8766
14816/60000 [======>.......................] - ETA: 1:05 - loss: 0.3951 - categorical_accuracy: 0.8769
14880/60000 [======>.......................] - ETA: 1:05 - loss: 0.3943 - categorical_accuracy: 0.8772
14944/60000 [======>.......................] - ETA: 1:05 - loss: 0.3937 - categorical_accuracy: 0.8774
14976/60000 [======>.......................] - ETA: 1:05 - loss: 0.3931 - categorical_accuracy: 0.8775
15040/60000 [======>.......................] - ETA: 1:05 - loss: 0.3920 - categorical_accuracy: 0.8779
15104/60000 [======>.......................] - ETA: 1:04 - loss: 0.3914 - categorical_accuracy: 0.8780
15168/60000 [======>.......................] - ETA: 1:04 - loss: 0.3904 - categorical_accuracy: 0.8785
15232/60000 [======>.......................] - ETA: 1:04 - loss: 0.3890 - categorical_accuracy: 0.8789
15296/60000 [======>.......................] - ETA: 1:04 - loss: 0.3876 - categorical_accuracy: 0.8793
15360/60000 [======>.......................] - ETA: 1:04 - loss: 0.3867 - categorical_accuracy: 0.8796
15424/60000 [======>.......................] - ETA: 1:04 - loss: 0.3857 - categorical_accuracy: 0.8801
15488/60000 [======>.......................] - ETA: 1:04 - loss: 0.3850 - categorical_accuracy: 0.8804
15552/60000 [======>.......................] - ETA: 1:04 - loss: 0.3839 - categorical_accuracy: 0.8806
15616/60000 [======>.......................] - ETA: 1:04 - loss: 0.3827 - categorical_accuracy: 0.8810
15680/60000 [======>.......................] - ETA: 1:04 - loss: 0.3816 - categorical_accuracy: 0.8814
15744/60000 [======>.......................] - ETA: 1:03 - loss: 0.3808 - categorical_accuracy: 0.8817
15808/60000 [======>.......................] - ETA: 1:03 - loss: 0.3794 - categorical_accuracy: 0.8821
15872/60000 [======>.......................] - ETA: 1:03 - loss: 0.3785 - categorical_accuracy: 0.8824
15936/60000 [======>.......................] - ETA: 1:03 - loss: 0.3773 - categorical_accuracy: 0.8828
16000/60000 [=======>......................] - ETA: 1:03 - loss: 0.3765 - categorical_accuracy: 0.8829
16064/60000 [=======>......................] - ETA: 1:03 - loss: 0.3754 - categorical_accuracy: 0.8832
16128/60000 [=======>......................] - ETA: 1:03 - loss: 0.3744 - categorical_accuracy: 0.8835
16192/60000 [=======>......................] - ETA: 1:03 - loss: 0.3738 - categorical_accuracy: 0.8838
16256/60000 [=======>......................] - ETA: 1:03 - loss: 0.3726 - categorical_accuracy: 0.8842
16320/60000 [=======>......................] - ETA: 1:03 - loss: 0.3722 - categorical_accuracy: 0.8843
16384/60000 [=======>......................] - ETA: 1:02 - loss: 0.3716 - categorical_accuracy: 0.8845
16448/60000 [=======>......................] - ETA: 1:02 - loss: 0.3706 - categorical_accuracy: 0.8847
16512/60000 [=======>......................] - ETA: 1:02 - loss: 0.3696 - categorical_accuracy: 0.8849
16576/60000 [=======>......................] - ETA: 1:02 - loss: 0.3686 - categorical_accuracy: 0.8852
16640/60000 [=======>......................] - ETA: 1:02 - loss: 0.3681 - categorical_accuracy: 0.8853
16704/60000 [=======>......................] - ETA: 1:02 - loss: 0.3673 - categorical_accuracy: 0.8855
16768/60000 [=======>......................] - ETA: 1:02 - loss: 0.3666 - categorical_accuracy: 0.8857
16832/60000 [=======>......................] - ETA: 1:02 - loss: 0.3656 - categorical_accuracy: 0.8861
16896/60000 [=======>......................] - ETA: 1:02 - loss: 0.3647 - categorical_accuracy: 0.8865
16960/60000 [=======>......................] - ETA: 1:02 - loss: 0.3635 - categorical_accuracy: 0.8869
17024/60000 [=======>......................] - ETA: 1:01 - loss: 0.3630 - categorical_accuracy: 0.8869
17088/60000 [=======>......................] - ETA: 1:01 - loss: 0.3617 - categorical_accuracy: 0.8873
17152/60000 [=======>......................] - ETA: 1:01 - loss: 0.3611 - categorical_accuracy: 0.8877
17216/60000 [=======>......................] - ETA: 1:01 - loss: 0.3603 - categorical_accuracy: 0.8878
17280/60000 [=======>......................] - ETA: 1:01 - loss: 0.3596 - categorical_accuracy: 0.8880
17344/60000 [=======>......................] - ETA: 1:01 - loss: 0.3590 - categorical_accuracy: 0.8881
17408/60000 [=======>......................] - ETA: 1:01 - loss: 0.3581 - categorical_accuracy: 0.8884
17472/60000 [=======>......................] - ETA: 1:01 - loss: 0.3579 - categorical_accuracy: 0.8885
17536/60000 [=======>......................] - ETA: 1:01 - loss: 0.3573 - categorical_accuracy: 0.8886
17600/60000 [=======>......................] - ETA: 1:01 - loss: 0.3567 - categorical_accuracy: 0.8888
17664/60000 [=======>......................] - ETA: 1:01 - loss: 0.3560 - categorical_accuracy: 0.8890
17728/60000 [=======>......................] - ETA: 1:00 - loss: 0.3551 - categorical_accuracy: 0.8893
17792/60000 [=======>......................] - ETA: 1:00 - loss: 0.3541 - categorical_accuracy: 0.8896
17824/60000 [=======>......................] - ETA: 1:00 - loss: 0.3537 - categorical_accuracy: 0.8896
17888/60000 [=======>......................] - ETA: 1:00 - loss: 0.3537 - categorical_accuracy: 0.8898
17952/60000 [=======>......................] - ETA: 1:00 - loss: 0.3528 - categorical_accuracy: 0.8901
18016/60000 [========>.....................] - ETA: 1:00 - loss: 0.3518 - categorical_accuracy: 0.8904
18080/60000 [========>.....................] - ETA: 1:00 - loss: 0.3507 - categorical_accuracy: 0.8907
18144/60000 [========>.....................] - ETA: 1:00 - loss: 0.3501 - categorical_accuracy: 0.8908
18208/60000 [========>.....................] - ETA: 1:00 - loss: 0.3497 - categorical_accuracy: 0.8910
18272/60000 [========>.....................] - ETA: 1:00 - loss: 0.3492 - categorical_accuracy: 0.8913
18336/60000 [========>.....................] - ETA: 1:00 - loss: 0.3489 - categorical_accuracy: 0.8914
18400/60000 [========>.....................] - ETA: 59s - loss: 0.3479 - categorical_accuracy: 0.8917 
18464/60000 [========>.....................] - ETA: 59s - loss: 0.3473 - categorical_accuracy: 0.8919
18528/60000 [========>.....................] - ETA: 59s - loss: 0.3466 - categorical_accuracy: 0.8921
18592/60000 [========>.....................] - ETA: 59s - loss: 0.3459 - categorical_accuracy: 0.8923
18624/60000 [========>.....................] - ETA: 59s - loss: 0.3456 - categorical_accuracy: 0.8925
18688/60000 [========>.....................] - ETA: 59s - loss: 0.3446 - categorical_accuracy: 0.8928
18752/60000 [========>.....................] - ETA: 59s - loss: 0.3441 - categorical_accuracy: 0.8930
18816/60000 [========>.....................] - ETA: 59s - loss: 0.3436 - categorical_accuracy: 0.8931
18880/60000 [========>.....................] - ETA: 59s - loss: 0.3430 - categorical_accuracy: 0.8933
18944/60000 [========>.....................] - ETA: 59s - loss: 0.3425 - categorical_accuracy: 0.8935
19008/60000 [========>.....................] - ETA: 59s - loss: 0.3418 - categorical_accuracy: 0.8938
19072/60000 [========>.....................] - ETA: 58s - loss: 0.3409 - categorical_accuracy: 0.8940
19136/60000 [========>.....................] - ETA: 58s - loss: 0.3404 - categorical_accuracy: 0.8943
19200/60000 [========>.....................] - ETA: 58s - loss: 0.3394 - categorical_accuracy: 0.8946
19264/60000 [========>.....................] - ETA: 58s - loss: 0.3389 - categorical_accuracy: 0.8948
19328/60000 [========>.....................] - ETA: 58s - loss: 0.3382 - categorical_accuracy: 0.8950
19392/60000 [========>.....................] - ETA: 58s - loss: 0.3375 - categorical_accuracy: 0.8951
19456/60000 [========>.....................] - ETA: 58s - loss: 0.3365 - categorical_accuracy: 0.8954
19520/60000 [========>.....................] - ETA: 58s - loss: 0.3359 - categorical_accuracy: 0.8956
19552/60000 [========>.....................] - ETA: 58s - loss: 0.3356 - categorical_accuracy: 0.8957
19584/60000 [========>.....................] - ETA: 58s - loss: 0.3352 - categorical_accuracy: 0.8958
19648/60000 [========>.....................] - ETA: 58s - loss: 0.3343 - categorical_accuracy: 0.8961
19712/60000 [========>.....................] - ETA: 58s - loss: 0.3333 - categorical_accuracy: 0.8964
19776/60000 [========>.....................] - ETA: 57s - loss: 0.3330 - categorical_accuracy: 0.8965
19840/60000 [========>.....................] - ETA: 57s - loss: 0.3322 - categorical_accuracy: 0.8968
19904/60000 [========>.....................] - ETA: 57s - loss: 0.3313 - categorical_accuracy: 0.8971
19968/60000 [========>.....................] - ETA: 57s - loss: 0.3306 - categorical_accuracy: 0.8973
20032/60000 [=========>....................] - ETA: 57s - loss: 0.3302 - categorical_accuracy: 0.8974
20096/60000 [=========>....................] - ETA: 57s - loss: 0.3293 - categorical_accuracy: 0.8977
20160/60000 [=========>....................] - ETA: 57s - loss: 0.3286 - categorical_accuracy: 0.8978
20224/60000 [=========>....................] - ETA: 57s - loss: 0.3281 - categorical_accuracy: 0.8980
20288/60000 [=========>....................] - ETA: 57s - loss: 0.3272 - categorical_accuracy: 0.8982
20352/60000 [=========>....................] - ETA: 57s - loss: 0.3276 - categorical_accuracy: 0.8983
20416/60000 [=========>....................] - ETA: 57s - loss: 0.3269 - categorical_accuracy: 0.8986
20480/60000 [=========>....................] - ETA: 56s - loss: 0.3261 - categorical_accuracy: 0.8988
20544/60000 [=========>....................] - ETA: 56s - loss: 0.3257 - categorical_accuracy: 0.8989
20608/60000 [=========>....................] - ETA: 56s - loss: 0.3250 - categorical_accuracy: 0.8992
20672/60000 [=========>....................] - ETA: 56s - loss: 0.3241 - categorical_accuracy: 0.8995
20736/60000 [=========>....................] - ETA: 56s - loss: 0.3235 - categorical_accuracy: 0.8997
20800/60000 [=========>....................] - ETA: 56s - loss: 0.3228 - categorical_accuracy: 0.9000
20864/60000 [=========>....................] - ETA: 56s - loss: 0.3223 - categorical_accuracy: 0.9001
20928/60000 [=========>....................] - ETA: 56s - loss: 0.3218 - categorical_accuracy: 0.9003
20992/60000 [=========>....................] - ETA: 56s - loss: 0.3213 - categorical_accuracy: 0.9005
21056/60000 [=========>....................] - ETA: 56s - loss: 0.3210 - categorical_accuracy: 0.9006
21088/60000 [=========>....................] - ETA: 56s - loss: 0.3206 - categorical_accuracy: 0.9007
21152/60000 [=========>....................] - ETA: 55s - loss: 0.3201 - categorical_accuracy: 0.9009
21216/60000 [=========>....................] - ETA: 55s - loss: 0.3194 - categorical_accuracy: 0.9011
21280/60000 [=========>....................] - ETA: 55s - loss: 0.3187 - categorical_accuracy: 0.9014
21344/60000 [=========>....................] - ETA: 55s - loss: 0.3185 - categorical_accuracy: 0.9014
21408/60000 [=========>....................] - ETA: 55s - loss: 0.3182 - categorical_accuracy: 0.9015
21472/60000 [=========>....................] - ETA: 55s - loss: 0.3178 - categorical_accuracy: 0.9016
21536/60000 [=========>....................] - ETA: 55s - loss: 0.3173 - categorical_accuracy: 0.9018
21600/60000 [=========>....................] - ETA: 55s - loss: 0.3165 - categorical_accuracy: 0.9020
21664/60000 [=========>....................] - ETA: 55s - loss: 0.3163 - categorical_accuracy: 0.9022
21728/60000 [=========>....................] - ETA: 55s - loss: 0.3162 - categorical_accuracy: 0.9022
21792/60000 [=========>....................] - ETA: 55s - loss: 0.3160 - categorical_accuracy: 0.9023
21856/60000 [=========>....................] - ETA: 54s - loss: 0.3159 - categorical_accuracy: 0.9022
21920/60000 [=========>....................] - ETA: 54s - loss: 0.3157 - categorical_accuracy: 0.9022
21984/60000 [=========>....................] - ETA: 54s - loss: 0.3150 - categorical_accuracy: 0.9025
22048/60000 [==========>...................] - ETA: 54s - loss: 0.3145 - categorical_accuracy: 0.9026
22112/60000 [==========>...................] - ETA: 54s - loss: 0.3141 - categorical_accuracy: 0.9027
22176/60000 [==========>...................] - ETA: 54s - loss: 0.3133 - categorical_accuracy: 0.9030
22240/60000 [==========>...................] - ETA: 54s - loss: 0.3127 - categorical_accuracy: 0.9032
22304/60000 [==========>...................] - ETA: 54s - loss: 0.3120 - categorical_accuracy: 0.9035
22368/60000 [==========>...................] - ETA: 54s - loss: 0.3116 - categorical_accuracy: 0.9037
22432/60000 [==========>...................] - ETA: 54s - loss: 0.3109 - categorical_accuracy: 0.9039
22496/60000 [==========>...................] - ETA: 53s - loss: 0.3105 - categorical_accuracy: 0.9041
22560/60000 [==========>...................] - ETA: 53s - loss: 0.3100 - categorical_accuracy: 0.9043
22624/60000 [==========>...................] - ETA: 53s - loss: 0.3093 - categorical_accuracy: 0.9045
22688/60000 [==========>...................] - ETA: 53s - loss: 0.3088 - categorical_accuracy: 0.9046
22752/60000 [==========>...................] - ETA: 53s - loss: 0.3082 - categorical_accuracy: 0.9048
22816/60000 [==========>...................] - ETA: 53s - loss: 0.3078 - categorical_accuracy: 0.9049
22880/60000 [==========>...................] - ETA: 53s - loss: 0.3079 - categorical_accuracy: 0.9049
22944/60000 [==========>...................] - ETA: 53s - loss: 0.3072 - categorical_accuracy: 0.9051
23008/60000 [==========>...................] - ETA: 53s - loss: 0.3068 - categorical_accuracy: 0.9052
23072/60000 [==========>...................] - ETA: 53s - loss: 0.3063 - categorical_accuracy: 0.9054
23136/60000 [==========>...................] - ETA: 53s - loss: 0.3060 - categorical_accuracy: 0.9055
23200/60000 [==========>...................] - ETA: 52s - loss: 0.3055 - categorical_accuracy: 0.9057
23264/60000 [==========>...................] - ETA: 52s - loss: 0.3051 - categorical_accuracy: 0.9058
23328/60000 [==========>...................] - ETA: 52s - loss: 0.3045 - categorical_accuracy: 0.9060
23392/60000 [==========>...................] - ETA: 52s - loss: 0.3039 - categorical_accuracy: 0.9062
23456/60000 [==========>...................] - ETA: 52s - loss: 0.3032 - categorical_accuracy: 0.9064
23520/60000 [==========>...................] - ETA: 52s - loss: 0.3027 - categorical_accuracy: 0.9065
23584/60000 [==========>...................] - ETA: 52s - loss: 0.3021 - categorical_accuracy: 0.9067
23648/60000 [==========>...................] - ETA: 52s - loss: 0.3018 - categorical_accuracy: 0.9069
23712/60000 [==========>...................] - ETA: 52s - loss: 0.3015 - categorical_accuracy: 0.9069
23776/60000 [==========>...................] - ETA: 52s - loss: 0.3011 - categorical_accuracy: 0.9070
23808/60000 [==========>...................] - ETA: 52s - loss: 0.3010 - categorical_accuracy: 0.9070
23872/60000 [==========>...................] - ETA: 51s - loss: 0.3004 - categorical_accuracy: 0.9072
23904/60000 [==========>...................] - ETA: 51s - loss: 0.3002 - categorical_accuracy: 0.9073
23968/60000 [==========>...................] - ETA: 51s - loss: 0.2999 - categorical_accuracy: 0.9073
24032/60000 [===========>..................] - ETA: 51s - loss: 0.2995 - categorical_accuracy: 0.9074
24096/60000 [===========>..................] - ETA: 51s - loss: 0.2989 - categorical_accuracy: 0.9076
24160/60000 [===========>..................] - ETA: 51s - loss: 0.2985 - categorical_accuracy: 0.9077
24224/60000 [===========>..................] - ETA: 51s - loss: 0.2980 - categorical_accuracy: 0.9079
24288/60000 [===========>..................] - ETA: 51s - loss: 0.2974 - categorical_accuracy: 0.9081
24352/60000 [===========>..................] - ETA: 51s - loss: 0.2971 - categorical_accuracy: 0.9082
24416/60000 [===========>..................] - ETA: 51s - loss: 0.2970 - categorical_accuracy: 0.9082
24480/60000 [===========>..................] - ETA: 51s - loss: 0.2965 - categorical_accuracy: 0.9083
24544/60000 [===========>..................] - ETA: 51s - loss: 0.2959 - categorical_accuracy: 0.9085
24608/60000 [===========>..................] - ETA: 50s - loss: 0.2953 - categorical_accuracy: 0.9088
24672/60000 [===========>..................] - ETA: 50s - loss: 0.2948 - categorical_accuracy: 0.9089
24736/60000 [===========>..................] - ETA: 50s - loss: 0.2942 - categorical_accuracy: 0.9091
24800/60000 [===========>..................] - ETA: 50s - loss: 0.2935 - categorical_accuracy: 0.9094
24864/60000 [===========>..................] - ETA: 50s - loss: 0.2929 - categorical_accuracy: 0.9095
24928/60000 [===========>..................] - ETA: 50s - loss: 0.2927 - categorical_accuracy: 0.9097
24992/60000 [===========>..................] - ETA: 50s - loss: 0.2921 - categorical_accuracy: 0.9099
25056/60000 [===========>..................] - ETA: 50s - loss: 0.2921 - categorical_accuracy: 0.9099
25120/60000 [===========>..................] - ETA: 50s - loss: 0.2917 - categorical_accuracy: 0.9100
25184/60000 [===========>..................] - ETA: 50s - loss: 0.2911 - categorical_accuracy: 0.9102
25248/60000 [===========>..................] - ETA: 49s - loss: 0.2910 - categorical_accuracy: 0.9103
25312/60000 [===========>..................] - ETA: 49s - loss: 0.2905 - categorical_accuracy: 0.9104
25376/60000 [===========>..................] - ETA: 49s - loss: 0.2906 - categorical_accuracy: 0.9105
25440/60000 [===========>..................] - ETA: 49s - loss: 0.2901 - categorical_accuracy: 0.9106
25504/60000 [===========>..................] - ETA: 49s - loss: 0.2896 - categorical_accuracy: 0.9108
25568/60000 [===========>..................] - ETA: 49s - loss: 0.2891 - categorical_accuracy: 0.9109
25632/60000 [===========>..................] - ETA: 49s - loss: 0.2888 - categorical_accuracy: 0.9110
25696/60000 [===========>..................] - ETA: 49s - loss: 0.2885 - categorical_accuracy: 0.9112
25760/60000 [===========>..................] - ETA: 49s - loss: 0.2881 - categorical_accuracy: 0.9113
25824/60000 [===========>..................] - ETA: 49s - loss: 0.2882 - categorical_accuracy: 0.9114
25888/60000 [===========>..................] - ETA: 49s - loss: 0.2876 - categorical_accuracy: 0.9115
25952/60000 [===========>..................] - ETA: 48s - loss: 0.2869 - categorical_accuracy: 0.9117
26016/60000 [============>.................] - ETA: 48s - loss: 0.2865 - categorical_accuracy: 0.9119
26080/60000 [============>.................] - ETA: 48s - loss: 0.2862 - categorical_accuracy: 0.9119
26144/60000 [============>.................] - ETA: 48s - loss: 0.2858 - categorical_accuracy: 0.9119
26208/60000 [============>.................] - ETA: 48s - loss: 0.2852 - categorical_accuracy: 0.9121
26272/60000 [============>.................] - ETA: 48s - loss: 0.2849 - categorical_accuracy: 0.9122
26336/60000 [============>.................] - ETA: 48s - loss: 0.2844 - categorical_accuracy: 0.9124
26400/60000 [============>.................] - ETA: 48s - loss: 0.2838 - categorical_accuracy: 0.9126
26464/60000 [============>.................] - ETA: 48s - loss: 0.2835 - categorical_accuracy: 0.9127
26496/60000 [============>.................] - ETA: 48s - loss: 0.2833 - categorical_accuracy: 0.9128
26560/60000 [============>.................] - ETA: 48s - loss: 0.2827 - categorical_accuracy: 0.9129
26624/60000 [============>.................] - ETA: 47s - loss: 0.2824 - categorical_accuracy: 0.9129
26688/60000 [============>.................] - ETA: 47s - loss: 0.2822 - categorical_accuracy: 0.9130
26752/60000 [============>.................] - ETA: 47s - loss: 0.2824 - categorical_accuracy: 0.9130
26816/60000 [============>.................] - ETA: 47s - loss: 0.2824 - categorical_accuracy: 0.9130
26880/60000 [============>.................] - ETA: 47s - loss: 0.2818 - categorical_accuracy: 0.9132
26944/60000 [============>.................] - ETA: 47s - loss: 0.2819 - categorical_accuracy: 0.9132
27008/60000 [============>.................] - ETA: 47s - loss: 0.2814 - categorical_accuracy: 0.9133
27072/60000 [============>.................] - ETA: 47s - loss: 0.2809 - categorical_accuracy: 0.9135
27136/60000 [============>.................] - ETA: 47s - loss: 0.2804 - categorical_accuracy: 0.9137
27200/60000 [============>.................] - ETA: 47s - loss: 0.2804 - categorical_accuracy: 0.9136
27264/60000 [============>.................] - ETA: 47s - loss: 0.2799 - categorical_accuracy: 0.9138
27328/60000 [============>.................] - ETA: 46s - loss: 0.2795 - categorical_accuracy: 0.9139
27392/60000 [============>.................] - ETA: 46s - loss: 0.2789 - categorical_accuracy: 0.9141
27456/60000 [============>.................] - ETA: 46s - loss: 0.2785 - categorical_accuracy: 0.9142
27520/60000 [============>.................] - ETA: 46s - loss: 0.2785 - categorical_accuracy: 0.9142
27584/60000 [============>.................] - ETA: 46s - loss: 0.2780 - categorical_accuracy: 0.9143
27648/60000 [============>.................] - ETA: 46s - loss: 0.2775 - categorical_accuracy: 0.9145
27712/60000 [============>.................] - ETA: 46s - loss: 0.2771 - categorical_accuracy: 0.9146
27776/60000 [============>.................] - ETA: 46s - loss: 0.2770 - categorical_accuracy: 0.9146
27840/60000 [============>.................] - ETA: 46s - loss: 0.2769 - categorical_accuracy: 0.9147
27904/60000 [============>.................] - ETA: 46s - loss: 0.2770 - categorical_accuracy: 0.9147
27968/60000 [============>.................] - ETA: 46s - loss: 0.2768 - categorical_accuracy: 0.9147
28032/60000 [=============>................] - ETA: 45s - loss: 0.2763 - categorical_accuracy: 0.9148
28096/60000 [=============>................] - ETA: 45s - loss: 0.2759 - categorical_accuracy: 0.9150
28128/60000 [=============>................] - ETA: 45s - loss: 0.2756 - categorical_accuracy: 0.9150
28160/60000 [=============>................] - ETA: 45s - loss: 0.2754 - categorical_accuracy: 0.9151
28224/60000 [=============>................] - ETA: 45s - loss: 0.2752 - categorical_accuracy: 0.9151
28288/60000 [=============>................] - ETA: 45s - loss: 0.2746 - categorical_accuracy: 0.9153
28352/60000 [=============>................] - ETA: 45s - loss: 0.2741 - categorical_accuracy: 0.9155
28416/60000 [=============>................] - ETA: 45s - loss: 0.2737 - categorical_accuracy: 0.9156
28480/60000 [=============>................] - ETA: 45s - loss: 0.2735 - categorical_accuracy: 0.9157
28544/60000 [=============>................] - ETA: 45s - loss: 0.2731 - categorical_accuracy: 0.9158
28608/60000 [=============>................] - ETA: 45s - loss: 0.2728 - categorical_accuracy: 0.9159
28672/60000 [=============>................] - ETA: 44s - loss: 0.2727 - categorical_accuracy: 0.9160
28736/60000 [=============>................] - ETA: 44s - loss: 0.2725 - categorical_accuracy: 0.9160
28800/60000 [=============>................] - ETA: 44s - loss: 0.2724 - categorical_accuracy: 0.9160
28864/60000 [=============>................] - ETA: 44s - loss: 0.2719 - categorical_accuracy: 0.9162
28928/60000 [=============>................] - ETA: 44s - loss: 0.2714 - categorical_accuracy: 0.9163
28992/60000 [=============>................] - ETA: 44s - loss: 0.2712 - categorical_accuracy: 0.9165
29056/60000 [=============>................] - ETA: 44s - loss: 0.2708 - categorical_accuracy: 0.9166
29120/60000 [=============>................] - ETA: 44s - loss: 0.2703 - categorical_accuracy: 0.9168
29184/60000 [=============>................] - ETA: 44s - loss: 0.2699 - categorical_accuracy: 0.9169
29248/60000 [=============>................] - ETA: 44s - loss: 0.2699 - categorical_accuracy: 0.9170
29312/60000 [=============>................] - ETA: 44s - loss: 0.2696 - categorical_accuracy: 0.9170
29376/60000 [=============>................] - ETA: 43s - loss: 0.2692 - categorical_accuracy: 0.9171
29440/60000 [=============>................] - ETA: 43s - loss: 0.2688 - categorical_accuracy: 0.9172
29504/60000 [=============>................] - ETA: 43s - loss: 0.2684 - categorical_accuracy: 0.9173
29568/60000 [=============>................] - ETA: 43s - loss: 0.2679 - categorical_accuracy: 0.9175
29632/60000 [=============>................] - ETA: 43s - loss: 0.2678 - categorical_accuracy: 0.9176
29696/60000 [=============>................] - ETA: 43s - loss: 0.2676 - categorical_accuracy: 0.9176
29760/60000 [=============>................] - ETA: 43s - loss: 0.2673 - categorical_accuracy: 0.9177
29824/60000 [=============>................] - ETA: 43s - loss: 0.2670 - categorical_accuracy: 0.9178
29888/60000 [=============>................] - ETA: 43s - loss: 0.2667 - categorical_accuracy: 0.9178
29952/60000 [=============>................] - ETA: 43s - loss: 0.2665 - categorical_accuracy: 0.9179
30016/60000 [==============>...............] - ETA: 43s - loss: 0.2660 - categorical_accuracy: 0.9180
30080/60000 [==============>...............] - ETA: 42s - loss: 0.2655 - categorical_accuracy: 0.9182
30112/60000 [==============>...............] - ETA: 42s - loss: 0.2652 - categorical_accuracy: 0.9183
30176/60000 [==============>...............] - ETA: 42s - loss: 0.2649 - categorical_accuracy: 0.9184
30240/60000 [==============>...............] - ETA: 42s - loss: 0.2646 - categorical_accuracy: 0.9185
30272/60000 [==============>...............] - ETA: 42s - loss: 0.2647 - categorical_accuracy: 0.9184
30304/60000 [==============>...............] - ETA: 42s - loss: 0.2645 - categorical_accuracy: 0.9185
30368/60000 [==============>...............] - ETA: 42s - loss: 0.2641 - categorical_accuracy: 0.9186
30432/60000 [==============>...............] - ETA: 42s - loss: 0.2637 - categorical_accuracy: 0.9188
30496/60000 [==============>...............] - ETA: 42s - loss: 0.2633 - categorical_accuracy: 0.9189
30560/60000 [==============>...............] - ETA: 42s - loss: 0.2634 - categorical_accuracy: 0.9189
30624/60000 [==============>...............] - ETA: 42s - loss: 0.2633 - categorical_accuracy: 0.9189
30688/60000 [==============>...............] - ETA: 42s - loss: 0.2628 - categorical_accuracy: 0.9191
30752/60000 [==============>...............] - ETA: 41s - loss: 0.2628 - categorical_accuracy: 0.9191
30816/60000 [==============>...............] - ETA: 41s - loss: 0.2626 - categorical_accuracy: 0.9192
30880/60000 [==============>...............] - ETA: 41s - loss: 0.2623 - categorical_accuracy: 0.9193
30944/60000 [==============>...............] - ETA: 41s - loss: 0.2620 - categorical_accuracy: 0.9194
31008/60000 [==============>...............] - ETA: 41s - loss: 0.2620 - categorical_accuracy: 0.9194
31072/60000 [==============>...............] - ETA: 41s - loss: 0.2618 - categorical_accuracy: 0.9195
31136/60000 [==============>...............] - ETA: 41s - loss: 0.2615 - categorical_accuracy: 0.9196
31200/60000 [==============>...............] - ETA: 41s - loss: 0.2612 - categorical_accuracy: 0.9197
31264/60000 [==============>...............] - ETA: 41s - loss: 0.2608 - categorical_accuracy: 0.9198
31328/60000 [==============>...............] - ETA: 41s - loss: 0.2608 - categorical_accuracy: 0.9198
31392/60000 [==============>...............] - ETA: 41s - loss: 0.2611 - categorical_accuracy: 0.9198
31456/60000 [==============>...............] - ETA: 40s - loss: 0.2608 - categorical_accuracy: 0.9199
31520/60000 [==============>...............] - ETA: 40s - loss: 0.2604 - categorical_accuracy: 0.9200
31552/60000 [==============>...............] - ETA: 40s - loss: 0.2603 - categorical_accuracy: 0.9200
31616/60000 [==============>...............] - ETA: 40s - loss: 0.2600 - categorical_accuracy: 0.9201
31680/60000 [==============>...............] - ETA: 40s - loss: 0.2598 - categorical_accuracy: 0.9202
31744/60000 [==============>...............] - ETA: 40s - loss: 0.2595 - categorical_accuracy: 0.9203
31808/60000 [==============>...............] - ETA: 40s - loss: 0.2593 - categorical_accuracy: 0.9204
31872/60000 [==============>...............] - ETA: 40s - loss: 0.2590 - categorical_accuracy: 0.9205
31936/60000 [==============>...............] - ETA: 40s - loss: 0.2587 - categorical_accuracy: 0.9206
32000/60000 [===============>..............] - ETA: 40s - loss: 0.2584 - categorical_accuracy: 0.9207
32064/60000 [===============>..............] - ETA: 40s - loss: 0.2581 - categorical_accuracy: 0.9208
32096/60000 [===============>..............] - ETA: 40s - loss: 0.2579 - categorical_accuracy: 0.9208
32160/60000 [===============>..............] - ETA: 39s - loss: 0.2578 - categorical_accuracy: 0.9208
32224/60000 [===============>..............] - ETA: 39s - loss: 0.2573 - categorical_accuracy: 0.9210
32288/60000 [===============>..............] - ETA: 39s - loss: 0.2569 - categorical_accuracy: 0.9211
32352/60000 [===============>..............] - ETA: 39s - loss: 0.2566 - categorical_accuracy: 0.9212
32384/60000 [===============>..............] - ETA: 39s - loss: 0.2563 - categorical_accuracy: 0.9213
32416/60000 [===============>..............] - ETA: 39s - loss: 0.2562 - categorical_accuracy: 0.9214
32480/60000 [===============>..............] - ETA: 39s - loss: 0.2559 - categorical_accuracy: 0.9215
32544/60000 [===============>..............] - ETA: 39s - loss: 0.2555 - categorical_accuracy: 0.9216
32608/60000 [===============>..............] - ETA: 39s - loss: 0.2550 - categorical_accuracy: 0.9217
32672/60000 [===============>..............] - ETA: 39s - loss: 0.2549 - categorical_accuracy: 0.9218
32736/60000 [===============>..............] - ETA: 39s - loss: 0.2548 - categorical_accuracy: 0.9219
32800/60000 [===============>..............] - ETA: 39s - loss: 0.2548 - categorical_accuracy: 0.9219
32864/60000 [===============>..............] - ETA: 38s - loss: 0.2546 - categorical_accuracy: 0.9220
32928/60000 [===============>..............] - ETA: 38s - loss: 0.2543 - categorical_accuracy: 0.9221
32992/60000 [===============>..............] - ETA: 38s - loss: 0.2539 - categorical_accuracy: 0.9222
33056/60000 [===============>..............] - ETA: 38s - loss: 0.2536 - categorical_accuracy: 0.9223
33120/60000 [===============>..............] - ETA: 38s - loss: 0.2535 - categorical_accuracy: 0.9223
33184/60000 [===============>..............] - ETA: 38s - loss: 0.2532 - categorical_accuracy: 0.9224
33248/60000 [===============>..............] - ETA: 38s - loss: 0.2530 - categorical_accuracy: 0.9224
33312/60000 [===============>..............] - ETA: 38s - loss: 0.2526 - categorical_accuracy: 0.9226
33376/60000 [===============>..............] - ETA: 38s - loss: 0.2524 - categorical_accuracy: 0.9226
33440/60000 [===============>..............] - ETA: 38s - loss: 0.2521 - categorical_accuracy: 0.9227
33504/60000 [===============>..............] - ETA: 38s - loss: 0.2518 - categorical_accuracy: 0.9228
33568/60000 [===============>..............] - ETA: 37s - loss: 0.2514 - categorical_accuracy: 0.9229
33632/60000 [===============>..............] - ETA: 37s - loss: 0.2510 - categorical_accuracy: 0.9230
33696/60000 [===============>..............] - ETA: 37s - loss: 0.2508 - categorical_accuracy: 0.9231
33760/60000 [===============>..............] - ETA: 37s - loss: 0.2504 - categorical_accuracy: 0.9232
33824/60000 [===============>..............] - ETA: 37s - loss: 0.2501 - categorical_accuracy: 0.9233
33888/60000 [===============>..............] - ETA: 37s - loss: 0.2497 - categorical_accuracy: 0.9234
33952/60000 [===============>..............] - ETA: 37s - loss: 0.2494 - categorical_accuracy: 0.9235
34016/60000 [================>.............] - ETA: 37s - loss: 0.2491 - categorical_accuracy: 0.9235
34080/60000 [================>.............] - ETA: 37s - loss: 0.2488 - categorical_accuracy: 0.9236
34144/60000 [================>.............] - ETA: 37s - loss: 0.2486 - categorical_accuracy: 0.9237
34176/60000 [================>.............] - ETA: 37s - loss: 0.2486 - categorical_accuracy: 0.9237
34240/60000 [================>.............] - ETA: 36s - loss: 0.2484 - categorical_accuracy: 0.9238
34304/60000 [================>.............] - ETA: 36s - loss: 0.2480 - categorical_accuracy: 0.9239
34368/60000 [================>.............] - ETA: 36s - loss: 0.2478 - categorical_accuracy: 0.9239
34432/60000 [================>.............] - ETA: 36s - loss: 0.2477 - categorical_accuracy: 0.9240
34496/60000 [================>.............] - ETA: 36s - loss: 0.2475 - categorical_accuracy: 0.9240
34560/60000 [================>.............] - ETA: 36s - loss: 0.2474 - categorical_accuracy: 0.9240
34592/60000 [================>.............] - ETA: 36s - loss: 0.2472 - categorical_accuracy: 0.9241
34656/60000 [================>.............] - ETA: 36s - loss: 0.2469 - categorical_accuracy: 0.9242
34720/60000 [================>.............] - ETA: 36s - loss: 0.2466 - categorical_accuracy: 0.9242
34784/60000 [================>.............] - ETA: 36s - loss: 0.2463 - categorical_accuracy: 0.9242
34816/60000 [================>.............] - ETA: 36s - loss: 0.2462 - categorical_accuracy: 0.9243
34880/60000 [================>.............] - ETA: 36s - loss: 0.2459 - categorical_accuracy: 0.9244
34944/60000 [================>.............] - ETA: 35s - loss: 0.2457 - categorical_accuracy: 0.9245
35008/60000 [================>.............] - ETA: 35s - loss: 0.2453 - categorical_accuracy: 0.9246
35072/60000 [================>.............] - ETA: 35s - loss: 0.2449 - categorical_accuracy: 0.9247
35136/60000 [================>.............] - ETA: 35s - loss: 0.2446 - categorical_accuracy: 0.9248
35200/60000 [================>.............] - ETA: 35s - loss: 0.2445 - categorical_accuracy: 0.9249
35264/60000 [================>.............] - ETA: 35s - loss: 0.2443 - categorical_accuracy: 0.9249
35328/60000 [================>.............] - ETA: 35s - loss: 0.2441 - categorical_accuracy: 0.9250
35392/60000 [================>.............] - ETA: 35s - loss: 0.2437 - categorical_accuracy: 0.9251
35456/60000 [================>.............] - ETA: 35s - loss: 0.2435 - categorical_accuracy: 0.9251
35520/60000 [================>.............] - ETA: 35s - loss: 0.2432 - categorical_accuracy: 0.9252
35584/60000 [================>.............] - ETA: 35s - loss: 0.2430 - categorical_accuracy: 0.9253
35648/60000 [================>.............] - ETA: 34s - loss: 0.2427 - categorical_accuracy: 0.9253
35712/60000 [================>.............] - ETA: 34s - loss: 0.2425 - categorical_accuracy: 0.9253
35776/60000 [================>.............] - ETA: 34s - loss: 0.2423 - categorical_accuracy: 0.9254
35840/60000 [================>.............] - ETA: 34s - loss: 0.2420 - categorical_accuracy: 0.9255
35904/60000 [================>.............] - ETA: 34s - loss: 0.2419 - categorical_accuracy: 0.9255
35968/60000 [================>.............] - ETA: 34s - loss: 0.2417 - categorical_accuracy: 0.9256
36032/60000 [=================>............] - ETA: 34s - loss: 0.2415 - categorical_accuracy: 0.9256
36096/60000 [=================>............] - ETA: 34s - loss: 0.2412 - categorical_accuracy: 0.9257
36160/60000 [=================>............] - ETA: 34s - loss: 0.2409 - categorical_accuracy: 0.9258
36224/60000 [=================>............] - ETA: 34s - loss: 0.2408 - categorical_accuracy: 0.9258
36288/60000 [=================>............] - ETA: 33s - loss: 0.2405 - categorical_accuracy: 0.9259
36352/60000 [=================>............] - ETA: 33s - loss: 0.2401 - categorical_accuracy: 0.9259
36416/60000 [=================>............] - ETA: 33s - loss: 0.2399 - categorical_accuracy: 0.9260
36480/60000 [=================>............] - ETA: 33s - loss: 0.2399 - categorical_accuracy: 0.9260
36544/60000 [=================>............] - ETA: 33s - loss: 0.2395 - categorical_accuracy: 0.9261
36608/60000 [=================>............] - ETA: 33s - loss: 0.2394 - categorical_accuracy: 0.9262
36672/60000 [=================>............] - ETA: 33s - loss: 0.2391 - categorical_accuracy: 0.9262
36736/60000 [=================>............] - ETA: 33s - loss: 0.2390 - categorical_accuracy: 0.9263
36800/60000 [=================>............] - ETA: 33s - loss: 0.2386 - categorical_accuracy: 0.9264
36864/60000 [=================>............] - ETA: 33s - loss: 0.2385 - categorical_accuracy: 0.9264
36928/60000 [=================>............] - ETA: 33s - loss: 0.2382 - categorical_accuracy: 0.9265
36992/60000 [=================>............] - ETA: 32s - loss: 0.2382 - categorical_accuracy: 0.9265
37056/60000 [=================>............] - ETA: 32s - loss: 0.2378 - categorical_accuracy: 0.9266
37120/60000 [=================>............] - ETA: 32s - loss: 0.2376 - categorical_accuracy: 0.9266
37184/60000 [=================>............] - ETA: 32s - loss: 0.2374 - categorical_accuracy: 0.9267
37248/60000 [=================>............] - ETA: 32s - loss: 0.2372 - categorical_accuracy: 0.9268
37312/60000 [=================>............] - ETA: 32s - loss: 0.2370 - categorical_accuracy: 0.9268
37376/60000 [=================>............] - ETA: 32s - loss: 0.2368 - categorical_accuracy: 0.9269
37440/60000 [=================>............] - ETA: 32s - loss: 0.2365 - categorical_accuracy: 0.9270
37504/60000 [=================>............] - ETA: 32s - loss: 0.2362 - categorical_accuracy: 0.9271
37568/60000 [=================>............] - ETA: 32s - loss: 0.2359 - categorical_accuracy: 0.9272
37632/60000 [=================>............] - ETA: 32s - loss: 0.2356 - categorical_accuracy: 0.9273
37696/60000 [=================>............] - ETA: 31s - loss: 0.2355 - categorical_accuracy: 0.9274
37760/60000 [=================>............] - ETA: 31s - loss: 0.2355 - categorical_accuracy: 0.9274
37824/60000 [=================>............] - ETA: 31s - loss: 0.2353 - categorical_accuracy: 0.9274
37888/60000 [=================>............] - ETA: 31s - loss: 0.2351 - categorical_accuracy: 0.9274
37952/60000 [=================>............] - ETA: 31s - loss: 0.2350 - categorical_accuracy: 0.9275
38016/60000 [==================>...........] - ETA: 31s - loss: 0.2347 - categorical_accuracy: 0.9276
38080/60000 [==================>...........] - ETA: 31s - loss: 0.2345 - categorical_accuracy: 0.9276
38144/60000 [==================>...........] - ETA: 31s - loss: 0.2342 - categorical_accuracy: 0.9277
38208/60000 [==================>...........] - ETA: 31s - loss: 0.2340 - categorical_accuracy: 0.9277
38272/60000 [==================>...........] - ETA: 31s - loss: 0.2338 - categorical_accuracy: 0.9278
38336/60000 [==================>...........] - ETA: 31s - loss: 0.2336 - categorical_accuracy: 0.9279
38400/60000 [==================>...........] - ETA: 30s - loss: 0.2336 - categorical_accuracy: 0.9279
38464/60000 [==================>...........] - ETA: 30s - loss: 0.2333 - categorical_accuracy: 0.9280
38528/60000 [==================>...........] - ETA: 30s - loss: 0.2330 - categorical_accuracy: 0.9281
38592/60000 [==================>...........] - ETA: 30s - loss: 0.2329 - categorical_accuracy: 0.9281
38656/60000 [==================>...........] - ETA: 30s - loss: 0.2327 - categorical_accuracy: 0.9282
38720/60000 [==================>...........] - ETA: 30s - loss: 0.2327 - categorical_accuracy: 0.9282
38784/60000 [==================>...........] - ETA: 30s - loss: 0.2324 - categorical_accuracy: 0.9282
38848/60000 [==================>...........] - ETA: 30s - loss: 0.2322 - categorical_accuracy: 0.9283
38912/60000 [==================>...........] - ETA: 30s - loss: 0.2321 - categorical_accuracy: 0.9282
38976/60000 [==================>...........] - ETA: 30s - loss: 0.2319 - categorical_accuracy: 0.9283
39008/60000 [==================>...........] - ETA: 30s - loss: 0.2318 - categorical_accuracy: 0.9283
39072/60000 [==================>...........] - ETA: 29s - loss: 0.2317 - categorical_accuracy: 0.9284
39136/60000 [==================>...........] - ETA: 29s - loss: 0.2314 - categorical_accuracy: 0.9285
39200/60000 [==================>...........] - ETA: 29s - loss: 0.2311 - categorical_accuracy: 0.9285
39264/60000 [==================>...........] - ETA: 29s - loss: 0.2308 - categorical_accuracy: 0.9286
39328/60000 [==================>...........] - ETA: 29s - loss: 0.2305 - categorical_accuracy: 0.9288
39392/60000 [==================>...........] - ETA: 29s - loss: 0.2303 - categorical_accuracy: 0.9288
39456/60000 [==================>...........] - ETA: 29s - loss: 0.2301 - categorical_accuracy: 0.9288
39520/60000 [==================>...........] - ETA: 29s - loss: 0.2298 - categorical_accuracy: 0.9289
39584/60000 [==================>...........] - ETA: 29s - loss: 0.2298 - categorical_accuracy: 0.9289
39648/60000 [==================>...........] - ETA: 29s - loss: 0.2298 - categorical_accuracy: 0.9289
39712/60000 [==================>...........] - ETA: 29s - loss: 0.2297 - categorical_accuracy: 0.9289
39776/60000 [==================>...........] - ETA: 28s - loss: 0.2294 - categorical_accuracy: 0.9291
39840/60000 [==================>...........] - ETA: 28s - loss: 0.2293 - categorical_accuracy: 0.9291
39904/60000 [==================>...........] - ETA: 28s - loss: 0.2292 - categorical_accuracy: 0.9292
39968/60000 [==================>...........] - ETA: 28s - loss: 0.2290 - categorical_accuracy: 0.9292
40032/60000 [===================>..........] - ETA: 28s - loss: 0.2287 - categorical_accuracy: 0.9293
40096/60000 [===================>..........] - ETA: 28s - loss: 0.2287 - categorical_accuracy: 0.9294
40160/60000 [===================>..........] - ETA: 28s - loss: 0.2287 - categorical_accuracy: 0.9295
40224/60000 [===================>..........] - ETA: 28s - loss: 0.2284 - categorical_accuracy: 0.9295
40288/60000 [===================>..........] - ETA: 28s - loss: 0.2283 - categorical_accuracy: 0.9295
40320/60000 [===================>..........] - ETA: 28s - loss: 0.2282 - categorical_accuracy: 0.9295
40384/60000 [===================>..........] - ETA: 28s - loss: 0.2281 - categorical_accuracy: 0.9295
40448/60000 [===================>..........] - ETA: 27s - loss: 0.2278 - categorical_accuracy: 0.9296
40512/60000 [===================>..........] - ETA: 27s - loss: 0.2275 - categorical_accuracy: 0.9297
40576/60000 [===================>..........] - ETA: 27s - loss: 0.2272 - categorical_accuracy: 0.9298
40640/60000 [===================>..........] - ETA: 27s - loss: 0.2269 - categorical_accuracy: 0.9299
40704/60000 [===================>..........] - ETA: 27s - loss: 0.2269 - categorical_accuracy: 0.9300
40768/60000 [===================>..........] - ETA: 27s - loss: 0.2268 - categorical_accuracy: 0.9300
40832/60000 [===================>..........] - ETA: 27s - loss: 0.2269 - categorical_accuracy: 0.9300
40896/60000 [===================>..........] - ETA: 27s - loss: 0.2266 - categorical_accuracy: 0.9301
40960/60000 [===================>..........] - ETA: 27s - loss: 0.2265 - categorical_accuracy: 0.9301
41024/60000 [===================>..........] - ETA: 27s - loss: 0.2264 - categorical_accuracy: 0.9302
41088/60000 [===================>..........] - ETA: 27s - loss: 0.2261 - categorical_accuracy: 0.9303
41152/60000 [===================>..........] - ETA: 26s - loss: 0.2259 - categorical_accuracy: 0.9303
41184/60000 [===================>..........] - ETA: 26s - loss: 0.2259 - categorical_accuracy: 0.9303
41248/60000 [===================>..........] - ETA: 26s - loss: 0.2259 - categorical_accuracy: 0.9303
41312/60000 [===================>..........] - ETA: 26s - loss: 0.2256 - categorical_accuracy: 0.9304
41376/60000 [===================>..........] - ETA: 26s - loss: 0.2253 - categorical_accuracy: 0.9305
41440/60000 [===================>..........] - ETA: 26s - loss: 0.2251 - categorical_accuracy: 0.9306
41504/60000 [===================>..........] - ETA: 26s - loss: 0.2248 - categorical_accuracy: 0.9307
41568/60000 [===================>..........] - ETA: 26s - loss: 0.2246 - categorical_accuracy: 0.9308
41632/60000 [===================>..........] - ETA: 26s - loss: 0.2245 - categorical_accuracy: 0.9308
41696/60000 [===================>..........] - ETA: 26s - loss: 0.2243 - categorical_accuracy: 0.9309
41760/60000 [===================>..........] - ETA: 26s - loss: 0.2242 - categorical_accuracy: 0.9309
41824/60000 [===================>..........] - ETA: 25s - loss: 0.2241 - categorical_accuracy: 0.9310
41888/60000 [===================>..........] - ETA: 25s - loss: 0.2238 - categorical_accuracy: 0.9311
41952/60000 [===================>..........] - ETA: 25s - loss: 0.2236 - categorical_accuracy: 0.9312
42016/60000 [====================>.........] - ETA: 25s - loss: 0.2234 - categorical_accuracy: 0.9312
42080/60000 [====================>.........] - ETA: 25s - loss: 0.2231 - categorical_accuracy: 0.9313
42144/60000 [====================>.........] - ETA: 25s - loss: 0.2229 - categorical_accuracy: 0.9314
42208/60000 [====================>.........] - ETA: 25s - loss: 0.2226 - categorical_accuracy: 0.9315
42272/60000 [====================>.........] - ETA: 25s - loss: 0.2225 - categorical_accuracy: 0.9315
42336/60000 [====================>.........] - ETA: 25s - loss: 0.2223 - categorical_accuracy: 0.9316
42400/60000 [====================>.........] - ETA: 25s - loss: 0.2222 - categorical_accuracy: 0.9317
42464/60000 [====================>.........] - ETA: 25s - loss: 0.2219 - categorical_accuracy: 0.9317
42528/60000 [====================>.........] - ETA: 24s - loss: 0.2219 - categorical_accuracy: 0.9317
42592/60000 [====================>.........] - ETA: 24s - loss: 0.2216 - categorical_accuracy: 0.9318
42656/60000 [====================>.........] - ETA: 24s - loss: 0.2216 - categorical_accuracy: 0.9319
42720/60000 [====================>.........] - ETA: 24s - loss: 0.2213 - categorical_accuracy: 0.9320
42784/60000 [====================>.........] - ETA: 24s - loss: 0.2214 - categorical_accuracy: 0.9320
42848/60000 [====================>.........] - ETA: 24s - loss: 0.2211 - categorical_accuracy: 0.9321
42912/60000 [====================>.........] - ETA: 24s - loss: 0.2209 - categorical_accuracy: 0.9321
42976/60000 [====================>.........] - ETA: 24s - loss: 0.2209 - categorical_accuracy: 0.9321
43040/60000 [====================>.........] - ETA: 24s - loss: 0.2207 - categorical_accuracy: 0.9322
43104/60000 [====================>.........] - ETA: 24s - loss: 0.2206 - categorical_accuracy: 0.9322
43168/60000 [====================>.........] - ETA: 24s - loss: 0.2205 - categorical_accuracy: 0.9322
43232/60000 [====================>.........] - ETA: 23s - loss: 0.2204 - categorical_accuracy: 0.9323
43296/60000 [====================>.........] - ETA: 23s - loss: 0.2203 - categorical_accuracy: 0.9323
43360/60000 [====================>.........] - ETA: 23s - loss: 0.2200 - categorical_accuracy: 0.9324
43424/60000 [====================>.........] - ETA: 23s - loss: 0.2198 - categorical_accuracy: 0.9324
43488/60000 [====================>.........] - ETA: 23s - loss: 0.2196 - categorical_accuracy: 0.9324
43552/60000 [====================>.........] - ETA: 23s - loss: 0.2194 - categorical_accuracy: 0.9325
43616/60000 [====================>.........] - ETA: 23s - loss: 0.2193 - categorical_accuracy: 0.9325
43680/60000 [====================>.........] - ETA: 23s - loss: 0.2192 - categorical_accuracy: 0.9326
43744/60000 [====================>.........] - ETA: 23s - loss: 0.2190 - categorical_accuracy: 0.9326
43808/60000 [====================>.........] - ETA: 23s - loss: 0.2189 - categorical_accuracy: 0.9326
43872/60000 [====================>.........] - ETA: 23s - loss: 0.2188 - categorical_accuracy: 0.9327
43936/60000 [====================>.........] - ETA: 22s - loss: 0.2185 - categorical_accuracy: 0.9328
44000/60000 [=====================>........] - ETA: 22s - loss: 0.2184 - categorical_accuracy: 0.9328
44064/60000 [=====================>........] - ETA: 22s - loss: 0.2181 - categorical_accuracy: 0.9329
44128/60000 [=====================>........] - ETA: 22s - loss: 0.2181 - categorical_accuracy: 0.9329
44192/60000 [=====================>........] - ETA: 22s - loss: 0.2178 - categorical_accuracy: 0.9330
44256/60000 [=====================>........] - ETA: 22s - loss: 0.2175 - categorical_accuracy: 0.9331
44320/60000 [=====================>........] - ETA: 22s - loss: 0.2173 - categorical_accuracy: 0.9332
44384/60000 [=====================>........] - ETA: 22s - loss: 0.2171 - categorical_accuracy: 0.9333
44448/60000 [=====================>........] - ETA: 22s - loss: 0.2169 - categorical_accuracy: 0.9333
44512/60000 [=====================>........] - ETA: 22s - loss: 0.2167 - categorical_accuracy: 0.9334
44576/60000 [=====================>........] - ETA: 22s - loss: 0.2164 - categorical_accuracy: 0.9335
44640/60000 [=====================>........] - ETA: 21s - loss: 0.2164 - categorical_accuracy: 0.9335
44704/60000 [=====================>........] - ETA: 21s - loss: 0.2162 - categorical_accuracy: 0.9336
44768/60000 [=====================>........] - ETA: 21s - loss: 0.2161 - categorical_accuracy: 0.9336
44832/60000 [=====================>........] - ETA: 21s - loss: 0.2160 - categorical_accuracy: 0.9337
44896/60000 [=====================>........] - ETA: 21s - loss: 0.2158 - categorical_accuracy: 0.9337
44960/60000 [=====================>........] - ETA: 21s - loss: 0.2157 - categorical_accuracy: 0.9338
45024/60000 [=====================>........] - ETA: 21s - loss: 0.2156 - categorical_accuracy: 0.9338
45088/60000 [=====================>........] - ETA: 21s - loss: 0.2155 - categorical_accuracy: 0.9338
45152/60000 [=====================>........] - ETA: 21s - loss: 0.2154 - categorical_accuracy: 0.9339
45216/60000 [=====================>........] - ETA: 21s - loss: 0.2152 - categorical_accuracy: 0.9339
45280/60000 [=====================>........] - ETA: 21s - loss: 0.2152 - categorical_accuracy: 0.9339
45344/60000 [=====================>........] - ETA: 20s - loss: 0.2150 - categorical_accuracy: 0.9340
45408/60000 [=====================>........] - ETA: 20s - loss: 0.2149 - categorical_accuracy: 0.9340
45472/60000 [=====================>........] - ETA: 20s - loss: 0.2147 - categorical_accuracy: 0.9340
45536/60000 [=====================>........] - ETA: 20s - loss: 0.2145 - categorical_accuracy: 0.9341
45568/60000 [=====================>........] - ETA: 20s - loss: 0.2144 - categorical_accuracy: 0.9341
45632/60000 [=====================>........] - ETA: 20s - loss: 0.2142 - categorical_accuracy: 0.9342
45696/60000 [=====================>........] - ETA: 20s - loss: 0.2139 - categorical_accuracy: 0.9343
45760/60000 [=====================>........] - ETA: 20s - loss: 0.2137 - categorical_accuracy: 0.9343
45824/60000 [=====================>........] - ETA: 20s - loss: 0.2136 - categorical_accuracy: 0.9344
45888/60000 [=====================>........] - ETA: 20s - loss: 0.2134 - categorical_accuracy: 0.9344
45952/60000 [=====================>........] - ETA: 20s - loss: 0.2135 - categorical_accuracy: 0.9344
46016/60000 [======================>.......] - ETA: 19s - loss: 0.2133 - categorical_accuracy: 0.9345
46080/60000 [======================>.......] - ETA: 19s - loss: 0.2131 - categorical_accuracy: 0.9345
46144/60000 [======================>.......] - ETA: 19s - loss: 0.2128 - categorical_accuracy: 0.9346
46208/60000 [======================>.......] - ETA: 19s - loss: 0.2128 - categorical_accuracy: 0.9346
46272/60000 [======================>.......] - ETA: 19s - loss: 0.2126 - categorical_accuracy: 0.9347
46336/60000 [======================>.......] - ETA: 19s - loss: 0.2124 - categorical_accuracy: 0.9347
46400/60000 [======================>.......] - ETA: 19s - loss: 0.2122 - categorical_accuracy: 0.9348
46464/60000 [======================>.......] - ETA: 19s - loss: 0.2119 - categorical_accuracy: 0.9349
46528/60000 [======================>.......] - ETA: 19s - loss: 0.2119 - categorical_accuracy: 0.9349
46592/60000 [======================>.......] - ETA: 19s - loss: 0.2117 - categorical_accuracy: 0.9349
46656/60000 [======================>.......] - ETA: 19s - loss: 0.2116 - categorical_accuracy: 0.9350
46720/60000 [======================>.......] - ETA: 18s - loss: 0.2115 - categorical_accuracy: 0.9350
46784/60000 [======================>.......] - ETA: 18s - loss: 0.2113 - categorical_accuracy: 0.9351
46848/60000 [======================>.......] - ETA: 18s - loss: 0.2111 - categorical_accuracy: 0.9351
46912/60000 [======================>.......] - ETA: 18s - loss: 0.2109 - categorical_accuracy: 0.9352
46976/60000 [======================>.......] - ETA: 18s - loss: 0.2108 - categorical_accuracy: 0.9352
47040/60000 [======================>.......] - ETA: 18s - loss: 0.2107 - categorical_accuracy: 0.9352
47104/60000 [======================>.......] - ETA: 18s - loss: 0.2105 - categorical_accuracy: 0.9353
47168/60000 [======================>.......] - ETA: 18s - loss: 0.2105 - categorical_accuracy: 0.9353
47232/60000 [======================>.......] - ETA: 18s - loss: 0.2104 - categorical_accuracy: 0.9353
47296/60000 [======================>.......] - ETA: 18s - loss: 0.2103 - categorical_accuracy: 0.9353
47360/60000 [======================>.......] - ETA: 18s - loss: 0.2101 - categorical_accuracy: 0.9354
47424/60000 [======================>.......] - ETA: 17s - loss: 0.2099 - categorical_accuracy: 0.9355
47488/60000 [======================>.......] - ETA: 17s - loss: 0.2098 - categorical_accuracy: 0.9355
47552/60000 [======================>.......] - ETA: 17s - loss: 0.2096 - categorical_accuracy: 0.9356
47616/60000 [======================>.......] - ETA: 17s - loss: 0.2094 - categorical_accuracy: 0.9356
47680/60000 [======================>.......] - ETA: 17s - loss: 0.2096 - categorical_accuracy: 0.9356
47744/60000 [======================>.......] - ETA: 17s - loss: 0.2094 - categorical_accuracy: 0.9357
47776/60000 [======================>.......] - ETA: 17s - loss: 0.2093 - categorical_accuracy: 0.9357
47840/60000 [======================>.......] - ETA: 17s - loss: 0.2091 - categorical_accuracy: 0.9358
47904/60000 [======================>.......] - ETA: 17s - loss: 0.2091 - categorical_accuracy: 0.9358
47968/60000 [======================>.......] - ETA: 17s - loss: 0.2089 - categorical_accuracy: 0.9358
48032/60000 [=======================>......] - ETA: 17s - loss: 0.2088 - categorical_accuracy: 0.9359
48096/60000 [=======================>......] - ETA: 16s - loss: 0.2086 - categorical_accuracy: 0.9359
48160/60000 [=======================>......] - ETA: 16s - loss: 0.2085 - categorical_accuracy: 0.9360
48224/60000 [=======================>......] - ETA: 16s - loss: 0.2084 - categorical_accuracy: 0.9359
48288/60000 [=======================>......] - ETA: 16s - loss: 0.2082 - categorical_accuracy: 0.9360
48352/60000 [=======================>......] - ETA: 16s - loss: 0.2080 - categorical_accuracy: 0.9361
48416/60000 [=======================>......] - ETA: 16s - loss: 0.2078 - categorical_accuracy: 0.9361
48480/60000 [=======================>......] - ETA: 16s - loss: 0.2076 - categorical_accuracy: 0.9361
48544/60000 [=======================>......] - ETA: 16s - loss: 0.2074 - categorical_accuracy: 0.9362
48608/60000 [=======================>......] - ETA: 16s - loss: 0.2072 - categorical_accuracy: 0.9363
48672/60000 [=======================>......] - ETA: 16s - loss: 0.2070 - categorical_accuracy: 0.9363
48736/60000 [=======================>......] - ETA: 16s - loss: 0.2068 - categorical_accuracy: 0.9364
48800/60000 [=======================>......] - ETA: 15s - loss: 0.2069 - categorical_accuracy: 0.9364
48864/60000 [=======================>......] - ETA: 15s - loss: 0.2067 - categorical_accuracy: 0.9365
48928/60000 [=======================>......] - ETA: 15s - loss: 0.2065 - categorical_accuracy: 0.9365
48992/60000 [=======================>......] - ETA: 15s - loss: 0.2063 - categorical_accuracy: 0.9365
49056/60000 [=======================>......] - ETA: 15s - loss: 0.2061 - categorical_accuracy: 0.9366
49120/60000 [=======================>......] - ETA: 15s - loss: 0.2060 - categorical_accuracy: 0.9366
49184/60000 [=======================>......] - ETA: 15s - loss: 0.2059 - categorical_accuracy: 0.9367
49248/60000 [=======================>......] - ETA: 15s - loss: 0.2057 - categorical_accuracy: 0.9368
49312/60000 [=======================>......] - ETA: 15s - loss: 0.2057 - categorical_accuracy: 0.9368
49376/60000 [=======================>......] - ETA: 15s - loss: 0.2056 - categorical_accuracy: 0.9368
49440/60000 [=======================>......] - ETA: 15s - loss: 0.2056 - categorical_accuracy: 0.9368
49504/60000 [=======================>......] - ETA: 14s - loss: 0.2054 - categorical_accuracy: 0.9369
49568/60000 [=======================>......] - ETA: 14s - loss: 0.2052 - categorical_accuracy: 0.9369
49632/60000 [=======================>......] - ETA: 14s - loss: 0.2051 - categorical_accuracy: 0.9369
49696/60000 [=======================>......] - ETA: 14s - loss: 0.2050 - categorical_accuracy: 0.9370
49760/60000 [=======================>......] - ETA: 14s - loss: 0.2049 - categorical_accuracy: 0.9370
49824/60000 [=======================>......] - ETA: 14s - loss: 0.2048 - categorical_accuracy: 0.9371
49888/60000 [=======================>......] - ETA: 14s - loss: 0.2047 - categorical_accuracy: 0.9371
49920/60000 [=======================>......] - ETA: 14s - loss: 0.2046 - categorical_accuracy: 0.9372
49984/60000 [=======================>......] - ETA: 14s - loss: 0.2047 - categorical_accuracy: 0.9371
50048/60000 [========================>.....] - ETA: 14s - loss: 0.2046 - categorical_accuracy: 0.9372
50112/60000 [========================>.....] - ETA: 14s - loss: 0.2046 - categorical_accuracy: 0.9372
50176/60000 [========================>.....] - ETA: 14s - loss: 0.2044 - categorical_accuracy: 0.9372
50208/60000 [========================>.....] - ETA: 13s - loss: 0.2043 - categorical_accuracy: 0.9372
50272/60000 [========================>.....] - ETA: 13s - loss: 0.2041 - categorical_accuracy: 0.9373
50336/60000 [========================>.....] - ETA: 13s - loss: 0.2040 - categorical_accuracy: 0.9374
50400/60000 [========================>.....] - ETA: 13s - loss: 0.2039 - categorical_accuracy: 0.9374
50464/60000 [========================>.....] - ETA: 13s - loss: 0.2037 - categorical_accuracy: 0.9375
50528/60000 [========================>.....] - ETA: 13s - loss: 0.2037 - categorical_accuracy: 0.9375
50592/60000 [========================>.....] - ETA: 13s - loss: 0.2035 - categorical_accuracy: 0.9376
50656/60000 [========================>.....] - ETA: 13s - loss: 0.2034 - categorical_accuracy: 0.9376
50720/60000 [========================>.....] - ETA: 13s - loss: 0.2033 - categorical_accuracy: 0.9377
50784/60000 [========================>.....] - ETA: 13s - loss: 0.2033 - categorical_accuracy: 0.9377
50816/60000 [========================>.....] - ETA: 13s - loss: 0.2032 - categorical_accuracy: 0.9377
50880/60000 [========================>.....] - ETA: 13s - loss: 0.2030 - categorical_accuracy: 0.9378
50944/60000 [========================>.....] - ETA: 12s - loss: 0.2030 - categorical_accuracy: 0.9378
51008/60000 [========================>.....] - ETA: 12s - loss: 0.2028 - categorical_accuracy: 0.9378
51072/60000 [========================>.....] - ETA: 12s - loss: 0.2027 - categorical_accuracy: 0.9379
51136/60000 [========================>.....] - ETA: 12s - loss: 0.2026 - categorical_accuracy: 0.9379
51200/60000 [========================>.....] - ETA: 12s - loss: 0.2024 - categorical_accuracy: 0.9379
51264/60000 [========================>.....] - ETA: 12s - loss: 0.2024 - categorical_accuracy: 0.9379
51328/60000 [========================>.....] - ETA: 12s - loss: 0.2022 - categorical_accuracy: 0.9380
51392/60000 [========================>.....] - ETA: 12s - loss: 0.2021 - categorical_accuracy: 0.9380
51456/60000 [========================>.....] - ETA: 12s - loss: 0.2020 - categorical_accuracy: 0.9381
51520/60000 [========================>.....] - ETA: 12s - loss: 0.2018 - categorical_accuracy: 0.9381
51584/60000 [========================>.....] - ETA: 12s - loss: 0.2017 - categorical_accuracy: 0.9381
51648/60000 [========================>.....] - ETA: 11s - loss: 0.2016 - categorical_accuracy: 0.9382
51712/60000 [========================>.....] - ETA: 11s - loss: 0.2015 - categorical_accuracy: 0.9382
51776/60000 [========================>.....] - ETA: 11s - loss: 0.2014 - categorical_accuracy: 0.9382
51840/60000 [========================>.....] - ETA: 11s - loss: 0.2013 - categorical_accuracy: 0.9382
51904/60000 [========================>.....] - ETA: 11s - loss: 0.2011 - categorical_accuracy: 0.9383
51968/60000 [========================>.....] - ETA: 11s - loss: 0.2009 - categorical_accuracy: 0.9383
52032/60000 [=========================>....] - ETA: 11s - loss: 0.2008 - categorical_accuracy: 0.9383
52064/60000 [=========================>....] - ETA: 11s - loss: 0.2007 - categorical_accuracy: 0.9384
52096/60000 [=========================>....] - ETA: 11s - loss: 0.2007 - categorical_accuracy: 0.9384
52160/60000 [=========================>....] - ETA: 11s - loss: 0.2006 - categorical_accuracy: 0.9384
52224/60000 [=========================>....] - ETA: 11s - loss: 0.2004 - categorical_accuracy: 0.9385
52288/60000 [=========================>....] - ETA: 11s - loss: 0.2002 - categorical_accuracy: 0.9386
52352/60000 [=========================>....] - ETA: 10s - loss: 0.2000 - categorical_accuracy: 0.9386
52416/60000 [=========================>....] - ETA: 10s - loss: 0.2000 - categorical_accuracy: 0.9386
52480/60000 [=========================>....] - ETA: 10s - loss: 0.1998 - categorical_accuracy: 0.9387
52512/60000 [=========================>....] - ETA: 10s - loss: 0.1997 - categorical_accuracy: 0.9387
52576/60000 [=========================>....] - ETA: 10s - loss: 0.1995 - categorical_accuracy: 0.9388
52640/60000 [=========================>....] - ETA: 10s - loss: 0.1994 - categorical_accuracy: 0.9388
52704/60000 [=========================>....] - ETA: 10s - loss: 0.1992 - categorical_accuracy: 0.9389
52768/60000 [=========================>....] - ETA: 10s - loss: 0.1992 - categorical_accuracy: 0.9389
52800/60000 [=========================>....] - ETA: 10s - loss: 0.1992 - categorical_accuracy: 0.9389
52864/60000 [=========================>....] - ETA: 10s - loss: 0.1990 - categorical_accuracy: 0.9389
52928/60000 [=========================>....] - ETA: 10s - loss: 0.1990 - categorical_accuracy: 0.9389
52992/60000 [=========================>....] - ETA: 9s - loss: 0.1988 - categorical_accuracy: 0.9390 
53024/60000 [=========================>....] - ETA: 9s - loss: 0.1989 - categorical_accuracy: 0.9390
53088/60000 [=========================>....] - ETA: 9s - loss: 0.1988 - categorical_accuracy: 0.9390
53152/60000 [=========================>....] - ETA: 9s - loss: 0.1987 - categorical_accuracy: 0.9390
53216/60000 [=========================>....] - ETA: 9s - loss: 0.1987 - categorical_accuracy: 0.9390
53248/60000 [=========================>....] - ETA: 9s - loss: 0.1986 - categorical_accuracy: 0.9391
53312/60000 [=========================>....] - ETA: 9s - loss: 0.1985 - categorical_accuracy: 0.9391
53376/60000 [=========================>....] - ETA: 9s - loss: 0.1984 - categorical_accuracy: 0.9391
53440/60000 [=========================>....] - ETA: 9s - loss: 0.1982 - categorical_accuracy: 0.9392
53504/60000 [=========================>....] - ETA: 9s - loss: 0.1981 - categorical_accuracy: 0.9393
53536/60000 [=========================>....] - ETA: 9s - loss: 0.1981 - categorical_accuracy: 0.9393
53600/60000 [=========================>....] - ETA: 9s - loss: 0.1980 - categorical_accuracy: 0.9393
53664/60000 [=========================>....] - ETA: 9s - loss: 0.1978 - categorical_accuracy: 0.9394
53728/60000 [=========================>....] - ETA: 8s - loss: 0.1977 - categorical_accuracy: 0.9394
53792/60000 [=========================>....] - ETA: 8s - loss: 0.1975 - categorical_accuracy: 0.9395
53856/60000 [=========================>....] - ETA: 8s - loss: 0.1973 - categorical_accuracy: 0.9396
53920/60000 [=========================>....] - ETA: 8s - loss: 0.1973 - categorical_accuracy: 0.9396
53984/60000 [=========================>....] - ETA: 8s - loss: 0.1971 - categorical_accuracy: 0.9396
54048/60000 [==========================>...] - ETA: 8s - loss: 0.1970 - categorical_accuracy: 0.9397
54112/60000 [==========================>...] - ETA: 8s - loss: 0.1970 - categorical_accuracy: 0.9397
54176/60000 [==========================>...] - ETA: 8s - loss: 0.1969 - categorical_accuracy: 0.9397
54240/60000 [==========================>...] - ETA: 8s - loss: 0.1967 - categorical_accuracy: 0.9398
54304/60000 [==========================>...] - ETA: 8s - loss: 0.1967 - categorical_accuracy: 0.9398
54368/60000 [==========================>...] - ETA: 8s - loss: 0.1967 - categorical_accuracy: 0.9398
54432/60000 [==========================>...] - ETA: 7s - loss: 0.1965 - categorical_accuracy: 0.9398
54464/60000 [==========================>...] - ETA: 7s - loss: 0.1965 - categorical_accuracy: 0.9399
54528/60000 [==========================>...] - ETA: 7s - loss: 0.1964 - categorical_accuracy: 0.9399
54592/60000 [==========================>...] - ETA: 7s - loss: 0.1962 - categorical_accuracy: 0.9399
54656/60000 [==========================>...] - ETA: 7s - loss: 0.1960 - categorical_accuracy: 0.9400
54720/60000 [==========================>...] - ETA: 7s - loss: 0.1959 - categorical_accuracy: 0.9400
54784/60000 [==========================>...] - ETA: 7s - loss: 0.1957 - categorical_accuracy: 0.9401
54848/60000 [==========================>...] - ETA: 7s - loss: 0.1956 - categorical_accuracy: 0.9401
54912/60000 [==========================>...] - ETA: 7s - loss: 0.1955 - categorical_accuracy: 0.9402
54976/60000 [==========================>...] - ETA: 7s - loss: 0.1953 - categorical_accuracy: 0.9403
55040/60000 [==========================>...] - ETA: 7s - loss: 0.1951 - categorical_accuracy: 0.9403
55104/60000 [==========================>...] - ETA: 6s - loss: 0.1950 - categorical_accuracy: 0.9403
55168/60000 [==========================>...] - ETA: 6s - loss: 0.1948 - categorical_accuracy: 0.9404
55232/60000 [==========================>...] - ETA: 6s - loss: 0.1946 - categorical_accuracy: 0.9405
55296/60000 [==========================>...] - ETA: 6s - loss: 0.1944 - categorical_accuracy: 0.9405
55360/60000 [==========================>...] - ETA: 6s - loss: 0.1943 - categorical_accuracy: 0.9406
55424/60000 [==========================>...] - ETA: 6s - loss: 0.1942 - categorical_accuracy: 0.9406
55488/60000 [==========================>...] - ETA: 6s - loss: 0.1940 - categorical_accuracy: 0.9407
55520/60000 [==========================>...] - ETA: 6s - loss: 0.1941 - categorical_accuracy: 0.9406
55584/60000 [==========================>...] - ETA: 6s - loss: 0.1939 - categorical_accuracy: 0.9407
55648/60000 [==========================>...] - ETA: 6s - loss: 0.1940 - categorical_accuracy: 0.9407
55712/60000 [==========================>...] - ETA: 6s - loss: 0.1939 - categorical_accuracy: 0.9407
55776/60000 [==========================>...] - ETA: 6s - loss: 0.1938 - categorical_accuracy: 0.9407
55840/60000 [==========================>...] - ETA: 5s - loss: 0.1936 - categorical_accuracy: 0.9408
55904/60000 [==========================>...] - ETA: 5s - loss: 0.1935 - categorical_accuracy: 0.9408
55968/60000 [==========================>...] - ETA: 5s - loss: 0.1933 - categorical_accuracy: 0.9409
56032/60000 [===========================>..] - ETA: 5s - loss: 0.1933 - categorical_accuracy: 0.9409
56096/60000 [===========================>..] - ETA: 5s - loss: 0.1933 - categorical_accuracy: 0.9410
56160/60000 [===========================>..] - ETA: 5s - loss: 0.1932 - categorical_accuracy: 0.9410
56224/60000 [===========================>..] - ETA: 5s - loss: 0.1930 - categorical_accuracy: 0.9411
56288/60000 [===========================>..] - ETA: 5s - loss: 0.1928 - categorical_accuracy: 0.9411
56352/60000 [===========================>..] - ETA: 5s - loss: 0.1926 - categorical_accuracy: 0.9412
56416/60000 [===========================>..] - ETA: 5s - loss: 0.1925 - categorical_accuracy: 0.9412
56480/60000 [===========================>..] - ETA: 5s - loss: 0.1924 - categorical_accuracy: 0.9413
56544/60000 [===========================>..] - ETA: 4s - loss: 0.1922 - categorical_accuracy: 0.9413
56608/60000 [===========================>..] - ETA: 4s - loss: 0.1921 - categorical_accuracy: 0.9413
56672/60000 [===========================>..] - ETA: 4s - loss: 0.1922 - categorical_accuracy: 0.9413
56736/60000 [===========================>..] - ETA: 4s - loss: 0.1922 - categorical_accuracy: 0.9413
56800/60000 [===========================>..] - ETA: 4s - loss: 0.1921 - categorical_accuracy: 0.9414
56864/60000 [===========================>..] - ETA: 4s - loss: 0.1919 - categorical_accuracy: 0.9414
56928/60000 [===========================>..] - ETA: 4s - loss: 0.1918 - categorical_accuracy: 0.9414
56992/60000 [===========================>..] - ETA: 4s - loss: 0.1916 - categorical_accuracy: 0.9415
57056/60000 [===========================>..] - ETA: 4s - loss: 0.1915 - categorical_accuracy: 0.9415
57088/60000 [===========================>..] - ETA: 4s - loss: 0.1914 - categorical_accuracy: 0.9415
57152/60000 [===========================>..] - ETA: 4s - loss: 0.1912 - categorical_accuracy: 0.9415
57216/60000 [===========================>..] - ETA: 3s - loss: 0.1911 - categorical_accuracy: 0.9416
57280/60000 [===========================>..] - ETA: 3s - loss: 0.1909 - categorical_accuracy: 0.9416
57344/60000 [===========================>..] - ETA: 3s - loss: 0.1907 - categorical_accuracy: 0.9417
57408/60000 [===========================>..] - ETA: 3s - loss: 0.1906 - categorical_accuracy: 0.9417
57472/60000 [===========================>..] - ETA: 3s - loss: 0.1905 - categorical_accuracy: 0.9417
57536/60000 [===========================>..] - ETA: 3s - loss: 0.1903 - categorical_accuracy: 0.9417
57600/60000 [===========================>..] - ETA: 3s - loss: 0.1901 - categorical_accuracy: 0.9418
57664/60000 [===========================>..] - ETA: 3s - loss: 0.1902 - categorical_accuracy: 0.9418
57728/60000 [===========================>..] - ETA: 3s - loss: 0.1900 - categorical_accuracy: 0.9419
57792/60000 [===========================>..] - ETA: 3s - loss: 0.1900 - categorical_accuracy: 0.9419
57856/60000 [===========================>..] - ETA: 3s - loss: 0.1898 - categorical_accuracy: 0.9420
57920/60000 [===========================>..] - ETA: 2s - loss: 0.1896 - categorical_accuracy: 0.9420
57984/60000 [===========================>..] - ETA: 2s - loss: 0.1895 - categorical_accuracy: 0.9421
58048/60000 [============================>.] - ETA: 2s - loss: 0.1894 - categorical_accuracy: 0.9421
58112/60000 [============================>.] - ETA: 2s - loss: 0.1893 - categorical_accuracy: 0.9421
58176/60000 [============================>.] - ETA: 2s - loss: 0.1892 - categorical_accuracy: 0.9422
58240/60000 [============================>.] - ETA: 2s - loss: 0.1891 - categorical_accuracy: 0.9422
58304/60000 [============================>.] - ETA: 2s - loss: 0.1891 - categorical_accuracy: 0.9422
58368/60000 [============================>.] - ETA: 2s - loss: 0.1890 - categorical_accuracy: 0.9422
58432/60000 [============================>.] - ETA: 2s - loss: 0.1888 - categorical_accuracy: 0.9423
58496/60000 [============================>.] - ETA: 2s - loss: 0.1888 - categorical_accuracy: 0.9423
58560/60000 [============================>.] - ETA: 2s - loss: 0.1888 - categorical_accuracy: 0.9423
58624/60000 [============================>.] - ETA: 1s - loss: 0.1886 - categorical_accuracy: 0.9423
58656/60000 [============================>.] - ETA: 1s - loss: 0.1885 - categorical_accuracy: 0.9423
58720/60000 [============================>.] - ETA: 1s - loss: 0.1884 - categorical_accuracy: 0.9424
58784/60000 [============================>.] - ETA: 1s - loss: 0.1882 - categorical_accuracy: 0.9425
58848/60000 [============================>.] - ETA: 1s - loss: 0.1884 - categorical_accuracy: 0.9425
58912/60000 [============================>.] - ETA: 1s - loss: 0.1882 - categorical_accuracy: 0.9425
58976/60000 [============================>.] - ETA: 1s - loss: 0.1881 - categorical_accuracy: 0.9425
59040/60000 [============================>.] - ETA: 1s - loss: 0.1881 - categorical_accuracy: 0.9425
59104/60000 [============================>.] - ETA: 1s - loss: 0.1880 - categorical_accuracy: 0.9426
59168/60000 [============================>.] - ETA: 1s - loss: 0.1878 - categorical_accuracy: 0.9426
59232/60000 [============================>.] - ETA: 1s - loss: 0.1877 - categorical_accuracy: 0.9426
59296/60000 [============================>.] - ETA: 1s - loss: 0.1875 - categorical_accuracy: 0.9427
59360/60000 [============================>.] - ETA: 0s - loss: 0.1875 - categorical_accuracy: 0.9427
59424/60000 [============================>.] - ETA: 0s - loss: 0.1875 - categorical_accuracy: 0.9427
59488/60000 [============================>.] - ETA: 0s - loss: 0.1874 - categorical_accuracy: 0.9427
59552/60000 [============================>.] - ETA: 0s - loss: 0.1873 - categorical_accuracy: 0.9428
59616/60000 [============================>.] - ETA: 0s - loss: 0.1874 - categorical_accuracy: 0.9427
59680/60000 [============================>.] - ETA: 0s - loss: 0.1873 - categorical_accuracy: 0.9428
59744/60000 [============================>.] - ETA: 0s - loss: 0.1871 - categorical_accuracy: 0.9428
59808/60000 [============================>.] - ETA: 0s - loss: 0.1872 - categorical_accuracy: 0.9428
59872/60000 [============================>.] - ETA: 0s - loss: 0.1870 - categorical_accuracy: 0.9429
59936/60000 [============================>.] - ETA: 0s - loss: 0.1871 - categorical_accuracy: 0.9429
60000/60000 [==============================] - 88s 1ms/step - loss: 0.1870 - categorical_accuracy: 0.9429 - val_loss: 0.0460 - val_categorical_accuracy: 0.9855

  ('#### Predict   ####################################################',) 

  ('#### Path params   ################################################',) 

  ('/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/', '/home/runner/work/mlmodels/mlmodels/keras_deepAR/') 

   32/10000 [..............................] - ETA: 15s
  224/10000 [..............................] - ETA: 4s 
  416/10000 [>.............................] - ETA: 3s
  608/10000 [>.............................] - ETA: 3s
  800/10000 [=>............................] - ETA: 2s
  992/10000 [=>............................] - ETA: 2s
 1216/10000 [==>...........................] - ETA: 2s
 1408/10000 [===>..........................] - ETA: 2s
 1600/10000 [===>..........................] - ETA: 2s
 1792/10000 [====>.........................] - ETA: 2s
 2016/10000 [=====>........................] - ETA: 2s
 2240/10000 [=====>........................] - ETA: 2s
 2464/10000 [======>.......................] - ETA: 2s
 2656/10000 [======>.......................] - ETA: 2s
 2880/10000 [=======>......................] - ETA: 1s
 3040/10000 [========>.....................] - ETA: 1s
 3232/10000 [========>.....................] - ETA: 1s
 3456/10000 [=========>....................] - ETA: 1s
 3648/10000 [=========>....................] - ETA: 1s
 3872/10000 [==========>...................] - ETA: 1s
 4096/10000 [===========>..................] - ETA: 1s
 4288/10000 [===========>..................] - ETA: 1s
 4512/10000 [============>.................] - ETA: 1s
 4704/10000 [=============>................] - ETA: 1s
 4896/10000 [=============>................] - ETA: 1s
 5120/10000 [==============>...............] - ETA: 1s
 5312/10000 [==============>...............] - ETA: 1s
 5504/10000 [===============>..............] - ETA: 1s
 5728/10000 [================>.............] - ETA: 1s
 5952/10000 [================>.............] - ETA: 1s
 6176/10000 [=================>............] - ETA: 1s
 6400/10000 [==================>...........] - ETA: 0s
 6624/10000 [==================>...........] - ETA: 0s
 6816/10000 [===================>..........] - ETA: 0s
 7040/10000 [====================>.........] - ETA: 0s
 7264/10000 [====================>.........] - ETA: 0s
 7488/10000 [=====================>........] - ETA: 0s
 7680/10000 [======================>.......] - ETA: 0s
 7904/10000 [======================>.......] - ETA: 0s
 8096/10000 [=======================>......] - ETA: 0s
 8320/10000 [=======================>......] - ETA: 0s
 8512/10000 [========================>.....] - ETA: 0s
 8704/10000 [=========================>....] - ETA: 0s
 8864/10000 [=========================>....] - ETA: 0s
 9056/10000 [==========================>...] - ETA: 0s
 9280/10000 [==========================>...] - ETA: 0s
 9472/10000 [===========================>..] - ETA: 0s
 9664/10000 [===========================>..] - ETA: 0s
 9856/10000 [============================>.] - ETA: 0s
10000/10000 [==============================] - 3s 268us/step
[[3.72793096e-07 1.46648873e-07 4.96977627e-05 ... 9.99934196e-01
  1.23368551e-07 5.76113598e-06]
 [9.01602980e-05 2.62232468e-04 9.99602973e-01 ... 6.41931521e-08
  9.07620779e-06 3.34813031e-08]
 [3.53657629e-06 9.99428451e-01 8.57460182e-05 ... 2.19607784e-04
  4.15839713e-05 6.00686690e-06]
 ...
 [1.21603236e-07 3.40710676e-06 2.44576892e-08 ... 1.71965130e-05
  1.02838139e-05 4.93204752e-05]
 [2.52136033e-06 1.01671205e-07 6.06900414e-08 ... 4.12359043e-07
  3.49599007e-03 1.44508886e-05]
 [1.15881521e-05 2.21987960e-07 2.92676432e-05 ... 2.60081112e-08
  2.70372493e-06 3.10412673e-07]]

  ('#### metrics   ####################################################',) 

  ('#### Path params   ################################################',) 

  ('/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/', '/home/runner/work/mlmodels/mlmodels/keras_deepAR/') 
{'loss_test:': 0.04596794061735272, 'accuracy_test:': 0.9854999780654907}

  ('#### Save   #######################################################',) 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/charcnn/result'}

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Warning: Permanently added the RSA host key for IP address '140.82.118.3' to the list of known hosts.
From github.com:arita37/mlmodels_store
   4b31bc3..b6c237a  master     -> origin/master
Updating 4b31bc3..b6c237a
Fast-forward
 .../20200519/list_log_pullrequest_20200519.md      |   2 +-
 error_list/20200519/list_log_testall_20200519.md   | 433 +++++++++++++++++++++
 2 files changed, 434 insertions(+), 1 deletion(-)
[master 5a9b667] ml_store
 1 file changed, 1124 insertions(+)
To github.com:arita37/mlmodels_store.git
   b6c237a..5a9b667  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//1_lstm.py 
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/compat/v2_compat.py:68: disable_resource_variables (from tensorflow.python.ops.variable_scope) is deprecated and will be removed in a future version.
Instructions for updating:
non-resource variables are not supported in the long term
start

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
{'loss': 0.36453530192375183, 'loss_history': []}

  #### Plot   ######################################################## 

  #### Save   ######################################################## 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/'}
Model saved in path: /home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm//model//model.ckpt

  #### Load   ######################################################## 
2020-05-19 04:27:36.649407: W tensorflow/core/framework/op_kernel.cc:1651] OP_REQUIRES failed at save_restore_v2_ops.cc:184 : Not found: Key Variable not found in checkpoint
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/', 'model_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/model'}
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/client/session.py", line 1365, in _do_call
    return fn(*args)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/client/session.py", line 1350, in _run_fn
    target_list, run_metadata)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/client/session.py", line 1443, in _call_tf_sessionrun
    run_metadata)
tensorflow.python.framework.errors_impl.NotFoundError: Key Variable not found in checkpoint
	 [[{{node save_1/RestoreV2}}]]

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 1290, in restore
    {self.saver_def.filename_tensor_name: save_path})
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/client/session.py", line 956, in run
    run_metadata_ptr)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/client/session.py", line 1180, in _run
    feed_dict_tensor, options, run_metadata)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/client/session.py", line 1359, in _do_run
    run_metadata)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/client/session.py", line 1384, in _do_call
    raise type(e)(node_def, op, message)
tensorflow.python.framework.errors_impl.NotFoundError: Key Variable not found in checkpoint
	 [[node save_1/RestoreV2 (defined at opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/framework/ops.py:1748) ]]

Original stack trace for 'save_1/RestoreV2':
  File "home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//1_lstm.py", line 332, in <module>
    test(data_path="", pars_choice="test01", config_mode="test")
  File "home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//1_lstm.py", line 320, in test
    session = load(out_pars)
  File "home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//1_lstm.py", line 199, in load
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


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 1300, in restore
    names_to_keys = object_graph_key_mapping(save_path)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 1618, in object_graph_key_mapping
    object_graph_string = reader.get_tensor(trackable.OBJECT_GRAPH_PROTO_KEY)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/pywrap_tensorflow_internal.py", line 915, in get_tensor
    return CheckpointReader_GetTensor(self, compat.as_bytes(tensor_str))
tensorflow.python.framework.errors_impl.NotFoundError: Key _CHECKPOINTABLE_OBJECT_GRAPH not found in checkpoint

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//1_lstm.py", line 332, in <module>
    test(data_path="", pars_choice="test01", config_mode="test")
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//1_lstm.py", line 320, in test
    session = load(out_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//1_lstm.py", line 199, in load
    return load_tf(load_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/util.py", line 477, in load_tf
    saver.restore(sess,  full_name)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/training/saver.py", line 1306, in restore
    err, "a Variable name or other graph key that is missing")
tensorflow.python.framework.errors_impl.NotFoundError: Restoring from checkpoint failed. This is most likely due to a Variable name or other graph key that is missing from the checkpoint. Please ensure that you have not altered the graph expected based on the checkpoint. Original error:

Key Variable not found in checkpoint
	 [[node save_1/RestoreV2 (defined at opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/framework/ops.py:1748) ]]

Original stack trace for 'save_1/RestoreV2':
  File "home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//1_lstm.py", line 332, in <module>
    test(data_path="", pars_choice="test01", config_mode="test")
  File "home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//1_lstm.py", line 320, in test
    session = load(out_pars)
  File "home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//1_lstm.py", line 199, in load
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


   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Already up to date.
[master be43684] ml_store
 1 file changed, 234 insertions(+)
To github.com:arita37/mlmodels_store.git
   5a9b667..be43684  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//temporal_fusion_google.py 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//temporal_fusion_google.py", line 17, in <module>
    from mlmodels.mode_tf.raw  import temporal_fusion_google
ModuleNotFoundError: No module named 'mlmodels.mode_tf'

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Already up to date.
[master 82fb86a] ml_store
 1 file changed, 36 insertions(+)
To github.com:arita37/mlmodels_store.git
   be43684..82fb86a  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon//gluon_automl.py 

  #### Loading params   ############################################## 

  #### Model params   ################################################ 

  #### Loading dataset   ############################################# 
/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/mxnet/optimizer/optimizer.py:167: UserWarning: WARNING: New optimizer gluonnlp.optimizer.lamb.LAMB is overriding existing optimizer mxnet.optimizer.optimizer.LAMB
  Optimizer.opt_registry[name].__name__))
Loaded data from: https://autogluon.s3.amazonaws.com/datasets/Inc/train.csv | Columns = 15 / 15 | Rows = 39073 -> 39073

  #### Model init, fit   ############################################# 
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
	Data preprocessing and feature engineering runtime = 0.24s ...
AutoGluon will gauge predictive performance using evaluation metric: accuracy
To change this, specify the eval_metric argument of fit()
AutoGluon will early stop models using evaluation metric: accuracy
Saving dataset/learner.pkl
Beginning hyperparameter tuning for Gradient Boosting Model...
Hyperparameter search space for Gradient Boosting Model: 
num_leaves:   Int: lower=26, upper=66
learning_rate:   Real: lower=0.005, upper=0.2
feature_fraction:   Real: lower=0.75, upper=1.0
min_data_in_leaf:   Int: lower=2, upper=30
Starting Experiments
Num of Finished Tasks is 0
Num of Pending Tasks is 5
  0%|          | 0/5 [00:00<?, ?it/s]Saving dataset/models/LightGBMClassifier/trial_0_model.pkl
Finished Task with config: {'feature_fraction': 1.0, 'learning_rate': 0.1, 'min_data_in_leaf': 20, 'num_leaves': 36} and reward: 0.3908
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xf0\x00\x00\x00\x00\x00\x00X\r\x00\x00\x00learning_rateq\x02G?\xb9\x99\x99\x99\x99\x99\x9aX\x10\x00\x00\x00min_data_in_leafq\x03K\x14X\n\x00\x00\x00num_leavesq\x04K$u.' and reward: 0.3908
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xf0\x00\x00\x00\x00\x00\x00X\r\x00\x00\x00learning_rateq\x02G?\xb9\x99\x99\x99\x99\x99\x9aX\x10\x00\x00\x00min_data_in_leafq\x03K\x14X\n\x00\x00\x00num_leavesq\x04K$u.' and reward: 0.3908
 40%|████      | 2/5 [00:19<00:29,  9.79s/it]Saving dataset/models/LightGBMClassifier/trial_1_model.pkl
Finished Task with config: {'feature_fraction': 0.7593474074847443, 'learning_rate': 0.018087534034883872, 'min_data_in_leaf': 21, 'num_leaves': 52} and reward: 0.3918
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xe8L\x92\xef.a-X\r\x00\x00\x00learning_rateq\x02G?\x92\x85\x89\xdc\x94\x98\x8bX\x10\x00\x00\x00min_data_in_leafq\x03K\x15X\n\x00\x00\x00num_leavesq\x04K4u.' and reward: 0.3918
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xe8L\x92\xef.a-X\r\x00\x00\x00learning_rateq\x02G?\x92\x85\x89\xdc\x94\x98\x8bX\x10\x00\x00\x00min_data_in_leafq\x03K\x15X\n\x00\x00\x00num_leavesq\x04K4u.' and reward: 0.3918
 60%|██████    | 3/5 [00:44<00:28, 14.34s/it]Saving dataset/models/LightGBMClassifier/trial_2_model.pkl
Finished Task with config: {'feature_fraction': 0.7960892281707374, 'learning_rate': 0.014906537036763336, 'min_data_in_leaf': 27, 'num_leaves': 47} and reward: 0.3902
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xe9y\x90\x1d\xf6\x1eMX\r\x00\x00\x00learning_rateq\x02G?\x8e\x87Q\x88\x8e[\xeeX\x10\x00\x00\x00min_data_in_leafq\x03K\x1bX\n\x00\x00\x00num_leavesq\x04K/u.' and reward: 0.3902
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xe9y\x90\x1d\xf6\x1eMX\r\x00\x00\x00learning_rateq\x02G?\x8e\x87Q\x88\x8e[\xeeX\x10\x00\x00\x00min_data_in_leafq\x03K\x1bX\n\x00\x00\x00num_leavesq\x04K/u.' and reward: 0.3902
 80%|████████  | 4/5 [01:08<00:17, 17.11s/it] 80%|████████  | 4/5 [01:08<00:17, 17.03s/it]
Saving dataset/models/LightGBMClassifier/trial_3_model.pkl
Finished Task with config: {'feature_fraction': 0.9578723302475229, 'learning_rate': 0.0706139993031698, 'min_data_in_leaf': 15, 'num_leaves': 63} and reward: 0.3924
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xee\xa6\xe3\xdf\x85\x01jX\r\x00\x00\x00learning_rateq\x02G?\xb2\x13\xc2Q\xa5\x9a\x00X\x10\x00\x00\x00min_data_in_leafq\x03K\x0fX\n\x00\x00\x00num_leavesq\x04K?u.' and reward: 0.3924
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xee\xa6\xe3\xdf\x85\x01jX\r\x00\x00\x00learning_rateq\x02G?\xb2\x13\xc2Q\xa5\x9a\x00X\x10\x00\x00\x00min_data_in_leafq\x03K\x0fX\n\x00\x00\x00num_leavesq\x04K?u.' and reward: 0.3924
Time for Gradient Boosting hyperparameter optimization: 96.87262964248657
Best hyperparameter configuration for Gradient Boosting Model: 
{'feature_fraction': 0.9578723302475229, 'learning_rate': 0.0706139993031698, 'min_data_in_leaf': 15, 'num_leaves': 63}
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
Saving dataset/models/NeuralNetClassifier/trial_4_tabularNN.pkl
Finished Task with config: {'activation.choice': 0, 'dropout_prob': 0.1, 'embedding_size_factor': 1.0, 'layers.choice': 0, 'learning_rate': 0.0005, 'network_type.choice': 0, 'use_batchnorm.choice': 0, 'weight_decay': 1e-06} and reward: 0.3894
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\xb9\x99\x99\x99\x99\x99\x9aX\x15\x00\x00\x00embedding_size_factorq\x03G?\xf0\x00\x00\x00\x00\x00\x00X\r\x00\x00\x00layers.choiceq\x04K\x00X\r\x00\x00\x00learning_rateq\x05G?@bM\xd2\xf1\xa9\xfcX\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G>\xb0\xc6\xf7\xa0\xb5\xed\x8du.' and reward: 0.3894
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\xb9\x99\x99\x99\x99\x99\x9aX\x15\x00\x00\x00embedding_size_factorq\x03G?\xf0\x00\x00\x00\x00\x00\x00X\r\x00\x00\x00layers.choiceq\x04K\x00X\r\x00\x00\x00learning_rateq\x05G?@bM\xd2\xf1\xa9\xfcX\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G>\xb0\xc6\xf7\xa0\xb5\xed\x8du.' and reward: 0.3894
 40%|████      | 2/5 [00:51<01:16, 25.57s/it]Loading: dataset/models/NeuralNetClassifier/train_tabNNdataset.pkl
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
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
Saving dataset/models/NeuralNetClassifier/trial_5_tabularNN.pkl
Finished Task with config: {'activation.choice': 1, 'dropout_prob': 0.11840655310961021, 'embedding_size_factor': 0.7765537906409312, 'layers.choice': 1, 'learning_rate': 0.005318263549581816, 'network_type.choice': 1, 'use_batchnorm.choice': 1, 'weight_decay': 3.727394694266211e-12} and reward: 0.3774
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x01X\x0c\x00\x00\x00dropout_probq\x02G?\xbeO\xe4Q<\xe4\x96X\x15\x00\x00\x00embedding_size_factorq\x03G?\xe8\xd9\x87U\xccgxX\r\x00\x00\x00layers.choiceq\x04K\x01X\r\x00\x00\x00learning_rateq\x05G?u\xc8\x9a\x80Ez\xc2X\x13\x00\x00\x00network_type.choiceq\x06K\x01X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x01X\x0c\x00\x00\x00weight_decayq\x08G=\x90d\xac_\xf2\x83\xffu.' and reward: 0.3774
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x01X\x0c\x00\x00\x00dropout_probq\x02G?\xbeO\xe4Q<\xe4\x96X\x15\x00\x00\x00embedding_size_factorq\x03G?\xe8\xd9\x87U\xccgxX\r\x00\x00\x00layers.choiceq\x04K\x01X\r\x00\x00\x00learning_rateq\x05G?u\xc8\x9a\x80Ez\xc2X\x13\x00\x00\x00network_type.choiceq\x06K\x01X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x01X\x0c\x00\x00\x00weight_decayq\x08G=\x90d\xac_\xf2\x83\xffu.' and reward: 0.3774
 60%|██████    | 3/5 [02:23<01:31, 45.54s/it] 60%|██████    | 3/5 [02:23<01:35, 47.75s/it]
Loading: dataset/models/NeuralNetClassifier/train_tabNNdataset.pkl
Loading: dataset/models/NeuralNetClassifier/validation_tabNNdataset.pkl
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
Saving dataset/models/NeuralNetClassifier/trial_6_tabularNN.pkl
Finished Task with config: {'activation.choice': 2, 'dropout_prob': 0.09027041547300176, 'embedding_size_factor': 0.8394031223840865, 'layers.choice': 2, 'learning_rate': 0.0024960082713257935, 'network_type.choice': 1, 'use_batchnorm.choice': 0, 'weight_decay': 2.6561649676218885e-12} and reward: 0.39
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x02X\x0c\x00\x00\x00dropout_probq\x02G?\xb7\x1b\xf6B@\xbciX\x15\x00\x00\x00embedding_size_factorq\x03G?\xea\xdcc\xef\xd9\x99\x16X\r\x00\x00\x00layers.choiceq\x04K\x02X\r\x00\x00\x00learning_rateq\x05G?dr\x82<\xab!\nX\x13\x00\x00\x00network_type.choiceq\x06K\x01X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G=\x87]&\xdb\x00\x8f\xa7u.' and reward: 0.39
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x02X\x0c\x00\x00\x00dropout_probq\x02G?\xb7\x1b\xf6B@\xbciX\x15\x00\x00\x00embedding_size_factorq\x03G?\xea\xdcc\xef\xd9\x99\x16X\r\x00\x00\x00layers.choiceq\x04K\x02X\r\x00\x00\x00learning_rateq\x05G?dr\x82<\xab!\nX\x13\x00\x00\x00network_type.choiceq\x06K\x01X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G=\x87]&\xdb\x00\x8f\xa7u.' and reward: 0.39
Please either provide filename or allow plot in get_training_curves
Time for Neural Network hyperparameter optimization: 195.74989366531372
Best hyperparameter configuration for Tabular Neural Network: 
{'activation.choice': 2, 'dropout_prob': 0.09027041547300176, 'embedding_size_factor': 0.8394031223840865, 'layers.choice': 2, 'learning_rate': 0.0024960082713257935, 'network_type.choice': 1, 'use_batchnorm.choice': 0, 'weight_decay': 2.6561649676218885e-12}
Saving dataset/models/trainer.pkl
Loading: dataset/models/LightGBMClassifier/trial_0_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_1_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_2_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_3_model.pkl
Loading: dataset/models/NeuralNetClassifier/trial_4_tabularNN.pkl
Loading: dataset/models/NeuralNetClassifier/trial_5_tabularNN.pkl
Loading: dataset/models/NeuralNetClassifier/trial_6_tabularNN.pkl
Fitting model: weighted_ensemble_k0_l1 ... Training model for up to 119.75s of the -177.28s of remaining time.
Ensemble size: 11
Ensemble weights: 
[0.45454545 0.         0.18181818 0.09090909 0.18181818 0.09090909
 0.        ]
	0.3982	 = Validation accuracy score
	1.62s	 = Training runtime
	0.0s	 = Validation runtime
Saving dataset/models/weighted_ensemble_k0_l1/model.pkl
Saving dataset/models/trainer.pkl
Saving dataset/models/trainer.pkl
Saving dataset/models/trainer.pkl
AutoGluon training complete, total runtime = 298.95s ...
Loading: dataset/models/trainer.pkl

  #### save the trained model  ####################################### 

  #### Predict   #################################################### 
Loaded data from: https://autogluon.s3.amazonaws.com/datasets/Inc/test.csv | Columns = 15 / 15 | Rows = 9769 -> 9769
Loading: dataset/models/trainer.pkl
Loading: dataset/models/weighted_ensemble_k0_l1/model.pkl
Loading: dataset/models/LightGBMClassifier/trial_3_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_0_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_2_model.pkl
Loading: dataset/models/NeuralNetClassifier/trial_6_tabularNN.pkl
Loading: dataset/models/NeuralNetClassifier/trial_4_tabularNN.pkl

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
Saving dataset/learner.pkl
TabularPredictor saved. To load, use: TabularPredictor.load(dataset/)
<mlmodels.model_gluon.util_autogluon.Model_empty object at 0x7f6d63619c88>

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Warning: Permanently added the RSA host key for IP address '140.82.113.3' to the list of known hosts.
From github.com:arita37/mlmodels_store
   82fb86a..32e71f4  master     -> origin/master
Updating 82fb86a..32e71f4
Fast-forward
 .../20200519/list_log_pullrequest_20200519.md      |   2 +-
 error_list/20200519/list_log_testall_20200519.md   | 175 +++++++++++++++++++++
 2 files changed, 176 insertions(+), 1 deletion(-)
[master 1386ee6] ml_store
 1 file changed, 248 insertions(+)
To github.com:arita37/mlmodels_store.git
   32e71f4..1386ee6  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon//fb_prophet.py 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon//fb_prophet.py", line 160, in <module>
    test(data_path = "model_fb/fbprophet.json", choice="json" )
TypeError: test() got an unexpected keyword argument 'choice'

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Already up to date.
[master 0c9bb87] ml_store
 1 file changed, 36 insertions(+)
To github.com:arita37/mlmodels_store.git
   1386ee6..0c9bb87  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon//gluonts_model.py 
INFO:root:Using CPU
INFO:root:Using CPU
INFO:root:Using CPU
INFO:root:Using CPU
INFO:root:Using CPU
INFO:root:Using CPU
INFO:root:Using CPU
INFO:root:Using CPU
INFO:root:Using CPU
INFO:root:Using CPU
INFO:root:Using CPU
INFO:root:Using CPU
INFO:root:Using CPU
INFO:root:Using CPU
INFO:root:Using CPU

  #### Loading params   ############################################## 

  model_gluon.gluonts_model 
{'model_name': 'deepar', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'num_layers': 2, 'num_cells': 40, 'cell_type': 'lstm', 'dropout_rate': 0.1, 'use_feat_dynamic_real': False, 'use_feat_static_cat': False, 'use_feat_static_real': False, 'scaling': True, 'num_parallel_samples': 100}} {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []} {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}} {'path': 'ztest/model_gluon/gluonts_deepar/', 'plot_prob': True, 'quantiles': [0.5]}

  #### Loading dataset   ############################################# 
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}

  #### Model init, fit   ############################################# 
INFO:root:Using CPU
INFO:root:Start model training
INFO:root:Epoch[0] Learning rate is 0.001
  0%|          | 0/10 [00:00<?, ?it/s]INFO:numexpr.utils:NumExpr defaulting to 2 threads.
INFO:root:Number of parameters in DeepARTrainingNetwork: 26844
100%|██████████| 10/10 [00:02<00:00,  3.90it/s, avg_epoch_loss=5.27]
INFO:root:Epoch[0] Elapsed time 2.565 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=5.265628
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 5.265627861022949 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7fcee6e14400>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7fcee6e14400>

  #### Save the trained model  ###################################### 
WARNING:root:Serializing RepresentableBlockPredictor instances does not save the prediction network structure in a backwards-compatible manner. Be careful not to use this method in production.

  ['version.json', 'glutonts_model_pars.pkl', 'prediction_net-network.json', 'prediction_net-0000.params', 'parameters.json', 'type.txt', 'input_transform.json'] 

  #### Load the trained model  ###################################### 
INFO:root:Using CPU
INFO:root:Using CPU

  #### Predict   #################################################### 
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}

  #### metrics   #################################################### 
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]WARNING:root:multiple 5 does not divide base seasonality 1.Falling back to seasonality 1
Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 95.95it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 1039.7657063802083,
    "abs_error": 365.1685791015625,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 2.419588681645424,
    "sMAPE": 0.5075968211742471,
    "MSIS": 96.78353432450874,
    "QuantileLoss[0.5]": 365.1685485839844,
    "Coverage[0.5]": 1.0,
    "RMSE": 32.24539822021443,
    "NRMSE": 0.6788504888466197,
    "ND": 0.6406466300027412,
    "wQuantileLoss[0.5]": 0.6406465764631305,
    "mean_wQuantileLoss": 0.6406465764631305,
    "MAE_Coverage": 0.5
}

  #### Plot   ####################################################### 

  #### Loading params   ############################################## 

  model_gluon.gluonts_model 
{'model_name': 'deepfactor', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'num_hidden_global': 50, 'num_layers_global': 1, 'num_factors': 10, 'num_hidden_local': 5, 'num_layers_local': 1, 'cell_type': 'lstm', 'num_parallel_samples': 100, 'embedding_dimension': 10}, '_comment': {'distr_output': 'StudentTOutput()', 'cardinality': 'List[int] = list([1])', 'context_length': 'None'}} {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []} {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}} {'path': 'ztest/model_gluon/gluonts_deepfactor/', 'plot_prob': True, 'quantiles': [0.5]}

  #### Loading dataset   ############################################# 
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}

  #### Model init, fit   ############################################# 

INFO:root:Using CPU
INFO:root:Start model training
INFO:root:Epoch[0] Learning rate is 0.001
  0%|          | 0/10 [00:00<?, ?it/s]INFO:root:Number of parameters in DeepFactorTrainingNetwork: 12466
100%|██████████| 10/10 [00:01<00:00,  7.63it/s, avg_epoch_loss=2.71e+3]
INFO:root:Epoch[0] Elapsed time 1.312 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=2713.411247
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 2713.4112467447917 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7fceba7e76d8>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7fceba7e76d8>

  #### Save the trained model  ###################################### 
WARNING:root:Serializing RepresentableBlockPredictor instances does not save the prediction network structure in a backwards-compatible manner. Be careful not to use this method in production.

  ['version.json', 'glutonts_model_pars.pkl', 'prediction_net-network.json', 'prediction_net-0000.params', 'parameters.json', 'type.txt', 'input_transform.json'] 

  #### Load the trained model  ###################################### 
INFO:root:Using CPU
INFO:root:Using CPU

  #### Predict   #################################################### 
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}

  #### metrics   #################################################### 
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 162.32it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 2262.8567708333335,
    "abs_error": 552.1011962890625,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 3.6581948231980244,
    "sMAPE": 1.8700508550675963,
    "MSIS": 146.3277993985751,
    "QuantileLoss[0.5]": 552.1012096405029,
    "Coverage[0.5]": 0.0,
    "RMSE": 47.5694941200065,
    "NRMSE": 1.0014630341054,
    "ND": 0.9685985899808114,
    "wQuantileLoss[0.5]": 0.9685986134043911,
    "mean_wQuantileLoss": 0.9685986134043911,
    "MAE_Coverage": 0.5
}

  #### Plot   ####################################################### 

  #### Loading params   ############################################## 

  model_gluon.gluonts_model 
{'model_name': 'transformer', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'embedding_dimension': 20, 'dropout_rate': 0.1, 'model_dim': 32, 'inner_ff_dim_scale': 4, 'pre_seq': 'dn', 'post_seq': 'drn', 'act_type': 'softrelu', 'num_heads': 8, 'scaling': True, 'use_feat_dynamic_real': False, 'use_feat_static_cat': False}, '_comment': {'cardinality': 'List[int] = list([1])', 'context_length': 'None', 'distr_output': 'DistributionOutput = StudentTOutput()', 'lags_seq': 'Optional[List[int]] = None', 'time_features': 'Optional[List[TimeFeature]] = None'}} {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []} {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}} {'path': 'ztest/model_gluon/gluonts_transformer/', 'plot_prob': True, 'quantiles': [0.5]}

  #### Loading dataset   ############################################# 
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}

  #### Model init, fit   ############################################# 

INFO:root:Using CPU
INFO:root:Start model training
INFO:root:Epoch[0] Learning rate is 0.001
  0%|          | 0/10 [00:00<?, ?it/s]INFO:root:Number of parameters in TransformerTrainingNetwork: 33911
100%|██████████| 10/10 [00:01<00:00,  5.22it/s, avg_epoch_loss=5.23]
INFO:root:Epoch[0] Elapsed time 1.917 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=5.234732
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 5.234732294082642 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7fceba8a5ba8>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7fceba8a5ba8>

  #### Save the trained model  ###################################### 
WARNING:root:Serializing RepresentableBlockPredictor instances does not save the prediction network structure in a backwards-compatible manner. Be careful not to use this method in production.

  ['version.json', 'glutonts_model_pars.pkl', 'prediction_net-network.json', 'prediction_net-0000.params', 'parameters.json', 'type.txt', 'input_transform.json'] 

  #### Load the trained model  ###################################### 
INFO:root:Using CPU
INFO:root:Using CPU

  #### Predict   #################################################### 
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}

  #### metrics   #################################################### 
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 131.23it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 221.31087239583334,
    "abs_error": 154.08013916015625,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 1.0209272706197925,
    "sMAPE": 0.2627258058833944,
    "MSIS": 40.83708758946464,
    "QuantileLoss[0.5]": 154.08013534545898,
    "Coverage[0.5]": 0.6666666666666666,
    "RMSE": 14.876520843121666,
    "NRMSE": 0.3131899124867719,
    "ND": 0.2703160336143092,
    "wQuantileLoss[0.5]": 0.27031602692185785,
    "mean_wQuantileLoss": 0.27031602692185785,
    "MAE_Coverage": 0.16666666666666663
}

  #### Plot   ####################################################### 

  #### Loading params   ############################################## 

  model_gluon.gluonts_model 
{'model_name': 'wavenet', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'embedding_dimension': 20, 'num_parallel_samples': 100, 'num_bins': 1024, 'hybridize_prediction_net': False, 'n_residue': 24, 'n_skip': 32, 'n_stacks': 1, 'temperature': 1.0, 'act_type': 'elu'}, '_comment': {'cardinality': 'List[int] = [1]', 'context_length': 'None', 'seasonality': 'Optional[int] = None', 'dilation_depth': 'Optional[int] = None', 'train_window_length': 'Optional[int] = None'}} {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []} {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}} {'path': 'ztest/model_gluon/gluonts_wavenet/', 'plot_prob': True, 'quantiles': [0.5]}

  #### Loading dataset   ############################################# 
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}

  #### Model init, fit   ############################################# 

INFO:root:Using CPU
INFO:gluonts.model.wavenet._estimator:Using dilation depth 10 and receptive field length 1024
INFO:root:using training windows of length = 12
INFO:root:Start model training
INFO:root:Epoch[0] Learning rate is 0.001
  0%|          | 0/10 [00:00<?, ?it/s]INFO:root:Number of parameters in WaveNet: 97636
 30%|███       | 3/10 [00:13<00:31,  4.45s/it, avg_epoch_loss=6.94] 60%|██████    | 6/10 [00:25<00:17,  4.29s/it, avg_epoch_loss=6.9]  90%|█████████ | 9/10 [00:36<00:04,  4.18s/it, avg_epoch_loss=6.87]100%|██████████| 10/10 [00:40<00:00,  4.08s/it, avg_epoch_loss=6.86]
INFO:root:Epoch[0] Elapsed time 40.760 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=6.858920
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 6.858920335769653 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7fceba8496a0>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7fceba8496a0>

  #### Save the trained model  ###################################### 
WARNING:root:Serializing RepresentableBlockPredictor instances does not save the prediction network structure in a backwards-compatible manner. Be careful not to use this method in production.

  ['version.json', 'glutonts_model_pars.pkl', 'prediction_net-network.json', 'prediction_net-0000.params', 'parameters.json', 'type.txt', 'input_transform.json'] 

  #### Load the trained model  ###################################### 
INFO:root:Using CPU
INFO:root:Using CPU
INFO:gluonts.model.wavenet._estimator:Using dilation depth 10 and receptive field length 1024

  #### Predict   #################################################### 
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}

  #### metrics   #################################################### 
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 99.04it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 52458.427083333336,
    "abs_error": 2680.474853515625,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 17.760691878141472,
    "sMAPE": 1.4061240047914163,
    "MSIS": 710.4278174800496,
    "QuantileLoss[0.5]": 2680.4750061035156,
    "Coverage[0.5]": 1.0,
    "RMSE": 229.03804723960894,
    "NRMSE": 4.82185362609703,
    "ND": 4.702587462308114,
    "wQuantileLoss[0.5]": 4.702587730006168,
    "mean_wQuantileLoss": 4.702587730006168,
    "MAE_Coverage": 0.5
}

  #### Plot   ####################################################### 

  #### Loading params   ############################################## 

  model_gluon.gluonts_model 
{'model_name': 'feedforward', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'batch_normalization': False, 'mean_scaling': True, 'num_parallel_samples': 100}, '_comment': {'num_hidden_dimensions': 'Optional[List[int]] = None', 'context_length': 'Optional[int] = None', 'distr_output': 'DistributionOutput = StudentTOutput()'}} {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []} {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}} {'path': 'ztest/model_gluon/gluonts_feedforward/', 'plot_prob': True, 'quantiles': [0.5]}

  #### Loading dataset   ############################################# 
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}

  #### Model init, fit   ############################################# 

INFO:root:Using CPU
INFO:root:Start model training
INFO:root:Epoch[0] Learning rate is 0.001
  0%|          | 0/10 [00:00<?, ?it/s]INFO:root:Number of parameters in SimpleFeedForwardTrainingNetwork: 20323
100%|██████████| 10/10 [00:00<00:00, 57.29it/s, avg_epoch_loss=5.16]
INFO:root:Epoch[0] Elapsed time 0.175 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=5.155511
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 5.155510711669922 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7fcea371a748>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7fcea371a748>

  #### Save the trained model  ###################################### 
WARNING:root:Serializing RepresentableBlockPredictor instances does not save the prediction network structure in a backwards-compatible manner. Be careful not to use this method in production.

  ['version.json', 'glutonts_model_pars.pkl', 'prediction_net-network.json', 'prediction_net-0000.params', 'parameters.json', 'type.txt', 'input_transform.json'] 

  #### Load the trained model  ###################################### 
INFO:root:Using CPU
INFO:root:Using CPU

  #### Predict   #################################################### 
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}

  #### metrics   #################################################### 
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 154.75it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 483.8924560546875,
    "abs_error": 182.67916870117188,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 1.2104230053123408,
    "sMAPE": 0.3092474896732564,
    "MSIS": 48.4169185948301,
    "QuantileLoss[0.5]": 182.67915725708008,
    "Coverage[0.5]": 0.5833333333333334,
    "RMSE": 21.997555683636477,
    "NRMSE": 0.4631064354449785,
    "ND": 0.3204897696511787,
    "wQuantileLoss[0.5]": 0.3204897495738247,
    "mean_wQuantileLoss": 0.3204897495738247,
    "MAE_Coverage": 0.08333333333333337
}

  #### Plot   ####################################################### 

  #### Loading params   ############################################## 

  model_gluon.gluonts_model 
{'model_name': 'gp_forecaster', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'cardinality': 2, 'max_iter_jitter': 10, 'jitter_method': 'iter', 'sample_noise': True, 'num_parallel_samples': 100}, '_comment': {'context_length': 'Optional[int] = None', 'kernel_output': 'KernelOutput = RBFKernelOutput()', 'dtype': 'DType = np.float64', 'time_features': 'Optional[List[TimeFeature]] = None'}} {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []} {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}} {'path': 'ztest/model_gluon/gluonts_gpforecaster/', 'plot_prob': True, 'quantiles': [0.5]}

  #### Loading dataset   ############################################# 
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}

  #### Model init, fit   ############################################# 

INFO:root:Using CPU
INFO:root:Start model training
INFO:root:Epoch[0] Learning rate is 0.001
  0%|          | 0/10 [00:00<?, ?it/s]INFO:root:Number of parameters in GaussianProcessTrainingNetwork: 14
100%|██████████| 10/10 [00:01<00:00,  7.65it/s, avg_epoch_loss=160]
INFO:root:Epoch[0] Elapsed time 1.308 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=160.137221
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 160.13722096982082 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7fceb801c940>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7fceb801c940>

  #### Save the trained model  ###################################### 
WARNING:root:Serializing RepresentableBlockPredictor instances does not save the prediction network structure in a backwards-compatible manner. Be careful not to use this method in production.

  ['version.json', 'glutonts_model_pars.pkl', 'prediction_net-network.json', 'prediction_net-0000.params', 'parameters.json', 'type.txt', 'input_transform.json'] 

  #### Load the trained model  ###################################### 
INFO:root:Using CPU
INFO:root:Using CPU

  #### Predict   #################################################### 
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}

  #### metrics   #################################################### 
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 162.16it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 721.6386473701223,
    "abs_error": 263.04314901123786,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 1.7429107063314655,
    "sMAPE": 0.5744170818242088,
    "MSIS": 69.71642825325863,
    "QuantileLoss[0.5]": 263.04314901123786,
    "Coverage[0.5]": 0.08333333333333333,
    "RMSE": 26.86333276736381,
    "NRMSE": 0.5655438477339749,
    "ND": 0.4614792087916454,
    "wQuantileLoss[0.5]": 0.4614792087916454,
    "mean_wQuantileLoss": 0.4614792087916454,
    "MAE_Coverage": 0.4166666666666667
}

  #### Plot   ####################################################### 

  #### Loading params   ############################################## 

  model_gluon.gluonts_model 
{'model_name': 'deepstate', 'model_pars': {'freq': '5min', 'prediction_length': 12, 'cardinality': [1], 'add_trend': False, 'num_periods_to_train': 4, 'num_layers': 2, 'num_cells': 40, 'cell_type': 'lstm', 'num_parallel_samples': 100, 'dropout_rate': 0.1, 'use_feat_dynamic_real': False, 'use_feat_static_cat': False, 'scaling': True}, '_comment': {'past_length': 'Optional[int] = None', 'time_features': 'Optional[List[TimeFeature]] = None', 'noise_std_bounds': 'ParameterBounds = ParameterBounds(1e-6, 1.0)', 'prior_cov_bounds': 'ParameterBounds = ParameterBounds(1e-6, 1.0)', 'innovation_bounds': 'ParameterBounds = ParameterBounds(1e-6, 0.01)', 'embedding_dimension': 'Optional[List[int]] = None', 'issm: Optional[ISSM]': 'None', 'cardinality': 'List[int]'}} {'train': True, 'dt_source': 'https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv', 'train_data_path': 'dataset/timeseries/train_deepar.csv', 'test_data_path': 'dataset/timeseries/train_deepar.csv', 'prediction_length': 12, 'freq': '5min', 'start': '2015-02-26 21:42:53', 'col_date': 'timestamp', 'col_ytarget': ['value'], 'num_series': 1, 'cols_cat': [], 'cols_num': []} {'num_samples': 100, 'compute_pars': {'batch_size': 32, 'clip_gradient': 100, 'epochs': 1, 'init': 'xavier', 'learning_rate': 0.001, 'learning_rate_decay_factor': 0.5, 'hybridize': False, 'num_batches_per_epoch': 10, 'minimum_learning_rate': 5e-05, 'patience': 10, 'weight_decay': 1e-08}} {'path': 'ztest/model_gluon/gluonts_deepstate/', 'plot_prob': True, 'quantiles': [0.5]}

  #### Loading dataset   ############################################# 
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}

  #### Model init, fit   ############################################# 

INFO:root:Using CPU
INFO:root:Start model training
INFO:root:Epoch[0] Learning rate is 0.001
  0%|          | 0/10 [00:00<?, ?it/s]INFO:root:Number of parameters in DeepStateTrainingNetwork: 28054
 10%|█         | 1/10 [01:55<17:15, 115.03s/it, avg_epoch_loss=0.653] 20%|██        | 2/10 [05:05<18:21, 137.63s/it, avg_epoch_loss=0.635] 30%|███       | 3/10 [08:18<18:00, 154.32s/it, avg_epoch_loss=0.618] 40%|████      | 4/10 [11:51<17:10, 171.74s/it, avg_epoch_loss=0.6]   50%|█████     | 5/10 [15:37<15:41, 188.23s/it, avg_epoch_loss=0.582] 60%|██████    | 6/10 [19:14<13:06, 196.74s/it, avg_epoch_loss=0.565] 70%|███████   | 7/10 [22:37<09:56, 198.77s/it, avg_epoch_loss=0.548] 80%|████████  | 8/10 [26:36<07:01, 210.71s/it, avg_epoch_loss=0.531] 90%|█████████ | 9/10 [29:57<03:27, 207.80s/it, avg_epoch_loss=0.516]100%|██████████| 10/10 [33:34<00:00, 210.59s/it, avg_epoch_loss=0.502]100%|██████████| 10/10 [33:34<00:00, 201.46s/it, avg_epoch_loss=0.502]
INFO:root:Epoch[0] Elapsed time 2014.557 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=0.501657
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 0.5016570329666138 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7fcea3603fd0>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7fcea3603fd0>

  #### Save the trained model  ###################################### 
WARNING:root:Serializing RepresentableBlockPredictor instances does not save the prediction network structure in a backwards-compatible manner. Be careful not to use this method in production.

  ['version.json', 'glutonts_model_pars.pkl', 'prediction_net-network.json', 'prediction_net-0000.params', 'parameters.json', 'type.txt', 'input_transform.json'] 

  #### Load the trained model  ###################################### 
INFO:root:Using CPU
INFO:root:Using CPU

  #### Predict   #################################################### 
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}

  #### metrics   #################################################### 
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 19.49it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 143.64437866210938,
    "abs_error": 113.09156799316406,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 0.7493390547977266,
    "sMAPE": 0.20097564209453803,
    "MSIS": 29.97356785373142,
    "QuantileLoss[0.5]": 113.0915756225586,
    "Coverage[0.5]": 0.4166666666666667,
    "RMSE": 11.985173284609171,
    "NRMSE": 0.2523194375707194,
    "ND": 0.19840625963712993,
    "wQuantileLoss[0.5]": 0.19840627302203262,
    "mean_wQuantileLoss": 0.19840627302203262,
    "MAE_Coverage": 0.08333333333333331
}

  #### Plot   ####################################################### 


   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Warning: Permanently added the RSA host key for IP address '140.82.112.4' to the list of known hosts.
From github.com:arita37/mlmodels_store
   0c9bb87..e299cde  master     -> origin/master
Updating 0c9bb87..e299cde
Fast-forward
 error_list/20200519/list_log_testall_20200519.md | 7 +++++++
 1 file changed, 7 insertions(+)
[master f14fdfd] ml_store
 1 file changed, 506 insertions(+)
To github.com:arita37/mlmodels_store.git
   e299cde..f14fdfd  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_sklearn//model_sklearn.py 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 

  #### save the trained model  ####################################### 

  #### Predict   ##################################################### 

  #### metrics   ##################################################### 
{'mode': 'test', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/tabular/titanic_train_preprocessed.csv', 'data_type': 'pandas', 'train': True}
{'roc_auc_score': 1.0}

  #### Plot   ######################################################## 

  #### Save/Load   ################################################### 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_sklearn/model_sklearn/model.pkl'}
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_sklearn/model_sklearn/model.pkl'}
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
                       max_depth=4, max_features='auto', max_leaf_nodes=None,
                       min_impurity_decrease=0.0, min_impurity_split=None,
                       min_samples_leaf=1, min_samples_split=2,
                       min_weight_fraction_leaf=0.0, n_estimators=10,
                       n_jobs=None, oob_score=False, random_state=0, verbose=0,
                       warm_start=False)
{'mode': 'test', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/tabular/titanic_train_preprocessed.csv', 'data_type': 'pandas', 'train': True}
{'roc_auc_score': 0.9615384615384616}

  #### Module init   ############################################ 

  <module 'mlmodels.model_sklearn.model_sklearn' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_sklearn/model_sklearn.py'> 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Model init   ############################################ 

  <mlmodels.model_sklearn.model_sklearn.Model object at 0x7f9f9b174630> 

  #### Fit   ######################################################## 

  #### Predict   #################################################### 
None

  #### Get  metrics   ################################################ 
{'mode': 'test', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/tabular/titanic_train_preprocessed.csv', 'data_type': 'pandas', 'train': True}

  #### Save   ######################################################## 

  #### Load   ######################################################## 

  ############ Model preparation   ################################## 

  #### Module init   ############################################ 

  <module 'mlmodels.model_sklearn.model_sklearn' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_sklearn/model_sklearn.py'> 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Model init   ############################################ 

  ############ Model fit   ########################################## 
fit success None

  ############ Prediction############################################ 
None

  ############ Save/ Load ############################################ 
/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/sklearn/ensemble/forest.py:245: FutureWarning: The default value of n_estimators will change from 10 in version 0.20 to 100 in 0.22.
  "10 in version 0.20 to 100 in 0.22.", FutureWarning)

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Already up to date.
[master 149ac47] ml_store
 1 file changed, 109 insertions(+)
To github.com:arita37/mlmodels_store.git
   f14fdfd..149ac47  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_sklearn//model_lightgbm.py 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 

  #### save the trained model  ####################################### 

  #### Predict   ##################################################### 
[[ 1.02817479 -0.50845713  1.7653351   0.77741921  0.61771419 -0.11877117
   0.45015551 -0.19899818  1.86647138  0.8709698 ]
 [ 1.01195228 -1.88141087  1.70018815  0.4972691  -0.91766462  0.2373327
  -1.09033833 -2.14444405 -0.36956243  0.60878366]
 [ 1.02242019  1.85300949  0.64435367  0.14225137  1.15080755  0.51350548
  -0.45994283  0.37245685 -0.1484898   0.37167029]
 [ 1.22867367  0.13437312 -0.18242041 -0.2683713  -1.73963799 -0.13167563
  -0.92687194  1.01855247  1.2305582  -0.49112514]
 [ 1.46893146 -1.47115693  0.58591043 -0.8301719   1.03345052 -0.8805776
  -0.95542526 -0.27909772  1.62284909  2.06578332]
 [ 1.36586461  3.9586027   0.54812958  0.64864364  0.84917607  0.10734329
   1.38631426 -1.39881282  0.08176782 -1.63744959]
 [ 1.39198128 -0.19022103 -0.53722302 -0.44873803  0.70455707 -0.67244804
  -0.70134443 -0.55749472  0.93916874  0.15626385]
 [ 1.77547698 -0.20339445 -0.19883786  0.24266944  0.96435056  0.20183018
  -0.54577417  0.66102029  1.79215821 -0.7003985 ]
 [ 1.17867274 -0.59980453 -0.6946936   1.12341216  1.17899425  0.30526704
   0.01335268  1.3887794  -0.66134424  0.6218035 ]
 [ 1.838294    0.50274088  0.12910158  1.55880554  1.32551412  0.1094027
   1.40754    -1.2197444   2.44936865  1.6169496 ]
 [ 0.35413361  0.21112476  0.92145007  0.01652757  0.90394545  0.17718772
   0.09542509 -1.11647002  0.0809271   0.0607502 ]
 [ 0.96457205 -0.10679399  1.12232832  1.45142926  1.21828168 -0.61803685
   0.43816635 -2.03720123 -1.94258918 -0.9970198 ]
 [ 0.84806927  0.45194604  0.63019567 -1.57915629  0.82798737 -0.82862798
  -0.10534471  0.52887975 -2.23708651 -0.4148469 ]
 [ 0.77528533  1.47016034  1.03298378 -0.87000822  0.78655651  0.36919047
  -0.14319575  0.85328219 -0.13971173 -0.22241403]
 [ 0.61363671  0.3166589   1.34710546 -1.89526695 -0.76045809  0.08972912
  -0.32905155  0.41026575  0.85987097 -1.04906775]
 [ 0.68188934 -1.15498263  1.22895559 -0.1776322   0.99854519 -1.51045638
  -0.27584606  1.01120706 -1.47656266  1.30970591]
 [ 0.88883881  1.03368687 -0.04970258  0.80884436  0.81405135  1.78975468
   1.14690038  0.45128402 -1.68405999  0.46664327]
 [ 0.6109426  -2.79099641 -1.33520272 -0.45611756 -0.94495995 -0.97989025
  -0.15699367  0.69257435 -0.47867236 -0.10646012]
 [ 1.1437713   0.7278135   0.35249436  0.51507361  1.17718111 -2.78253447
  -1.94332341  0.58464661  0.32427424 -0.23643695]
 [ 0.76170668 -1.48515645  1.30253554 -0.59246129 -1.64162479 -2.30490794
  -1.34869645 -0.03181717  0.11248774 -0.36261209]
 [ 0.5630779  -1.17598267 -0.17418034  1.01012718  1.06796368  0.92001793
  -0.16819884 -0.19505734  0.80539342  0.4611641 ]
 [ 0.77370361  1.27852808 -2.11416392 -0.44222928  1.06821044  0.32352735
  -2.50644065 -0.10999149  0.00854895 -0.41163916]
 [ 0.69211449 -0.06065249  2.05635552 -2.413503    1.17456965 -1.77756638
  -0.28173627 -0.77785883  1.11584111  1.76024923]
 [ 0.89891716  0.55743945 -0.75806733  0.18103874  0.84146721  1.10717545
   0.69336623  1.44287693 -0.53968156 -0.8088472 ]
 [ 0.87122579 -0.20975294 -0.45698786  0.93514778 -0.87353582  1.81252782
   0.92550121  0.14010988 -1.41914878  1.06898597]]

  #### metrics   ##################################################### 
{}

  #### Plot   ######################################################## 

  #### Save/Load   ################################################### 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_sklearn/model_lightgbm/model.pkl'}
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_sklearn/model_lightgbm/model.pkl'}
<__main__.Model object at 0x7f1c208ecda0>

  #### Module init   ############################################ 

  <module 'mlmodels.model_sklearn.model_lightgbm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_sklearn/model_lightgbm.py'> 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Model init   ############################################ 

  <mlmodels.model_sklearn.model_lightgbm.Model object at 0x7f1c3ac695f8> 

  #### Fit   ######################################################## 

  #### Predict   #################################################### 
[[ 0.44118981  0.47985237 -0.1920037  -1.55269878 -1.88873982  0.57846442
   0.39859839 -0.9612636  -1.45832446 -3.05376438]
 [ 0.92686981  0.39233491 -0.4234783   0.44838065 -1.09230828  1.1253235
  -0.94843966  0.10405339  0.52800342  1.00796648]
 [ 1.12641981 -0.6294416   1.1010002  -1.1134361   0.94459507 -0.06741002
  -0.1834002   1.16143998 -0.02752939  0.78002714]
 [ 0.98042741  1.93752881 -0.23083974  0.36633201  1.10018476 -1.04458938
  -0.34498721  2.05117344  0.585662   -2.793085  ]
 [ 0.96703727  0.38271517 -0.80618482 -0.28899734  0.90852604 -0.39181624
   1.62091229  0.68400133 -0.35340998 -0.25167421]
 [ 0.89562312 -2.29820588 -0.01952256  1.45652739 -1.85064099  0.31663724
   0.11133727 -2.66412594 -0.42642862 -0.83998891]
 [ 1.18947778 -0.68067814 -0.05682448 -0.08450803  0.82178321 -0.29736188
  -0.18657899  0.417302    0.78477065  0.49233656]
 [ 1.37661405 -0.60022533  0.72591685 -0.37951752 -0.62754626 -1.01480369
   0.96622086  0.4359862  -0.68748739  3.32107876]
 [ 0.62368852  1.2066079   0.90399917 -0.28286355 -1.18913787 -0.26632688
   1.42361443  1.06897162  0.04037143  1.57546791]
 [ 0.77370361  1.27852808 -2.11416392 -0.44222928  1.06821044  0.32352735
  -2.50644065 -0.10999149  0.00854895 -0.41163916]
 [ 1.18468624 -1.00016919 -0.59384307  1.04499441  0.96548233  0.6085147
  -0.625342   -0.0693287  -0.10839207 -0.34390071]
 [ 1.12062155 -0.7029204  -1.22957425  0.72555052 -1.18013412 -0.32420422
   1.10223673  0.81434313  0.78046993  1.10861676]
 [ 0.76170668 -1.48515645  1.30253554 -0.59246129 -1.64162479 -2.30490794
  -1.34869645 -0.03181717  0.11248774 -0.36261209]
 [ 0.98379959 -0.40724002  0.93272141  0.16056499 -1.278618   -0.12014998
   0.19975956  0.38560229  0.71829074 -0.5301198 ]
 [ 0.89551051  0.92061512  0.79452824 -0.03536792  0.8780991   2.11060505
  -1.02188594 -1.30653407  0.07638048 -1.87316098]
 [ 1.58463774  0.057121   -0.01771832 -0.79954749  1.32970299 -0.2915946
  -1.1077125  -0.25898285  0.1892932  -1.71939447]
 [ 0.99785516 -0.6001388   0.45794708  0.14676526 -0.93355729  0.57180488
   0.57296273 -0.03681766  0.11236849 -0.01781755]
 [ 2.07582971 -1.40232915 -0.47918492  0.45112294  1.03436581 -0.6949209
  -0.4189379   0.5154138  -1.11487105 -1.95210529]
 [ 1.34728643 -0.36453805  0.08075099 -0.45971768 -0.8894876   1.70548352
   0.09499611  0.24050555 -0.9994265  -0.76780375]
 [ 0.87699465  1.23225307 -0.86778722 -0.25417987  0.89189141  1.39984394
  -0.87728152 -0.78191168 -0.43750898 -1.44087602]
 [ 0.86146256  0.07432055 -1.34501002 -0.19956072 -1.47533915 -0.65460317
  -0.31456386  0.3180143  -0.89027155 -1.29525789]
 [ 1.66752297  1.22372221 -0.4599301  -0.0593679  -0.493857    1.4489894
  -1.18110317 -0.47758085  0.02599999 -0.79079995]
 [ 1.36586461  3.9586027   0.54812958  0.64864364  0.84917607  0.10734329
   1.38631426 -1.39881282  0.08176782 -1.63744959]
 [ 1.18559003  0.08646441  1.23289919 -2.14246673  1.033341   -0.83016886
   0.36723181  0.45161595  1.10417433 -0.42285696]
 [ 0.87122579 -0.20975294 -0.45698786  0.93514778 -0.87353582  1.81252782
   0.92550121  0.14010988 -1.41914878  1.06898597]]
None

  #### Get  metrics   ################################################ 

  #### Save   ######################################################## 

  #### Load   ######################################################## 

  ############ Model preparation   ################################## 

  #### Module init   ############################################ 

  <module 'mlmodels.model_sklearn.model_lightgbm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_sklearn/model_lightgbm.py'> 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Model init   ############################################ 

  ############ Model fit   ########################################## 
fit success None

  ############ Prediction############################################ 
[[ 0.94781411 -1.13379204  0.64098587 -0.1905483  -1.23912256  0.23333913
  -0.3169012   0.43499832  0.9104236   1.21987438]
 [ 0.89562312 -2.29820588 -0.01952256  1.45652739 -1.85064099  0.31663724
   0.11133727 -2.66412594 -0.42642862 -0.83998891]
 [ 1.39198128 -0.19022103 -0.53722302 -0.44873803  0.70455707 -0.67244804
  -0.70134443 -0.55749472  0.93916874  0.15626385]
 [ 0.46739791 -0.23787527 -0.15449119 -0.75566277 -0.54706224  1.85143789
  -1.46405357  0.20909668  1.55501599 -0.09243232]
 [ 1.16777676 -0.66575452 -1.23312074 -1.67419581  1.01313574  0.82502982
  -0.12046457 -0.49821356 -0.31098498 -1.18231813]
 [ 0.9292506  -1.10657307 -1.95816909 -0.3592241  -1.21258781  0.5053819
   0.54264529  1.2179409  -1.94068096  0.67780757]
 [ 0.88861146  0.84958685 -0.03091142 -0.12215402 -1.14722826 -0.68085157
  -0.32606131 -1.06787658 -0.07667936  0.35571726]
 [ 0.69211449 -0.06065249  2.05635552 -2.413503    1.17456965 -1.77756638
  -0.28173627 -0.77785883  1.11584111  1.76024923]
 [ 1.27991386 -0.87142207 -0.32403233 -0.86482994 -0.96853969  0.60874908
   0.50798434  0.5616381   1.51475038 -1.51107661]
 [ 0.96457205 -0.10679399  1.12232832  1.45142926  1.21828168 -0.61803685
   0.43816635 -2.03720123 -1.94258918 -0.9970198 ]
 [ 0.70017571  0.55607351  0.08968641  1.69380911  0.88239331  0.19686978
  -0.56378873  0.16986926 -1.16400797 -0.6011568 ]
 [ 0.76170668 -1.48515645  1.30253554 -0.59246129 -1.64162479 -2.30490794
  -1.34869645 -0.03181717  0.11248774 -0.36261209]
 [ 0.8786438   1.03703898 -0.47712421  0.67261975 -1.04948638  2.42887697
   0.52475049  1.00568668  0.35356722 -0.03599018]
 [ 0.96703727  0.38271517 -0.80618482 -0.28899734  0.90852604 -0.39181624
   1.62091229  0.68400133 -0.35340998 -0.25167421]
 [ 1.01177337  0.09574677  0.73140252  1.0334508  -1.42203164 -0.14627327
  -0.01745495 -0.85749682 -0.93418184  0.95449567]
 [ 1.06040861  0.5103076   0.50172511 -0.91579185 -0.90731836 -0.40725204
  -0.17961229  0.98495167  1.07125243 -0.59334375]
 [ 0.88838944  0.28299553  0.01795589  0.10803082 -0.84967187  0.02941762
  -0.50397395 -0.13479313  1.04921829 -1.27046078]
 [ 0.87226739 -2.51630386 -0.77507029 -0.59566788  1.02600767 -0.30912132
   1.74643509  0.51093777  1.71066184  0.14164054]
 [ 0.92686981  0.39233491 -0.4234783   0.44838065 -1.09230828  1.1253235
  -0.94843966  0.10405339  0.52800342  1.00796648]
 [ 1.22867367  0.13437312 -0.18242041 -0.2683713  -1.73963799 -0.13167563
  -0.92687194  1.01855247  1.2305582  -0.49112514]
 [ 0.79032389  1.61336137 -2.09424782 -0.37480469  0.91588404 -0.74996962
   0.31027229  2.0546241   0.05340954 -0.22876583]
 [ 0.6236295   0.98635218  1.45391758 -0.46615486  0.93640333  1.38499134
   0.03494359 -1.07296428  0.49515861  0.66168108]
 [ 0.5630779  -1.17598267 -0.17418034  1.01012718  1.06796368  0.92001793
  -0.16819884 -0.19505734  0.80539342  0.4611641 ]
 [ 0.85982375  0.17195713 -0.34898419  0.49056104 -1.15649503 -1.39528303
   0.61472628 -0.52235647 -0.3692559  -0.977773  ]
 [ 0.85335555 -0.70435033 -0.67938378 -0.04586669 -1.29936179 -0.21873346
   0.59003946  1.53920701 -1.14870423 -0.95090925]]
None

  ############ Save/ Load ############################################ 

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Already up to date.
[master 6206e6a] ml_store
 1 file changed, 247 insertions(+)
To github.com:arita37/mlmodels_store.git
   149ac47..6206e6a  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//nbeats.py 

  #### Loading params   ####################################### 

  #### Loading dataset  ####################################### 
   milk_production_pounds
0                     589
1                     561
2                     640
3                     656
4                     727
[[0.60784314]
 [0.57894737]
 [0.66047472]
 [0.67698658]
 [0.750258  ]
 [0.71929825]
 [0.66047472]
 [0.61816305]
 [0.58617131]
 [0.59545924]
 [0.57069143]
 [0.6006192 ]
 [0.61919505]
 [0.58410733]
 [0.67389061]
 [0.69453044]
 [0.76573787]
 [0.73890609]
 [0.68111455]
 [0.63673891]
 [0.60165119]
 [0.60577915]
 [0.58307534]
 [0.61713106]
 [0.64809082]
 [0.6377709 ]
 [0.71001032]
 [0.72755418]
 [0.79463364]
 [0.75954592]
 [0.6996904 ]
 [0.65944272]
 [0.62332301]
 [0.63054696]
 [0.6130031 ]
 [0.65428277]
 [0.67905057]
 [0.64189886]
 [0.73168215]
 [0.74509804]
 [0.80701754]
 [0.78018576]
 [0.7244582 ]
 [0.67389061]
 [0.63467492]
 [0.64086687]
 [0.62125903]
 [0.65531476]
 [0.69865841]
 [0.65531476]
 [0.75954592]
 [0.77915377]
 [0.8369453 ]
 [0.82352941]
 [0.75851393]
 [0.71929825]
 [0.68214654]
 [0.68833849]
 [0.66563467]
 [0.71001032]
 [0.73581011]
 [0.68833849]
 [0.78637771]
 [0.80908153]
 [0.86377709]
 [0.84313725]
 [0.79153767]
 [0.74509804]
 [0.70278638]
 [0.70897833]
 [0.68111455]
 [0.72033024]
 [0.73993808]
 [0.71826625]
 [0.7997936 ]
 [0.82146543]
 [0.88544892]
 [0.85242518]
 [0.80804954]
 [0.76367389]
 [0.72342621]
 [0.72858617]
 [0.69865841]
 [0.73374613]
 [0.75748194]
 [0.7120743 ]
 [0.81011352]
 [0.83075335]
 [0.89886481]
 [0.87203302]
 [0.82662539]
 [0.78844169]
 [0.74819401]
 [0.74613003]
 [0.7120743 ]
 [0.75748194]
 [0.77399381]
 [0.72961816]
 [0.83281734]
 [0.8503612 ]
 [0.91434469]
 [0.88648091]
 [0.84520124]
 [0.80804954]
 [0.76367389]
 [0.77089783]
 [0.73374613]
 [0.7750258 ]
 [0.82972136]
 [0.78018576]
 [0.8875129 ]
 [0.90608875]
 [0.97213622]
 [0.94220846]
 [0.89680083]
 [0.86068111]
 [0.81527348]
 [0.8255934 ]
 [0.7874097 ]
 [0.8255934 ]
 [0.85242518]
 [0.8245614 ]
 [0.91847265]
 [0.92879257]
 [0.99174407]
 [0.96491228]
 [0.92260062]
 [0.88235294]
 [0.83488132]
 [0.83591331]
 [0.79050568]
 [0.83075335]
 [0.84726522]
 [0.79772962]
 [0.91124871]
 [0.92672859]
 [0.9876161 ]
 [0.95356037]
 [0.90918473]
 [0.86377709]
 [0.80908153]
 [0.81630547]
 [0.78431373]
 [0.82765738]
 [0.85448916]
 [0.80288958]
 [0.91744066]
 [0.93085655]
 [1.        ]
 [0.97729618]
 [0.9370485 ]
 [0.89473684]
 [0.84107327]
 [0.8379773 ]
 [0.79772962]
 [0.83900929]
 [0.86068111]
 [0.80701754]
 [0.92053664]
 [0.93188854]
 [0.99690402]
 [0.96697626]
 [0.9246646 ]
 [0.88544892]
 [0.84313725]
 [0.85345717]
 [0.82249742]
 [0.86996904]]

  #### Model setup   ########################################## 
| N-Beats
| --  Stack Generic (#0) (share_weights_in_stack=0)
     | -- GenericBlock(units=256, thetas_dim=7, backcast_length=10, forecast_length=5, share_thetas=False) at @140474744819664
     | -- GenericBlock(units=256, thetas_dim=7, backcast_length=10, forecast_length=5, share_thetas=False) at @140474744819440
     | -- GenericBlock(units=256, thetas_dim=7, backcast_length=10, forecast_length=5, share_thetas=False) at @140474744818208
| --  Stack Generic (#1) (share_weights_in_stack=0)
     | -- GenericBlock(units=256, thetas_dim=8, backcast_length=10, forecast_length=5, share_thetas=False) at @140474744817760
     | -- GenericBlock(units=256, thetas_dim=8, backcast_length=10, forecast_length=5, share_thetas=False) at @140474744817256
     | -- GenericBlock(units=256, thetas_dim=8, backcast_length=10, forecast_length=5, share_thetas=False) at @140474744816920

  #### Model fit   ############################################ 
   milk_production_pounds
0                     589
1                     561
2                     640
3                     656
4                     727
[[0.60784314]
 [0.57894737]
 [0.66047472]
 [0.67698658]
 [0.750258  ]
 [0.71929825]
 [0.66047472]
 [0.61816305]
 [0.58617131]
 [0.59545924]
 [0.57069143]
 [0.6006192 ]
 [0.61919505]
 [0.58410733]
 [0.67389061]
 [0.69453044]
 [0.76573787]
 [0.73890609]
 [0.68111455]
 [0.63673891]
 [0.60165119]
 [0.60577915]
 [0.58307534]
 [0.61713106]
 [0.64809082]
 [0.6377709 ]
 [0.71001032]
 [0.72755418]
 [0.79463364]
 [0.75954592]
 [0.6996904 ]
 [0.65944272]
 [0.62332301]
 [0.63054696]
 [0.6130031 ]
 [0.65428277]
 [0.67905057]
 [0.64189886]
 [0.73168215]
 [0.74509804]
 [0.80701754]
 [0.78018576]
 [0.7244582 ]
 [0.67389061]
 [0.63467492]
 [0.64086687]
 [0.62125903]
 [0.65531476]
 [0.69865841]
 [0.65531476]
 [0.75954592]
 [0.77915377]
 [0.8369453 ]
 [0.82352941]
 [0.75851393]
 [0.71929825]
 [0.68214654]
 [0.68833849]
 [0.66563467]
 [0.71001032]
 [0.73581011]
 [0.68833849]
 [0.78637771]
 [0.80908153]
 [0.86377709]
 [0.84313725]
 [0.79153767]
 [0.74509804]
 [0.70278638]
 [0.70897833]
 [0.68111455]
 [0.72033024]
 [0.73993808]
 [0.71826625]
 [0.7997936 ]
 [0.82146543]
 [0.88544892]
 [0.85242518]
 [0.80804954]
 [0.76367389]
 [0.72342621]
 [0.72858617]
 [0.69865841]
 [0.73374613]
 [0.75748194]
 [0.7120743 ]
 [0.81011352]
 [0.83075335]
 [0.89886481]
 [0.87203302]
 [0.82662539]
 [0.78844169]
 [0.74819401]
 [0.74613003]
 [0.7120743 ]
 [0.75748194]
 [0.77399381]
 [0.72961816]
 [0.83281734]
 [0.8503612 ]
 [0.91434469]
 [0.88648091]
 [0.84520124]
 [0.80804954]
 [0.76367389]
 [0.77089783]
 [0.73374613]
 [0.7750258 ]
 [0.82972136]
 [0.78018576]
 [0.8875129 ]
 [0.90608875]
 [0.97213622]
 [0.94220846]
 [0.89680083]
 [0.86068111]
 [0.81527348]
 [0.8255934 ]
 [0.7874097 ]
 [0.8255934 ]
 [0.85242518]
 [0.8245614 ]
 [0.91847265]
 [0.92879257]
 [0.99174407]
 [0.96491228]
 [0.92260062]
 [0.88235294]
 [0.83488132]
 [0.83591331]
 [0.79050568]
 [0.83075335]
 [0.84726522]
 [0.79772962]
 [0.91124871]
 [0.92672859]
 [0.9876161 ]
 [0.95356037]
 [0.90918473]
 [0.86377709]
 [0.80908153]
 [0.81630547]
 [0.78431373]
 [0.82765738]
 [0.85448916]
 [0.80288958]
 [0.91744066]
 [0.93085655]
 [1.        ]
 [0.97729618]
 [0.9370485 ]
 [0.89473684]
 [0.84107327]
 [0.8379773 ]
 [0.79772962]
 [0.83900929]
 [0.86068111]
 [0.80701754]
 [0.92053664]
 [0.93188854]
 [0.99690402]
 [0.96697626]
 [0.9246646 ]
 [0.88544892]
 [0.84313725]
 [0.85345717]
 [0.82249742]
 [0.86996904]]
--- fiting ---
grad_step = 000000, loss = 0.394448
plot()
Saved image to .//n_beats_0.png.
grad_step = 000001, loss = 0.275642
grad_step = 000002, loss = 0.185854
grad_step = 000003, loss = 0.101231
grad_step = 000004, loss = 0.046282
grad_step = 000005, loss = 0.050176
grad_step = 000006, loss = 0.058623
grad_step = 000007, loss = 0.038143
grad_step = 000008, loss = 0.017188
grad_step = 000009, loss = 0.006738
grad_step = 000010, loss = 0.007483
grad_step = 000011, loss = 0.012616
grad_step = 000012, loss = 0.016515
grad_step = 000013, loss = 0.017227
grad_step = 000014, loss = 0.015336
grad_step = 000015, loss = 0.012392
grad_step = 000016, loss = 0.010063
grad_step = 000017, loss = 0.009246
grad_step = 000018, loss = 0.009586
grad_step = 000019, loss = 0.009928
grad_step = 000020, loss = 0.009472
grad_step = 000021, loss = 0.008394
grad_step = 000022, loss = 0.007380
grad_step = 000023, loss = 0.006878
grad_step = 000024, loss = 0.006824
grad_step = 000025, loss = 0.006913
grad_step = 000026, loss = 0.006890
grad_step = 000027, loss = 0.006757
grad_step = 000028, loss = 0.006649
grad_step = 000029, loss = 0.006682
grad_step = 000030, loss = 0.006785
grad_step = 000031, loss = 0.006771
grad_step = 000032, loss = 0.006548
grad_step = 000033, loss = 0.006202
grad_step = 000034, loss = 0.005903
grad_step = 000035, loss = 0.005763
grad_step = 000036, loss = 0.005755
grad_step = 000037, loss = 0.005784
grad_step = 000038, loss = 0.005748
grad_step = 000039, loss = 0.005639
grad_step = 000040, loss = 0.005513
grad_step = 000041, loss = 0.005433
grad_step = 000042, loss = 0.005418
grad_step = 000043, loss = 0.005428
grad_step = 000044, loss = 0.005411
grad_step = 000045, loss = 0.005355
grad_step = 000046, loss = 0.005285
grad_step = 000047, loss = 0.005221
grad_step = 000048, loss = 0.005161
grad_step = 000049, loss = 0.005094
grad_step = 000050, loss = 0.005020
grad_step = 000051, loss = 0.004960
grad_step = 000052, loss = 0.004923
grad_step = 000053, loss = 0.004896
grad_step = 000054, loss = 0.004856
grad_step = 000055, loss = 0.004797
grad_step = 000056, loss = 0.004736
grad_step = 000057, loss = 0.004689
grad_step = 000058, loss = 0.004653
grad_step = 000059, loss = 0.004610
grad_step = 000060, loss = 0.004552
grad_step = 000061, loss = 0.004483
grad_step = 000062, loss = 0.004419
grad_step = 000063, loss = 0.004357
grad_step = 000064, loss = 0.004299
grad_step = 000065, loss = 0.004238
grad_step = 000066, loss = 0.004178
grad_step = 000067, loss = 0.004118
grad_step = 000068, loss = 0.004045
grad_step = 000069, loss = 0.003964
grad_step = 000070, loss = 0.003890
grad_step = 000071, loss = 0.003816
grad_step = 000072, loss = 0.003734
grad_step = 000073, loss = 0.003646
grad_step = 000074, loss = 0.003559
grad_step = 000075, loss = 0.003466
grad_step = 000076, loss = 0.003368
grad_step = 000077, loss = 0.003271
grad_step = 000078, loss = 0.003166
grad_step = 000079, loss = 0.003060
grad_step = 000080, loss = 0.002954
grad_step = 000081, loss = 0.002844
grad_step = 000082, loss = 0.002735
grad_step = 000083, loss = 0.002622
grad_step = 000084, loss = 0.002518
grad_step = 000085, loss = 0.002422
grad_step = 000086, loss = 0.002335
grad_step = 000087, loss = 0.002256
grad_step = 000088, loss = 0.002186
grad_step = 000089, loss = 0.002126
grad_step = 000090, loss = 0.002075
grad_step = 000091, loss = 0.002032
grad_step = 000092, loss = 0.001995
grad_step = 000093, loss = 0.001959
grad_step = 000094, loss = 0.001923
grad_step = 000095, loss = 0.001881
grad_step = 000096, loss = 0.001832
grad_step = 000097, loss = 0.001784
grad_step = 000098, loss = 0.001744
grad_step = 000099, loss = 0.001705
grad_step = 000100, loss = 0.001661
plot()
Saved image to .//n_beats_100.png.
grad_step = 000101, loss = 0.001616
grad_step = 000102, loss = 0.001578
grad_step = 000103, loss = 0.001545
grad_step = 000104, loss = 0.001511
grad_step = 000105, loss = 0.001475
grad_step = 000106, loss = 0.001445
grad_step = 000107, loss = 0.001415
grad_step = 000108, loss = 0.001383
grad_step = 000109, loss = 0.001349
grad_step = 000110, loss = 0.001319
grad_step = 000111, loss = 0.001291
grad_step = 000112, loss = 0.001262
grad_step = 000113, loss = 0.001232
grad_step = 000114, loss = 0.001205
grad_step = 000115, loss = 0.001182
grad_step = 000116, loss = 0.001161
grad_step = 000117, loss = 0.001140
grad_step = 000118, loss = 0.001122
grad_step = 000119, loss = 0.001104
grad_step = 000120, loss = 0.001088
grad_step = 000121, loss = 0.001073
grad_step = 000122, loss = 0.001059
grad_step = 000123, loss = 0.001045
grad_step = 000124, loss = 0.001031
grad_step = 000125, loss = 0.001017
grad_step = 000126, loss = 0.001003
grad_step = 000127, loss = 0.000989
grad_step = 000128, loss = 0.000976
grad_step = 000129, loss = 0.000963
grad_step = 000130, loss = 0.000950
grad_step = 000131, loss = 0.000938
grad_step = 000132, loss = 0.000925
grad_step = 000133, loss = 0.000910
grad_step = 000134, loss = 0.000895
grad_step = 000135, loss = 0.000880
grad_step = 000136, loss = 0.000866
grad_step = 000137, loss = 0.000852
grad_step = 000138, loss = 0.000839
grad_step = 000139, loss = 0.000826
grad_step = 000140, loss = 0.000813
grad_step = 000141, loss = 0.000800
grad_step = 000142, loss = 0.000788
grad_step = 000143, loss = 0.000777
grad_step = 000144, loss = 0.000768
grad_step = 000145, loss = 0.000766
grad_step = 000146, loss = 0.000781
grad_step = 000147, loss = 0.000816
grad_step = 000148, loss = 0.000819
grad_step = 000149, loss = 0.000747
grad_step = 000150, loss = 0.000709
grad_step = 000151, loss = 0.000747
grad_step = 000152, loss = 0.000740
grad_step = 000153, loss = 0.000689
grad_step = 000154, loss = 0.000697
grad_step = 000155, loss = 0.000711
grad_step = 000156, loss = 0.000675
grad_step = 000157, loss = 0.000667
grad_step = 000158, loss = 0.000683
grad_step = 000159, loss = 0.000661
grad_step = 000160, loss = 0.000646
grad_step = 000161, loss = 0.000657
grad_step = 000162, loss = 0.000648
grad_step = 000163, loss = 0.000630
grad_step = 000164, loss = 0.000634
grad_step = 000165, loss = 0.000633
grad_step = 000166, loss = 0.000618
grad_step = 000167, loss = 0.000614
grad_step = 000168, loss = 0.000617
grad_step = 000169, loss = 0.000608
grad_step = 000170, loss = 0.000599
grad_step = 000171, loss = 0.000600
grad_step = 000172, loss = 0.000598
grad_step = 000173, loss = 0.000589
grad_step = 000174, loss = 0.000584
grad_step = 000175, loss = 0.000584
grad_step = 000176, loss = 0.000581
grad_step = 000177, loss = 0.000574
grad_step = 000178, loss = 0.000569
grad_step = 000179, loss = 0.000568
grad_step = 000180, loss = 0.000565
grad_step = 000181, loss = 0.000560
grad_step = 000182, loss = 0.000555
grad_step = 000183, loss = 0.000551
grad_step = 000184, loss = 0.000549
grad_step = 000185, loss = 0.000548
grad_step = 000186, loss = 0.000544
grad_step = 000187, loss = 0.000540
grad_step = 000188, loss = 0.000535
grad_step = 000189, loss = 0.000530
grad_step = 000190, loss = 0.000527
grad_step = 000191, loss = 0.000524
grad_step = 000192, loss = 0.000521
grad_step = 000193, loss = 0.000518
grad_step = 000194, loss = 0.000515
grad_step = 000195, loss = 0.000513
grad_step = 000196, loss = 0.000513
grad_step = 000197, loss = 0.000514
grad_step = 000198, loss = 0.000518
grad_step = 000199, loss = 0.000525
grad_step = 000200, loss = 0.000536
plot()
Saved image to .//n_beats_200.png.
grad_step = 000201, loss = 0.000543
grad_step = 000202, loss = 0.000538
grad_step = 000203, loss = 0.000516
grad_step = 000204, loss = 0.000491
grad_step = 000205, loss = 0.000480
grad_step = 000206, loss = 0.000486
grad_step = 000207, loss = 0.000498
grad_step = 000208, loss = 0.000503
grad_step = 000209, loss = 0.000495
grad_step = 000210, loss = 0.000478
grad_step = 000211, loss = 0.000465
grad_step = 000212, loss = 0.000462
grad_step = 000213, loss = 0.000467
grad_step = 000214, loss = 0.000473
grad_step = 000215, loss = 0.000474
grad_step = 000216, loss = 0.000469
grad_step = 000217, loss = 0.000460
grad_step = 000218, loss = 0.000450
grad_step = 000219, loss = 0.000443
grad_step = 000220, loss = 0.000441
grad_step = 000221, loss = 0.000442
grad_step = 000222, loss = 0.000445
grad_step = 000223, loss = 0.000447
grad_step = 000224, loss = 0.000449
grad_step = 000225, loss = 0.000449
grad_step = 000226, loss = 0.000447
grad_step = 000227, loss = 0.000443
grad_step = 000228, loss = 0.000436
grad_step = 000229, loss = 0.000428
grad_step = 000230, loss = 0.000422
grad_step = 000231, loss = 0.000416
grad_step = 000232, loss = 0.000412
grad_step = 000233, loss = 0.000408
grad_step = 000234, loss = 0.000406
grad_step = 000235, loss = 0.000405
grad_step = 000236, loss = 0.000404
grad_step = 000237, loss = 0.000404
grad_step = 000238, loss = 0.000409
grad_step = 000239, loss = 0.000421
grad_step = 000240, loss = 0.000454
grad_step = 000241, loss = 0.000516
grad_step = 000242, loss = 0.000604
grad_step = 000243, loss = 0.000612
grad_step = 000244, loss = 0.000506
grad_step = 000245, loss = 0.000395
grad_step = 000246, loss = 0.000424
grad_step = 000247, loss = 0.000498
grad_step = 000248, loss = 0.000462
grad_step = 000249, loss = 0.000388
grad_step = 000250, loss = 0.000403
grad_step = 000251, loss = 0.000448
grad_step = 000252, loss = 0.000417
grad_step = 000253, loss = 0.000374
grad_step = 000254, loss = 0.000398
grad_step = 000255, loss = 0.000420
grad_step = 000256, loss = 0.000387
grad_step = 000257, loss = 0.000367
grad_step = 000258, loss = 0.000390
grad_step = 000259, loss = 0.000395
grad_step = 000260, loss = 0.000370
grad_step = 000261, loss = 0.000362
grad_step = 000262, loss = 0.000378
grad_step = 000263, loss = 0.000379
grad_step = 000264, loss = 0.000361
grad_step = 000265, loss = 0.000355
grad_step = 000266, loss = 0.000364
grad_step = 000267, loss = 0.000366
grad_step = 000268, loss = 0.000356
grad_step = 000269, loss = 0.000348
grad_step = 000270, loss = 0.000351
grad_step = 000271, loss = 0.000354
grad_step = 000272, loss = 0.000351
grad_step = 000273, loss = 0.000344
grad_step = 000274, loss = 0.000341
grad_step = 000275, loss = 0.000342
grad_step = 000276, loss = 0.000343
grad_step = 000277, loss = 0.000342
grad_step = 000278, loss = 0.000340
grad_step = 000279, loss = 0.000335
grad_step = 000280, loss = 0.000331
grad_step = 000281, loss = 0.000330
grad_step = 000282, loss = 0.000331
grad_step = 000283, loss = 0.000333
grad_step = 000284, loss = 0.000332
grad_step = 000285, loss = 0.000330
grad_step = 000286, loss = 0.000327
grad_step = 000287, loss = 0.000325
grad_step = 000288, loss = 0.000323
grad_step = 000289, loss = 0.000321
grad_step = 000290, loss = 0.000318
grad_step = 000291, loss = 0.000316
grad_step = 000292, loss = 0.000316
grad_step = 000293, loss = 0.000315
grad_step = 000294, loss = 0.000315
grad_step = 000295, loss = 0.000314
grad_step = 000296, loss = 0.000315
grad_step = 000297, loss = 0.000318
grad_step = 000298, loss = 0.000325
grad_step = 000299, loss = 0.000338
grad_step = 000300, loss = 0.000365
plot()
Saved image to .//n_beats_300.png.
grad_step = 000301, loss = 0.000400
grad_step = 000302, loss = 0.000451
grad_step = 000303, loss = 0.000466
grad_step = 000304, loss = 0.000448
grad_step = 000305, loss = 0.000369
grad_step = 000306, loss = 0.000309
grad_step = 000307, loss = 0.000317
grad_step = 000308, loss = 0.000365
grad_step = 000309, loss = 0.000394
grad_step = 000310, loss = 0.000356
grad_step = 000311, loss = 0.000307
grad_step = 000312, loss = 0.000302
grad_step = 000313, loss = 0.000333
grad_step = 000314, loss = 0.000354
grad_step = 000315, loss = 0.000332
grad_step = 000316, loss = 0.000299
grad_step = 000317, loss = 0.000296
grad_step = 000318, loss = 0.000315
grad_step = 000319, loss = 0.000329
grad_step = 000320, loss = 0.000315
grad_step = 000321, loss = 0.000294
grad_step = 000322, loss = 0.000290
grad_step = 000323, loss = 0.000298
grad_step = 000324, loss = 0.000308
grad_step = 000325, loss = 0.000303
grad_step = 000326, loss = 0.000291
grad_step = 000327, loss = 0.000285
grad_step = 000328, loss = 0.000286
grad_step = 000329, loss = 0.000292
grad_step = 000330, loss = 0.000292
grad_step = 000331, loss = 0.000287
grad_step = 000332, loss = 0.000283
grad_step = 000333, loss = 0.000280
grad_step = 000334, loss = 0.000281
grad_step = 000335, loss = 0.000280
grad_step = 000336, loss = 0.000279
grad_step = 000337, loss = 0.000278
grad_step = 000338, loss = 0.000278
grad_step = 000339, loss = 0.000277
grad_step = 000340, loss = 0.000277
grad_step = 000341, loss = 0.000275
grad_step = 000342, loss = 0.000271
grad_step = 000343, loss = 0.000269
grad_step = 000344, loss = 0.000268
grad_step = 000345, loss = 0.000270
grad_step = 000346, loss = 0.000270
grad_step = 000347, loss = 0.000268
grad_step = 000348, loss = 0.000266
grad_step = 000349, loss = 0.000265
grad_step = 000350, loss = 0.000266
grad_step = 000351, loss = 0.000266
grad_step = 000352, loss = 0.000266
grad_step = 000353, loss = 0.000265
grad_step = 000354, loss = 0.000265
grad_step = 000355, loss = 0.000266
grad_step = 000356, loss = 0.000270
grad_step = 000357, loss = 0.000276
grad_step = 000358, loss = 0.000283
grad_step = 000359, loss = 0.000297
grad_step = 000360, loss = 0.000313
grad_step = 000361, loss = 0.000339
grad_step = 000362, loss = 0.000353
grad_step = 000363, loss = 0.000364
grad_step = 000364, loss = 0.000343
grad_step = 000365, loss = 0.000311
grad_step = 000366, loss = 0.000273
grad_step = 000367, loss = 0.000253
grad_step = 000368, loss = 0.000259
grad_step = 000369, loss = 0.000279
grad_step = 000370, loss = 0.000298
grad_step = 000371, loss = 0.000298
grad_step = 000372, loss = 0.000283
grad_step = 000373, loss = 0.000262
grad_step = 000374, loss = 0.000248
grad_step = 000375, loss = 0.000246
grad_step = 000376, loss = 0.000255
grad_step = 000377, loss = 0.000265
grad_step = 000378, loss = 0.000269
grad_step = 000379, loss = 0.000267
grad_step = 000380, loss = 0.000258
grad_step = 000381, loss = 0.000250
grad_step = 000382, loss = 0.000244
grad_step = 000383, loss = 0.000243
grad_step = 000384, loss = 0.000245
grad_step = 000385, loss = 0.000247
grad_step = 000386, loss = 0.000247
grad_step = 000387, loss = 0.000245
grad_step = 000388, loss = 0.000243
grad_step = 000389, loss = 0.000242
grad_step = 000390, loss = 0.000242
grad_step = 000391, loss = 0.000242
grad_step = 000392, loss = 0.000241
grad_step = 000393, loss = 0.000238
grad_step = 000394, loss = 0.000235
grad_step = 000395, loss = 0.000232
grad_step = 000396, loss = 0.000231
grad_step = 000397, loss = 0.000231
grad_step = 000398, loss = 0.000232
grad_step = 000399, loss = 0.000232
grad_step = 000400, loss = 0.000231
plot()
Saved image to .//n_beats_400.png.
grad_step = 000401, loss = 0.000230
grad_step = 000402, loss = 0.000228
grad_step = 000403, loss = 0.000227
grad_step = 000404, loss = 0.000227
grad_step = 000405, loss = 0.000228
grad_step = 000406, loss = 0.000231
grad_step = 000407, loss = 0.000239
grad_step = 000408, loss = 0.000255
grad_step = 000409, loss = 0.000284
grad_step = 000410, loss = 0.000341
grad_step = 000411, loss = 0.000417
grad_step = 000412, loss = 0.000529
grad_step = 000413, loss = 0.000559
grad_step = 000414, loss = 0.000503
grad_step = 000415, loss = 0.000326
grad_step = 000416, loss = 0.000241
grad_step = 000417, loss = 0.000305
grad_step = 000418, loss = 0.000388
grad_step = 000419, loss = 0.000364
grad_step = 000420, loss = 0.000250
grad_step = 000421, loss = 0.000242
grad_step = 000422, loss = 0.000322
grad_step = 000423, loss = 0.000317
grad_step = 000424, loss = 0.000243
grad_step = 000425, loss = 0.000228
grad_step = 000426, loss = 0.000280
grad_step = 000427, loss = 0.000285
grad_step = 000428, loss = 0.000232
grad_step = 000429, loss = 0.000223
grad_step = 000430, loss = 0.000258
grad_step = 000431, loss = 0.000259
grad_step = 000432, loss = 0.000227
grad_step = 000433, loss = 0.000219
grad_step = 000434, loss = 0.000236
grad_step = 000435, loss = 0.000242
grad_step = 000436, loss = 0.000224
grad_step = 000437, loss = 0.000215
grad_step = 000438, loss = 0.000224
grad_step = 000439, loss = 0.000229
grad_step = 000440, loss = 0.000220
grad_step = 000441, loss = 0.000211
grad_step = 000442, loss = 0.000215
grad_step = 000443, loss = 0.000220
grad_step = 000444, loss = 0.000216
grad_step = 000445, loss = 0.000209
grad_step = 000446, loss = 0.000209
grad_step = 000447, loss = 0.000213
grad_step = 000448, loss = 0.000213
grad_step = 000449, loss = 0.000208
grad_step = 000450, loss = 0.000205
grad_step = 000451, loss = 0.000207
grad_step = 000452, loss = 0.000208
grad_step = 000453, loss = 0.000207
grad_step = 000454, loss = 0.000203
grad_step = 000455, loss = 0.000202
grad_step = 000456, loss = 0.000204
grad_step = 000457, loss = 0.000204
grad_step = 000458, loss = 0.000202
grad_step = 000459, loss = 0.000200
grad_step = 000460, loss = 0.000199
grad_step = 000461, loss = 0.000200
grad_step = 000462, loss = 0.000200
grad_step = 000463, loss = 0.000199
grad_step = 000464, loss = 0.000197
grad_step = 000465, loss = 0.000196
grad_step = 000466, loss = 0.000196
grad_step = 000467, loss = 0.000197
grad_step = 000468, loss = 0.000196
grad_step = 000469, loss = 0.000195
grad_step = 000470, loss = 0.000194
grad_step = 000471, loss = 0.000194
grad_step = 000472, loss = 0.000194
grad_step = 000473, loss = 0.000193
grad_step = 000474, loss = 0.000193
grad_step = 000475, loss = 0.000192
grad_step = 000476, loss = 0.000191
grad_step = 000477, loss = 0.000191
grad_step = 000478, loss = 0.000191
grad_step = 000479, loss = 0.000190
grad_step = 000480, loss = 0.000190
grad_step = 000481, loss = 0.000189
grad_step = 000482, loss = 0.000189
grad_step = 000483, loss = 0.000188
grad_step = 000484, loss = 0.000188
grad_step = 000485, loss = 0.000187
grad_step = 000486, loss = 0.000187
grad_step = 000487, loss = 0.000187
grad_step = 000488, loss = 0.000186
grad_step = 000489, loss = 0.000186
grad_step = 000490, loss = 0.000186
grad_step = 000491, loss = 0.000185
grad_step = 000492, loss = 0.000185
grad_step = 000493, loss = 0.000185
grad_step = 000494, loss = 0.000185
grad_step = 000495, loss = 0.000187
grad_step = 000496, loss = 0.000190
grad_step = 000497, loss = 0.000196
grad_step = 000498, loss = 0.000209
grad_step = 000499, loss = 0.000228
grad_step = 000500, loss = 0.000263
plot()
Saved image to .//n_beats_500.png.
grad_step = 000501, loss = 0.000304
Finished.

  #### Predict    ############################################# 
   milk_production_pounds
0                     589
1                     561
2                     640
3                     656
4                     727
[[0.60784314]
 [0.57894737]
 [0.66047472]
 [0.67698658]
 [0.750258  ]
 [0.71929825]
 [0.66047472]
 [0.61816305]
 [0.58617131]
 [0.59545924]
 [0.57069143]
 [0.6006192 ]
 [0.61919505]
 [0.58410733]
 [0.67389061]
 [0.69453044]
 [0.76573787]
 [0.73890609]
 [0.68111455]
 [0.63673891]
 [0.60165119]
 [0.60577915]
 [0.58307534]
 [0.61713106]
 [0.64809082]
 [0.6377709 ]
 [0.71001032]
 [0.72755418]
 [0.79463364]
 [0.75954592]
 [0.6996904 ]
 [0.65944272]
 [0.62332301]
 [0.63054696]
 [0.6130031 ]
 [0.65428277]
 [0.67905057]
 [0.64189886]
 [0.73168215]
 [0.74509804]
 [0.80701754]
 [0.78018576]
 [0.7244582 ]
 [0.67389061]
 [0.63467492]
 [0.64086687]
 [0.62125903]
 [0.65531476]
 [0.69865841]
 [0.65531476]
 [0.75954592]
 [0.77915377]
 [0.8369453 ]
 [0.82352941]
 [0.75851393]
 [0.71929825]
 [0.68214654]
 [0.68833849]
 [0.66563467]
 [0.71001032]
 [0.73581011]
 [0.68833849]
 [0.78637771]
 [0.80908153]
 [0.86377709]
 [0.84313725]
 [0.79153767]
 [0.74509804]
 [0.70278638]
 [0.70897833]
 [0.68111455]
 [0.72033024]
 [0.73993808]
 [0.71826625]
 [0.7997936 ]
 [0.82146543]
 [0.88544892]
 [0.85242518]
 [0.80804954]
 [0.76367389]
 [0.72342621]
 [0.72858617]
 [0.69865841]
 [0.73374613]
 [0.75748194]
 [0.7120743 ]
 [0.81011352]
 [0.83075335]
 [0.89886481]
 [0.87203302]
 [0.82662539]
 [0.78844169]
 [0.74819401]
 [0.74613003]
 [0.7120743 ]
 [0.75748194]
 [0.77399381]
 [0.72961816]
 [0.83281734]
 [0.8503612 ]
 [0.91434469]
 [0.88648091]
 [0.84520124]
 [0.80804954]
 [0.76367389]
 [0.77089783]
 [0.73374613]
 [0.7750258 ]
 [0.82972136]
 [0.78018576]
 [0.8875129 ]
 [0.90608875]
 [0.97213622]
 [0.94220846]
 [0.89680083]
 [0.86068111]
 [0.81527348]
 [0.8255934 ]
 [0.7874097 ]
 [0.8255934 ]
 [0.85242518]
 [0.8245614 ]
 [0.91847265]
 [0.92879257]
 [0.99174407]
 [0.96491228]
 [0.92260062]
 [0.88235294]
 [0.83488132]
 [0.83591331]
 [0.79050568]
 [0.83075335]
 [0.84726522]
 [0.79772962]
 [0.91124871]
 [0.92672859]
 [0.9876161 ]
 [0.95356037]
 [0.90918473]
 [0.86377709]
 [0.80908153]
 [0.81630547]
 [0.78431373]
 [0.82765738]
 [0.85448916]
 [0.80288958]
 [0.91744066]
 [0.93085655]
 [1.        ]
 [0.97729618]
 [0.9370485 ]
 [0.89473684]
 [0.84107327]
 [0.8379773 ]
 [0.79772962]
 [0.83900929]
 [0.86068111]
 [0.80701754]
 [0.92053664]
 [0.93188854]
 [0.99690402]
 [0.96697626]
 [0.9246646 ]
 [0.88544892]
 [0.84313725]
 [0.85345717]
 [0.82249742]
 [0.86996904]]
[[0.8425652  0.8425523  0.8999631  0.9364637  1.0131253 ]
 [0.8395136  0.9102174  0.9289285  1.0091286  0.98027265]
 [0.8728747  0.92080206 0.97505224 0.98141855 0.94808257]
 [0.911834   0.97976524 0.96199715 0.9358308  0.9167052 ]
 [0.9865116  0.9710516  0.93818057 0.91770303 0.8616815 ]
 [0.9619702  0.9281408  0.89026415 0.8503069  0.8631586 ]
 [0.916352   0.88750434 0.8119629  0.8398177  0.79927015]
 [0.87396085 0.8297536  0.8286616  0.80754876 0.8466264 ]
 [0.81578434 0.8217494  0.78402895 0.8290369  0.8655702 ]
 [0.8076485  0.791017   0.81072664 0.8504289  0.814138  ]
 [0.79707116 0.80710566 0.83025634 0.8210689  0.91776365]
 [0.81602633 0.8487209  0.8110359  0.89989686 0.95136   ]
 [0.8334203  0.8417048  0.9007692  0.9390674  1.009282  ]
 [0.8343449  0.91725624 0.9314161  1.0119948  0.9699652 ]
 [0.8910651  0.932507   0.9806397  0.9690721  0.9320549 ]
 [0.92316926 0.98856443 0.9571025  0.9205444  0.8973597 ]
 [0.9877532  0.9693579  0.9195589  0.89545685 0.8367966 ]
 [0.958603   0.912857   0.87374747 0.82976305 0.84741336]
 [0.9173588  0.88539547 0.8036073  0.8316976  0.7967385 ]
 [0.8825117  0.8334283  0.8263026  0.8084328  0.84485537]
 [0.83041465 0.83401716 0.78792703 0.8318604  0.87444943]
 [0.8276602  0.8041645  0.81795764 0.8601527  0.82213295]
 [0.8113011  0.8188117  0.8400502  0.82944727 0.9227717 ]
 [0.82214457 0.8555927  0.8158099  0.9033608  0.95029587]
 [0.85065573 0.8460858  0.90045077 0.936758   1.0215671 ]
 [0.84783787 0.91632295 0.9338683  1.0154662  0.9907094 ]
 [0.8801481  0.931964   0.98441374 0.99302393 0.95825756]
 [0.9240368  0.99399626 0.9776073  0.94878894 0.9287647 ]
 [0.99724495 0.9873383  0.95310295 0.9283405  0.8679078 ]
 [0.97360337 0.93814415 0.9016598  0.8573451  0.8686832 ]
 [0.92590195 0.8963748  0.81870526 0.84492624 0.8075226 ]]

  #### Plot     ############################################### 
Saved image to ztest/model_tch/nbeats//n_beats_test.png.

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Already up to date.
[master 5ef3aeb] ml_store
 1 file changed, 1123 insertions(+)
To github.com:arita37/mlmodels_store.git
   6206e6a..5ef3aeb  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//transformer_classifier.py 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//transformer_classifier.py", line 522, in <module>
    model_pars, data_pars, compute_pars, out_pars = get_params(param_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//transformer_classifier.py", line 418, in get_params
    cf = json.load(open(data_path, mode='r'))
FileNotFoundError: [Errno 2] No such file or directory: 'model_tch/transformer_classifier.json'

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Already up to date.
[master 5fa97af] ml_store
 1 file changed, 38 insertions(+)
To github.com:arita37/mlmodels_store.git
   5ef3aeb..5fa97af  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//matchzoo_models.py 

  #### Loading params   ############################################## 

  {'dataset': 'WIKI_QA', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/nlp/', 'dataset_pars': {'data_pack': '', 'mode': 'pair', 'num_dup': 2, 'num_neg': 1, 'batch_size': 20, 'resample': True, 'sort': False, 'callbacks': 'PADDING'}, 'dataloader': '', 'dataloader_pars': {'device': 'cpu', 'dataset': 'None', 'stage': 'train', 'callback': 'PADDING'}, 'preprocess': {'train': {'transform': True, 'mode': 'pair', 'num_dup': 2, 'num_neg': 1, 'batch_size': 20, 'stage': 'train', 'resample': True, 'sort': False, 'dataloader_callback': 'PADDING'}, 'test': {'transform': True, 'batch_size': 20, 'stage': 'dev', 'dataloader_callback': 'PADDING'}}} {'checkpointdir': 'ztest/model_tch/MATCHZOO/BERT/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/MATCHZOO/BERT/'} 

  #### Loading dataset   ############################################# 

  #### Model init   ################################################## 
  0%|          | 0/231508 [00:00<?, ?B/s]100%|██████████| 231508/231508 [00:00<00:00, 19521419.56B/s]
  0%|          | 0/433 [00:00<?, ?B/s]100%|██████████| 433/433 [00:00<00:00, 325064.19B/s]
  0%|          | 0/440473133 [00:00<?, ?B/s]  1%|          | 2570240/440473133 [00:00<00:17, 25699422.17B/s]  1%|▏         | 6347776/440473133 [00:00<00:15, 28424886.99B/s]  3%|▎         | 12043264/440473133 [00:00<00:12, 33451915.10B/s]  4%|▍         | 18017280/440473133 [00:00<00:10, 38537715.57B/s]  5%|▌         | 22036480/440473133 [00:00<00:10, 39018206.55B/s]  6%|▌         | 26938368/440473133 [00:00<00:09, 41561718.30B/s]  8%|▊         | 33489920/440473133 [00:00<00:08, 46681128.27B/s]  9%|▉         | 40074240/440473133 [00:00<00:07, 51143936.76B/s] 11%|█         | 46629888/440473133 [00:00<00:07, 54755291.43B/s] 12%|█▏        | 53016576/440473133 [00:01<00:06, 57202313.59B/s] 14%|█▎        | 59640832/440473133 [00:01<00:06, 59641223.07B/s] 15%|█▌        | 66282496/440473133 [00:01<00:06, 61522013.27B/s] 17%|█▋        | 72910848/440473133 [00:01<00:05, 62874511.23B/s] 18%|█▊        | 79304704/440473133 [00:01<00:05, 62900993.21B/s] 19%|█▉        | 85668864/440473133 [00:01<00:05, 61134748.24B/s] 21%|██        | 92279808/440473133 [00:01<00:05, 62542428.23B/s] 22%|██▏       | 98972672/440473133 [00:01<00:05, 63795515.50B/s] 24%|██▍       | 105637888/440473133 [00:01<00:05, 64625763.87B/s] 25%|██▌       | 112245760/440473133 [00:01<00:05, 65054732.17B/s] 27%|██▋       | 118774784/440473133 [00:02<00:05, 64134231.57B/s] 28%|██▊       | 125413376/440473133 [00:02<00:04, 64791788.95B/s] 30%|██▉       | 132060160/440473133 [00:02<00:04, 65284487.19B/s] 32%|███▏      | 138754048/440473133 [00:02<00:04, 65771525.72B/s] 33%|███▎      | 145463296/440473133 [00:02<00:04, 66162103.27B/s] 35%|███▍      | 152086528/440473133 [00:02<00:08, 32496095.37B/s] 36%|███▌      | 158707712/440473133 [00:02<00:07, 38355085.18B/s] 38%|███▊      | 165307392/440473133 [00:03<00:06, 43866448.63B/s] 39%|███▉      | 171955200/440473133 [00:03<00:05, 48850316.63B/s] 41%|████      | 178564096/440473133 [00:03<00:04, 52996453.45B/s] 42%|████▏     | 185205760/440473133 [00:03<00:04, 56416184.04B/s] 44%|████▎     | 191802368/440473133 [00:03<00:04, 58976974.46B/s] 45%|████▌     | 198380544/440473133 [00:03<00:03, 60863894.89B/s] 47%|████▋     | 205006848/440473133 [00:03<00:03, 62380722.27B/s] 48%|████▊     | 211603456/440473133 [00:03<00:03, 63409906.45B/s] 50%|████▉     | 218215424/440473133 [00:03<00:03, 64198486.71B/s] 51%|█████     | 224798720/440473133 [00:03<00:03, 64676261.52B/s] 53%|█████▎    | 231368704/440473133 [00:04<00:03, 63599162.39B/s] 54%|█████▍    | 237906944/440473133 [00:04<00:03, 64122189.56B/s] 56%|█████▌    | 244512768/440473133 [00:04<00:03, 64688645.06B/s] 57%|█████▋    | 251086848/440473133 [00:04<00:02, 64997355.10B/s] 59%|█████▊    | 257683456/440473133 [00:04<00:02, 65282494.97B/s] 60%|█████▉    | 264231936/440473133 [00:04<00:02, 64393169.86B/s] 61%|██████▏   | 270756864/440473133 [00:04<00:02, 64642888.81B/s] 63%|██████▎   | 277405696/440473133 [00:04<00:02, 65182261.52B/s] 64%|██████▍   | 284077056/440473133 [00:04<00:02, 65633556.03B/s] 66%|██████▌   | 290699264/440473133 [00:04<00:02, 65808095.12B/s] 68%|██████▊   | 297369600/440473133 [00:05<00:02, 66072568.13B/s] 69%|██████▉   | 303981568/440473133 [00:05<00:02, 65176258.00B/s] 71%|███████   | 310562816/440473133 [00:05<00:01, 65363758.26B/s] 72%|███████▏  | 317104128/440473133 [00:05<00:01, 65032457.55B/s] 74%|███████▎  | 323781632/440473133 [00:05<00:01, 65542312.41B/s] 75%|███████▌  | 330437632/440473133 [00:05<00:01, 65843189.91B/s] 77%|███████▋  | 337148928/440473133 [00:05<00:01, 66218037.71B/s] 78%|███████▊  | 343790592/440473133 [00:05<00:01, 66277181.35B/s] 80%|███████▉  | 350450688/440473133 [00:05<00:01, 66373955.53B/s] 81%|████████  | 357089280/440473133 [00:05<00:01, 65661023.47B/s] 83%|████████▎ | 363658240/440473133 [00:06<00:01, 64360566.38B/s] 84%|████████▍ | 370285568/440473133 [00:06<00:01, 64921067.21B/s] 86%|████████▌ | 376784896/440473133 [00:06<00:00, 64689373.40B/s] 87%|████████▋ | 383473664/440473133 [00:06<00:00, 65332419.22B/s] 89%|████████▊ | 390153216/440473133 [00:06<00:00, 65763620.83B/s] 90%|█████████ | 396755968/440473133 [00:06<00:00, 65841178.76B/s] 92%|█████████▏| 403343360/440473133 [00:06<00:00, 64625813.75B/s] 93%|█████████▎| 410007552/440473133 [00:06<00:00, 65215364.32B/s] 95%|█████████▍| 416722944/440473133 [00:06<00:00, 65782698.19B/s] 96%|█████████▌| 423439360/440473133 [00:07<00:00, 66188958.46B/s] 98%|█████████▊| 430063616/440473133 [00:07<00:00, 66161962.16B/s] 99%|█████████▉| 436727808/440473133 [00:07<00:00, 66303778.19B/s]100%|██████████| 440473133/440473133 [00:07<00:00, 60685782.84B/s]Downloading data from https://download.microsoft.com/download/E/5/F/E5FCFCEE-7005-4814-853D-DAA7C66507E0/WikiQACorpus.zip

   8192/7094233 [..............................] - ETA: 0s
1130496/7094233 [===>..........................] - ETA: 0s
2170880/7094233 [========>.....................] - ETA: 0s
3211264/7094233 [============>.................] - ETA: 0s
4251648/7094233 [================>.............] - ETA: 0s
5021696/7094233 [====================>.........] - ETA: 0s
6324224/7094233 [=========================>....] - ETA: 0s
7094272/7094233 [==============================] - 1s 0us/step

Processing text_left with encode:   0%|          | 0/2118 [00:00<?, ?it/s]Processing text_left with encode:   0%|          | 2/2118 [00:00<02:33, 13.80it/s]Processing text_left with encode:  20%|██        | 426/2118 [00:00<01:25, 19.69it/s]Processing text_left with encode:  40%|████      | 849/2118 [00:00<00:45, 28.07it/s]Processing text_left with encode:  56%|█████▌    | 1180/2118 [00:00<00:23, 39.96it/s]Processing text_left with encode:  76%|███████▋  | 1615/2118 [00:00<00:08, 56.86it/s]Processing text_left with encode:  97%|█████████▋| 2057/2118 [00:00<00:00, 80.78it/s]Processing text_left with encode: 100%|██████████| 2118/2118 [00:00<00:00, 3206.26it/s]
Processing text_right with encode:   0%|          | 0/18841 [00:00<?, ?it/s]Processing text_right with encode:   1%|          | 150/18841 [00:00<00:16, 1141.76it/s]Processing text_right with encode:   2%|▏         | 316/18841 [00:00<00:14, 1258.45it/s]Processing text_right with encode:   3%|▎         | 477/18841 [00:00<00:13, 1346.47it/s]Processing text_right with encode:   3%|▎         | 649/18841 [00:00<00:12, 1439.75it/s]Processing text_right with encode:   4%|▍         | 807/18841 [00:00<00:12, 1476.53it/s]Processing text_right with encode:   5%|▌         | 965/18841 [00:00<00:11, 1501.02it/s]Processing text_right with encode:   6%|▌         | 1120/18841 [00:00<00:11, 1512.24it/s]Processing text_right with encode:   7%|▋         | 1276/18841 [00:00<00:11, 1525.43it/s]Processing text_right with encode:   8%|▊         | 1425/18841 [00:00<00:11, 1511.62it/s]Processing text_right with encode:   8%|▊         | 1587/18841 [00:01<00:11, 1542.09it/s]Processing text_right with encode:   9%|▉         | 1755/18841 [00:01<00:10, 1579.26it/s]Processing text_right with encode:  10%|█         | 1912/18841 [00:01<00:10, 1562.95it/s]Processing text_right with encode:  11%|█         | 2068/18841 [00:01<00:10, 1551.31it/s]Processing text_right with encode:  12%|█▏        | 2238/18841 [00:01<00:10, 1590.04it/s]Processing text_right with encode:  13%|█▎        | 2398/18841 [00:01<00:10, 1591.15it/s]Processing text_right with encode:  14%|█▎        | 2562/18841 [00:01<00:10, 1604.90it/s]Processing text_right with encode:  14%|█▍        | 2724/18841 [00:01<00:10, 1606.50it/s]Processing text_right with encode:  15%|█▌        | 2902/18841 [00:01<00:09, 1650.72it/s]Processing text_right with encode:  16%|█▋        | 3068/18841 [00:01<00:09, 1604.34it/s]Processing text_right with encode:  17%|█▋        | 3229/18841 [00:02<00:09, 1591.99it/s]Processing text_right with encode:  18%|█▊        | 3389/18841 [00:02<00:09, 1585.10it/s]Processing text_right with encode:  19%|█▉        | 3548/18841 [00:02<00:09, 1559.09it/s]Processing text_right with encode:  20%|█▉        | 3705/18841 [00:02<00:09, 1558.17it/s]Processing text_right with encode:  21%|██        | 3868/18841 [00:02<00:09, 1578.94it/s]Processing text_right with encode:  21%|██▏       | 4035/18841 [00:02<00:09, 1602.54it/s]Processing text_right with encode:  22%|██▏       | 4196/18841 [00:02<00:09, 1576.89it/s]Processing text_right with encode:  23%|██▎       | 4354/18841 [00:02<00:09, 1574.09it/s]Processing text_right with encode:  24%|██▍       | 4512/18841 [00:02<00:09, 1565.46it/s]Processing text_right with encode:  25%|██▍       | 4669/18841 [00:02<00:09, 1551.91it/s]Processing text_right with encode:  26%|██▌       | 4840/18841 [00:03<00:08, 1595.13it/s]Processing text_right with encode:  27%|██▋       | 5002/18841 [00:03<00:08, 1601.61it/s]Processing text_right with encode:  27%|██▋       | 5173/18841 [00:03<00:08, 1631.71it/s]Processing text_right with encode:  28%|██▊       | 5344/18841 [00:03<00:08, 1651.25it/s]Processing text_right with encode:  29%|██▉       | 5512/18841 [00:03<00:08, 1656.66it/s]Processing text_right with encode:  30%|███       | 5678/18841 [00:03<00:08, 1621.09it/s]Processing text_right with encode:  31%|███       | 5841/18841 [00:03<00:08, 1621.79it/s]Processing text_right with encode:  32%|███▏      | 6004/18841 [00:03<00:07, 1611.69it/s]Processing text_right with encode:  33%|███▎      | 6166/18841 [00:03<00:07, 1601.11it/s]Processing text_right with encode:  34%|███▎      | 6327/18841 [00:03<00:07, 1578.73it/s]Processing text_right with encode:  34%|███▍      | 6495/18841 [00:04<00:07, 1606.19it/s]Processing text_right with encode:  35%|███▌      | 6662/18841 [00:04<00:07, 1623.45it/s]Processing text_right with encode:  36%|███▌      | 6825/18841 [00:04<00:07, 1613.66it/s]Processing text_right with encode:  37%|███▋      | 6987/18841 [00:04<00:07, 1593.27it/s]Processing text_right with encode:  38%|███▊      | 7147/18841 [00:04<00:07, 1588.37it/s]Processing text_right with encode:  39%|███▉      | 7311/18841 [00:04<00:07, 1602.06it/s]Processing text_right with encode:  40%|███▉      | 7482/18841 [00:04<00:06, 1630.99it/s]Processing text_right with encode:  41%|████      | 7646/18841 [00:04<00:06, 1608.44it/s]Processing text_right with encode:  41%|████▏     | 7808/18841 [00:04<00:06, 1605.47it/s]Processing text_right with encode:  42%|████▏     | 7969/18841 [00:05<00:06, 1597.00it/s]Processing text_right with encode:  43%|████▎     | 8131/18841 [00:05<00:06, 1603.68it/s]Processing text_right with encode:  44%|████▍     | 8297/18841 [00:05<00:06, 1617.39it/s]Processing text_right with encode:  45%|████▍     | 8459/18841 [00:05<00:06, 1612.26it/s]Processing text_right with encode:  46%|████▌     | 8621/18841 [00:05<00:06, 1597.75it/s]Processing text_right with encode:  47%|████▋     | 8791/18841 [00:05<00:06, 1626.73it/s]Processing text_right with encode:  48%|████▊     | 8954/18841 [00:05<00:06, 1598.77it/s]Processing text_right with encode:  48%|████▊     | 9115/18841 [00:05<00:06, 1591.08it/s]Processing text_right with encode:  49%|████▉     | 9278/18841 [00:05<00:05, 1601.80it/s]Processing text_right with encode:  50%|█████     | 9439/18841 [00:05<00:05, 1589.58it/s]Processing text_right with encode:  51%|█████     | 9606/18841 [00:06<00:05, 1612.49it/s]Processing text_right with encode:  52%|█████▏    | 9768/18841 [00:06<00:05, 1554.48it/s]Processing text_right with encode:  53%|█████▎    | 9925/18841 [00:06<00:05, 1542.16it/s]Processing text_right with encode:  54%|█████▎    | 10095/18841 [00:06<00:05, 1585.96it/s]Processing text_right with encode:  54%|█████▍    | 10255/18841 [00:06<00:05, 1569.69it/s]Processing text_right with encode:  55%|█████▌    | 10445/18841 [00:06<00:05, 1651.19it/s]Processing text_right with encode:  56%|█████▋    | 10612/18841 [00:06<00:05, 1626.47it/s]Processing text_right with encode:  57%|█████▋    | 10776/18841 [00:06<00:04, 1623.35it/s]Processing text_right with encode:  58%|█████▊    | 10940/18841 [00:06<00:04, 1615.01it/s]Processing text_right with encode:  59%|█████▉    | 11103/18841 [00:06<00:04, 1579.52it/s]Processing text_right with encode:  60%|█████▉    | 11262/18841 [00:07<00:04, 1579.35it/s]Processing text_right with encode:  61%|██████    | 11421/18841 [00:07<00:04, 1572.51it/s]Processing text_right with encode:  61%|██████▏   | 11580/18841 [00:07<00:04, 1576.74it/s]Processing text_right with encode:  62%|██████▏   | 11742/18841 [00:07<00:04, 1585.85it/s]Processing text_right with encode:  63%|██████▎   | 11905/18841 [00:07<00:04, 1596.81it/s]Processing text_right with encode:  64%|██████▍   | 12071/18841 [00:07<00:04, 1611.33it/s]Processing text_right with encode:  65%|██████▍   | 12233/18841 [00:07<00:04, 1605.64it/s]Processing text_right with encode:  66%|██████▌   | 12394/18841 [00:07<00:04, 1587.98it/s]Processing text_right with encode:  67%|██████▋   | 12553/18841 [00:07<00:03, 1576.07it/s]Processing text_right with encode:  67%|██████▋   | 12715/18841 [00:07<00:03, 1586.79it/s]Processing text_right with encode:  68%|██████▊   | 12876/18841 [00:08<00:03, 1591.16it/s]Processing text_right with encode:  69%|██████▉   | 13039/18841 [00:08<00:03, 1601.36it/s]Processing text_right with encode:  70%|███████   | 13200/18841 [00:08<00:03, 1587.84it/s]Processing text_right with encode:  71%|███████   | 13367/18841 [00:08<00:03, 1610.59it/s]Processing text_right with encode:  72%|███████▏  | 13530/18841 [00:08<00:03, 1614.42it/s]Processing text_right with encode:  73%|███████▎  | 13696/18841 [00:08<00:03, 1627.50it/s]Processing text_right with encode:  74%|███████▎  | 13861/18841 [00:08<00:03, 1632.54it/s]Processing text_right with encode:  74%|███████▍  | 14028/18841 [00:08<00:02, 1643.33it/s]Processing text_right with encode:  75%|███████▌  | 14193/18841 [00:08<00:02, 1606.75it/s]Processing text_right with encode:  76%|███████▌  | 14354/18841 [00:09<00:02, 1596.28it/s]Processing text_right with encode:  77%|███████▋  | 14514/18841 [00:09<00:02, 1592.47it/s]Processing text_right with encode:  78%|███████▊  | 14692/18841 [00:09<00:02, 1643.22it/s]Processing text_right with encode:  79%|███████▉  | 14858/18841 [00:09<00:02, 1644.26it/s]Processing text_right with encode:  80%|███████▉  | 15023/18841 [00:09<00:02, 1617.63it/s]Processing text_right with encode:  81%|████████  | 15186/18841 [00:09<00:02, 1617.60it/s]Processing text_right with encode:  81%|████████▏ | 15348/18841 [00:09<00:02, 1611.80it/s]Processing text_right with encode:  82%|████████▏ | 15512/18841 [00:09<00:02, 1618.84it/s]Processing text_right with encode:  83%|████████▎ | 15677/18841 [00:09<00:01, 1626.14it/s]Processing text_right with encode:  84%|████████▍ | 15840/18841 [00:09<00:01, 1605.20it/s]Processing text_right with encode:  85%|████████▍ | 16001/18841 [00:10<00:01, 1594.92it/s]Processing text_right with encode:  86%|████████▌ | 16161/18841 [00:10<00:01, 1579.25it/s]Processing text_right with encode:  87%|████████▋ | 16320/18841 [00:10<00:01, 1575.35it/s]Processing text_right with encode:  88%|████████▊ | 16486/18841 [00:10<00:01, 1599.56it/s]Processing text_right with encode:  88%|████████▊ | 16647/18841 [00:10<00:01, 1578.24it/s]Processing text_right with encode:  89%|████████▉ | 16814/18841 [00:10<00:01, 1601.82it/s]Processing text_right with encode:  90%|█████████ | 16975/18841 [00:10<00:01, 1551.40it/s]Processing text_right with encode:  91%|█████████ | 17135/18841 [00:10<00:01, 1564.77it/s]Processing text_right with encode:  92%|█████████▏| 17292/18841 [00:10<00:00, 1552.77it/s]Processing text_right with encode:  93%|█████████▎| 17452/18841 [00:10<00:00, 1565.67it/s]Processing text_right with encode:  93%|█████████▎| 17615/18841 [00:11<00:00, 1582.05it/s]Processing text_right with encode:  94%|█████████▍| 17781/18841 [00:11<00:00, 1603.43it/s]Processing text_right with encode:  95%|█████████▌| 17942/18841 [00:11<00:00, 1590.53it/s]Processing text_right with encode:  96%|█████████▌| 18131/18841 [00:11<00:00, 1668.74it/s]Processing text_right with encode:  97%|█████████▋| 18300/18841 [00:11<00:00, 1621.50it/s]Processing text_right with encode:  98%|█████████▊| 18476/18841 [00:11<00:00, 1658.26it/s]Processing text_right with encode:  99%|█████████▉| 18646/18841 [00:11<00:00, 1665.90it/s]Processing text_right with encode: 100%|█████████▉| 18814/18841 [00:11<00:00, 1645.48it/s]Processing text_right with encode: 100%|██████████| 18841/18841 [00:11<00:00, 1598.04it/s]
Processing length_left with len:   0%|          | 0/2118 [00:00<?, ?it/s]Processing length_left with len: 100%|██████████| 2118/2118 [00:00<00:00, 490504.99it/s]
Processing length_right with len:   0%|          | 0/18841 [00:00<?, ?it/s]Processing length_right with len: 100%|██████████| 18841/18841 [00:00<00:00, 748497.62it/s]
Processing text_left with encode:   0%|          | 0/633 [00:00<?, ?it/s]Processing text_left with encode:  69%|██████▊   | 435/633 [00:00<00:00, 4341.92it/s]Processing text_left with encode: 100%|██████████| 633/633 [00:00<00:00, 4312.03it/s]
Processing text_right with encode:   0%|          | 0/5961 [00:00<?, ?it/s]Processing text_right with encode:   3%|▎         | 170/5961 [00:00<00:03, 1686.38it/s]Processing text_right with encode:   6%|▌         | 337/5961 [00:00<00:03, 1677.86it/s]Processing text_right with encode:   8%|▊         | 488/5961 [00:00<00:03, 1620.41it/s]Processing text_right with encode:  11%|█         | 656/5961 [00:00<00:03, 1637.39it/s]Processing text_right with encode:  14%|█▎        | 819/5961 [00:00<00:03, 1634.70it/s]Processing text_right with encode:  17%|█▋        | 988/5961 [00:00<00:03, 1647.88it/s]Processing text_right with encode:  19%|█▉        | 1156/5961 [00:00<00:02, 1656.48it/s]Processing text_right with encode:  22%|██▏       | 1324/5961 [00:00<00:02, 1657.61it/s]Processing text_right with encode:  25%|██▍       | 1489/5961 [00:00<00:02, 1650.99it/s]Processing text_right with encode:  28%|██▊       | 1648/5961 [00:01<00:02, 1622.38it/s]Processing text_right with encode:  30%|███       | 1806/5961 [00:01<00:02, 1572.77it/s]Processing text_right with encode:  33%|███▎      | 1968/5961 [00:01<00:02, 1585.48it/s]Processing text_right with encode:  36%|███▌      | 2137/5961 [00:01<00:02, 1613.49it/s]Processing text_right with encode:  39%|███▊      | 2298/5961 [00:01<00:02, 1585.75it/s]Processing text_right with encode:  41%|████      | 2456/5961 [00:01<00:02, 1549.02it/s]Processing text_right with encode:  44%|████▍     | 2626/5961 [00:01<00:02, 1591.23it/s]Processing text_right with encode:  47%|████▋     | 2812/5961 [00:01<00:01, 1661.90it/s]Processing text_right with encode:  50%|████▉     | 2980/5961 [00:01<00:01, 1654.97it/s]Processing text_right with encode:  53%|█████▎    | 3152/5961 [00:01<00:01, 1673.03it/s]Processing text_right with encode:  56%|█████▌    | 3320/5961 [00:02<00:01, 1648.56it/s]Processing text_right with encode:  58%|█████▊    | 3486/5961 [00:02<00:01, 1614.97it/s]Processing text_right with encode:  61%|██████▏   | 3660/5961 [00:02<00:01, 1648.17it/s]Processing text_right with encode:  64%|██████▍   | 3826/5961 [00:02<00:01, 1611.33it/s]Processing text_right with encode:  67%|██████▋   | 4003/5961 [00:02<00:01, 1652.83it/s]Processing text_right with encode:  70%|███████   | 4176/5961 [00:02<00:01, 1673.94it/s]Processing text_right with encode:  73%|███████▎  | 4344/5961 [00:02<00:00, 1657.66it/s]Processing text_right with encode:  76%|███████▌  | 4511/5961 [00:02<00:00, 1645.59it/s]Processing text_right with encode:  78%|███████▊  | 4676/5961 [00:02<00:00, 1639.65it/s]Processing text_right with encode:  81%|████████  | 4841/5961 [00:02<00:00, 1608.08it/s]Processing text_right with encode:  84%|████████▍ | 5003/5961 [00:03<00:00, 1578.49it/s]Processing text_right with encode:  87%|████████▋ | 5169/5961 [00:03<00:00, 1601.50it/s]Processing text_right with encode:  89%|████████▉ | 5330/5961 [00:03<00:00, 1599.34it/s]Processing text_right with encode:  92%|█████████▏| 5491/5961 [00:03<00:00, 1590.58it/s]Processing text_right with encode:  95%|█████████▍| 5651/5961 [00:03<00:00, 1562.32it/s]Processing text_right with encode:  97%|█████████▋| 5808/5961 [00:03<00:00, 1548.87it/s]Processing text_right with encode: 100%|██████████| 5961/5961 [00:03<00:00, 1623.15it/s]
Processing length_left with len:   0%|          | 0/633 [00:00<?, ?it/s]Processing length_left with len: 100%|██████████| 633/633 [00:00<00:00, 462300.96it/s]
Processing length_right with len:   0%|          | 0/5961 [00:00<?, ?it/s]Processing length_right with len: 100%|██████████| 5961/5961 [00:00<00:00, 708018.18it/s]
  #### Model  fit   ############################################# 

  0%|          | 0/102 [00:00<?, ?it/s]Epoch 1/1:   0%|          | 0/102 [00:20<?, ?it/s]Epoch 1/1:   0%|          | 0/102 [00:20<?, ?it/s, loss=1.009]Epoch 1/1:   1%|          | 1/102 [00:20<34:55, 20.75s/it, loss=1.009]Epoch 1/1:   1%|          | 1/102 [02:00<34:55, 20.75s/it, loss=1.009]Epoch 1/1:   1%|          | 1/102 [02:00<34:55, 20.75s/it, loss=0.942]Epoch 1/1:   2%|▏         | 2/102 [02:00<1:14:15, 44.56s/it, loss=0.942]Epoch 1/1:   2%|▏         | 2/102 [02:56<1:14:15, 44.56s/it, loss=0.942]Epoch 1/1:   2%|▏         | 2/102 [02:56<1:14:15, 44.56s/it, loss=1.039]Epoch 1/1:   3%|▎         | 3/102 [02:56<1:18:51, 47.79s/it, loss=1.039]Epoch 1/1:   3%|▎         | 3/102 [03:15<1:18:51, 47.79s/it, loss=1.039]Epoch 1/1:   3%|▎         | 3/102 [03:15<1:18:51, 47.79s/it, loss=1.010]Epoch 1/1:   4%|▍         | 4/102 [03:15<1:04:19, 39.38s/it, loss=1.010]Epoch 1/1:   4%|▍         | 4/102 [05:10<1:04:19, 39.38s/it, loss=1.010]Epoch 1/1:   4%|▍         | 4/102 [05:10<1:04:19, 39.38s/it, loss=1.069]Epoch 1/1:   5%|▍         | 5/102 [05:10<1:40:01, 61.87s/it, loss=1.069]Epoch 1/1:   5%|▍         | 5/102 [06:06<1:40:01, 61.87s/it, loss=1.069]Epoch 1/1:   5%|▍         | 5/102 [06:06<1:40:01, 61.87s/it, loss=0.918]Epoch 1/1:   6%|▌         | 6/102 [06:06<1:36:02, 60.03s/it, loss=0.918]Epoch 1/1:   6%|▌         | 6/102 [08:10<1:36:02, 60.03s/it, loss=0.918]Epoch 1/1:   6%|▌         | 6/102 [08:10<1:36:02, 60.03s/it, loss=0.964]Epoch 1/1:   7%|▋         | 7/102 [08:10<2:05:36, 79.33s/it, loss=0.964]Killed

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
From github.com:arita37/mlmodels_store
   5fa97af..fd086d8  master     -> origin/master
Updating 5fa97af..fd086d8
Fast-forward
 deps.txt                                           |   6 +-
 error_list/20200519/list_log_testall_20200519.md   |   9 +
 ...-10_73f54da32a5da4768415eb9105ad096255137679.py | 637 +++++++++++++++++++++
 3 files changed, 651 insertions(+), 1 deletion(-)
 create mode 100644 log_pullrequest/log_pr_2020-05-19-05-10_73f54da32a5da4768415eb9105ad096255137679.py
[master 5ea193a] ml_store
 1 file changed, 72 insertions(+)
To github.com:arita37/mlmodels_store.git
   fd086d8..5ea193a  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//torchhub.py 

  #### Loading params   ############################################## 

  {'data_info': {'data_path': 'mlmodels/dataset/vision/MNIST', 'dataset': 'MNIST', 'data_type': 'tch_dataset', 'batch_size': 10, 'train': True}, 'preprocessors': [{'name': 'tch_dataset_start', 'uri': 'mlmodels/preprocess/generic.py::get_dataset_torch', 'args': {'dataloader': 'torchvision.datasets:MNIST', 'to_image': True, 'transform': {'uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'pass_data_pars': False, 'arg': {}}, 'shuffle': True, 'download': True}}]} {'checkpointdir': 'ztest/model_tch/torchhub/restnet18/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/restnet18/'} 

  #### Loading dataset   ############################################# 

  URL:  mlmodels/preprocess/generic.py::get_dataset_torch {'dataloader': 'torchvision.datasets:MNIST', 'to_image': True, 'transform': {'uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'pass_data_pars': False, 'arg': {}}, 'shuffle': True, 'download': True} 

###### load_callable_from_uri LOADED <function get_dataset_torch at 0x7f7fe5de5d90>

 ######### postional parameteres :  ['data_info']

 ######### Execute : preprocessor_func <function get_dataset_torch at 0x7f7fe5de5d90>

  function with postional parmater data_info <function get_dataset_torch at 0x7f7fe5de5d90> , (data_info, **args) 

  #### If transformer URI is Provided {'uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'pass_data_pars': False, 'arg': {}} 

  #### Loading dataloader URI 

  dataset :  <class 'torchvision.datasets.mnist.MNIST'> 
0it [00:00, ?it/s]  0%|          | 16384/9912422 [00:00<01:12, 136609.46it/s] 80%|████████  | 7946240/9912422 [00:00<00:10, 195012.38it/s]9920512it [00:00, 41927411.01it/s]                           
0it [00:00, ?it/s]32768it [00:00, 679220.72it/s]
0it [00:00, ?it/s]  6%|▋         | 106496/1648877 [00:00<00:01, 1039987.24it/s]1654784it [00:00, 12720907.66it/s]                           
0it [00:00, ?it/s]8192it [00:00, 252773.38it/s]Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz to mlmodels/dataset/vision/MNIST/MNIST/raw/train-images-idx3-ubyte.gz
Extracting mlmodels/dataset/vision/MNIST/MNIST/raw/train-images-idx3-ubyte.gz to mlmodels/dataset/vision/MNIST/MNIST/raw
Downloading http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz to mlmodels/dataset/vision/MNIST/MNIST/raw/train-labels-idx1-ubyte.gz
Extracting mlmodels/dataset/vision/MNIST/MNIST/raw/train-labels-idx1-ubyte.gz to mlmodels/dataset/vision/MNIST/MNIST/raw
Downloading http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz to mlmodels/dataset/vision/MNIST/MNIST/raw/t10k-images-idx3-ubyte.gz
Extracting mlmodels/dataset/vision/MNIST/MNIST/raw/t10k-images-idx3-ubyte.gz to mlmodels/dataset/vision/MNIST/MNIST/raw
Downloading http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz to mlmodels/dataset/vision/MNIST/MNIST/raw/t10k-labels-idx1-ubyte.gz
Extracting mlmodels/dataset/vision/MNIST/MNIST/raw/t10k-labels-idx1-ubyte.gz to mlmodels/dataset/vision/MNIST/MNIST/raw
Processing...
Done!

  #### Model init, fit   ############################################# 

  URL:  mlmodels/preprocess/generic.py::get_dataset_torch {'dataloader': 'torchvision.datasets:MNIST', 'to_image': True, 'transform': {'uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'pass_data_pars': False, 'arg': {}}, 'shuffle': True, 'download': True} 

###### load_callable_from_uri LOADED <function get_dataset_torch at 0x7f7fe5119ae8>

 ######### postional parameteres :  ['data_info']

 ######### Execute : preprocessor_func <function get_dataset_torch at 0x7f7fe5119ae8>

  function with postional parmater data_info <function get_dataset_torch at 0x7f7fe5119ae8> , (data_info, **args) 

  #### If transformer URI is Provided {'uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'pass_data_pars': False, 'arg': {}} 

  #### Loading dataloader URI 

  dataset :  <class 'torchvision.datasets.mnist.MNIST'> 
Train Epoch: 1 	 Loss: 0.001966156482696533 	 Accuracy: 0
Train Epoch: 1 	 Loss: 0.011121248006820678 	 Accuracy: 1
model saves at 1 accuracy
Train Epoch: 2 	 Loss: 0.001223211387793223 	 Accuracy: 0
Train Epoch: 2 	 Loss: 0.010563305377960205 	 Accuracy: 0

  #### Predict   ##################################################### 

  URL:  mlmodels/preprocess/generic.py::get_dataset_torch {'dataloader': 'torchvision.datasets:MNIST', 'to_image': True, 'transform': {'uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'pass_data_pars': False, 'arg': {}}, 'shuffle': True, 'download': True} 

###### load_callable_from_uri LOADED <function get_dataset_torch at 0x7f7fe51198c8>

 ######### postional parameteres :  ['data_info']

 ######### Execute : preprocessor_func <function get_dataset_torch at 0x7f7fe51198c8>

  function with postional parmater data_info <function get_dataset_torch at 0x7f7fe51198c8> , (data_info, **args) 

  #### If transformer URI is Provided {'uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'pass_data_pars': False, 'arg': {}} 

  #### Loading dataloader URI 

  dataset :  <class 'torchvision.datasets.mnist.MNIST'> 

  #### metrics   ##################################################### 
None

  #### Plot   ######################################################## 

  #### Save  ######################################################### 

  /home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/restnet18//torch_model/ ['model.pb', 'torch_model_pars.pkl'] 

  #### Load   ######################################################## 
<__main__.Model object at 0x7f7fe578f898>

  #### Loading params   ############################################## 

  {'data_info': {'data_path': 'mlmodels/dataset/vision/MNIST', 'dataset': 'MNIST', 'data_type': 'tch_dataset', 'batch_size': 10, 'train': True}, 'preprocessors': [{'name': 'tch_dataset_start', 'uri': 'mlmodels.preprocess.generic::get_dataset_torch', 'args': {'dataloader': 'torchvision.datasets:MNIST', 'to_image': True, 'transform': {'uri': 'mlmodels.preprocess.image:torch_transform_mnist', 'pass_data_pars': False, 'arg': {'fixed_size': 256, 'path': 'dataset/vision/MNIST/'}}, 'shuffle': True, 'download': True}}]} {'checkpointdir': 'ztest/model_tch/torchhub/restnet18/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/restnet18/'} 

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 

  #### Predict   ##################################################### 
img_01.png
torch_model

  #### metrics   ##################################################### 

  #### Plot   ######################################################## 

  #### Save/Load   ################################################### 

  /home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/restnet18//torch_model/ ['model.pb', 'torch_model_pars.pkl'] 
img_01.png
torch_model

Downloading: "https://github.com/pytorch/vision/archive/master.zip" to /home/runner/.cache/torch/hub/master.zip
Using cache found in /home/runner/.cache/torch/hub/pytorch_vision_master
Downloading: "https://github.com/facebookresearch/pytorch_GAN_zoo/archive/hub.zip" to /home/runner/.cache/torch/hub/hub.zip
Using cache found in /home/runner/.cache/torch/hub/facebookresearch_pytorch_GAN_zoo_hub
<__main__.Model object at 0x7f7fe4717a58>

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Already up to date.
[master 8ec8de7] ml_store
 2 files changed, 149 insertions(+), 5 deletions(-)
To github.com:arita37/mlmodels_store.git
   5ea193a..8ec8de7  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//03_nbeats_dataloader.py 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//03_nbeats_dataloader.py", line 9, in <module>
    from dataloader import DataLoader
ModuleNotFoundError: No module named 'dataloader'

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Already up to date.
[master dd6b6a5] ml_store
 1 file changed, 36 insertions(+)
Warning: Permanently added the RSA host key for IP address '140.82.112.3' to the list of known hosts.
To github.com:arita37/mlmodels_store.git
   8ec8de7..dd6b6a5  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//transformer_sentence.py 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 
Epoch:   0%|          | 0/1 [00:00<?, ?it/s]
Iteration:   0%|          | 0/29440 [00:00<?, ?it/s][A
Iteration:   0%|          | 1/29440 [00:19<160:40:41, 19.65s/it][A
Iteration:   0%|          | 2/29440 [01:31<288:28:53, 35.28s/it][A
Iteration:   0%|          | 3/29440 [02:09<295:54:02, 36.19s/it][A
Iteration:   0%|          | 4/29440 [02:49<305:07:18, 37.32s/it][A
Iteration:   0%|          | 5/29440 [04:46<501:07:20, 61.29s/it][A
Iteration:   0%|          | 6/29440 [05:45<494:24:05, 60.47s/it][A
Iteration:   0%|          | 7/29440 [06:37<472:57:03, 57.85s/it][A
Iteration:   0%|          | 8/29440 [06:50<364:08:09, 44.54s/it][A
Iteration:   0%|          | 9/29440 [08:47<540:55:58, 66.17s/it][A
Iteration:   0%|          | 10/29440 [11:43<810:29:49, 99.14s/it][A
Iteration:   0%|          | 11/29440 [13:41<857:47:52, 104.93s/it][A
Iteration:   0%|          | 12/29440 [14:34<729:38:54, 89.26s/it] [A
Iteration:   0%|          | 13/29440 [15:06<588:42:51, 72.02s/it][A
Iteration:   0%|          | 14/29440 [15:40<495:07:19, 60.57s/it][A
Iteration:   0%|          | 15/29440 [17:52<669:52:38, 81.96s/it][AKilled

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
From github.com:arita37/mlmodels_store
   dd6b6a5..1d17166  master     -> origin/master
Updating dd6b6a5..1d17166
Fast-forward
 error_list/20200519/list_log_testall_20200519.md | 7 +++++++
 1 file changed, 7 insertions(+)
[master ba96dbe] ml_store
 1 file changed, 63 insertions(+)
To github.com:arita37/mlmodels_store.git
   1d17166..ba96dbe  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//pytorch_vae.py 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//pytorch_vae.py", line 34, in <module>
    "beta_vae": md.model.beta_vae,
AttributeError: module 'mlmodels.model_tch.raw.pytorch_vae' has no attribute 'model'

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Already up to date.
[master 68909b7] ml_store
 1 file changed, 36 insertions(+)
To github.com:arita37/mlmodels_store.git
   ba96dbe..68909b7  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//pplm.py 
 Generating text ... 
= Prefix of sentence =
<|endoftext|>The potato

 Unperturbed generated text :

<|endoftext|>The potato-shaped, potato-eating insect of modern times (Ophiocordyceps elegans) has a unique ability to adapt quickly to a wide range of environments. It is able to survive in many different environments, including the Arctic, deserts

 Perturbed generated text :

<|endoftext|>The potato bomb is nothing new. It's been on the news a lot since 9/11. In fact, since the bombing in Paris last November, a bomb has been detonated in every major European country in the European Union.

The bomb in Brussels


   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
From github.com:arita37/mlmodels_store
   68909b7..2a8033f  master     -> origin/master
Updating 68909b7..2a8033f
Fast-forward
 error_list/20200519/list_log_testall_20200519.md | 7 +++++++
 1 file changed, 7 insertions(+)
[master 8f6ced2] ml_store
 1 file changed, 51 insertions(+)
To github.com:arita37/mlmodels_store.git
   2a8033f..8f6ced2  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//textcnn.py 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/textcnn/model', 'checkpointdir': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/textcnn//checkpoint/'}

  #### Loading dataset   ############################################# 
>>>>> load:  {'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_sample.txt', 'train_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_train.csv', 'valid_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/recommender/IMDB_valid.csv', 'split_if_exists': True, 'frac': 0.99, 'lang': 'en', 'pretrained_emb': 'glove.6B.300d', 'batch_size': 64, 'val_batch_size': 64}
Spliting original file to train/valid set...

  Download en 
Collecting en_core_web_sm==2.2.5
  Downloading https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.5/en_core_web_sm-2.2.5.tar.gz (12.0 MB)
Requirement already satisfied: spacy>=2.2.2 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from en_core_web_sm==2.2.5) (2.2.4)
Requirement already satisfied: cymem<2.1.0,>=2.0.2 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (2.0.3)
Requirement already satisfied: setuptools in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (45.2.0)
Requirement already satisfied: plac<1.2.0,>=0.9.6 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (1.1.3)
Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (1.0.2)
Requirement already satisfied: thinc==7.4.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (7.4.0)
Requirement already satisfied: blis<0.5.0,>=0.4.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (0.4.1)
Requirement already satisfied: preshed<3.1.0,>=3.0.2 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (3.0.2)
Requirement already satisfied: srsly<1.1.0,>=1.0.2 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (1.0.2)
Requirement already satisfied: requests<3.0.0,>=2.13.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (2.23.0)
Requirement already satisfied: tqdm<5.0.0,>=4.38.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (4.46.0)
Requirement already satisfied: numpy>=1.15.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (1.18.4)
Requirement already satisfied: catalogue<1.1.0,>=0.0.7 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (1.0.0)
Requirement already satisfied: wasabi<1.1.0,>=0.4.0 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from spacy>=2.2.2->en_core_web_sm==2.2.5) (0.6.0)
Requirement already satisfied: certifi>=2017.4.17 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from requests<3.0.0,>=2.13.0->spacy>=2.2.2->en_core_web_sm==2.2.5) (2020.4.5.1)
Requirement already satisfied: chardet<4,>=3.0.2 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from requests<3.0.0,>=2.13.0->spacy>=2.2.2->en_core_web_sm==2.2.5) (3.0.4)
Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from requests<3.0.0,>=2.13.0->spacy>=2.2.2->en_core_web_sm==2.2.5) (1.25.9)
Requirement already satisfied: idna<3,>=2.5 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from requests<3.0.0,>=2.13.0->spacy>=2.2.2->en_core_web_sm==2.2.5) (2.9)
Requirement already satisfied: importlib-metadata>=0.20; python_version < "3.8" in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from catalogue<1.1.0,>=0.0.7->spacy>=2.2.2->en_core_web_sm==2.2.5) (1.6.0)
Requirement already satisfied: zipp>=0.5 in /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages (from importlib-metadata>=0.20; python_version < "3.8"->catalogue<1.1.0,>=0.0.7->spacy>=2.2.2->en_core_web_sm==2.2.5) (3.1.0)
Building wheels for collected packages: en-core-web-sm
  Building wheel for en-core-web-sm (setup.py): started
  Building wheel for en-core-web-sm (setup.py): finished with status 'done'
  Created wheel for en-core-web-sm: filename=en_core_web_sm-2.2.5-py3-none-any.whl size=12011738 sha256=d3d7ce3caa9dd625f1dc4b7ed6668d4ab189c9d8f23f89de641e86e4420067b1
  Stored in directory: /tmp/pip-ephem-wheel-cache-thqv21qv/wheels/b5/94/56/596daa677d7e91038cbddfcf32b591d0c915a1b3a3e3d3c79d
Successfully built en-core-web-sm
Installing collected packages: en-core-web-sm
Successfully installed en-core-web-sm-2.2.5
[38;5;2m✔ Download and installation successful[0m
You can now load the model via spacy.load('en_core_web_sm')
[38;5;2m✔ Linking successful[0m
/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/en_core_web_sm
-->
/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/spacy/data/en
You can now load the model via spacy.load('en')
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//textcnn.py", line 153, in create_tabular_dataset
    spacy_en = spacy.load( f'{lang}_core_web_sm', disable= disable)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/spacy/__init__.py", line 30, in load
    return util.load_model(name, **overrides)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/spacy/util.py", line 169, in load_model
    raise IOError(Errors.E050.format(name=name))
OSError: [E050] Can't find model 'en_core_web_sm'. It doesn't seem to be a shortcut link, a Python package or a valid path to a data directory.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//textcnn.py", line 477, in <module>
    test( data_path="model_tch/textcnn.json", pars_choice = "test01" )
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//textcnn.py", line 442, in test
    Xtuple = get_dataset(data_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//textcnn.py", line 334, in get_dataset
    trainset, validset, vocab = create_tabular_dataset( data_pars['train_path'], data_pars['valid_path'], lang, pretrained_emb)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//textcnn.py", line 159, in create_tabular_dataset
    spacy_en = spacy.load( f'{lang}_core_web_sm', disable= disable)  
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/spacy/__init__.py", line 30, in load
    return util.load_model(name, **overrides)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/spacy/util.py", line 169, in load_model
    raise IOError(Errors.E050.format(name=name))
OSError: [E050] Can't find model 'en_core_web_sm'. It doesn't seem to be a shortcut link, a Python package or a valid path to a data directory.

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Already up to date.
[master 0b45cc9] ml_store
 2 files changed, 106 insertions(+)
To github.com:arita37/mlmodels_store.git
   8f6ced2..0b45cc9  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//mlp.py 

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all  &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
deps.txt
error_list
log_benchmark
log_dataloader
log_import
log_json
log_jupyter
log_pullrequest
log_test_cli
log_testall
test_jupyter
Fetching origin
Already up to date.
[master cddd428] ml_store
 1 file changed, 32 insertions(+)
To github.com:arita37/mlmodels_store.git
   0b45cc9..cddd428  master -> master
