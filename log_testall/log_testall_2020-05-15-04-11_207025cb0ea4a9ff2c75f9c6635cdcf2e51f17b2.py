
  test_all /home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json Namespace(config_file='/home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json', config_mode='test', do='test_all', folder=None, log_file=None, save_folder='ztest/') 

  ml_test --do test_all 





 ************************************************************************************************************************

 ******** TAG ::  {'github_repo_url': 'https://github.com/arita37/mlmodels/tree/207025cb0ea4a9ff2c75f9c6635cdcf2e51f17b2', 'url_branch_file': 'https://github.com/arita37/mlmodels/blob/dev/', 'repo': 'arita37/mlmodels', 'branch': 'dev', 'sha': '207025cb0ea4a9ff2c75f9c6635cdcf2e51f17b2', 'workflow': 'test_all'}

 ******** GITHUB_WOKFLOW : https://github.com/arita37/mlmodels/actions?query=workflow%3Atest_all

 ******** GITHUB_REPO_BRANCH : https://github.com/arita37/mlmodels/tree/dev/

 ******** GITHUB_REPO_URL : https://github.com/arita37/mlmodels/tree/207025cb0ea4a9ff2c75f9c6635cdcf2e51f17b2

 ******** GITHUB_COMMIT_URL : https://github.com/arita37/mlmodels/commit/207025cb0ea4a9ff2c75f9c6635cdcf2e51f17b2

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

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
Already up to date.
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master 8df0c1b] ml_store
 1 file changed, 59 insertions(+)
 create mode 100644 log_testall/log_testall_2020-05-15-04-11_207025cb0ea4a9ff2c75f9c6635cdcf2e51f17b2.py
To github.com:arita37/mlmodels_store.git
   ee10ddf..8df0c1b  master -> master





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

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
Warning: Permanently added the RSA host key for IP address '140.82.113.4' to the list of known hosts.
Already up to date.
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master b645530] ml_store
 1 file changed, 48 insertions(+)
To github.com:arita37/mlmodels_store.git
   8df0c1b..b645530  master -> master





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

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
From github.com:arita37/mlmodels_store
   b645530..f1b2a84  master     -> origin/master
Updating b645530..f1b2a84
Fast-forward
 ...-10_207025cb0ea4a9ff2c75f9c6635cdcf2e51f17b2.py | 611 +++++++++++++++++++++
 1 file changed, 611 insertions(+)
 create mode 100644 log_pullrequest/log_pr_2020-05-15-04-10_207025cb0ea4a9ff2c75f9c6635cdcf2e51f17b2.py
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master 6534df9] ml_store
 1 file changed, 53 insertions(+)
To github.com:arita37/mlmodels_store.git
   f1b2a84..6534df9  master -> master





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
sequence_sum (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 1)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 2)]          0                                            
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
linear0sparse_seq_emb_sequence_ (None, 3, 1)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         9           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         6           sequence_max[0][0]               
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         1           sparse_feature_2[0][0]           
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
sparse_seq_emb_sequence_sum (Em (None, 3, 4)         16          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 1, 4)         36          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 2, 4)         24          sequence_max[0][0]               
__________________________________________________________________________________________________
concatenate (Concatenate)       (None, 1, 7)         0           no_mask[0][0]                    
                                                                 no_mask[1][0]                    
                                                                 no_mask[2][0]                    
                                                                 no_mask[3][0]                    
                                                                 no_mask[4][0]                    
                                                                 no_mask[5][0]                    
                                                                 no_mask[6][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         28          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         12          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         4           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer (Sequenc (None, 1, 4)         0           weighted_sequence_layer[0][0]    2020-05-15 04:12:33.119977: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 AVX512F FMA
2020-05-15 04:12:33.124934: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2095195000 Hz
2020-05-15 04:12:33.125110: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x563023eb36e0 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-15 04:12:33.125125: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version

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
Total params: 213
Trainable params: 213
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 1s - loss: 0.2500 - binary_crossentropy: 0.6932500/500 [==============================] - 1s 1ms/sample - loss: 0.2535 - binary_crossentropy: 0.8293 - val_loss: 0.2543 - val_binary_crossentropy: 0.8313

  #### metrics   #################################################### 
{'MSE': 0.25368320808575523}

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
sequence_sum (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 1)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 2)]          0                                            
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
linear0sparse_seq_emb_sequence_ (None, 3, 1)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         9           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         6           sequence_max[0][0]               
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         1           sparse_feature_2[0][0]           
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
sparse_seq_emb_sequence_sum (Em (None, 3, 4)         16          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 1, 4)         36          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 2, 4)         24          sequence_max[0][0]               
__________________________________________________________________________________________________
concatenate (Concatenate)       (None, 1, 7)         0           no_mask[0][0]                    
                                                                 no_mask[1][0]                    
                                                                 no_mask[2][0]                    
                                                                 no_mask[3][0]                    
                                                                 no_mask[4][0]                    
                                                                 no_mask[5][0]                    
                                                                 no_mask[6][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         28          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         12          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         4           sparse_feature_2[0][0]           
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
Total params: 213
Trainable params: 213
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
sequence_sum (InputLayer)       [(None, 8)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_3 (Weig (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 8, 4)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 9, 4)         36          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 3, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         28          sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 8, 1)         1           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         9           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_5 (NoMask)              (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_12[0][0]  
                                                                 sequence_pooling_layer_13[0][0]  
                                                                 sequence_pooling_layer_14[0][0]  
                                                                 sequence_pooling_layer_15[0][0]  
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_0[0][0]           
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
Total params: 473
Trainable params: 473
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 1s - loss: 0.2512 - binary_crossentropy: 0.6939500/500 [==============================] - 1s 2ms/sample - loss: 0.2528 - binary_crossentropy: 0.6978 - val_loss: 0.2521 - val_binary_crossentropy: 0.7231

  #### metrics   #################################################### 
{'MSE': 0.25231174000318407}

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
sequence_sum (InputLayer)       [(None, 8)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_3 (Weig (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 8, 4)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 9, 4)         36          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 3, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         28          sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 8, 1)         1           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         9           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_5 (NoMask)              (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_12[0][0]  
                                                                 sequence_pooling_layer_13[0][0]  
                                                                 sequence_pooling_layer_14[0][0]  
                                                                 sequence_pooling_layer_15[0][0]  
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_0[0][0]           
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
Total params: 473
Trainable params: 473
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
sequence_sum (InputLayer)       [(None, 7)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 9)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 7, 4)         16          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 9, 4)         8           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 9, 4)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         4           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         12          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         28          sparse_feature_2[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 7, 1)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         2           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         2           sequence_max[0][0]               
__________________________________________________________________________________________________
conv2d_1 (Conv2D)               (None, 3, 4, 1)      5           k_max_pooling[0][0]              
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         1           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_2[0][0]           
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
Total params: 567
Trainable params: 567
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 2s - loss: 0.2500 - binary_crossentropy: 0.6931500/500 [==============================] - 1s 2ms/sample - loss: 0.2499 - binary_crossentropy: 0.6930 - val_loss: 0.2492 - val_binary_crossentropy: 0.6907

  #### metrics   #################################################### 
{'MSE': 0.24945090795342068}

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
sequence_sum (InputLayer)       [(None, 7)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 9)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 7, 4)         16          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 9, 4)         8           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 9, 4)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         4           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         12          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         28          sparse_feature_2[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 7, 1)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         2           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         2           sequence_max[0][0]               
__________________________________________________________________________________________________
conv2d_1 (Conv2D)               (None, 3, 4, 1)      5           k_max_pooling[0][0]              
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         1           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_2[0][0]           
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
Total params: 567
Trainable params: 567
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
sequence_sum (InputLayer)       [(None, 4)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 3)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 4, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 3, 4)         36          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 3, 4)         16          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         12          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         32          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         16          sparse_feature_2[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 4, 1)         7           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         9           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         4           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_4 (Flatten)             (None, 28)           0           concatenate_9[0][0]              
__________________________________________________________________________________________________
flatten_5 (Flatten)             (None, 3)            0           concatenate_10[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         4           sparse_feature_2[0][0]           
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
Total params: 453
Trainable params: 453
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 2s - loss: 0.2936 - binary_crossentropy: 1.0758500/500 [==============================] - 1s 3ms/sample - loss: 0.3081 - binary_crossentropy: 0.9803 - val_loss: 0.3091 - val_binary_crossentropy: 0.9899

  #### metrics   #################################################### 
{'MSE': 0.3040328473743224}

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
sequence_sum (InputLayer)       [(None, 4)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 3)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 4, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 3, 4)         36          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 3, 4)         16          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         12          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         32          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         16          sparse_feature_2[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 4, 1)         7           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         9           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         4           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_4 (Flatten)             (None, 28)           0           concatenate_9[0][0]              
__________________________________________________________________________________________________
flatten_5 (Flatten)             (None, 3)            0           concatenate_10[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         4           sparse_feature_2[0][0]           
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
Total params: 453
Trainable params: 453
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
sequence_sum (InputLayer)       [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_12 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 2, 4)         12          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 2, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 1, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         12          sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 2, 1)         3           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         7           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
concatenate_14 (Concatenate)    (None, 1, 20)        0           no_mask_22[0][0]                 
                                                                 no_mask_22[1][0]                 
                                                                 no_mask_22[2][0]                 
                                                                 no_mask_22[3][0]                 
                                                                 no_mask_22[4][0]                 
__________________________________________________________________________________________________
no_mask_23 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_0[0][0]           
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
Total params: 163
Trainable params: 163
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 2s - loss: 0.3255 - binary_crossentropy: 2.1597500/500 [==============================] - 2s 3ms/sample - loss: 0.3200 - binary_crossentropy: 1.9120 - val_loss: 0.2995 - val_binary_crossentropy: 1.4725

  #### metrics   #################################################### 
{'MSE': 0.3088213041591331}

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
sequence_sum (InputLayer)       [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_12 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 2, 4)         12          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 2, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 1, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         12          sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 2, 1)         3           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         7           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
concatenate_14 (Concatenate)    (None, 1, 20)        0           no_mask_22[0][0]                 
                                                                 no_mask_22[1][0]                 
                                                                 no_mask_22[2][0]                 
                                                                 no_mask_22[3][0]                 
                                                                 no_mask_22[4][0]                 
__________________________________________________________________________________________________
no_mask_23 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_0[0][0]           
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
Total params: 163
Trainable params: 163
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
dnn_4 (DNN)                     (None, 4)            152         concatenate_20[0][0]             2020-05-15 04:13:55.512470: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-15 04:13:55.514468: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-15 04:13:55.519864: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-15 04:13:55.529908: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-15 04:13:55.531642: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-15 04:13:55.533146: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-15 04:13:55.534493: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

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
1/1 [==============================] - 3s 3s/sample - loss: 0.2500 - binary_crossentropy: 0.6931 - val_loss: 0.2472 - val_binary_crossentropy: 0.6876
2020-05-15 04:13:56.897755: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-15 04:13:56.899482: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-15 04:13:56.903761: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-15 04:13:56.912371: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-15 04:13:56.913871: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-15 04:13:56.915325: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-15 04:13:56.916593: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

  #### metrics   #################################################### 
{'MSE': 0.24607864521890357}

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
2020-05-15 04:14:21.409009: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-15 04:14:21.410447: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-15 04:14:21.413958: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-15 04:14:21.420040: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-15 04:14:21.421040: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-15 04:14:21.421985: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-15 04:14:21.422843: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
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
1/1 [==============================] - 3s 3s/sample - loss: 0.2500 - binary_crossentropy: 0.6931 - val_loss: 0.2495 - val_binary_crossentropy: 0.6922
2020-05-15 04:14:23.021779: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-15 04:14:23.022854: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-15 04:14:23.025212: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-15 04:14:23.030080: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-15 04:14:23.030920: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-15 04:14:23.031715: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-15 04:14:23.032412: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

  #### metrics   #################################################### 
{'MSE': 0.24925567955697403}

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
concatenate_27 (Concatenate)    (None, 1, 16)        0           no_mask_36[0][0]                 2020-05-15 04:14:57.112389: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-15 04:14:57.117342: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-15 04:14:57.131687: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-15 04:14:57.156692: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-15 04:14:57.161150: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-15 04:14:57.165091: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-15 04:14:57.169151: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

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
1/1 [==============================] - 5s 5s/sample - loss: 0.0874 - binary_crossentropy: 0.3505 - val_loss: 0.2764 - val_binary_crossentropy: 0.7489
2020-05-15 04:14:59.484404: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-15 04:14:59.489138: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-15 04:14:59.501420: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-15 04:14:59.527017: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-15 04:14:59.531303: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-15 04:14:59.535162: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-15 04:14:59.538615: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

  #### metrics   #################################################### 
{'MSE': 0.22223406716544622}

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
sequence_sum (InputLayer)       [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 9)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 5, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 5, 4)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 9, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         12          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         24          sparse_feature_1[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 5, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         1           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_48 (NoMask)             (None, 120)          0           flatten_19[0][0]                 
__________________________________________________________________________________________________
concatenate_39 (Concatenate)    (None, 2)            0           no_mask_49[0][0]                 
                                                                 no_mask_49[1][0]                 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           sparse_feature_1[0][0]           
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
Total params: 695
Trainable params: 695
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 7s - loss: 0.2776 - binary_crossentropy: 0.7577500/500 [==============================] - 4s 9ms/sample - loss: 0.2839 - binary_crossentropy: 0.7729 - val_loss: 0.2970 - val_binary_crossentropy: 0.7975

  #### metrics   #################################################### 
{'MSE': 0.28895530665521824}

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
sequence_sum (InputLayer)       [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 9)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 5, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 5, 4)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 9, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         12          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         24          sparse_feature_1[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 5, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         1           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_48 (NoMask)             (None, 120)          0           flatten_19[0][0]                 
__________________________________________________________________________________________________
concatenate_39 (Concatenate)    (None, 2)            0           no_mask_49[0][0]                 
                                                                 no_mask_49[1][0]                 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           sparse_feature_1[0][0]           
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
Total params: 695
Trainable params: 695
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
sequence_sum (InputLayer)       [(None, 8)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 2)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 8, 2)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 9, 2)         18          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 2, 2)         2           sequence_max[0][0]               
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
sparse_emb_sparse_feature_0 (Em (None, 1, 2)         18          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_3 (Em (None, 1, 2)         6           sparse_feature_3[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 2)         12          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_4 (Em (None, 1, 2)         8           sparse_feature_4[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 2)         4           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_5 (Em (None, 1, 2)         10          sparse_feature_5[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 8, 1)         2           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         9           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         1           sequence_max[0][0]               
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
linear0sparse_emb_sparse_featur (None, 1, 1)         9           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_3[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         4           sparse_feature_4[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         2           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           sparse_feature_5[0][0]           
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
Total params: 236
Trainable params: 236
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 6s - loss: 0.4900 - binary_crossentropy: 7.5582500/500 [==============================] - 5s 9ms/sample - loss: 0.5380 - binary_crossentropy: 8.2986 - val_loss: 0.4920 - val_binary_crossentropy: 7.5891

  #### metrics   #################################################### 
{'MSE': 0.515}

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
sequence_sum (InputLayer)       [(None, 8)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 2)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 8, 2)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 9, 2)         18          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 2, 2)         2           sequence_max[0][0]               
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
sparse_emb_sparse_feature_0 (Em (None, 1, 2)         18          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_3 (Em (None, 1, 2)         6           sparse_feature_3[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 2)         12          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_4 (Em (None, 1, 2)         8           sparse_feature_4[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 2)         4           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_5 (Em (None, 1, 2)         10          sparse_feature_5[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 8, 1)         2           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         9           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         1           sequence_max[0][0]               
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
linear0sparse_emb_sparse_featur (None, 1, 1)         9           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_3[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         4           sparse_feature_4[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         2           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           sparse_feature_5[0][0]           
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
Total params: 236
Trainable params: 236
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
sequence_sum (InputLayer)       [(None, 4)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 3)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 7)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_21 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 4, 4)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 3, 4)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 7, 4)         20          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         20          sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 4, 1)         1           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         1           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 7, 1)         5           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_24 (Flatten)            (None, 20)           0           concatenate_55[0][0]             
__________________________________________________________________________________________________
flatten_25 (Flatten)            (None, 1)            0           no_mask_69[0][0]                 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           sparse_feature_0[0][0]           
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
Total params: 1,864
Trainable params: 1,864
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 6s - loss: 0.2976 - binary_crossentropy: 0.8041500/500 [==============================] - 5s 9ms/sample - loss: 0.2647 - binary_crossentropy: 0.7328 - val_loss: 0.2978 - val_binary_crossentropy: 0.8034

  #### metrics   #################################################### 
{'MSE': 0.27990862174581727}

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
sequence_sum (InputLayer)       [(None, 4)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 3)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 7)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_21 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 4, 4)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 3, 4)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 7, 4)         20          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         20          sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 4, 1)         1           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         1           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 7, 1)         5           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_24 (Flatten)            (None, 20)           0           concatenate_55[0][0]             
__________________________________________________________________________________________________
flatten_25 (Flatten)            (None, 1)            0           no_mask_69[0][0]                 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           sparse_feature_0[0][0]           
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
Total params: 1,864
Trainable params: 1,864
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
regionsequence_sum (InputLayer) [(None, 7)]          0                                            
__________________________________________________________________________________________________
regionsequence_mean (InputLayer [(None, 8)]          0                                            
__________________________________________________________________________________________________
regionsequence_max (InputLayer) [(None, 7)]          0                                            
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
region_10sparse_seq_emb_regions (None, 7, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 8, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 7, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_26 (Wei (None, 3, 1)         0           region_20sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 7, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 8, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 7, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_28 (Wei (None, 3, 1)         0           region_30sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 7, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 8, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 7, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_30 (Wei (None, 3, 1)         0           region_40sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 7, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 8, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 7, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_32 (Wei (None, 3, 1)         0           learner_10sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 7, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 8, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 7, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_34 (Wei (None, 3, 1)         0           learner_20sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 7, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 8, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 7, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_36 (Wei (None, 3, 1)         0           learner_30sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 7, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 8, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 7, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_38 (Wei (None, 3, 1)         0           learner_40sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 7, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 8, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 7, 1)         4           regionsequence_max[0][0]         
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
100/500 [=====>........................] - ETA: 9s - loss: 0.2719 - binary_crossentropy: 0.7409500/500 [==============================] - 6s 12ms/sample - loss: 0.2638 - binary_crossentropy: 0.7235 - val_loss: 0.2711 - val_binary_crossentropy: 0.7387

  #### metrics   #################################################### 
{'MSE': 0.2667780250732783}

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
regionsequence_sum (InputLayer) [(None, 7)]          0                                            
__________________________________________________________________________________________________
regionsequence_mean (InputLayer [(None, 8)]          0                                            
__________________________________________________________________________________________________
regionsequence_max (InputLayer) [(None, 7)]          0                                            
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
region_10sparse_seq_emb_regions (None, 7, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 8, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 7, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_26 (Wei (None, 3, 1)         0           region_20sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 7, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 8, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 7, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_28 (Wei (None, 3, 1)         0           region_30sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 7, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 8, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 7, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_30 (Wei (None, 3, 1)         0           region_40sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 7, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 8, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 7, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_32 (Wei (None, 3, 1)         0           learner_10sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 7, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 8, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 7, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_34 (Wei (None, 3, 1)         0           learner_20sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 7, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 8, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 7, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_36 (Wei (None, 3, 1)         0           learner_30sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 7, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 8, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 7, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_38 (Wei (None, 3, 1)         0           learner_40sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 7, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 8, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 7, 1)         4           regionsequence_max[0][0]         
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
sequence_sum (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 4)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 2)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_40 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 3, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 4, 4)         12          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 2, 4)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         16          sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 3, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 4, 1)         3           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         2           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_101 (NoMask)            (None, 1, 4)         0           bi_interaction_pooling[0][0]     
__________________________________________________________________________________________________
no_mask_102 (NoMask)            (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         4           sparse_feature_0[0][0]           
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
Total params: 1,377
Trainable params: 1,377
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 7s - loss: 0.3231 - binary_crossentropy: 2.6685500/500 [==============================] - 6s 12ms/sample - loss: 0.3012 - binary_crossentropy: 2.3286 - val_loss: 0.3033 - val_binary_crossentropy: 2.3329

  #### metrics   #################################################### 
{'MSE': 0.30283644438222684}

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
sequence_sum (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 4)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 2)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_40 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 3, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 4, 4)         12          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 2, 4)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         16          sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 3, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 4, 1)         3           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         2           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_101 (NoMask)            (None, 1, 4)         0           bi_interaction_pooling[0][0]     
__________________________________________________________________________________________________
no_mask_102 (NoMask)            (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         4           sparse_feature_0[0][0]           
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
Total params: 1,377
Trainable params: 1,377
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
sequence_sum (InputLayer)       [(None, 8)]          0                                            
__________________________________________________________________________________________________
hash_17 (Hash)                  (None, 1)            0           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 5)]          0                                            
__________________________________________________________________________________________________
hash_18 (Hash)                  (None, 1)            0           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 5)]          0                                            
__________________________________________________________________________________________________
hash_19 (Hash)                  (None, 1)            0           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
hash_20 (Hash)                  (None, 1)            0           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
hash_21 (Hash)                  (None, 1)            0           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_spa (None, 1, 4)         12          hash_14[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_spa (None, 1, 4)         20          hash_15[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         12          hash_16[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 8, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         12          hash_17[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 5, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         12          hash_18[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 5, 4)         16          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         20          hash_19[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 8, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         20          hash_20[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 5, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         20          hash_21[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 5, 4)         16          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 8, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 5, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 8, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_max_sequenc (None, 5, 4)         16          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 5, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sequence_max_sequenc (None, 5, 4)         16          sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 8, 1)         7           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         7           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         4           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_29 (Flatten)            (None, 40)           0           no_mask_116[0][0]                
__________________________________________________________________________________________________
flatten_30 (Flatten)            (None, 2)            0           concatenate_81[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           hash_10[0][0]                    
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           hash_11[0][0]                    
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
100/500 [=====>........................] - ETA: 9s - loss: 0.2578 - binary_crossentropy: 0.7090500/500 [==============================] - 7s 13ms/sample - loss: 0.2517 - binary_crossentropy: 0.6966 - val_loss: 0.2507 - val_binary_crossentropy: 0.6945

  #### metrics   #################################################### 
{'MSE': 0.2505470856542226}

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
sequence_sum (InputLayer)       [(None, 8)]          0                                            
__________________________________________________________________________________________________
hash_17 (Hash)                  (None, 1)            0           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 5)]          0                                            
__________________________________________________________________________________________________
hash_18 (Hash)                  (None, 1)            0           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 5)]          0                                            
__________________________________________________________________________________________________
hash_19 (Hash)                  (None, 1)            0           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
hash_20 (Hash)                  (None, 1)            0           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
hash_21 (Hash)                  (None, 1)            0           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_spa (None, 1, 4)         12          hash_14[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_spa (None, 1, 4)         20          hash_15[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         12          hash_16[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 8, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         12          hash_17[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 5, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         12          hash_18[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 5, 4)         16          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         20          hash_19[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 8, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         20          hash_20[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 5, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         20          hash_21[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 5, 4)         16          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 8, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 5, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 8, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_max_sequenc (None, 5, 4)         16          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 5, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sequence_max_sequenc (None, 5, 4)         16          sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 8, 1)         7           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         7           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         4           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_29 (Flatten)            (None, 40)           0           no_mask_116[0][0]                
__________________________________________________________________________________________________
flatten_30 (Flatten)            (None, 2)            0           concatenate_81[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           hash_10[0][0]                    
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           hash_11[0][0]                    
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
Model: "model_14"
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
sequence_sum (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 2)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_43 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 3, 4)         36          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 9, 4)         24          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 2, 4)         16          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         32          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_190 (Seq (None, 1, 4)         0           weighted_sequence_layer_43[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_191 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_192 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_193 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
no_mask_119 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_190[0][0] 
                                                                 sequence_pooling_layer_191[0][0] 
                                                                 sequence_pooling_layer_192[0][0] 
                                                                 sequence_pooling_layer_193[0][0] 
__________________________________________________________________________________________________
concatenate_83 (Concatenate)    (None, 1, 20)        0           no_mask_119[0][0]                
                                                                 no_mask_119[1][0]                
                                                                 no_mask_119[2][0]                
                                                                 no_mask_119[3][0]                
                                                                 no_mask_119[4][0]                
__________________________________________________________________________________________________
inner_product_layer (InnerProdu (None, 10, 1)        0           sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_190[0][0] 
                                                                 sequence_pooling_layer_191[0][0] 
                                                                 sequence_pooling_layer_192[0][0] 
                                                                 sequence_pooling_layer_193[0][0] 
__________________________________________________________________________________________________
reshape (Reshape)               (None, 20)           0           concatenate_83[0][0]             
__________________________________________________________________________________________________
flatten_31 (Flatten)            (None, 10)           0           inner_product_layer[0][0]        
__________________________________________________________________________________________________
outter_product_layer (OutterPro (None, 10)           160         sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_190[0][0] 
                                                                 sequence_pooling_layer_191[0][0] 
                                                                 sequence_pooling_layer_192[0][0] 
                                                                 sequence_pooling_layer_193[0][0] 
__________________________________________________________________________________________________
concatenate_84 (Concatenate)    (None, 40)           0           reshape[0][0]                    
                                                                 flatten_31[0][0]                 
                                                                 outter_product_layer[0][0]       
__________________________________________________________________________________________________
dense_feature_0 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
no_mask_120 (NoMask)            (None, 40)           0           concatenate_84[0][0]             
__________________________________________________________________________________________________
no_mask_121 (NoMask)            (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
flatten_32 (Flatten)            (None, 40)           0           no_mask_120[0][0]                
__________________________________________________________________________________________________
flatten_33 (Flatten)            (None, 1)            0           no_mask_121[0][0]                
__________________________________________________________________________________________________
no_mask_122 (NoMask)            multiple             0           flatten_32[0][0]                 
                                                                 flatten_33[0][0]                 
__________________________________________________________________________________________________
concatenate_85 (Concatenate)    (None, 41)           0           no_mask_122[0][0]                
                                                                 no_mask_122[1][0]                
__________________________________________________________________________________________________
dnn_19 (DNN)                    (None, 4)            188         concatenate_85[0][0]             
__________________________________________________________________________________________________
dense_12 (Dense)                (None, 1)            4           dnn_19[0][0]                     
__________________________________________________________________________________________________
prediction_layer_17 (Prediction (None, 1)            1           dense_12[0][0]                   
==================================================================================================
Total params: 469
Trainable params: 469
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 8s - loss: 0.2503 - binary_crossentropy: 0.6937500/500 [==============================] - 6s 13ms/sample - loss: 0.2548 - binary_crossentropy: 0.7031 - val_loss: 0.2505 - val_binary_crossentropy: 0.6941

  #### metrics   #################################################### 
{'MSE': 0.25046054960188}

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
Model: "model_14"
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
sequence_sum (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 2)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_43 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 3, 4)         36          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 9, 4)         24          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 2, 4)         16          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         32          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_190 (Seq (None, 1, 4)         0           weighted_sequence_layer_43[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_191 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_192 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_193 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
no_mask_119 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_190[0][0] 
                                                                 sequence_pooling_layer_191[0][0] 
                                                                 sequence_pooling_layer_192[0][0] 
                                                                 sequence_pooling_layer_193[0][0] 
__________________________________________________________________________________________________
concatenate_83 (Concatenate)    (None, 1, 20)        0           no_mask_119[0][0]                
                                                                 no_mask_119[1][0]                
                                                                 no_mask_119[2][0]                
                                                                 no_mask_119[3][0]                
                                                                 no_mask_119[4][0]                
__________________________________________________________________________________________________
inner_product_layer (InnerProdu (None, 10, 1)        0           sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_190[0][0] 
                                                                 sequence_pooling_layer_191[0][0] 
                                                                 sequence_pooling_layer_192[0][0] 
                                                                 sequence_pooling_layer_193[0][0] 
__________________________________________________________________________________________________
reshape (Reshape)               (None, 20)           0           concatenate_83[0][0]             
__________________________________________________________________________________________________
flatten_31 (Flatten)            (None, 10)           0           inner_product_layer[0][0]        
__________________________________________________________________________________________________
outter_product_layer (OutterPro (None, 10)           160         sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_190[0][0] 
                                                                 sequence_pooling_layer_191[0][0] 
                                                                 sequence_pooling_layer_192[0][0] 
                                                                 sequence_pooling_layer_193[0][0] 
__________________________________________________________________________________________________
concatenate_84 (Concatenate)    (None, 40)           0           reshape[0][0]                    
                                                                 flatten_31[0][0]                 
                                                                 outter_product_layer[0][0]       
__________________________________________________________________________________________________
dense_feature_0 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
no_mask_120 (NoMask)            (None, 40)           0           concatenate_84[0][0]             
__________________________________________________________________________________________________
no_mask_121 (NoMask)            (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
flatten_32 (Flatten)            (None, 40)           0           no_mask_120[0][0]                
__________________________________________________________________________________________________
flatten_33 (Flatten)            (None, 1)            0           no_mask_121[0][0]                
__________________________________________________________________________________________________
no_mask_122 (NoMask)            multiple             0           flatten_32[0][0]                 
                                                                 flatten_33[0][0]                 
__________________________________________________________________________________________________
concatenate_85 (Concatenate)    (None, 41)           0           no_mask_122[0][0]                
                                                                 no_mask_122[1][0]                
__________________________________________________________________________________________________
dnn_19 (DNN)                    (None, 4)            188         concatenate_85[0][0]             
__________________________________________________________________________________________________
dense_12 (Dense)                (None, 1)            4           dnn_19[0][0]                     
__________________________________________________________________________________________________
prediction_layer_17 (Prediction (None, 1)            1           dense_12[0][0]                   
==================================================================================================
Total params: 469
Trainable params: 469
Non-trainable params: 0
__________________________________________________________________________________________________

  #### Loading params   ############################################## 

  #### Path params   ################################################# 

  #### Model params   ################################################ 
{'model_name': 'WDL', 'optimization': 'adam', 'cost': 'mse'} {'dataset_type': 'synthesis', 'sample_size': 8, 'test_size': 0.2, 'dataset_name': 'WDL', 'sparse_feature_num': 2, 'dense_feature_num': 0} {'batch_size': 100, 'epochs': 1, 'validation_split': 0.5} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/deepctr/model_WDL.h5'}

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 
Model: "model_15"
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
sequence_sum (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 8)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_1 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_44 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 3, 4)         24          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 2, 4)         24          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 8, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         8           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         20          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_194 (Seq (None, 1, 4)         0           weighted_sequence_layer_44[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_195 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_196 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_197 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
weighted_sequence_layer_45 (Wei (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         6           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         6           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 8, 1)         7           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_125 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sparse_emb_sparse_feature_1[0][0]
                                                                 sequence_pooling_layer_194[0][0] 
                                                                 sequence_pooling_layer_195[0][0] 
                                                                 sequence_pooling_layer_196[0][0] 
                                                                 sequence_pooling_layer_197[0][0] 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         2           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_198 (Seq (None, 1, 1)         0           weighted_sequence_layer_45[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_199 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_200 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_201 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
concatenate_87 (Concatenate)    (None, 1, 24)        0           no_mask_125[0][0]                
                                                                 no_mask_125[1][0]                
                                                                 no_mask_125[2][0]                
                                                                 no_mask_125[3][0]                
                                                                 no_mask_125[4][0]                
                                                                 no_mask_125[5][0]                
__________________________________________________________________________________________________
no_mask_123 (NoMask)            (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_198[0][0] 
                                                                 sequence_pooling_layer_199[0][0] 
                                                                 sequence_pooling_layer_200[0][0] 
                                                                 sequence_pooling_layer_201[0][0] 
__________________________________________________________________________________________________
flatten_34 (Flatten)            (None, 24)           0           concatenate_87[0][0]             
__________________________________________________________________________________________________
concatenate_86 (Concatenate)    (None, 1, 6)         0           no_mask_123[0][0]                
                                                                 no_mask_123[1][0]                
                                                                 no_mask_123[2][0]                
                                                                 no_mask_123[3][0]                
                                                                 no_mask_123[4][0]                
                                                                 no_mask_123[5][0]                
__________________________________________________________________________________________________
dnn_20 (DNN)                    (None, 32)           1856        flatten_34[0][0]                 
__________________________________________________________________________________________________
linear_18 (Linear)              (None, 1, 1)         0           concatenate_86[0][0]             
__________________________________________________________________________________________________
dense_13 (Dense)                (None, 1)            32          dnn_20[0][0]                     
__________________________________________________________________________________________________
no_mask_124 (NoMask)            (None, 1, 1)         0           linear_18[0][0]                  
__________________________________________________________________________________________________
add_32 (Add)                    (None, 1, 1)         0           dense_13[0][0]                   
                                                                 no_mask_124[0][0]                
__________________________________________________________________________________________________
prediction_layer_18 (Prediction (None, 1)            1           add_32[0][0]                     
==================================================================================================
Total params: 2,029
Trainable params: 2,029
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 8s - loss: 0.2500 - binary_crossentropy: 0.6931500/500 [==============================] - 7s 13ms/sample - loss: 0.2500 - binary_crossentropy: 0.6931 - val_loss: 0.2500 - val_binary_crossentropy: 0.6931

  #### metrics   #################################################### 
{'MSE': 0.2498047670402626}

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
Model: "model_15"
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
sequence_sum (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 8)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_feature_1 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_44 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 3, 4)         24          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 2, 4)         24          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 8, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         8           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         20          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_194 (Seq (None, 1, 4)         0           weighted_sequence_layer_44[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_195 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_196 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_197 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
weighted_sequence_layer_45 (Wei (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         6           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         6           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 8, 1)         7           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_125 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sparse_emb_sparse_feature_1[0][0]
                                                                 sequence_pooling_layer_194[0][0] 
                                                                 sequence_pooling_layer_195[0][0] 
                                                                 sequence_pooling_layer_196[0][0] 
                                                                 sequence_pooling_layer_197[0][0] 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         2           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_198 (Seq (None, 1, 1)         0           weighted_sequence_layer_45[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_199 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_200 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_201 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
concatenate_87 (Concatenate)    (None, 1, 24)        0           no_mask_125[0][0]                
                                                                 no_mask_125[1][0]                
                                                                 no_mask_125[2][0]                
                                                                 no_mask_125[3][0]                
                                                                 no_mask_125[4][0]                
                                                                 no_mask_125[5][0]                
__________________________________________________________________________________________________
no_mask_123 (NoMask)            (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_198[0][0] 
                                                                 sequence_pooling_layer_199[0][0] 
                                                                 sequence_pooling_layer_200[0][0] 
                                                                 sequence_pooling_layer_201[0][0] 
__________________________________________________________________________________________________
flatten_34 (Flatten)            (None, 24)           0           concatenate_87[0][0]             
__________________________________________________________________________________________________
concatenate_86 (Concatenate)    (None, 1, 6)         0           no_mask_123[0][0]                
                                                                 no_mask_123[1][0]                
                                                                 no_mask_123[2][0]                
                                                                 no_mask_123[3][0]                
                                                                 no_mask_123[4][0]                
                                                                 no_mask_123[5][0]                
__________________________________________________________________________________________________
dnn_20 (DNN)                    (None, 32)           1856        flatten_34[0][0]                 
__________________________________________________________________________________________________
linear_18 (Linear)              (None, 1, 1)         0           concatenate_86[0][0]             
__________________________________________________________________________________________________
dense_13 (Dense)                (None, 1)            32          dnn_20[0][0]                     
__________________________________________________________________________________________________
no_mask_124 (NoMask)            (None, 1, 1)         0           linear_18[0][0]                  
__________________________________________________________________________________________________
add_32 (Add)                    (None, 1, 1)         0           dense_13[0][0]                   
                                                                 no_mask_124[0][0]                
__________________________________________________________________________________________________
prediction_layer_18 (Prediction (None, 1)            1           add_32[0][0]                     
==================================================================================================
Total params: 2,029
Trainable params: 2,029
Non-trainable params: 0
__________________________________________________________________________________________________

  #### Loading params   ############################################## 

  #### Path params   ################################################# 

  #### Model params   ################################################ 
{'model_name': 'xDeepFM', 'optimization': 'adam', 'cost': 'mse'} {'dataset_type': 'synthesis', 'sample_size': 8, 'test_size': 0.2, 'dataset_name': 'xDeepFM', 'sparse_feature_num': 1, 'dense_feature_num': 1} {'batch_size': 100, 'epochs': 1, 'validation_split': 0.5} {'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/deepctr/model_xDeepFM.h5'}

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 
Model: "model_16"
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
sequence_max (InputLayer)       [(None, 8)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_47 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 5, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 6, 4)         12          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 8, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         36          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_206 (Seq (None, 1, 4)         0           weighted_sequence_layer_47[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_207 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_208 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_209 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
dense_feature_0 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
no_mask_130 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_206[0][0] 
                                                                 sequence_pooling_layer_207[0][0] 
                                                                 sequence_pooling_layer_208[0][0] 
                                                                 sequence_pooling_layer_209[0][0] 
__________________________________________________________________________________________________
weighted_sequence_layer_48 (Wei (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         7           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         3           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 8, 1)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
concatenate_90 (Concatenate)    (None, 1, 20)        0           no_mask_130[0][0]                
                                                                 no_mask_130[1][0]                
                                                                 no_mask_130[2][0]                
                                                                 no_mask_130[3][0]                
                                                                 no_mask_130[4][0]                
__________________________________________________________________________________________________
no_mask_131 (NoMask)            (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         9           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_210 (Seq (None, 1, 1)         0           weighted_sequence_layer_48[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_211 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_212 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_213 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
flatten_35 (Flatten)            (None, 20)           0           concatenate_90[0][0]             
__________________________________________________________________________________________________
flatten_36 (Flatten)            (None, 1)            0           no_mask_131[0][0]                
__________________________________________________________________________________________________
no_mask_126 (NoMask)            (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_210[0][0] 
                                                                 sequence_pooling_layer_211[0][0] 
                                                                 sequence_pooling_layer_212[0][0] 
                                                                 sequence_pooling_layer_213[0][0] 
__________________________________________________________________________________________________
no_mask_132 (NoMask)            multiple             0           flatten_35[0][0]                 
                                                                 flatten_36[0][0]                 
__________________________________________________________________________________________________
concatenate_88 (Concatenate)    (None, 1, 5)         0           no_mask_126[0][0]                
                                                                 no_mask_126[1][0]                
                                                                 no_mask_126[2][0]                
                                                                 no_mask_126[3][0]                
                                                                 no_mask_126[4][0]                
__________________________________________________________________________________________________
no_mask_127 (NoMask)            (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
concatenate_91 (Concatenate)    (None, 21)           0           no_mask_132[0][0]                
                                                                 no_mask_132[1][0]                
__________________________________________________________________________________________________
linear_19 (Linear)              (None, 1)            1           concatenate_88[0][0]             
                                                                 no_mask_127[0][0]                
__________________________________________________________________________________________________
dnn_21 (DNN)                    (None, 8)            176         concatenate_91[0][0]             
__________________________________________________________________________________________________
no_mask_128 (NoMask)            (None, 1)            0           linear_19[0][0]                  
__________________________________________________________________________________________________
dense_14 (Dense)                (None, 1)            8           dnn_21[0][0]                     
__________________________________________________________________________________________________
add_35 (Add)                    (None, 1)            0           no_mask_128[0][0]                
                                                                 dense_14[0][0]                   
__________________________________________________________________________________________________
prediction_layer_19 (Prediction (None, 1)            1           add_35[0][0]                     
==================================================================================================
Total params: 331
Trainable params: 331
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 9s - loss: 0.2761 - binary_crossentropy: 0.7570500/500 [==============================] - 7s 14ms/sample - loss: 0.3078 - binary_crossentropy: 0.8331 - val_loss: 0.3045 - val_binary_crossentropy: 0.8223

  #### metrics   #################################################### 
{'MSE': 0.3040469754686096}

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
Model: "model_16"
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
sequence_max (InputLayer)       [(None, 8)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_47 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 5, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 6, 4)         12          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 8, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         36          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_206 (Seq (None, 1, 4)         0           weighted_sequence_layer_47[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_207 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_sum[0][0]
__________________________________________________________________________________________________
sequence_pooling_layer_208 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_mean[0][0
__________________________________________________________________________________________________
sequence_pooling_layer_209 (Seq (None, 1, 4)         0           sparse_seq_emb_sequence_max[0][0]
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
dense_feature_0 (InputLayer)    [(None, 1)]          0                                            
__________________________________________________________________________________________________
no_mask_130 (NoMask)            (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_206[0][0] 
                                                                 sequence_pooling_layer_207[0][0] 
                                                                 sequence_pooling_layer_208[0][0] 
                                                                 sequence_pooling_layer_209[0][0] 
__________________________________________________________________________________________________
weighted_sequence_layer_48 (Wei (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         7           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         3           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 8, 1)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
concatenate_90 (Concatenate)    (None, 1, 20)        0           no_mask_130[0][0]                
                                                                 no_mask_130[1][0]                
                                                                 no_mask_130[2][0]                
                                                                 no_mask_130[3][0]                
                                                                 no_mask_130[4][0]                
__________________________________________________________________________________________________
no_mask_131 (NoMask)            (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         9           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer_210 (Seq (None, 1, 1)         0           weighted_sequence_layer_48[0][0] 
                                                                 weighted_seq_seq_length[0][0]    
__________________________________________________________________________________________________
sequence_pooling_layer_211 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_su
__________________________________________________________________________________________________
sequence_pooling_layer_212 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_me
__________________________________________________________________________________________________
sequence_pooling_layer_213 (Seq (None, 1, 1)         0           linear0sparse_seq_emb_sequence_ma
__________________________________________________________________________________________________
flatten_35 (Flatten)            (None, 20)           0           concatenate_90[0][0]             
__________________________________________________________________________________________________
flatten_36 (Flatten)            (None, 1)            0           no_mask_131[0][0]                
__________________________________________________________________________________________________
no_mask_126 (NoMask)            (None, 1, 1)         0           linear0sparse_emb_sparse_feature_
                                                                 sequence_pooling_layer_210[0][0] 
                                                                 sequence_pooling_layer_211[0][0] 
                                                                 sequence_pooling_layer_212[0][0] 
                                                                 sequence_pooling_layer_213[0][0] 
__________________________________________________________________________________________________
no_mask_132 (NoMask)            multiple             0           flatten_35[0][0]                 
                                                                 flatten_36[0][0]                 
__________________________________________________________________________________________________
concatenate_88 (Concatenate)    (None, 1, 5)         0           no_mask_126[0][0]                
                                                                 no_mask_126[1][0]                
                                                                 no_mask_126[2][0]                
                                                                 no_mask_126[3][0]                
                                                                 no_mask_126[4][0]                
__________________________________________________________________________________________________
no_mask_127 (NoMask)            (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
concatenate_91 (Concatenate)    (None, 21)           0           no_mask_132[0][0]                
                                                                 no_mask_132[1][0]                
__________________________________________________________________________________________________
linear_19 (Linear)              (None, 1)            1           concatenate_88[0][0]             
                                                                 no_mask_127[0][0]                
__________________________________________________________________________________________________
dnn_21 (DNN)                    (None, 8)            176         concatenate_91[0][0]             
__________________________________________________________________________________________________
no_mask_128 (NoMask)            (None, 1)            0           linear_19[0][0]                  
__________________________________________________________________________________________________
dense_14 (Dense)                (None, 1)            8           dnn_21[0][0]                     
__________________________________________________________________________________________________
add_35 (Add)                    (None, 1)            0           no_mask_128[0][0]                
                                                                 dense_14[0][0]                   
__________________________________________________________________________________________________
prediction_layer_19 (Prediction (None, 1)            1           add_35[0][0]                     
==================================================================================================
Total params: 331
Trainable params: 331
Non-trainable params: 0
__________________________________________________________________________________________________

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
From github.com:arita37/mlmodels_store
   6534df9..76a311e  master     -> origin/master
Updating 6534df9..76a311e
Fast-forward
 .../20200515/list_log_dataloader_20200515.md       |   2 +-
 error_list/20200515/list_log_testall_20200515.md   | 910 +--------------------
 2 files changed, 5 insertions(+), 907 deletions(-)
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master 2f5b048] ml_store
 1 file changed, 5667 insertions(+)
To github.com:arita37/mlmodels_store.git
   76a311e..2f5b048  master -> master





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

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
Already up to date.
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master d7cdb78] ml_store
 1 file changed, 50 insertions(+)
To github.com:arita37/mlmodels_store.git
   2f5b048..d7cdb78  master -> master





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

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
Already up to date.
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master a3e63a3] ml_store
 1 file changed, 46 insertions(+)
To github.com:arita37/mlmodels_store.git
   d7cdb78..a3e63a3  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//Autokeras.py 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//Autokeras.py", line 12, in <module>
    import autokeras as ak
ModuleNotFoundError: No module named 'autokeras'

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
Already up to date.
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master 5e2b442] ml_store
 1 file changed, 35 insertions(+)
To github.com:arita37/mlmodels_store.git
   a3e63a3..5e2b442  master -> master





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

2020-05-15 04:28:07.662741: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 AVX512F FMA
2020-05-15 04:28:07.667330: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2095195000 Hz
2020-05-15 04:28:07.667491: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x562d91008850 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-15 04:28:07.667504: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
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

128/354 [=========>....................] - ETA: 5s - loss: 1.3850
256/354 [====================>.........] - ETA: 2s - loss: 1.2645
354/354 [==============================] - 9s 26ms/step - loss: 1.1261 - val_loss: 2.3335

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

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
Already up to date.
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master 2950f68] ml_store
 1 file changed, 149 insertions(+)
To github.com:arita37/mlmodels_store.git
   5e2b442..2950f68  master -> master





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

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
Already up to date.
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master 2a353d6] ml_store
 1 file changed, 47 insertions(+)
To github.com:arita37/mlmodels_store.git
   2950f68..2a353d6  master -> master





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

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
Already up to date.
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master 051ceab] ml_store
 1 file changed, 44 insertions(+)
To github.com:arita37/mlmodels_store.git
   2a353d6..051ceab  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//textcnn.py 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Loading dataset   ############################################# 
Loading data...
Downloading data from https://s3.amazonaws.com/text-datasets/imdb.npz

    8192/17464789 [..............................] - ETA: 0s
 3620864/17464789 [=====>........................] - ETA: 0s
11329536/17464789 [==================>...........] - ETA: 0s
16334848/17464789 [===========================>..] - ETA: 0s
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
2020-05-15 04:29:01.045775: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 AVX512F FMA
2020-05-15 04:29:01.050184: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2095195000 Hz
2020-05-15 04:29:01.050341: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x560df4f99fb0 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-15 04:29:01.050355: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
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

 1000/25000 [>.............................] - ETA: 11s - loss: 7.4213 - accuracy: 0.5160
 2000/25000 [=>............................] - ETA: 7s - loss: 7.5976 - accuracy: 0.5045 
 3000/25000 [==>...........................] - ETA: 6s - loss: 7.6104 - accuracy: 0.5037
 4000/25000 [===>..........................] - ETA: 5s - loss: 7.5440 - accuracy: 0.5080
 5000/25000 [=====>........................] - ETA: 5s - loss: 7.5869 - accuracy: 0.5052
 6000/25000 [======>.......................] - ETA: 4s - loss: 7.6206 - accuracy: 0.5030
 7000/25000 [=======>......................] - ETA: 4s - loss: 7.6141 - accuracy: 0.5034
 8000/25000 [========>.....................] - ETA: 4s - loss: 7.6321 - accuracy: 0.5023
 9000/25000 [=========>....................] - ETA: 3s - loss: 7.6274 - accuracy: 0.5026
10000/25000 [===========>..................] - ETA: 3s - loss: 7.6237 - accuracy: 0.5028
11000/25000 [============>.................] - ETA: 3s - loss: 7.6429 - accuracy: 0.5015
12000/25000 [=============>................] - ETA: 3s - loss: 7.6360 - accuracy: 0.5020
13000/25000 [==============>...............] - ETA: 2s - loss: 7.6277 - accuracy: 0.5025
14000/25000 [===============>..............] - ETA: 2s - loss: 7.6458 - accuracy: 0.5014
15000/25000 [=================>............] - ETA: 2s - loss: 7.6523 - accuracy: 0.5009
16000/25000 [==================>...........] - ETA: 2s - loss: 7.6417 - accuracy: 0.5016
17000/25000 [===================>..........] - ETA: 1s - loss: 7.6278 - accuracy: 0.5025
18000/25000 [====================>.........] - ETA: 1s - loss: 7.6581 - accuracy: 0.5006
19000/25000 [=====================>........] - ETA: 1s - loss: 7.6561 - accuracy: 0.5007
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6567 - accuracy: 0.5006
21000/25000 [========================>.....] - ETA: 0s - loss: 7.6542 - accuracy: 0.5008
22000/25000 [=========================>....] - ETA: 0s - loss: 7.6450 - accuracy: 0.5014
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6566 - accuracy: 0.5007
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6615 - accuracy: 0.5003
25000/25000 [==============================] - 7s 267us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000

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
(<mlmodels.util.Model_empty object at 0x7f0f69dbdc18>, None)

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

  <mlmodels.model_keras.textcnn.Model object at 0x7f0f4c71da20> 

  #### Fit   ######################################################## 
Loading data...
Pad sequences (samples x time)...
Train on 25000 samples, validate on 25000 samples
Epoch 1/1

 1000/25000 [>.............................] - ETA: 10s - loss: 7.7740 - accuracy: 0.4930
 2000/25000 [=>............................] - ETA: 7s - loss: 7.8506 - accuracy: 0.4880 
 3000/25000 [==>...........................] - ETA: 6s - loss: 7.7586 - accuracy: 0.4940
 4000/25000 [===>..........................] - ETA: 5s - loss: 7.6551 - accuracy: 0.5008
 5000/25000 [=====>........................] - ETA: 5s - loss: 7.6390 - accuracy: 0.5018
 6000/25000 [======>.......................] - ETA: 4s - loss: 7.6385 - accuracy: 0.5018
 7000/25000 [=======>......................] - ETA: 4s - loss: 7.6513 - accuracy: 0.5010
 8000/25000 [========>.....................] - ETA: 4s - loss: 7.7126 - accuracy: 0.4970
 9000/25000 [=========>....................] - ETA: 3s - loss: 7.6786 - accuracy: 0.4992
10000/25000 [===========>..................] - ETA: 3s - loss: 7.6774 - accuracy: 0.4993
11000/25000 [============>.................] - ETA: 3s - loss: 7.6597 - accuracy: 0.5005
12000/25000 [=============>................] - ETA: 2s - loss: 7.6781 - accuracy: 0.4992
13000/25000 [==============>...............] - ETA: 2s - loss: 7.6761 - accuracy: 0.4994
14000/25000 [===============>..............] - ETA: 2s - loss: 7.6633 - accuracy: 0.5002
15000/25000 [=================>............] - ETA: 2s - loss: 7.6544 - accuracy: 0.5008
16000/25000 [==================>...........] - ETA: 2s - loss: 7.6360 - accuracy: 0.5020
17000/25000 [===================>..........] - ETA: 1s - loss: 7.6522 - accuracy: 0.5009
18000/25000 [====================>.........] - ETA: 1s - loss: 7.6462 - accuracy: 0.5013
19000/25000 [=====================>........] - ETA: 1s - loss: 7.6553 - accuracy: 0.5007
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6666 - accuracy: 0.5000
21000/25000 [========================>.....] - ETA: 0s - loss: 7.6579 - accuracy: 0.5006
22000/25000 [=========================>....] - ETA: 0s - loss: 7.6687 - accuracy: 0.4999
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6666 - accuracy: 0.5000
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6743 - accuracy: 0.4995
25000/25000 [==============================] - 7s 267us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000

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

 1000/25000 [>.............................] - ETA: 11s - loss: 7.6820 - accuracy: 0.4990
 2000/25000 [=>............................] - ETA: 7s - loss: 7.8583 - accuracy: 0.4875 
 3000/25000 [==>...........................] - ETA: 6s - loss: 7.9171 - accuracy: 0.4837
 4000/25000 [===>..........................] - ETA: 5s - loss: 7.8315 - accuracy: 0.4893
 5000/25000 [=====>........................] - ETA: 5s - loss: 7.8016 - accuracy: 0.4912
 6000/25000 [======>.......................] - ETA: 4s - loss: 7.7740 - accuracy: 0.4930
 7000/25000 [=======>......................] - ETA: 4s - loss: 7.7367 - accuracy: 0.4954
 8000/25000 [========>.....................] - ETA: 4s - loss: 7.6590 - accuracy: 0.5005
 9000/25000 [=========>....................] - ETA: 3s - loss: 7.6479 - accuracy: 0.5012
10000/25000 [===========>..................] - ETA: 3s - loss: 7.6958 - accuracy: 0.4981
11000/25000 [============>.................] - ETA: 3s - loss: 7.6889 - accuracy: 0.4985
12000/25000 [=============>................] - ETA: 3s - loss: 7.6756 - accuracy: 0.4994
13000/25000 [==============>...............] - ETA: 2s - loss: 7.6253 - accuracy: 0.5027
14000/25000 [===============>..............] - ETA: 2s - loss: 7.6414 - accuracy: 0.5016
15000/25000 [=================>............] - ETA: 2s - loss: 7.6319 - accuracy: 0.5023
16000/25000 [==================>...........] - ETA: 2s - loss: 7.6455 - accuracy: 0.5014
17000/25000 [===================>..........] - ETA: 1s - loss: 7.6360 - accuracy: 0.5020
18000/25000 [====================>.........] - ETA: 1s - loss: 7.6700 - accuracy: 0.4998
19000/25000 [=====================>........] - ETA: 1s - loss: 7.6626 - accuracy: 0.5003
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6789 - accuracy: 0.4992
21000/25000 [========================>.....] - ETA: 0s - loss: 7.6783 - accuracy: 0.4992
22000/25000 [=========================>....] - ETA: 0s - loss: 7.6882 - accuracy: 0.4986
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6780 - accuracy: 0.4993
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6807 - accuracy: 0.4991
25000/25000 [==============================] - 6s 257us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000
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

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
From github.com:arita37/mlmodels_store
   051ceab..9634a3c  master     -> origin/master
Updating 051ceab..9634a3c
Fast-forward
 .../20200515/list_log_dataloader_20200515.md       |  2 +-
 error_list/20200515/list_log_testall_20200515.md   | 89 ++++++++++++++++++++++
 2 files changed, 90 insertions(+), 1 deletion(-)
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master 4efcbcd] ml_store
 1 file changed, 323 insertions(+)
To github.com:arita37/mlmodels_store.git
   9634a3c..4efcbcd  master -> master





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

13/13 [==============================] - 1s 114ms/step - loss: nan
Epoch 2/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 3/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 4/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 5/10

13/13 [==============================] - 0s 3ms/step - loss: nan
Epoch 6/10

13/13 [==============================] - 0s 3ms/step - loss: nan
Epoch 7/10

13/13 [==============================] - 0s 3ms/step - loss: nan
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

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
Already up to date.
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master 33c0e91] ml_store
 1 file changed, 125 insertions(+)
To github.com:arita37/mlmodels_store.git
   4efcbcd..33c0e91  master -> master





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
 2129920/11490434 [====>.........................] - ETA: 0s
 9338880/11490434 [=======================>......] - ETA: 0s
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

   32/60000 [..............................] - ETA: 6:57 - loss: 2.2873 - categorical_accuracy: 0.0625
   96/60000 [..............................] - ETA: 3:13 - loss: 2.2440 - categorical_accuracy: 0.1771
  160/60000 [..............................] - ETA: 2:28 - loss: 2.2224 - categorical_accuracy: 0.1937
  224/60000 [..............................] - ETA: 2:09 - loss: 2.1914 - categorical_accuracy: 0.2143
  288/60000 [..............................] - ETA: 1:57 - loss: 2.1489 - categorical_accuracy: 0.2292
  352/60000 [..............................] - ETA: 1:50 - loss: 2.1001 - categorical_accuracy: 0.2386
  416/60000 [..............................] - ETA: 1:45 - loss: 2.0567 - categorical_accuracy: 0.2668
  480/60000 [..............................] - ETA: 1:41 - loss: 2.0017 - categorical_accuracy: 0.2937
  544/60000 [..............................] - ETA: 1:37 - loss: 1.9411 - categorical_accuracy: 0.3199
  608/60000 [..............................] - ETA: 1:34 - loss: 1.9129 - categorical_accuracy: 0.3306
  672/60000 [..............................] - ETA: 1:32 - loss: 1.8653 - categorical_accuracy: 0.3467
  736/60000 [..............................] - ETA: 1:30 - loss: 1.7961 - categorical_accuracy: 0.3709
  768/60000 [..............................] - ETA: 1:30 - loss: 1.7829 - categorical_accuracy: 0.3776
  832/60000 [..............................] - ETA: 1:29 - loss: 1.7258 - categorical_accuracy: 0.4062
  896/60000 [..............................] - ETA: 1:28 - loss: 1.6805 - categorical_accuracy: 0.4241
  960/60000 [..............................] - ETA: 1:28 - loss: 1.6334 - categorical_accuracy: 0.4437
 1024/60000 [..............................] - ETA: 1:27 - loss: 1.5794 - categorical_accuracy: 0.4658
 1088/60000 [..............................] - ETA: 1:26 - loss: 1.5294 - categorical_accuracy: 0.4825
 1152/60000 [..............................] - ETA: 1:26 - loss: 1.4937 - categorical_accuracy: 0.4913
 1216/60000 [..............................] - ETA: 1:25 - loss: 1.4421 - categorical_accuracy: 0.5099
 1280/60000 [..............................] - ETA: 1:25 - loss: 1.4025 - categorical_accuracy: 0.5211
 1344/60000 [..............................] - ETA: 1:24 - loss: 1.3773 - categorical_accuracy: 0.5320
 1408/60000 [..............................] - ETA: 1:23 - loss: 1.3445 - categorical_accuracy: 0.5419
 1472/60000 [..............................] - ETA: 1:23 - loss: 1.3153 - categorical_accuracy: 0.5530
 1536/60000 [..............................] - ETA: 1:22 - loss: 1.2929 - categorical_accuracy: 0.5632
 1600/60000 [..............................] - ETA: 1:21 - loss: 1.2665 - categorical_accuracy: 0.5731
 1632/60000 [..............................] - ETA: 1:22 - loss: 1.2486 - categorical_accuracy: 0.5797
 1696/60000 [..............................] - ETA: 1:21 - loss: 1.2280 - categorical_accuracy: 0.5861
 1760/60000 [..............................] - ETA: 1:21 - loss: 1.1949 - categorical_accuracy: 0.5972
 1824/60000 [..............................] - ETA: 1:21 - loss: 1.1825 - categorical_accuracy: 0.6014
 1888/60000 [..............................] - ETA: 1:21 - loss: 1.1636 - categorical_accuracy: 0.6081
 1952/60000 [..............................] - ETA: 1:20 - loss: 1.1472 - categorical_accuracy: 0.6137
 2016/60000 [>.............................] - ETA: 1:20 - loss: 1.1348 - categorical_accuracy: 0.6186
 2080/60000 [>.............................] - ETA: 1:20 - loss: 1.1246 - categorical_accuracy: 0.6240
 2144/60000 [>.............................] - ETA: 1:20 - loss: 1.1085 - categorical_accuracy: 0.6292
 2208/60000 [>.............................] - ETA: 1:19 - loss: 1.0906 - categorical_accuracy: 0.6354
 2272/60000 [>.............................] - ETA: 1:19 - loss: 1.0727 - categorical_accuracy: 0.6408
 2336/60000 [>.............................] - ETA: 1:19 - loss: 1.0572 - categorical_accuracy: 0.6468
 2400/60000 [>.............................] - ETA: 1:18 - loss: 1.0434 - categorical_accuracy: 0.6533
 2464/60000 [>.............................] - ETA: 1:18 - loss: 1.0281 - categorical_accuracy: 0.6591
 2528/60000 [>.............................] - ETA: 1:18 - loss: 1.0141 - categorical_accuracy: 0.6646
 2592/60000 [>.............................] - ETA: 1:18 - loss: 1.0062 - categorical_accuracy: 0.6678
 2656/60000 [>.............................] - ETA: 1:18 - loss: 0.9912 - categorical_accuracy: 0.6736
 2720/60000 [>.............................] - ETA: 1:18 - loss: 0.9811 - categorical_accuracy: 0.6768
 2784/60000 [>.............................] - ETA: 1:17 - loss: 0.9689 - categorical_accuracy: 0.6803
 2848/60000 [>.............................] - ETA: 1:17 - loss: 0.9610 - categorical_accuracy: 0.6833
 2912/60000 [>.............................] - ETA: 1:17 - loss: 0.9485 - categorical_accuracy: 0.6858
 2976/60000 [>.............................] - ETA: 1:17 - loss: 0.9348 - categorical_accuracy: 0.6909
 3040/60000 [>.............................] - ETA: 1:17 - loss: 0.9220 - categorical_accuracy: 0.6957
 3104/60000 [>.............................] - ETA: 1:16 - loss: 0.9128 - categorical_accuracy: 0.6994
 3136/60000 [>.............................] - ETA: 1:17 - loss: 0.9063 - categorical_accuracy: 0.7015
 3200/60000 [>.............................] - ETA: 1:17 - loss: 0.9033 - categorical_accuracy: 0.7019
 3264/60000 [>.............................] - ETA: 1:17 - loss: 0.8928 - categorical_accuracy: 0.7050
 3328/60000 [>.............................] - ETA: 1:16 - loss: 0.8852 - categorical_accuracy: 0.7085
 3392/60000 [>.............................] - ETA: 1:16 - loss: 0.8752 - categorical_accuracy: 0.7117
 3456/60000 [>.............................] - ETA: 1:16 - loss: 0.8661 - categorical_accuracy: 0.7153
 3520/60000 [>.............................] - ETA: 1:16 - loss: 0.8539 - categorical_accuracy: 0.7196
 3584/60000 [>.............................] - ETA: 1:16 - loss: 0.8440 - categorical_accuracy: 0.7235
 3648/60000 [>.............................] - ETA: 1:16 - loss: 0.8347 - categorical_accuracy: 0.7272
 3712/60000 [>.............................] - ETA: 1:16 - loss: 0.8280 - categorical_accuracy: 0.7295
 3776/60000 [>.............................] - ETA: 1:16 - loss: 0.8197 - categorical_accuracy: 0.7320
 3840/60000 [>.............................] - ETA: 1:15 - loss: 0.8123 - categorical_accuracy: 0.7341
 3904/60000 [>.............................] - ETA: 1:15 - loss: 0.8034 - categorical_accuracy: 0.7374
 3968/60000 [>.............................] - ETA: 1:15 - loss: 0.8020 - categorical_accuracy: 0.7379
 4032/60000 [=>............................] - ETA: 1:15 - loss: 0.7997 - categorical_accuracy: 0.7396
 4096/60000 [=>............................] - ETA: 1:15 - loss: 0.7916 - categorical_accuracy: 0.7422
 4160/60000 [=>............................] - ETA: 1:15 - loss: 0.7865 - categorical_accuracy: 0.7445
 4224/60000 [=>............................] - ETA: 1:15 - loss: 0.7813 - categorical_accuracy: 0.7460
 4288/60000 [=>............................] - ETA: 1:15 - loss: 0.7739 - categorical_accuracy: 0.7486
 4352/60000 [=>............................] - ETA: 1:15 - loss: 0.7679 - categorical_accuracy: 0.7514
 4416/60000 [=>............................] - ETA: 1:14 - loss: 0.7600 - categorical_accuracy: 0.7545
 4480/60000 [=>............................] - ETA: 1:14 - loss: 0.7558 - categorical_accuracy: 0.7565
 4544/60000 [=>............................] - ETA: 1:14 - loss: 0.7518 - categorical_accuracy: 0.7575
 4608/60000 [=>............................] - ETA: 1:14 - loss: 0.7479 - categorical_accuracy: 0.7585
 4672/60000 [=>............................] - ETA: 1:14 - loss: 0.7415 - categorical_accuracy: 0.7605
 4736/60000 [=>............................] - ETA: 1:14 - loss: 0.7356 - categorical_accuracy: 0.7627
 4800/60000 [=>............................] - ETA: 1:14 - loss: 0.7296 - categorical_accuracy: 0.7648
 4864/60000 [=>............................] - ETA: 1:14 - loss: 0.7238 - categorical_accuracy: 0.7662
 4928/60000 [=>............................] - ETA: 1:13 - loss: 0.7186 - categorical_accuracy: 0.7679
 4992/60000 [=>............................] - ETA: 1:13 - loss: 0.7114 - categorical_accuracy: 0.7698
 5056/60000 [=>............................] - ETA: 1:13 - loss: 0.7059 - categorical_accuracy: 0.7716
 5120/60000 [=>............................] - ETA: 1:13 - loss: 0.7002 - categorical_accuracy: 0.7736
 5184/60000 [=>............................] - ETA: 1:13 - loss: 0.6961 - categorical_accuracy: 0.7749
 5248/60000 [=>............................] - ETA: 1:13 - loss: 0.6907 - categorical_accuracy: 0.7769
 5312/60000 [=>............................] - ETA: 1:13 - loss: 0.6856 - categorical_accuracy: 0.7782
 5376/60000 [=>............................] - ETA: 1:13 - loss: 0.6826 - categorical_accuracy: 0.7794
 5440/60000 [=>............................] - ETA: 1:13 - loss: 0.6794 - categorical_accuracy: 0.7801
 5472/60000 [=>............................] - ETA: 1:13 - loss: 0.6774 - categorical_accuracy: 0.7809
 5536/60000 [=>............................] - ETA: 1:13 - loss: 0.6727 - categorical_accuracy: 0.7827
 5600/60000 [=>............................] - ETA: 1:13 - loss: 0.6674 - categorical_accuracy: 0.7846
 5664/60000 [=>............................] - ETA: 1:13 - loss: 0.6625 - categorical_accuracy: 0.7864
 5728/60000 [=>............................] - ETA: 1:13 - loss: 0.6603 - categorical_accuracy: 0.7879
 5792/60000 [=>............................] - ETA: 1:13 - loss: 0.6550 - categorical_accuracy: 0.7899
 5856/60000 [=>............................] - ETA: 1:13 - loss: 0.6541 - categorical_accuracy: 0.7905
 5920/60000 [=>............................] - ETA: 1:12 - loss: 0.6496 - categorical_accuracy: 0.7922
 5984/60000 [=>............................] - ETA: 1:12 - loss: 0.6456 - categorical_accuracy: 0.7936
 6048/60000 [==>...........................] - ETA: 1:12 - loss: 0.6401 - categorical_accuracy: 0.7953
 6112/60000 [==>...........................] - ETA: 1:12 - loss: 0.6362 - categorical_accuracy: 0.7968
 6176/60000 [==>...........................] - ETA: 1:12 - loss: 0.6328 - categorical_accuracy: 0.7979
 6240/60000 [==>...........................] - ETA: 1:12 - loss: 0.6312 - categorical_accuracy: 0.7986
 6304/60000 [==>...........................] - ETA: 1:12 - loss: 0.6268 - categorical_accuracy: 0.8001
 6368/60000 [==>...........................] - ETA: 1:12 - loss: 0.6228 - categorical_accuracy: 0.8012
 6432/60000 [==>...........................] - ETA: 1:12 - loss: 0.6194 - categorical_accuracy: 0.8024
 6496/60000 [==>...........................] - ETA: 1:12 - loss: 0.6158 - categorical_accuracy: 0.8036
 6560/60000 [==>...........................] - ETA: 1:12 - loss: 0.6133 - categorical_accuracy: 0.8049
 6624/60000 [==>...........................] - ETA: 1:12 - loss: 0.6105 - categorical_accuracy: 0.8059
 6688/60000 [==>...........................] - ETA: 1:12 - loss: 0.6062 - categorical_accuracy: 0.8071
 6752/60000 [==>...........................] - ETA: 1:12 - loss: 0.6041 - categorical_accuracy: 0.8081
 6816/60000 [==>...........................] - ETA: 1:11 - loss: 0.5997 - categorical_accuracy: 0.8096
 6880/60000 [==>...........................] - ETA: 1:11 - loss: 0.5957 - categorical_accuracy: 0.8108
 6944/60000 [==>...........................] - ETA: 1:11 - loss: 0.5919 - categorical_accuracy: 0.8121
 7008/60000 [==>...........................] - ETA: 1:11 - loss: 0.5889 - categorical_accuracy: 0.8131
 7072/60000 [==>...........................] - ETA: 1:11 - loss: 0.5865 - categorical_accuracy: 0.8133
 7136/60000 [==>...........................] - ETA: 1:11 - loss: 0.5842 - categorical_accuracy: 0.8142
 7200/60000 [==>...........................] - ETA: 1:11 - loss: 0.5807 - categorical_accuracy: 0.8154
 7264/60000 [==>...........................] - ETA: 1:11 - loss: 0.5781 - categorical_accuracy: 0.8165
 7328/60000 [==>...........................] - ETA: 1:11 - loss: 0.5764 - categorical_accuracy: 0.8173
 7392/60000 [==>...........................] - ETA: 1:10 - loss: 0.5748 - categorical_accuracy: 0.8176
 7456/60000 [==>...........................] - ETA: 1:10 - loss: 0.5716 - categorical_accuracy: 0.8187
 7520/60000 [==>...........................] - ETA: 1:10 - loss: 0.5704 - categorical_accuracy: 0.8193
 7584/60000 [==>...........................] - ETA: 1:10 - loss: 0.5672 - categorical_accuracy: 0.8203
 7648/60000 [==>...........................] - ETA: 1:10 - loss: 0.5631 - categorical_accuracy: 0.8217
 7680/60000 [==>...........................] - ETA: 1:10 - loss: 0.5635 - categorical_accuracy: 0.8215
 7744/60000 [==>...........................] - ETA: 1:10 - loss: 0.5610 - categorical_accuracy: 0.8218
 7808/60000 [==>...........................] - ETA: 1:10 - loss: 0.5577 - categorical_accuracy: 0.8230
 7872/60000 [==>...........................] - ETA: 1:10 - loss: 0.5552 - categorical_accuracy: 0.8239
 7904/60000 [==>...........................] - ETA: 1:10 - loss: 0.5537 - categorical_accuracy: 0.8244
 7968/60000 [==>...........................] - ETA: 1:10 - loss: 0.5513 - categorical_accuracy: 0.8254
 8032/60000 [===>..........................] - ETA: 1:10 - loss: 0.5485 - categorical_accuracy: 0.8261
 8096/60000 [===>..........................] - ETA: 1:10 - loss: 0.5460 - categorical_accuracy: 0.8268
 8160/60000 [===>..........................] - ETA: 1:10 - loss: 0.5440 - categorical_accuracy: 0.8275
 8224/60000 [===>..........................] - ETA: 1:10 - loss: 0.5421 - categorical_accuracy: 0.8282
 8288/60000 [===>..........................] - ETA: 1:10 - loss: 0.5400 - categorical_accuracy: 0.8287
 8352/60000 [===>..........................] - ETA: 1:09 - loss: 0.5376 - categorical_accuracy: 0.8294
 8416/60000 [===>..........................] - ETA: 1:09 - loss: 0.5344 - categorical_accuracy: 0.8304
 8480/60000 [===>..........................] - ETA: 1:09 - loss: 0.5322 - categorical_accuracy: 0.8310
 8544/60000 [===>..........................] - ETA: 1:09 - loss: 0.5299 - categorical_accuracy: 0.8320
 8608/60000 [===>..........................] - ETA: 1:09 - loss: 0.5274 - categorical_accuracy: 0.8328
 8672/60000 [===>..........................] - ETA: 1:09 - loss: 0.5251 - categorical_accuracy: 0.8336
 8736/60000 [===>..........................] - ETA: 1:09 - loss: 0.5235 - categorical_accuracy: 0.8339
 8800/60000 [===>..........................] - ETA: 1:09 - loss: 0.5208 - categorical_accuracy: 0.8345
 8864/60000 [===>..........................] - ETA: 1:09 - loss: 0.5188 - categorical_accuracy: 0.8352
 8928/60000 [===>..........................] - ETA: 1:09 - loss: 0.5160 - categorical_accuracy: 0.8361
 8992/60000 [===>..........................] - ETA: 1:09 - loss: 0.5146 - categorical_accuracy: 0.8363
 9056/60000 [===>..........................] - ETA: 1:08 - loss: 0.5116 - categorical_accuracy: 0.8373
 9120/60000 [===>..........................] - ETA: 1:08 - loss: 0.5098 - categorical_accuracy: 0.8379
 9184/60000 [===>..........................] - ETA: 1:08 - loss: 0.5078 - categorical_accuracy: 0.8386
 9248/60000 [===>..........................] - ETA: 1:08 - loss: 0.5050 - categorical_accuracy: 0.8395
 9312/60000 [===>..........................] - ETA: 1:08 - loss: 0.5021 - categorical_accuracy: 0.8406
 9376/60000 [===>..........................] - ETA: 1:08 - loss: 0.4999 - categorical_accuracy: 0.8414
 9440/60000 [===>..........................] - ETA: 1:08 - loss: 0.4970 - categorical_accuracy: 0.8424
 9504/60000 [===>..........................] - ETA: 1:08 - loss: 0.4951 - categorical_accuracy: 0.8428
 9568/60000 [===>..........................] - ETA: 1:08 - loss: 0.4931 - categorical_accuracy: 0.8434
 9632/60000 [===>..........................] - ETA: 1:08 - loss: 0.4915 - categorical_accuracy: 0.8441
 9696/60000 [===>..........................] - ETA: 1:08 - loss: 0.4904 - categorical_accuracy: 0.8446
 9760/60000 [===>..........................] - ETA: 1:07 - loss: 0.4881 - categorical_accuracy: 0.8454
 9824/60000 [===>..........................] - ETA: 1:07 - loss: 0.4856 - categorical_accuracy: 0.8461
 9888/60000 [===>..........................] - ETA: 1:07 - loss: 0.4836 - categorical_accuracy: 0.8464
 9952/60000 [===>..........................] - ETA: 1:07 - loss: 0.4824 - categorical_accuracy: 0.8470
10016/60000 [====>.........................] - ETA: 1:07 - loss: 0.4802 - categorical_accuracy: 0.8475
10080/60000 [====>.........................] - ETA: 1:07 - loss: 0.4786 - categorical_accuracy: 0.8481
10144/60000 [====>.........................] - ETA: 1:07 - loss: 0.4767 - categorical_accuracy: 0.8486
10208/60000 [====>.........................] - ETA: 1:07 - loss: 0.4751 - categorical_accuracy: 0.8488
10272/60000 [====>.........................] - ETA: 1:07 - loss: 0.4744 - categorical_accuracy: 0.8491
10336/60000 [====>.........................] - ETA: 1:07 - loss: 0.4724 - categorical_accuracy: 0.8497
10400/60000 [====>.........................] - ETA: 1:07 - loss: 0.4700 - categorical_accuracy: 0.8505
10464/60000 [====>.........................] - ETA: 1:07 - loss: 0.4692 - categorical_accuracy: 0.8510
10528/60000 [====>.........................] - ETA: 1:07 - loss: 0.4676 - categorical_accuracy: 0.8516
10592/60000 [====>.........................] - ETA: 1:06 - loss: 0.4681 - categorical_accuracy: 0.8517
10656/60000 [====>.........................] - ETA: 1:06 - loss: 0.4674 - categorical_accuracy: 0.8518
10720/60000 [====>.........................] - ETA: 1:06 - loss: 0.4667 - categorical_accuracy: 0.8522
10784/60000 [====>.........................] - ETA: 1:06 - loss: 0.4653 - categorical_accuracy: 0.8525
10848/60000 [====>.........................] - ETA: 1:06 - loss: 0.4633 - categorical_accuracy: 0.8532
10912/60000 [====>.........................] - ETA: 1:06 - loss: 0.4628 - categorical_accuracy: 0.8536
10976/60000 [====>.........................] - ETA: 1:06 - loss: 0.4607 - categorical_accuracy: 0.8542
11040/60000 [====>.........................] - ETA: 1:06 - loss: 0.4590 - categorical_accuracy: 0.8546
11104/60000 [====>.........................] - ETA: 1:06 - loss: 0.4570 - categorical_accuracy: 0.8554
11168/60000 [====>.........................] - ETA: 1:06 - loss: 0.4567 - categorical_accuracy: 0.8558
11232/60000 [====>.........................] - ETA: 1:06 - loss: 0.4553 - categorical_accuracy: 0.8562
11296/60000 [====>.........................] - ETA: 1:06 - loss: 0.4534 - categorical_accuracy: 0.8568
11360/60000 [====>.........................] - ETA: 1:06 - loss: 0.4519 - categorical_accuracy: 0.8572
11424/60000 [====>.........................] - ETA: 1:05 - loss: 0.4502 - categorical_accuracy: 0.8578
11488/60000 [====>.........................] - ETA: 1:05 - loss: 0.4485 - categorical_accuracy: 0.8583
11552/60000 [====>.........................] - ETA: 1:05 - loss: 0.4471 - categorical_accuracy: 0.8586
11616/60000 [====>.........................] - ETA: 1:05 - loss: 0.4454 - categorical_accuracy: 0.8592
11680/60000 [====>.........................] - ETA: 1:05 - loss: 0.4440 - categorical_accuracy: 0.8598
11744/60000 [====>.........................] - ETA: 1:05 - loss: 0.4423 - categorical_accuracy: 0.8602
11808/60000 [====>.........................] - ETA: 1:05 - loss: 0.4411 - categorical_accuracy: 0.8605
11872/60000 [====>.........................] - ETA: 1:05 - loss: 0.4403 - categorical_accuracy: 0.8608
11936/60000 [====>.........................] - ETA: 1:05 - loss: 0.4389 - categorical_accuracy: 0.8612
12000/60000 [=====>........................] - ETA: 1:05 - loss: 0.4371 - categorical_accuracy: 0.8618
12064/60000 [=====>........................] - ETA: 1:05 - loss: 0.4353 - categorical_accuracy: 0.8623
12128/60000 [=====>........................] - ETA: 1:04 - loss: 0.4337 - categorical_accuracy: 0.8627
12160/60000 [=====>........................] - ETA: 1:04 - loss: 0.4328 - categorical_accuracy: 0.8630
12224/60000 [=====>........................] - ETA: 1:04 - loss: 0.4336 - categorical_accuracy: 0.8631
12288/60000 [=====>........................] - ETA: 1:04 - loss: 0.4324 - categorical_accuracy: 0.8637
12352/60000 [=====>........................] - ETA: 1:04 - loss: 0.4314 - categorical_accuracy: 0.8641
12416/60000 [=====>........................] - ETA: 1:04 - loss: 0.4301 - categorical_accuracy: 0.8645
12480/60000 [=====>........................] - ETA: 1:04 - loss: 0.4296 - categorical_accuracy: 0.8647
12544/60000 [=====>........................] - ETA: 1:04 - loss: 0.4289 - categorical_accuracy: 0.8648
12608/60000 [=====>........................] - ETA: 1:04 - loss: 0.4272 - categorical_accuracy: 0.8654
12672/60000 [=====>........................] - ETA: 1:04 - loss: 0.4260 - categorical_accuracy: 0.8658
12736/60000 [=====>........................] - ETA: 1:04 - loss: 0.4246 - categorical_accuracy: 0.8662
12800/60000 [=====>........................] - ETA: 1:04 - loss: 0.4229 - categorical_accuracy: 0.8668
12864/60000 [=====>........................] - ETA: 1:04 - loss: 0.4222 - categorical_accuracy: 0.8671
12928/60000 [=====>........................] - ETA: 1:04 - loss: 0.4211 - categorical_accuracy: 0.8675
12992/60000 [=====>........................] - ETA: 1:04 - loss: 0.4202 - categorical_accuracy: 0.8678
13056/60000 [=====>........................] - ETA: 1:03 - loss: 0.4196 - categorical_accuracy: 0.8681
13120/60000 [=====>........................] - ETA: 1:03 - loss: 0.4181 - categorical_accuracy: 0.8686
13184/60000 [=====>........................] - ETA: 1:03 - loss: 0.4171 - categorical_accuracy: 0.8689
13248/60000 [=====>........................] - ETA: 1:03 - loss: 0.4158 - categorical_accuracy: 0.8693
13312/60000 [=====>........................] - ETA: 1:03 - loss: 0.4147 - categorical_accuracy: 0.8697
13344/60000 [=====>........................] - ETA: 1:03 - loss: 0.4144 - categorical_accuracy: 0.8698
13408/60000 [=====>........................] - ETA: 1:03 - loss: 0.4135 - categorical_accuracy: 0.8700
13472/60000 [=====>........................] - ETA: 1:03 - loss: 0.4120 - categorical_accuracy: 0.8705
13536/60000 [=====>........................] - ETA: 1:03 - loss: 0.4108 - categorical_accuracy: 0.8709
13600/60000 [=====>........................] - ETA: 1:03 - loss: 0.4096 - categorical_accuracy: 0.8713
13664/60000 [=====>........................] - ETA: 1:03 - loss: 0.4088 - categorical_accuracy: 0.8716
13728/60000 [=====>........................] - ETA: 1:03 - loss: 0.4079 - categorical_accuracy: 0.8719
13792/60000 [=====>........................] - ETA: 1:03 - loss: 0.4065 - categorical_accuracy: 0.8722
13856/60000 [=====>........................] - ETA: 1:03 - loss: 0.4052 - categorical_accuracy: 0.8727
13920/60000 [=====>........................] - ETA: 1:02 - loss: 0.4046 - categorical_accuracy: 0.8729
13984/60000 [=====>........................] - ETA: 1:02 - loss: 0.4032 - categorical_accuracy: 0.8733
14048/60000 [======>.......................] - ETA: 1:02 - loss: 0.4021 - categorical_accuracy: 0.8737
14080/60000 [======>.......................] - ETA: 1:02 - loss: 0.4017 - categorical_accuracy: 0.8738
14144/60000 [======>.......................] - ETA: 1:02 - loss: 0.4008 - categorical_accuracy: 0.8740
14208/60000 [======>.......................] - ETA: 1:02 - loss: 0.4004 - categorical_accuracy: 0.8742
14272/60000 [======>.......................] - ETA: 1:02 - loss: 0.4000 - categorical_accuracy: 0.8744
14336/60000 [======>.......................] - ETA: 1:02 - loss: 0.3986 - categorical_accuracy: 0.8749
14400/60000 [======>.......................] - ETA: 1:02 - loss: 0.3977 - categorical_accuracy: 0.8751
14464/60000 [======>.......................] - ETA: 1:02 - loss: 0.3972 - categorical_accuracy: 0.8753
14528/60000 [======>.......................] - ETA: 1:02 - loss: 0.3962 - categorical_accuracy: 0.8757
14592/60000 [======>.......................] - ETA: 1:02 - loss: 0.3954 - categorical_accuracy: 0.8760
14656/60000 [======>.......................] - ETA: 1:02 - loss: 0.3939 - categorical_accuracy: 0.8764
14720/60000 [======>.......................] - ETA: 1:01 - loss: 0.3925 - categorical_accuracy: 0.8769
14784/60000 [======>.......................] - ETA: 1:01 - loss: 0.3921 - categorical_accuracy: 0.8770
14848/60000 [======>.......................] - ETA: 1:01 - loss: 0.3916 - categorical_accuracy: 0.8771
14912/60000 [======>.......................] - ETA: 1:01 - loss: 0.3907 - categorical_accuracy: 0.8774
14976/60000 [======>.......................] - ETA: 1:01 - loss: 0.3904 - categorical_accuracy: 0.8777
15040/60000 [======>.......................] - ETA: 1:01 - loss: 0.3898 - categorical_accuracy: 0.8779
15104/60000 [======>.......................] - ETA: 1:01 - loss: 0.3891 - categorical_accuracy: 0.8782
15168/60000 [======>.......................] - ETA: 1:01 - loss: 0.3888 - categorical_accuracy: 0.8783
15232/60000 [======>.......................] - ETA: 1:01 - loss: 0.3880 - categorical_accuracy: 0.8785
15296/60000 [======>.......................] - ETA: 1:01 - loss: 0.3872 - categorical_accuracy: 0.8787
15360/60000 [======>.......................] - ETA: 1:01 - loss: 0.3862 - categorical_accuracy: 0.8790
15392/60000 [======>.......................] - ETA: 1:01 - loss: 0.3856 - categorical_accuracy: 0.8793
15456/60000 [======>.......................] - ETA: 1:01 - loss: 0.3845 - categorical_accuracy: 0.8797
15520/60000 [======>.......................] - ETA: 1:00 - loss: 0.3835 - categorical_accuracy: 0.8800
15584/60000 [======>.......................] - ETA: 1:00 - loss: 0.3826 - categorical_accuracy: 0.8803
15648/60000 [======>.......................] - ETA: 1:00 - loss: 0.3812 - categorical_accuracy: 0.8808
15712/60000 [======>.......................] - ETA: 1:00 - loss: 0.3804 - categorical_accuracy: 0.8809
15776/60000 [======>.......................] - ETA: 1:00 - loss: 0.3791 - categorical_accuracy: 0.8813
15840/60000 [======>.......................] - ETA: 1:00 - loss: 0.3782 - categorical_accuracy: 0.8816
15904/60000 [======>.......................] - ETA: 1:00 - loss: 0.3784 - categorical_accuracy: 0.8817
15968/60000 [======>.......................] - ETA: 1:00 - loss: 0.3772 - categorical_accuracy: 0.8821
16032/60000 [=======>......................] - ETA: 1:00 - loss: 0.3761 - categorical_accuracy: 0.8824
16096/60000 [=======>......................] - ETA: 1:00 - loss: 0.3761 - categorical_accuracy: 0.8823
16160/60000 [=======>......................] - ETA: 1:00 - loss: 0.3757 - categorical_accuracy: 0.8824
16224/60000 [=======>......................] - ETA: 1:00 - loss: 0.3745 - categorical_accuracy: 0.8827
16288/60000 [=======>......................] - ETA: 59s - loss: 0.3737 - categorical_accuracy: 0.8830 
16352/60000 [=======>......................] - ETA: 59s - loss: 0.3728 - categorical_accuracy: 0.8833
16416/60000 [=======>......................] - ETA: 59s - loss: 0.3714 - categorical_accuracy: 0.8837
16448/60000 [=======>......................] - ETA: 59s - loss: 0.3708 - categorical_accuracy: 0.8839
16480/60000 [=======>......................] - ETA: 59s - loss: 0.3704 - categorical_accuracy: 0.8840
16512/60000 [=======>......................] - ETA: 59s - loss: 0.3708 - categorical_accuracy: 0.8840
16576/60000 [=======>......................] - ETA: 59s - loss: 0.3697 - categorical_accuracy: 0.8844
16640/60000 [=======>......................] - ETA: 59s - loss: 0.3687 - categorical_accuracy: 0.8847
16704/60000 [=======>......................] - ETA: 59s - loss: 0.3680 - categorical_accuracy: 0.8849
16768/60000 [=======>......................] - ETA: 59s - loss: 0.3674 - categorical_accuracy: 0.8852
16832/60000 [=======>......................] - ETA: 59s - loss: 0.3665 - categorical_accuracy: 0.8855
16896/60000 [=======>......................] - ETA: 59s - loss: 0.3655 - categorical_accuracy: 0.8858
16928/60000 [=======>......................] - ETA: 59s - loss: 0.3650 - categorical_accuracy: 0.8860
16992/60000 [=======>......................] - ETA: 59s - loss: 0.3639 - categorical_accuracy: 0.8864
17056/60000 [=======>......................] - ETA: 59s - loss: 0.3627 - categorical_accuracy: 0.8867
17120/60000 [=======>......................] - ETA: 58s - loss: 0.3623 - categorical_accuracy: 0.8869
17184/60000 [=======>......................] - ETA: 58s - loss: 0.3616 - categorical_accuracy: 0.8872
17248/60000 [=======>......................] - ETA: 58s - loss: 0.3613 - categorical_accuracy: 0.8873
17312/60000 [=======>......................] - ETA: 58s - loss: 0.3602 - categorical_accuracy: 0.8877
17376/60000 [=======>......................] - ETA: 58s - loss: 0.3591 - categorical_accuracy: 0.8880
17440/60000 [=======>......................] - ETA: 58s - loss: 0.3583 - categorical_accuracy: 0.8882
17504/60000 [=======>......................] - ETA: 58s - loss: 0.3576 - categorical_accuracy: 0.8885
17568/60000 [=======>......................] - ETA: 58s - loss: 0.3566 - categorical_accuracy: 0.8887
17632/60000 [=======>......................] - ETA: 58s - loss: 0.3561 - categorical_accuracy: 0.8890
17696/60000 [=======>......................] - ETA: 58s - loss: 0.3551 - categorical_accuracy: 0.8893
17760/60000 [=======>......................] - ETA: 58s - loss: 0.3540 - categorical_accuracy: 0.8896
17824/60000 [=======>......................] - ETA: 57s - loss: 0.3537 - categorical_accuracy: 0.8898
17888/60000 [=======>......................] - ETA: 57s - loss: 0.3527 - categorical_accuracy: 0.8900
17952/60000 [=======>......................] - ETA: 57s - loss: 0.3522 - categorical_accuracy: 0.8903
18016/60000 [========>.....................] - ETA: 57s - loss: 0.3511 - categorical_accuracy: 0.8907
18080/60000 [========>.....................] - ETA: 57s - loss: 0.3505 - categorical_accuracy: 0.8909
18144/60000 [========>.....................] - ETA: 57s - loss: 0.3497 - categorical_accuracy: 0.8911
18208/60000 [========>.....................] - ETA: 57s - loss: 0.3492 - categorical_accuracy: 0.8913
18272/60000 [========>.....................] - ETA: 57s - loss: 0.3487 - categorical_accuracy: 0.8915
18336/60000 [========>.....................] - ETA: 57s - loss: 0.3479 - categorical_accuracy: 0.8917
18368/60000 [========>.....................] - ETA: 57s - loss: 0.3475 - categorical_accuracy: 0.8918
18432/60000 [========>.....................] - ETA: 57s - loss: 0.3468 - categorical_accuracy: 0.8920
18496/60000 [========>.....................] - ETA: 57s - loss: 0.3462 - categorical_accuracy: 0.8922
18560/60000 [========>.....................] - ETA: 56s - loss: 0.3459 - categorical_accuracy: 0.8922
18624/60000 [========>.....................] - ETA: 56s - loss: 0.3453 - categorical_accuracy: 0.8924
18688/60000 [========>.....................] - ETA: 56s - loss: 0.3442 - categorical_accuracy: 0.8927
18752/60000 [========>.....................] - ETA: 56s - loss: 0.3435 - categorical_accuracy: 0.8929
18816/60000 [========>.....................] - ETA: 56s - loss: 0.3426 - categorical_accuracy: 0.8931
18880/60000 [========>.....................] - ETA: 56s - loss: 0.3420 - categorical_accuracy: 0.8934
18944/60000 [========>.....................] - ETA: 56s - loss: 0.3414 - categorical_accuracy: 0.8935
19008/60000 [========>.....................] - ETA: 56s - loss: 0.3416 - categorical_accuracy: 0.8935
19072/60000 [========>.....................] - ETA: 56s - loss: 0.3406 - categorical_accuracy: 0.8938
19136/60000 [========>.....................] - ETA: 56s - loss: 0.3397 - categorical_accuracy: 0.8941
19200/60000 [========>.....................] - ETA: 56s - loss: 0.3389 - categorical_accuracy: 0.8943
19264/60000 [========>.....................] - ETA: 56s - loss: 0.3383 - categorical_accuracy: 0.8944
19328/60000 [========>.....................] - ETA: 55s - loss: 0.3376 - categorical_accuracy: 0.8946
19392/60000 [========>.....................] - ETA: 55s - loss: 0.3370 - categorical_accuracy: 0.8948
19456/60000 [========>.....................] - ETA: 55s - loss: 0.3363 - categorical_accuracy: 0.8950
19520/60000 [========>.....................] - ETA: 55s - loss: 0.3357 - categorical_accuracy: 0.8952
19584/60000 [========>.....................] - ETA: 55s - loss: 0.3348 - categorical_accuracy: 0.8955
19648/60000 [========>.....................] - ETA: 55s - loss: 0.3340 - categorical_accuracy: 0.8957
19712/60000 [========>.....................] - ETA: 55s - loss: 0.3336 - categorical_accuracy: 0.8959
19776/60000 [========>.....................] - ETA: 55s - loss: 0.3333 - categorical_accuracy: 0.8959
19840/60000 [========>.....................] - ETA: 55s - loss: 0.3325 - categorical_accuracy: 0.8962
19904/60000 [========>.....................] - ETA: 55s - loss: 0.3319 - categorical_accuracy: 0.8964
19968/60000 [========>.....................] - ETA: 55s - loss: 0.3317 - categorical_accuracy: 0.8965
20032/60000 [=========>....................] - ETA: 55s - loss: 0.3313 - categorical_accuracy: 0.8967
20096/60000 [=========>....................] - ETA: 54s - loss: 0.3304 - categorical_accuracy: 0.8969
20160/60000 [=========>....................] - ETA: 54s - loss: 0.3295 - categorical_accuracy: 0.8973
20224/60000 [=========>....................] - ETA: 54s - loss: 0.3288 - categorical_accuracy: 0.8974
20288/60000 [=========>....................] - ETA: 54s - loss: 0.3283 - categorical_accuracy: 0.8976
20352/60000 [=========>....................] - ETA: 54s - loss: 0.3277 - categorical_accuracy: 0.8977
20416/60000 [=========>....................] - ETA: 54s - loss: 0.3269 - categorical_accuracy: 0.8980
20480/60000 [=========>....................] - ETA: 54s - loss: 0.3262 - categorical_accuracy: 0.8982
20544/60000 [=========>....................] - ETA: 54s - loss: 0.3256 - categorical_accuracy: 0.8983
20608/60000 [=========>....................] - ETA: 54s - loss: 0.3249 - categorical_accuracy: 0.8985
20672/60000 [=========>....................] - ETA: 54s - loss: 0.3240 - categorical_accuracy: 0.8988
20736/60000 [=========>....................] - ETA: 54s - loss: 0.3232 - categorical_accuracy: 0.8991
20800/60000 [=========>....................] - ETA: 53s - loss: 0.3227 - categorical_accuracy: 0.8992
20864/60000 [=========>....................] - ETA: 53s - loss: 0.3220 - categorical_accuracy: 0.8994
20928/60000 [=========>....................] - ETA: 53s - loss: 0.3213 - categorical_accuracy: 0.8996
20960/60000 [=========>....................] - ETA: 53s - loss: 0.3209 - categorical_accuracy: 0.8997
21024/60000 [=========>....................] - ETA: 53s - loss: 0.3202 - categorical_accuracy: 0.9000
21088/60000 [=========>....................] - ETA: 53s - loss: 0.3199 - categorical_accuracy: 0.9001
21152/60000 [=========>....................] - ETA: 53s - loss: 0.3194 - categorical_accuracy: 0.9003
21216/60000 [=========>....................] - ETA: 53s - loss: 0.3186 - categorical_accuracy: 0.9005
21280/60000 [=========>....................] - ETA: 53s - loss: 0.3177 - categorical_accuracy: 0.9008
21344/60000 [=========>....................] - ETA: 53s - loss: 0.3174 - categorical_accuracy: 0.9009
21408/60000 [=========>....................] - ETA: 53s - loss: 0.3170 - categorical_accuracy: 0.9010
21472/60000 [=========>....................] - ETA: 53s - loss: 0.3163 - categorical_accuracy: 0.9012
21536/60000 [=========>....................] - ETA: 53s - loss: 0.3159 - categorical_accuracy: 0.9013
21600/60000 [=========>....................] - ETA: 52s - loss: 0.3152 - categorical_accuracy: 0.9016
21664/60000 [=========>....................] - ETA: 52s - loss: 0.3145 - categorical_accuracy: 0.9018
21728/60000 [=========>....................] - ETA: 52s - loss: 0.3142 - categorical_accuracy: 0.9019
21792/60000 [=========>....................] - ETA: 52s - loss: 0.3138 - categorical_accuracy: 0.9020
21856/60000 [=========>....................] - ETA: 52s - loss: 0.3132 - categorical_accuracy: 0.9022
21920/60000 [=========>....................] - ETA: 52s - loss: 0.3127 - categorical_accuracy: 0.9024
21984/60000 [=========>....................] - ETA: 52s - loss: 0.3124 - categorical_accuracy: 0.9025
22048/60000 [==========>...................] - ETA: 52s - loss: 0.3120 - categorical_accuracy: 0.9026
22112/60000 [==========>...................] - ETA: 52s - loss: 0.3115 - categorical_accuracy: 0.9028
22176/60000 [==========>...................] - ETA: 52s - loss: 0.3114 - categorical_accuracy: 0.9029
22240/60000 [==========>...................] - ETA: 52s - loss: 0.3106 - categorical_accuracy: 0.9031
22272/60000 [==========>...................] - ETA: 51s - loss: 0.3102 - categorical_accuracy: 0.9032
22304/60000 [==========>...................] - ETA: 51s - loss: 0.3099 - categorical_accuracy: 0.9033
22368/60000 [==========>...................] - ETA: 51s - loss: 0.3097 - categorical_accuracy: 0.9034
22432/60000 [==========>...................] - ETA: 51s - loss: 0.3096 - categorical_accuracy: 0.9035
22496/60000 [==========>...................] - ETA: 51s - loss: 0.3092 - categorical_accuracy: 0.9036
22528/60000 [==========>...................] - ETA: 51s - loss: 0.3089 - categorical_accuracy: 0.9037
22592/60000 [==========>...................] - ETA: 51s - loss: 0.3083 - categorical_accuracy: 0.9039
22656/60000 [==========>...................] - ETA: 51s - loss: 0.3079 - categorical_accuracy: 0.9040
22720/60000 [==========>...................] - ETA: 51s - loss: 0.3077 - categorical_accuracy: 0.9042
22784/60000 [==========>...................] - ETA: 51s - loss: 0.3077 - categorical_accuracy: 0.9042
22848/60000 [==========>...................] - ETA: 51s - loss: 0.3074 - categorical_accuracy: 0.9043
22912/60000 [==========>...................] - ETA: 51s - loss: 0.3071 - categorical_accuracy: 0.9043
22976/60000 [==========>...................] - ETA: 51s - loss: 0.3065 - categorical_accuracy: 0.9046
23040/60000 [==========>...................] - ETA: 50s - loss: 0.3058 - categorical_accuracy: 0.9047
23072/60000 [==========>...................] - ETA: 50s - loss: 0.3055 - categorical_accuracy: 0.9049
23136/60000 [==========>...................] - ETA: 50s - loss: 0.3053 - categorical_accuracy: 0.9049
23200/60000 [==========>...................] - ETA: 50s - loss: 0.3046 - categorical_accuracy: 0.9050
23264/60000 [==========>...................] - ETA: 50s - loss: 0.3046 - categorical_accuracy: 0.9050
23328/60000 [==========>...................] - ETA: 50s - loss: 0.3047 - categorical_accuracy: 0.9051
23392/60000 [==========>...................] - ETA: 50s - loss: 0.3047 - categorical_accuracy: 0.9051
23424/60000 [==========>...................] - ETA: 50s - loss: 0.3044 - categorical_accuracy: 0.9052
23488/60000 [==========>...................] - ETA: 50s - loss: 0.3042 - categorical_accuracy: 0.9054
23552/60000 [==========>...................] - ETA: 50s - loss: 0.3036 - categorical_accuracy: 0.9055
23616/60000 [==========>...................] - ETA: 50s - loss: 0.3037 - categorical_accuracy: 0.9056
23680/60000 [==========>...................] - ETA: 50s - loss: 0.3033 - categorical_accuracy: 0.9057
23744/60000 [==========>...................] - ETA: 50s - loss: 0.3031 - categorical_accuracy: 0.9059
23808/60000 [==========>...................] - ETA: 49s - loss: 0.3033 - categorical_accuracy: 0.9059
23872/60000 [==========>...................] - ETA: 49s - loss: 0.3026 - categorical_accuracy: 0.9060
23936/60000 [==========>...................] - ETA: 49s - loss: 0.3022 - categorical_accuracy: 0.9062
24000/60000 [===========>..................] - ETA: 49s - loss: 0.3016 - categorical_accuracy: 0.9064
24064/60000 [===========>..................] - ETA: 49s - loss: 0.3011 - categorical_accuracy: 0.9065
24128/60000 [===========>..................] - ETA: 49s - loss: 0.3005 - categorical_accuracy: 0.9067
24192/60000 [===========>..................] - ETA: 49s - loss: 0.3005 - categorical_accuracy: 0.9067
24256/60000 [===========>..................] - ETA: 49s - loss: 0.3002 - categorical_accuracy: 0.9069
24320/60000 [===========>..................] - ETA: 49s - loss: 0.2996 - categorical_accuracy: 0.9071
24384/60000 [===========>..................] - ETA: 49s - loss: 0.2990 - categorical_accuracy: 0.9072
24448/60000 [===========>..................] - ETA: 49s - loss: 0.2984 - categorical_accuracy: 0.9074
24512/60000 [===========>..................] - ETA: 49s - loss: 0.2981 - categorical_accuracy: 0.9075
24576/60000 [===========>..................] - ETA: 48s - loss: 0.2979 - categorical_accuracy: 0.9075
24640/60000 [===========>..................] - ETA: 48s - loss: 0.2974 - categorical_accuracy: 0.9076
24704/60000 [===========>..................] - ETA: 48s - loss: 0.2968 - categorical_accuracy: 0.9078
24768/60000 [===========>..................] - ETA: 48s - loss: 0.2964 - categorical_accuracy: 0.9079
24832/60000 [===========>..................] - ETA: 48s - loss: 0.2967 - categorical_accuracy: 0.9079
24896/60000 [===========>..................] - ETA: 48s - loss: 0.2963 - categorical_accuracy: 0.9081
24960/60000 [===========>..................] - ETA: 48s - loss: 0.2957 - categorical_accuracy: 0.9083
25024/60000 [===========>..................] - ETA: 48s - loss: 0.2954 - categorical_accuracy: 0.9084
25088/60000 [===========>..................] - ETA: 48s - loss: 0.2948 - categorical_accuracy: 0.9086
25152/60000 [===========>..................] - ETA: 48s - loss: 0.2942 - categorical_accuracy: 0.9088
25216/60000 [===========>..................] - ETA: 48s - loss: 0.2940 - categorical_accuracy: 0.9088
25280/60000 [===========>..................] - ETA: 47s - loss: 0.2935 - categorical_accuracy: 0.9089
25312/60000 [===========>..................] - ETA: 47s - loss: 0.2933 - categorical_accuracy: 0.9090
25376/60000 [===========>..................] - ETA: 47s - loss: 0.2926 - categorical_accuracy: 0.9092
25440/60000 [===========>..................] - ETA: 47s - loss: 0.2922 - categorical_accuracy: 0.9093
25504/60000 [===========>..................] - ETA: 47s - loss: 0.2916 - categorical_accuracy: 0.9094
25568/60000 [===========>..................] - ETA: 47s - loss: 0.2912 - categorical_accuracy: 0.9095
25632/60000 [===========>..................] - ETA: 47s - loss: 0.2908 - categorical_accuracy: 0.9096
25696/60000 [===========>..................] - ETA: 47s - loss: 0.2907 - categorical_accuracy: 0.9097
25760/60000 [===========>..................] - ETA: 47s - loss: 0.2902 - categorical_accuracy: 0.9099
25824/60000 [===========>..................] - ETA: 47s - loss: 0.2901 - categorical_accuracy: 0.9100
25888/60000 [===========>..................] - ETA: 47s - loss: 0.2895 - categorical_accuracy: 0.9102
25952/60000 [===========>..................] - ETA: 47s - loss: 0.2889 - categorical_accuracy: 0.9105
26016/60000 [============>.................] - ETA: 47s - loss: 0.2884 - categorical_accuracy: 0.9106
26080/60000 [============>.................] - ETA: 46s - loss: 0.2880 - categorical_accuracy: 0.9107
26144/60000 [============>.................] - ETA: 46s - loss: 0.2875 - categorical_accuracy: 0.9109
26208/60000 [============>.................] - ETA: 46s - loss: 0.2873 - categorical_accuracy: 0.9109
26272/60000 [============>.................] - ETA: 46s - loss: 0.2868 - categorical_accuracy: 0.9111
26336/60000 [============>.................] - ETA: 46s - loss: 0.2863 - categorical_accuracy: 0.9113
26400/60000 [============>.................] - ETA: 46s - loss: 0.2858 - categorical_accuracy: 0.9114
26464/60000 [============>.................] - ETA: 46s - loss: 0.2855 - categorical_accuracy: 0.9115
26528/60000 [============>.................] - ETA: 46s - loss: 0.2850 - categorical_accuracy: 0.9117
26592/60000 [============>.................] - ETA: 46s - loss: 0.2845 - categorical_accuracy: 0.9118
26656/60000 [============>.................] - ETA: 46s - loss: 0.2841 - categorical_accuracy: 0.9119
26720/60000 [============>.................] - ETA: 46s - loss: 0.2835 - categorical_accuracy: 0.9121
26784/60000 [============>.................] - ETA: 45s - loss: 0.2834 - categorical_accuracy: 0.9122
26848/60000 [============>.................] - ETA: 45s - loss: 0.2830 - categorical_accuracy: 0.9123
26912/60000 [============>.................] - ETA: 45s - loss: 0.2827 - categorical_accuracy: 0.9124
26976/60000 [============>.................] - ETA: 45s - loss: 0.2823 - categorical_accuracy: 0.9125
27040/60000 [============>.................] - ETA: 45s - loss: 0.2822 - categorical_accuracy: 0.9126
27104/60000 [============>.................] - ETA: 45s - loss: 0.2819 - categorical_accuracy: 0.9127
27168/60000 [============>.................] - ETA: 45s - loss: 0.2814 - categorical_accuracy: 0.9129
27232/60000 [============>.................] - ETA: 45s - loss: 0.2812 - categorical_accuracy: 0.9128
27296/60000 [============>.................] - ETA: 45s - loss: 0.2808 - categorical_accuracy: 0.9130
27360/60000 [============>.................] - ETA: 45s - loss: 0.2807 - categorical_accuracy: 0.9130
27424/60000 [============>.................] - ETA: 45s - loss: 0.2804 - categorical_accuracy: 0.9131
27488/60000 [============>.................] - ETA: 44s - loss: 0.2799 - categorical_accuracy: 0.9133
27552/60000 [============>.................] - ETA: 44s - loss: 0.2796 - categorical_accuracy: 0.9134
27616/60000 [============>.................] - ETA: 44s - loss: 0.2796 - categorical_accuracy: 0.9133
27680/60000 [============>.................] - ETA: 44s - loss: 0.2792 - categorical_accuracy: 0.9134
27744/60000 [============>.................] - ETA: 44s - loss: 0.2791 - categorical_accuracy: 0.9135
27808/60000 [============>.................] - ETA: 44s - loss: 0.2789 - categorical_accuracy: 0.9136
27872/60000 [============>.................] - ETA: 44s - loss: 0.2784 - categorical_accuracy: 0.9138
27936/60000 [============>.................] - ETA: 44s - loss: 0.2782 - categorical_accuracy: 0.9138
28000/60000 [=============>................] - ETA: 44s - loss: 0.2783 - categorical_accuracy: 0.9139
28064/60000 [=============>................] - ETA: 44s - loss: 0.2778 - categorical_accuracy: 0.9141
28128/60000 [=============>................] - ETA: 44s - loss: 0.2773 - categorical_accuracy: 0.9142
28192/60000 [=============>................] - ETA: 43s - loss: 0.2772 - categorical_accuracy: 0.9143
28256/60000 [=============>................] - ETA: 43s - loss: 0.2769 - categorical_accuracy: 0.9144
28320/60000 [=============>................] - ETA: 43s - loss: 0.2767 - categorical_accuracy: 0.9145
28384/60000 [=============>................] - ETA: 43s - loss: 0.2763 - categorical_accuracy: 0.9147
28448/60000 [=============>................] - ETA: 43s - loss: 0.2763 - categorical_accuracy: 0.9148
28480/60000 [=============>................] - ETA: 43s - loss: 0.2760 - categorical_accuracy: 0.9149
28544/60000 [=============>................] - ETA: 43s - loss: 0.2755 - categorical_accuracy: 0.9150
28608/60000 [=============>................] - ETA: 43s - loss: 0.2752 - categorical_accuracy: 0.9151
28672/60000 [=============>................] - ETA: 43s - loss: 0.2749 - categorical_accuracy: 0.9152
28736/60000 [=============>................] - ETA: 43s - loss: 0.2747 - categorical_accuracy: 0.9153
28768/60000 [=============>................] - ETA: 43s - loss: 0.2744 - categorical_accuracy: 0.9154
28832/60000 [=============>................] - ETA: 43s - loss: 0.2742 - categorical_accuracy: 0.9154
28864/60000 [=============>................] - ETA: 43s - loss: 0.2740 - categorical_accuracy: 0.9155
28928/60000 [=============>................] - ETA: 42s - loss: 0.2734 - categorical_accuracy: 0.9157
28992/60000 [=============>................] - ETA: 42s - loss: 0.2728 - categorical_accuracy: 0.9159
29056/60000 [=============>................] - ETA: 42s - loss: 0.2725 - categorical_accuracy: 0.9160
29120/60000 [=============>................] - ETA: 42s - loss: 0.2722 - categorical_accuracy: 0.9161
29152/60000 [=============>................] - ETA: 42s - loss: 0.2722 - categorical_accuracy: 0.9161
29216/60000 [=============>................] - ETA: 42s - loss: 0.2722 - categorical_accuracy: 0.9162
29280/60000 [=============>................] - ETA: 42s - loss: 0.2718 - categorical_accuracy: 0.9163
29344/60000 [=============>................] - ETA: 42s - loss: 0.2716 - categorical_accuracy: 0.9164
29408/60000 [=============>................] - ETA: 42s - loss: 0.2713 - categorical_accuracy: 0.9165
29472/60000 [=============>................] - ETA: 42s - loss: 0.2709 - categorical_accuracy: 0.9166
29536/60000 [=============>................] - ETA: 42s - loss: 0.2710 - categorical_accuracy: 0.9166
29600/60000 [=============>................] - ETA: 42s - loss: 0.2707 - categorical_accuracy: 0.9167
29664/60000 [=============>................] - ETA: 41s - loss: 0.2703 - categorical_accuracy: 0.9168
29728/60000 [=============>................] - ETA: 41s - loss: 0.2697 - categorical_accuracy: 0.9170
29792/60000 [=============>................] - ETA: 41s - loss: 0.2695 - categorical_accuracy: 0.9170
29856/60000 [=============>................] - ETA: 41s - loss: 0.2697 - categorical_accuracy: 0.9171
29920/60000 [=============>................] - ETA: 41s - loss: 0.2695 - categorical_accuracy: 0.9172
29984/60000 [=============>................] - ETA: 41s - loss: 0.2692 - categorical_accuracy: 0.9173
30016/60000 [==============>...............] - ETA: 41s - loss: 0.2691 - categorical_accuracy: 0.9173
30080/60000 [==============>...............] - ETA: 41s - loss: 0.2688 - categorical_accuracy: 0.9174
30144/60000 [==============>...............] - ETA: 41s - loss: 0.2686 - categorical_accuracy: 0.9174
30208/60000 [==============>...............] - ETA: 41s - loss: 0.2682 - categorical_accuracy: 0.9175
30272/60000 [==============>...............] - ETA: 41s - loss: 0.2678 - categorical_accuracy: 0.9177
30336/60000 [==============>...............] - ETA: 41s - loss: 0.2674 - categorical_accuracy: 0.9178
30400/60000 [==============>...............] - ETA: 40s - loss: 0.2671 - categorical_accuracy: 0.9179
30464/60000 [==============>...............] - ETA: 40s - loss: 0.2667 - categorical_accuracy: 0.9180
30528/60000 [==============>...............] - ETA: 40s - loss: 0.2666 - categorical_accuracy: 0.9180
30592/60000 [==============>...............] - ETA: 40s - loss: 0.2668 - categorical_accuracy: 0.9180
30656/60000 [==============>...............] - ETA: 40s - loss: 0.2664 - categorical_accuracy: 0.9181
30720/60000 [==============>...............] - ETA: 40s - loss: 0.2661 - categorical_accuracy: 0.9182
30784/60000 [==============>...............] - ETA: 40s - loss: 0.2660 - categorical_accuracy: 0.9183
30848/60000 [==============>...............] - ETA: 40s - loss: 0.2657 - categorical_accuracy: 0.9184
30912/60000 [==============>...............] - ETA: 40s - loss: 0.2653 - categorical_accuracy: 0.9185
30976/60000 [==============>...............] - ETA: 40s - loss: 0.2649 - categorical_accuracy: 0.9186
31040/60000 [==============>...............] - ETA: 40s - loss: 0.2646 - categorical_accuracy: 0.9187
31104/60000 [==============>...............] - ETA: 39s - loss: 0.2642 - categorical_accuracy: 0.9188
31168/60000 [==============>...............] - ETA: 39s - loss: 0.2637 - categorical_accuracy: 0.9190
31232/60000 [==============>...............] - ETA: 39s - loss: 0.2633 - categorical_accuracy: 0.9191
31296/60000 [==============>...............] - ETA: 39s - loss: 0.2630 - categorical_accuracy: 0.9192
31360/60000 [==============>...............] - ETA: 39s - loss: 0.2628 - categorical_accuracy: 0.9192
31424/60000 [==============>...............] - ETA: 39s - loss: 0.2628 - categorical_accuracy: 0.9192
31488/60000 [==============>...............] - ETA: 39s - loss: 0.2628 - categorical_accuracy: 0.9192
31552/60000 [==============>...............] - ETA: 39s - loss: 0.2626 - categorical_accuracy: 0.9193
31616/60000 [==============>...............] - ETA: 39s - loss: 0.2623 - categorical_accuracy: 0.9193
31680/60000 [==============>...............] - ETA: 39s - loss: 0.2621 - categorical_accuracy: 0.9194
31744/60000 [==============>...............] - ETA: 39s - loss: 0.2618 - categorical_accuracy: 0.9195
31808/60000 [==============>...............] - ETA: 38s - loss: 0.2620 - categorical_accuracy: 0.9195
31872/60000 [==============>...............] - ETA: 38s - loss: 0.2623 - categorical_accuracy: 0.9194
31936/60000 [==============>...............] - ETA: 38s - loss: 0.2624 - categorical_accuracy: 0.9194
31968/60000 [==============>...............] - ETA: 38s - loss: 0.2623 - categorical_accuracy: 0.9194
32032/60000 [===============>..............] - ETA: 38s - loss: 0.2619 - categorical_accuracy: 0.9195
32096/60000 [===============>..............] - ETA: 38s - loss: 0.2615 - categorical_accuracy: 0.9196
32128/60000 [===============>..............] - ETA: 38s - loss: 0.2613 - categorical_accuracy: 0.9197
32192/60000 [===============>..............] - ETA: 38s - loss: 0.2609 - categorical_accuracy: 0.9199
32256/60000 [===============>..............] - ETA: 38s - loss: 0.2605 - categorical_accuracy: 0.9200
32320/60000 [===============>..............] - ETA: 38s - loss: 0.2604 - categorical_accuracy: 0.9200
32384/60000 [===============>..............] - ETA: 38s - loss: 0.2601 - categorical_accuracy: 0.9201
32448/60000 [===============>..............] - ETA: 38s - loss: 0.2597 - categorical_accuracy: 0.9202
32480/60000 [===============>..............] - ETA: 38s - loss: 0.2597 - categorical_accuracy: 0.9202
32544/60000 [===============>..............] - ETA: 37s - loss: 0.2593 - categorical_accuracy: 0.9203
32608/60000 [===============>..............] - ETA: 37s - loss: 0.2589 - categorical_accuracy: 0.9204
32672/60000 [===============>..............] - ETA: 37s - loss: 0.2588 - categorical_accuracy: 0.9205
32736/60000 [===============>..............] - ETA: 37s - loss: 0.2588 - categorical_accuracy: 0.9205
32800/60000 [===============>..............] - ETA: 37s - loss: 0.2587 - categorical_accuracy: 0.9205
32864/60000 [===============>..............] - ETA: 37s - loss: 0.2584 - categorical_accuracy: 0.9206
32928/60000 [===============>..............] - ETA: 37s - loss: 0.2581 - categorical_accuracy: 0.9207
32992/60000 [===============>..............] - ETA: 37s - loss: 0.2577 - categorical_accuracy: 0.9208
33056/60000 [===============>..............] - ETA: 37s - loss: 0.2574 - categorical_accuracy: 0.9209
33120/60000 [===============>..............] - ETA: 37s - loss: 0.2570 - categorical_accuracy: 0.9210
33184/60000 [===============>..............] - ETA: 37s - loss: 0.2569 - categorical_accuracy: 0.9210
33248/60000 [===============>..............] - ETA: 37s - loss: 0.2567 - categorical_accuracy: 0.9211
33312/60000 [===============>..............] - ETA: 36s - loss: 0.2565 - categorical_accuracy: 0.9212
33376/60000 [===============>..............] - ETA: 36s - loss: 0.2562 - categorical_accuracy: 0.9213
33408/60000 [===============>..............] - ETA: 36s - loss: 0.2561 - categorical_accuracy: 0.9213
33472/60000 [===============>..............] - ETA: 36s - loss: 0.2558 - categorical_accuracy: 0.9215
33536/60000 [===============>..............] - ETA: 36s - loss: 0.2557 - categorical_accuracy: 0.9215
33600/60000 [===============>..............] - ETA: 36s - loss: 0.2555 - categorical_accuracy: 0.9215
33664/60000 [===============>..............] - ETA: 36s - loss: 0.2553 - categorical_accuracy: 0.9215
33728/60000 [===============>..............] - ETA: 36s - loss: 0.2552 - categorical_accuracy: 0.9216
33792/60000 [===============>..............] - ETA: 36s - loss: 0.2548 - categorical_accuracy: 0.9217
33856/60000 [===============>..............] - ETA: 36s - loss: 0.2546 - categorical_accuracy: 0.9218
33920/60000 [===============>..............] - ETA: 36s - loss: 0.2545 - categorical_accuracy: 0.9218
33984/60000 [===============>..............] - ETA: 35s - loss: 0.2543 - categorical_accuracy: 0.9218
34048/60000 [================>.............] - ETA: 35s - loss: 0.2540 - categorical_accuracy: 0.9219
34112/60000 [================>.............] - ETA: 35s - loss: 0.2537 - categorical_accuracy: 0.9220
34144/60000 [================>.............] - ETA: 35s - loss: 0.2535 - categorical_accuracy: 0.9220
34208/60000 [================>.............] - ETA: 35s - loss: 0.2532 - categorical_accuracy: 0.9221
34272/60000 [================>.............] - ETA: 35s - loss: 0.2528 - categorical_accuracy: 0.9222
34304/60000 [================>.............] - ETA: 35s - loss: 0.2526 - categorical_accuracy: 0.9223
34368/60000 [================>.............] - ETA: 35s - loss: 0.2524 - categorical_accuracy: 0.9223
34432/60000 [================>.............] - ETA: 35s - loss: 0.2520 - categorical_accuracy: 0.9224
34496/60000 [================>.............] - ETA: 35s - loss: 0.2516 - categorical_accuracy: 0.9225
34560/60000 [================>.............] - ETA: 35s - loss: 0.2512 - categorical_accuracy: 0.9227
34624/60000 [================>.............] - ETA: 35s - loss: 0.2509 - categorical_accuracy: 0.9228
34688/60000 [================>.............] - ETA: 35s - loss: 0.2509 - categorical_accuracy: 0.9228
34752/60000 [================>.............] - ETA: 34s - loss: 0.2510 - categorical_accuracy: 0.9229
34816/60000 [================>.............] - ETA: 34s - loss: 0.2507 - categorical_accuracy: 0.9230
34880/60000 [================>.............] - ETA: 34s - loss: 0.2504 - categorical_accuracy: 0.9231
34944/60000 [================>.............] - ETA: 34s - loss: 0.2500 - categorical_accuracy: 0.9232
35008/60000 [================>.............] - ETA: 34s - loss: 0.2498 - categorical_accuracy: 0.9232
35072/60000 [================>.............] - ETA: 34s - loss: 0.2497 - categorical_accuracy: 0.9232
35136/60000 [================>.............] - ETA: 34s - loss: 0.2496 - categorical_accuracy: 0.9233
35200/60000 [================>.............] - ETA: 34s - loss: 0.2494 - categorical_accuracy: 0.9234
35264/60000 [================>.............] - ETA: 34s - loss: 0.2492 - categorical_accuracy: 0.9234
35328/60000 [================>.............] - ETA: 34s - loss: 0.2489 - categorical_accuracy: 0.9235
35392/60000 [================>.............] - ETA: 34s - loss: 0.2487 - categorical_accuracy: 0.9236
35456/60000 [================>.............] - ETA: 33s - loss: 0.2483 - categorical_accuracy: 0.9237
35520/60000 [================>.............] - ETA: 33s - loss: 0.2480 - categorical_accuracy: 0.9238
35584/60000 [================>.............] - ETA: 33s - loss: 0.2478 - categorical_accuracy: 0.9238
35648/60000 [================>.............] - ETA: 33s - loss: 0.2474 - categorical_accuracy: 0.9239
35712/60000 [================>.............] - ETA: 33s - loss: 0.2474 - categorical_accuracy: 0.9239
35776/60000 [================>.............] - ETA: 33s - loss: 0.2471 - categorical_accuracy: 0.9240
35840/60000 [================>.............] - ETA: 33s - loss: 0.2467 - categorical_accuracy: 0.9241
35904/60000 [================>.............] - ETA: 33s - loss: 0.2464 - categorical_accuracy: 0.9242
35968/60000 [================>.............] - ETA: 33s - loss: 0.2462 - categorical_accuracy: 0.9243
36032/60000 [=================>............] - ETA: 33s - loss: 0.2460 - categorical_accuracy: 0.9243
36096/60000 [=================>............] - ETA: 33s - loss: 0.2457 - categorical_accuracy: 0.9245
36160/60000 [=================>............] - ETA: 33s - loss: 0.2453 - categorical_accuracy: 0.9246
36224/60000 [=================>............] - ETA: 32s - loss: 0.2451 - categorical_accuracy: 0.9246
36288/60000 [=================>............] - ETA: 32s - loss: 0.2453 - categorical_accuracy: 0.9247
36352/60000 [=================>............] - ETA: 32s - loss: 0.2449 - categorical_accuracy: 0.9248
36416/60000 [=================>............] - ETA: 32s - loss: 0.2447 - categorical_accuracy: 0.9248
36480/60000 [=================>............] - ETA: 32s - loss: 0.2445 - categorical_accuracy: 0.9249
36512/60000 [=================>............] - ETA: 32s - loss: 0.2443 - categorical_accuracy: 0.9250
36576/60000 [=================>............] - ETA: 32s - loss: 0.2440 - categorical_accuracy: 0.9251
36640/60000 [=================>............] - ETA: 32s - loss: 0.2439 - categorical_accuracy: 0.9252
36704/60000 [=================>............] - ETA: 32s - loss: 0.2435 - categorical_accuracy: 0.9253
36768/60000 [=================>............] - ETA: 32s - loss: 0.2432 - categorical_accuracy: 0.9254
36832/60000 [=================>............] - ETA: 32s - loss: 0.2430 - categorical_accuracy: 0.9255
36896/60000 [=================>............] - ETA: 31s - loss: 0.2428 - categorical_accuracy: 0.9255
36960/60000 [=================>............] - ETA: 31s - loss: 0.2426 - categorical_accuracy: 0.9256
37024/60000 [=================>............] - ETA: 31s - loss: 0.2423 - categorical_accuracy: 0.9257
37088/60000 [=================>............] - ETA: 31s - loss: 0.2420 - categorical_accuracy: 0.9258
37152/60000 [=================>............] - ETA: 31s - loss: 0.2417 - categorical_accuracy: 0.9258
37216/60000 [=================>............] - ETA: 31s - loss: 0.2415 - categorical_accuracy: 0.9259
37280/60000 [=================>............] - ETA: 31s - loss: 0.2412 - categorical_accuracy: 0.9260
37344/60000 [=================>............] - ETA: 31s - loss: 0.2410 - categorical_accuracy: 0.9260
37408/60000 [=================>............] - ETA: 31s - loss: 0.2410 - categorical_accuracy: 0.9260
37472/60000 [=================>............] - ETA: 31s - loss: 0.2409 - categorical_accuracy: 0.9260
37536/60000 [=================>............] - ETA: 31s - loss: 0.2407 - categorical_accuracy: 0.9261
37600/60000 [=================>............] - ETA: 31s - loss: 0.2407 - categorical_accuracy: 0.9261
37664/60000 [=================>............] - ETA: 30s - loss: 0.2405 - categorical_accuracy: 0.9262
37728/60000 [=================>............] - ETA: 30s - loss: 0.2401 - categorical_accuracy: 0.9263
37792/60000 [=================>............] - ETA: 30s - loss: 0.2400 - categorical_accuracy: 0.9263
37856/60000 [=================>............] - ETA: 30s - loss: 0.2396 - categorical_accuracy: 0.9265
37920/60000 [=================>............] - ETA: 30s - loss: 0.2393 - categorical_accuracy: 0.9265
37984/60000 [=================>............] - ETA: 30s - loss: 0.2392 - categorical_accuracy: 0.9265
38048/60000 [==================>...........] - ETA: 30s - loss: 0.2389 - categorical_accuracy: 0.9266
38112/60000 [==================>...........] - ETA: 30s - loss: 0.2387 - categorical_accuracy: 0.9267
38176/60000 [==================>...........] - ETA: 30s - loss: 0.2384 - categorical_accuracy: 0.9268
38240/60000 [==================>...........] - ETA: 30s - loss: 0.2383 - categorical_accuracy: 0.9268
38304/60000 [==================>...........] - ETA: 30s - loss: 0.2381 - categorical_accuracy: 0.9268
38368/60000 [==================>...........] - ETA: 29s - loss: 0.2378 - categorical_accuracy: 0.9269
38432/60000 [==================>...........] - ETA: 29s - loss: 0.2376 - categorical_accuracy: 0.9270
38496/60000 [==================>...........] - ETA: 29s - loss: 0.2374 - categorical_accuracy: 0.9271
38528/60000 [==================>...........] - ETA: 29s - loss: 0.2372 - categorical_accuracy: 0.9271
38560/60000 [==================>...........] - ETA: 29s - loss: 0.2373 - categorical_accuracy: 0.9272
38624/60000 [==================>...........] - ETA: 29s - loss: 0.2369 - categorical_accuracy: 0.9273
38688/60000 [==================>...........] - ETA: 29s - loss: 0.2368 - categorical_accuracy: 0.9273
38752/60000 [==================>...........] - ETA: 29s - loss: 0.2365 - categorical_accuracy: 0.9274
38816/60000 [==================>...........] - ETA: 29s - loss: 0.2362 - categorical_accuracy: 0.9275
38880/60000 [==================>...........] - ETA: 29s - loss: 0.2361 - categorical_accuracy: 0.9275
38944/60000 [==================>...........] - ETA: 29s - loss: 0.2358 - categorical_accuracy: 0.9276
39008/60000 [==================>...........] - ETA: 29s - loss: 0.2355 - categorical_accuracy: 0.9277
39072/60000 [==================>...........] - ETA: 29s - loss: 0.2354 - categorical_accuracy: 0.9277
39136/60000 [==================>...........] - ETA: 28s - loss: 0.2353 - categorical_accuracy: 0.9277
39200/60000 [==================>...........] - ETA: 28s - loss: 0.2350 - categorical_accuracy: 0.9278
39264/60000 [==================>...........] - ETA: 28s - loss: 0.2348 - categorical_accuracy: 0.9278
39328/60000 [==================>...........] - ETA: 28s - loss: 0.2345 - categorical_accuracy: 0.9280
39392/60000 [==================>...........] - ETA: 28s - loss: 0.2342 - categorical_accuracy: 0.9280
39456/60000 [==================>...........] - ETA: 28s - loss: 0.2339 - categorical_accuracy: 0.9281
39520/60000 [==================>...........] - ETA: 28s - loss: 0.2336 - categorical_accuracy: 0.9282
39584/60000 [==================>...........] - ETA: 28s - loss: 0.2335 - categorical_accuracy: 0.9282
39648/60000 [==================>...........] - ETA: 28s - loss: 0.2334 - categorical_accuracy: 0.9283
39712/60000 [==================>...........] - ETA: 28s - loss: 0.2333 - categorical_accuracy: 0.9283
39776/60000 [==================>...........] - ETA: 28s - loss: 0.2331 - categorical_accuracy: 0.9283
39840/60000 [==================>...........] - ETA: 27s - loss: 0.2329 - categorical_accuracy: 0.9284
39904/60000 [==================>...........] - ETA: 27s - loss: 0.2327 - categorical_accuracy: 0.9284
39936/60000 [==================>...........] - ETA: 27s - loss: 0.2326 - categorical_accuracy: 0.9285
40000/60000 [===================>..........] - ETA: 27s - loss: 0.2326 - categorical_accuracy: 0.9285
40064/60000 [===================>..........] - ETA: 27s - loss: 0.2323 - categorical_accuracy: 0.9286
40128/60000 [===================>..........] - ETA: 27s - loss: 0.2321 - categorical_accuracy: 0.9287
40192/60000 [===================>..........] - ETA: 27s - loss: 0.2320 - categorical_accuracy: 0.9287
40256/60000 [===================>..........] - ETA: 27s - loss: 0.2317 - categorical_accuracy: 0.9288
40320/60000 [===================>..........] - ETA: 27s - loss: 0.2317 - categorical_accuracy: 0.9288
40384/60000 [===================>..........] - ETA: 27s - loss: 0.2315 - categorical_accuracy: 0.9289
40448/60000 [===================>..........] - ETA: 27s - loss: 0.2312 - categorical_accuracy: 0.9290
40512/60000 [===================>..........] - ETA: 26s - loss: 0.2311 - categorical_accuracy: 0.9290
40576/60000 [===================>..........] - ETA: 26s - loss: 0.2309 - categorical_accuracy: 0.9290
40640/60000 [===================>..........] - ETA: 26s - loss: 0.2308 - categorical_accuracy: 0.9291
40704/60000 [===================>..........] - ETA: 26s - loss: 0.2306 - categorical_accuracy: 0.9291
40768/60000 [===================>..........] - ETA: 26s - loss: 0.2305 - categorical_accuracy: 0.9292
40832/60000 [===================>..........] - ETA: 26s - loss: 0.2302 - categorical_accuracy: 0.9293
40896/60000 [===================>..........] - ETA: 26s - loss: 0.2299 - categorical_accuracy: 0.9294
40960/60000 [===================>..........] - ETA: 26s - loss: 0.2297 - categorical_accuracy: 0.9294
41024/60000 [===================>..........] - ETA: 26s - loss: 0.2294 - categorical_accuracy: 0.9295
41088/60000 [===================>..........] - ETA: 26s - loss: 0.2293 - categorical_accuracy: 0.9295
41152/60000 [===================>..........] - ETA: 26s - loss: 0.2291 - categorical_accuracy: 0.9296
41216/60000 [===================>..........] - ETA: 26s - loss: 0.2288 - categorical_accuracy: 0.9296
41280/60000 [===================>..........] - ETA: 25s - loss: 0.2286 - categorical_accuracy: 0.9297
41344/60000 [===================>..........] - ETA: 25s - loss: 0.2285 - categorical_accuracy: 0.9297
41408/60000 [===================>..........] - ETA: 25s - loss: 0.2282 - categorical_accuracy: 0.9297
41472/60000 [===================>..........] - ETA: 25s - loss: 0.2281 - categorical_accuracy: 0.9298
41536/60000 [===================>..........] - ETA: 25s - loss: 0.2279 - categorical_accuracy: 0.9299
41600/60000 [===================>..........] - ETA: 25s - loss: 0.2276 - categorical_accuracy: 0.9299
41664/60000 [===================>..........] - ETA: 25s - loss: 0.2273 - categorical_accuracy: 0.9300
41728/60000 [===================>..........] - ETA: 25s - loss: 0.2274 - categorical_accuracy: 0.9300
41792/60000 [===================>..........] - ETA: 25s - loss: 0.2276 - categorical_accuracy: 0.9300
41856/60000 [===================>..........] - ETA: 25s - loss: 0.2276 - categorical_accuracy: 0.9300
41920/60000 [===================>..........] - ETA: 25s - loss: 0.2273 - categorical_accuracy: 0.9301
41984/60000 [===================>..........] - ETA: 24s - loss: 0.2272 - categorical_accuracy: 0.9301
42048/60000 [====================>.........] - ETA: 24s - loss: 0.2271 - categorical_accuracy: 0.9301
42112/60000 [====================>.........] - ETA: 24s - loss: 0.2269 - categorical_accuracy: 0.9302
42176/60000 [====================>.........] - ETA: 24s - loss: 0.2267 - categorical_accuracy: 0.9303
42240/60000 [====================>.........] - ETA: 24s - loss: 0.2266 - categorical_accuracy: 0.9303
42304/60000 [====================>.........] - ETA: 24s - loss: 0.2264 - categorical_accuracy: 0.9304
42368/60000 [====================>.........] - ETA: 24s - loss: 0.2262 - categorical_accuracy: 0.9304
42432/60000 [====================>.........] - ETA: 24s - loss: 0.2259 - categorical_accuracy: 0.9305
42496/60000 [====================>.........] - ETA: 24s - loss: 0.2257 - categorical_accuracy: 0.9306
42560/60000 [====================>.........] - ETA: 24s - loss: 0.2257 - categorical_accuracy: 0.9306
42624/60000 [====================>.........] - ETA: 24s - loss: 0.2254 - categorical_accuracy: 0.9307
42688/60000 [====================>.........] - ETA: 23s - loss: 0.2253 - categorical_accuracy: 0.9308
42752/60000 [====================>.........] - ETA: 23s - loss: 0.2250 - categorical_accuracy: 0.9309
42816/60000 [====================>.........] - ETA: 23s - loss: 0.2248 - categorical_accuracy: 0.9309
42880/60000 [====================>.........] - ETA: 23s - loss: 0.2245 - categorical_accuracy: 0.9310
42944/60000 [====================>.........] - ETA: 23s - loss: 0.2242 - categorical_accuracy: 0.9311
43008/60000 [====================>.........] - ETA: 23s - loss: 0.2239 - categorical_accuracy: 0.9312
43072/60000 [====================>.........] - ETA: 23s - loss: 0.2237 - categorical_accuracy: 0.9313
43136/60000 [====================>.........] - ETA: 23s - loss: 0.2235 - categorical_accuracy: 0.9313
43200/60000 [====================>.........] - ETA: 23s - loss: 0.2234 - categorical_accuracy: 0.9314
43264/60000 [====================>.........] - ETA: 23s - loss: 0.2231 - categorical_accuracy: 0.9315
43328/60000 [====================>.........] - ETA: 23s - loss: 0.2229 - categorical_accuracy: 0.9315
43392/60000 [====================>.........] - ETA: 22s - loss: 0.2228 - categorical_accuracy: 0.9316
43456/60000 [====================>.........] - ETA: 22s - loss: 0.2228 - categorical_accuracy: 0.9317
43520/60000 [====================>.........] - ETA: 22s - loss: 0.2226 - categorical_accuracy: 0.9317
43584/60000 [====================>.........] - ETA: 22s - loss: 0.2225 - categorical_accuracy: 0.9318
43648/60000 [====================>.........] - ETA: 22s - loss: 0.2223 - categorical_accuracy: 0.9318
43712/60000 [====================>.........] - ETA: 22s - loss: 0.2221 - categorical_accuracy: 0.9319
43776/60000 [====================>.........] - ETA: 22s - loss: 0.2219 - categorical_accuracy: 0.9320
43840/60000 [====================>.........] - ETA: 22s - loss: 0.2218 - categorical_accuracy: 0.9320
43904/60000 [====================>.........] - ETA: 22s - loss: 0.2218 - categorical_accuracy: 0.9320
43968/60000 [====================>.........] - ETA: 22s - loss: 0.2215 - categorical_accuracy: 0.9321
44032/60000 [=====================>........] - ETA: 22s - loss: 0.2213 - categorical_accuracy: 0.9321
44096/60000 [=====================>........] - ETA: 22s - loss: 0.2210 - categorical_accuracy: 0.9322
44160/60000 [=====================>........] - ETA: 21s - loss: 0.2210 - categorical_accuracy: 0.9322
44224/60000 [=====================>........] - ETA: 21s - loss: 0.2209 - categorical_accuracy: 0.9322
44256/60000 [=====================>........] - ETA: 21s - loss: 0.2208 - categorical_accuracy: 0.9323
44320/60000 [=====================>........] - ETA: 21s - loss: 0.2206 - categorical_accuracy: 0.9323
44384/60000 [=====================>........] - ETA: 21s - loss: 0.2205 - categorical_accuracy: 0.9323
44448/60000 [=====================>........] - ETA: 21s - loss: 0.2203 - categorical_accuracy: 0.9324
44512/60000 [=====================>........] - ETA: 21s - loss: 0.2204 - categorical_accuracy: 0.9324
44576/60000 [=====================>........] - ETA: 21s - loss: 0.2203 - categorical_accuracy: 0.9324
44640/60000 [=====================>........] - ETA: 21s - loss: 0.2200 - categorical_accuracy: 0.9325
44704/60000 [=====================>........] - ETA: 21s - loss: 0.2198 - categorical_accuracy: 0.9326
44768/60000 [=====================>........] - ETA: 21s - loss: 0.2196 - categorical_accuracy: 0.9326
44832/60000 [=====================>........] - ETA: 21s - loss: 0.2194 - categorical_accuracy: 0.9327
44896/60000 [=====================>........] - ETA: 20s - loss: 0.2194 - categorical_accuracy: 0.9326
44960/60000 [=====================>........] - ETA: 20s - loss: 0.2192 - categorical_accuracy: 0.9327
45024/60000 [=====================>........] - ETA: 20s - loss: 0.2189 - categorical_accuracy: 0.9328
45088/60000 [=====================>........] - ETA: 20s - loss: 0.2188 - categorical_accuracy: 0.9328
45152/60000 [=====================>........] - ETA: 20s - loss: 0.2187 - categorical_accuracy: 0.9329
45216/60000 [=====================>........] - ETA: 20s - loss: 0.2186 - categorical_accuracy: 0.9329
45280/60000 [=====================>........] - ETA: 20s - loss: 0.2184 - categorical_accuracy: 0.9330
45344/60000 [=====================>........] - ETA: 20s - loss: 0.2183 - categorical_accuracy: 0.9330
45408/60000 [=====================>........] - ETA: 20s - loss: 0.2181 - categorical_accuracy: 0.9331
45472/60000 [=====================>........] - ETA: 20s - loss: 0.2179 - categorical_accuracy: 0.9331
45536/60000 [=====================>........] - ETA: 20s - loss: 0.2179 - categorical_accuracy: 0.9331
45600/60000 [=====================>........] - ETA: 19s - loss: 0.2178 - categorical_accuracy: 0.9332
45664/60000 [=====================>........] - ETA: 19s - loss: 0.2177 - categorical_accuracy: 0.9332
45696/60000 [=====================>........] - ETA: 19s - loss: 0.2178 - categorical_accuracy: 0.9331
45760/60000 [=====================>........] - ETA: 19s - loss: 0.2176 - categorical_accuracy: 0.9332
45824/60000 [=====================>........] - ETA: 19s - loss: 0.2175 - categorical_accuracy: 0.9333
45888/60000 [=====================>........] - ETA: 19s - loss: 0.2172 - categorical_accuracy: 0.9334
45952/60000 [=====================>........] - ETA: 19s - loss: 0.2172 - categorical_accuracy: 0.9334
45984/60000 [=====================>........] - ETA: 19s - loss: 0.2172 - categorical_accuracy: 0.9334
46048/60000 [======================>.......] - ETA: 19s - loss: 0.2170 - categorical_accuracy: 0.9334
46112/60000 [======================>.......] - ETA: 19s - loss: 0.2168 - categorical_accuracy: 0.9335
46176/60000 [======================>.......] - ETA: 19s - loss: 0.2167 - categorical_accuracy: 0.9335
46240/60000 [======================>.......] - ETA: 19s - loss: 0.2164 - categorical_accuracy: 0.9336
46304/60000 [======================>.......] - ETA: 18s - loss: 0.2163 - categorical_accuracy: 0.9337
46368/60000 [======================>.......] - ETA: 18s - loss: 0.2162 - categorical_accuracy: 0.9337
46432/60000 [======================>.......] - ETA: 18s - loss: 0.2160 - categorical_accuracy: 0.9338
46496/60000 [======================>.......] - ETA: 18s - loss: 0.2159 - categorical_accuracy: 0.9338
46560/60000 [======================>.......] - ETA: 18s - loss: 0.2157 - categorical_accuracy: 0.9338
46624/60000 [======================>.......] - ETA: 18s - loss: 0.2154 - categorical_accuracy: 0.9339
46688/60000 [======================>.......] - ETA: 18s - loss: 0.2153 - categorical_accuracy: 0.9340
46752/60000 [======================>.......] - ETA: 18s - loss: 0.2152 - categorical_accuracy: 0.9340
46816/60000 [======================>.......] - ETA: 18s - loss: 0.2149 - categorical_accuracy: 0.9341
46880/60000 [======================>.......] - ETA: 18s - loss: 0.2147 - categorical_accuracy: 0.9342
46944/60000 [======================>.......] - ETA: 18s - loss: 0.2146 - categorical_accuracy: 0.9342
47008/60000 [======================>.......] - ETA: 18s - loss: 0.2145 - categorical_accuracy: 0.9343
47072/60000 [======================>.......] - ETA: 17s - loss: 0.2144 - categorical_accuracy: 0.9342
47136/60000 [======================>.......] - ETA: 17s - loss: 0.2145 - categorical_accuracy: 0.9343
47200/60000 [======================>.......] - ETA: 17s - loss: 0.2143 - categorical_accuracy: 0.9343
47264/60000 [======================>.......] - ETA: 17s - loss: 0.2140 - categorical_accuracy: 0.9344
47328/60000 [======================>.......] - ETA: 17s - loss: 0.2138 - categorical_accuracy: 0.9345
47392/60000 [======================>.......] - ETA: 17s - loss: 0.2138 - categorical_accuracy: 0.9345
47456/60000 [======================>.......] - ETA: 17s - loss: 0.2137 - categorical_accuracy: 0.9345
47520/60000 [======================>.......] - ETA: 17s - loss: 0.2137 - categorical_accuracy: 0.9345
47584/60000 [======================>.......] - ETA: 17s - loss: 0.2135 - categorical_accuracy: 0.9345
47648/60000 [======================>.......] - ETA: 17s - loss: 0.2133 - categorical_accuracy: 0.9346
47680/60000 [======================>.......] - ETA: 17s - loss: 0.2133 - categorical_accuracy: 0.9346
47744/60000 [======================>.......] - ETA: 17s - loss: 0.2131 - categorical_accuracy: 0.9347
47808/60000 [======================>.......] - ETA: 16s - loss: 0.2130 - categorical_accuracy: 0.9348
47872/60000 [======================>.......] - ETA: 16s - loss: 0.2128 - categorical_accuracy: 0.9348
47936/60000 [======================>.......] - ETA: 16s - loss: 0.2126 - categorical_accuracy: 0.9349
48000/60000 [=======================>......] - ETA: 16s - loss: 0.2123 - categorical_accuracy: 0.9350
48064/60000 [=======================>......] - ETA: 16s - loss: 0.2121 - categorical_accuracy: 0.9351
48128/60000 [=======================>......] - ETA: 16s - loss: 0.2119 - categorical_accuracy: 0.9351
48192/60000 [=======================>......] - ETA: 16s - loss: 0.2118 - categorical_accuracy: 0.9352
48256/60000 [=======================>......] - ETA: 16s - loss: 0.2116 - categorical_accuracy: 0.9352
48320/60000 [=======================>......] - ETA: 16s - loss: 0.2114 - categorical_accuracy: 0.9353
48384/60000 [=======================>......] - ETA: 16s - loss: 0.2114 - categorical_accuracy: 0.9353
48448/60000 [=======================>......] - ETA: 16s - loss: 0.2113 - categorical_accuracy: 0.9353
48512/60000 [=======================>......] - ETA: 15s - loss: 0.2111 - categorical_accuracy: 0.9354
48576/60000 [=======================>......] - ETA: 15s - loss: 0.2109 - categorical_accuracy: 0.9354
48608/60000 [=======================>......] - ETA: 15s - loss: 0.2108 - categorical_accuracy: 0.9355
48672/60000 [=======================>......] - ETA: 15s - loss: 0.2105 - categorical_accuracy: 0.9355
48736/60000 [=======================>......] - ETA: 15s - loss: 0.2103 - categorical_accuracy: 0.9356
48800/60000 [=======================>......] - ETA: 15s - loss: 0.2101 - categorical_accuracy: 0.9356
48864/60000 [=======================>......] - ETA: 15s - loss: 0.2100 - categorical_accuracy: 0.9357
48928/60000 [=======================>......] - ETA: 15s - loss: 0.2098 - categorical_accuracy: 0.9357
48992/60000 [=======================>......] - ETA: 15s - loss: 0.2097 - categorical_accuracy: 0.9358
49056/60000 [=======================>......] - ETA: 15s - loss: 0.2095 - categorical_accuracy: 0.9358
49120/60000 [=======================>......] - ETA: 15s - loss: 0.2094 - categorical_accuracy: 0.9358
49184/60000 [=======================>......] - ETA: 14s - loss: 0.2091 - categorical_accuracy: 0.9359
49248/60000 [=======================>......] - ETA: 14s - loss: 0.2091 - categorical_accuracy: 0.9359
49312/60000 [=======================>......] - ETA: 14s - loss: 0.2089 - categorical_accuracy: 0.9359
49376/60000 [=======================>......] - ETA: 14s - loss: 0.2088 - categorical_accuracy: 0.9360
49440/60000 [=======================>......] - ETA: 14s - loss: 0.2085 - categorical_accuracy: 0.9361
49504/60000 [=======================>......] - ETA: 14s - loss: 0.2084 - categorical_accuracy: 0.9361
49568/60000 [=======================>......] - ETA: 14s - loss: 0.2082 - categorical_accuracy: 0.9361
49632/60000 [=======================>......] - ETA: 14s - loss: 0.2080 - categorical_accuracy: 0.9362
49696/60000 [=======================>......] - ETA: 14s - loss: 0.2077 - categorical_accuracy: 0.9363
49728/60000 [=======================>......] - ETA: 14s - loss: 0.2077 - categorical_accuracy: 0.9363
49792/60000 [=======================>......] - ETA: 14s - loss: 0.2076 - categorical_accuracy: 0.9363
49856/60000 [=======================>......] - ETA: 14s - loss: 0.2074 - categorical_accuracy: 0.9363
49920/60000 [=======================>......] - ETA: 13s - loss: 0.2072 - categorical_accuracy: 0.9364
49984/60000 [=======================>......] - ETA: 13s - loss: 0.2070 - categorical_accuracy: 0.9364
50048/60000 [========================>.....] - ETA: 13s - loss: 0.2069 - categorical_accuracy: 0.9365
50112/60000 [========================>.....] - ETA: 13s - loss: 0.2068 - categorical_accuracy: 0.9365
50176/60000 [========================>.....] - ETA: 13s - loss: 0.2066 - categorical_accuracy: 0.9365
50240/60000 [========================>.....] - ETA: 13s - loss: 0.2066 - categorical_accuracy: 0.9365
50304/60000 [========================>.....] - ETA: 13s - loss: 0.2064 - categorical_accuracy: 0.9366
50368/60000 [========================>.....] - ETA: 13s - loss: 0.2063 - categorical_accuracy: 0.9366
50432/60000 [========================>.....] - ETA: 13s - loss: 0.2061 - categorical_accuracy: 0.9367
50496/60000 [========================>.....] - ETA: 13s - loss: 0.2059 - categorical_accuracy: 0.9368
50560/60000 [========================>.....] - ETA: 13s - loss: 0.2057 - categorical_accuracy: 0.9368
50624/60000 [========================>.....] - ETA: 13s - loss: 0.2058 - categorical_accuracy: 0.9369
50688/60000 [========================>.....] - ETA: 12s - loss: 0.2059 - categorical_accuracy: 0.9368
50752/60000 [========================>.....] - ETA: 12s - loss: 0.2057 - categorical_accuracy: 0.9369
50816/60000 [========================>.....] - ETA: 12s - loss: 0.2056 - categorical_accuracy: 0.9370
50848/60000 [========================>.....] - ETA: 12s - loss: 0.2055 - categorical_accuracy: 0.9370
50912/60000 [========================>.....] - ETA: 12s - loss: 0.2055 - categorical_accuracy: 0.9370
50976/60000 [========================>.....] - ETA: 12s - loss: 0.2053 - categorical_accuracy: 0.9371
51040/60000 [========================>.....] - ETA: 12s - loss: 0.2052 - categorical_accuracy: 0.9371
51104/60000 [========================>.....] - ETA: 12s - loss: 0.2050 - categorical_accuracy: 0.9372
51168/60000 [========================>.....] - ETA: 12s - loss: 0.2049 - categorical_accuracy: 0.9372
51232/60000 [========================>.....] - ETA: 12s - loss: 0.2048 - categorical_accuracy: 0.9372
51296/60000 [========================>.....] - ETA: 12s - loss: 0.2048 - categorical_accuracy: 0.9373
51360/60000 [========================>.....] - ETA: 11s - loss: 0.2046 - categorical_accuracy: 0.9373
51424/60000 [========================>.....] - ETA: 11s - loss: 0.2045 - categorical_accuracy: 0.9373
51488/60000 [========================>.....] - ETA: 11s - loss: 0.2043 - categorical_accuracy: 0.9374
51552/60000 [========================>.....] - ETA: 11s - loss: 0.2043 - categorical_accuracy: 0.9375
51616/60000 [========================>.....] - ETA: 11s - loss: 0.2041 - categorical_accuracy: 0.9376
51680/60000 [========================>.....] - ETA: 11s - loss: 0.2042 - categorical_accuracy: 0.9375
51744/60000 [========================>.....] - ETA: 11s - loss: 0.2043 - categorical_accuracy: 0.9375
51808/60000 [========================>.....] - ETA: 11s - loss: 0.2041 - categorical_accuracy: 0.9376
51840/60000 [========================>.....] - ETA: 11s - loss: 0.2040 - categorical_accuracy: 0.9376
51904/60000 [========================>.....] - ETA: 11s - loss: 0.2038 - categorical_accuracy: 0.9377
51968/60000 [========================>.....] - ETA: 11s - loss: 0.2036 - categorical_accuracy: 0.9378
52032/60000 [=========================>....] - ETA: 11s - loss: 0.2034 - categorical_accuracy: 0.9378
52096/60000 [=========================>....] - ETA: 10s - loss: 0.2032 - categorical_accuracy: 0.9379
52160/60000 [=========================>....] - ETA: 10s - loss: 0.2030 - categorical_accuracy: 0.9380
52224/60000 [=========================>....] - ETA: 10s - loss: 0.2029 - categorical_accuracy: 0.9380
52288/60000 [=========================>....] - ETA: 10s - loss: 0.2027 - categorical_accuracy: 0.9381
52352/60000 [=========================>....] - ETA: 10s - loss: 0.2026 - categorical_accuracy: 0.9381
52416/60000 [=========================>....] - ETA: 10s - loss: 0.2027 - categorical_accuracy: 0.9381
52480/60000 [=========================>....] - ETA: 10s - loss: 0.2025 - categorical_accuracy: 0.9382
52544/60000 [=========================>....] - ETA: 10s - loss: 0.2024 - categorical_accuracy: 0.9382
52608/60000 [=========================>....] - ETA: 10s - loss: 0.2022 - categorical_accuracy: 0.9383
52672/60000 [=========================>....] - ETA: 10s - loss: 0.2021 - categorical_accuracy: 0.9383
52736/60000 [=========================>....] - ETA: 10s - loss: 0.2019 - categorical_accuracy: 0.9383
52800/60000 [=========================>....] - ETA: 9s - loss: 0.2018 - categorical_accuracy: 0.9384 
52864/60000 [=========================>....] - ETA: 9s - loss: 0.2017 - categorical_accuracy: 0.9384
52928/60000 [=========================>....] - ETA: 9s - loss: 0.2015 - categorical_accuracy: 0.9385
52992/60000 [=========================>....] - ETA: 9s - loss: 0.2014 - categorical_accuracy: 0.9385
53056/60000 [=========================>....] - ETA: 9s - loss: 0.2013 - categorical_accuracy: 0.9385
53120/60000 [=========================>....] - ETA: 9s - loss: 0.2011 - categorical_accuracy: 0.9386
53184/60000 [=========================>....] - ETA: 9s - loss: 0.2009 - categorical_accuracy: 0.9387
53248/60000 [=========================>....] - ETA: 9s - loss: 0.2007 - categorical_accuracy: 0.9387
53312/60000 [=========================>....] - ETA: 9s - loss: 0.2005 - categorical_accuracy: 0.9388
53376/60000 [=========================>....] - ETA: 9s - loss: 0.2005 - categorical_accuracy: 0.9388
53440/60000 [=========================>....] - ETA: 9s - loss: 0.2003 - categorical_accuracy: 0.9388
53504/60000 [=========================>....] - ETA: 8s - loss: 0.2002 - categorical_accuracy: 0.9389
53568/60000 [=========================>....] - ETA: 8s - loss: 0.2000 - categorical_accuracy: 0.9389
53600/60000 [=========================>....] - ETA: 8s - loss: 0.2000 - categorical_accuracy: 0.9389
53664/60000 [=========================>....] - ETA: 8s - loss: 0.1998 - categorical_accuracy: 0.9390
53728/60000 [=========================>....] - ETA: 8s - loss: 0.1998 - categorical_accuracy: 0.9390
53792/60000 [=========================>....] - ETA: 8s - loss: 0.1998 - categorical_accuracy: 0.9390
53856/60000 [=========================>....] - ETA: 8s - loss: 0.1996 - categorical_accuracy: 0.9391
53920/60000 [=========================>....] - ETA: 8s - loss: 0.1994 - categorical_accuracy: 0.9391
53984/60000 [=========================>....] - ETA: 8s - loss: 0.1993 - categorical_accuracy: 0.9392
54048/60000 [==========================>...] - ETA: 8s - loss: 0.1991 - categorical_accuracy: 0.9393
54112/60000 [==========================>...] - ETA: 8s - loss: 0.1991 - categorical_accuracy: 0.9393
54176/60000 [==========================>...] - ETA: 8s - loss: 0.1991 - categorical_accuracy: 0.9393
54240/60000 [==========================>...] - ETA: 7s - loss: 0.1989 - categorical_accuracy: 0.9393
54304/60000 [==========================>...] - ETA: 7s - loss: 0.1987 - categorical_accuracy: 0.9394
54368/60000 [==========================>...] - ETA: 7s - loss: 0.1985 - categorical_accuracy: 0.9394
54432/60000 [==========================>...] - ETA: 7s - loss: 0.1985 - categorical_accuracy: 0.9394
54496/60000 [==========================>...] - ETA: 7s - loss: 0.1984 - categorical_accuracy: 0.9395
54560/60000 [==========================>...] - ETA: 7s - loss: 0.1982 - categorical_accuracy: 0.9395
54624/60000 [==========================>...] - ETA: 7s - loss: 0.1981 - categorical_accuracy: 0.9396
54688/60000 [==========================>...] - ETA: 7s - loss: 0.1979 - categorical_accuracy: 0.9396
54752/60000 [==========================>...] - ETA: 7s - loss: 0.1978 - categorical_accuracy: 0.9396
54816/60000 [==========================>...] - ETA: 7s - loss: 0.1976 - categorical_accuracy: 0.9397
54880/60000 [==========================>...] - ETA: 7s - loss: 0.1974 - categorical_accuracy: 0.9398
54944/60000 [==========================>...] - ETA: 7s - loss: 0.1973 - categorical_accuracy: 0.9398
55008/60000 [==========================>...] - ETA: 6s - loss: 0.1973 - categorical_accuracy: 0.9398
55072/60000 [==========================>...] - ETA: 6s - loss: 0.1971 - categorical_accuracy: 0.9398
55136/60000 [==========================>...] - ETA: 6s - loss: 0.1969 - categorical_accuracy: 0.9399
55200/60000 [==========================>...] - ETA: 6s - loss: 0.1968 - categorical_accuracy: 0.9399
55264/60000 [==========================>...] - ETA: 6s - loss: 0.1967 - categorical_accuracy: 0.9400
55328/60000 [==========================>...] - ETA: 6s - loss: 0.1965 - categorical_accuracy: 0.9400
55392/60000 [==========================>...] - ETA: 6s - loss: 0.1965 - categorical_accuracy: 0.9401
55456/60000 [==========================>...] - ETA: 6s - loss: 0.1965 - categorical_accuracy: 0.9401
55520/60000 [==========================>...] - ETA: 6s - loss: 0.1965 - categorical_accuracy: 0.9401
55584/60000 [==========================>...] - ETA: 6s - loss: 0.1964 - categorical_accuracy: 0.9401
55648/60000 [==========================>...] - ETA: 6s - loss: 0.1962 - categorical_accuracy: 0.9401
55712/60000 [==========================>...] - ETA: 5s - loss: 0.1965 - categorical_accuracy: 0.9401
55776/60000 [==========================>...] - ETA: 5s - loss: 0.1964 - categorical_accuracy: 0.9401
55840/60000 [==========================>...] - ETA: 5s - loss: 0.1962 - categorical_accuracy: 0.9402
55904/60000 [==========================>...] - ETA: 5s - loss: 0.1961 - categorical_accuracy: 0.9402
55968/60000 [==========================>...] - ETA: 5s - loss: 0.1959 - categorical_accuracy: 0.9402
56032/60000 [===========================>..] - ETA: 5s - loss: 0.1958 - categorical_accuracy: 0.9403
56096/60000 [===========================>..] - ETA: 5s - loss: 0.1959 - categorical_accuracy: 0.9403
56160/60000 [===========================>..] - ETA: 5s - loss: 0.1958 - categorical_accuracy: 0.9403
56224/60000 [===========================>..] - ETA: 5s - loss: 0.1957 - categorical_accuracy: 0.9403
56256/60000 [===========================>..] - ETA: 5s - loss: 0.1956 - categorical_accuracy: 0.9403
56320/60000 [===========================>..] - ETA: 5s - loss: 0.1954 - categorical_accuracy: 0.9404
56384/60000 [===========================>..] - ETA: 5s - loss: 0.1953 - categorical_accuracy: 0.9404
56448/60000 [===========================>..] - ETA: 4s - loss: 0.1953 - categorical_accuracy: 0.9405
56512/60000 [===========================>..] - ETA: 4s - loss: 0.1951 - categorical_accuracy: 0.9405
56576/60000 [===========================>..] - ETA: 4s - loss: 0.1950 - categorical_accuracy: 0.9406
56640/60000 [===========================>..] - ETA: 4s - loss: 0.1949 - categorical_accuracy: 0.9406
56704/60000 [===========================>..] - ETA: 4s - loss: 0.1947 - categorical_accuracy: 0.9407
56768/60000 [===========================>..] - ETA: 4s - loss: 0.1946 - categorical_accuracy: 0.9407
56832/60000 [===========================>..] - ETA: 4s - loss: 0.1944 - categorical_accuracy: 0.9408
56864/60000 [===========================>..] - ETA: 4s - loss: 0.1945 - categorical_accuracy: 0.9407
56928/60000 [===========================>..] - ETA: 4s - loss: 0.1943 - categorical_accuracy: 0.9408
56992/60000 [===========================>..] - ETA: 4s - loss: 0.1941 - categorical_accuracy: 0.9408
57056/60000 [===========================>..] - ETA: 4s - loss: 0.1940 - categorical_accuracy: 0.9409
57120/60000 [===========================>..] - ETA: 3s - loss: 0.1938 - categorical_accuracy: 0.9409
57184/60000 [===========================>..] - ETA: 3s - loss: 0.1938 - categorical_accuracy: 0.9409
57248/60000 [===========================>..] - ETA: 3s - loss: 0.1938 - categorical_accuracy: 0.9409
57312/60000 [===========================>..] - ETA: 3s - loss: 0.1937 - categorical_accuracy: 0.9410
57376/60000 [===========================>..] - ETA: 3s - loss: 0.1935 - categorical_accuracy: 0.9411
57408/60000 [===========================>..] - ETA: 3s - loss: 0.1934 - categorical_accuracy: 0.9411
57472/60000 [===========================>..] - ETA: 3s - loss: 0.1933 - categorical_accuracy: 0.9411
57536/60000 [===========================>..] - ETA: 3s - loss: 0.1932 - categorical_accuracy: 0.9411
57600/60000 [===========================>..] - ETA: 3s - loss: 0.1931 - categorical_accuracy: 0.9412
57664/60000 [===========================>..] - ETA: 3s - loss: 0.1929 - categorical_accuracy: 0.9412
57728/60000 [===========================>..] - ETA: 3s - loss: 0.1928 - categorical_accuracy: 0.9412
57792/60000 [===========================>..] - ETA: 3s - loss: 0.1927 - categorical_accuracy: 0.9413
57856/60000 [===========================>..] - ETA: 2s - loss: 0.1926 - categorical_accuracy: 0.9413
57920/60000 [===========================>..] - ETA: 2s - loss: 0.1925 - categorical_accuracy: 0.9414
57984/60000 [===========================>..] - ETA: 2s - loss: 0.1925 - categorical_accuracy: 0.9414
58048/60000 [============================>.] - ETA: 2s - loss: 0.1923 - categorical_accuracy: 0.9414
58112/60000 [============================>.] - ETA: 2s - loss: 0.1923 - categorical_accuracy: 0.9415
58176/60000 [============================>.] - ETA: 2s - loss: 0.1922 - categorical_accuracy: 0.9415
58240/60000 [============================>.] - ETA: 2s - loss: 0.1921 - categorical_accuracy: 0.9415
58304/60000 [============================>.] - ETA: 2s - loss: 0.1919 - categorical_accuracy: 0.9416
58368/60000 [============================>.] - ETA: 2s - loss: 0.1918 - categorical_accuracy: 0.9416
58432/60000 [============================>.] - ETA: 2s - loss: 0.1916 - categorical_accuracy: 0.9417
58496/60000 [============================>.] - ETA: 2s - loss: 0.1915 - categorical_accuracy: 0.9417
58560/60000 [============================>.] - ETA: 1s - loss: 0.1914 - categorical_accuracy: 0.9417
58624/60000 [============================>.] - ETA: 1s - loss: 0.1913 - categorical_accuracy: 0.9417
58688/60000 [============================>.] - ETA: 1s - loss: 0.1912 - categorical_accuracy: 0.9418
58752/60000 [============================>.] - ETA: 1s - loss: 0.1911 - categorical_accuracy: 0.9418
58816/60000 [============================>.] - ETA: 1s - loss: 0.1910 - categorical_accuracy: 0.9418
58880/60000 [============================>.] - ETA: 1s - loss: 0.1909 - categorical_accuracy: 0.9419
58944/60000 [============================>.] - ETA: 1s - loss: 0.1909 - categorical_accuracy: 0.9419
59008/60000 [============================>.] - ETA: 1s - loss: 0.1908 - categorical_accuracy: 0.9419
59072/60000 [============================>.] - ETA: 1s - loss: 0.1908 - categorical_accuracy: 0.9420
59136/60000 [============================>.] - ETA: 1s - loss: 0.1907 - categorical_accuracy: 0.9420
59200/60000 [============================>.] - ETA: 1s - loss: 0.1907 - categorical_accuracy: 0.9420
59264/60000 [============================>.] - ETA: 1s - loss: 0.1905 - categorical_accuracy: 0.9420
59328/60000 [============================>.] - ETA: 0s - loss: 0.1904 - categorical_accuracy: 0.9421
59392/60000 [============================>.] - ETA: 0s - loss: 0.1903 - categorical_accuracy: 0.9421
59456/60000 [============================>.] - ETA: 0s - loss: 0.1903 - categorical_accuracy: 0.9421
59520/60000 [============================>.] - ETA: 0s - loss: 0.1903 - categorical_accuracy: 0.9422
59552/60000 [============================>.] - ETA: 0s - loss: 0.1902 - categorical_accuracy: 0.9422
59584/60000 [============================>.] - ETA: 0s - loss: 0.1901 - categorical_accuracy: 0.9422
59648/60000 [============================>.] - ETA: 0s - loss: 0.1901 - categorical_accuracy: 0.9422
59712/60000 [============================>.] - ETA: 0s - loss: 0.1900 - categorical_accuracy: 0.9423
59776/60000 [============================>.] - ETA: 0s - loss: 0.1899 - categorical_accuracy: 0.9423
59840/60000 [============================>.] - ETA: 0s - loss: 0.1897 - categorical_accuracy: 0.9423
59904/60000 [============================>.] - ETA: 0s - loss: 0.1897 - categorical_accuracy: 0.9424
59968/60000 [============================>.] - ETA: 0s - loss: 0.1896 - categorical_accuracy: 0.9424
60000/60000 [==============================] - 86s 1ms/step - loss: 0.1895 - categorical_accuracy: 0.9424 - val_loss: 0.0538 - val_categorical_accuracy: 0.9821

  ('#### Predict   ####################################################',) 

  ('#### Path params   ################################################',) 

  ('/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/', '/home/runner/work/mlmodels/mlmodels/keras_deepAR/') 

   32/10000 [..............................] - ETA: 14s
  288/10000 [..............................] - ETA: 3s 
  512/10000 [>.............................] - ETA: 2s
  736/10000 [=>............................] - ETA: 2s
  960/10000 [=>............................] - ETA: 2s
 1184/10000 [==>...........................] - ETA: 2s
 1408/10000 [===>..........................] - ETA: 2s
 1632/10000 [===>..........................] - ETA: 2s
 1888/10000 [====>.........................] - ETA: 2s
 2144/10000 [=====>........................] - ETA: 1s
 2400/10000 [======>.......................] - ETA: 1s
 2624/10000 [======>.......................] - ETA: 1s
 2880/10000 [=======>......................] - ETA: 1s
 3104/10000 [========>.....................] - ETA: 1s
 3328/10000 [========>.....................] - ETA: 1s
 3520/10000 [=========>....................] - ETA: 1s
 3680/10000 [==========>...................] - ETA: 1s
 3904/10000 [==========>...................] - ETA: 1s
 4128/10000 [===========>..................] - ETA: 1s
 4352/10000 [============>.................] - ETA: 1s
 4576/10000 [============>.................] - ETA: 1s
 4800/10000 [=============>................] - ETA: 1s
 5056/10000 [==============>...............] - ETA: 1s
 5280/10000 [==============>...............] - ETA: 1s
 5504/10000 [===============>..............] - ETA: 1s
 5728/10000 [================>.............] - ETA: 1s
 5952/10000 [================>.............] - ETA: 0s
 6208/10000 [=================>............] - ETA: 0s
 6464/10000 [==================>...........] - ETA: 0s
 6656/10000 [==================>...........] - ETA: 0s
 6880/10000 [===================>..........] - ETA: 0s
 7104/10000 [====================>.........] - ETA: 0s
 7328/10000 [====================>.........] - ETA: 0s
 7552/10000 [=====================>........] - ETA: 0s
 7776/10000 [======================>.......] - ETA: 0s
 8000/10000 [=======================>......] - ETA: 0s
 8224/10000 [=======================>......] - ETA: 0s
 8448/10000 [========================>.....] - ETA: 0s
 8672/10000 [=========================>....] - ETA: 0s
 8896/10000 [=========================>....] - ETA: 0s
 9152/10000 [==========================>...] - ETA: 0s
 9376/10000 [===========================>..] - ETA: 0s
 9600/10000 [===========================>..] - ETA: 0s
 9824/10000 [============================>.] - ETA: 0s
10000/10000 [==============================] - 2s 244us/step
[[2.9288717e-08 2.0921354e-09 5.3389812e-07 ... 9.9999821e-01
  5.4291638e-09 1.1942709e-06]
 [7.4091135e-05 3.1997802e-04 9.9951005e-01 ... 5.9814319e-08
  1.6867582e-05 6.8644943e-09]
 [2.2295843e-07 9.9987018e-01 1.1212690e-05 ... 1.4734743e-05
  6.3076682e-06 2.6935504e-07]
 ...
 [5.2773599e-09 5.1034178e-08 2.3795408e-09 ... 2.6318064e-06
  4.9136531e-07 2.0233785e-05]
 [4.3661557e-06 8.3502488e-07 5.2650975e-08 ... 3.0082145e-07
  1.6730054e-03 8.8718895e-07]
 [1.4746084e-06 2.5210488e-08 1.4016597e-06 ... 1.0877814e-09
  2.2714478e-06 3.3655840e-09]]

  ('#### metrics   ####################################################',) 

  ('#### Path params   ################################################',) 

  ('/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/', '/home/runner/work/mlmodels/mlmodels/keras_deepAR/') 
{'loss_test:': 0.05383375459704548, 'accuracy_test:': 0.9821000099182129}

  ('#### Save   #######################################################',) 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/charcnn/result'}

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
Warning: Permanently added the RSA host key for IP address '140.82.113.3' to the list of known hosts.
From github.com:arita37/mlmodels_store
   33c0e91..9a6e048  master     -> origin/master
Updating 33c0e91..9a6e048
Fast-forward
 .../20200515/list_log_dataloader_20200515.md       |   2 +-
 error_list/20200515/list_log_testall_20200515.md   | 432 +++++++++++++++++++++
 2 files changed, 433 insertions(+), 1 deletion(-)
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master 61a8768] ml_store
 1 file changed, 1114 insertions(+)
To github.com:arita37/mlmodels_store.git
   9a6e048..61a8768  master -> master





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
{'loss': 0.500361256301403, 'loss_history': []}

  #### Plot   ######################################################## 

  #### Save   ######################################################## 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/'}
Model saved in path: /home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm//model//model.ckpt

  #### Load   ######################################################## 
2020-05-15 04:32:05.033727: W tensorflow/core/framework/op_kernel.cc:1651] OP_REQUIRES failed at save_restore_v2_ops.cc:184 : Not found: Key Variable not found in checkpoint
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


   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
Already up to date.
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master da57131] ml_store
 1 file changed, 233 insertions(+)
To github.com:arita37/mlmodels_store.git
   61a8768..da57131  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//temporal_fusion_google.py 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//temporal_fusion_google.py", line 17, in <module>
    from mlmodels.mode_tf.raw  import temporal_fusion_google
ModuleNotFoundError: No module named 'mlmodels.mode_tf'

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
Already up to date.
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master 6d74fbd] ml_store
 1 file changed, 35 insertions(+)
To github.com:arita37/mlmodels_store.git
   da57131..6d74fbd  master -> master





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
	Data preprocessing and feature engineering runtime = 0.22s ...
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
 40%|████      | 2/5 [00:19<00:29,  9.70s/it]Saving dataset/models/LightGBMClassifier/trial_1_model.pkl
Finished Task with config: {'feature_fraction': 0.9978912413306537, 'learning_rate': 0.01089357771697609, 'min_data_in_leaf': 10, 'num_leaves': 34} and reward: 0.387
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xef\xee\xb9\x9c\xcf\\+X\r\x00\x00\x00learning_rateq\x02G?\x86O_@?,\x87X\x10\x00\x00\x00min_data_in_leafq\x03K\nX\n\x00\x00\x00num_leavesq\x04K"u.' and reward: 0.387
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xef\xee\xb9\x9c\xcf\\+X\r\x00\x00\x00learning_rateq\x02G?\x86O_@?,\x87X\x10\x00\x00\x00min_data_in_leafq\x03K\nX\n\x00\x00\x00num_leavesq\x04K"u.' and reward: 0.387
 60%|██████    | 3/5 [00:38<00:25, 12.56s/it]Saving dataset/models/LightGBMClassifier/trial_2_model.pkl
Finished Task with config: {'feature_fraction': 0.8779425158894283, 'learning_rate': 0.013895998243555818, 'min_data_in_leaf': 5, 'num_leaves': 62} and reward: 0.3908
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xec\x18\x1a\xe70j\xf2X\r\x00\x00\x00learning_rateq\x02G?\x8cu\x81P\x02\xc1\x86X\x10\x00\x00\x00min_data_in_leafq\x03K\x05X\n\x00\x00\x00num_leavesq\x04K>u.' and reward: 0.3908
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xec\x18\x1a\xe70j\xf2X\r\x00\x00\x00learning_rateq\x02G?\x8cu\x81P\x02\xc1\x86X\x10\x00\x00\x00min_data_in_leafq\x03K\x05X\n\x00\x00\x00num_leavesq\x04K>u.' and reward: 0.3908
 80%|████████  | 4/5 [01:06<00:17, 17.17s/it] 80%|████████  | 4/5 [01:06<00:16, 16.64s/it]
Saving dataset/models/LightGBMClassifier/trial_3_model.pkl
Finished Task with config: {'feature_fraction': 0.9231962832828323, 'learning_rate': 0.035567905590453974, 'min_data_in_leaf': 25, 'num_leaves': 31} and reward: 0.3954
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xed\x8a\xd2\xee\x8f\xa1\xedX\r\x00\x00\x00learning_rateq\x02G?\xa25\xf4\xde\x98\xaf\xb0X\x10\x00\x00\x00min_data_in_leafq\x03K\x19X\n\x00\x00\x00num_leavesq\x04K\x1fu.' and reward: 0.3954
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xed\x8a\xd2\xee\x8f\xa1\xedX\r\x00\x00\x00learning_rateq\x02G?\xa25\xf4\xde\x98\xaf\xb0X\x10\x00\x00\x00min_data_in_leafq\x03K\x19X\n\x00\x00\x00num_leavesq\x04K\x1fu.' and reward: 0.3954
Time for Gradient Boosting hyperparameter optimization: 84.94493651390076
Best hyperparameter configuration for Gradient Boosting Model: 
{'feature_fraction': 0.9231962832828323, 'learning_rate': 0.035567905590453974, 'min_data_in_leaf': 25, 'num_leaves': 31}
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
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 10% CPU time recently (threshold: 10%)
Saving dataset/models/NeuralNetClassifier/trial_4_tabularNN.pkl
Finished Task with config: {'activation.choice': 0, 'dropout_prob': 0.1, 'embedding_size_factor': 1.0, 'layers.choice': 0, 'learning_rate': 0.0005, 'network_type.choice': 0, 'use_batchnorm.choice': 0, 'weight_decay': 1e-06} and reward: 0.3894
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\xb9\x99\x99\x99\x99\x99\x9aX\x15\x00\x00\x00embedding_size_factorq\x03G?\xf0\x00\x00\x00\x00\x00\x00X\r\x00\x00\x00layers.choiceq\x04K\x00X\r\x00\x00\x00learning_rateq\x05G?@bM\xd2\xf1\xa9\xfcX\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G>\xb0\xc6\xf7\xa0\xb5\xed\x8du.' and reward: 0.3894
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\xb9\x99\x99\x99\x99\x99\x9aX\x15\x00\x00\x00embedding_size_factorq\x03G?\xf0\x00\x00\x00\x00\x00\x00X\r\x00\x00\x00layers.choiceq\x04K\x00X\r\x00\x00\x00learning_rateq\x05G?@bM\xd2\xf1\xa9\xfcX\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G>\xb0\xc6\xf7\xa0\xb5\xed\x8du.' and reward: 0.3894
 40%|████      | 2/5 [00:50<01:15, 25.14s/it]Loading: dataset/models/NeuralNetClassifier/train_tabNNdataset.pkl
Loading: dataset/models/NeuralNetClassifier/validation_tabNNdataset.pkl
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
distributed.utils_perf - WARNING - full garbage collections took 11% CPU time recently (threshold: 10%)
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
Finished Task with config: {'activation.choice': 0, 'dropout_prob': 0.2287016945077311, 'embedding_size_factor': 0.8210700829922506, 'layers.choice': 1, 'learning_rate': 0.00011387115286184473, 'network_type.choice': 0, 'use_batchnorm.choice': 0, 'weight_decay': 0.06720387994103812} and reward: 0.3724
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\xcdF\x18\xdd9\xa9\x96X\x15\x00\x00\x00embedding_size_factorq\x03G?\xeaF4\xc4E\x9f\x84X\r\x00\x00\x00layers.choiceq\x04K\x01X\r\x00\x00\x00learning_rateq\x05G?\x1d\xd9\xc3\x82\x8f6\x93X\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G?\xb14F\x02\x82\xd5mu.' and reward: 0.3724
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\xcdF\x18\xdd9\xa9\x96X\x15\x00\x00\x00embedding_size_factorq\x03G?\xeaF4\xc4E\x9f\x84X\r\x00\x00\x00layers.choiceq\x04K\x01X\r\x00\x00\x00learning_rateq\x05G?\x1d\xd9\xc3\x82\x8f6\x93X\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G?\xb14F\x02\x82\xd5mu.' and reward: 0.3724
 60%|██████    | 3/5 [02:09<01:23, 41.51s/it] 60%|██████    | 3/5 [02:09<01:26, 43.33s/it]
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
Saving dataset/models/NeuralNetClassifier/trial_6_tabularNN.pkl
Finished Task with config: {'activation.choice': 0, 'dropout_prob': 0.3342089289905667, 'embedding_size_factor': 0.6471232425514845, 'layers.choice': 3, 'learning_rate': 0.0061634952220981365, 'network_type.choice': 1, 'use_batchnorm.choice': 1, 'weight_decay': 0.05398447149015069} and reward: 0.1408
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\xd5c\xad\xd9\x02\xecCX\x15\x00\x00\x00embedding_size_factorq\x03G?\xe4\xb5;\xcdg\xae\xe9X\r\x00\x00\x00layers.choiceq\x04K\x03X\r\x00\x00\x00learning_rateq\x05G?y>\xe4\xa6\x87\x05\x00X\x13\x00\x00\x00network_type.choiceq\x06K\x01X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x01X\x0c\x00\x00\x00weight_decayq\x08G?\xab\xa3\xdaG\x15\x86zu.' and reward: 0.1408
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\xd5c\xad\xd9\x02\xecCX\x15\x00\x00\x00embedding_size_factorq\x03G?\xe4\xb5;\xcdg\xae\xe9X\r\x00\x00\x00layers.choiceq\x04K\x03X\r\x00\x00\x00learning_rateq\x05G?y>\xe4\xa6\x87\x05\x00X\x13\x00\x00\x00network_type.choiceq\x06K\x01X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x01X\x0c\x00\x00\x00weight_decayq\x08G?\xab\xa3\xdaG\x15\x86zu.' and reward: 0.1408
Please either provide filename or allow plot in get_training_curves
Time for Neural Network hyperparameter optimization: 182.3013186454773
Best hyperparameter configuration for Tabular Neural Network: 
{'activation.choice': 0, 'dropout_prob': 0.1, 'embedding_size_factor': 1.0, 'layers.choice': 0, 'learning_rate': 0.0005, 'network_type.choice': 0, 'use_batchnorm.choice': 0, 'weight_decay': 1e-06}
Saving dataset/models/trainer.pkl
Loading: dataset/models/LightGBMClassifier/trial_0_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_1_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_2_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_3_model.pkl
Loading: dataset/models/NeuralNetClassifier/trial_4_tabularNN.pkl
Loading: dataset/models/NeuralNetClassifier/trial_5_tabularNN.pkl
Loading: dataset/models/NeuralNetClassifier/trial_6_tabularNN.pkl
Fitting model: weighted_ensemble_k0_l1 ... Training model for up to 119.78s of the -151.73s of remaining time.
Ensemble size: 43
Ensemble weights: 
[0.93023256 0.         0.         0.         0.04651163 0.
 0.02325581]
	0.3956	 = Validation accuracy score
	1.54s	 = Training runtime
	0.0s	 = Validation runtime
Saving dataset/models/weighted_ensemble_k0_l1/model.pkl
Saving dataset/models/trainer.pkl
Saving dataset/models/trainer.pkl
Saving dataset/models/trainer.pkl
AutoGluon training complete, total runtime = 273.32s ...
Loading: dataset/models/trainer.pkl

  #### save the trained model  ####################################### 

  #### Predict   #################################################### 
Loaded data from: https://autogluon.s3.amazonaws.com/datasets/Inc/test.csv | Columns = 15 / 15 | Rows = 9769 -> 9769
Loading: dataset/models/trainer.pkl
Loading: dataset/models/weighted_ensemble_k0_l1/model.pkl
Loading: dataset/models/LightGBMClassifier/trial_3_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_1_model.pkl
Loading: dataset/models/NeuralNetClassifier/trial_6_tabularNN.pkl

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
Saving dataset/learner.pkl
TabularPredictor saved. To load, use: TabularPredictor.load(dataset/)
<mlmodels.model_gluon.util_autogluon.Model_empty object at 0x7f0e4c51b358>

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
From github.com:arita37/mlmodels_store
   6d74fbd..33b5250  master     -> origin/master
Updating 6d74fbd..33b5250
Fast-forward
 .../20200515/list_log_dataloader_20200515.md       |    2 +-
 error_list/20200515/list_log_testall_20200515.md   |  174 ++
 ...-12_207025cb0ea4a9ff2c75f9c6635cdcf2e51f17b2.py | 2467 ++++++++++++++++++++
 3 files changed, 2642 insertions(+), 1 deletion(-)
 create mode 100644 log_benchmark/log_benchmark_2020-05-15-04-12_207025cb0ea4a9ff2c75f9c6635cdcf2e51f17b2.py
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master 00c95fb] ml_store
 1 file changed, 309 insertions(+)
To github.com:arita37/mlmodels_store.git
   33b5250..00c95fb  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon//fb_prophet.py 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon//fb_prophet.py", line 160, in <module>
    test(data_path = "model_fb/fbprophet.json", choice="json" )
TypeError: test() got an unexpected keyword argument 'choice'

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
Already up to date.
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master 1f3856e] ml_store
 1 file changed, 35 insertions(+)
To github.com:arita37/mlmodels_store.git
   00c95fb..1f3856e  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon//gluonts_model.py 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon//gluonts_model.py", line 15, in <module>
    from gluonts.model.deepar import DeepAREstimator
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/__init__.py", line 15, in <module>
    from ._estimator import DeepAREstimator
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/model/deepar/_estimator.py", line 24, in <module>
    from gluonts.distribution import DistributionOutput, StudentTOutput
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/__init__.py", line 15, in <module>
    from . import bijection
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 28, in <module>
    class Bijection:
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/distribution/bijection.py", line 36, in Bijection
    @validated()
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/gluonts/core/component.py", line 398, in validator
    **init_fields,
  File "pydantic/main.py", line 778, in pydantic.main.create_model
TypeError: create_model() takes exactly 1 positional argument (0 given)

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
Warning: Permanently added the RSA host key for IP address '140.82.114.4' to the list of known hosts.
Already up to date.
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master d7a7095] ml_store
 1 file changed, 49 insertions(+)
To github.com:arita37/mlmodels_store.git
   1f3856e..d7a7095  master -> master





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
{'roc_auc_score': 1.0}

  #### Module init   ############################################ 

  <module 'mlmodels.model_sklearn.model_sklearn' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_sklearn/model_sklearn.py'> 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Model init   ############################################ 

  <mlmodels.model_sklearn.model_sklearn.Model object at 0x7f8700109f98> 

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

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
Already up to date.
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master cf1535f] ml_store
 1 file changed, 108 insertions(+)
To github.com:arita37/mlmodels_store.git
   d7a7095..cf1535f  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_sklearn//model_lightgbm.py 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 

  #### save the trained model  ####################################### 

  #### Predict   ##################################################### 
[[ 6.23629500e-01  9.86352180e-01  1.45391758e+00 -4.66154857e-01
   9.36403332e-01  1.38499134e+00  3.49435894e-02 -1.07296428e+00
   4.95158611e-01  6.61681076e-01]
 [ 1.21619061e+00 -1.90005215e-02  8.60891241e-01 -2.26760192e-01
  -1.36419132e+00 -1.56450785e+00  1.63169151e+00  9.31255679e-01
   9.49808815e-01 -8.80189065e-01]
 [ 9.71395338e-01  7.13049050e-01  1.76041518e+00  1.30620607e+00
   1.05765490e+00 -6.04602969e-01  1.28376990e-01  6.36583409e-01
   1.40925339e+00  9.66539250e-01]
 [ 7.83440538e-01 -5.11884476e-02  8.24584625e-01 -7.25597119e-01
   9.31717197e-01 -8.67768678e-01  3.03085711e+00 -1.35977326e-01
  -7.97269785e-01  6.54580153e-01]
 [ 9.36211246e-01  2.04377395e-01 -1.49419377e+00  6.12232523e-01
  -9.84377246e-01  7.44884536e-01  4.94341651e-01 -3.62812886e-02
  -8.32395348e-01 -4.46699203e-01]
 [ 1.66752297e+00  1.22372221e+00 -4.59930104e-01 -5.93679025e-02
  -4.93856997e-01  1.44898940e+00 -1.18110317e+00 -4.77580855e-01
   2.59999942e-02 -7.90799954e-01]
 [ 1.83829400e+00  5.02740882e-01  1.29101580e-01  1.55880554e+00
   1.32551412e+00  1.09402696e-01  1.40754000e+00 -1.21974440e+00
   2.44936865e+00  1.61694960e+00]
 [ 8.78643802e-01  1.03703898e+00 -4.77124206e-01  6.72619748e-01
  -1.04948638e+00  2.42887697e+00  5.24750492e-01  1.00568668e+00
   3.53567216e-01 -3.59901817e-02]
 [ 7.73703613e-01  1.27852808e+00 -2.11416392e+00 -4.42229280e-01
   1.06821044e+00  3.23527354e-01 -2.50644065e+00 -1.09991490e-01
   8.54894544e-03 -4.11639163e-01]
 [ 6.25673373e-01  5.92472801e-01  6.74570707e-01  1.19783084e+00
   1.23187251e+00  1.70459417e+00 -7.67309826e-01  1.04008915e+00
  -9.18440038e-01  1.46089238e+00]
 [ 1.39198128e+00 -1.90221025e-01 -5.37223024e-01 -4.48738033e-01
   7.04557071e-01 -6.72448039e-01 -7.01344426e-01 -5.57494722e-01
   9.39168744e-01  1.56263850e-01]
 [ 1.01195228e+00 -1.88141087e+00  1.70018815e+00  4.97269099e-01
  -9.17664624e-01  2.37332699e-01 -1.09033833e+00 -2.14444405e+00
  -3.69562425e-01  6.08783659e-01]
 [ 1.13545112e+00  8.61623101e-01  4.90616924e-02 -2.08639057e+00
  -1.11469020e+00  3.61801641e-01 -8.06178212e-01  4.25920177e-01
   4.90803971e-02 -5.96086335e-01]
 [ 8.53355545e-01 -7.04350332e-01 -6.79383783e-01 -4.58666861e-02
  -1.29936179e+00 -2.18733459e-01  5.90039464e-01  1.53920701e+00
  -1.14870423e+00 -9.50909251e-01]
 [ 1.18947778e+00 -6.80678141e-01 -5.68244809e-02 -8.45080274e-02
   8.21783210e-01 -2.97361883e-01 -1.86578994e-01  4.17302005e-01
   7.84770651e-01  4.92336556e-01]
 [ 1.06523311e+00 -6.64867767e-01  1.00806543e+00 -1.94504696e+00
  -1.23017555e+00 -9.15424368e-01  3.37220938e-01  1.22515585e+00
  -1.05354607e+00  7.85226920e-01]
 [ 1.06040861e+00  5.10307597e-01  5.01725109e-01 -9.15791849e-01
  -9.07318361e-01 -4.07252043e-01 -1.79612295e-01  9.84951672e-01
   1.07125243e+00 -5.93343754e-01]
 [ 8.72267394e-01 -2.51630386e+00 -7.75070287e-01 -5.95667881e-01
   1.02600767e+00 -3.09121319e-01  1.74643509e+00  5.10937774e-01
   1.71066184e+00  1.41640538e-01]
 [ 1.98519313e+00  6.74711526e-01 -1.39662042e+00  6.18539131e-01
   1.22382712e+00 -4.43171931e-01 -1.89148284e-03  1.81053491e+00
  -1.30572692e+00 -8.61316361e-01]
 [ 8.57719529e-01  9.81122462e-02 -2.60466059e-01  1.06032751e+00
  -1.39003042e+00 -1.71116766e+00  2.65642403e-01  1.65712464e+00
   1.41767401e+00  4.45096710e-01]
 [ 1.09488485e+00 -6.96245395e-02 -1.16444148e-01  3.53870427e-01
  -1.44189096e+00 -1.86955017e-01  1.29118890e+00 -1.53236162e-01
  -2.43250851e+00 -2.27729800e+00]
 [ 9.67037267e-01  3.82715174e-01 -8.06184817e-01 -2.88997343e-01
   9.08526041e-01 -3.91816240e-01  1.62091229e+00  6.84001328e-01
  -3.53409983e-01 -2.51674208e-01]
 [ 3.45715997e-01 -4.13029310e-01 -4.68673816e-01  1.83471763e+00
   7.71514409e-01  5.64382855e-01  2.18628366e-02  2.13782807e+00
  -7.85533997e-01  8.53281222e-01]
 [ 1.34728643e+00 -3.64538050e-01  8.07509886e-02 -4.59717681e-01
  -8.89487596e-01  1.70548352e+00  9.49961101e-02  2.40505552e-01
  -9.99426501e-01 -7.67803746e-01]
 [ 4.67397905e-01 -2.37875265e-01 -1.54491194e-01 -7.55662765e-01
  -5.47062239e-01  1.85143789e+00 -1.46405357e+00  2.09096677e-01
   1.55501599e+00 -9.24323185e-02]]

  #### metrics   ##################################################### 
{}

  #### Plot   ######################################################## 

  #### Save/Load   ################################################### 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_sklearn/model_lightgbm/model.pkl'}
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_sklearn/model_lightgbm/model.pkl'}
<__main__.Model object at 0x7f66aa63af60>

  #### Module init   ############################################ 

  <module 'mlmodels.model_sklearn.model_lightgbm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_sklearn/model_lightgbm.py'> 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Model init   ############################################ 

  <mlmodels.model_sklearn.model_lightgbm.Model object at 0x7f66c49a9748> 

  #### Fit   ######################################################## 

  #### Predict   #################################################### 
[[ 1.24549398 -0.72239191  1.1181334   1.09899633  1.00277655 -0.90163449
  -0.53223402 -0.82246719  0.72171129  0.6743961 ]
 [ 0.44118981  0.47985237 -0.1920037  -1.55269878 -1.88873982  0.57846442
   0.39859839 -0.9612636  -1.45832446 -3.05376438]
 [ 1.06523311 -0.66486777  1.00806543 -1.94504696 -1.23017555 -0.91542437
   0.33722094  1.22515585 -1.05354607  0.78522692]
 [ 0.93621125  0.20437739 -1.49419377  0.61223252 -0.98437725  0.74488454
   0.49434165 -0.03628129 -0.83239535 -0.4466992 ]
 [ 1.34728643 -0.36453805  0.08075099 -0.45971768 -0.8894876   1.70548352
   0.09499611  0.24050555 -0.9994265  -0.76780375]
 [ 1.12062155 -0.7029204  -1.22957425  0.72555052 -1.18013412 -0.32420422
   1.10223673  0.81434313  0.78046993  1.10861676]
 [ 1.37661405 -0.60022533  0.72591685 -0.37951752 -0.62754626 -1.01480369
   0.96622086  0.4359862  -0.68748739  3.32107876]
 [ 1.09488485 -0.06962454 -0.11644415  0.35387043 -1.44189096 -0.18695502
   1.2911889  -0.15323616 -2.43250851 -2.277298  ]
 [ 1.01195228 -1.88141087  1.70018815  0.4972691  -0.91766462  0.2373327
  -1.09033833 -2.14444405 -0.36956243  0.60878366]
 [ 1.02242019  1.85300949  0.64435367  0.14225137  1.15080755  0.51350548
  -0.45994283  0.37245685 -0.1484898   0.37167029]
 [ 0.97139534  0.71304905  1.76041518  1.30620607  1.0576549  -0.60460297
   0.12837699  0.63658341  1.40925339  0.96653925]
 [ 1.16755486  0.0353601   0.7147896  -1.53879325  1.10863359 -0.44789518
  -1.75592564  0.61798553 -0.18417633  0.85270406]
 [ 1.36586461  3.9586027   0.54812958  0.64864364  0.84917607  0.10734329
   1.38631426 -1.39881282  0.08176782 -1.63744959]
 [ 1.58463774  0.057121   -0.01771832 -0.79954749  1.32970299 -0.2915946
  -1.1077125  -0.25898285  0.1892932  -1.71939447]
 [ 0.81583612 -1.39169388  2.50598029  0.45021774 -0.88286982  0.62743708
  -1.19586151  0.75133724  0.14039544  1.91979229]
 [ 1.12641981 -0.6294416   1.1010002  -1.1134361   0.94459507 -0.06741002
  -0.1834002   1.16143998 -0.02752939  0.78002714]
 [ 0.345716   -0.41302931 -0.46867382  1.83471763  0.77151441  0.56438286
   0.02186284  2.13782807 -0.785534    0.85328122]
 [ 0.92686981  0.39233491 -0.4234783   0.44838065 -1.09230828  1.1253235
  -0.94843966  0.10405339  0.52800342  1.00796648]
 [ 0.46739791 -0.23787527 -0.15449119 -0.75566277 -0.54706224  1.85143789
  -1.46405357  0.20909668  1.55501599 -0.09243232]
 [ 0.85335555 -0.70435033 -0.67938378 -0.04586669 -1.29936179 -0.21873346
   0.59003946  1.53920701 -1.14870423 -0.95090925]
 [ 0.85729649  0.9561217  -0.82609743 -0.70584051  1.13872896  1.19268607
   0.28267571 -0.23794194  1.15528789  0.6210827 ]
 [ 0.77528533  1.47016034  1.03298378 -0.87000822  0.78655651  0.36919047
  -0.14319575  0.85328219 -0.13971173 -0.22241403]
 [ 1.64661853 -1.52568032 -0.6069984   0.79502609  1.08480038 -0.37443832
   0.42952614  0.1340482   1.20205486  0.10622272]
 [ 0.87226739 -2.51630386 -0.77507029 -0.59566788  1.02600767 -0.30912132
   1.74643509  0.51093777  1.71066184  0.14164054]
 [ 0.94781411 -1.13379204  0.64098587 -0.1905483  -1.23912256  0.23333913
  -0.3169012   0.43499832  0.9104236   1.21987438]]
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
[[ 0.44689516  0.38653915  1.35010682 -0.85145566  0.85063796  1.00088142
  -1.1601701  -0.38483225  1.45810824 -0.33128317]
 [ 1.34728643 -0.36453805  0.08075099 -0.45971768 -0.8894876   1.70548352
   0.09499611  0.24050555 -0.9994265  -0.76780375]
 [ 1.46893146 -1.47115693  0.58591043 -0.8301719   1.03345052 -0.8805776
  -0.95542526 -0.27909772  1.62284909  2.06578332]
 [ 0.56998385 -0.53302033 -0.17545897 -1.42655542  0.60660431  1.76795995
  -0.11598519 -0.47537288  0.47761018 -0.93391466]
 [ 0.5630779  -1.17598267 -0.17418034  1.01012718  1.06796368  0.92001793
  -0.16819884 -0.19505734  0.80539342  0.4611641 ]
 [ 0.96457205 -0.10679399  1.12232832  1.45142926  1.21828168 -0.61803685
   0.43816635 -2.03720123 -1.94258918 -0.9970198 ]
 [ 0.6675918  -0.45252497 -0.60598132  1.16128569 -1.44620987  1.06996554
   1.92381543 -1.04553425  0.35528451  1.80358898]
 [ 0.87874071 -0.01923163  0.31965694  0.15001628 -1.46662161  0.46353432
  -0.89868319  0.39788042 -0.99601089  0.3181542 ]
 [ 1.77547698 -0.20339445 -0.19883786  0.24266944  0.96435056  0.20183018
  -0.54577417  0.66102029  1.79215821 -0.7003985 ]
 [ 0.87699465  1.23225307 -0.86778722 -0.25417987  0.89189141  1.39984394
  -0.87728152 -0.78191168 -0.43750898 -1.44087602]
 [ 0.345716   -0.41302931 -0.46867382  1.83471763  0.77151441  0.56438286
   0.02186284  2.13782807 -0.785534    0.85328122]
 [ 1.01195228 -1.88141087  1.70018815  0.4972691  -0.91766462  0.2373327
  -1.09033833 -2.14444405 -0.36956243  0.60878366]
 [ 1.18947778 -0.68067814 -0.05682448 -0.08450803  0.82178321 -0.29736188
  -0.18657899  0.417302    0.78477065  0.49233656]
 [ 0.89551051  0.92061512  0.79452824 -0.03536792  0.8780991   2.11060505
  -1.02188594 -1.30653407  0.07638048 -1.87316098]
 [ 0.89562312 -2.29820588 -0.01952256  1.45652739 -1.85064099  0.31663724
   0.11133727 -2.66412594 -0.42642862 -0.83998891]
 [ 2.07582971 -1.40232915 -0.47918492  0.45112294  1.03436581 -0.6949209
  -0.4189379   0.5154138  -1.11487105 -1.95210529]
 [ 0.94781411 -1.13379204  0.64098587 -0.1905483  -1.23912256  0.23333913
  -0.3169012   0.43499832  0.9104236   1.21987438]
 [ 0.87122579 -0.20975294 -0.45698786  0.93514778 -0.87353582  1.81252782
   0.92550121  0.14010988 -1.41914878  1.06898597]
 [ 1.37661405 -0.60022533  0.72591685 -0.37951752 -0.62754626 -1.01480369
   0.96622086  0.4359862  -0.68748739  3.32107876]
 [ 0.84806927  0.45194604  0.63019567 -1.57915629  0.82798737 -0.82862798
  -0.10534471  0.52887975 -2.23708651 -0.4148469 ]
 [ 0.85729649  0.9561217  -0.82609743 -0.70584051  1.13872896  1.19268607
   0.28267571 -0.23794194  1.15528789  0.6210827 ]
 [ 0.96703727  0.38271517 -0.80618482 -0.28899734  0.90852604 -0.39181624
   1.62091229  0.68400133 -0.35340998 -0.25167421]
 [ 0.97139534  0.71304905  1.76041518  1.30620607  1.0576549  -0.60460297
   0.12837699  0.63658341  1.40925339  0.96653925]
 [ 0.77370361  1.27852808 -2.11416392 -0.44222928  1.06821044  0.32352735
  -2.50644065 -0.10999149  0.00854895 -0.41163916]
 [ 1.4468218   0.80745592  1.49810818  0.31223869 -0.68243019 -0.19332164
   0.28807817 -2.07680202  0.94750117 -0.30097615]]
None

  ############ Save/ Load ############################################ 

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
Already up to date.
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master 036d01b] ml_store
 1 file changed, 271 insertions(+)
To github.com:arita37/mlmodels_store.git
   cf1535f..036d01b  master -> master





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
     | -- GenericBlock(units=256, thetas_dim=7, backcast_length=10, forecast_length=5, share_thetas=False) at @139877718659024
     | -- GenericBlock(units=256, thetas_dim=7, backcast_length=10, forecast_length=5, share_thetas=False) at @139877718658800
     | -- GenericBlock(units=256, thetas_dim=7, backcast_length=10, forecast_length=5, share_thetas=False) at @139877718657568
| --  Stack Generic (#1) (share_weights_in_stack=0)
     | -- GenericBlock(units=256, thetas_dim=8, backcast_length=10, forecast_length=5, share_thetas=False) at @139877718657120
     | -- GenericBlock(units=256, thetas_dim=8, backcast_length=10, forecast_length=5, share_thetas=False) at @139877718656616
     | -- GenericBlock(units=256, thetas_dim=8, backcast_length=10, forecast_length=5, share_thetas=False) at @139877718656280

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
grad_step = 000000, loss = 0.497398
plot()
Saved image to .//n_beats_0.png.
grad_step = 000001, loss = 0.367852
grad_step = 000002, loss = 0.280880
grad_step = 000003, loss = 0.189365
grad_step = 000004, loss = 0.107196
grad_step = 000005, loss = 0.065548
grad_step = 000006, loss = 0.079636
grad_step = 000007, loss = 0.071159
grad_step = 000008, loss = 0.037124
grad_step = 000009, loss = 0.013284
grad_step = 000010, loss = 0.010056
grad_step = 000011, loss = 0.017410
grad_step = 000012, loss = 0.024294
grad_step = 000013, loss = 0.025514
grad_step = 000014, loss = 0.021532
grad_step = 000015, loss = 0.015478
grad_step = 000016, loss = 0.011397
grad_step = 000017, loss = 0.011486
grad_step = 000018, loss = 0.013939
grad_step = 000019, loss = 0.014671
grad_step = 000020, loss = 0.012253
grad_step = 000021, loss = 0.008693
grad_step = 000022, loss = 0.006426
grad_step = 000023, loss = 0.006157
grad_step = 000024, loss = 0.007030
grad_step = 000025, loss = 0.007864
grad_step = 000026, loss = 0.008097
grad_step = 000027, loss = 0.007841
grad_step = 000028, loss = 0.007547
grad_step = 000029, loss = 0.007493
grad_step = 000030, loss = 0.007528
grad_step = 000031, loss = 0.007318
grad_step = 000032, loss = 0.006767
grad_step = 000033, loss = 0.006132
grad_step = 000034, loss = 0.005751
grad_step = 000035, loss = 0.005722
grad_step = 000036, loss = 0.005841
grad_step = 000037, loss = 0.005857
grad_step = 000038, loss = 0.005675
grad_step = 000039, loss = 0.005412
grad_step = 000040, loss = 0.005256
grad_step = 000041, loss = 0.005290
grad_step = 000042, loss = 0.005417
grad_step = 000043, loss = 0.005472
grad_step = 000044, loss = 0.005382
grad_step = 000045, loss = 0.005221
grad_step = 000046, loss = 0.005087
grad_step = 000047, loss = 0.005002
grad_step = 000048, loss = 0.004923
grad_step = 000049, loss = 0.004824
grad_step = 000050, loss = 0.004739
grad_step = 000051, loss = 0.004704
grad_step = 000052, loss = 0.004692
grad_step = 000053, loss = 0.004659
grad_step = 000054, loss = 0.004590
grad_step = 000055, loss = 0.004519
grad_step = 000056, loss = 0.004477
grad_step = 000057, loss = 0.004448
grad_step = 000058, loss = 0.004400
grad_step = 000059, loss = 0.004323
grad_step = 000060, loss = 0.004239
grad_step = 000061, loss = 0.004171
grad_step = 000062, loss = 0.004114
grad_step = 000063, loss = 0.004051
grad_step = 000064, loss = 0.003983
grad_step = 000065, loss = 0.003924
grad_step = 000066, loss = 0.003872
grad_step = 000067, loss = 0.003807
grad_step = 000068, loss = 0.003726
grad_step = 000069, loss = 0.003650
grad_step = 000070, loss = 0.003585
grad_step = 000071, loss = 0.003515
grad_step = 000072, loss = 0.003434
grad_step = 000073, loss = 0.003358
grad_step = 000074, loss = 0.003281
grad_step = 000075, loss = 0.003196
grad_step = 000076, loss = 0.003115
grad_step = 000077, loss = 0.003043
grad_step = 000078, loss = 0.002963
grad_step = 000079, loss = 0.002878
grad_step = 000080, loss = 0.002802
grad_step = 000081, loss = 0.002720
grad_step = 000082, loss = 0.002644
grad_step = 000083, loss = 0.002565
grad_step = 000084, loss = 0.002483
grad_step = 000085, loss = 0.002413
grad_step = 000086, loss = 0.002339
grad_step = 000087, loss = 0.002273
grad_step = 000088, loss = 0.002202
grad_step = 000089, loss = 0.002137
grad_step = 000090, loss = 0.002071
grad_step = 000091, loss = 0.002019
grad_step = 000092, loss = 0.001969
grad_step = 000093, loss = 0.001927
grad_step = 000094, loss = 0.001885
grad_step = 000095, loss = 0.001847
grad_step = 000096, loss = 0.001813
grad_step = 000097, loss = 0.001777
grad_step = 000098, loss = 0.001745
grad_step = 000099, loss = 0.001718
grad_step = 000100, loss = 0.001690
plot()
Saved image to .//n_beats_100.png.
grad_step = 000101, loss = 0.001664
grad_step = 000102, loss = 0.001639
grad_step = 000103, loss = 0.001617
grad_step = 000104, loss = 0.001594
grad_step = 000105, loss = 0.001570
grad_step = 000106, loss = 0.001543
grad_step = 000107, loss = 0.001517
grad_step = 000108, loss = 0.001492
grad_step = 000109, loss = 0.001473
grad_step = 000110, loss = 0.001452
grad_step = 000111, loss = 0.001427
grad_step = 000112, loss = 0.001400
grad_step = 000113, loss = 0.001375
grad_step = 000114, loss = 0.001356
grad_step = 000115, loss = 0.001337
grad_step = 000116, loss = 0.001316
grad_step = 000117, loss = 0.001294
grad_step = 000118, loss = 0.001272
grad_step = 000119, loss = 0.001253
grad_step = 000120, loss = 0.001235
grad_step = 000121, loss = 0.001217
grad_step = 000122, loss = 0.001199
grad_step = 000123, loss = 0.001182
grad_step = 000124, loss = 0.001164
grad_step = 000125, loss = 0.001147
grad_step = 000126, loss = 0.001130
grad_step = 000127, loss = 0.001113
grad_step = 000128, loss = 0.001094
grad_step = 000129, loss = 0.001074
grad_step = 000130, loss = 0.001054
grad_step = 000131, loss = 0.001035
grad_step = 000132, loss = 0.001019
grad_step = 000133, loss = 0.001002
grad_step = 000134, loss = 0.000986
grad_step = 000135, loss = 0.000971
grad_step = 000136, loss = 0.000960
grad_step = 000137, loss = 0.000954
grad_step = 000138, loss = 0.000961
grad_step = 000139, loss = 0.000965
grad_step = 000140, loss = 0.000938
grad_step = 000141, loss = 0.000894
grad_step = 000142, loss = 0.000887
grad_step = 000143, loss = 0.000899
grad_step = 000144, loss = 0.000877
grad_step = 000145, loss = 0.000848
grad_step = 000146, loss = 0.000850
grad_step = 000147, loss = 0.000848
grad_step = 000148, loss = 0.000824
grad_step = 000149, loss = 0.000810
grad_step = 000150, loss = 0.000813
grad_step = 000151, loss = 0.000803
grad_step = 000152, loss = 0.000783
grad_step = 000153, loss = 0.000774
grad_step = 000154, loss = 0.000773
grad_step = 000155, loss = 0.000789
grad_step = 000156, loss = 0.000794
grad_step = 000157, loss = 0.000761
grad_step = 000158, loss = 0.000732
grad_step = 000159, loss = 0.000741
grad_step = 000160, loss = 0.000745
grad_step = 000161, loss = 0.000721
grad_step = 000162, loss = 0.000704
grad_step = 000163, loss = 0.000710
grad_step = 000164, loss = 0.000705
grad_step = 000165, loss = 0.000685
grad_step = 000166, loss = 0.000677
grad_step = 000167, loss = 0.000680
grad_step = 000168, loss = 0.000672
grad_step = 000169, loss = 0.000655
grad_step = 000170, loss = 0.000650
grad_step = 000171, loss = 0.000650
grad_step = 000172, loss = 0.000642
grad_step = 000173, loss = 0.000628
grad_step = 000174, loss = 0.000621
grad_step = 000175, loss = 0.000619
grad_step = 000176, loss = 0.000615
grad_step = 000177, loss = 0.000606
grad_step = 000178, loss = 0.000596
grad_step = 000179, loss = 0.000590
grad_step = 000180, loss = 0.000588
grad_step = 000181, loss = 0.000586
grad_step = 000182, loss = 0.000580
grad_step = 000183, loss = 0.000572
grad_step = 000184, loss = 0.000563
grad_step = 000185, loss = 0.000557
grad_step = 000186, loss = 0.000554
grad_step = 000187, loss = 0.000552
grad_step = 000188, loss = 0.000551
grad_step = 000189, loss = 0.000549
grad_step = 000190, loss = 0.000546
grad_step = 000191, loss = 0.000541
grad_step = 000192, loss = 0.000534
grad_step = 000193, loss = 0.000526
grad_step = 000194, loss = 0.000519
grad_step = 000195, loss = 0.000515
grad_step = 000196, loss = 0.000512
grad_step = 000197, loss = 0.000510
grad_step = 000198, loss = 0.000512
grad_step = 000199, loss = 0.000517
grad_step = 000200, loss = 0.000530
plot()
Saved image to .//n_beats_200.png.
grad_step = 000201, loss = 0.000548
grad_step = 000202, loss = 0.000566
grad_step = 000203, loss = 0.000557
grad_step = 000204, loss = 0.000526
grad_step = 000205, loss = 0.000493
grad_step = 000206, loss = 0.000485
grad_step = 000207, loss = 0.000502
grad_step = 000208, loss = 0.000518
grad_step = 000209, loss = 0.000513
grad_step = 000210, loss = 0.000488
grad_step = 000211, loss = 0.000472
grad_step = 000212, loss = 0.000478
grad_step = 000213, loss = 0.000491
grad_step = 000214, loss = 0.000491
grad_step = 000215, loss = 0.000476
grad_step = 000216, loss = 0.000462
grad_step = 000217, loss = 0.000461
grad_step = 000218, loss = 0.000468
grad_step = 000219, loss = 0.000474
grad_step = 000220, loss = 0.000469
grad_step = 000221, loss = 0.000458
grad_step = 000222, loss = 0.000449
grad_step = 000223, loss = 0.000447
grad_step = 000224, loss = 0.000451
grad_step = 000225, loss = 0.000455
grad_step = 000226, loss = 0.000456
grad_step = 000227, loss = 0.000452
grad_step = 000228, loss = 0.000445
grad_step = 000229, loss = 0.000438
grad_step = 000230, loss = 0.000433
grad_step = 000231, loss = 0.000431
grad_step = 000232, loss = 0.000431
grad_step = 000233, loss = 0.000433
grad_step = 000234, loss = 0.000435
grad_step = 000235, loss = 0.000439
grad_step = 000236, loss = 0.000443
grad_step = 000237, loss = 0.000448
grad_step = 000238, loss = 0.000450
grad_step = 000239, loss = 0.000450
grad_step = 000240, loss = 0.000444
grad_step = 000241, loss = 0.000434
grad_step = 000242, loss = 0.000423
grad_step = 000243, loss = 0.000413
grad_step = 000244, loss = 0.000408
grad_step = 000245, loss = 0.000407
grad_step = 000246, loss = 0.000408
grad_step = 000247, loss = 0.000413
grad_step = 000248, loss = 0.000419
grad_step = 000249, loss = 0.000427
grad_step = 000250, loss = 0.000436
grad_step = 000251, loss = 0.000445
grad_step = 000252, loss = 0.000449
grad_step = 000253, loss = 0.000442
grad_step = 000254, loss = 0.000425
grad_step = 000255, loss = 0.000404
grad_step = 000256, loss = 0.000390
grad_step = 000257, loss = 0.000388
grad_step = 000258, loss = 0.000396
grad_step = 000259, loss = 0.000407
grad_step = 000260, loss = 0.000415
grad_step = 000261, loss = 0.000415
grad_step = 000262, loss = 0.000407
grad_step = 000263, loss = 0.000393
grad_step = 000264, loss = 0.000381
grad_step = 000265, loss = 0.000374
grad_step = 000266, loss = 0.000374
grad_step = 000267, loss = 0.000379
grad_step = 000268, loss = 0.000386
grad_step = 000269, loss = 0.000392
grad_step = 000270, loss = 0.000398
grad_step = 000271, loss = 0.000400
grad_step = 000272, loss = 0.000397
grad_step = 000273, loss = 0.000388
grad_step = 000274, loss = 0.000377
grad_step = 000275, loss = 0.000367
grad_step = 000276, loss = 0.000359
grad_step = 000277, loss = 0.000356
grad_step = 000278, loss = 0.000357
grad_step = 000279, loss = 0.000361
grad_step = 000280, loss = 0.000366
grad_step = 000281, loss = 0.000374
grad_step = 000282, loss = 0.000384
grad_step = 000283, loss = 0.000397
grad_step = 000284, loss = 0.000406
grad_step = 000285, loss = 0.000411
grad_step = 000286, loss = 0.000399
grad_step = 000287, loss = 0.000377
grad_step = 000288, loss = 0.000353
grad_step = 000289, loss = 0.000340
grad_step = 000290, loss = 0.000343
grad_step = 000291, loss = 0.000354
grad_step = 000292, loss = 0.000367
grad_step = 000293, loss = 0.000374
grad_step = 000294, loss = 0.000373
grad_step = 000295, loss = 0.000363
grad_step = 000296, loss = 0.000349
grad_step = 000297, loss = 0.000335
grad_step = 000298, loss = 0.000328
grad_step = 000299, loss = 0.000327
grad_step = 000300, loss = 0.000331
plot()
Saved image to .//n_beats_300.png.
grad_step = 000301, loss = 0.000337
grad_step = 000302, loss = 0.000344
grad_step = 000303, loss = 0.000351
grad_step = 000304, loss = 0.000357
grad_step = 000305, loss = 0.000363
grad_step = 000306, loss = 0.000362
grad_step = 000307, loss = 0.000358
grad_step = 000308, loss = 0.000346
grad_step = 000309, loss = 0.000332
grad_step = 000310, loss = 0.000319
grad_step = 000311, loss = 0.000312
grad_step = 000312, loss = 0.000312
grad_step = 000313, loss = 0.000316
grad_step = 000314, loss = 0.000324
grad_step = 000315, loss = 0.000332
grad_step = 000316, loss = 0.000342
grad_step = 000317, loss = 0.000351
grad_step = 000318, loss = 0.000360
grad_step = 000319, loss = 0.000361
grad_step = 000320, loss = 0.000357
grad_step = 000321, loss = 0.000341
grad_step = 000322, loss = 0.000319
grad_step = 000323, loss = 0.000302
grad_step = 000324, loss = 0.000297
grad_step = 000325, loss = 0.000304
grad_step = 000326, loss = 0.000315
grad_step = 000327, loss = 0.000324
grad_step = 000328, loss = 0.000326
grad_step = 000329, loss = 0.000321
grad_step = 000330, loss = 0.000310
grad_step = 000331, loss = 0.000298
grad_step = 000332, loss = 0.000290
grad_step = 000333, loss = 0.000287
grad_step = 000334, loss = 0.000288
grad_step = 000335, loss = 0.000292
grad_step = 000336, loss = 0.000297
grad_step = 000337, loss = 0.000302
grad_step = 000338, loss = 0.000308
grad_step = 000339, loss = 0.000315
grad_step = 000340, loss = 0.000330
grad_step = 000341, loss = 0.000343
grad_step = 000342, loss = 0.000359
grad_step = 000343, loss = 0.000348
grad_step = 000344, loss = 0.000324
grad_step = 000345, loss = 0.000301
grad_step = 000346, loss = 0.000297
grad_step = 000347, loss = 0.000299
grad_step = 000348, loss = 0.000292
grad_step = 000349, loss = 0.000285
grad_step = 000350, loss = 0.000293
grad_step = 000351, loss = 0.000305
grad_step = 000352, loss = 0.000301
grad_step = 000353, loss = 0.000284
grad_step = 000354, loss = 0.000272
grad_step = 000355, loss = 0.000275
grad_step = 000356, loss = 0.000284
grad_step = 000357, loss = 0.000284
grad_step = 000358, loss = 0.000276
grad_step = 000359, loss = 0.000267
grad_step = 000360, loss = 0.000265
grad_step = 000361, loss = 0.000270
grad_step = 000362, loss = 0.000274
grad_step = 000363, loss = 0.000272
grad_step = 000364, loss = 0.000266
grad_step = 000365, loss = 0.000261
grad_step = 000366, loss = 0.000261
grad_step = 000367, loss = 0.000263
grad_step = 000368, loss = 0.000265
grad_step = 000369, loss = 0.000264
grad_step = 000370, loss = 0.000260
grad_step = 000371, loss = 0.000257
grad_step = 000372, loss = 0.000257
grad_step = 000373, loss = 0.000262
grad_step = 000374, loss = 0.000274
grad_step = 000375, loss = 0.000302
grad_step = 000376, loss = 0.000372
grad_step = 000377, loss = 0.000545
grad_step = 000378, loss = 0.000768
grad_step = 000379, loss = 0.000847
grad_step = 000380, loss = 0.000453
grad_step = 000381, loss = 0.000327
grad_step = 000382, loss = 0.000519
grad_step = 000383, loss = 0.000425
grad_step = 000384, loss = 0.000381
grad_step = 000385, loss = 0.000413
grad_step = 000386, loss = 0.000305
grad_step = 000387, loss = 0.000425
grad_step = 000388, loss = 0.000333
grad_step = 000389, loss = 0.000304
grad_step = 000390, loss = 0.000373
grad_step = 000391, loss = 0.000289
grad_step = 000392, loss = 0.000327
grad_step = 000393, loss = 0.000291
grad_step = 000394, loss = 0.000307
grad_step = 000395, loss = 0.000313
grad_step = 000396, loss = 0.000262
grad_step = 000397, loss = 0.000317
grad_step = 000398, loss = 0.000277
grad_step = 000399, loss = 0.000281
grad_step = 000400, loss = 0.000283
plot()
Saved image to .//n_beats_400.png.
grad_step = 000401, loss = 0.000266
grad_step = 000402, loss = 0.000286
grad_step = 000403, loss = 0.000262
grad_step = 000404, loss = 0.000259
grad_step = 000405, loss = 0.000278
grad_step = 000406, loss = 0.000254
grad_step = 000407, loss = 0.000259
grad_step = 000408, loss = 0.000261
grad_step = 000409, loss = 0.000251
grad_step = 000410, loss = 0.000260
grad_step = 000411, loss = 0.000252
grad_step = 000412, loss = 0.000245
grad_step = 000413, loss = 0.000256
grad_step = 000414, loss = 0.000249
grad_step = 000415, loss = 0.000242
grad_step = 000416, loss = 0.000249
grad_step = 000417, loss = 0.000245
grad_step = 000418, loss = 0.000243
grad_step = 000419, loss = 0.000245
grad_step = 000420, loss = 0.000241
grad_step = 000421, loss = 0.000238
grad_step = 000422, loss = 0.000243
grad_step = 000423, loss = 0.000240
grad_step = 000424, loss = 0.000236
grad_step = 000425, loss = 0.000237
grad_step = 000426, loss = 0.000237
grad_step = 000427, loss = 0.000235
grad_step = 000428, loss = 0.000235
grad_step = 000429, loss = 0.000235
grad_step = 000430, loss = 0.000233
grad_step = 000431, loss = 0.000232
grad_step = 000432, loss = 0.000233
grad_step = 000433, loss = 0.000232
grad_step = 000434, loss = 0.000231
grad_step = 000435, loss = 0.000231
grad_step = 000436, loss = 0.000230
grad_step = 000437, loss = 0.000229
grad_step = 000438, loss = 0.000229
grad_step = 000439, loss = 0.000229
grad_step = 000440, loss = 0.000228
grad_step = 000441, loss = 0.000227
grad_step = 000442, loss = 0.000227
grad_step = 000443, loss = 0.000226
grad_step = 000444, loss = 0.000226
grad_step = 000445, loss = 0.000225
grad_step = 000446, loss = 0.000225
grad_step = 000447, loss = 0.000225
grad_step = 000448, loss = 0.000224
grad_step = 000449, loss = 0.000223
grad_step = 000450, loss = 0.000223
grad_step = 000451, loss = 0.000223
grad_step = 000452, loss = 0.000222
grad_step = 000453, loss = 0.000222
grad_step = 000454, loss = 0.000221
grad_step = 000455, loss = 0.000221
grad_step = 000456, loss = 0.000220
grad_step = 000457, loss = 0.000220
grad_step = 000458, loss = 0.000219
grad_step = 000459, loss = 0.000219
grad_step = 000460, loss = 0.000218
grad_step = 000461, loss = 0.000218
grad_step = 000462, loss = 0.000218
grad_step = 000463, loss = 0.000217
grad_step = 000464, loss = 0.000217
grad_step = 000465, loss = 0.000217
grad_step = 000466, loss = 0.000217
grad_step = 000467, loss = 0.000217
grad_step = 000468, loss = 0.000219
grad_step = 000469, loss = 0.000221
grad_step = 000470, loss = 0.000227
grad_step = 000471, loss = 0.000236
grad_step = 000472, loss = 0.000250
grad_step = 000473, loss = 0.000272
grad_step = 000474, loss = 0.000295
grad_step = 000475, loss = 0.000320
grad_step = 000476, loss = 0.000327
grad_step = 000477, loss = 0.000312
grad_step = 000478, loss = 0.000271
grad_step = 000479, loss = 0.000230
grad_step = 000480, loss = 0.000213
grad_step = 000481, loss = 0.000225
grad_step = 000482, loss = 0.000249
grad_step = 000483, loss = 0.000262
grad_step = 000484, loss = 0.000254
grad_step = 000485, loss = 0.000231
grad_step = 000486, loss = 0.000213
grad_step = 000487, loss = 0.000212
grad_step = 000488, loss = 0.000226
grad_step = 000489, loss = 0.000239
grad_step = 000490, loss = 0.000242
grad_step = 000491, loss = 0.000235
grad_step = 000492, loss = 0.000222
grad_step = 000493, loss = 0.000211
grad_step = 000494, loss = 0.000210
grad_step = 000495, loss = 0.000215
grad_step = 000496, loss = 0.000221
grad_step = 000497, loss = 0.000224
grad_step = 000498, loss = 0.000222
grad_step = 000499, loss = 0.000218
grad_step = 000500, loss = 0.000215
plot()
Saved image to .//n_beats_500.png.
grad_step = 000501, loss = 0.000213
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
[[0.86088586 0.84520316 0.9321059  0.9679598  1.0202739 ]
 [0.8326607  0.918546   0.94390744 1.0062436  0.99478203]
 [0.9030942  0.9129287  1.000505   0.9963446  0.9585825 ]
 [0.9218735  0.99895203 0.98481256 0.9544177  0.9252423 ]
 [1.0051851  0.9903505  0.956847   0.918768   0.8651393 ]
 [0.9744815  0.9465828  0.9195543  0.8657541  0.8646014 ]
 [0.930227   0.9053529  0.86082345 0.8576853  0.82800025]
 [0.89019537 0.82500076 0.8585618  0.8300103  0.84726965]
 [0.8174139  0.8388342  0.8186951  0.83563244 0.8722291 ]
 [0.8308698  0.8051834  0.84510773 0.8496696  0.8278295 ]
 [0.802041   0.83376366 0.844671   0.8511125  0.92798245]
 [0.8152608  0.8511394  0.8317094  0.9177511  0.95992976]
 [0.8523556  0.84264183 0.92595273 0.9659249  1.0161514 ]
 [0.83386564 0.9283576  0.94358385 1.0038149  0.98606795]
 [0.92157584 0.9313174  1.002816   0.9884014  0.9422726 ]
 [0.93560266 1.0097257  0.97995317 0.93848777 0.90493476]
 [1.0047216  0.9809753  0.9418306  0.90187275 0.84414816]
 [0.96912324 0.92606485 0.89888746 0.84483266 0.84653604]
 [0.92615783 0.8913176  0.8401187  0.8425586  0.8178346 ]
 [0.9011884  0.8325108  0.8458716  0.8257172  0.8439731 ]
 [0.8340236  0.8507036  0.81809783 0.83736736 0.87566125]
 [0.84846294 0.82215697 0.8472199  0.8560716  0.8348932 ]
 [0.817595   0.84392166 0.85195434 0.8558973  0.9295163 ]
 [0.8237922  0.8672     0.83884245 0.92126596 0.96228766]
 [0.87200236 0.8501987  0.93229645 0.97012305 1.0289221 ]
 [0.84137684 0.92727935 0.94734377 1.0132962  1.0053254 ]
 [0.9114922  0.9241395  1.0088484  1.0097555  0.9713992 ]
 [0.93480796 1.0120375  0.9975965  0.96885777 0.9374535 ]
 [1.0162439  1.002429   0.97114486 0.93177235 0.87339985]
 [0.985673   0.95226765 0.92955095 0.8732422  0.8695078 ]
 [0.93694705 0.909867   0.8659442  0.8631071  0.8344511 ]]

  #### Plot     ############################################### 
Saved image to ztest/model_tch/nbeats//n_beats_test.png.

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
Already up to date.
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master 1271a33] ml_store
 1 file changed, 1122 insertions(+)
To github.com:arita37/mlmodels_store.git
   036d01b..1271a33  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//transformer_classifier.py 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//transformer_classifier.py", line 522, in <module>
    model_pars, data_pars, compute_pars, out_pars = get_params(param_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//transformer_classifier.py", line 418, in get_params
    cf = json.load(open(data_path, mode='r'))
FileNotFoundError: [Errno 2] No such file or directory: 'model_tch/transformer_classifier.json'

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
Already up to date.
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master ef19752] ml_store
 1 file changed, 37 insertions(+)
To github.com:arita37/mlmodels_store.git
   1271a33..ef19752  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//matchzoo_models.py 

  #### Loading params   ############################################## 

  {'dataset': 'WIKI_QA', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/nlp/', 'dataset_pars': {'data_pack': '', 'mode': 'pair', 'num_dup': 2, 'num_neg': 1, 'batch_size': 20, 'resample': True, 'sort': False, 'callbacks': 'PADDING'}, 'dataloader': '', 'dataloader_pars': {'device': 'cpu', 'dataset': 'None', 'stage': 'train', 'callback': 'PADDING'}, 'preprocess': {'train': {'transform': True, 'mode': 'pair', 'num_dup': 2, 'num_neg': 1, 'batch_size': 20, 'stage': 'train', 'resample': True, 'sort': False, 'dataloader_callback': 'PADDING'}, 'test': {'transform': True, 'batch_size': 20, 'stage': 'dev', 'dataloader_callback': 'PADDING'}}} {'checkpointdir': 'ztest/model_tch/MATCHZOO/BERT/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/MATCHZOO/BERT/'} 

  #### Loading dataset   ############################################# 

  #### Model init   ################################################## 
  0%|          | 0/231508 [00:00<?, ?B/s]100%|██████████| 231508/231508 [00:00<00:00, 10994530.34B/s]
  0%|          | 0/433 [00:00<?, ?B/s]100%|██████████| 433/433 [00:00<00:00, 228071.53B/s]
  0%|          | 0/440473133 [00:00<?, ?B/s]  1%|          | 4890624/440473133 [00:00<00:08, 48897659.63B/s]  3%|▎         | 11340800/440473133 [00:00<00:08, 52722195.58B/s]  4%|▍         | 18036736/440473133 [00:00<00:07, 56312275.47B/s]  6%|▌         | 24837120/440473133 [00:00<00:07, 59373984.18B/s]  7%|▋         | 31824896/440473133 [00:00<00:06, 62176324.87B/s]  9%|▉         | 38745088/440473133 [00:00<00:06, 64129020.37B/s] 10%|█         | 45570048/440473133 [00:00<00:06, 65310171.67B/s] 12%|█▏        | 52431872/440473133 [00:00<00:05, 66264508.37B/s] 13%|█▎        | 59261952/440473133 [00:00<00:05, 66862129.26B/s] 15%|█▍        | 66061312/440473133 [00:01<00:05, 67188971.59B/s] 17%|█▋        | 72918016/440473133 [00:01<00:05, 67594700.75B/s] 18%|█▊        | 79738880/440473133 [00:01<00:05, 67777641.85B/s] 20%|█▉        | 86464512/440473133 [00:01<00:05, 67370812.86B/s] 21%|██        | 93479936/440473133 [00:01<00:05, 68181725.74B/s] 23%|██▎       | 100303872/440473133 [00:01<00:04, 68197172.81B/s] 24%|██▍       | 107317248/440473133 [00:01<00:04, 68766507.22B/s] 26%|██▌       | 114224128/440473133 [00:01<00:04, 68856789.19B/s] 28%|██▊       | 121153536/440473133 [00:01<00:04, 68983927.75B/s] 29%|██▉       | 128047104/440473133 [00:01<00:04, 68721708.89B/s] 31%|███       | 135016448/440473133 [00:02<00:04, 69008142.34B/s] 32%|███▏      | 141948928/440473133 [00:02<00:04, 69095219.49B/s] 34%|███▍      | 148857856/440473133 [00:02<00:04, 68997168.42B/s] 35%|███▌      | 155908096/440473133 [00:02<00:04, 69436437.52B/s] 37%|███▋      | 162953216/440473133 [00:02<00:03, 69730693.93B/s] 39%|███▊      | 169998336/440473133 [00:02<00:03, 69944369.74B/s] 40%|████      | 177140736/440473133 [00:02<00:03, 70379866.84B/s] 42%|████▏     | 184384512/440473133 [00:02<00:03, 70984424.15B/s] 43%|████▎     | 191484928/440473133 [00:02<00:03, 70922604.89B/s] 45%|████▌     | 198764544/440473133 [00:02<00:03, 71473382.31B/s] 47%|████▋     | 205924352/440473133 [00:03<00:03, 71510562.08B/s] 48%|████▊     | 213076992/440473133 [00:03<00:03, 71310934.54B/s] 50%|████▉     | 220210176/440473133 [00:03<00:03, 70412191.16B/s] 52%|█████▏    | 227255296/440473133 [00:03<00:03, 70204558.31B/s] 53%|█████▎    | 234278912/440473133 [00:03<00:02, 69834161.35B/s] 55%|█████▍    | 241331200/440473133 [00:03<00:02, 70038484.71B/s] 56%|█████▋    | 248337408/440473133 [00:03<00:02, 69923178.78B/s] 58%|█████▊    | 255331328/440473133 [00:03<00:02, 69771528.96B/s] 60%|█████▉    | 262309888/440473133 [00:03<00:02, 69665613.83B/s] 61%|██████    | 269277184/440473133 [00:03<00:02, 68886791.06B/s] 63%|██████▎   | 276476928/440473133 [00:04<00:02, 69790733.97B/s] 64%|██████▍   | 283506688/440473133 [00:04<00:02, 69937963.36B/s] 66%|██████▌   | 290504704/440473133 [00:04<00:02, 69757427.65B/s] 68%|██████▊   | 297483264/440473133 [00:04<00:02, 69213670.79B/s] 69%|██████▉   | 304437248/440473133 [00:04<00:01, 69307612.69B/s] 71%|███████   | 311452672/440473133 [00:04<00:01, 69558924.57B/s] 72%|███████▏  | 318499840/440473133 [00:04<00:01, 69829338.34B/s] 74%|███████▍  | 325484544/440473133 [00:04<00:01, 69136406.25B/s] 75%|███████▌  | 332527616/440473133 [00:04<00:01, 69514396.94B/s] 77%|███████▋  | 339627008/440473133 [00:04<00:01, 69949785.91B/s] 79%|███████▊  | 346719232/440473133 [00:05<00:01, 70237188.01B/s] 80%|████████  | 353744896/440473133 [00:05<00:01, 70095070.03B/s] 82%|████████▏ | 360756224/440473133 [00:05<00:01, 69952179.08B/s] 83%|████████▎ | 367753216/440473133 [00:05<00:01, 68846212.33B/s] 85%|████████▌ | 374805504/440473133 [00:05<00:00, 69335242.12B/s] 87%|████████▋ | 382094336/440473133 [00:05<00:00, 70362426.60B/s] 88%|████████▊ | 389355520/440473133 [00:05<00:00, 71019667.58B/s] 90%|█████████ | 396509184/440473133 [00:05<00:00, 71173486.81B/s] 92%|█████████▏| 403631104/440473133 [00:05<00:00, 70884516.54B/s] 93%|█████████▎| 410844160/440473133 [00:05<00:00, 71231610.55B/s] 95%|█████████▍| 417970176/440473133 [00:06<00:00, 71086227.52B/s] 97%|█████████▋| 425080832/440473133 [00:06<00:00, 71004757.07B/s] 98%|█████████▊| 432183296/440473133 [00:06<00:00, 69941050.02B/s]100%|█████████▉| 439182336/440473133 [00:06<00:00, 69431652.56B/s]100%|██████████| 440473133/440473133 [00:06<00:00, 69240988.53B/s]Downloading data from https://download.microsoft.com/download/E/5/F/E5FCFCEE-7005-4814-853D-DAA7C66507E0/WikiQACorpus.zip

   8192/7094233 [..............................] - ETA: 0s
 131072/7094233 [..............................] - ETA: 2s
 565248/7094233 [=>............................] - ETA: 1s
2670592/7094233 [==========>...................] - ETA: 0s
7094272/7094233 [==============================] - 0s 0us/step

Processing text_left with encode:   0%|          | 0/2118 [00:00<?, ?it/s]Processing text_left with encode:  17%|█▋        | 363/2118 [00:00<00:00, 3629.58it/s]Processing text_left with encode:  40%|███▉      | 844/2118 [00:00<00:00, 3917.85it/s]Processing text_left with encode:  63%|██████▎   | 1329/2118 [00:00<00:00, 4157.50it/s]Processing text_left with encode:  86%|████████▌ | 1818/2118 [00:00<00:00, 4352.64it/s]Processing text_left with encode: 100%|██████████| 2118/2118 [00:00<00:00, 4601.34it/s]
Processing text_right with encode:   0%|          | 0/18841 [00:00<?, ?it/s]Processing text_right with encode:   1%|          | 171/18841 [00:00<00:10, 1703.43it/s]Processing text_right with encode:   2%|▏         | 355/18841 [00:00<00:10, 1739.50it/s]Processing text_right with encode:   3%|▎         | 532/18841 [00:00<00:10, 1744.21it/s]Processing text_right with encode:   4%|▍         | 709/18841 [00:00<00:10, 1749.39it/s]Processing text_right with encode:   5%|▍         | 888/18841 [00:00<00:10, 1760.60it/s]Processing text_right with encode:   6%|▌         | 1060/18841 [00:00<00:10, 1744.62it/s]Processing text_right with encode:   6%|▋         | 1222/18841 [00:00<00:10, 1703.40it/s]Processing text_right with encode:   7%|▋         | 1389/18841 [00:00<00:10, 1692.51it/s]Processing text_right with encode:   8%|▊         | 1564/18841 [00:00<00:10, 1709.04it/s]Processing text_right with encode:   9%|▉         | 1753/18841 [00:01<00:09, 1757.51it/s]Processing text_right with encode:  10%|█         | 1925/18841 [00:01<00:09, 1740.41it/s]Processing text_right with encode:  11%|█         | 2102/18841 [00:01<00:09, 1747.51it/s]Processing text_right with encode:  12%|█▏        | 2293/18841 [00:01<00:09, 1791.06it/s]Processing text_right with encode:  13%|█▎        | 2471/18841 [00:01<00:09, 1783.10it/s]Processing text_right with encode:  14%|█▍        | 2649/18841 [00:01<00:09, 1777.69it/s]Processing text_right with encode:  15%|█▌        | 2850/18841 [00:01<00:08, 1840.55it/s]Processing text_right with encode:  16%|█▌        | 3035/18841 [00:01<00:08, 1759.11it/s]Processing text_right with encode:  17%|█▋        | 3212/18841 [00:01<00:08, 1749.09it/s]Processing text_right with encode:  18%|█▊        | 3388/18841 [00:01<00:08, 1733.68it/s]Processing text_right with encode:  19%|█▉        | 3562/18841 [00:02<00:08, 1714.39it/s]Processing text_right with encode:  20%|█▉        | 3741/18841 [00:02<00:08, 1734.86it/s]Processing text_right with encode:  21%|██        | 3915/18841 [00:02<00:08, 1719.19it/s]Processing text_right with encode:  22%|██▏       | 4102/18841 [00:02<00:08, 1761.72it/s]Processing text_right with encode:  23%|██▎       | 4279/18841 [00:02<00:08, 1748.95it/s]Processing text_right with encode:  24%|██▎       | 4455/18841 [00:02<00:08, 1723.39it/s]Processing text_right with encode:  25%|██▍       | 4629/18841 [00:02<00:08, 1727.96it/s]Processing text_right with encode:  26%|██▌       | 4806/18841 [00:02<00:08, 1738.99it/s]Processing text_right with encode:  26%|██▋       | 4982/18841 [00:02<00:07, 1744.42it/s]Processing text_right with encode:  27%|██▋       | 5168/18841 [00:02<00:07, 1775.51it/s]Processing text_right with encode:  28%|██▊       | 5355/18841 [00:03<00:07, 1801.95it/s]Processing text_right with encode:  29%|██▉       | 5536/18841 [00:03<00:07, 1776.76it/s]Processing text_right with encode:  30%|███       | 5714/18841 [00:03<00:07, 1757.56it/s]Processing text_right with encode:  31%|███▏      | 5890/18841 [00:03<00:07, 1747.01it/s]Processing text_right with encode:  32%|███▏      | 6065/18841 [00:03<00:07, 1708.58it/s]Processing text_right with encode:  33%|███▎      | 6237/18841 [00:03<00:07, 1696.12it/s]Processing text_right with encode:  34%|███▍      | 6420/18841 [00:03<00:07, 1733.89it/s]Processing text_right with encode:  35%|███▌      | 6605/18841 [00:03<00:06, 1766.62it/s]Processing text_right with encode:  36%|███▌      | 6783/18841 [00:03<00:06, 1748.95it/s]Processing text_right with encode:  37%|███▋      | 6959/18841 [00:03<00:06, 1730.43it/s]Processing text_right with encode:  38%|███▊      | 7133/18841 [00:04<00:06, 1717.28it/s]Processing text_right with encode:  39%|███▉      | 7325/18841 [00:04<00:06, 1765.92it/s]Processing text_right with encode:  40%|███▉      | 7508/18841 [00:04<00:06, 1782.37it/s]Processing text_right with encode:  41%|████      | 7687/18841 [00:04<00:06, 1765.70it/s]Processing text_right with encode:  42%|████▏     | 7866/18841 [00:04<00:06, 1772.79it/s]Processing text_right with encode:  43%|████▎     | 8044/18841 [00:04<00:06, 1737.12it/s]Processing text_right with encode:  44%|████▎     | 8221/18841 [00:04<00:06, 1745.11it/s]Processing text_right with encode:  45%|████▍     | 8403/18841 [00:04<00:05, 1765.11it/s]Processing text_right with encode:  46%|████▌     | 8580/18841 [00:04<00:05, 1741.76it/s]Processing text_right with encode:  47%|████▋     | 8766/18841 [00:04<00:05, 1772.60it/s]Processing text_right with encode:  47%|████▋     | 8944/18841 [00:05<00:05, 1770.41it/s]Processing text_right with encode:  48%|████▊     | 9122/18841 [00:05<00:05, 1753.86it/s]Processing text_right with encode:  49%|████▉     | 9302/18841 [00:05<00:05, 1766.96it/s]Processing text_right with encode:  50%|█████     | 9481/18841 [00:05<00:05, 1773.04it/s]Processing text_right with encode:  51%|█████▏    | 9661/18841 [00:05<00:05, 1779.95it/s]Processing text_right with encode:  52%|█████▏    | 9840/18841 [00:05<00:05, 1733.03it/s]Processing text_right with encode:  53%|█████▎    | 10033/18841 [00:05<00:04, 1786.38it/s]Processing text_right with encode:  54%|█████▍    | 10213/18841 [00:05<00:04, 1745.79it/s]Processing text_right with encode:  55%|█████▌    | 10389/18841 [00:05<00:04, 1749.82it/s]Processing text_right with encode:  56%|█████▌    | 10587/18841 [00:06<00:04, 1811.91it/s]Processing text_right with encode:  57%|█████▋    | 10770/18841 [00:06<00:04, 1780.49it/s]Processing text_right with encode:  58%|█████▊    | 10949/18841 [00:06<00:04, 1747.05it/s]Processing text_right with encode:  59%|█████▉    | 11125/18841 [00:06<00:04, 1668.90it/s]Processing text_right with encode:  60%|█████▉    | 11296/18841 [00:06<00:04, 1679.55it/s]Processing text_right with encode:  61%|██████    | 11469/18841 [00:06<00:04, 1693.02it/s]Processing text_right with encode:  62%|██████▏   | 11639/18841 [00:06<00:04, 1681.91it/s]Processing text_right with encode:  63%|██████▎   | 11822/18841 [00:06<00:04, 1722.53it/s]Processing text_right with encode:  64%|██████▎   | 11995/18841 [00:06<00:04, 1710.04it/s]Processing text_right with encode:  65%|██████▍   | 12167/18841 [00:06<00:03, 1705.94it/s]Processing text_right with encode:  66%|██████▌   | 12342/18841 [00:07<00:03, 1717.83it/s]Processing text_right with encode:  66%|██████▋   | 12518/18841 [00:07<00:03, 1727.57it/s]Processing text_right with encode:  67%|██████▋   | 12693/18841 [00:07<00:03, 1732.02it/s]Processing text_right with encode:  68%|██████▊   | 12872/18841 [00:07<00:03, 1748.40it/s]Processing text_right with encode:  69%|██████▉   | 13055/18841 [00:07<00:03, 1771.58it/s]Processing text_right with encode:  70%|███████   | 13233/18841 [00:07<00:03, 1743.10it/s]Processing text_right with encode:  71%|███████   | 13420/18841 [00:07<00:03, 1777.44it/s]Processing text_right with encode:  72%|███████▏  | 13605/18841 [00:07<00:02, 1798.24it/s]Processing text_right with encode:  73%|███████▎  | 13800/18841 [00:07<00:02, 1838.75it/s]Processing text_right with encode:  74%|███████▍  | 13986/18841 [00:07<00:02, 1843.08it/s]Processing text_right with encode:  75%|███████▌  | 14171/18841 [00:08<00:02, 1789.67it/s]Processing text_right with encode:  76%|███████▌  | 14351/18841 [00:08<00:02, 1738.91it/s]Processing text_right with encode:  77%|███████▋  | 14526/18841 [00:08<00:02, 1731.47it/s]Processing text_right with encode:  78%|███████▊  | 14717/18841 [00:08<00:02, 1779.64it/s]Processing text_right with encode:  79%|███████▉  | 14898/18841 [00:08<00:02, 1788.59it/s]Processing text_right with encode:  80%|████████  | 15078/18841 [00:08<00:02, 1780.55it/s]Processing text_right with encode:  81%|████████  | 15257/18841 [00:08<00:02, 1782.25it/s]Processing text_right with encode:  82%|████████▏ | 15436/18841 [00:08<00:01, 1784.04it/s]Processing text_right with encode:  83%|████████▎ | 15627/18841 [00:08<00:01, 1818.75it/s]Processing text_right with encode:  84%|████████▍ | 15820/18841 [00:08<00:01, 1850.36it/s]Processing text_right with encode:  85%|████████▍ | 16006/18841 [00:09<00:01, 1795.68it/s]Processing text_right with encode:  86%|████████▌ | 16187/18841 [00:09<00:01, 1786.87it/s]Processing text_right with encode:  87%|████████▋ | 16370/18841 [00:09<00:01, 1798.02it/s]Processing text_right with encode:  88%|████████▊ | 16551/18841 [00:09<00:01, 1771.76it/s]Processing text_right with encode:  89%|████████▉ | 16741/18841 [00:09<00:01, 1805.68it/s]Processing text_right with encode:  90%|████████▉ | 16922/18841 [00:09<00:01, 1784.09it/s]Processing text_right with encode:  91%|█████████ | 17101/18841 [00:09<00:00, 1767.40it/s]Processing text_right with encode:  92%|█████████▏| 17278/18841 [00:09<00:00, 1746.54it/s]Processing text_right with encode:  93%|█████████▎| 17453/18841 [00:09<00:00, 1690.87it/s]Processing text_right with encode:  94%|█████████▎| 17636/18841 [00:10<00:00, 1726.23it/s]Processing text_right with encode:  95%|█████████▍| 17816/18841 [00:10<00:00, 1746.43it/s]Processing text_right with encode:  96%|█████████▌| 18007/18841 [00:10<00:00, 1788.74it/s]Processing text_right with encode:  97%|█████████▋| 18203/18841 [00:10<00:00, 1835.71it/s]Processing text_right with encode:  98%|█████████▊| 18388/18841 [00:10<00:00, 1823.77it/s]Processing text_right with encode:  99%|█████████▊| 18584/18841 [00:10<00:00, 1861.67it/s]Processing text_right with encode: 100%|█████████▉| 18771/18841 [00:10<00:00, 1840.31it/s]Processing text_right with encode: 100%|██████████| 18841/18841 [00:10<00:00, 1762.75it/s]
Processing length_left with len:   0%|          | 0/2118 [00:00<?, ?it/s]Processing length_left with len: 100%|██████████| 2118/2118 [00:00<00:00, 402151.92it/s]
Processing length_right with len:   0%|          | 0/18841 [00:00<?, ?it/s]Processing length_right with len: 100%|██████████| 18841/18841 [00:00<00:00, 799450.49it/s]
Processing text_left with encode:   0%|          | 0/633 [00:00<?, ?it/s]Processing text_left with encode:  74%|███████▍  | 468/633 [00:00<00:00, 4673.82it/s]Processing text_left with encode: 100%|██████████| 633/633 [00:00<00:00, 4685.98it/s]
Processing text_right with encode:   0%|          | 0/5961 [00:00<?, ?it/s]Processing text_right with encode:   3%|▎         | 176/5961 [00:00<00:03, 1758.53it/s]Processing text_right with encode:   6%|▌         | 340/5961 [00:00<00:03, 1718.30it/s]Processing text_right with encode:   9%|▊         | 508/5961 [00:00<00:03, 1704.62it/s]Processing text_right with encode:  12%|█▏        | 698/5961 [00:00<00:02, 1758.60it/s]Processing text_right with encode:  15%|█▍        | 890/5961 [00:00<00:02, 1804.04it/s]Processing text_right with encode:  18%|█▊        | 1073/5961 [00:00<00:02, 1810.04it/s]Processing text_right with encode:  21%|██        | 1259/5961 [00:00<00:02, 1822.40it/s]Processing text_right with encode:  24%|██▍       | 1438/5961 [00:00<00:02, 1810.87it/s]Processing text_right with encode:  27%|██▋       | 1614/5961 [00:00<00:02, 1792.26it/s]Processing text_right with encode:  30%|██▉       | 1787/5961 [00:01<00:02, 1765.49it/s]Processing text_right with encode:  33%|███▎      | 1972/5961 [00:01<00:02, 1787.20it/s]Processing text_right with encode:  36%|███▌      | 2155/5961 [00:01<00:02, 1799.81it/s]Processing text_right with encode:  39%|███▉      | 2333/5961 [00:01<00:02, 1790.59it/s]Processing text_right with encode:  42%|████▏     | 2511/5961 [00:01<00:01, 1738.75it/s]Processing text_right with encode:  45%|████▌     | 2695/5961 [00:01<00:01, 1765.93it/s]Processing text_right with encode:  49%|████▊     | 2899/5961 [00:01<00:01, 1839.16it/s]Processing text_right with encode:  52%|█████▏    | 3091/5961 [00:01<00:01, 1862.00it/s]Processing text_right with encode:  55%|█████▍    | 3278/5961 [00:01<00:01, 1830.50it/s]Processing text_right with encode:  58%|█████▊    | 3462/5961 [00:01<00:01, 1727.98it/s]Processing text_right with encode:  61%|██████    | 3644/5961 [00:02<00:01, 1753.17it/s]Processing text_right with encode:  64%|██████▍   | 3823/5961 [00:02<00:01, 1760.57it/s]Processing text_right with encode:  67%|██████▋   | 4012/5961 [00:02<00:01, 1796.87it/s]Processing text_right with encode:  70%|███████   | 4199/5961 [00:02<00:00, 1816.86it/s]Processing text_right with encode:  74%|███████▎  | 4382/5961 [00:02<00:00, 1808.08it/s]Processing text_right with encode:  77%|███████▋  | 4564/5961 [00:02<00:00, 1798.26it/s]Processing text_right with encode:  80%|███████▉  | 4745/5961 [00:02<00:00, 1790.71it/s]Processing text_right with encode:  83%|████████▎ | 4925/5961 [00:02<00:00, 1737.97it/s]Processing text_right with encode:  86%|████████▌ | 5102/5961 [00:02<00:00, 1745.67it/s]Processing text_right with encode:  89%|████████▊ | 5277/5961 [00:02<00:00, 1678.34it/s]Processing text_right with encode:  91%|█████████▏| 5446/5961 [00:03<00:00, 1670.55it/s]Processing text_right with encode:  94%|█████████▍| 5614/5961 [00:03<00:00, 1647.30it/s]Processing text_right with encode:  97%|█████████▋| 5780/5961 [00:03<00:00, 1619.84it/s]Processing text_right with encode: 100%|██████████| 5961/5961 [00:03<00:00, 1763.83it/s]
Processing length_left with len:   0%|          | 0/633 [00:00<?, ?it/s]Processing length_left with len: 100%|██████████| 633/633 [00:00<00:00, 388497.87it/s]
Processing length_right with len:   0%|          | 0/5961 [00:00<?, ?it/s]Processing length_right with len: 100%|██████████| 5961/5961 [00:00<00:00, 671363.45it/s]
  #### Model  fit   ############################################# 

  0%|          | 0/102 [00:00<?, ?it/s]Epoch 1/1:   0%|          | 0/102 [00:18<?, ?it/s]Epoch 1/1:   0%|          | 0/102 [00:18<?, ?it/s, loss=1.442]Epoch 1/1:   1%|          | 1/102 [00:18<31:12, 18.54s/it, loss=1.442]Killed

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
From github.com:arita37/mlmodels_store
   ef19752..ace4480  master     -> origin/master
Updating ef19752..ace4480
Fast-forward
 error_list/20200515/list_log_benchmark_20200515.md | 166 ++++++++++-----------
 .../20200515/list_log_dataloader_20200515.md       |   2 +-
 error_list/20200515/list_log_testall_20200515.md   |  36 +++++
 3 files changed, 120 insertions(+), 84 deletions(-)
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master ad2d5ba] ml_store
 1 file changed, 67 insertions(+)
To github.com:arita37/mlmodels_store.git
   ace4480..ad2d5ba  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//torchhub.py 

  #### Loading params   ############################################## 

  {'dataset': 'torchvision.datasets:MNIST', 'transform_uri': 'mlmodels.preprocess.image.py:torch_transform_mnist', '2nd___transform_uri': '/mnt/hgfs/d/gitdev/mlmodels/mlmodels/preprocess/image.py:torch_transform_mnist', 'data_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/', 'train_batch_size': 4, 'test_batch_size': 1} {'checkpointdir': 'ztest/model_tch/torchhub/restnet18/checkpoints/', 'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tch/torchhub/restnet18/'} 

  #### Loading dataset   ############################################# 

  #### If transformer URI is Provided 

  #### Loading dataloader URI 
0it [00:00, ?it/s]  0%|          | 16384/9912422 [00:00<01:21, 122053.82it/s] 78%|███████▊  | 7725056/9912422 [00:00<00:12, 174244.10it/s]9920512it [00:00, 39200535.08it/s]                           
0it [00:00, ?it/s]32768it [00:00, 638662.78it/s]
0it [00:00, ?it/s]  3%|▎         | 49152/1648877 [00:00<00:03, 466891.85it/s]1654784it [00:00, 11255695.66it/s]                         
0it [00:00, ?it/s]8192it [00:00, 168418.53it/s]dataset :  <class 'torchvision.datasets.mnist.MNIST'>
Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz to /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw/train-images-idx3-ubyte.gz
Extracting /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw/train-images-idx3-ubyte.gz to /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw
Downloading http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz to /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw/train-labels-idx1-ubyte.gz
Extracting /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw/train-labels-idx1-ubyte.gz to /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw
Downloading http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz to /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw/t10k-images-idx3-ubyte.gz
Extracting /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw/t10k-images-idx3-ubyte.gz to /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw
Downloading http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz to /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw/t10k-labels-idx1-ubyte.gz
Extracting /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw/t10k-labels-idx1-ubyte.gz to /home/runner/work/mlmodels/mlmodels/mlmodels/dataset/vision/MNIST/raw
Processing...
Done!

  #### Model init, fit   ############################################# 

  #### If transformer URI is Provided 

  #### Loading dataloader URI 

Downloading: "https://github.com/pytorch/vision/archive/master.zip" to /home/runner/.cache/torch/hub/master.zip
dataset :  <class 'torchvision.datasets.mnist.MNIST'>
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//torchhub.py", line 406, in <module>
    test(data_path="model_tch/torchhub_cnn_list.json", pars_choice="json", config_mode="resnet18")
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//torchhub.py", line 338, in test
    model, session = fit(model, data_pars, compute_pars, out_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//torchhub.py", line 207, in fit
    tr_loss, tr_acc = _train(model0, device, train_iter, criterion, optimizer, epoch, epochs, imax=imax_train)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//torchhub.py", line 46, in _train
    for i,batch in enumerate(train_itr):
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/dataloader.py", line 346, in __next__
    data = self.dataset_fetcher.fetch(index)  # may raise StopIteration
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/fetch.py", line 47, in fetch
    return self.collate_fn(data)
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in default_collate
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 80, in <listcomp>
    return [default_collate(samples) for samples in transposed]
  File "/opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/torch/utils/data/_utils/collate.py", line 82, in default_collate
    raise TypeError(default_collate_err_msg_format.format(elem_type))
TypeError: default_collate: batch must contain tensors, numpy arrays, numbers, dicts or lists; found <class 'PIL.Image.Image'>

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
Already up to date.
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
[master 0723b36] ml_store
 1 file changed, 84 insertions(+)
To github.com:arita37/mlmodels_store.git
   ad2d5ba..0723b36  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//03_nbeats_dataloader.py 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//03_nbeats_dataloader.py", line 9, in <module>
    from dataloader import DataLoader
ModuleNotFoundError: No module named 'dataloader'

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git pull --all    ;            ls &&  git add --all &&  git commit -m "ml_store"  ;            git push --all ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
Fetching origin
Already up to date.
Logs
README.md
README_actions.md
create_error_file.py
create_github_issues.py
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
