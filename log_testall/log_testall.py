
  test_all /home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json Namespace(config_file='/home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json', config_mode='test', do='test_all', folder=None, log_file=None, save_folder='ztest/') 

  ml_test --do test_all 





 ************************************************************************************************************************

 ******** TAG ::  {'github_repo_url': 'https://github.com/arita37/mlmodels/tree/3aee4395159545a95b0d7c8ed6830ec48eff1164', 'url_branch_file': 'https://github.com/arita37/mlmodels/blob/dev/', 'repo': 'arita37/mlmodels', 'branch': 'dev', 'sha': '3aee4395159545a95b0d7c8ed6830ec48eff1164', 'workflow': 'test_all'}

 ******** GITHUB_WOKFLOW : https://github.com/arita37/mlmodels/actions?query=workflow%3Atest_all

 ******** GITHUB_REPO_BRANCH : https://github.com/arita37/mlmodels/tree/dev/

 ******** GITHUB_REPO_URL : https://github.com/arita37/mlmodels/tree/3aee4395159545a95b0d7c8ed6830ec48eff1164

 ******** GITHUB_COMMIT_URL : https://github.com/arita37/mlmodels/commit/3aee4395159545a95b0d7c8ed6830ec48eff1164

 ******** Click here for Online DEBUGGER : https://gitpod.io/#https://github.com/arita37/mlmodels/tree/3aee4395159545a95b0d7c8ed6830ec48eff1164

 ************************************************************************************************************************

  ############Check model ################################ 

  ['model_keras.keras_gan', 'model_keras.nbeats', 'model_keras.01_deepctr', 'model_keras.textvae', 'model_keras.namentity_crm_bilstm_dataloader', 'model_keras.Autokeras', 'model_keras.charcnn_zhang', 'model_keras.charcnn', 'model_keras.namentity_crm_bilstm', 'model_keras.textcnn', 'model_keras.armdn', 'model_keras.02_cnn', 'model_tf.1_lstm', 'model_tf.temporal_fusion_google', 'model_gluon.gluon_automl', 'model_gluon.fb_prophet', 'model_gluon.gluonts_model', 'model_sklearn.model_sklearn', 'model_sklearn.model_lightgbm', 'model_tch.nbeats', 'model_tch.transformer_classifier', 'model_tch.matchzoo_models', 'model_tch.torchhub', 'model_tch.03_nbeats_dataloader', 'model_tch.transformer_sentence', 'model_tch.pytorch_vae', 'model_tch.pplm', 'model_tch.textcnn', 'model_tch.mlp'] 

  Used ['model_keras.keras_gan', 'model_keras.nbeats', 'model_keras.01_deepctr', 'model_keras.textvae', 'model_keras.namentity_crm_bilstm_dataloader', 'model_keras.Autokeras', 'model_keras.charcnn_zhang', 'model_keras.charcnn', 'model_keras.namentity_crm_bilstm', 'model_keras.textcnn', 'model_keras.armdn', 'model_keras.02_cnn', 'model_tf.1_lstm', 'model_tf.temporal_fusion_google', 'model_gluon.gluon_automl', 'model_gluon.fb_prophet', 'model_gluon.gluonts_model', 'model_sklearn.model_sklearn', 'model_sklearn.model_lightgbm', 'model_tch.nbeats', 'model_tch.transformer_classifier', 'model_tch.matchzoo_models', 'model_tch.torchhub', 'model_tch.03_nbeats_dataloader', 'model_tch.transformer_sentence', 'model_tch.pytorch_vae', 'model_tch.pplm', 'model_tch.textcnn', 'model_tch.mlp'] 





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
From github.com:arita37/mlmodels_store
   9e3c504..472c30c  master     -> origin/master
Updating 9e3c504..472c30c
Fast-forward
 ...-11_3aee4395159545a95b0d7c8ed6830ec48eff1164.py | 626 +++++++++++++++++++++
 1 file changed, 626 insertions(+)
 create mode 100644 log_pullrequest/log_pr_2020-05-23-08-11_3aee4395159545a95b0d7c8ed6830ec48eff1164.py
[master ae3f979] ml_store
 2 files changed, 69 insertions(+), 10987 deletions(-)
 rewrite log_testall/log_testall.py (99%)
To github.com:arita37/mlmodels_store.git
   472c30c..ae3f979  master -> master





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
Warning: Permanently added the RSA host key for IP address '140.82.112.3' to the list of known hosts.
Already up to date.
[master 19f73cb] ml_store
 1 file changed, 50 insertions(+)
To github.com:arita37/mlmodels_store.git
   ae3f979..19f73cb  master -> master





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
sequence_sum (InputLayer)       [(None, 9)]          0                                            
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
weighted_sequence_layer_1 (Weig (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         1           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         9           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         2           sequence_max[0][0]               
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           sparse_feature_1[0][0]           
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
sparse_seq_emb_sequence_sum (Em (None, 9, 4)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 5, 4)         36          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 3, 4)         8           sequence_max[0][0]               
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
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         20          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         4           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer (Sequenc (None, 1, 4)         0           weighted_sequence_layer[0][0]    2020-05-23 08:14:59.452785: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2020-05-23 08:14:59.466990: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2294680000 Hz
2020-05-23 08:14:59.467268: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x56534f7df080 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-23 08:14:59.467289: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version

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
Total params: 188
Trainable params: 188
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 2s - loss: 0.2875 - binary_crossentropy: 1.6828500/500 [==============================] - 1s 2ms/sample - loss: 0.2696 - binary_crossentropy: 1.3800 - val_loss: 0.2810 - val_binary_crossentropy: 1.5635

  #### metrics   #################################################### 
{'MSE': 0.2752048908831304}

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
sequence_sum (InputLayer)       [(None, 9)]          0                                            
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
weighted_sequence_layer_1 (Weig (None, 3, 1)         0           linear0sparse_seq_emb_weighted_se
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         1           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         9           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         2           sequence_max[0][0]               
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           sparse_feature_1[0][0]           
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
sparse_seq_emb_sequence_sum (Em (None, 9, 4)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 5, 4)         36          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 3, 4)         8           sequence_max[0][0]               
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
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         20          sparse_feature_1[0][0]           
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
Total params: 188
Trainable params: 188
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
sequence_sum (InputLayer)       [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 4)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_3 (Weig (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 6, 4)         12          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 2, 4)         20          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 4, 4)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         20          sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 6, 1)         3           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         5           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 4, 1)         2           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_5 (NoMask)              (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_12[0][0]  
                                                                 sequence_pooling_layer_13[0][0]  
                                                                 sequence_pooling_layer_14[0][0]  
                                                                 sequence_pooling_layer_15[0][0]  
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           sparse_feature_0[0][0]           
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
Total params: 423
Trainable params: 423
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 1s - loss: 0.2494 - binary_crossentropy: 0.9450500/500 [==============================] - 1s 2ms/sample - loss: 0.2574 - binary_crossentropy: 0.9917 - val_loss: 0.2539 - val_binary_crossentropy: 0.9319

  #### metrics   #################################################### 
{'MSE': 0.2554947479005859}

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
sequence_sum (InputLayer)       [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 4)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_3 (Weig (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 6, 4)         12          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 2, 4)         20          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 4, 4)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         20          sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 6, 1)         3           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         5           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 4, 1)         2           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_5 (NoMask)              (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_12[0][0]  
                                                                 sequence_pooling_layer_13[0][0]  
                                                                 sequence_pooling_layer_14[0][0]  
                                                                 sequence_pooling_layer_15[0][0]  
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           sparse_feature_0[0][0]           
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
Total params: 423
Trainable params: 423
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
sequence_mean (InputLayer)      [(None, 9)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 9, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 9, 4)         12          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 5, 4)         4           sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         8           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         16          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         20          sparse_feature_2[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 9, 1)         7           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         3           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         1           sequence_max[0][0]               
__________________________________________________________________________________________________
conv2d_1 (Conv2D)               (None, 3, 4, 1)      5           k_max_pooling[0][0]              
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         2           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         4           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           sparse_feature_2[0][0]           
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
Total params: 582
Trainable params: 582
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 2s - loss: 0.4500 - binary_crossentropy: 6.9412500/500 [==============================] - 1s 3ms/sample - loss: 0.4880 - binary_crossentropy: 7.5274 - val_loss: 0.5060 - val_binary_crossentropy: 7.8050

  #### metrics   #################################################### 
{'MSE': 0.497}

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
sequence_mean (InputLayer)      [(None, 9)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 9, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 9, 4)         12          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 5, 4)         4           sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         8           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         16          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         20          sparse_feature_2[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 9, 1)         7           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         3           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         1           sequence_max[0][0]               
__________________________________________________________________________________________________
conv2d_1 (Conv2D)               (None, 3, 4, 1)      5           k_max_pooling[0][0]              
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         2           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         4           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           sparse_feature_2[0][0]           
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
Total params: 582
Trainable params: 582
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
sequence_sum (InputLayer)       [(None, 8)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 4)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 9)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 8, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 4, 4)         24          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 9, 4)         4           sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         12          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         4           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         32          sparse_feature_2[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 8, 1)         7           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 4, 1)         6           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         1           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_4 (Flatten)             (None, 28)           0           concatenate_9[0][0]              
__________________________________________________________________________________________________
flatten_5 (Flatten)             (None, 3)            0           concatenate_10[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         1           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_2[0][0]           
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
Total params: 408
Trainable params: 408
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 2s - loss: 0.4400 - binary_crossentropy: 6.7782500/500 [==============================] - 1s 3ms/sample - loss: 0.5160 - binary_crossentropy: 7.9537 - val_loss: 0.5220 - val_binary_crossentropy: 8.0518

  #### metrics   #################################################### 
{'MSE': 0.517}

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
sequence_sum (InputLayer)       [(None, 8)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 4)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 9)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 8, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 4, 4)         24          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 9, 4)         4           sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         12          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         4           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         32          sparse_feature_2[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 8, 1)         7           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 4, 1)         6           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         1           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_4 (Flatten)             (None, 28)           0           concatenate_9[0][0]              
__________________________________________________________________________________________________
flatten_5 (Flatten)             (None, 3)            0           concatenate_10[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         1           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_2[0][0]           
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
Total params: 408
Trainable params: 408
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
sequence_sum (InputLayer)       [(None, 4)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 7)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 5)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_12 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 4, 4)         36          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 7, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 5, 4)         8           sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 4, 1)         9           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 7, 1)         7           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         2           sequence_max[0][0]               
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
100/500 [=====>........................] - ETA: 3s - loss: 0.2537 - binary_crossentropy: 0.8291500/500 [==============================] - 2s 4ms/sample - loss: 0.2545 - binary_crossentropy: 0.8314 - val_loss: 0.2531 - val_binary_crossentropy: 0.8282

  #### metrics   #################################################### 
{'MSE': 0.25360249396081286}

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
sequence_sum (InputLayer)       [(None, 4)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 7)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 5)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_12 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 4, 4)         36          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 7, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 5, 4)         8           sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 4, 1)         9           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 7, 1)         7           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         2           sequence_max[0][0]               
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
dnn_4 (DNN)                     (None, 4)            152         concatenate_20[0][0]             2020-05-23 08:16:31.194984: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-23 08:16:31.197362: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-23 08:16:31.204168: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-23 08:16:31.216051: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-23 08:16:31.217961: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-23 08:16:31.219949: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-23 08:16:31.221691: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

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
1/1 [==============================] - 3s 3s/sample - loss: 0.2500 - binary_crossentropy: 0.6931 - val_loss: 0.2502 - val_binary_crossentropy: 0.6936
2020-05-23 08:16:32.664657: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-23 08:16:32.666796: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-23 08:16:32.671645: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-23 08:16:32.682225: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-23 08:16:32.683926: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-23 08:16:32.685555: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-23 08:16:32.687061: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

  #### metrics   #################################################### 
{'MSE': 0.2501981822893586}

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
2020-05-23 08:16:59.067853: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-23 08:16:59.069466: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-23 08:16:59.074096: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-23 08:16:59.081280: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-23 08:16:59.082742: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-23 08:16:59.083862: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-23 08:16:59.084842: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
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
1/1 [==============================] - 3s 3s/sample - loss: 0.2500 - binary_crossentropy: 0.6931 - val_loss: 0.2519 - val_binary_crossentropy: 0.6969
2020-05-23 08:17:00.788316: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-23 08:17:00.789533: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-23 08:17:00.792879: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-23 08:17:00.798884: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-23 08:17:00.800039: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-23 08:17:00.801100: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-23 08:17:00.802144: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

  #### metrics   #################################################### 
{'MSE': 0.25235120925439897}

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
concatenate_27 (Concatenate)    (None, 1, 16)        0           no_mask_36[0][0]                 2020-05-23 08:17:39.022420: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-23 08:17:39.028044: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-23 08:17:39.045455: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-23 08:17:39.075305: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-23 08:17:39.080309: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-23 08:17:39.084820: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-23 08:17:39.089468: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

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
1/1 [==============================] - 6s 6s/sample - loss: 0.0497 - binary_crossentropy: 0.2521 - val_loss: 0.3173 - val_binary_crossentropy: 0.8500
2020-05-23 08:17:41.589456: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-23 08:17:41.594723: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-23 08:17:41.608370: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-23 08:17:41.635723: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-23 08:17:41.640527: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-23 08:17:41.644916: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-23 08:17:41.649179: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

  #### metrics   #################################################### 
{'MSE': 0.23083157395178588}

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
sequence_sum (InputLayer)       [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 7)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 6, 4)         36          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 6, 4)         32          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 7, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         12          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         28          sparse_feature_1[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 6, 1)         9           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         8           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 7, 1)         7           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_48 (NoMask)             (None, 120)          0           flatten_19[0][0]                 
__________________________________________________________________________________________________
concatenate_39 (Concatenate)    (None, 2)            0           no_mask_49[0][0]                 
                                                                 no_mask_49[1][0]                 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_1[0][0]           
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
Total params: 735
Trainable params: 735
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 7s - loss: 0.3260 - binary_crossentropy: 0.9019500/500 [==============================] - 5s 9ms/sample - loss: 0.3196 - binary_crossentropy: 0.8742 - val_loss: 0.3222 - val_binary_crossentropy: 0.8839

  #### metrics   #################################################### 
{'MSE': 0.3193555874446756}

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
sequence_sum (InputLayer)       [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 7)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 6, 4)         36          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 6, 4)         32          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 7, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         12          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         28          sparse_feature_1[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 6, 1)         9           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         8           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 7, 1)         7           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_48 (NoMask)             (None, 120)          0           flatten_19[0][0]                 
__________________________________________________________________________________________________
concatenate_39 (Concatenate)    (None, 2)            0           no_mask_49[0][0]                 
                                                                 no_mask_49[1][0]                 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_1[0][0]           
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
Total params: 735
Trainable params: 735
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
sequence_sum (InputLayer)       [(None, 7)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 3)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 7, 2)         14          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 6, 2)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 3, 2)         8           sequence_max[0][0]               
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
sparse_emb_sparse_feature_0 (Em (None, 1, 2)         8           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_3 (Em (None, 1, 2)         18          sparse_feature_3[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 2)         4           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_4 (Em (None, 1, 2)         12          sparse_feature_4[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 2)         14          sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_5 (Em (None, 1, 2)         18          sparse_feature_5[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 7, 1)         7           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         2           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         4           sequence_max[0][0]               
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
linear0sparse_emb_sparse_featur (None, 1, 1)         4           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         9           sparse_feature_3[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         2           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           sparse_feature_4[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         9           sparse_feature_5[0][0]           
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
Total params: 263
Trainable params: 263
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 7s - loss: 0.2633 - binary_crossentropy: 0.7233500/500 [==============================] - 5s 10ms/sample - loss: 0.2783 - binary_crossentropy: 0.8335 - val_loss: 0.2662 - val_binary_crossentropy: 0.9087

  #### metrics   #################################################### 
{'MSE': 0.2680960074793378}

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
sequence_sum (InputLayer)       [(None, 7)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 3)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 7, 2)         14          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 6, 2)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 3, 2)         8           sequence_max[0][0]               
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
sparse_emb_sparse_feature_0 (Em (None, 1, 2)         8           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_3 (Em (None, 1, 2)         18          sparse_feature_3[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 2)         4           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_4 (Em (None, 1, 2)         12          sparse_feature_4[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 2)         14          sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_5 (Em (None, 1, 2)         18          sparse_feature_5[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 7, 1)         7           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         2           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         4           sequence_max[0][0]               
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
linear0sparse_emb_sparse_featur (None, 1, 1)         4           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         9           sparse_feature_3[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         2           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           sparse_feature_4[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         9           sparse_feature_5[0][0]           
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
Total params: 263
Trainable params: 263
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
sequence_sum (InputLayer)       [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 6)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_21 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 9, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 2, 4)         24          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 6, 4)         20          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         12          sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 9, 1)         7           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         6           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         5           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_24 (Flatten)            (None, 20)           0           concatenate_55[0][0]             
__________________________________________________________________________________________________
flatten_25 (Flatten)            (None, 1)            0           no_mask_69[0][0]                 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_0[0][0]           
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
Total params: 1,909
Trainable params: 1,909
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 6s - loss: 0.2637 - binary_crossentropy: 0.7281500/500 [==============================] - 5s 10ms/sample - loss: 0.2686 - binary_crossentropy: 0.7383 - val_loss: 0.2698 - val_binary_crossentropy: 0.7378

  #### metrics   #################################################### 
{'MSE': 0.26642675836638763}

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
sequence_sum (InputLayer)       [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 6)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_21 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 9, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 2, 4)         24          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 6, 4)         20          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         12          sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 9, 1)         7           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         6           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         5           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_24 (Flatten)            (None, 20)           0           concatenate_55[0][0]             
__________________________________________________________________________________________________
flatten_25 (Flatten)            (None, 1)            0           no_mask_69[0][0]                 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_0[0][0]           
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
Total params: 1,909
Trainable params: 1,909
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
regionsequence_sum (InputLayer) [(None, 4)]          0                                            
__________________________________________________________________________________________________
regionsequence_mean (InputLayer [(None, 2)]          0                                            
__________________________________________________________________________________________________
regionsequence_max (InputLayer) [(None, 4)]          0                                            
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
region_10sparse_seq_emb_regions (None, 4, 1)         4           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 2, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 4, 1)         8           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_26 (Wei (None, 3, 1)         0           region_20sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 4, 1)         4           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 2, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 4, 1)         8           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_28 (Wei (None, 3, 1)         0           region_30sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 4, 1)         4           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 2, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 4, 1)         8           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_30 (Wei (None, 3, 1)         0           region_40sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 4, 1)         4           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 2, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 4, 1)         8           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_32 (Wei (None, 3, 1)         0           learner_10sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 4, 1)         4           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 2, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 4, 1)         8           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_34 (Wei (None, 3, 1)         0           learner_20sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 4, 1)         4           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 2, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 4, 1)         8           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_36 (Wei (None, 3, 1)         0           learner_30sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 4, 1)         4           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 2, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 4, 1)         8           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_38 (Wei (None, 3, 1)         0           learner_40sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 4, 1)         4           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 2, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 4, 1)         8           regionsequence_max[0][0]         
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
Total params: 184
Trainable params: 184
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 9s - loss: 0.2532 - binary_crossentropy: 0.6994500/500 [==============================] - 6s 13ms/sample - loss: 0.2541 - binary_crossentropy: 0.7012 - val_loss: 0.2548 - val_binary_crossentropy: 0.7026

  #### metrics   #################################################### 
{'MSE': 0.2540920327284141}

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
regionsequence_sum (InputLayer) [(None, 4)]          0                                            
__________________________________________________________________________________________________
regionsequence_mean (InputLayer [(None, 2)]          0                                            
__________________________________________________________________________________________________
regionsequence_max (InputLayer) [(None, 4)]          0                                            
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
region_10sparse_seq_emb_regions (None, 4, 1)         4           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 2, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 4, 1)         8           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_26 (Wei (None, 3, 1)         0           region_20sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 4, 1)         4           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 2, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 4, 1)         8           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_28 (Wei (None, 3, 1)         0           region_30sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 4, 1)         4           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 2, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 4, 1)         8           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_30 (Wei (None, 3, 1)         0           region_40sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 4, 1)         4           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 2, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 4, 1)         8           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_32 (Wei (None, 3, 1)         0           learner_10sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 4, 1)         4           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 2, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 4, 1)         8           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_34 (Wei (None, 3, 1)         0           learner_20sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 4, 1)         4           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 2, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 4, 1)         8           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_36 (Wei (None, 3, 1)         0           learner_30sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 4, 1)         4           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 2, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 4, 1)         8           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_38 (Wei (None, 3, 1)         0           learner_40sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 4, 1)         4           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 2, 1)         7           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 4, 1)         8           regionsequence_max[0][0]         
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
Total params: 184
Trainable params: 184
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
sequence_sum (InputLayer)       [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 8)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_40 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 6, 4)         24          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 8, 4)         20          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 1, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         36          sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 6, 1)         6           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 8, 1)         5           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_101 (NoMask)            (None, 1, 4)         0           bi_interaction_pooling[0][0]     
__________________________________________________________________________________________________
no_mask_102 (NoMask)            (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         9           sparse_feature_0[0][0]           
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
Total params: 1,432
Trainable params: 1,432
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 8s - loss: 0.2736 - binary_crossentropy: 1.1258500/500 [==============================] - 6s 12ms/sample - loss: 0.2850 - binary_crossentropy: 1.4700 - val_loss: 0.3015 - val_binary_crossentropy: 1.7404

  #### metrics   #################################################### 
{'MSE': 0.2910322061462283}

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
sequence_sum (InputLayer)       [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 8)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 1)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_40 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 6, 4)         24          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 8, 4)         20          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 1, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         36          sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 6, 1)         6           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 8, 1)         5           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_101 (NoMask)            (None, 1, 4)         0           bi_interaction_pooling[0][0]     
__________________________________________________________________________________________________
no_mask_102 (NoMask)            (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         9           sparse_feature_0[0][0]           
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
Total params: 1,432
Trainable params: 1,432
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
sequence_sum (InputLayer)       [(None, 5)]          0                                            
__________________________________________________________________________________________________
hash_17 (Hash)                  (None, 1)            0           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 3)]          0                                            
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
sparse_emb_sparse_feature_0_spa (None, 1, 4)         4           hash_14[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_spa (None, 1, 4)         28          hash_15[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         4           hash_16[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 5, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         4           hash_17[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 3, 4)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         4           hash_18[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 5, 4)         36          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         28          hash_19[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 5, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         28          hash_20[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 3, 4)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         28          hash_21[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 5, 4)         36          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 5, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 3, 4)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 5, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_max_sequenc (None, 5, 4)         36          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 3, 4)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sequence_max_sequenc (None, 5, 4)         36          sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 5, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         1           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         9           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_29 (Flatten)            (None, 40)           0           no_mask_116[0][0]                
__________________________________________________________________________________________________
flatten_30 (Flatten)            (None, 2)            0           concatenate_81[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         1           hash_10[0][0]                    
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           hash_11[0][0]                    
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
100/500 [=====>........................] - ETA: 9s - loss: 0.2396 - binary_crossentropy: 0.6723500/500 [==============================] - 7s 14ms/sample - loss: 0.2544 - binary_crossentropy: 0.7031 - val_loss: 0.2545 - val_binary_crossentropy: 0.7024

  #### metrics   #################################################### 
{'MSE': 0.25285078556795204}

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
sequence_sum (InputLayer)       [(None, 5)]          0                                            
__________________________________________________________________________________________________
hash_17 (Hash)                  (None, 1)            0           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 3)]          0                                            
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
sparse_emb_sparse_feature_0_spa (None, 1, 4)         4           hash_14[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_spa (None, 1, 4)         28          hash_15[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         4           hash_16[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 5, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         4           hash_17[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 3, 4)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         4           hash_18[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 5, 4)         36          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         28          hash_19[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 5, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         28          hash_20[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 3, 4)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         28          hash_21[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 5, 4)         36          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 5, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 3, 4)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 5, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_max_sequenc (None, 5, 4)         36          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 3, 4)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sequence_max_sequenc (None, 5, 4)         36          sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 5, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         1           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         9           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_29 (Flatten)            (None, 40)           0           no_mask_116[0][0]                
__________________________________________________________________________________________________
flatten_30 (Flatten)            (None, 2)            0           concatenate_81[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         1           hash_10[0][0]                    
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           hash_11[0][0]                    
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
   19f73cb..33986f9  master     -> origin/master
Updating 19f73cb..33986f9
Fast-forward
 .../20200523/list_log_pullrequest_20200523.md      |   2 +-
 error_list/20200523/list_log_testall_20200523.md   | 783 +--------------------
 2 files changed, 2 insertions(+), 783 deletions(-)
[master 112b605] ml_store
 1 file changed, 4953 insertions(+)
Warning: Permanently added the RSA host key for IP address '140.82.113.4' to the list of known hosts.
To github.com:arita37/mlmodels_store.git
   33986f9..112b605  master -> master





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
[master 4806c7c] ml_store
 1 file changed, 52 insertions(+)
To github.com:arita37/mlmodels_store.git
   112b605..4806c7c  master -> master





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
[master 53d85a0] ml_store
 1 file changed, 47 insertions(+)
Warning: Permanently added the RSA host key for IP address '140.82.114.3' to the list of known hosts.
To github.com:arita37/mlmodels_store.git
   4806c7c..53d85a0  master -> master





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
[master 0dd85f4] ml_store
 1 file changed, 37 insertions(+)
To github.com:arita37/mlmodels_store.git
   53d85a0..0dd85f4  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//charcnn_zhang.py 
/home/runner/work/mlmodels/mlmodels/mlmodels/dataset

  #### Loading params   ############################################## 

  #### Loading daaset   ############################################# 
Using TensorFlow backend.
Loading data...
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//charcnn_zhang.py", line 284, in <module>
    test(pars_choice="json", data_path= f"{root_path}/model_keras/charcnn_zhang.json")
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//charcnn_zhang.py", line 248, in test
    Xtuple = get_dataset(data_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//charcnn_zhang.py", line 139, in get_dataset
    train_data.load_data()
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/raw/char_cnn/data_utils.py", line 41, in load_data
    with open(self.data_source, 'r', encoding='utf-8') as f:
FileNotFoundError: [Errno 2] No such file or directory: '/home/runner/work/mlmodels/mlmodels/mlmodels/dataset/text/ag_news_csv/train.csv'

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
[master 3f9ec33] ml_store
 1 file changed, 49 insertions(+)
To github.com:arita37/mlmodels_store.git
   0dd85f4..3f9ec33  master -> master





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
[master 7fb3b61] ml_store
 1 file changed, 48 insertions(+)
To github.com:arita37/mlmodels_store.git
   3f9ec33..7fb3b61  master -> master





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
Already up to date.
[master a10115c] ml_store
 1 file changed, 45 insertions(+)
To github.com:arita37/mlmodels_store.git
   7fb3b61..a10115c  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//textcnn.py 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Loading dataset   ############################################# 
Loading data...
Downloading data from https://s3.amazonaws.com/text-datasets/imdb.npz

    8192/17464789 [..............................] - ETA: 0s
 3284992/17464789 [====>.........................] - ETA: 0s
11313152/17464789 [==================>...........] - ETA: 0s
16384000/17464789 [===========================>..] - ETA: 0s
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
2020-05-23 08:28:12.350509: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2020-05-23 08:28:12.355501: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2294680000 Hz
2020-05-23 08:28:12.355659: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x556bb4406ea0 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-23 08:28:12.355676: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
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

 1000/25000 [>.............................] - ETA: 14s - loss: 7.5746 - accuracy: 0.5060
 2000/25000 [=>............................] - ETA: 10s - loss: 7.5516 - accuracy: 0.5075
 3000/25000 [==>...........................] - ETA: 9s - loss: 7.6513 - accuracy: 0.5010 
 4000/25000 [===>..........................] - ETA: 8s - loss: 7.5133 - accuracy: 0.5100
 5000/25000 [=====>........................] - ETA: 7s - loss: 7.5593 - accuracy: 0.5070
 6000/25000 [======>.......................] - ETA: 6s - loss: 7.5542 - accuracy: 0.5073
 7000/25000 [=======>......................] - ETA: 6s - loss: 7.5681 - accuracy: 0.5064
 8000/25000 [========>.....................] - ETA: 6s - loss: 7.5861 - accuracy: 0.5052
 9000/25000 [=========>....................] - ETA: 5s - loss: 7.6411 - accuracy: 0.5017
10000/25000 [===========>..................] - ETA: 5s - loss: 7.6605 - accuracy: 0.5004
11000/25000 [============>.................] - ETA: 4s - loss: 7.6722 - accuracy: 0.4996
12000/25000 [=============>................] - ETA: 4s - loss: 7.6730 - accuracy: 0.4996
13000/25000 [==============>...............] - ETA: 4s - loss: 7.6879 - accuracy: 0.4986
14000/25000 [===============>..............] - ETA: 3s - loss: 7.6611 - accuracy: 0.5004
15000/25000 [=================>............] - ETA: 3s - loss: 7.6656 - accuracy: 0.5001
16000/25000 [==================>...........] - ETA: 3s - loss: 7.6810 - accuracy: 0.4991
17000/25000 [===================>..........] - ETA: 2s - loss: 7.6657 - accuracy: 0.5001
18000/25000 [====================>.........] - ETA: 2s - loss: 7.7015 - accuracy: 0.4977
19000/25000 [=====================>........] - ETA: 2s - loss: 7.6965 - accuracy: 0.4981
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6881 - accuracy: 0.4986
21000/25000 [========================>.....] - ETA: 1s - loss: 7.6922 - accuracy: 0.4983
22000/25000 [=========================>....] - ETA: 0s - loss: 7.6910 - accuracy: 0.4984
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6873 - accuracy: 0.4987
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6813 - accuracy: 0.4990
25000/25000 [==============================] - 10s 402us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000

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
(<mlmodels.util.Model_empty object at 0x7f4a003e0860>, None)

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

  <mlmodels.model_keras.textcnn.Model object at 0x7f49eef5f2b0> 

  #### Fit   ######################################################## 
Loading data...
Pad sequences (samples x time)...
Train on 25000 samples, validate on 25000 samples
Epoch 1/1

 1000/25000 [>.............................] - ETA: 13s - loss: 8.1726 - accuracy: 0.4670
 2000/25000 [=>............................] - ETA: 10s - loss: 8.0423 - accuracy: 0.4755
 3000/25000 [==>...........................] - ETA: 8s - loss: 7.9171 - accuracy: 0.4837 
 4000/25000 [===>..........................] - ETA: 7s - loss: 7.7931 - accuracy: 0.4918
 5000/25000 [=====>........................] - ETA: 7s - loss: 7.7832 - accuracy: 0.4924
 6000/25000 [======>.......................] - ETA: 6s - loss: 7.6998 - accuracy: 0.4978
 7000/25000 [=======>......................] - ETA: 6s - loss: 7.6601 - accuracy: 0.5004
 8000/25000 [========>.....................] - ETA: 5s - loss: 7.6072 - accuracy: 0.5039
 9000/25000 [=========>....................] - ETA: 5s - loss: 7.6138 - accuracy: 0.5034
10000/25000 [===========>..................] - ETA: 5s - loss: 7.6022 - accuracy: 0.5042
11000/25000 [============>.................] - ETA: 4s - loss: 7.5914 - accuracy: 0.5049
12000/25000 [=============>................] - ETA: 4s - loss: 7.6257 - accuracy: 0.5027
13000/25000 [==============>...............] - ETA: 4s - loss: 7.6619 - accuracy: 0.5003
14000/25000 [===============>..............] - ETA: 3s - loss: 7.6590 - accuracy: 0.5005
15000/25000 [=================>............] - ETA: 3s - loss: 7.6656 - accuracy: 0.5001
16000/25000 [==================>...........] - ETA: 2s - loss: 7.6800 - accuracy: 0.4991
17000/25000 [===================>..........] - ETA: 2s - loss: 7.6747 - accuracy: 0.4995
18000/25000 [====================>.........] - ETA: 2s - loss: 7.6641 - accuracy: 0.5002
19000/25000 [=====================>........] - ETA: 1s - loss: 7.6715 - accuracy: 0.4997
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6689 - accuracy: 0.4999
21000/25000 [========================>.....] - ETA: 1s - loss: 7.6776 - accuracy: 0.4993
22000/25000 [=========================>....] - ETA: 0s - loss: 7.6785 - accuracy: 0.4992
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6660 - accuracy: 0.5000
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6666 - accuracy: 0.5000
25000/25000 [==============================] - 10s 397us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000

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

 1000/25000 [>.............................] - ETA: 14s - loss: 7.9120 - accuracy: 0.4840
 2000/25000 [=>............................] - ETA: 10s - loss: 8.0576 - accuracy: 0.4745
 3000/25000 [==>...........................] - ETA: 9s - loss: 7.9580 - accuracy: 0.4810 
 4000/25000 [===>..........................] - ETA: 8s - loss: 7.9081 - accuracy: 0.4843
 5000/25000 [=====>........................] - ETA: 7s - loss: 7.8660 - accuracy: 0.4870
 6000/25000 [======>.......................] - ETA: 6s - loss: 7.8148 - accuracy: 0.4903
 7000/25000 [=======>......................] - ETA: 6s - loss: 7.7981 - accuracy: 0.4914
 8000/25000 [========>.....................] - ETA: 6s - loss: 7.8161 - accuracy: 0.4902
 9000/25000 [=========>....................] - ETA: 5s - loss: 7.7825 - accuracy: 0.4924
10000/25000 [===========>..................] - ETA: 5s - loss: 7.7694 - accuracy: 0.4933
11000/25000 [============>.................] - ETA: 4s - loss: 7.7363 - accuracy: 0.4955
12000/25000 [=============>................] - ETA: 4s - loss: 7.7420 - accuracy: 0.4951
13000/25000 [==============>...............] - ETA: 4s - loss: 7.7162 - accuracy: 0.4968
14000/25000 [===============>..............] - ETA: 3s - loss: 7.6885 - accuracy: 0.4986
15000/25000 [=================>............] - ETA: 3s - loss: 7.6871 - accuracy: 0.4987
16000/25000 [==================>...........] - ETA: 3s - loss: 7.6906 - accuracy: 0.4984
17000/25000 [===================>..........] - ETA: 2s - loss: 7.6684 - accuracy: 0.4999
18000/25000 [====================>.........] - ETA: 2s - loss: 7.6709 - accuracy: 0.4997
19000/25000 [=====================>........] - ETA: 2s - loss: 7.6739 - accuracy: 0.4995
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6605 - accuracy: 0.5004
21000/25000 [========================>.....] - ETA: 1s - loss: 7.6659 - accuracy: 0.5000
22000/25000 [=========================>....] - ETA: 0s - loss: 7.6569 - accuracy: 0.5006
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6560 - accuracy: 0.5007
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6737 - accuracy: 0.4995
25000/25000 [==============================] - 10s 405us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000
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
Warning: Permanently added the RSA host key for IP address '140.82.113.3' to the list of known hosts.
From github.com:arita37/mlmodels_store
   a10115c..f78f99d  master     -> origin/master
Updating a10115c..f78f99d
Fast-forward
 error_list/20200523/list_log_testall_20200523.md | 99 ++++++++++++++++++++++++
 1 file changed, 99 insertions(+)
[master 3b9705c] ml_store
 1 file changed, 324 insertions(+)
To github.com:arita37/mlmodels_store.git
   f78f99d..3b9705c  master -> master





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

13/13 [==============================] - 2s 135ms/step - loss: nan
Epoch 2/10

13/13 [==============================] - 0s 5ms/step - loss: nan
Epoch 3/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 4/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 5/10

13/13 [==============================] - 0s 5ms/step - loss: nan
Epoch 6/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 7/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 8/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 9/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 10/10

13/13 [==============================] - 0s 5ms/step - loss: nan

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
[master 0b14cdb] ml_store
 1 file changed, 126 insertions(+)
Warning: Permanently added the RSA host key for IP address '140.82.112.4' to the list of known hosts.
To github.com:arita37/mlmodels_store.git
   3b9705c..0b14cdb  master -> master





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
 4440064/11490434 [==========>...................] - ETA: 0s
11100160/11490434 [===========================>..] - ETA: 0s
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

   32/60000 [..............................] - ETA: 8:18 - loss: 2.2951 - categorical_accuracy: 0.0625
   64/60000 [..............................] - ETA: 5:17 - loss: 2.2846 - categorical_accuracy: 0.1250
   96/60000 [..............................] - ETA: 4:14 - loss: 2.2760 - categorical_accuracy: 0.1354
  128/60000 [..............................] - ETA: 3:40 - loss: 2.2614 - categorical_accuracy: 0.1484
  160/60000 [..............................] - ETA: 3:19 - loss: 2.2383 - categorical_accuracy: 0.1813
  192/60000 [..............................] - ETA: 3:04 - loss: 2.2096 - categorical_accuracy: 0.1927
  224/60000 [..............................] - ETA: 2:54 - loss: 2.1762 - categorical_accuracy: 0.2232
  256/60000 [..............................] - ETA: 2:46 - loss: 2.1603 - categorical_accuracy: 0.2227
  288/60000 [..............................] - ETA: 2:40 - loss: 2.1222 - categorical_accuracy: 0.2674
  320/60000 [..............................] - ETA: 2:35 - loss: 2.1392 - categorical_accuracy: 0.2562
  352/60000 [..............................] - ETA: 2:31 - loss: 2.1102 - categorical_accuracy: 0.2756
  384/60000 [..............................] - ETA: 2:28 - loss: 2.0750 - categorical_accuracy: 0.2969
  416/60000 [..............................] - ETA: 2:26 - loss: 2.0402 - categorical_accuracy: 0.3077
  448/60000 [..............................] - ETA: 2:24 - loss: 2.0185 - categorical_accuracy: 0.3125
  480/60000 [..............................] - ETA: 2:22 - loss: 1.9725 - categorical_accuracy: 0.3292
  512/60000 [..............................] - ETA: 2:20 - loss: 1.9267 - categorical_accuracy: 0.3477
  544/60000 [..............................] - ETA: 2:18 - loss: 1.8843 - categorical_accuracy: 0.3640
  576/60000 [..............................] - ETA: 2:17 - loss: 1.8297 - categorical_accuracy: 0.3872
  608/60000 [..............................] - ETA: 2:15 - loss: 1.7955 - categorical_accuracy: 0.3931
  640/60000 [..............................] - ETA: 2:14 - loss: 1.7637 - categorical_accuracy: 0.4062
  672/60000 [..............................] - ETA: 2:13 - loss: 1.7427 - categorical_accuracy: 0.4122
  704/60000 [..............................] - ETA: 2:12 - loss: 1.7004 - categorical_accuracy: 0.4276
  736/60000 [..............................] - ETA: 2:11 - loss: 1.6838 - categorical_accuracy: 0.4348
  768/60000 [..............................] - ETA: 2:10 - loss: 1.6550 - categorical_accuracy: 0.4466
  800/60000 [..............................] - ETA: 2:09 - loss: 1.6349 - categorical_accuracy: 0.4575
  832/60000 [..............................] - ETA: 2:08 - loss: 1.6137 - categorical_accuracy: 0.4651
  864/60000 [..............................] - ETA: 2:08 - loss: 1.5747 - categorical_accuracy: 0.4792
  896/60000 [..............................] - ETA: 2:07 - loss: 1.5437 - categorical_accuracy: 0.4900
  928/60000 [..............................] - ETA: 2:06 - loss: 1.5382 - categorical_accuracy: 0.4946
  960/60000 [..............................] - ETA: 2:06 - loss: 1.5274 - categorical_accuracy: 0.4990
  992/60000 [..............................] - ETA: 2:05 - loss: 1.5136 - categorical_accuracy: 0.5050
 1024/60000 [..............................] - ETA: 2:05 - loss: 1.4892 - categorical_accuracy: 0.5146
 1056/60000 [..............................] - ETA: 2:04 - loss: 1.4638 - categorical_accuracy: 0.5246
 1088/60000 [..............................] - ETA: 2:04 - loss: 1.4488 - categorical_accuracy: 0.5294
 1120/60000 [..............................] - ETA: 2:04 - loss: 1.4309 - categorical_accuracy: 0.5375
 1152/60000 [..............................] - ETA: 2:03 - loss: 1.4104 - categorical_accuracy: 0.5460
 1184/60000 [..............................] - ETA: 2:03 - loss: 1.3996 - categorical_accuracy: 0.5524
 1216/60000 [..............................] - ETA: 2:02 - loss: 1.3805 - categorical_accuracy: 0.5584
 1248/60000 [..............................] - ETA: 2:02 - loss: 1.3638 - categorical_accuracy: 0.5625
 1280/60000 [..............................] - ETA: 2:01 - loss: 1.3480 - categorical_accuracy: 0.5680
 1312/60000 [..............................] - ETA: 2:01 - loss: 1.3296 - categorical_accuracy: 0.5747
 1344/60000 [..............................] - ETA: 2:01 - loss: 1.3105 - categorical_accuracy: 0.5811
 1376/60000 [..............................] - ETA: 2:00 - loss: 1.2926 - categorical_accuracy: 0.5858
 1408/60000 [..............................] - ETA: 2:00 - loss: 1.2758 - categorical_accuracy: 0.5909
 1440/60000 [..............................] - ETA: 2:00 - loss: 1.2633 - categorical_accuracy: 0.5924
 1472/60000 [..............................] - ETA: 1:59 - loss: 1.2491 - categorical_accuracy: 0.5978
 1504/60000 [..............................] - ETA: 1:59 - loss: 1.2372 - categorical_accuracy: 0.6024
 1536/60000 [..............................] - ETA: 1:59 - loss: 1.2254 - categorical_accuracy: 0.6061
 1568/60000 [..............................] - ETA: 1:58 - loss: 1.2103 - categorical_accuracy: 0.6110
 1600/60000 [..............................] - ETA: 1:58 - loss: 1.1942 - categorical_accuracy: 0.6175
 1632/60000 [..............................] - ETA: 1:58 - loss: 1.1785 - categorical_accuracy: 0.6225
 1664/60000 [..............................] - ETA: 1:58 - loss: 1.1653 - categorical_accuracy: 0.6256
 1696/60000 [..............................] - ETA: 1:58 - loss: 1.1537 - categorical_accuracy: 0.6303
 1728/60000 [..............................] - ETA: 1:57 - loss: 1.1394 - categorical_accuracy: 0.6354
 1760/60000 [..............................] - ETA: 1:57 - loss: 1.1310 - categorical_accuracy: 0.6392
 1792/60000 [..............................] - ETA: 1:57 - loss: 1.1165 - categorical_accuracy: 0.6440
 1824/60000 [..............................] - ETA: 1:57 - loss: 1.1043 - categorical_accuracy: 0.6469
 1856/60000 [..............................] - ETA: 1:57 - loss: 1.0956 - categorical_accuracy: 0.6498
 1888/60000 [..............................] - ETA: 1:56 - loss: 1.0949 - categorical_accuracy: 0.6510
 1920/60000 [..............................] - ETA: 1:56 - loss: 1.0891 - categorical_accuracy: 0.6526
 1952/60000 [..............................] - ETA: 1:56 - loss: 1.0769 - categorical_accuracy: 0.6562
 1984/60000 [..............................] - ETA: 1:56 - loss: 1.0665 - categorical_accuracy: 0.6598
 2016/60000 [>.............................] - ETA: 1:56 - loss: 1.0589 - categorical_accuracy: 0.6627
 2048/60000 [>.............................] - ETA: 1:56 - loss: 1.0556 - categorical_accuracy: 0.6636
 2080/60000 [>.............................] - ETA: 1:56 - loss: 1.0444 - categorical_accuracy: 0.6673
 2112/60000 [>.............................] - ETA: 1:55 - loss: 1.0390 - categorical_accuracy: 0.6695
 2144/60000 [>.............................] - ETA: 1:55 - loss: 1.0300 - categorical_accuracy: 0.6726
 2176/60000 [>.............................] - ETA: 1:55 - loss: 1.0208 - categorical_accuracy: 0.6751
 2208/60000 [>.............................] - ETA: 1:55 - loss: 1.0215 - categorical_accuracy: 0.6757
 2240/60000 [>.............................] - ETA: 1:55 - loss: 1.0137 - categorical_accuracy: 0.6781
 2272/60000 [>.............................] - ETA: 1:55 - loss: 1.0109 - categorical_accuracy: 0.6787
 2304/60000 [>.............................] - ETA: 1:54 - loss: 1.0033 - categorical_accuracy: 0.6806
 2336/60000 [>.............................] - ETA: 1:54 - loss: 0.9977 - categorical_accuracy: 0.6836
 2368/60000 [>.............................] - ETA: 1:54 - loss: 0.9918 - categorical_accuracy: 0.6854
 2400/60000 [>.............................] - ETA: 1:54 - loss: 0.9861 - categorical_accuracy: 0.6875
 2432/60000 [>.............................] - ETA: 1:54 - loss: 0.9789 - categorical_accuracy: 0.6904
 2464/60000 [>.............................] - ETA: 1:53 - loss: 0.9712 - categorical_accuracy: 0.6928
 2496/60000 [>.............................] - ETA: 1:53 - loss: 0.9620 - categorical_accuracy: 0.6955
 2528/60000 [>.............................] - ETA: 1:53 - loss: 0.9552 - categorical_accuracy: 0.6974
 2560/60000 [>.............................] - ETA: 1:53 - loss: 0.9534 - categorical_accuracy: 0.6988
 2592/60000 [>.............................] - ETA: 1:53 - loss: 0.9451 - categorical_accuracy: 0.7025
 2624/60000 [>.............................] - ETA: 1:53 - loss: 0.9406 - categorical_accuracy: 0.7035
 2656/60000 [>.............................] - ETA: 1:53 - loss: 0.9366 - categorical_accuracy: 0.7044
 2688/60000 [>.............................] - ETA: 1:52 - loss: 0.9296 - categorical_accuracy: 0.7065
 2720/60000 [>.............................] - ETA: 1:53 - loss: 0.9235 - categorical_accuracy: 0.7085
 2752/60000 [>.............................] - ETA: 1:52 - loss: 0.9172 - categorical_accuracy: 0.7100
 2784/60000 [>.............................] - ETA: 1:52 - loss: 0.9096 - categorical_accuracy: 0.7123
 2816/60000 [>.............................] - ETA: 1:52 - loss: 0.9070 - categorical_accuracy: 0.7138
 2848/60000 [>.............................] - ETA: 1:52 - loss: 0.9058 - categorical_accuracy: 0.7149
 2880/60000 [>.............................] - ETA: 1:52 - loss: 0.9043 - categorical_accuracy: 0.7149
 2912/60000 [>.............................] - ETA: 1:52 - loss: 0.9008 - categorical_accuracy: 0.7163
 2944/60000 [>.............................] - ETA: 1:52 - loss: 0.8939 - categorical_accuracy: 0.7191
 2976/60000 [>.............................] - ETA: 1:52 - loss: 0.8869 - categorical_accuracy: 0.7214
 3008/60000 [>.............................] - ETA: 1:51 - loss: 0.8810 - categorical_accuracy: 0.7234
 3040/60000 [>.............................] - ETA: 1:51 - loss: 0.8753 - categorical_accuracy: 0.7247
 3072/60000 [>.............................] - ETA: 1:51 - loss: 0.8703 - categorical_accuracy: 0.7262
 3104/60000 [>.............................] - ETA: 1:51 - loss: 0.8656 - categorical_accuracy: 0.7274
 3136/60000 [>.............................] - ETA: 1:51 - loss: 0.8606 - categorical_accuracy: 0.7296
 3168/60000 [>.............................] - ETA: 1:51 - loss: 0.8549 - categorical_accuracy: 0.7307
 3200/60000 [>.............................] - ETA: 1:51 - loss: 0.8499 - categorical_accuracy: 0.7325
 3232/60000 [>.............................] - ETA: 1:51 - loss: 0.8470 - categorical_accuracy: 0.7336
 3264/60000 [>.............................] - ETA: 1:50 - loss: 0.8428 - categorical_accuracy: 0.7350
 3296/60000 [>.............................] - ETA: 1:50 - loss: 0.8381 - categorical_accuracy: 0.7367
 3328/60000 [>.............................] - ETA: 1:50 - loss: 0.8329 - categorical_accuracy: 0.7380
 3360/60000 [>.............................] - ETA: 1:50 - loss: 0.8285 - categorical_accuracy: 0.7396
 3392/60000 [>.............................] - ETA: 1:50 - loss: 0.8228 - categorical_accuracy: 0.7415
 3424/60000 [>.............................] - ETA: 1:50 - loss: 0.8173 - categorical_accuracy: 0.7427
 3456/60000 [>.............................] - ETA: 1:50 - loss: 0.8149 - categorical_accuracy: 0.7433
 3488/60000 [>.............................] - ETA: 1:50 - loss: 0.8125 - categorical_accuracy: 0.7443
 3520/60000 [>.............................] - ETA: 1:50 - loss: 0.8097 - categorical_accuracy: 0.7452
 3552/60000 [>.............................] - ETA: 1:50 - loss: 0.8046 - categorical_accuracy: 0.7463
 3584/60000 [>.............................] - ETA: 1:49 - loss: 0.8023 - categorical_accuracy: 0.7469
 3616/60000 [>.............................] - ETA: 1:49 - loss: 0.7963 - categorical_accuracy: 0.7492
 3648/60000 [>.............................] - ETA: 1:49 - loss: 0.7935 - categorical_accuracy: 0.7503
 3680/60000 [>.............................] - ETA: 1:49 - loss: 0.7913 - categorical_accuracy: 0.7514
 3712/60000 [>.............................] - ETA: 1:49 - loss: 0.7885 - categorical_accuracy: 0.7527
 3744/60000 [>.............................] - ETA: 1:49 - loss: 0.7873 - categorical_accuracy: 0.7535
 3776/60000 [>.............................] - ETA: 1:49 - loss: 0.7829 - categorical_accuracy: 0.7550
 3808/60000 [>.............................] - ETA: 1:49 - loss: 0.7780 - categorical_accuracy: 0.7568
 3840/60000 [>.............................] - ETA: 1:49 - loss: 0.7767 - categorical_accuracy: 0.7570
 3872/60000 [>.............................] - ETA: 1:49 - loss: 0.7741 - categorical_accuracy: 0.7577
 3904/60000 [>.............................] - ETA: 1:49 - loss: 0.7690 - categorical_accuracy: 0.7595
 3936/60000 [>.............................] - ETA: 1:49 - loss: 0.7684 - categorical_accuracy: 0.7599
 3968/60000 [>.............................] - ETA: 1:49 - loss: 0.7661 - categorical_accuracy: 0.7613
 4000/60000 [=>............................] - ETA: 1:48 - loss: 0.7634 - categorical_accuracy: 0.7620
 4032/60000 [=>............................] - ETA: 1:48 - loss: 0.7602 - categorical_accuracy: 0.7629
 4064/60000 [=>............................] - ETA: 1:48 - loss: 0.7562 - categorical_accuracy: 0.7643
 4096/60000 [=>............................] - ETA: 1:48 - loss: 0.7530 - categorical_accuracy: 0.7651
 4128/60000 [=>............................] - ETA: 1:48 - loss: 0.7527 - categorical_accuracy: 0.7653
 4160/60000 [=>............................] - ETA: 1:48 - loss: 0.7486 - categorical_accuracy: 0.7666
 4192/60000 [=>............................] - ETA: 1:48 - loss: 0.7451 - categorical_accuracy: 0.7677
 4224/60000 [=>............................] - ETA: 1:48 - loss: 0.7415 - categorical_accuracy: 0.7689
 4256/60000 [=>............................] - ETA: 1:48 - loss: 0.7381 - categorical_accuracy: 0.7702
 4288/60000 [=>............................] - ETA: 1:48 - loss: 0.7362 - categorical_accuracy: 0.7710
 4320/60000 [=>............................] - ETA: 1:48 - loss: 0.7334 - categorical_accuracy: 0.7725
 4352/60000 [=>............................] - ETA: 1:48 - loss: 0.7289 - categorical_accuracy: 0.7739
 4384/60000 [=>............................] - ETA: 1:48 - loss: 0.7268 - categorical_accuracy: 0.7751
 4416/60000 [=>............................] - ETA: 1:48 - loss: 0.7219 - categorical_accuracy: 0.7767
 4448/60000 [=>............................] - ETA: 1:48 - loss: 0.7190 - categorical_accuracy: 0.7774
 4480/60000 [=>............................] - ETA: 1:47 - loss: 0.7161 - categorical_accuracy: 0.7781
 4512/60000 [=>............................] - ETA: 1:47 - loss: 0.7137 - categorical_accuracy: 0.7788
 4544/60000 [=>............................] - ETA: 1:47 - loss: 0.7102 - categorical_accuracy: 0.7799
 4576/60000 [=>............................] - ETA: 1:47 - loss: 0.7080 - categorical_accuracy: 0.7808
 4608/60000 [=>............................] - ETA: 1:47 - loss: 0.7049 - categorical_accuracy: 0.7817
 4640/60000 [=>............................] - ETA: 1:47 - loss: 0.7015 - categorical_accuracy: 0.7828
 4672/60000 [=>............................] - ETA: 1:47 - loss: 0.6991 - categorical_accuracy: 0.7836
 4704/60000 [=>............................] - ETA: 1:47 - loss: 0.6972 - categorical_accuracy: 0.7844
 4736/60000 [=>............................] - ETA: 1:47 - loss: 0.6933 - categorical_accuracy: 0.7857
 4768/60000 [=>............................] - ETA: 1:47 - loss: 0.6914 - categorical_accuracy: 0.7869
 4800/60000 [=>............................] - ETA: 1:47 - loss: 0.6897 - categorical_accuracy: 0.7873
 4832/60000 [=>............................] - ETA: 1:47 - loss: 0.6867 - categorical_accuracy: 0.7883
 4864/60000 [=>............................] - ETA: 1:46 - loss: 0.6835 - categorical_accuracy: 0.7893
 4896/60000 [=>............................] - ETA: 1:46 - loss: 0.6803 - categorical_accuracy: 0.7902
 4928/60000 [=>............................] - ETA: 1:46 - loss: 0.6784 - categorical_accuracy: 0.7906
 4960/60000 [=>............................] - ETA: 1:46 - loss: 0.6758 - categorical_accuracy: 0.7913
 4992/60000 [=>............................] - ETA: 1:46 - loss: 0.6741 - categorical_accuracy: 0.7917
 5024/60000 [=>............................] - ETA: 1:46 - loss: 0.6717 - categorical_accuracy: 0.7926
 5056/60000 [=>............................] - ETA: 1:46 - loss: 0.6697 - categorical_accuracy: 0.7933
 5088/60000 [=>............................] - ETA: 1:46 - loss: 0.6682 - categorical_accuracy: 0.7936
 5120/60000 [=>............................] - ETA: 1:46 - loss: 0.6657 - categorical_accuracy: 0.7943
 5152/60000 [=>............................] - ETA: 1:46 - loss: 0.6626 - categorical_accuracy: 0.7952
 5184/60000 [=>............................] - ETA: 1:46 - loss: 0.6596 - categorical_accuracy: 0.7963
 5216/60000 [=>............................] - ETA: 1:45 - loss: 0.6564 - categorical_accuracy: 0.7974
 5248/60000 [=>............................] - ETA: 1:45 - loss: 0.6534 - categorical_accuracy: 0.7980
 5280/60000 [=>............................] - ETA: 1:45 - loss: 0.6530 - categorical_accuracy: 0.7987
 5312/60000 [=>............................] - ETA: 1:45 - loss: 0.6507 - categorical_accuracy: 0.7993
 5344/60000 [=>............................] - ETA: 1:45 - loss: 0.6478 - categorical_accuracy: 0.8001
 5376/60000 [=>............................] - ETA: 1:45 - loss: 0.6461 - categorical_accuracy: 0.8006
 5408/60000 [=>............................] - ETA: 1:45 - loss: 0.6437 - categorical_accuracy: 0.8014
 5440/60000 [=>............................] - ETA: 1:45 - loss: 0.6407 - categorical_accuracy: 0.8022
 5472/60000 [=>............................] - ETA: 1:45 - loss: 0.6379 - categorical_accuracy: 0.8030
 5504/60000 [=>............................] - ETA: 1:45 - loss: 0.6353 - categorical_accuracy: 0.8038
 5536/60000 [=>............................] - ETA: 1:45 - loss: 0.6324 - categorical_accuracy: 0.8044
 5568/60000 [=>............................] - ETA: 1:45 - loss: 0.6301 - categorical_accuracy: 0.8051
 5600/60000 [=>............................] - ETA: 1:45 - loss: 0.6278 - categorical_accuracy: 0.8057
 5632/60000 [=>............................] - ETA: 1:45 - loss: 0.6259 - categorical_accuracy: 0.8063
 5664/60000 [=>............................] - ETA: 1:44 - loss: 0.6248 - categorical_accuracy: 0.8065
 5696/60000 [=>............................] - ETA: 1:44 - loss: 0.6223 - categorical_accuracy: 0.8072
 5728/60000 [=>............................] - ETA: 1:44 - loss: 0.6208 - categorical_accuracy: 0.8076
 5760/60000 [=>............................] - ETA: 1:44 - loss: 0.6186 - categorical_accuracy: 0.8082
 5792/60000 [=>............................] - ETA: 1:44 - loss: 0.6155 - categorical_accuracy: 0.8092
 5824/60000 [=>............................] - ETA: 1:44 - loss: 0.6133 - categorical_accuracy: 0.8098
 5856/60000 [=>............................] - ETA: 1:44 - loss: 0.6117 - categorical_accuracy: 0.8099
 5888/60000 [=>............................] - ETA: 1:44 - loss: 0.6106 - categorical_accuracy: 0.8108
 5920/60000 [=>............................] - ETA: 1:44 - loss: 0.6084 - categorical_accuracy: 0.8115
 5952/60000 [=>............................] - ETA: 1:44 - loss: 0.6062 - categorical_accuracy: 0.8120
 5984/60000 [=>............................] - ETA: 1:44 - loss: 0.6034 - categorical_accuracy: 0.8128
 6016/60000 [==>...........................] - ETA: 1:44 - loss: 0.6016 - categorical_accuracy: 0.8135
 6048/60000 [==>...........................] - ETA: 1:44 - loss: 0.6013 - categorical_accuracy: 0.8137
 6080/60000 [==>...........................] - ETA: 1:44 - loss: 0.5996 - categorical_accuracy: 0.8141
 6112/60000 [==>...........................] - ETA: 1:44 - loss: 0.5973 - categorical_accuracy: 0.8148
 6144/60000 [==>...........................] - ETA: 1:43 - loss: 0.5953 - categorical_accuracy: 0.8154
 6176/60000 [==>...........................] - ETA: 1:43 - loss: 0.5949 - categorical_accuracy: 0.8157
 6208/60000 [==>...........................] - ETA: 1:43 - loss: 0.5932 - categorical_accuracy: 0.8165
 6240/60000 [==>...........................] - ETA: 1:43 - loss: 0.5909 - categorical_accuracy: 0.8173
 6272/60000 [==>...........................] - ETA: 1:43 - loss: 0.5885 - categorical_accuracy: 0.8181
 6304/60000 [==>...........................] - ETA: 1:43 - loss: 0.5870 - categorical_accuracy: 0.8185
 6336/60000 [==>...........................] - ETA: 1:43 - loss: 0.5861 - categorical_accuracy: 0.8188
 6368/60000 [==>...........................] - ETA: 1:43 - loss: 0.5855 - categorical_accuracy: 0.8191
 6400/60000 [==>...........................] - ETA: 1:43 - loss: 0.5853 - categorical_accuracy: 0.8194
 6432/60000 [==>...........................] - ETA: 1:43 - loss: 0.5834 - categorical_accuracy: 0.8198
 6464/60000 [==>...........................] - ETA: 1:43 - loss: 0.5811 - categorical_accuracy: 0.8205
 6496/60000 [==>...........................] - ETA: 1:43 - loss: 0.5789 - categorical_accuracy: 0.8214
 6528/60000 [==>...........................] - ETA: 1:43 - loss: 0.5766 - categorical_accuracy: 0.8220
 6560/60000 [==>...........................] - ETA: 1:42 - loss: 0.5751 - categorical_accuracy: 0.8223
 6592/60000 [==>...........................] - ETA: 1:42 - loss: 0.5742 - categorical_accuracy: 0.8227
 6624/60000 [==>...........................] - ETA: 1:42 - loss: 0.5726 - categorical_accuracy: 0.8232
 6656/60000 [==>...........................] - ETA: 1:42 - loss: 0.5721 - categorical_accuracy: 0.8233
 6688/60000 [==>...........................] - ETA: 1:42 - loss: 0.5703 - categorical_accuracy: 0.8237
 6720/60000 [==>...........................] - ETA: 1:42 - loss: 0.5687 - categorical_accuracy: 0.8240
 6752/60000 [==>...........................] - ETA: 1:42 - loss: 0.5679 - categorical_accuracy: 0.8242
 6784/60000 [==>...........................] - ETA: 1:42 - loss: 0.5658 - categorical_accuracy: 0.8246
 6816/60000 [==>...........................] - ETA: 1:42 - loss: 0.5640 - categorical_accuracy: 0.8253
 6848/60000 [==>...........................] - ETA: 1:42 - loss: 0.5619 - categorical_accuracy: 0.8259
 6880/60000 [==>...........................] - ETA: 1:42 - loss: 0.5601 - categorical_accuracy: 0.8263
 6912/60000 [==>...........................] - ETA: 1:42 - loss: 0.5592 - categorical_accuracy: 0.8262
 6944/60000 [==>...........................] - ETA: 1:42 - loss: 0.5571 - categorical_accuracy: 0.8269
 6976/60000 [==>...........................] - ETA: 1:42 - loss: 0.5554 - categorical_accuracy: 0.8276
 7008/60000 [==>...........................] - ETA: 1:41 - loss: 0.5539 - categorical_accuracy: 0.8281
 7040/60000 [==>...........................] - ETA: 1:41 - loss: 0.5533 - categorical_accuracy: 0.8280
 7072/60000 [==>...........................] - ETA: 1:41 - loss: 0.5522 - categorical_accuracy: 0.8282
 7104/60000 [==>...........................] - ETA: 1:41 - loss: 0.5503 - categorical_accuracy: 0.8287
 7136/60000 [==>...........................] - ETA: 1:41 - loss: 0.5486 - categorical_accuracy: 0.8292
 7168/60000 [==>...........................] - ETA: 1:41 - loss: 0.5487 - categorical_accuracy: 0.8294
 7200/60000 [==>...........................] - ETA: 1:41 - loss: 0.5471 - categorical_accuracy: 0.8297
 7232/60000 [==>...........................] - ETA: 1:41 - loss: 0.5459 - categorical_accuracy: 0.8301
 7264/60000 [==>...........................] - ETA: 1:41 - loss: 0.5449 - categorical_accuracy: 0.8303
 7296/60000 [==>...........................] - ETA: 1:41 - loss: 0.5438 - categorical_accuracy: 0.8307
 7328/60000 [==>...........................] - ETA: 1:41 - loss: 0.5429 - categorical_accuracy: 0.8308
 7360/60000 [==>...........................] - ETA: 1:41 - loss: 0.5409 - categorical_accuracy: 0.8314
 7392/60000 [==>...........................] - ETA: 1:41 - loss: 0.5395 - categorical_accuracy: 0.8320
 7424/60000 [==>...........................] - ETA: 1:41 - loss: 0.5378 - categorical_accuracy: 0.8324
 7456/60000 [==>...........................] - ETA: 1:40 - loss: 0.5364 - categorical_accuracy: 0.8329
 7488/60000 [==>...........................] - ETA: 1:40 - loss: 0.5348 - categorical_accuracy: 0.8335
 7520/60000 [==>...........................] - ETA: 1:40 - loss: 0.5336 - categorical_accuracy: 0.8338
 7552/60000 [==>...........................] - ETA: 1:40 - loss: 0.5328 - categorical_accuracy: 0.8340
 7584/60000 [==>...........................] - ETA: 1:40 - loss: 0.5312 - categorical_accuracy: 0.8345
 7616/60000 [==>...........................] - ETA: 1:40 - loss: 0.5315 - categorical_accuracy: 0.8346
 7648/60000 [==>...........................] - ETA: 1:40 - loss: 0.5304 - categorical_accuracy: 0.8349
 7680/60000 [==>...........................] - ETA: 1:40 - loss: 0.5289 - categorical_accuracy: 0.8353
 7712/60000 [==>...........................] - ETA: 1:40 - loss: 0.5278 - categorical_accuracy: 0.8357
 7744/60000 [==>...........................] - ETA: 1:40 - loss: 0.5263 - categorical_accuracy: 0.8361
 7776/60000 [==>...........................] - ETA: 1:40 - loss: 0.5255 - categorical_accuracy: 0.8362
 7808/60000 [==>...........................] - ETA: 1:40 - loss: 0.5240 - categorical_accuracy: 0.8366
 7840/60000 [==>...........................] - ETA: 1:40 - loss: 0.5225 - categorical_accuracy: 0.8371
 7872/60000 [==>...........................] - ETA: 1:40 - loss: 0.5213 - categorical_accuracy: 0.8375
 7904/60000 [==>...........................] - ETA: 1:40 - loss: 0.5202 - categorical_accuracy: 0.8378
 7936/60000 [==>...........................] - ETA: 1:40 - loss: 0.5185 - categorical_accuracy: 0.8385
 7968/60000 [==>...........................] - ETA: 1:39 - loss: 0.5174 - categorical_accuracy: 0.8389
 8000/60000 [===>..........................] - ETA: 1:39 - loss: 0.5163 - categorical_accuracy: 0.8391
 8032/60000 [===>..........................] - ETA: 1:39 - loss: 0.5146 - categorical_accuracy: 0.8396
 8064/60000 [===>..........................] - ETA: 1:39 - loss: 0.5143 - categorical_accuracy: 0.8398
 8096/60000 [===>..........................] - ETA: 1:39 - loss: 0.5130 - categorical_accuracy: 0.8403
 8128/60000 [===>..........................] - ETA: 1:39 - loss: 0.5111 - categorical_accuracy: 0.8409
 8160/60000 [===>..........................] - ETA: 1:39 - loss: 0.5096 - categorical_accuracy: 0.8414
 8192/60000 [===>..........................] - ETA: 1:39 - loss: 0.5089 - categorical_accuracy: 0.8417
 8224/60000 [===>..........................] - ETA: 1:39 - loss: 0.5075 - categorical_accuracy: 0.8422
 8256/60000 [===>..........................] - ETA: 1:39 - loss: 0.5063 - categorical_accuracy: 0.8425
 8288/60000 [===>..........................] - ETA: 1:39 - loss: 0.5053 - categorical_accuracy: 0.8430
 8320/60000 [===>..........................] - ETA: 1:39 - loss: 0.5037 - categorical_accuracy: 0.8435
 8352/60000 [===>..........................] - ETA: 1:39 - loss: 0.5022 - categorical_accuracy: 0.8440
 8384/60000 [===>..........................] - ETA: 1:39 - loss: 0.5019 - categorical_accuracy: 0.8442
 8416/60000 [===>..........................] - ETA: 1:39 - loss: 0.5006 - categorical_accuracy: 0.8445
 8448/60000 [===>..........................] - ETA: 1:38 - loss: 0.5000 - categorical_accuracy: 0.8443
 8480/60000 [===>..........................] - ETA: 1:38 - loss: 0.4986 - categorical_accuracy: 0.8447
 8512/60000 [===>..........................] - ETA: 1:38 - loss: 0.4978 - categorical_accuracy: 0.8449
 8544/60000 [===>..........................] - ETA: 1:38 - loss: 0.4962 - categorical_accuracy: 0.8454
 8576/60000 [===>..........................] - ETA: 1:38 - loss: 0.4949 - categorical_accuracy: 0.8457
 8608/60000 [===>..........................] - ETA: 1:38 - loss: 0.4940 - categorical_accuracy: 0.8460
 8640/60000 [===>..........................] - ETA: 1:38 - loss: 0.4929 - categorical_accuracy: 0.8463
 8672/60000 [===>..........................] - ETA: 1:38 - loss: 0.4914 - categorical_accuracy: 0.8467
 8704/60000 [===>..........................] - ETA: 1:38 - loss: 0.4905 - categorical_accuracy: 0.8471
 8736/60000 [===>..........................] - ETA: 1:38 - loss: 0.4896 - categorical_accuracy: 0.8474
 8768/60000 [===>..........................] - ETA: 1:38 - loss: 0.4883 - categorical_accuracy: 0.8479
 8800/60000 [===>..........................] - ETA: 1:38 - loss: 0.4871 - categorical_accuracy: 0.8481
 8832/60000 [===>..........................] - ETA: 1:38 - loss: 0.4863 - categorical_accuracy: 0.8484
 8864/60000 [===>..........................] - ETA: 1:38 - loss: 0.4851 - categorical_accuracy: 0.8487
 8896/60000 [===>..........................] - ETA: 1:38 - loss: 0.4846 - categorical_accuracy: 0.8489
 8928/60000 [===>..........................] - ETA: 1:37 - loss: 0.4835 - categorical_accuracy: 0.8492
 8960/60000 [===>..........................] - ETA: 1:37 - loss: 0.4834 - categorical_accuracy: 0.8496
 8992/60000 [===>..........................] - ETA: 1:37 - loss: 0.4820 - categorical_accuracy: 0.8500
 9024/60000 [===>..........................] - ETA: 1:37 - loss: 0.4812 - categorical_accuracy: 0.8503
 9056/60000 [===>..........................] - ETA: 1:37 - loss: 0.4797 - categorical_accuracy: 0.8508
 9088/60000 [===>..........................] - ETA: 1:37 - loss: 0.4781 - categorical_accuracy: 0.8513
 9120/60000 [===>..........................] - ETA: 1:37 - loss: 0.4769 - categorical_accuracy: 0.8516
 9152/60000 [===>..........................] - ETA: 1:37 - loss: 0.4757 - categorical_accuracy: 0.8521
 9184/60000 [===>..........................] - ETA: 1:37 - loss: 0.4756 - categorical_accuracy: 0.8521
 9216/60000 [===>..........................] - ETA: 1:37 - loss: 0.4746 - categorical_accuracy: 0.8523
 9248/60000 [===>..........................] - ETA: 1:37 - loss: 0.4743 - categorical_accuracy: 0.8524
 9280/60000 [===>..........................] - ETA: 1:37 - loss: 0.4739 - categorical_accuracy: 0.8525
 9312/60000 [===>..........................] - ETA: 1:37 - loss: 0.4730 - categorical_accuracy: 0.8528
 9344/60000 [===>..........................] - ETA: 1:37 - loss: 0.4723 - categorical_accuracy: 0.8530
 9376/60000 [===>..........................] - ETA: 1:37 - loss: 0.4718 - categorical_accuracy: 0.8531
 9408/60000 [===>..........................] - ETA: 1:37 - loss: 0.4705 - categorical_accuracy: 0.8535
 9440/60000 [===>..........................] - ETA: 1:37 - loss: 0.4706 - categorical_accuracy: 0.8536
 9472/60000 [===>..........................] - ETA: 1:36 - loss: 0.4693 - categorical_accuracy: 0.8541
 9504/60000 [===>..........................] - ETA: 1:36 - loss: 0.4685 - categorical_accuracy: 0.8543
 9536/60000 [===>..........................] - ETA: 1:36 - loss: 0.4675 - categorical_accuracy: 0.8546
 9568/60000 [===>..........................] - ETA: 1:36 - loss: 0.4663 - categorical_accuracy: 0.8549
 9600/60000 [===>..........................] - ETA: 1:36 - loss: 0.4654 - categorical_accuracy: 0.8553
 9632/60000 [===>..........................] - ETA: 1:36 - loss: 0.4642 - categorical_accuracy: 0.8557
 9664/60000 [===>..........................] - ETA: 1:36 - loss: 0.4629 - categorical_accuracy: 0.8561
 9696/60000 [===>..........................] - ETA: 1:36 - loss: 0.4618 - categorical_accuracy: 0.8564
 9728/60000 [===>..........................] - ETA: 1:36 - loss: 0.4608 - categorical_accuracy: 0.8566
 9760/60000 [===>..........................] - ETA: 1:36 - loss: 0.4598 - categorical_accuracy: 0.8570
 9792/60000 [===>..........................] - ETA: 1:36 - loss: 0.4586 - categorical_accuracy: 0.8574
 9824/60000 [===>..........................] - ETA: 1:36 - loss: 0.4578 - categorical_accuracy: 0.8577
 9856/60000 [===>..........................] - ETA: 1:36 - loss: 0.4565 - categorical_accuracy: 0.8582
 9888/60000 [===>..........................] - ETA: 1:36 - loss: 0.4558 - categorical_accuracy: 0.8583
 9920/60000 [===>..........................] - ETA: 1:36 - loss: 0.4545 - categorical_accuracy: 0.8588
 9952/60000 [===>..........................] - ETA: 1:36 - loss: 0.4533 - categorical_accuracy: 0.8591
 9984/60000 [===>..........................] - ETA: 1:35 - loss: 0.4520 - categorical_accuracy: 0.8595
10016/60000 [====>.........................] - ETA: 1:35 - loss: 0.4507 - categorical_accuracy: 0.8599
10048/60000 [====>.........................] - ETA: 1:35 - loss: 0.4495 - categorical_accuracy: 0.8603
10080/60000 [====>.........................] - ETA: 1:35 - loss: 0.4488 - categorical_accuracy: 0.8606
10112/60000 [====>.........................] - ETA: 1:35 - loss: 0.4478 - categorical_accuracy: 0.8610
10144/60000 [====>.........................] - ETA: 1:35 - loss: 0.4466 - categorical_accuracy: 0.8613
10176/60000 [====>.........................] - ETA: 1:35 - loss: 0.4459 - categorical_accuracy: 0.8615
10208/60000 [====>.........................] - ETA: 1:35 - loss: 0.4447 - categorical_accuracy: 0.8619
10240/60000 [====>.........................] - ETA: 1:35 - loss: 0.4442 - categorical_accuracy: 0.8620
10272/60000 [====>.........................] - ETA: 1:35 - loss: 0.4433 - categorical_accuracy: 0.8623
10304/60000 [====>.........................] - ETA: 1:35 - loss: 0.4434 - categorical_accuracy: 0.8625
10336/60000 [====>.........................] - ETA: 1:35 - loss: 0.4424 - categorical_accuracy: 0.8627
10368/60000 [====>.........................] - ETA: 1:35 - loss: 0.4416 - categorical_accuracy: 0.8629
10400/60000 [====>.........................] - ETA: 1:35 - loss: 0.4407 - categorical_accuracy: 0.8633
10432/60000 [====>.........................] - ETA: 1:34 - loss: 0.4397 - categorical_accuracy: 0.8636
10464/60000 [====>.........................] - ETA: 1:34 - loss: 0.4389 - categorical_accuracy: 0.8638
10496/60000 [====>.........................] - ETA: 1:34 - loss: 0.4383 - categorical_accuracy: 0.8639
10528/60000 [====>.........................] - ETA: 1:34 - loss: 0.4373 - categorical_accuracy: 0.8642
10560/60000 [====>.........................] - ETA: 1:34 - loss: 0.4365 - categorical_accuracy: 0.8644
10592/60000 [====>.........................] - ETA: 1:34 - loss: 0.4355 - categorical_accuracy: 0.8647
10624/60000 [====>.........................] - ETA: 1:34 - loss: 0.4346 - categorical_accuracy: 0.8649
10656/60000 [====>.........................] - ETA: 1:34 - loss: 0.4337 - categorical_accuracy: 0.8652
10688/60000 [====>.........................] - ETA: 1:34 - loss: 0.4326 - categorical_accuracy: 0.8656
10720/60000 [====>.........................] - ETA: 1:34 - loss: 0.4315 - categorical_accuracy: 0.8659
10752/60000 [====>.........................] - ETA: 1:34 - loss: 0.4310 - categorical_accuracy: 0.8660
10784/60000 [====>.........................] - ETA: 1:34 - loss: 0.4300 - categorical_accuracy: 0.8662
10816/60000 [====>.........................] - ETA: 1:34 - loss: 0.4295 - categorical_accuracy: 0.8664
10848/60000 [====>.........................] - ETA: 1:34 - loss: 0.4286 - categorical_accuracy: 0.8667
10880/60000 [====>.........................] - ETA: 1:34 - loss: 0.4276 - categorical_accuracy: 0.8670
10912/60000 [====>.........................] - ETA: 1:34 - loss: 0.4281 - categorical_accuracy: 0.8672
10944/60000 [====>.........................] - ETA: 1:34 - loss: 0.4279 - categorical_accuracy: 0.8672
10976/60000 [====>.........................] - ETA: 1:33 - loss: 0.4267 - categorical_accuracy: 0.8676
11008/60000 [====>.........................] - ETA: 1:33 - loss: 0.4268 - categorical_accuracy: 0.8676
11040/60000 [====>.........................] - ETA: 1:33 - loss: 0.4263 - categorical_accuracy: 0.8676
11072/60000 [====>.........................] - ETA: 1:33 - loss: 0.4258 - categorical_accuracy: 0.8679
11104/60000 [====>.........................] - ETA: 1:33 - loss: 0.4256 - categorical_accuracy: 0.8680
11136/60000 [====>.........................] - ETA: 1:33 - loss: 0.4250 - categorical_accuracy: 0.8682
11168/60000 [====>.........................] - ETA: 1:33 - loss: 0.4240 - categorical_accuracy: 0.8686
11200/60000 [====>.........................] - ETA: 1:33 - loss: 0.4238 - categorical_accuracy: 0.8687
11232/60000 [====>.........................] - ETA: 1:33 - loss: 0.4232 - categorical_accuracy: 0.8690
11264/60000 [====>.........................] - ETA: 1:33 - loss: 0.4226 - categorical_accuracy: 0.8692
11296/60000 [====>.........................] - ETA: 1:33 - loss: 0.4218 - categorical_accuracy: 0.8695
11328/60000 [====>.........................] - ETA: 1:33 - loss: 0.4212 - categorical_accuracy: 0.8698
11360/60000 [====>.........................] - ETA: 1:33 - loss: 0.4205 - categorical_accuracy: 0.8699
11392/60000 [====>.........................] - ETA: 1:33 - loss: 0.4202 - categorical_accuracy: 0.8698
11424/60000 [====>.........................] - ETA: 1:33 - loss: 0.4196 - categorical_accuracy: 0.8700
11456/60000 [====>.........................] - ETA: 1:33 - loss: 0.4196 - categorical_accuracy: 0.8699
11488/60000 [====>.........................] - ETA: 1:32 - loss: 0.4193 - categorical_accuracy: 0.8700
11520/60000 [====>.........................] - ETA: 1:32 - loss: 0.4194 - categorical_accuracy: 0.8701
11552/60000 [====>.........................] - ETA: 1:32 - loss: 0.4191 - categorical_accuracy: 0.8702
11584/60000 [====>.........................] - ETA: 1:32 - loss: 0.4191 - categorical_accuracy: 0.8703
11616/60000 [====>.........................] - ETA: 1:32 - loss: 0.4187 - categorical_accuracy: 0.8704
11648/60000 [====>.........................] - ETA: 1:32 - loss: 0.4180 - categorical_accuracy: 0.8706
11680/60000 [====>.........................] - ETA: 1:32 - loss: 0.4175 - categorical_accuracy: 0.8707
11712/60000 [====>.........................] - ETA: 1:32 - loss: 0.4167 - categorical_accuracy: 0.8709
11744/60000 [====>.........................] - ETA: 1:32 - loss: 0.4159 - categorical_accuracy: 0.8711
11776/60000 [====>.........................] - ETA: 1:32 - loss: 0.4151 - categorical_accuracy: 0.8714
11808/60000 [====>.........................] - ETA: 1:32 - loss: 0.4142 - categorical_accuracy: 0.8717
11840/60000 [====>.........................] - ETA: 1:32 - loss: 0.4134 - categorical_accuracy: 0.8720
11872/60000 [====>.........................] - ETA: 1:32 - loss: 0.4129 - categorical_accuracy: 0.8721
11904/60000 [====>.........................] - ETA: 1:32 - loss: 0.4119 - categorical_accuracy: 0.8725
11936/60000 [====>.........................] - ETA: 1:32 - loss: 0.4112 - categorical_accuracy: 0.8727
11968/60000 [====>.........................] - ETA: 1:32 - loss: 0.4107 - categorical_accuracy: 0.8728
12000/60000 [=====>........................] - ETA: 1:31 - loss: 0.4098 - categorical_accuracy: 0.8732
12032/60000 [=====>........................] - ETA: 1:31 - loss: 0.4091 - categorical_accuracy: 0.8733
12064/60000 [=====>........................] - ETA: 1:31 - loss: 0.4084 - categorical_accuracy: 0.8735
12096/60000 [=====>........................] - ETA: 1:31 - loss: 0.4074 - categorical_accuracy: 0.8738
12128/60000 [=====>........................] - ETA: 1:31 - loss: 0.4069 - categorical_accuracy: 0.8739
12160/60000 [=====>........................] - ETA: 1:31 - loss: 0.4066 - categorical_accuracy: 0.8741
12192/60000 [=====>........................] - ETA: 1:31 - loss: 0.4061 - categorical_accuracy: 0.8743
12224/60000 [=====>........................] - ETA: 1:31 - loss: 0.4054 - categorical_accuracy: 0.8745
12256/60000 [=====>........................] - ETA: 1:31 - loss: 0.4044 - categorical_accuracy: 0.8748
12288/60000 [=====>........................] - ETA: 1:31 - loss: 0.4039 - categorical_accuracy: 0.8750
12320/60000 [=====>........................] - ETA: 1:31 - loss: 0.4034 - categorical_accuracy: 0.8752
12352/60000 [=====>........................] - ETA: 1:31 - loss: 0.4025 - categorical_accuracy: 0.8754
12384/60000 [=====>........................] - ETA: 1:31 - loss: 0.4018 - categorical_accuracy: 0.8756
12416/60000 [=====>........................] - ETA: 1:31 - loss: 0.4011 - categorical_accuracy: 0.8759
12448/60000 [=====>........................] - ETA: 1:31 - loss: 0.4002 - categorical_accuracy: 0.8761
12480/60000 [=====>........................] - ETA: 1:30 - loss: 0.3999 - categorical_accuracy: 0.8761
12512/60000 [=====>........................] - ETA: 1:30 - loss: 0.3992 - categorical_accuracy: 0.8763
12544/60000 [=====>........................] - ETA: 1:30 - loss: 0.3990 - categorical_accuracy: 0.8762
12576/60000 [=====>........................] - ETA: 1:30 - loss: 0.3984 - categorical_accuracy: 0.8764
12608/60000 [=====>........................] - ETA: 1:30 - loss: 0.3982 - categorical_accuracy: 0.8765
12640/60000 [=====>........................] - ETA: 1:30 - loss: 0.3975 - categorical_accuracy: 0.8767
12672/60000 [=====>........................] - ETA: 1:30 - loss: 0.3973 - categorical_accuracy: 0.8767
12704/60000 [=====>........................] - ETA: 1:30 - loss: 0.3974 - categorical_accuracy: 0.8768
12736/60000 [=====>........................] - ETA: 1:30 - loss: 0.3971 - categorical_accuracy: 0.8769
12768/60000 [=====>........................] - ETA: 1:30 - loss: 0.3962 - categorical_accuracy: 0.8772
12800/60000 [=====>........................] - ETA: 1:30 - loss: 0.3954 - categorical_accuracy: 0.8774
12832/60000 [=====>........................] - ETA: 1:30 - loss: 0.3946 - categorical_accuracy: 0.8777
12864/60000 [=====>........................] - ETA: 1:30 - loss: 0.3945 - categorical_accuracy: 0.8778
12896/60000 [=====>........................] - ETA: 1:30 - loss: 0.3939 - categorical_accuracy: 0.8780
12928/60000 [=====>........................] - ETA: 1:30 - loss: 0.3934 - categorical_accuracy: 0.8781
12960/60000 [=====>........................] - ETA: 1:30 - loss: 0.3925 - categorical_accuracy: 0.8784
12992/60000 [=====>........................] - ETA: 1:29 - loss: 0.3920 - categorical_accuracy: 0.8785
13024/60000 [=====>........................] - ETA: 1:29 - loss: 0.3911 - categorical_accuracy: 0.8788
13056/60000 [=====>........................] - ETA: 1:29 - loss: 0.3909 - categorical_accuracy: 0.8789
13088/60000 [=====>........................] - ETA: 1:29 - loss: 0.3903 - categorical_accuracy: 0.8791
13120/60000 [=====>........................] - ETA: 1:29 - loss: 0.3896 - categorical_accuracy: 0.8793
13152/60000 [=====>........................] - ETA: 1:29 - loss: 0.3898 - categorical_accuracy: 0.8793
13184/60000 [=====>........................] - ETA: 1:29 - loss: 0.3899 - categorical_accuracy: 0.8792
13216/60000 [=====>........................] - ETA: 1:29 - loss: 0.3897 - categorical_accuracy: 0.8794
13248/60000 [=====>........................] - ETA: 1:29 - loss: 0.3899 - categorical_accuracy: 0.8795
13280/60000 [=====>........................] - ETA: 1:29 - loss: 0.3897 - categorical_accuracy: 0.8796
13312/60000 [=====>........................] - ETA: 1:29 - loss: 0.3893 - categorical_accuracy: 0.8797
13344/60000 [=====>........................] - ETA: 1:29 - loss: 0.3888 - categorical_accuracy: 0.8799
13376/60000 [=====>........................] - ETA: 1:29 - loss: 0.3882 - categorical_accuracy: 0.8800
13408/60000 [=====>........................] - ETA: 1:29 - loss: 0.3883 - categorical_accuracy: 0.8801
13440/60000 [=====>........................] - ETA: 1:29 - loss: 0.3882 - categorical_accuracy: 0.8801
13472/60000 [=====>........................] - ETA: 1:28 - loss: 0.3877 - categorical_accuracy: 0.8802
13504/60000 [=====>........................] - ETA: 1:28 - loss: 0.3880 - categorical_accuracy: 0.8801
13536/60000 [=====>........................] - ETA: 1:28 - loss: 0.3873 - categorical_accuracy: 0.8803
13568/60000 [=====>........................] - ETA: 1:28 - loss: 0.3872 - categorical_accuracy: 0.8803
13600/60000 [=====>........................] - ETA: 1:28 - loss: 0.3874 - categorical_accuracy: 0.8804
13632/60000 [=====>........................] - ETA: 1:28 - loss: 0.3869 - categorical_accuracy: 0.8806
13664/60000 [=====>........................] - ETA: 1:28 - loss: 0.3863 - categorical_accuracy: 0.8808
13696/60000 [=====>........................] - ETA: 1:28 - loss: 0.3860 - categorical_accuracy: 0.8808
13728/60000 [=====>........................] - ETA: 1:28 - loss: 0.3852 - categorical_accuracy: 0.8810
13760/60000 [=====>........................] - ETA: 1:28 - loss: 0.3849 - categorical_accuracy: 0.8812
13792/60000 [=====>........................] - ETA: 1:28 - loss: 0.3844 - categorical_accuracy: 0.8814
13824/60000 [=====>........................] - ETA: 1:28 - loss: 0.3840 - categorical_accuracy: 0.8815
13856/60000 [=====>........................] - ETA: 1:28 - loss: 0.3834 - categorical_accuracy: 0.8816
13888/60000 [=====>........................] - ETA: 1:28 - loss: 0.3829 - categorical_accuracy: 0.8817
13920/60000 [=====>........................] - ETA: 1:28 - loss: 0.3823 - categorical_accuracy: 0.8819
13952/60000 [=====>........................] - ETA: 1:27 - loss: 0.3816 - categorical_accuracy: 0.8822
13984/60000 [=====>........................] - ETA: 1:27 - loss: 0.3811 - categorical_accuracy: 0.8823
14016/60000 [======>.......................] - ETA: 1:27 - loss: 0.3804 - categorical_accuracy: 0.8825
14048/60000 [======>.......................] - ETA: 1:27 - loss: 0.3802 - categorical_accuracy: 0.8824
14080/60000 [======>.......................] - ETA: 1:27 - loss: 0.3801 - categorical_accuracy: 0.8824
14112/60000 [======>.......................] - ETA: 1:27 - loss: 0.3793 - categorical_accuracy: 0.8827
14144/60000 [======>.......................] - ETA: 1:27 - loss: 0.3788 - categorical_accuracy: 0.8828
14176/60000 [======>.......................] - ETA: 1:27 - loss: 0.3781 - categorical_accuracy: 0.8830
14208/60000 [======>.......................] - ETA: 1:27 - loss: 0.3776 - categorical_accuracy: 0.8832
14240/60000 [======>.......................] - ETA: 1:27 - loss: 0.3782 - categorical_accuracy: 0.8832
14272/60000 [======>.......................] - ETA: 1:27 - loss: 0.3777 - categorical_accuracy: 0.8834
14304/60000 [======>.......................] - ETA: 1:27 - loss: 0.3772 - categorical_accuracy: 0.8835
14336/60000 [======>.......................] - ETA: 1:27 - loss: 0.3768 - categorical_accuracy: 0.8836
14368/60000 [======>.......................] - ETA: 1:27 - loss: 0.3765 - categorical_accuracy: 0.8837
14400/60000 [======>.......................] - ETA: 1:27 - loss: 0.3760 - categorical_accuracy: 0.8838
14432/60000 [======>.......................] - ETA: 1:27 - loss: 0.3758 - categorical_accuracy: 0.8839
14464/60000 [======>.......................] - ETA: 1:27 - loss: 0.3756 - categorical_accuracy: 0.8839
14496/60000 [======>.......................] - ETA: 1:26 - loss: 0.3751 - categorical_accuracy: 0.8841
14528/60000 [======>.......................] - ETA: 1:26 - loss: 0.3743 - categorical_accuracy: 0.8844
14560/60000 [======>.......................] - ETA: 1:26 - loss: 0.3750 - categorical_accuracy: 0.8843
14592/60000 [======>.......................] - ETA: 1:26 - loss: 0.3743 - categorical_accuracy: 0.8845
14624/60000 [======>.......................] - ETA: 1:26 - loss: 0.3738 - categorical_accuracy: 0.8846
14656/60000 [======>.......................] - ETA: 1:26 - loss: 0.3731 - categorical_accuracy: 0.8849
14688/60000 [======>.......................] - ETA: 1:26 - loss: 0.3725 - categorical_accuracy: 0.8851
14720/60000 [======>.......................] - ETA: 1:26 - loss: 0.3718 - categorical_accuracy: 0.8853
14752/60000 [======>.......................] - ETA: 1:26 - loss: 0.3714 - categorical_accuracy: 0.8854
14784/60000 [======>.......................] - ETA: 1:26 - loss: 0.3707 - categorical_accuracy: 0.8856
14816/60000 [======>.......................] - ETA: 1:26 - loss: 0.3704 - categorical_accuracy: 0.8858
14848/60000 [======>.......................] - ETA: 1:26 - loss: 0.3700 - categorical_accuracy: 0.8859
14880/60000 [======>.......................] - ETA: 1:26 - loss: 0.3700 - categorical_accuracy: 0.8860
14912/60000 [======>.......................] - ETA: 1:26 - loss: 0.3694 - categorical_accuracy: 0.8862
14944/60000 [======>.......................] - ETA: 1:26 - loss: 0.3690 - categorical_accuracy: 0.8863
14976/60000 [======>.......................] - ETA: 1:25 - loss: 0.3683 - categorical_accuracy: 0.8866
15008/60000 [======>.......................] - ETA: 1:25 - loss: 0.3677 - categorical_accuracy: 0.8867
15040/60000 [======>.......................] - ETA: 1:25 - loss: 0.3674 - categorical_accuracy: 0.8868
15072/60000 [======>.......................] - ETA: 1:25 - loss: 0.3669 - categorical_accuracy: 0.8867
15104/60000 [======>.......................] - ETA: 1:25 - loss: 0.3668 - categorical_accuracy: 0.8867
15136/60000 [======>.......................] - ETA: 1:25 - loss: 0.3671 - categorical_accuracy: 0.8868
15168/60000 [======>.......................] - ETA: 1:25 - loss: 0.3672 - categorical_accuracy: 0.8869
15200/60000 [======>.......................] - ETA: 1:25 - loss: 0.3668 - categorical_accuracy: 0.8870
15232/60000 [======>.......................] - ETA: 1:25 - loss: 0.3661 - categorical_accuracy: 0.8873
15264/60000 [======>.......................] - ETA: 1:25 - loss: 0.3655 - categorical_accuracy: 0.8875
15296/60000 [======>.......................] - ETA: 1:25 - loss: 0.3647 - categorical_accuracy: 0.8877
15328/60000 [======>.......................] - ETA: 1:25 - loss: 0.3641 - categorical_accuracy: 0.8880
15360/60000 [======>.......................] - ETA: 1:25 - loss: 0.3636 - categorical_accuracy: 0.8881
15392/60000 [======>.......................] - ETA: 1:25 - loss: 0.3637 - categorical_accuracy: 0.8882
15424/60000 [======>.......................] - ETA: 1:25 - loss: 0.3639 - categorical_accuracy: 0.8882
15456/60000 [======>.......................] - ETA: 1:24 - loss: 0.3632 - categorical_accuracy: 0.8885
15488/60000 [======>.......................] - ETA: 1:24 - loss: 0.3626 - categorical_accuracy: 0.8887
15520/60000 [======>.......................] - ETA: 1:24 - loss: 0.3621 - categorical_accuracy: 0.8888
15552/60000 [======>.......................] - ETA: 1:24 - loss: 0.3617 - categorical_accuracy: 0.8889
15584/60000 [======>.......................] - ETA: 1:24 - loss: 0.3610 - categorical_accuracy: 0.8891
15616/60000 [======>.......................] - ETA: 1:24 - loss: 0.3608 - categorical_accuracy: 0.8891
15648/60000 [======>.......................] - ETA: 1:24 - loss: 0.3602 - categorical_accuracy: 0.8893
15680/60000 [======>.......................] - ETA: 1:24 - loss: 0.3596 - categorical_accuracy: 0.8895
15712/60000 [======>.......................] - ETA: 1:24 - loss: 0.3594 - categorical_accuracy: 0.8896
15744/60000 [======>.......................] - ETA: 1:24 - loss: 0.3591 - categorical_accuracy: 0.8897
15776/60000 [======>.......................] - ETA: 1:24 - loss: 0.3586 - categorical_accuracy: 0.8898
15808/60000 [======>.......................] - ETA: 1:24 - loss: 0.3583 - categorical_accuracy: 0.8900
15840/60000 [======>.......................] - ETA: 1:24 - loss: 0.3584 - categorical_accuracy: 0.8900
15872/60000 [======>.......................] - ETA: 1:24 - loss: 0.3578 - categorical_accuracy: 0.8902
15904/60000 [======>.......................] - ETA: 1:24 - loss: 0.3576 - categorical_accuracy: 0.8903
15936/60000 [======>.......................] - ETA: 1:24 - loss: 0.3570 - categorical_accuracy: 0.8905
15968/60000 [======>.......................] - ETA: 1:24 - loss: 0.3564 - categorical_accuracy: 0.8907
16000/60000 [=======>......................] - ETA: 1:23 - loss: 0.3561 - categorical_accuracy: 0.8907
16032/60000 [=======>......................] - ETA: 1:23 - loss: 0.3559 - categorical_accuracy: 0.8907
16064/60000 [=======>......................] - ETA: 1:23 - loss: 0.3556 - categorical_accuracy: 0.8907
16096/60000 [=======>......................] - ETA: 1:23 - loss: 0.3556 - categorical_accuracy: 0.8906
16128/60000 [=======>......................] - ETA: 1:23 - loss: 0.3559 - categorical_accuracy: 0.8905
16160/60000 [=======>......................] - ETA: 1:23 - loss: 0.3554 - categorical_accuracy: 0.8907
16192/60000 [=======>......................] - ETA: 1:23 - loss: 0.3551 - categorical_accuracy: 0.8909
16224/60000 [=======>......................] - ETA: 1:23 - loss: 0.3546 - categorical_accuracy: 0.8910
16256/60000 [=======>......................] - ETA: 1:23 - loss: 0.3542 - categorical_accuracy: 0.8912
16288/60000 [=======>......................] - ETA: 1:23 - loss: 0.3537 - categorical_accuracy: 0.8913
16320/60000 [=======>......................] - ETA: 1:23 - loss: 0.3531 - categorical_accuracy: 0.8915
16352/60000 [=======>......................] - ETA: 1:23 - loss: 0.3525 - categorical_accuracy: 0.8918
16384/60000 [=======>......................] - ETA: 1:23 - loss: 0.3521 - categorical_accuracy: 0.8918
16416/60000 [=======>......................] - ETA: 1:23 - loss: 0.3519 - categorical_accuracy: 0.8919
16448/60000 [=======>......................] - ETA: 1:23 - loss: 0.3518 - categorical_accuracy: 0.8918
16480/60000 [=======>......................] - ETA: 1:23 - loss: 0.3514 - categorical_accuracy: 0.8919
16512/60000 [=======>......................] - ETA: 1:22 - loss: 0.3512 - categorical_accuracy: 0.8920
16544/60000 [=======>......................] - ETA: 1:22 - loss: 0.3514 - categorical_accuracy: 0.8920
16576/60000 [=======>......................] - ETA: 1:22 - loss: 0.3509 - categorical_accuracy: 0.8921
16608/60000 [=======>......................] - ETA: 1:22 - loss: 0.3504 - categorical_accuracy: 0.8923
16640/60000 [=======>......................] - ETA: 1:22 - loss: 0.3498 - categorical_accuracy: 0.8924
16672/60000 [=======>......................] - ETA: 1:22 - loss: 0.3493 - categorical_accuracy: 0.8926
16704/60000 [=======>......................] - ETA: 1:22 - loss: 0.3492 - categorical_accuracy: 0.8926
16736/60000 [=======>......................] - ETA: 1:22 - loss: 0.3489 - categorical_accuracy: 0.8927
16768/60000 [=======>......................] - ETA: 1:22 - loss: 0.3485 - categorical_accuracy: 0.8928
16800/60000 [=======>......................] - ETA: 1:22 - loss: 0.3479 - categorical_accuracy: 0.8930
16832/60000 [=======>......................] - ETA: 1:22 - loss: 0.3481 - categorical_accuracy: 0.8929
16864/60000 [=======>......................] - ETA: 1:22 - loss: 0.3478 - categorical_accuracy: 0.8930
16896/60000 [=======>......................] - ETA: 1:22 - loss: 0.3475 - categorical_accuracy: 0.8931
16928/60000 [=======>......................] - ETA: 1:22 - loss: 0.3470 - categorical_accuracy: 0.8933
16960/60000 [=======>......................] - ETA: 1:22 - loss: 0.3468 - categorical_accuracy: 0.8934
16992/60000 [=======>......................] - ETA: 1:22 - loss: 0.3463 - categorical_accuracy: 0.8935
17024/60000 [=======>......................] - ETA: 1:21 - loss: 0.3459 - categorical_accuracy: 0.8936
17056/60000 [=======>......................] - ETA: 1:21 - loss: 0.3458 - categorical_accuracy: 0.8936
17088/60000 [=======>......................] - ETA: 1:21 - loss: 0.3455 - categorical_accuracy: 0.8937
17120/60000 [=======>......................] - ETA: 1:21 - loss: 0.3453 - categorical_accuracy: 0.8938
17152/60000 [=======>......................] - ETA: 1:21 - loss: 0.3449 - categorical_accuracy: 0.8939
17184/60000 [=======>......................] - ETA: 1:21 - loss: 0.3443 - categorical_accuracy: 0.8941
17216/60000 [=======>......................] - ETA: 1:21 - loss: 0.3442 - categorical_accuracy: 0.8941
17248/60000 [=======>......................] - ETA: 1:21 - loss: 0.3437 - categorical_accuracy: 0.8942
17280/60000 [=======>......................] - ETA: 1:21 - loss: 0.3433 - categorical_accuracy: 0.8944
17312/60000 [=======>......................] - ETA: 1:21 - loss: 0.3427 - categorical_accuracy: 0.8945
17344/60000 [=======>......................] - ETA: 1:21 - loss: 0.3422 - categorical_accuracy: 0.8947
17376/60000 [=======>......................] - ETA: 1:21 - loss: 0.3417 - categorical_accuracy: 0.8949
17408/60000 [=======>......................] - ETA: 1:21 - loss: 0.3414 - categorical_accuracy: 0.8949
17440/60000 [=======>......................] - ETA: 1:21 - loss: 0.3410 - categorical_accuracy: 0.8951
17472/60000 [=======>......................] - ETA: 1:21 - loss: 0.3407 - categorical_accuracy: 0.8953
17504/60000 [=======>......................] - ETA: 1:21 - loss: 0.3404 - categorical_accuracy: 0.8954
17536/60000 [=======>......................] - ETA: 1:21 - loss: 0.3398 - categorical_accuracy: 0.8956
17568/60000 [=======>......................] - ETA: 1:20 - loss: 0.3398 - categorical_accuracy: 0.8957
17600/60000 [=======>......................] - ETA: 1:20 - loss: 0.3393 - categorical_accuracy: 0.8959
17632/60000 [=======>......................] - ETA: 1:20 - loss: 0.3391 - categorical_accuracy: 0.8960
17664/60000 [=======>......................] - ETA: 1:20 - loss: 0.3386 - categorical_accuracy: 0.8961
17696/60000 [=======>......................] - ETA: 1:20 - loss: 0.3385 - categorical_accuracy: 0.8962
17728/60000 [=======>......................] - ETA: 1:20 - loss: 0.3381 - categorical_accuracy: 0.8964
17760/60000 [=======>......................] - ETA: 1:20 - loss: 0.3380 - categorical_accuracy: 0.8965
17792/60000 [=======>......................] - ETA: 1:20 - loss: 0.3377 - categorical_accuracy: 0.8965
17824/60000 [=======>......................] - ETA: 1:20 - loss: 0.3373 - categorical_accuracy: 0.8966
17856/60000 [=======>......................] - ETA: 1:20 - loss: 0.3367 - categorical_accuracy: 0.8968
17888/60000 [=======>......................] - ETA: 1:20 - loss: 0.3365 - categorical_accuracy: 0.8969
17920/60000 [=======>......................] - ETA: 1:20 - loss: 0.3362 - categorical_accuracy: 0.8970
17952/60000 [=======>......................] - ETA: 1:20 - loss: 0.3360 - categorical_accuracy: 0.8971
17984/60000 [=======>......................] - ETA: 1:20 - loss: 0.3356 - categorical_accuracy: 0.8972
18016/60000 [========>.....................] - ETA: 1:20 - loss: 0.3352 - categorical_accuracy: 0.8974
18048/60000 [========>.....................] - ETA: 1:19 - loss: 0.3347 - categorical_accuracy: 0.8976
18080/60000 [========>.....................] - ETA: 1:19 - loss: 0.3343 - categorical_accuracy: 0.8977
18112/60000 [========>.....................] - ETA: 1:19 - loss: 0.3342 - categorical_accuracy: 0.8977
18144/60000 [========>.....................] - ETA: 1:19 - loss: 0.3342 - categorical_accuracy: 0.8977
18176/60000 [========>.....................] - ETA: 1:19 - loss: 0.3338 - categorical_accuracy: 0.8979
18208/60000 [========>.....................] - ETA: 1:19 - loss: 0.3335 - categorical_accuracy: 0.8980
18240/60000 [========>.....................] - ETA: 1:19 - loss: 0.3330 - categorical_accuracy: 0.8981
18272/60000 [========>.....................] - ETA: 1:19 - loss: 0.3325 - categorical_accuracy: 0.8983
18304/60000 [========>.....................] - ETA: 1:19 - loss: 0.3324 - categorical_accuracy: 0.8983
18336/60000 [========>.....................] - ETA: 1:19 - loss: 0.3319 - categorical_accuracy: 0.8985
18368/60000 [========>.....................] - ETA: 1:19 - loss: 0.3314 - categorical_accuracy: 0.8986
18400/60000 [========>.....................] - ETA: 1:19 - loss: 0.3315 - categorical_accuracy: 0.8986
18432/60000 [========>.....................] - ETA: 1:19 - loss: 0.3314 - categorical_accuracy: 0.8987
18464/60000 [========>.....................] - ETA: 1:19 - loss: 0.3313 - categorical_accuracy: 0.8988
18496/60000 [========>.....................] - ETA: 1:19 - loss: 0.3309 - categorical_accuracy: 0.8988
18528/60000 [========>.....................] - ETA: 1:19 - loss: 0.3305 - categorical_accuracy: 0.8990
18560/60000 [========>.....................] - ETA: 1:18 - loss: 0.3303 - categorical_accuracy: 0.8990
18592/60000 [========>.....................] - ETA: 1:18 - loss: 0.3298 - categorical_accuracy: 0.8991
18624/60000 [========>.....................] - ETA: 1:18 - loss: 0.3297 - categorical_accuracy: 0.8992
18656/60000 [========>.....................] - ETA: 1:18 - loss: 0.3298 - categorical_accuracy: 0.8992
18688/60000 [========>.....................] - ETA: 1:18 - loss: 0.3301 - categorical_accuracy: 0.8992
18720/60000 [========>.....................] - ETA: 1:18 - loss: 0.3297 - categorical_accuracy: 0.8994
18752/60000 [========>.....................] - ETA: 1:18 - loss: 0.3293 - categorical_accuracy: 0.8994
18784/60000 [========>.....................] - ETA: 1:18 - loss: 0.3288 - categorical_accuracy: 0.8996
18816/60000 [========>.....................] - ETA: 1:18 - loss: 0.3284 - categorical_accuracy: 0.8997
18848/60000 [========>.....................] - ETA: 1:18 - loss: 0.3283 - categorical_accuracy: 0.8998
18880/60000 [========>.....................] - ETA: 1:18 - loss: 0.3278 - categorical_accuracy: 0.8999
18912/60000 [========>.....................] - ETA: 1:18 - loss: 0.3283 - categorical_accuracy: 0.8999
18944/60000 [========>.....................] - ETA: 1:18 - loss: 0.3279 - categorical_accuracy: 0.9000
18976/60000 [========>.....................] - ETA: 1:18 - loss: 0.3276 - categorical_accuracy: 0.9000
19008/60000 [========>.....................] - ETA: 1:18 - loss: 0.3277 - categorical_accuracy: 0.9001
19040/60000 [========>.....................] - ETA: 1:18 - loss: 0.3274 - categorical_accuracy: 0.9002
19072/60000 [========>.....................] - ETA: 1:18 - loss: 0.3272 - categorical_accuracy: 0.9002
19104/60000 [========>.....................] - ETA: 1:17 - loss: 0.3273 - categorical_accuracy: 0.9002
19136/60000 [========>.....................] - ETA: 1:17 - loss: 0.3270 - categorical_accuracy: 0.9003
19168/60000 [========>.....................] - ETA: 1:17 - loss: 0.3267 - categorical_accuracy: 0.9004
19200/60000 [========>.....................] - ETA: 1:17 - loss: 0.3263 - categorical_accuracy: 0.9005
19232/60000 [========>.....................] - ETA: 1:17 - loss: 0.3262 - categorical_accuracy: 0.9005
19264/60000 [========>.....................] - ETA: 1:17 - loss: 0.3259 - categorical_accuracy: 0.9006
19296/60000 [========>.....................] - ETA: 1:17 - loss: 0.3256 - categorical_accuracy: 0.9008
19328/60000 [========>.....................] - ETA: 1:17 - loss: 0.3253 - categorical_accuracy: 0.9009
19360/60000 [========>.....................] - ETA: 1:17 - loss: 0.3249 - categorical_accuracy: 0.9009
19392/60000 [========>.....................] - ETA: 1:17 - loss: 0.3244 - categorical_accuracy: 0.9011
19424/60000 [========>.....................] - ETA: 1:17 - loss: 0.3244 - categorical_accuracy: 0.9011
19456/60000 [========>.....................] - ETA: 1:17 - loss: 0.3239 - categorical_accuracy: 0.9013
19488/60000 [========>.....................] - ETA: 1:17 - loss: 0.3235 - categorical_accuracy: 0.9014
19520/60000 [========>.....................] - ETA: 1:17 - loss: 0.3233 - categorical_accuracy: 0.9015
19552/60000 [========>.....................] - ETA: 1:17 - loss: 0.3238 - categorical_accuracy: 0.9015
19584/60000 [========>.....................] - ETA: 1:16 - loss: 0.3235 - categorical_accuracy: 0.9016
19616/60000 [========>.....................] - ETA: 1:16 - loss: 0.3232 - categorical_accuracy: 0.9017
19648/60000 [========>.....................] - ETA: 1:16 - loss: 0.3231 - categorical_accuracy: 0.9018
19680/60000 [========>.....................] - ETA: 1:16 - loss: 0.3228 - categorical_accuracy: 0.9019
19712/60000 [========>.....................] - ETA: 1:16 - loss: 0.3227 - categorical_accuracy: 0.9018
19744/60000 [========>.....................] - ETA: 1:16 - loss: 0.3227 - categorical_accuracy: 0.9019
19776/60000 [========>.....................] - ETA: 1:16 - loss: 0.3224 - categorical_accuracy: 0.9020
19808/60000 [========>.....................] - ETA: 1:16 - loss: 0.3220 - categorical_accuracy: 0.9022
19840/60000 [========>.....................] - ETA: 1:16 - loss: 0.3217 - categorical_accuracy: 0.9023
19872/60000 [========>.....................] - ETA: 1:16 - loss: 0.3213 - categorical_accuracy: 0.9024
19904/60000 [========>.....................] - ETA: 1:16 - loss: 0.3210 - categorical_accuracy: 0.9025
19936/60000 [========>.....................] - ETA: 1:16 - loss: 0.3209 - categorical_accuracy: 0.9025
19968/60000 [========>.....................] - ETA: 1:16 - loss: 0.3208 - categorical_accuracy: 0.9025
20000/60000 [=========>....................] - ETA: 1:16 - loss: 0.3209 - categorical_accuracy: 0.9025
20032/60000 [=========>....................] - ETA: 1:16 - loss: 0.3206 - categorical_accuracy: 0.9027
20064/60000 [=========>....................] - ETA: 1:16 - loss: 0.3202 - categorical_accuracy: 0.9028
20096/60000 [=========>....................] - ETA: 1:16 - loss: 0.3197 - categorical_accuracy: 0.9030
20128/60000 [=========>....................] - ETA: 1:15 - loss: 0.3195 - categorical_accuracy: 0.9031
20160/60000 [=========>....................] - ETA: 1:15 - loss: 0.3191 - categorical_accuracy: 0.9032
20192/60000 [=========>....................] - ETA: 1:15 - loss: 0.3189 - categorical_accuracy: 0.9032
20224/60000 [=========>....................] - ETA: 1:15 - loss: 0.3186 - categorical_accuracy: 0.9032
20256/60000 [=========>....................] - ETA: 1:15 - loss: 0.3185 - categorical_accuracy: 0.9033
20288/60000 [=========>....................] - ETA: 1:15 - loss: 0.3181 - categorical_accuracy: 0.9034
20320/60000 [=========>....................] - ETA: 1:15 - loss: 0.3178 - categorical_accuracy: 0.9034
20352/60000 [=========>....................] - ETA: 1:15 - loss: 0.3173 - categorical_accuracy: 0.9036
20384/60000 [=========>....................] - ETA: 1:15 - loss: 0.3169 - categorical_accuracy: 0.9037
20416/60000 [=========>....................] - ETA: 1:15 - loss: 0.3167 - categorical_accuracy: 0.9038
20448/60000 [=========>....................] - ETA: 1:15 - loss: 0.3163 - categorical_accuracy: 0.9040
20480/60000 [=========>....................] - ETA: 1:15 - loss: 0.3167 - categorical_accuracy: 0.9039
20512/60000 [=========>....................] - ETA: 1:15 - loss: 0.3163 - categorical_accuracy: 0.9040
20544/60000 [=========>....................] - ETA: 1:15 - loss: 0.3164 - categorical_accuracy: 0.9040
20576/60000 [=========>....................] - ETA: 1:15 - loss: 0.3162 - categorical_accuracy: 0.9040
20608/60000 [=========>....................] - ETA: 1:15 - loss: 0.3157 - categorical_accuracy: 0.9041
20640/60000 [=========>....................] - ETA: 1:14 - loss: 0.3154 - categorical_accuracy: 0.9042
20672/60000 [=========>....................] - ETA: 1:14 - loss: 0.3151 - categorical_accuracy: 0.9043
20704/60000 [=========>....................] - ETA: 1:14 - loss: 0.3147 - categorical_accuracy: 0.9044
20736/60000 [=========>....................] - ETA: 1:14 - loss: 0.3143 - categorical_accuracy: 0.9045
20768/60000 [=========>....................] - ETA: 1:14 - loss: 0.3141 - categorical_accuracy: 0.9046
20800/60000 [=========>....................] - ETA: 1:14 - loss: 0.3137 - categorical_accuracy: 0.9047
20832/60000 [=========>....................] - ETA: 1:14 - loss: 0.3135 - categorical_accuracy: 0.9048
20864/60000 [=========>....................] - ETA: 1:14 - loss: 0.3134 - categorical_accuracy: 0.9047
20896/60000 [=========>....................] - ETA: 1:14 - loss: 0.3131 - categorical_accuracy: 0.9048
20928/60000 [=========>....................] - ETA: 1:14 - loss: 0.3127 - categorical_accuracy: 0.9049
20960/60000 [=========>....................] - ETA: 1:14 - loss: 0.3123 - categorical_accuracy: 0.9050
20992/60000 [=========>....................] - ETA: 1:14 - loss: 0.3119 - categorical_accuracy: 0.9051
21024/60000 [=========>....................] - ETA: 1:14 - loss: 0.3118 - categorical_accuracy: 0.9051
21056/60000 [=========>....................] - ETA: 1:14 - loss: 0.3114 - categorical_accuracy: 0.9053
21088/60000 [=========>....................] - ETA: 1:14 - loss: 0.3110 - categorical_accuracy: 0.9054
21120/60000 [=========>....................] - ETA: 1:14 - loss: 0.3109 - categorical_accuracy: 0.9054
21152/60000 [=========>....................] - ETA: 1:13 - loss: 0.3106 - categorical_accuracy: 0.9055
21184/60000 [=========>....................] - ETA: 1:13 - loss: 0.3103 - categorical_accuracy: 0.9056
21216/60000 [=========>....................] - ETA: 1:13 - loss: 0.3101 - categorical_accuracy: 0.9057
21248/60000 [=========>....................] - ETA: 1:13 - loss: 0.3100 - categorical_accuracy: 0.9057
21280/60000 [=========>....................] - ETA: 1:13 - loss: 0.3097 - categorical_accuracy: 0.9058
21312/60000 [=========>....................] - ETA: 1:13 - loss: 0.3093 - categorical_accuracy: 0.9059
21344/60000 [=========>....................] - ETA: 1:13 - loss: 0.3089 - categorical_accuracy: 0.9061
21376/60000 [=========>....................] - ETA: 1:13 - loss: 0.3087 - categorical_accuracy: 0.9061
21408/60000 [=========>....................] - ETA: 1:13 - loss: 0.3083 - categorical_accuracy: 0.9062
21440/60000 [=========>....................] - ETA: 1:13 - loss: 0.3080 - categorical_accuracy: 0.9062
21472/60000 [=========>....................] - ETA: 1:13 - loss: 0.3076 - categorical_accuracy: 0.9062
21504/60000 [=========>....................] - ETA: 1:13 - loss: 0.3072 - categorical_accuracy: 0.9064
21536/60000 [=========>....................] - ETA: 1:13 - loss: 0.3069 - categorical_accuracy: 0.9065
21568/60000 [=========>....................] - ETA: 1:13 - loss: 0.3065 - categorical_accuracy: 0.9066
21600/60000 [=========>....................] - ETA: 1:13 - loss: 0.3066 - categorical_accuracy: 0.9067
21632/60000 [=========>....................] - ETA: 1:13 - loss: 0.3062 - categorical_accuracy: 0.9068
21664/60000 [=========>....................] - ETA: 1:13 - loss: 0.3059 - categorical_accuracy: 0.9069
21696/60000 [=========>....................] - ETA: 1:12 - loss: 0.3055 - categorical_accuracy: 0.9070
21728/60000 [=========>....................] - ETA: 1:12 - loss: 0.3053 - categorical_accuracy: 0.9070
21760/60000 [=========>....................] - ETA: 1:12 - loss: 0.3049 - categorical_accuracy: 0.9071
21792/60000 [=========>....................] - ETA: 1:12 - loss: 0.3046 - categorical_accuracy: 0.9073
21824/60000 [=========>....................] - ETA: 1:12 - loss: 0.3044 - categorical_accuracy: 0.9073
21856/60000 [=========>....................] - ETA: 1:12 - loss: 0.3040 - categorical_accuracy: 0.9074
21888/60000 [=========>....................] - ETA: 1:12 - loss: 0.3036 - categorical_accuracy: 0.9075
21920/60000 [=========>....................] - ETA: 1:12 - loss: 0.3033 - categorical_accuracy: 0.9076
21952/60000 [=========>....................] - ETA: 1:12 - loss: 0.3029 - categorical_accuracy: 0.9078
21984/60000 [=========>....................] - ETA: 1:12 - loss: 0.3027 - categorical_accuracy: 0.9078
22016/60000 [==========>...................] - ETA: 1:12 - loss: 0.3027 - categorical_accuracy: 0.9078
22048/60000 [==========>...................] - ETA: 1:12 - loss: 0.3026 - categorical_accuracy: 0.9079
22080/60000 [==========>...................] - ETA: 1:12 - loss: 0.3022 - categorical_accuracy: 0.9080
22112/60000 [==========>...................] - ETA: 1:12 - loss: 0.3018 - categorical_accuracy: 0.9081
22144/60000 [==========>...................] - ETA: 1:12 - loss: 0.3014 - categorical_accuracy: 0.9083
22176/60000 [==========>...................] - ETA: 1:12 - loss: 0.3011 - categorical_accuracy: 0.9083
22208/60000 [==========>...................] - ETA: 1:11 - loss: 0.3008 - categorical_accuracy: 0.9084
22240/60000 [==========>...................] - ETA: 1:11 - loss: 0.3005 - categorical_accuracy: 0.9085
22272/60000 [==========>...................] - ETA: 1:11 - loss: 0.3004 - categorical_accuracy: 0.9085
22304/60000 [==========>...................] - ETA: 1:11 - loss: 0.3001 - categorical_accuracy: 0.9086
22336/60000 [==========>...................] - ETA: 1:11 - loss: 0.2997 - categorical_accuracy: 0.9087
22368/60000 [==========>...................] - ETA: 1:11 - loss: 0.2995 - categorical_accuracy: 0.9088
22400/60000 [==========>...................] - ETA: 1:11 - loss: 0.2991 - categorical_accuracy: 0.9089
22432/60000 [==========>...................] - ETA: 1:11 - loss: 0.2987 - categorical_accuracy: 0.9091
22464/60000 [==========>...................] - ETA: 1:11 - loss: 0.2986 - categorical_accuracy: 0.9091
22496/60000 [==========>...................] - ETA: 1:11 - loss: 0.2982 - categorical_accuracy: 0.9093
22528/60000 [==========>...................] - ETA: 1:11 - loss: 0.2978 - categorical_accuracy: 0.9094
22560/60000 [==========>...................] - ETA: 1:11 - loss: 0.2976 - categorical_accuracy: 0.9094
22592/60000 [==========>...................] - ETA: 1:11 - loss: 0.2974 - categorical_accuracy: 0.9095
22624/60000 [==========>...................] - ETA: 1:11 - loss: 0.2974 - categorical_accuracy: 0.9095
22656/60000 [==========>...................] - ETA: 1:11 - loss: 0.2971 - categorical_accuracy: 0.9096
22688/60000 [==========>...................] - ETA: 1:11 - loss: 0.2967 - categorical_accuracy: 0.9097
22720/60000 [==========>...................] - ETA: 1:10 - loss: 0.2964 - categorical_accuracy: 0.9098
22752/60000 [==========>...................] - ETA: 1:10 - loss: 0.2961 - categorical_accuracy: 0.9099
22784/60000 [==========>...................] - ETA: 1:10 - loss: 0.2957 - categorical_accuracy: 0.9100
22816/60000 [==========>...................] - ETA: 1:10 - loss: 0.2954 - categorical_accuracy: 0.9100
22848/60000 [==========>...................] - ETA: 1:10 - loss: 0.2954 - categorical_accuracy: 0.9101
22880/60000 [==========>...................] - ETA: 1:10 - loss: 0.2953 - categorical_accuracy: 0.9101
22912/60000 [==========>...................] - ETA: 1:10 - loss: 0.2951 - categorical_accuracy: 0.9101
22944/60000 [==========>...................] - ETA: 1:10 - loss: 0.2948 - categorical_accuracy: 0.9102
22976/60000 [==========>...................] - ETA: 1:10 - loss: 0.2947 - categorical_accuracy: 0.9103
23008/60000 [==========>...................] - ETA: 1:10 - loss: 0.2943 - categorical_accuracy: 0.9104
23040/60000 [==========>...................] - ETA: 1:10 - loss: 0.2943 - categorical_accuracy: 0.9104
23072/60000 [==========>...................] - ETA: 1:10 - loss: 0.2939 - categorical_accuracy: 0.9105
23104/60000 [==========>...................] - ETA: 1:10 - loss: 0.2937 - categorical_accuracy: 0.9106
23136/60000 [==========>...................] - ETA: 1:10 - loss: 0.2937 - categorical_accuracy: 0.9106
23168/60000 [==========>...................] - ETA: 1:10 - loss: 0.2935 - categorical_accuracy: 0.9106
23200/60000 [==========>...................] - ETA: 1:10 - loss: 0.2933 - categorical_accuracy: 0.9106
23232/60000 [==========>...................] - ETA: 1:09 - loss: 0.2929 - categorical_accuracy: 0.9108
23264/60000 [==========>...................] - ETA: 1:09 - loss: 0.2927 - categorical_accuracy: 0.9108
23296/60000 [==========>...................] - ETA: 1:09 - loss: 0.2923 - categorical_accuracy: 0.9109
23328/60000 [==========>...................] - ETA: 1:09 - loss: 0.2920 - categorical_accuracy: 0.9111
23360/60000 [==========>...................] - ETA: 1:09 - loss: 0.2918 - categorical_accuracy: 0.9111
23392/60000 [==========>...................] - ETA: 1:09 - loss: 0.2918 - categorical_accuracy: 0.9112
23424/60000 [==========>...................] - ETA: 1:09 - loss: 0.2914 - categorical_accuracy: 0.9113
23456/60000 [==========>...................] - ETA: 1:09 - loss: 0.2911 - categorical_accuracy: 0.9114
23488/60000 [==========>...................] - ETA: 1:09 - loss: 0.2908 - categorical_accuracy: 0.9114
23520/60000 [==========>...................] - ETA: 1:09 - loss: 0.2907 - categorical_accuracy: 0.9115
23552/60000 [==========>...................] - ETA: 1:09 - loss: 0.2903 - categorical_accuracy: 0.9116
23584/60000 [==========>...................] - ETA: 1:09 - loss: 0.2900 - categorical_accuracy: 0.9117
23616/60000 [==========>...................] - ETA: 1:09 - loss: 0.2898 - categorical_accuracy: 0.9117
23648/60000 [==========>...................] - ETA: 1:09 - loss: 0.2895 - categorical_accuracy: 0.9118
23680/60000 [==========>...................] - ETA: 1:09 - loss: 0.2893 - categorical_accuracy: 0.9118
23712/60000 [==========>...................] - ETA: 1:09 - loss: 0.2891 - categorical_accuracy: 0.9118
23744/60000 [==========>...................] - ETA: 1:09 - loss: 0.2890 - categorical_accuracy: 0.9118
23776/60000 [==========>...................] - ETA: 1:08 - loss: 0.2887 - categorical_accuracy: 0.9119
23808/60000 [==========>...................] - ETA: 1:08 - loss: 0.2887 - categorical_accuracy: 0.9119
23840/60000 [==========>...................] - ETA: 1:08 - loss: 0.2888 - categorical_accuracy: 0.9119
23872/60000 [==========>...................] - ETA: 1:08 - loss: 0.2885 - categorical_accuracy: 0.9120
23904/60000 [==========>...................] - ETA: 1:08 - loss: 0.2883 - categorical_accuracy: 0.9121
23936/60000 [==========>...................] - ETA: 1:08 - loss: 0.2880 - categorical_accuracy: 0.9122
23968/60000 [==========>...................] - ETA: 1:08 - loss: 0.2877 - categorical_accuracy: 0.9123
24000/60000 [===========>..................] - ETA: 1:08 - loss: 0.2877 - categorical_accuracy: 0.9123
24032/60000 [===========>..................] - ETA: 1:08 - loss: 0.2875 - categorical_accuracy: 0.9123
24064/60000 [===========>..................] - ETA: 1:08 - loss: 0.2873 - categorical_accuracy: 0.9124
24096/60000 [===========>..................] - ETA: 1:08 - loss: 0.2872 - categorical_accuracy: 0.9124
24128/60000 [===========>..................] - ETA: 1:08 - loss: 0.2870 - categorical_accuracy: 0.9125
24160/60000 [===========>..................] - ETA: 1:08 - loss: 0.2868 - categorical_accuracy: 0.9125
24192/60000 [===========>..................] - ETA: 1:08 - loss: 0.2865 - categorical_accuracy: 0.9126
24224/60000 [===========>..................] - ETA: 1:08 - loss: 0.2862 - categorical_accuracy: 0.9126
24256/60000 [===========>..................] - ETA: 1:08 - loss: 0.2861 - categorical_accuracy: 0.9127
24288/60000 [===========>..................] - ETA: 1:07 - loss: 0.2858 - categorical_accuracy: 0.9128
24320/60000 [===========>..................] - ETA: 1:07 - loss: 0.2856 - categorical_accuracy: 0.9129
24352/60000 [===========>..................] - ETA: 1:07 - loss: 0.2855 - categorical_accuracy: 0.9129
24384/60000 [===========>..................] - ETA: 1:07 - loss: 0.2852 - categorical_accuracy: 0.9129
24416/60000 [===========>..................] - ETA: 1:07 - loss: 0.2851 - categorical_accuracy: 0.9130
24448/60000 [===========>..................] - ETA: 1:07 - loss: 0.2850 - categorical_accuracy: 0.9130
24480/60000 [===========>..................] - ETA: 1:07 - loss: 0.2848 - categorical_accuracy: 0.9131
24512/60000 [===========>..................] - ETA: 1:07 - loss: 0.2848 - categorical_accuracy: 0.9130
24544/60000 [===========>..................] - ETA: 1:07 - loss: 0.2846 - categorical_accuracy: 0.9131
24576/60000 [===========>..................] - ETA: 1:07 - loss: 0.2844 - categorical_accuracy: 0.9131
24608/60000 [===========>..................] - ETA: 1:07 - loss: 0.2841 - categorical_accuracy: 0.9132
24640/60000 [===========>..................] - ETA: 1:07 - loss: 0.2839 - categorical_accuracy: 0.9133
24672/60000 [===========>..................] - ETA: 1:07 - loss: 0.2838 - categorical_accuracy: 0.9133
24704/60000 [===========>..................] - ETA: 1:07 - loss: 0.2835 - categorical_accuracy: 0.9134
24736/60000 [===========>..................] - ETA: 1:07 - loss: 0.2831 - categorical_accuracy: 0.9135
24768/60000 [===========>..................] - ETA: 1:07 - loss: 0.2829 - categorical_accuracy: 0.9136
24800/60000 [===========>..................] - ETA: 1:07 - loss: 0.2826 - categorical_accuracy: 0.9136
24832/60000 [===========>..................] - ETA: 1:06 - loss: 0.2824 - categorical_accuracy: 0.9137
24864/60000 [===========>..................] - ETA: 1:06 - loss: 0.2824 - categorical_accuracy: 0.9136
24896/60000 [===========>..................] - ETA: 1:06 - loss: 0.2820 - categorical_accuracy: 0.9137
24928/60000 [===========>..................] - ETA: 1:06 - loss: 0.2818 - categorical_accuracy: 0.9138
24960/60000 [===========>..................] - ETA: 1:06 - loss: 0.2818 - categorical_accuracy: 0.9138
24992/60000 [===========>..................] - ETA: 1:06 - loss: 0.2817 - categorical_accuracy: 0.9138
25024/60000 [===========>..................] - ETA: 1:06 - loss: 0.2814 - categorical_accuracy: 0.9139
25056/60000 [===========>..................] - ETA: 1:06 - loss: 0.2812 - categorical_accuracy: 0.9139
25088/60000 [===========>..................] - ETA: 1:06 - loss: 0.2809 - categorical_accuracy: 0.9140
25120/60000 [===========>..................] - ETA: 1:06 - loss: 0.2807 - categorical_accuracy: 0.9141
25152/60000 [===========>..................] - ETA: 1:06 - loss: 0.2804 - categorical_accuracy: 0.9142
25184/60000 [===========>..................] - ETA: 1:06 - loss: 0.2802 - categorical_accuracy: 0.9142
25216/60000 [===========>..................] - ETA: 1:06 - loss: 0.2800 - categorical_accuracy: 0.9143
25248/60000 [===========>..................] - ETA: 1:06 - loss: 0.2797 - categorical_accuracy: 0.9144
25280/60000 [===========>..................] - ETA: 1:06 - loss: 0.2796 - categorical_accuracy: 0.9144
25312/60000 [===========>..................] - ETA: 1:06 - loss: 0.2794 - categorical_accuracy: 0.9145
25344/60000 [===========>..................] - ETA: 1:05 - loss: 0.2792 - categorical_accuracy: 0.9145
25376/60000 [===========>..................] - ETA: 1:05 - loss: 0.2790 - categorical_accuracy: 0.9146
25408/60000 [===========>..................] - ETA: 1:05 - loss: 0.2787 - categorical_accuracy: 0.9147
25440/60000 [===========>..................] - ETA: 1:05 - loss: 0.2785 - categorical_accuracy: 0.9147
25472/60000 [===========>..................] - ETA: 1:05 - loss: 0.2783 - categorical_accuracy: 0.9147
25504/60000 [===========>..................] - ETA: 1:05 - loss: 0.2780 - categorical_accuracy: 0.9148
25536/60000 [===========>..................] - ETA: 1:05 - loss: 0.2782 - categorical_accuracy: 0.9148
25568/60000 [===========>..................] - ETA: 1:05 - loss: 0.2779 - categorical_accuracy: 0.9149
25600/60000 [===========>..................] - ETA: 1:05 - loss: 0.2776 - categorical_accuracy: 0.9150
25632/60000 [===========>..................] - ETA: 1:05 - loss: 0.2775 - categorical_accuracy: 0.9150
25664/60000 [===========>..................] - ETA: 1:05 - loss: 0.2776 - categorical_accuracy: 0.9151
25696/60000 [===========>..................] - ETA: 1:05 - loss: 0.2774 - categorical_accuracy: 0.9151
25728/60000 [===========>..................] - ETA: 1:05 - loss: 0.2771 - categorical_accuracy: 0.9152
25760/60000 [===========>..................] - ETA: 1:05 - loss: 0.2769 - categorical_accuracy: 0.9153
25792/60000 [===========>..................] - ETA: 1:05 - loss: 0.2766 - categorical_accuracy: 0.9153
25824/60000 [===========>..................] - ETA: 1:05 - loss: 0.2763 - categorical_accuracy: 0.9154
25856/60000 [===========>..................] - ETA: 1:05 - loss: 0.2761 - categorical_accuracy: 0.9155
25888/60000 [===========>..................] - ETA: 1:04 - loss: 0.2759 - categorical_accuracy: 0.9155
25920/60000 [===========>..................] - ETA: 1:04 - loss: 0.2756 - categorical_accuracy: 0.9156
25952/60000 [===========>..................] - ETA: 1:04 - loss: 0.2757 - categorical_accuracy: 0.9156
25984/60000 [===========>..................] - ETA: 1:04 - loss: 0.2755 - categorical_accuracy: 0.9156
26016/60000 [============>.................] - ETA: 1:04 - loss: 0.2756 - categorical_accuracy: 0.9157
26048/60000 [============>.................] - ETA: 1:04 - loss: 0.2753 - categorical_accuracy: 0.9158
26080/60000 [============>.................] - ETA: 1:04 - loss: 0.2753 - categorical_accuracy: 0.9157
26112/60000 [============>.................] - ETA: 1:04 - loss: 0.2750 - categorical_accuracy: 0.9158
26144/60000 [============>.................] - ETA: 1:04 - loss: 0.2747 - categorical_accuracy: 0.9159
26176/60000 [============>.................] - ETA: 1:04 - loss: 0.2746 - categorical_accuracy: 0.9160
26208/60000 [============>.................] - ETA: 1:04 - loss: 0.2743 - categorical_accuracy: 0.9161
26240/60000 [============>.................] - ETA: 1:04 - loss: 0.2741 - categorical_accuracy: 0.9161
26272/60000 [============>.................] - ETA: 1:04 - loss: 0.2739 - categorical_accuracy: 0.9162
26304/60000 [============>.................] - ETA: 1:04 - loss: 0.2736 - categorical_accuracy: 0.9162
26336/60000 [============>.................] - ETA: 1:04 - loss: 0.2734 - categorical_accuracy: 0.9163
26368/60000 [============>.................] - ETA: 1:04 - loss: 0.2732 - categorical_accuracy: 0.9163
26400/60000 [============>.................] - ETA: 1:03 - loss: 0.2730 - categorical_accuracy: 0.9164
26432/60000 [============>.................] - ETA: 1:03 - loss: 0.2728 - categorical_accuracy: 0.9165
26464/60000 [============>.................] - ETA: 1:03 - loss: 0.2725 - categorical_accuracy: 0.9166
26496/60000 [============>.................] - ETA: 1:03 - loss: 0.2722 - categorical_accuracy: 0.9167
26528/60000 [============>.................] - ETA: 1:03 - loss: 0.2720 - categorical_accuracy: 0.9168
26560/60000 [============>.................] - ETA: 1:03 - loss: 0.2718 - categorical_accuracy: 0.9168
26592/60000 [============>.................] - ETA: 1:03 - loss: 0.2716 - categorical_accuracy: 0.9168
26624/60000 [============>.................] - ETA: 1:03 - loss: 0.2713 - categorical_accuracy: 0.9169
26656/60000 [============>.................] - ETA: 1:03 - loss: 0.2710 - categorical_accuracy: 0.9170
26688/60000 [============>.................] - ETA: 1:03 - loss: 0.2709 - categorical_accuracy: 0.9170
26720/60000 [============>.................] - ETA: 1:03 - loss: 0.2706 - categorical_accuracy: 0.9171
26752/60000 [============>.................] - ETA: 1:03 - loss: 0.2705 - categorical_accuracy: 0.9172
26784/60000 [============>.................] - ETA: 1:03 - loss: 0.2705 - categorical_accuracy: 0.9172
26816/60000 [============>.................] - ETA: 1:03 - loss: 0.2703 - categorical_accuracy: 0.9173
26848/60000 [============>.................] - ETA: 1:03 - loss: 0.2700 - categorical_accuracy: 0.9173
26880/60000 [============>.................] - ETA: 1:03 - loss: 0.2697 - categorical_accuracy: 0.9174
26912/60000 [============>.................] - ETA: 1:03 - loss: 0.2695 - categorical_accuracy: 0.9175
26944/60000 [============>.................] - ETA: 1:02 - loss: 0.2694 - categorical_accuracy: 0.9176
26976/60000 [============>.................] - ETA: 1:02 - loss: 0.2694 - categorical_accuracy: 0.9176
27008/60000 [============>.................] - ETA: 1:02 - loss: 0.2691 - categorical_accuracy: 0.9177
27040/60000 [============>.................] - ETA: 1:02 - loss: 0.2689 - categorical_accuracy: 0.9177
27072/60000 [============>.................] - ETA: 1:02 - loss: 0.2686 - categorical_accuracy: 0.9178
27104/60000 [============>.................] - ETA: 1:02 - loss: 0.2684 - categorical_accuracy: 0.9179
27136/60000 [============>.................] - ETA: 1:02 - loss: 0.2683 - categorical_accuracy: 0.9179
27168/60000 [============>.................] - ETA: 1:02 - loss: 0.2680 - categorical_accuracy: 0.9180
27200/60000 [============>.................] - ETA: 1:02 - loss: 0.2678 - categorical_accuracy: 0.9181
27232/60000 [============>.................] - ETA: 1:02 - loss: 0.2676 - categorical_accuracy: 0.9181
27264/60000 [============>.................] - ETA: 1:02 - loss: 0.2674 - categorical_accuracy: 0.9181
27296/60000 [============>.................] - ETA: 1:02 - loss: 0.2673 - categorical_accuracy: 0.9182
27328/60000 [============>.................] - ETA: 1:02 - loss: 0.2672 - categorical_accuracy: 0.9182
27360/60000 [============>.................] - ETA: 1:02 - loss: 0.2670 - categorical_accuracy: 0.9182
27392/60000 [============>.................] - ETA: 1:02 - loss: 0.2667 - categorical_accuracy: 0.9183
27424/60000 [============>.................] - ETA: 1:02 - loss: 0.2666 - categorical_accuracy: 0.9183
27456/60000 [============>.................] - ETA: 1:02 - loss: 0.2664 - categorical_accuracy: 0.9183
27488/60000 [============>.................] - ETA: 1:01 - loss: 0.2663 - categorical_accuracy: 0.9184
27520/60000 [============>.................] - ETA: 1:01 - loss: 0.2661 - categorical_accuracy: 0.9185
27552/60000 [============>.................] - ETA: 1:01 - loss: 0.2658 - categorical_accuracy: 0.9186
27584/60000 [============>.................] - ETA: 1:01 - loss: 0.2655 - categorical_accuracy: 0.9186
27616/60000 [============>.................] - ETA: 1:01 - loss: 0.2653 - categorical_accuracy: 0.9187
27648/60000 [============>.................] - ETA: 1:01 - loss: 0.2651 - categorical_accuracy: 0.9188
27680/60000 [============>.................] - ETA: 1:01 - loss: 0.2656 - categorical_accuracy: 0.9187
27712/60000 [============>.................] - ETA: 1:01 - loss: 0.2653 - categorical_accuracy: 0.9188
27744/60000 [============>.................] - ETA: 1:01 - loss: 0.2650 - categorical_accuracy: 0.9189
27776/60000 [============>.................] - ETA: 1:01 - loss: 0.2649 - categorical_accuracy: 0.9189
27808/60000 [============>.................] - ETA: 1:01 - loss: 0.2648 - categorical_accuracy: 0.9189
27840/60000 [============>.................] - ETA: 1:01 - loss: 0.2646 - categorical_accuracy: 0.9190
27872/60000 [============>.................] - ETA: 1:01 - loss: 0.2645 - categorical_accuracy: 0.9191
27904/60000 [============>.................] - ETA: 1:01 - loss: 0.2642 - categorical_accuracy: 0.9191
27936/60000 [============>.................] - ETA: 1:01 - loss: 0.2640 - categorical_accuracy: 0.9192
27968/60000 [============>.................] - ETA: 1:01 - loss: 0.2640 - categorical_accuracy: 0.9192
28000/60000 [=============>................] - ETA: 1:00 - loss: 0.2640 - categorical_accuracy: 0.9192
28032/60000 [=============>................] - ETA: 1:00 - loss: 0.2638 - categorical_accuracy: 0.9192
28064/60000 [=============>................] - ETA: 1:00 - loss: 0.2637 - categorical_accuracy: 0.9193
28096/60000 [=============>................] - ETA: 1:00 - loss: 0.2638 - categorical_accuracy: 0.9193
28128/60000 [=============>................] - ETA: 1:00 - loss: 0.2635 - categorical_accuracy: 0.9194
28160/60000 [=============>................] - ETA: 1:00 - loss: 0.2633 - categorical_accuracy: 0.9194
28192/60000 [=============>................] - ETA: 1:00 - loss: 0.2631 - categorical_accuracy: 0.9195
28224/60000 [=============>................] - ETA: 1:00 - loss: 0.2630 - categorical_accuracy: 0.9195
28256/60000 [=============>................] - ETA: 1:00 - loss: 0.2629 - categorical_accuracy: 0.9196
28288/60000 [=============>................] - ETA: 1:00 - loss: 0.2626 - categorical_accuracy: 0.9196
28320/60000 [=============>................] - ETA: 1:00 - loss: 0.2625 - categorical_accuracy: 0.9196
28352/60000 [=============>................] - ETA: 1:00 - loss: 0.2626 - categorical_accuracy: 0.9197
28384/60000 [=============>................] - ETA: 1:00 - loss: 0.2624 - categorical_accuracy: 0.9196
28416/60000 [=============>................] - ETA: 1:00 - loss: 0.2621 - categorical_accuracy: 0.9197
28448/60000 [=============>................] - ETA: 1:00 - loss: 0.2619 - categorical_accuracy: 0.9198
28480/60000 [=============>................] - ETA: 1:00 - loss: 0.2616 - categorical_accuracy: 0.9199
28512/60000 [=============>................] - ETA: 59s - loss: 0.2614 - categorical_accuracy: 0.9200 
28544/60000 [=============>................] - ETA: 59s - loss: 0.2611 - categorical_accuracy: 0.9201
28576/60000 [=============>................] - ETA: 59s - loss: 0.2609 - categorical_accuracy: 0.9202
28608/60000 [=============>................] - ETA: 59s - loss: 0.2606 - categorical_accuracy: 0.9202
28640/60000 [=============>................] - ETA: 59s - loss: 0.2605 - categorical_accuracy: 0.9203
28672/60000 [=============>................] - ETA: 59s - loss: 0.2603 - categorical_accuracy: 0.9203
28704/60000 [=============>................] - ETA: 59s - loss: 0.2600 - categorical_accuracy: 0.9204
28736/60000 [=============>................] - ETA: 59s - loss: 0.2599 - categorical_accuracy: 0.9205
28768/60000 [=============>................] - ETA: 59s - loss: 0.2598 - categorical_accuracy: 0.9205
28800/60000 [=============>................] - ETA: 59s - loss: 0.2596 - categorical_accuracy: 0.9206
28832/60000 [=============>................] - ETA: 59s - loss: 0.2594 - categorical_accuracy: 0.9206
28864/60000 [=============>................] - ETA: 59s - loss: 0.2594 - categorical_accuracy: 0.9207
28896/60000 [=============>................] - ETA: 59s - loss: 0.2591 - categorical_accuracy: 0.9208
28928/60000 [=============>................] - ETA: 59s - loss: 0.2589 - categorical_accuracy: 0.9208
28960/60000 [=============>................] - ETA: 59s - loss: 0.2588 - categorical_accuracy: 0.9209
28992/60000 [=============>................] - ETA: 59s - loss: 0.2587 - categorical_accuracy: 0.9209
29024/60000 [=============>................] - ETA: 59s - loss: 0.2584 - categorical_accuracy: 0.9210
29056/60000 [=============>................] - ETA: 58s - loss: 0.2583 - categorical_accuracy: 0.9210
29088/60000 [=============>................] - ETA: 58s - loss: 0.2584 - categorical_accuracy: 0.9210
29120/60000 [=============>................] - ETA: 58s - loss: 0.2584 - categorical_accuracy: 0.9211
29152/60000 [=============>................] - ETA: 58s - loss: 0.2582 - categorical_accuracy: 0.9211
29184/60000 [=============>................] - ETA: 58s - loss: 0.2580 - categorical_accuracy: 0.9212
29216/60000 [=============>................] - ETA: 58s - loss: 0.2578 - categorical_accuracy: 0.9212
29248/60000 [=============>................] - ETA: 58s - loss: 0.2576 - categorical_accuracy: 0.9213
29280/60000 [=============>................] - ETA: 58s - loss: 0.2574 - categorical_accuracy: 0.9214
29312/60000 [=============>................] - ETA: 58s - loss: 0.2574 - categorical_accuracy: 0.9214
29344/60000 [=============>................] - ETA: 58s - loss: 0.2573 - categorical_accuracy: 0.9214
29376/60000 [=============>................] - ETA: 58s - loss: 0.2571 - categorical_accuracy: 0.9215
29408/60000 [=============>................] - ETA: 58s - loss: 0.2571 - categorical_accuracy: 0.9214
29440/60000 [=============>................] - ETA: 58s - loss: 0.2569 - categorical_accuracy: 0.9215
29472/60000 [=============>................] - ETA: 58s - loss: 0.2567 - categorical_accuracy: 0.9216
29504/60000 [=============>................] - ETA: 58s - loss: 0.2567 - categorical_accuracy: 0.9215
29536/60000 [=============>................] - ETA: 58s - loss: 0.2565 - categorical_accuracy: 0.9216
29568/60000 [=============>................] - ETA: 57s - loss: 0.2563 - categorical_accuracy: 0.9217
29600/60000 [=============>................] - ETA: 57s - loss: 0.2560 - categorical_accuracy: 0.9218
29632/60000 [=============>................] - ETA: 57s - loss: 0.2560 - categorical_accuracy: 0.9218
29664/60000 [=============>................] - ETA: 57s - loss: 0.2560 - categorical_accuracy: 0.9218
29696/60000 [=============>................] - ETA: 57s - loss: 0.2557 - categorical_accuracy: 0.9219
29728/60000 [=============>................] - ETA: 57s - loss: 0.2555 - categorical_accuracy: 0.9219
29760/60000 [=============>................] - ETA: 57s - loss: 0.2553 - categorical_accuracy: 0.9220
29792/60000 [=============>................] - ETA: 57s - loss: 0.2552 - categorical_accuracy: 0.9221
29824/60000 [=============>................] - ETA: 57s - loss: 0.2553 - categorical_accuracy: 0.9220
29856/60000 [=============>................] - ETA: 57s - loss: 0.2554 - categorical_accuracy: 0.9221
29888/60000 [=============>................] - ETA: 57s - loss: 0.2551 - categorical_accuracy: 0.9221
29920/60000 [=============>................] - ETA: 57s - loss: 0.2550 - categorical_accuracy: 0.9221
29952/60000 [=============>................] - ETA: 57s - loss: 0.2549 - categorical_accuracy: 0.9222
29984/60000 [=============>................] - ETA: 57s - loss: 0.2549 - categorical_accuracy: 0.9222
30016/60000 [==============>...............] - ETA: 57s - loss: 0.2548 - categorical_accuracy: 0.9222
30048/60000 [==============>...............] - ETA: 57s - loss: 0.2547 - categorical_accuracy: 0.9222
30080/60000 [==============>...............] - ETA: 57s - loss: 0.2545 - categorical_accuracy: 0.9223
30112/60000 [==============>...............] - ETA: 56s - loss: 0.2547 - categorical_accuracy: 0.9222
30144/60000 [==============>...............] - ETA: 56s - loss: 0.2545 - categorical_accuracy: 0.9223
30176/60000 [==============>...............] - ETA: 56s - loss: 0.2543 - categorical_accuracy: 0.9224
30208/60000 [==============>...............] - ETA: 56s - loss: 0.2545 - categorical_accuracy: 0.9223
30240/60000 [==============>...............] - ETA: 56s - loss: 0.2542 - categorical_accuracy: 0.9224
30272/60000 [==============>...............] - ETA: 56s - loss: 0.2541 - categorical_accuracy: 0.9225
30304/60000 [==============>...............] - ETA: 56s - loss: 0.2540 - categorical_accuracy: 0.9225
30336/60000 [==============>...............] - ETA: 56s - loss: 0.2538 - categorical_accuracy: 0.9226
30368/60000 [==============>...............] - ETA: 56s - loss: 0.2536 - categorical_accuracy: 0.9226
30400/60000 [==============>...............] - ETA: 56s - loss: 0.2535 - categorical_accuracy: 0.9226
30432/60000 [==============>...............] - ETA: 56s - loss: 0.2534 - categorical_accuracy: 0.9227
30464/60000 [==============>...............] - ETA: 56s - loss: 0.2531 - categorical_accuracy: 0.9228
30496/60000 [==============>...............] - ETA: 56s - loss: 0.2533 - categorical_accuracy: 0.9227
30528/60000 [==============>...............] - ETA: 56s - loss: 0.2532 - categorical_accuracy: 0.9227
30560/60000 [==============>...............] - ETA: 56s - loss: 0.2530 - categorical_accuracy: 0.9227
30592/60000 [==============>...............] - ETA: 56s - loss: 0.2530 - categorical_accuracy: 0.9228
30624/60000 [==============>...............] - ETA: 55s - loss: 0.2533 - categorical_accuracy: 0.9228
30656/60000 [==============>...............] - ETA: 55s - loss: 0.2531 - categorical_accuracy: 0.9228
30688/60000 [==============>...............] - ETA: 55s - loss: 0.2529 - categorical_accuracy: 0.9229
30720/60000 [==============>...............] - ETA: 55s - loss: 0.2526 - categorical_accuracy: 0.9230
30752/60000 [==============>...............] - ETA: 55s - loss: 0.2524 - categorical_accuracy: 0.9231
30784/60000 [==============>...............] - ETA: 55s - loss: 0.2524 - categorical_accuracy: 0.9231
30816/60000 [==============>...............] - ETA: 55s - loss: 0.2529 - categorical_accuracy: 0.9230
30848/60000 [==============>...............] - ETA: 55s - loss: 0.2528 - categorical_accuracy: 0.9231
30880/60000 [==============>...............] - ETA: 55s - loss: 0.2526 - categorical_accuracy: 0.9232
30912/60000 [==============>...............] - ETA: 55s - loss: 0.2524 - categorical_accuracy: 0.9232
30944/60000 [==============>...............] - ETA: 55s - loss: 0.2522 - categorical_accuracy: 0.9233
30976/60000 [==============>...............] - ETA: 55s - loss: 0.2520 - categorical_accuracy: 0.9234
31008/60000 [==============>...............] - ETA: 55s - loss: 0.2518 - categorical_accuracy: 0.9234
31040/60000 [==============>...............] - ETA: 55s - loss: 0.2519 - categorical_accuracy: 0.9234
31072/60000 [==============>...............] - ETA: 55s - loss: 0.2518 - categorical_accuracy: 0.9234
31104/60000 [==============>...............] - ETA: 55s - loss: 0.2516 - categorical_accuracy: 0.9235
31136/60000 [==============>...............] - ETA: 55s - loss: 0.2515 - categorical_accuracy: 0.9235
31168/60000 [==============>...............] - ETA: 54s - loss: 0.2513 - categorical_accuracy: 0.9235
31200/60000 [==============>...............] - ETA: 54s - loss: 0.2511 - categorical_accuracy: 0.9236
31232/60000 [==============>...............] - ETA: 54s - loss: 0.2512 - categorical_accuracy: 0.9237
31264/60000 [==============>...............] - ETA: 54s - loss: 0.2509 - categorical_accuracy: 0.9237
31296/60000 [==============>...............] - ETA: 54s - loss: 0.2507 - categorical_accuracy: 0.9238
31328/60000 [==============>...............] - ETA: 54s - loss: 0.2506 - categorical_accuracy: 0.9238
31360/60000 [==============>...............] - ETA: 54s - loss: 0.2505 - categorical_accuracy: 0.9239
31392/60000 [==============>...............] - ETA: 54s - loss: 0.2504 - categorical_accuracy: 0.9239
31424/60000 [==============>...............] - ETA: 54s - loss: 0.2504 - categorical_accuracy: 0.9239
31456/60000 [==============>...............] - ETA: 54s - loss: 0.2502 - categorical_accuracy: 0.9240
31488/60000 [==============>...............] - ETA: 54s - loss: 0.2500 - categorical_accuracy: 0.9240
31520/60000 [==============>...............] - ETA: 54s - loss: 0.2498 - categorical_accuracy: 0.9241
31552/60000 [==============>...............] - ETA: 54s - loss: 0.2495 - categorical_accuracy: 0.9242
31584/60000 [==============>...............] - ETA: 54s - loss: 0.2495 - categorical_accuracy: 0.9242
31616/60000 [==============>...............] - ETA: 54s - loss: 0.2494 - categorical_accuracy: 0.9242
31648/60000 [==============>...............] - ETA: 54s - loss: 0.2492 - categorical_accuracy: 0.9243
31680/60000 [==============>...............] - ETA: 53s - loss: 0.2490 - categorical_accuracy: 0.9243
31712/60000 [==============>...............] - ETA: 53s - loss: 0.2491 - categorical_accuracy: 0.9243
31744/60000 [==============>...............] - ETA: 53s - loss: 0.2489 - categorical_accuracy: 0.9244
31776/60000 [==============>...............] - ETA: 53s - loss: 0.2487 - categorical_accuracy: 0.9244
31808/60000 [==============>...............] - ETA: 53s - loss: 0.2487 - categorical_accuracy: 0.9244
31840/60000 [==============>...............] - ETA: 53s - loss: 0.2486 - categorical_accuracy: 0.9244
31872/60000 [==============>...............] - ETA: 53s - loss: 0.2485 - categorical_accuracy: 0.9244
31904/60000 [==============>...............] - ETA: 53s - loss: 0.2486 - categorical_accuracy: 0.9245
31936/60000 [==============>...............] - ETA: 53s - loss: 0.2484 - categorical_accuracy: 0.9245
31968/60000 [==============>...............] - ETA: 53s - loss: 0.2482 - categorical_accuracy: 0.9245
32000/60000 [===============>..............] - ETA: 53s - loss: 0.2480 - categorical_accuracy: 0.9246
32032/60000 [===============>..............] - ETA: 53s - loss: 0.2478 - categorical_accuracy: 0.9247
32064/60000 [===============>..............] - ETA: 53s - loss: 0.2476 - categorical_accuracy: 0.9248
32096/60000 [===============>..............] - ETA: 53s - loss: 0.2474 - categorical_accuracy: 0.9248
32128/60000 [===============>..............] - ETA: 53s - loss: 0.2473 - categorical_accuracy: 0.9249
32160/60000 [===============>..............] - ETA: 53s - loss: 0.2472 - categorical_accuracy: 0.9248
32192/60000 [===============>..............] - ETA: 52s - loss: 0.2470 - categorical_accuracy: 0.9249
32224/60000 [===============>..............] - ETA: 52s - loss: 0.2469 - categorical_accuracy: 0.9249
32256/60000 [===============>..............] - ETA: 52s - loss: 0.2471 - categorical_accuracy: 0.9249
32288/60000 [===============>..............] - ETA: 52s - loss: 0.2470 - categorical_accuracy: 0.9250
32320/60000 [===============>..............] - ETA: 52s - loss: 0.2468 - categorical_accuracy: 0.9250
32352/60000 [===============>..............] - ETA: 52s - loss: 0.2466 - categorical_accuracy: 0.9251
32384/60000 [===============>..............] - ETA: 52s - loss: 0.2465 - categorical_accuracy: 0.9251
32416/60000 [===============>..............] - ETA: 52s - loss: 0.2463 - categorical_accuracy: 0.9252
32448/60000 [===============>..............] - ETA: 52s - loss: 0.2462 - categorical_accuracy: 0.9252
32480/60000 [===============>..............] - ETA: 52s - loss: 0.2461 - categorical_accuracy: 0.9252
32512/60000 [===============>..............] - ETA: 52s - loss: 0.2459 - categorical_accuracy: 0.9253
32544/60000 [===============>..............] - ETA: 52s - loss: 0.2457 - categorical_accuracy: 0.9253
32576/60000 [===============>..............] - ETA: 52s - loss: 0.2458 - categorical_accuracy: 0.9253
32608/60000 [===============>..............] - ETA: 52s - loss: 0.2456 - categorical_accuracy: 0.9254
32640/60000 [===============>..............] - ETA: 52s - loss: 0.2455 - categorical_accuracy: 0.9254
32672/60000 [===============>..............] - ETA: 52s - loss: 0.2454 - categorical_accuracy: 0.9254
32704/60000 [===============>..............] - ETA: 52s - loss: 0.2452 - categorical_accuracy: 0.9255
32736/60000 [===============>..............] - ETA: 51s - loss: 0.2450 - categorical_accuracy: 0.9256
32768/60000 [===============>..............] - ETA: 51s - loss: 0.2448 - categorical_accuracy: 0.9256
32800/60000 [===============>..............] - ETA: 51s - loss: 0.2446 - categorical_accuracy: 0.9257
32832/60000 [===============>..............] - ETA: 51s - loss: 0.2444 - categorical_accuracy: 0.9257
32864/60000 [===============>..............] - ETA: 51s - loss: 0.2443 - categorical_accuracy: 0.9258
32896/60000 [===============>..............] - ETA: 51s - loss: 0.2441 - categorical_accuracy: 0.9259
32928/60000 [===============>..............] - ETA: 51s - loss: 0.2439 - categorical_accuracy: 0.9259
32960/60000 [===============>..............] - ETA: 51s - loss: 0.2437 - categorical_accuracy: 0.9259
32992/60000 [===============>..............] - ETA: 51s - loss: 0.2437 - categorical_accuracy: 0.9260
33024/60000 [===============>..............] - ETA: 51s - loss: 0.2435 - categorical_accuracy: 0.9260
33056/60000 [===============>..............] - ETA: 51s - loss: 0.2438 - categorical_accuracy: 0.9260
33088/60000 [===============>..............] - ETA: 51s - loss: 0.2437 - categorical_accuracy: 0.9260
33120/60000 [===============>..............] - ETA: 51s - loss: 0.2436 - categorical_accuracy: 0.9261
33152/60000 [===============>..............] - ETA: 51s - loss: 0.2434 - categorical_accuracy: 0.9261
33184/60000 [===============>..............] - ETA: 51s - loss: 0.2433 - categorical_accuracy: 0.9261
33216/60000 [===============>..............] - ETA: 51s - loss: 0.2431 - categorical_accuracy: 0.9262
33248/60000 [===============>..............] - ETA: 50s - loss: 0.2430 - categorical_accuracy: 0.9262
33280/60000 [===============>..............] - ETA: 50s - loss: 0.2429 - categorical_accuracy: 0.9263
33312/60000 [===============>..............] - ETA: 50s - loss: 0.2427 - categorical_accuracy: 0.9263
33344/60000 [===============>..............] - ETA: 50s - loss: 0.2426 - categorical_accuracy: 0.9263
33376/60000 [===============>..............] - ETA: 50s - loss: 0.2424 - categorical_accuracy: 0.9264
33408/60000 [===============>..............] - ETA: 50s - loss: 0.2422 - categorical_accuracy: 0.9265
33440/60000 [===============>..............] - ETA: 50s - loss: 0.2420 - categorical_accuracy: 0.9266
33472/60000 [===============>..............] - ETA: 50s - loss: 0.2420 - categorical_accuracy: 0.9265
33504/60000 [===============>..............] - ETA: 50s - loss: 0.2419 - categorical_accuracy: 0.9265
33536/60000 [===============>..............] - ETA: 50s - loss: 0.2417 - categorical_accuracy: 0.9265
33568/60000 [===============>..............] - ETA: 50s - loss: 0.2415 - categorical_accuracy: 0.9266
33600/60000 [===============>..............] - ETA: 50s - loss: 0.2413 - categorical_accuracy: 0.9267
33632/60000 [===============>..............] - ETA: 50s - loss: 0.2413 - categorical_accuracy: 0.9267
33664/60000 [===============>..............] - ETA: 50s - loss: 0.2411 - categorical_accuracy: 0.9267
33696/60000 [===============>..............] - ETA: 50s - loss: 0.2410 - categorical_accuracy: 0.9268
33728/60000 [===============>..............] - ETA: 50s - loss: 0.2410 - categorical_accuracy: 0.9267
33760/60000 [===============>..............] - ETA: 49s - loss: 0.2408 - categorical_accuracy: 0.9268
33792/60000 [===============>..............] - ETA: 49s - loss: 0.2408 - categorical_accuracy: 0.9268
33824/60000 [===============>..............] - ETA: 49s - loss: 0.2406 - categorical_accuracy: 0.9269
33856/60000 [===============>..............] - ETA: 49s - loss: 0.2406 - categorical_accuracy: 0.9269
33888/60000 [===============>..............] - ETA: 49s - loss: 0.2404 - categorical_accuracy: 0.9269
33920/60000 [===============>..............] - ETA: 49s - loss: 0.2404 - categorical_accuracy: 0.9269
33952/60000 [===============>..............] - ETA: 49s - loss: 0.2402 - categorical_accuracy: 0.9270
33984/60000 [===============>..............] - ETA: 49s - loss: 0.2400 - categorical_accuracy: 0.9270
34016/60000 [================>.............] - ETA: 49s - loss: 0.2399 - categorical_accuracy: 0.9270
34048/60000 [================>.............] - ETA: 49s - loss: 0.2397 - categorical_accuracy: 0.9271
34080/60000 [================>.............] - ETA: 49s - loss: 0.2396 - categorical_accuracy: 0.9271
34112/60000 [================>.............] - ETA: 49s - loss: 0.2395 - categorical_accuracy: 0.9271
34144/60000 [================>.............] - ETA: 49s - loss: 0.2394 - categorical_accuracy: 0.9271
34176/60000 [================>.............] - ETA: 49s - loss: 0.2394 - categorical_accuracy: 0.9271
34208/60000 [================>.............] - ETA: 49s - loss: 0.2392 - categorical_accuracy: 0.9272
34240/60000 [================>.............] - ETA: 49s - loss: 0.2390 - categorical_accuracy: 0.9272
34272/60000 [================>.............] - ETA: 48s - loss: 0.2389 - categorical_accuracy: 0.9272
34304/60000 [================>.............] - ETA: 48s - loss: 0.2388 - categorical_accuracy: 0.9273
34336/60000 [================>.............] - ETA: 48s - loss: 0.2389 - categorical_accuracy: 0.9272
34368/60000 [================>.............] - ETA: 48s - loss: 0.2388 - categorical_accuracy: 0.9273
34400/60000 [================>.............] - ETA: 48s - loss: 0.2386 - categorical_accuracy: 0.9273
34432/60000 [================>.............] - ETA: 48s - loss: 0.2384 - categorical_accuracy: 0.9274
34464/60000 [================>.............] - ETA: 48s - loss: 0.2382 - categorical_accuracy: 0.9275
34496/60000 [================>.............] - ETA: 48s - loss: 0.2380 - categorical_accuracy: 0.9275
34528/60000 [================>.............] - ETA: 48s - loss: 0.2380 - categorical_accuracy: 0.9276
34560/60000 [================>.............] - ETA: 48s - loss: 0.2378 - categorical_accuracy: 0.9276
34592/60000 [================>.............] - ETA: 48s - loss: 0.2377 - categorical_accuracy: 0.9276
34624/60000 [================>.............] - ETA: 48s - loss: 0.2377 - categorical_accuracy: 0.9276
34656/60000 [================>.............] - ETA: 48s - loss: 0.2376 - categorical_accuracy: 0.9276
34688/60000 [================>.............] - ETA: 48s - loss: 0.2374 - categorical_accuracy: 0.9277
34720/60000 [================>.............] - ETA: 48s - loss: 0.2374 - categorical_accuracy: 0.9277
34752/60000 [================>.............] - ETA: 48s - loss: 0.2372 - categorical_accuracy: 0.9277
34784/60000 [================>.............] - ETA: 47s - loss: 0.2372 - categorical_accuracy: 0.9278
34816/60000 [================>.............] - ETA: 47s - loss: 0.2370 - categorical_accuracy: 0.9278
34848/60000 [================>.............] - ETA: 47s - loss: 0.2368 - categorical_accuracy: 0.9279
34880/60000 [================>.............] - ETA: 47s - loss: 0.2366 - categorical_accuracy: 0.9279
34912/60000 [================>.............] - ETA: 47s - loss: 0.2366 - categorical_accuracy: 0.9280
34944/60000 [================>.............] - ETA: 47s - loss: 0.2364 - categorical_accuracy: 0.9280
34976/60000 [================>.............] - ETA: 47s - loss: 0.2362 - categorical_accuracy: 0.9280
35008/60000 [================>.............] - ETA: 47s - loss: 0.2361 - categorical_accuracy: 0.9280
35040/60000 [================>.............] - ETA: 47s - loss: 0.2360 - categorical_accuracy: 0.9281
35072/60000 [================>.............] - ETA: 47s - loss: 0.2358 - categorical_accuracy: 0.9282
35104/60000 [================>.............] - ETA: 47s - loss: 0.2357 - categorical_accuracy: 0.9282
35136/60000 [================>.............] - ETA: 47s - loss: 0.2357 - categorical_accuracy: 0.9282
35168/60000 [================>.............] - ETA: 47s - loss: 0.2355 - categorical_accuracy: 0.9283
35200/60000 [================>.............] - ETA: 47s - loss: 0.2355 - categorical_accuracy: 0.9283
35232/60000 [================>.............] - ETA: 47s - loss: 0.2353 - categorical_accuracy: 0.9283
35264/60000 [================>.............] - ETA: 47s - loss: 0.2351 - categorical_accuracy: 0.9284
35296/60000 [================>.............] - ETA: 47s - loss: 0.2349 - categorical_accuracy: 0.9284
35328/60000 [================>.............] - ETA: 46s - loss: 0.2348 - categorical_accuracy: 0.9284
35360/60000 [================>.............] - ETA: 46s - loss: 0.2347 - categorical_accuracy: 0.9285
35392/60000 [================>.............] - ETA: 46s - loss: 0.2345 - categorical_accuracy: 0.9285
35424/60000 [================>.............] - ETA: 46s - loss: 0.2344 - categorical_accuracy: 0.9286
35456/60000 [================>.............] - ETA: 46s - loss: 0.2343 - categorical_accuracy: 0.9286
35488/60000 [================>.............] - ETA: 46s - loss: 0.2342 - categorical_accuracy: 0.9287
35520/60000 [================>.............] - ETA: 46s - loss: 0.2340 - categorical_accuracy: 0.9287
35552/60000 [================>.............] - ETA: 46s - loss: 0.2338 - categorical_accuracy: 0.9288
35584/60000 [================>.............] - ETA: 46s - loss: 0.2337 - categorical_accuracy: 0.9288
35616/60000 [================>.............] - ETA: 46s - loss: 0.2335 - categorical_accuracy: 0.9289
35648/60000 [================>.............] - ETA: 46s - loss: 0.2334 - categorical_accuracy: 0.9289
35680/60000 [================>.............] - ETA: 46s - loss: 0.2334 - categorical_accuracy: 0.9289
35712/60000 [================>.............] - ETA: 46s - loss: 0.2333 - categorical_accuracy: 0.9289
35744/60000 [================>.............] - ETA: 46s - loss: 0.2332 - categorical_accuracy: 0.9290
35776/60000 [================>.............] - ETA: 46s - loss: 0.2330 - categorical_accuracy: 0.9290
35808/60000 [================>.............] - ETA: 46s - loss: 0.2328 - categorical_accuracy: 0.9291
35840/60000 [================>.............] - ETA: 46s - loss: 0.2327 - categorical_accuracy: 0.9291
35872/60000 [================>.............] - ETA: 45s - loss: 0.2326 - categorical_accuracy: 0.9292
35904/60000 [================>.............] - ETA: 45s - loss: 0.2326 - categorical_accuracy: 0.9292
35936/60000 [================>.............] - ETA: 45s - loss: 0.2324 - categorical_accuracy: 0.9292
35968/60000 [================>.............] - ETA: 45s - loss: 0.2322 - categorical_accuracy: 0.9293
36000/60000 [=================>............] - ETA: 45s - loss: 0.2321 - categorical_accuracy: 0.9293
36032/60000 [=================>............] - ETA: 45s - loss: 0.2320 - categorical_accuracy: 0.9294
36064/60000 [=================>............] - ETA: 45s - loss: 0.2319 - categorical_accuracy: 0.9294
36096/60000 [=================>............] - ETA: 45s - loss: 0.2320 - categorical_accuracy: 0.9294
36128/60000 [=================>............] - ETA: 45s - loss: 0.2319 - categorical_accuracy: 0.9294
36160/60000 [=================>............] - ETA: 45s - loss: 0.2318 - categorical_accuracy: 0.9294
36192/60000 [=================>............] - ETA: 45s - loss: 0.2318 - categorical_accuracy: 0.9294
36224/60000 [=================>............] - ETA: 45s - loss: 0.2316 - categorical_accuracy: 0.9295
36256/60000 [=================>............] - ETA: 45s - loss: 0.2315 - categorical_accuracy: 0.9295
36288/60000 [=================>............] - ETA: 45s - loss: 0.2314 - categorical_accuracy: 0.9295
36320/60000 [=================>............] - ETA: 45s - loss: 0.2315 - categorical_accuracy: 0.9295
36352/60000 [=================>............] - ETA: 45s - loss: 0.2313 - categorical_accuracy: 0.9296
36384/60000 [=================>............] - ETA: 44s - loss: 0.2314 - categorical_accuracy: 0.9296
36416/60000 [=================>............] - ETA: 44s - loss: 0.2312 - categorical_accuracy: 0.9297
36448/60000 [=================>............] - ETA: 44s - loss: 0.2313 - categorical_accuracy: 0.9297
36480/60000 [=================>............] - ETA: 44s - loss: 0.2312 - categorical_accuracy: 0.9297
36512/60000 [=================>............] - ETA: 44s - loss: 0.2311 - categorical_accuracy: 0.9297
36544/60000 [=================>............] - ETA: 44s - loss: 0.2309 - categorical_accuracy: 0.9298
36576/60000 [=================>............] - ETA: 44s - loss: 0.2307 - categorical_accuracy: 0.9298
36608/60000 [=================>............] - ETA: 44s - loss: 0.2306 - categorical_accuracy: 0.9298
36640/60000 [=================>............] - ETA: 44s - loss: 0.2304 - categorical_accuracy: 0.9299
36672/60000 [=================>............] - ETA: 44s - loss: 0.2302 - categorical_accuracy: 0.9299
36704/60000 [=================>............] - ETA: 44s - loss: 0.2301 - categorical_accuracy: 0.9300
36736/60000 [=================>............] - ETA: 44s - loss: 0.2299 - categorical_accuracy: 0.9301
36768/60000 [=================>............] - ETA: 44s - loss: 0.2297 - categorical_accuracy: 0.9301
36800/60000 [=================>............] - ETA: 44s - loss: 0.2297 - categorical_accuracy: 0.9301
36832/60000 [=================>............] - ETA: 44s - loss: 0.2295 - categorical_accuracy: 0.9302
36864/60000 [=================>............] - ETA: 44s - loss: 0.2294 - categorical_accuracy: 0.9302
36896/60000 [=================>............] - ETA: 44s - loss: 0.2292 - categorical_accuracy: 0.9303
36928/60000 [=================>............] - ETA: 43s - loss: 0.2290 - categorical_accuracy: 0.9303
36960/60000 [=================>............] - ETA: 43s - loss: 0.2291 - categorical_accuracy: 0.9303
36992/60000 [=================>............] - ETA: 43s - loss: 0.2290 - categorical_accuracy: 0.9304
37024/60000 [=================>............] - ETA: 43s - loss: 0.2290 - categorical_accuracy: 0.9304
37056/60000 [=================>............] - ETA: 43s - loss: 0.2288 - categorical_accuracy: 0.9305
37088/60000 [=================>............] - ETA: 43s - loss: 0.2287 - categorical_accuracy: 0.9305
37120/60000 [=================>............] - ETA: 43s - loss: 0.2286 - categorical_accuracy: 0.9305
37152/60000 [=================>............] - ETA: 43s - loss: 0.2288 - categorical_accuracy: 0.9305
37184/60000 [=================>............] - ETA: 43s - loss: 0.2286 - categorical_accuracy: 0.9305
37216/60000 [=================>............] - ETA: 43s - loss: 0.2284 - categorical_accuracy: 0.9306
37248/60000 [=================>............] - ETA: 43s - loss: 0.2286 - categorical_accuracy: 0.9306
37280/60000 [=================>............] - ETA: 43s - loss: 0.2286 - categorical_accuracy: 0.9306
37312/60000 [=================>............] - ETA: 43s - loss: 0.2285 - categorical_accuracy: 0.9306
37344/60000 [=================>............] - ETA: 43s - loss: 0.2284 - categorical_accuracy: 0.9306
37376/60000 [=================>............] - ETA: 43s - loss: 0.2283 - categorical_accuracy: 0.9306
37408/60000 [=================>............] - ETA: 43s - loss: 0.2282 - categorical_accuracy: 0.9306
37440/60000 [=================>............] - ETA: 42s - loss: 0.2283 - categorical_accuracy: 0.9306
37472/60000 [=================>............] - ETA: 42s - loss: 0.2282 - categorical_accuracy: 0.9306
37504/60000 [=================>............] - ETA: 42s - loss: 0.2281 - categorical_accuracy: 0.9306
37536/60000 [=================>............] - ETA: 42s - loss: 0.2279 - categorical_accuracy: 0.9307
37568/60000 [=================>............] - ETA: 42s - loss: 0.2278 - categorical_accuracy: 0.9307
37600/60000 [=================>............] - ETA: 42s - loss: 0.2276 - categorical_accuracy: 0.9307
37632/60000 [=================>............] - ETA: 42s - loss: 0.2276 - categorical_accuracy: 0.9308
37664/60000 [=================>............] - ETA: 42s - loss: 0.2274 - categorical_accuracy: 0.9308
37696/60000 [=================>............] - ETA: 42s - loss: 0.2273 - categorical_accuracy: 0.9308
37728/60000 [=================>............] - ETA: 42s - loss: 0.2272 - categorical_accuracy: 0.9308
37760/60000 [=================>............] - ETA: 42s - loss: 0.2271 - categorical_accuracy: 0.9309
37792/60000 [=================>............] - ETA: 42s - loss: 0.2269 - categorical_accuracy: 0.9309
37824/60000 [=================>............] - ETA: 42s - loss: 0.2270 - categorical_accuracy: 0.9309
37856/60000 [=================>............] - ETA: 42s - loss: 0.2269 - categorical_accuracy: 0.9309
37888/60000 [=================>............] - ETA: 42s - loss: 0.2268 - categorical_accuracy: 0.9310
37920/60000 [=================>............] - ETA: 42s - loss: 0.2268 - categorical_accuracy: 0.9310
37952/60000 [=================>............] - ETA: 41s - loss: 0.2267 - categorical_accuracy: 0.9310
37984/60000 [=================>............] - ETA: 41s - loss: 0.2265 - categorical_accuracy: 0.9311
38016/60000 [==================>...........] - ETA: 41s - loss: 0.2264 - categorical_accuracy: 0.9312
38048/60000 [==================>...........] - ETA: 41s - loss: 0.2262 - categorical_accuracy: 0.9312
38080/60000 [==================>...........] - ETA: 41s - loss: 0.2261 - categorical_accuracy: 0.9312
38112/60000 [==================>...........] - ETA: 41s - loss: 0.2261 - categorical_accuracy: 0.9313
38144/60000 [==================>...........] - ETA: 41s - loss: 0.2260 - categorical_accuracy: 0.9313
38176/60000 [==================>...........] - ETA: 41s - loss: 0.2258 - categorical_accuracy: 0.9313
38208/60000 [==================>...........] - ETA: 41s - loss: 0.2257 - categorical_accuracy: 0.9313
38240/60000 [==================>...........] - ETA: 41s - loss: 0.2257 - categorical_accuracy: 0.9313
38272/60000 [==================>...........] - ETA: 41s - loss: 0.2255 - categorical_accuracy: 0.9314
38304/60000 [==================>...........] - ETA: 41s - loss: 0.2255 - categorical_accuracy: 0.9314
38336/60000 [==================>...........] - ETA: 41s - loss: 0.2254 - categorical_accuracy: 0.9314
38368/60000 [==================>...........] - ETA: 41s - loss: 0.2253 - categorical_accuracy: 0.9314
38400/60000 [==================>...........] - ETA: 41s - loss: 0.2252 - categorical_accuracy: 0.9314
38432/60000 [==================>...........] - ETA: 41s - loss: 0.2252 - categorical_accuracy: 0.9314
38464/60000 [==================>...........] - ETA: 41s - loss: 0.2250 - categorical_accuracy: 0.9314
38496/60000 [==================>...........] - ETA: 40s - loss: 0.2249 - categorical_accuracy: 0.9315
38528/60000 [==================>...........] - ETA: 40s - loss: 0.2247 - categorical_accuracy: 0.9315
38560/60000 [==================>...........] - ETA: 40s - loss: 0.2247 - categorical_accuracy: 0.9316
38592/60000 [==================>...........] - ETA: 40s - loss: 0.2246 - categorical_accuracy: 0.9316
38624/60000 [==================>...........] - ETA: 40s - loss: 0.2246 - categorical_accuracy: 0.9316
38656/60000 [==================>...........] - ETA: 40s - loss: 0.2247 - categorical_accuracy: 0.9316
38688/60000 [==================>...........] - ETA: 40s - loss: 0.2245 - categorical_accuracy: 0.9317
38720/60000 [==================>...........] - ETA: 40s - loss: 0.2244 - categorical_accuracy: 0.9317
38752/60000 [==================>...........] - ETA: 40s - loss: 0.2242 - categorical_accuracy: 0.9317
38784/60000 [==================>...........] - ETA: 40s - loss: 0.2241 - categorical_accuracy: 0.9318
38816/60000 [==================>...........] - ETA: 40s - loss: 0.2239 - categorical_accuracy: 0.9318
38848/60000 [==================>...........] - ETA: 40s - loss: 0.2238 - categorical_accuracy: 0.9319
38880/60000 [==================>...........] - ETA: 40s - loss: 0.2236 - categorical_accuracy: 0.9319
38912/60000 [==================>...........] - ETA: 40s - loss: 0.2235 - categorical_accuracy: 0.9319
38944/60000 [==================>...........] - ETA: 40s - loss: 0.2234 - categorical_accuracy: 0.9320
38976/60000 [==================>...........] - ETA: 40s - loss: 0.2232 - categorical_accuracy: 0.9320
39008/60000 [==================>...........] - ETA: 39s - loss: 0.2231 - categorical_accuracy: 0.9321
39040/60000 [==================>...........] - ETA: 39s - loss: 0.2231 - categorical_accuracy: 0.9321
39072/60000 [==================>...........] - ETA: 39s - loss: 0.2230 - categorical_accuracy: 0.9321
39104/60000 [==================>...........] - ETA: 39s - loss: 0.2229 - categorical_accuracy: 0.9322
39136/60000 [==================>...........] - ETA: 39s - loss: 0.2227 - categorical_accuracy: 0.9322
39168/60000 [==================>...........] - ETA: 39s - loss: 0.2227 - categorical_accuracy: 0.9322
39200/60000 [==================>...........] - ETA: 39s - loss: 0.2227 - categorical_accuracy: 0.9322
39232/60000 [==================>...........] - ETA: 39s - loss: 0.2226 - categorical_accuracy: 0.9322
39264/60000 [==================>...........] - ETA: 39s - loss: 0.2226 - categorical_accuracy: 0.9323
39296/60000 [==================>...........] - ETA: 39s - loss: 0.2225 - categorical_accuracy: 0.9323
39328/60000 [==================>...........] - ETA: 39s - loss: 0.2224 - categorical_accuracy: 0.9323
39360/60000 [==================>...........] - ETA: 39s - loss: 0.2224 - categorical_accuracy: 0.9323
39392/60000 [==================>...........] - ETA: 39s - loss: 0.2224 - categorical_accuracy: 0.9323
39424/60000 [==================>...........] - ETA: 39s - loss: 0.2223 - categorical_accuracy: 0.9323
39456/60000 [==================>...........] - ETA: 39s - loss: 0.2222 - categorical_accuracy: 0.9324
39488/60000 [==================>...........] - ETA: 39s - loss: 0.2220 - categorical_accuracy: 0.9324
39520/60000 [==================>...........] - ETA: 38s - loss: 0.2218 - categorical_accuracy: 0.9325
39552/60000 [==================>...........] - ETA: 38s - loss: 0.2219 - categorical_accuracy: 0.9325
39584/60000 [==================>...........] - ETA: 38s - loss: 0.2219 - categorical_accuracy: 0.9324
39616/60000 [==================>...........] - ETA: 38s - loss: 0.2218 - categorical_accuracy: 0.9325
39648/60000 [==================>...........] - ETA: 38s - loss: 0.2217 - categorical_accuracy: 0.9325
39680/60000 [==================>...........] - ETA: 38s - loss: 0.2215 - categorical_accuracy: 0.9326
39712/60000 [==================>...........] - ETA: 38s - loss: 0.2215 - categorical_accuracy: 0.9326
39744/60000 [==================>...........] - ETA: 38s - loss: 0.2213 - categorical_accuracy: 0.9326
39776/60000 [==================>...........] - ETA: 38s - loss: 0.2211 - categorical_accuracy: 0.9327
39808/60000 [==================>...........] - ETA: 38s - loss: 0.2211 - categorical_accuracy: 0.9327
39840/60000 [==================>...........] - ETA: 38s - loss: 0.2211 - categorical_accuracy: 0.9328
39872/60000 [==================>...........] - ETA: 38s - loss: 0.2213 - categorical_accuracy: 0.9327
39904/60000 [==================>...........] - ETA: 38s - loss: 0.2212 - categorical_accuracy: 0.9328
39936/60000 [==================>...........] - ETA: 38s - loss: 0.2211 - categorical_accuracy: 0.9328
39968/60000 [==================>...........] - ETA: 38s - loss: 0.2210 - categorical_accuracy: 0.9328
40000/60000 [===================>..........] - ETA: 38s - loss: 0.2209 - categorical_accuracy: 0.9328
40032/60000 [===================>..........] - ETA: 38s - loss: 0.2208 - categorical_accuracy: 0.9328
40064/60000 [===================>..........] - ETA: 37s - loss: 0.2207 - categorical_accuracy: 0.9329
40096/60000 [===================>..........] - ETA: 37s - loss: 0.2205 - categorical_accuracy: 0.9329
40128/60000 [===================>..........] - ETA: 37s - loss: 0.2204 - categorical_accuracy: 0.9330
40160/60000 [===================>..........] - ETA: 37s - loss: 0.2203 - categorical_accuracy: 0.9330
40192/60000 [===================>..........] - ETA: 37s - loss: 0.2202 - categorical_accuracy: 0.9330
40224/60000 [===================>..........] - ETA: 37s - loss: 0.2203 - categorical_accuracy: 0.9330
40256/60000 [===================>..........] - ETA: 37s - loss: 0.2202 - categorical_accuracy: 0.9331
40288/60000 [===================>..........] - ETA: 37s - loss: 0.2200 - categorical_accuracy: 0.9331
40320/60000 [===================>..........] - ETA: 37s - loss: 0.2199 - categorical_accuracy: 0.9332
40352/60000 [===================>..........] - ETA: 37s - loss: 0.2198 - categorical_accuracy: 0.9332
40384/60000 [===================>..........] - ETA: 37s - loss: 0.2199 - categorical_accuracy: 0.9332
40416/60000 [===================>..........] - ETA: 37s - loss: 0.2198 - categorical_accuracy: 0.9332
40448/60000 [===================>..........] - ETA: 37s - loss: 0.2197 - categorical_accuracy: 0.9332
40480/60000 [===================>..........] - ETA: 37s - loss: 0.2196 - categorical_accuracy: 0.9332
40512/60000 [===================>..........] - ETA: 37s - loss: 0.2195 - categorical_accuracy: 0.9333
40544/60000 [===================>..........] - ETA: 37s - loss: 0.2193 - categorical_accuracy: 0.9333
40576/60000 [===================>..........] - ETA: 36s - loss: 0.2192 - categorical_accuracy: 0.9334
40608/60000 [===================>..........] - ETA: 36s - loss: 0.2190 - categorical_accuracy: 0.9334
40640/60000 [===================>..........] - ETA: 36s - loss: 0.2191 - categorical_accuracy: 0.9334
40672/60000 [===================>..........] - ETA: 36s - loss: 0.2189 - categorical_accuracy: 0.9335
40704/60000 [===================>..........] - ETA: 36s - loss: 0.2188 - categorical_accuracy: 0.9335
40736/60000 [===================>..........] - ETA: 36s - loss: 0.2187 - categorical_accuracy: 0.9335
40768/60000 [===================>..........] - ETA: 36s - loss: 0.2186 - categorical_accuracy: 0.9336
40800/60000 [===================>..........] - ETA: 36s - loss: 0.2186 - categorical_accuracy: 0.9336
40832/60000 [===================>..........] - ETA: 36s - loss: 0.2184 - categorical_accuracy: 0.9336
40864/60000 [===================>..........] - ETA: 36s - loss: 0.2182 - categorical_accuracy: 0.9337
40896/60000 [===================>..........] - ETA: 36s - loss: 0.2181 - categorical_accuracy: 0.9337
40928/60000 [===================>..........] - ETA: 36s - loss: 0.2179 - categorical_accuracy: 0.9338
40960/60000 [===================>..........] - ETA: 36s - loss: 0.2179 - categorical_accuracy: 0.9338
40992/60000 [===================>..........] - ETA: 36s - loss: 0.2178 - categorical_accuracy: 0.9338
41024/60000 [===================>..........] - ETA: 36s - loss: 0.2177 - categorical_accuracy: 0.9338
41056/60000 [===================>..........] - ETA: 36s - loss: 0.2176 - categorical_accuracy: 0.9339
41088/60000 [===================>..........] - ETA: 35s - loss: 0.2176 - categorical_accuracy: 0.9339
41120/60000 [===================>..........] - ETA: 35s - loss: 0.2175 - categorical_accuracy: 0.9339
41152/60000 [===================>..........] - ETA: 35s - loss: 0.2174 - categorical_accuracy: 0.9339
41184/60000 [===================>..........] - ETA: 35s - loss: 0.2174 - categorical_accuracy: 0.9339
41216/60000 [===================>..........] - ETA: 35s - loss: 0.2174 - categorical_accuracy: 0.9339
41248/60000 [===================>..........] - ETA: 35s - loss: 0.2174 - categorical_accuracy: 0.9339
41280/60000 [===================>..........] - ETA: 35s - loss: 0.2174 - categorical_accuracy: 0.9339
41312/60000 [===================>..........] - ETA: 35s - loss: 0.2172 - categorical_accuracy: 0.9340
41344/60000 [===================>..........] - ETA: 35s - loss: 0.2171 - categorical_accuracy: 0.9340
41376/60000 [===================>..........] - ETA: 35s - loss: 0.2169 - categorical_accuracy: 0.9341
41408/60000 [===================>..........] - ETA: 35s - loss: 0.2168 - categorical_accuracy: 0.9341
41440/60000 [===================>..........] - ETA: 35s - loss: 0.2167 - categorical_accuracy: 0.9341
41472/60000 [===================>..........] - ETA: 35s - loss: 0.2166 - categorical_accuracy: 0.9342
41504/60000 [===================>..........] - ETA: 35s - loss: 0.2164 - categorical_accuracy: 0.9342
41536/60000 [===================>..........] - ETA: 35s - loss: 0.2163 - categorical_accuracy: 0.9342
41568/60000 [===================>..........] - ETA: 35s - loss: 0.2162 - categorical_accuracy: 0.9343
41600/60000 [===================>..........] - ETA: 35s - loss: 0.2161 - categorical_accuracy: 0.9343
41632/60000 [===================>..........] - ETA: 34s - loss: 0.2159 - categorical_accuracy: 0.9344
41664/60000 [===================>..........] - ETA: 34s - loss: 0.2158 - categorical_accuracy: 0.9344
41696/60000 [===================>..........] - ETA: 34s - loss: 0.2157 - categorical_accuracy: 0.9345
41728/60000 [===================>..........] - ETA: 34s - loss: 0.2155 - categorical_accuracy: 0.9345
41760/60000 [===================>..........] - ETA: 34s - loss: 0.2154 - categorical_accuracy: 0.9346
41792/60000 [===================>..........] - ETA: 34s - loss: 0.2153 - categorical_accuracy: 0.9346
41824/60000 [===================>..........] - ETA: 34s - loss: 0.2152 - categorical_accuracy: 0.9346
41856/60000 [===================>..........] - ETA: 34s - loss: 0.2150 - categorical_accuracy: 0.9347
41888/60000 [===================>..........] - ETA: 34s - loss: 0.2149 - categorical_accuracy: 0.9347
41920/60000 [===================>..........] - ETA: 34s - loss: 0.2147 - categorical_accuracy: 0.9348
41952/60000 [===================>..........] - ETA: 34s - loss: 0.2146 - categorical_accuracy: 0.9348
41984/60000 [===================>..........] - ETA: 34s - loss: 0.2144 - categorical_accuracy: 0.9349
42016/60000 [====================>.........] - ETA: 34s - loss: 0.2143 - categorical_accuracy: 0.9349
42048/60000 [====================>.........] - ETA: 34s - loss: 0.2143 - categorical_accuracy: 0.9349
42080/60000 [====================>.........] - ETA: 34s - loss: 0.2141 - categorical_accuracy: 0.9350
42112/60000 [====================>.........] - ETA: 34s - loss: 0.2140 - categorical_accuracy: 0.9350
42144/60000 [====================>.........] - ETA: 33s - loss: 0.2139 - categorical_accuracy: 0.9351
42176/60000 [====================>.........] - ETA: 33s - loss: 0.2139 - categorical_accuracy: 0.9351
42208/60000 [====================>.........] - ETA: 33s - loss: 0.2139 - categorical_accuracy: 0.9351
42240/60000 [====================>.........] - ETA: 33s - loss: 0.2138 - categorical_accuracy: 0.9351
42272/60000 [====================>.........] - ETA: 33s - loss: 0.2138 - categorical_accuracy: 0.9351
42304/60000 [====================>.........] - ETA: 33s - loss: 0.2136 - categorical_accuracy: 0.9352
42336/60000 [====================>.........] - ETA: 33s - loss: 0.2135 - categorical_accuracy: 0.9352
42368/60000 [====================>.........] - ETA: 33s - loss: 0.2135 - categorical_accuracy: 0.9352
42400/60000 [====================>.........] - ETA: 33s - loss: 0.2135 - categorical_accuracy: 0.9352
42432/60000 [====================>.........] - ETA: 33s - loss: 0.2134 - categorical_accuracy: 0.9353
42464/60000 [====================>.........] - ETA: 33s - loss: 0.2132 - categorical_accuracy: 0.9353
42496/60000 [====================>.........] - ETA: 33s - loss: 0.2132 - categorical_accuracy: 0.9353
42528/60000 [====================>.........] - ETA: 33s - loss: 0.2132 - categorical_accuracy: 0.9353
42560/60000 [====================>.........] - ETA: 33s - loss: 0.2131 - categorical_accuracy: 0.9354
42592/60000 [====================>.........] - ETA: 33s - loss: 0.2130 - categorical_accuracy: 0.9354
42624/60000 [====================>.........] - ETA: 33s - loss: 0.2129 - categorical_accuracy: 0.9354
42656/60000 [====================>.........] - ETA: 32s - loss: 0.2128 - categorical_accuracy: 0.9354
42688/60000 [====================>.........] - ETA: 32s - loss: 0.2127 - categorical_accuracy: 0.9355
42720/60000 [====================>.........] - ETA: 32s - loss: 0.2125 - categorical_accuracy: 0.9355
42752/60000 [====================>.........] - ETA: 32s - loss: 0.2128 - categorical_accuracy: 0.9355
42784/60000 [====================>.........] - ETA: 32s - loss: 0.2127 - categorical_accuracy: 0.9355
42816/60000 [====================>.........] - ETA: 32s - loss: 0.2125 - categorical_accuracy: 0.9356
42848/60000 [====================>.........] - ETA: 32s - loss: 0.2125 - categorical_accuracy: 0.9356
42880/60000 [====================>.........] - ETA: 32s - loss: 0.2124 - categorical_accuracy: 0.9356
42912/60000 [====================>.........] - ETA: 32s - loss: 0.2122 - categorical_accuracy: 0.9357
42944/60000 [====================>.........] - ETA: 32s - loss: 0.2121 - categorical_accuracy: 0.9357
42976/60000 [====================>.........] - ETA: 32s - loss: 0.2119 - categorical_accuracy: 0.9358
43008/60000 [====================>.........] - ETA: 32s - loss: 0.2118 - categorical_accuracy: 0.9358
43040/60000 [====================>.........] - ETA: 32s - loss: 0.2117 - categorical_accuracy: 0.9358
43072/60000 [====================>.........] - ETA: 32s - loss: 0.2116 - categorical_accuracy: 0.9359
43104/60000 [====================>.........] - ETA: 32s - loss: 0.2115 - categorical_accuracy: 0.9359
43136/60000 [====================>.........] - ETA: 32s - loss: 0.2114 - categorical_accuracy: 0.9359
43168/60000 [====================>.........] - ETA: 32s - loss: 0.2113 - categorical_accuracy: 0.9359
43200/60000 [====================>.........] - ETA: 31s - loss: 0.2112 - categorical_accuracy: 0.9359
43232/60000 [====================>.........] - ETA: 31s - loss: 0.2111 - categorical_accuracy: 0.9359
43264/60000 [====================>.........] - ETA: 31s - loss: 0.2110 - categorical_accuracy: 0.9360
43296/60000 [====================>.........] - ETA: 31s - loss: 0.2109 - categorical_accuracy: 0.9360
43328/60000 [====================>.........] - ETA: 31s - loss: 0.2108 - categorical_accuracy: 0.9360
43360/60000 [====================>.........] - ETA: 31s - loss: 0.2106 - categorical_accuracy: 0.9361
43392/60000 [====================>.........] - ETA: 31s - loss: 0.2105 - categorical_accuracy: 0.9361
43424/60000 [====================>.........] - ETA: 31s - loss: 0.2104 - categorical_accuracy: 0.9361
43456/60000 [====================>.........] - ETA: 31s - loss: 0.2103 - categorical_accuracy: 0.9362
43488/60000 [====================>.........] - ETA: 31s - loss: 0.2102 - categorical_accuracy: 0.9362
43520/60000 [====================>.........] - ETA: 31s - loss: 0.2101 - categorical_accuracy: 0.9362
43552/60000 [====================>.........] - ETA: 31s - loss: 0.2102 - categorical_accuracy: 0.9362
43584/60000 [====================>.........] - ETA: 31s - loss: 0.2101 - categorical_accuracy: 0.9362
43616/60000 [====================>.........] - ETA: 31s - loss: 0.2100 - categorical_accuracy: 0.9362
43648/60000 [====================>.........] - ETA: 31s - loss: 0.2100 - categorical_accuracy: 0.9362
43680/60000 [====================>.........] - ETA: 31s - loss: 0.2099 - categorical_accuracy: 0.9362
43712/60000 [====================>.........] - ETA: 30s - loss: 0.2098 - categorical_accuracy: 0.9362
43744/60000 [====================>.........] - ETA: 30s - loss: 0.2097 - categorical_accuracy: 0.9363
43776/60000 [====================>.........] - ETA: 30s - loss: 0.2097 - categorical_accuracy: 0.9363
43808/60000 [====================>.........] - ETA: 30s - loss: 0.2095 - categorical_accuracy: 0.9363
43840/60000 [====================>.........] - ETA: 30s - loss: 0.2094 - categorical_accuracy: 0.9364
43872/60000 [====================>.........] - ETA: 30s - loss: 0.2093 - categorical_accuracy: 0.9364
43904/60000 [====================>.........] - ETA: 30s - loss: 0.2092 - categorical_accuracy: 0.9364
43936/60000 [====================>.........] - ETA: 30s - loss: 0.2090 - categorical_accuracy: 0.9365
43968/60000 [====================>.........] - ETA: 30s - loss: 0.2090 - categorical_accuracy: 0.9365
44000/60000 [=====================>........] - ETA: 30s - loss: 0.2089 - categorical_accuracy: 0.9365
44032/60000 [=====================>........] - ETA: 30s - loss: 0.2087 - categorical_accuracy: 0.9365
44064/60000 [=====================>........] - ETA: 30s - loss: 0.2087 - categorical_accuracy: 0.9366
44096/60000 [=====================>........] - ETA: 30s - loss: 0.2088 - categorical_accuracy: 0.9366
44128/60000 [=====================>........] - ETA: 30s - loss: 0.2087 - categorical_accuracy: 0.9366
44160/60000 [=====================>........] - ETA: 30s - loss: 0.2086 - categorical_accuracy: 0.9366
44192/60000 [=====================>........] - ETA: 30s - loss: 0.2085 - categorical_accuracy: 0.9367
44224/60000 [=====================>........] - ETA: 30s - loss: 0.2084 - categorical_accuracy: 0.9367
44256/60000 [=====================>........] - ETA: 29s - loss: 0.2083 - categorical_accuracy: 0.9367
44288/60000 [=====================>........] - ETA: 29s - loss: 0.2081 - categorical_accuracy: 0.9368
44320/60000 [=====================>........] - ETA: 29s - loss: 0.2080 - categorical_accuracy: 0.9368
44352/60000 [=====================>........] - ETA: 29s - loss: 0.2079 - categorical_accuracy: 0.9369
44384/60000 [=====================>........] - ETA: 29s - loss: 0.2078 - categorical_accuracy: 0.9369
44416/60000 [=====================>........] - ETA: 29s - loss: 0.2077 - categorical_accuracy: 0.9369
44448/60000 [=====================>........] - ETA: 29s - loss: 0.2076 - categorical_accuracy: 0.9369
44480/60000 [=====================>........] - ETA: 29s - loss: 0.2075 - categorical_accuracy: 0.9369
44512/60000 [=====================>........] - ETA: 29s - loss: 0.2074 - categorical_accuracy: 0.9370
44544/60000 [=====================>........] - ETA: 29s - loss: 0.2073 - categorical_accuracy: 0.9370
44576/60000 [=====================>........] - ETA: 29s - loss: 0.2072 - categorical_accuracy: 0.9370
44608/60000 [=====================>........] - ETA: 29s - loss: 0.2071 - categorical_accuracy: 0.9370
44640/60000 [=====================>........] - ETA: 29s - loss: 0.2071 - categorical_accuracy: 0.9370
44672/60000 [=====================>........] - ETA: 29s - loss: 0.2070 - categorical_accuracy: 0.9371
44704/60000 [=====================>........] - ETA: 29s - loss: 0.2068 - categorical_accuracy: 0.9371
44736/60000 [=====================>........] - ETA: 29s - loss: 0.2067 - categorical_accuracy: 0.9371
44768/60000 [=====================>........] - ETA: 28s - loss: 0.2067 - categorical_accuracy: 0.9371
44800/60000 [=====================>........] - ETA: 28s - loss: 0.2066 - categorical_accuracy: 0.9371
44832/60000 [=====================>........] - ETA: 28s - loss: 0.2065 - categorical_accuracy: 0.9372
44864/60000 [=====================>........] - ETA: 28s - loss: 0.2063 - categorical_accuracy: 0.9372
44896/60000 [=====================>........] - ETA: 28s - loss: 0.2063 - categorical_accuracy: 0.9373
44928/60000 [=====================>........] - ETA: 28s - loss: 0.2061 - categorical_accuracy: 0.9373
44960/60000 [=====================>........] - ETA: 28s - loss: 0.2061 - categorical_accuracy: 0.9373
44992/60000 [=====================>........] - ETA: 28s - loss: 0.2059 - categorical_accuracy: 0.9373
45024/60000 [=====================>........] - ETA: 28s - loss: 0.2058 - categorical_accuracy: 0.9374
45056/60000 [=====================>........] - ETA: 28s - loss: 0.2058 - categorical_accuracy: 0.9374
45088/60000 [=====================>........] - ETA: 28s - loss: 0.2057 - categorical_accuracy: 0.9374
45120/60000 [=====================>........] - ETA: 28s - loss: 0.2056 - categorical_accuracy: 0.9375
45152/60000 [=====================>........] - ETA: 28s - loss: 0.2056 - categorical_accuracy: 0.9375
45184/60000 [=====================>........] - ETA: 28s - loss: 0.2054 - categorical_accuracy: 0.9375
45216/60000 [=====================>........] - ETA: 28s - loss: 0.2053 - categorical_accuracy: 0.9376
45248/60000 [=====================>........] - ETA: 28s - loss: 0.2053 - categorical_accuracy: 0.9376
45280/60000 [=====================>........] - ETA: 28s - loss: 0.2053 - categorical_accuracy: 0.9376
45312/60000 [=====================>........] - ETA: 27s - loss: 0.2052 - categorical_accuracy: 0.9376
45344/60000 [=====================>........] - ETA: 27s - loss: 0.2052 - categorical_accuracy: 0.9376
45376/60000 [=====================>........] - ETA: 27s - loss: 0.2050 - categorical_accuracy: 0.9376
45408/60000 [=====================>........] - ETA: 27s - loss: 0.2049 - categorical_accuracy: 0.9377
45440/60000 [=====================>........] - ETA: 27s - loss: 0.2048 - categorical_accuracy: 0.9377
45472/60000 [=====================>........] - ETA: 27s - loss: 0.2048 - categorical_accuracy: 0.9377
45504/60000 [=====================>........] - ETA: 27s - loss: 0.2048 - categorical_accuracy: 0.9377
45536/60000 [=====================>........] - ETA: 27s - loss: 0.2047 - categorical_accuracy: 0.9377
45568/60000 [=====================>........] - ETA: 27s - loss: 0.2046 - categorical_accuracy: 0.9377
45600/60000 [=====================>........] - ETA: 27s - loss: 0.2046 - categorical_accuracy: 0.9377
45632/60000 [=====================>........] - ETA: 27s - loss: 0.2045 - categorical_accuracy: 0.9377
45664/60000 [=====================>........] - ETA: 27s - loss: 0.2044 - categorical_accuracy: 0.9378
45696/60000 [=====================>........] - ETA: 27s - loss: 0.2043 - categorical_accuracy: 0.9378
45728/60000 [=====================>........] - ETA: 27s - loss: 0.2044 - categorical_accuracy: 0.9378
45760/60000 [=====================>........] - ETA: 27s - loss: 0.2043 - categorical_accuracy: 0.9378
45792/60000 [=====================>........] - ETA: 27s - loss: 0.2042 - categorical_accuracy: 0.9378
45824/60000 [=====================>........] - ETA: 26s - loss: 0.2041 - categorical_accuracy: 0.9378
45856/60000 [=====================>........] - ETA: 26s - loss: 0.2041 - categorical_accuracy: 0.9378
45888/60000 [=====================>........] - ETA: 26s - loss: 0.2040 - categorical_accuracy: 0.9379
45920/60000 [=====================>........] - ETA: 26s - loss: 0.2039 - categorical_accuracy: 0.9379
45952/60000 [=====================>........] - ETA: 26s - loss: 0.2039 - categorical_accuracy: 0.9379
45984/60000 [=====================>........] - ETA: 26s - loss: 0.2037 - categorical_accuracy: 0.9380
46016/60000 [======================>.......] - ETA: 26s - loss: 0.2036 - categorical_accuracy: 0.9380
46048/60000 [======================>.......] - ETA: 26s - loss: 0.2036 - categorical_accuracy: 0.9380
46080/60000 [======================>.......] - ETA: 26s - loss: 0.2034 - categorical_accuracy: 0.9381
46112/60000 [======================>.......] - ETA: 26s - loss: 0.2033 - categorical_accuracy: 0.9381
46144/60000 [======================>.......] - ETA: 26s - loss: 0.2032 - categorical_accuracy: 0.9381
46176/60000 [======================>.......] - ETA: 26s - loss: 0.2031 - categorical_accuracy: 0.9381
46208/60000 [======================>.......] - ETA: 26s - loss: 0.2030 - categorical_accuracy: 0.9382
46240/60000 [======================>.......] - ETA: 26s - loss: 0.2030 - categorical_accuracy: 0.9382
46272/60000 [======================>.......] - ETA: 26s - loss: 0.2029 - categorical_accuracy: 0.9382
46304/60000 [======================>.......] - ETA: 26s - loss: 0.2028 - categorical_accuracy: 0.9382
46336/60000 [======================>.......] - ETA: 25s - loss: 0.2027 - categorical_accuracy: 0.9383
46368/60000 [======================>.......] - ETA: 25s - loss: 0.2026 - categorical_accuracy: 0.9383
46400/60000 [======================>.......] - ETA: 25s - loss: 0.2025 - categorical_accuracy: 0.9383
46432/60000 [======================>.......] - ETA: 25s - loss: 0.2026 - categorical_accuracy: 0.9383
46464/60000 [======================>.......] - ETA: 25s - loss: 0.2025 - categorical_accuracy: 0.9384
46496/60000 [======================>.......] - ETA: 25s - loss: 0.2024 - categorical_accuracy: 0.9384
46528/60000 [======================>.......] - ETA: 25s - loss: 0.2023 - categorical_accuracy: 0.9384
46560/60000 [======================>.......] - ETA: 25s - loss: 0.2022 - categorical_accuracy: 0.9384
46592/60000 [======================>.......] - ETA: 25s - loss: 0.2021 - categorical_accuracy: 0.9385
46624/60000 [======================>.......] - ETA: 25s - loss: 0.2020 - categorical_accuracy: 0.9385
46656/60000 [======================>.......] - ETA: 25s - loss: 0.2020 - categorical_accuracy: 0.9385
46688/60000 [======================>.......] - ETA: 25s - loss: 0.2019 - categorical_accuracy: 0.9385
46720/60000 [======================>.......] - ETA: 25s - loss: 0.2018 - categorical_accuracy: 0.9386
46752/60000 [======================>.......] - ETA: 25s - loss: 0.2018 - categorical_accuracy: 0.9386
46784/60000 [======================>.......] - ETA: 25s - loss: 0.2016 - categorical_accuracy: 0.9386
46816/60000 [======================>.......] - ETA: 25s - loss: 0.2015 - categorical_accuracy: 0.9386
46848/60000 [======================>.......] - ETA: 25s - loss: 0.2014 - categorical_accuracy: 0.9387
46880/60000 [======================>.......] - ETA: 24s - loss: 0.2013 - categorical_accuracy: 0.9387
46912/60000 [======================>.......] - ETA: 24s - loss: 0.2012 - categorical_accuracy: 0.9387
46944/60000 [======================>.......] - ETA: 24s - loss: 0.2011 - categorical_accuracy: 0.9388
46976/60000 [======================>.......] - ETA: 24s - loss: 0.2010 - categorical_accuracy: 0.9388
47008/60000 [======================>.......] - ETA: 24s - loss: 0.2009 - categorical_accuracy: 0.9388
47040/60000 [======================>.......] - ETA: 24s - loss: 0.2008 - categorical_accuracy: 0.9389
47072/60000 [======================>.......] - ETA: 24s - loss: 0.2007 - categorical_accuracy: 0.9389
47104/60000 [======================>.......] - ETA: 24s - loss: 0.2007 - categorical_accuracy: 0.9389
47136/60000 [======================>.......] - ETA: 24s - loss: 0.2006 - categorical_accuracy: 0.9389
47168/60000 [======================>.......] - ETA: 24s - loss: 0.2005 - categorical_accuracy: 0.9389
47200/60000 [======================>.......] - ETA: 24s - loss: 0.2004 - categorical_accuracy: 0.9390
47232/60000 [======================>.......] - ETA: 24s - loss: 0.2003 - categorical_accuracy: 0.9390
47264/60000 [======================>.......] - ETA: 24s - loss: 0.2002 - categorical_accuracy: 0.9390
47296/60000 [======================>.......] - ETA: 24s - loss: 0.2001 - categorical_accuracy: 0.9391
47328/60000 [======================>.......] - ETA: 24s - loss: 0.2000 - categorical_accuracy: 0.9391
47360/60000 [======================>.......] - ETA: 24s - loss: 0.1999 - categorical_accuracy: 0.9391
47392/60000 [======================>.......] - ETA: 23s - loss: 0.1999 - categorical_accuracy: 0.9391
47424/60000 [======================>.......] - ETA: 23s - loss: 0.1999 - categorical_accuracy: 0.9391
47456/60000 [======================>.......] - ETA: 23s - loss: 0.1999 - categorical_accuracy: 0.9391
47488/60000 [======================>.......] - ETA: 23s - loss: 0.1998 - categorical_accuracy: 0.9392
47520/60000 [======================>.......] - ETA: 23s - loss: 0.1999 - categorical_accuracy: 0.9391
47552/60000 [======================>.......] - ETA: 23s - loss: 0.2001 - categorical_accuracy: 0.9391
47584/60000 [======================>.......] - ETA: 23s - loss: 0.2001 - categorical_accuracy: 0.9391
47616/60000 [======================>.......] - ETA: 23s - loss: 0.2001 - categorical_accuracy: 0.9391
47648/60000 [======================>.......] - ETA: 23s - loss: 0.2000 - categorical_accuracy: 0.9391
47680/60000 [======================>.......] - ETA: 23s - loss: 0.2000 - categorical_accuracy: 0.9391
47712/60000 [======================>.......] - ETA: 23s - loss: 0.1998 - categorical_accuracy: 0.9392
47744/60000 [======================>.......] - ETA: 23s - loss: 0.1998 - categorical_accuracy: 0.9392
47776/60000 [======================>.......] - ETA: 23s - loss: 0.1997 - categorical_accuracy: 0.9392
47808/60000 [======================>.......] - ETA: 23s - loss: 0.1996 - categorical_accuracy: 0.9393
47840/60000 [======================>.......] - ETA: 23s - loss: 0.1995 - categorical_accuracy: 0.9393
47872/60000 [======================>.......] - ETA: 23s - loss: 0.1995 - categorical_accuracy: 0.9393
47904/60000 [======================>.......] - ETA: 22s - loss: 0.1994 - categorical_accuracy: 0.9393
47936/60000 [======================>.......] - ETA: 22s - loss: 0.1993 - categorical_accuracy: 0.9393
47968/60000 [======================>.......] - ETA: 22s - loss: 0.1993 - categorical_accuracy: 0.9393
48000/60000 [=======================>......] - ETA: 22s - loss: 0.1991 - categorical_accuracy: 0.9394
48032/60000 [=======================>......] - ETA: 22s - loss: 0.1991 - categorical_accuracy: 0.9394
48064/60000 [=======================>......] - ETA: 22s - loss: 0.1990 - categorical_accuracy: 0.9394
48096/60000 [=======================>......] - ETA: 22s - loss: 0.1989 - categorical_accuracy: 0.9394
48128/60000 [=======================>......] - ETA: 22s - loss: 0.1989 - categorical_accuracy: 0.9394
48160/60000 [=======================>......] - ETA: 22s - loss: 0.1988 - categorical_accuracy: 0.9395
48192/60000 [=======================>......] - ETA: 22s - loss: 0.1987 - categorical_accuracy: 0.9395
48224/60000 [=======================>......] - ETA: 22s - loss: 0.1986 - categorical_accuracy: 0.9395
48256/60000 [=======================>......] - ETA: 22s - loss: 0.1985 - categorical_accuracy: 0.9395
48288/60000 [=======================>......] - ETA: 22s - loss: 0.1985 - categorical_accuracy: 0.9396
48320/60000 [=======================>......] - ETA: 22s - loss: 0.1985 - categorical_accuracy: 0.9395
48352/60000 [=======================>......] - ETA: 22s - loss: 0.1986 - categorical_accuracy: 0.9395
48384/60000 [=======================>......] - ETA: 22s - loss: 0.1986 - categorical_accuracy: 0.9395
48416/60000 [=======================>......] - ETA: 22s - loss: 0.1985 - categorical_accuracy: 0.9396
48448/60000 [=======================>......] - ETA: 21s - loss: 0.1986 - categorical_accuracy: 0.9395
48480/60000 [=======================>......] - ETA: 21s - loss: 0.1985 - categorical_accuracy: 0.9396
48512/60000 [=======================>......] - ETA: 21s - loss: 0.1984 - categorical_accuracy: 0.9396
48544/60000 [=======================>......] - ETA: 21s - loss: 0.1984 - categorical_accuracy: 0.9396
48576/60000 [=======================>......] - ETA: 21s - loss: 0.1983 - categorical_accuracy: 0.9396
48608/60000 [=======================>......] - ETA: 21s - loss: 0.1982 - categorical_accuracy: 0.9397
48640/60000 [=======================>......] - ETA: 21s - loss: 0.1982 - categorical_accuracy: 0.9396
48672/60000 [=======================>......] - ETA: 21s - loss: 0.1981 - categorical_accuracy: 0.9397
48704/60000 [=======================>......] - ETA: 21s - loss: 0.1980 - categorical_accuracy: 0.9397
48736/60000 [=======================>......] - ETA: 21s - loss: 0.1979 - categorical_accuracy: 0.9397
48768/60000 [=======================>......] - ETA: 21s - loss: 0.1979 - categorical_accuracy: 0.9398
48800/60000 [=======================>......] - ETA: 21s - loss: 0.1979 - categorical_accuracy: 0.9398
48832/60000 [=======================>......] - ETA: 21s - loss: 0.1978 - categorical_accuracy: 0.9398
48864/60000 [=======================>......] - ETA: 21s - loss: 0.1977 - categorical_accuracy: 0.9399
48896/60000 [=======================>......] - ETA: 21s - loss: 0.1977 - categorical_accuracy: 0.9399
48928/60000 [=======================>......] - ETA: 21s - loss: 0.1976 - categorical_accuracy: 0.9399
48960/60000 [=======================>......] - ETA: 20s - loss: 0.1974 - categorical_accuracy: 0.9399
48992/60000 [=======================>......] - ETA: 20s - loss: 0.1975 - categorical_accuracy: 0.9399
49024/60000 [=======================>......] - ETA: 20s - loss: 0.1975 - categorical_accuracy: 0.9399
49056/60000 [=======================>......] - ETA: 20s - loss: 0.1975 - categorical_accuracy: 0.9399
49088/60000 [=======================>......] - ETA: 20s - loss: 0.1976 - categorical_accuracy: 0.9399
49120/60000 [=======================>......] - ETA: 20s - loss: 0.1975 - categorical_accuracy: 0.9399
49152/60000 [=======================>......] - ETA: 20s - loss: 0.1975 - categorical_accuracy: 0.9400
49184/60000 [=======================>......] - ETA: 20s - loss: 0.1974 - categorical_accuracy: 0.9400
49216/60000 [=======================>......] - ETA: 20s - loss: 0.1973 - categorical_accuracy: 0.9400
49248/60000 [=======================>......] - ETA: 20s - loss: 0.1973 - categorical_accuracy: 0.9400
49280/60000 [=======================>......] - ETA: 20s - loss: 0.1972 - categorical_accuracy: 0.9400
49312/60000 [=======================>......] - ETA: 20s - loss: 0.1971 - categorical_accuracy: 0.9401
49344/60000 [=======================>......] - ETA: 20s - loss: 0.1971 - categorical_accuracy: 0.9401
49376/60000 [=======================>......] - ETA: 20s - loss: 0.1970 - categorical_accuracy: 0.9401
49408/60000 [=======================>......] - ETA: 20s - loss: 0.1970 - categorical_accuracy: 0.9401
49440/60000 [=======================>......] - ETA: 20s - loss: 0.1970 - categorical_accuracy: 0.9401
49472/60000 [=======================>......] - ETA: 20s - loss: 0.1969 - categorical_accuracy: 0.9402
49504/60000 [=======================>......] - ETA: 19s - loss: 0.1968 - categorical_accuracy: 0.9402
49536/60000 [=======================>......] - ETA: 19s - loss: 0.1968 - categorical_accuracy: 0.9402
49568/60000 [=======================>......] - ETA: 19s - loss: 0.1967 - categorical_accuracy: 0.9402
49600/60000 [=======================>......] - ETA: 19s - loss: 0.1966 - categorical_accuracy: 0.9403
49632/60000 [=======================>......] - ETA: 19s - loss: 0.1965 - categorical_accuracy: 0.9403
49664/60000 [=======================>......] - ETA: 19s - loss: 0.1964 - categorical_accuracy: 0.9403
49696/60000 [=======================>......] - ETA: 19s - loss: 0.1963 - categorical_accuracy: 0.9404
49728/60000 [=======================>......] - ETA: 19s - loss: 0.1962 - categorical_accuracy: 0.9404
49760/60000 [=======================>......] - ETA: 19s - loss: 0.1962 - categorical_accuracy: 0.9404
49792/60000 [=======================>......] - ETA: 19s - loss: 0.1961 - categorical_accuracy: 0.9405
49824/60000 [=======================>......] - ETA: 19s - loss: 0.1960 - categorical_accuracy: 0.9405
49856/60000 [=======================>......] - ETA: 19s - loss: 0.1959 - categorical_accuracy: 0.9405
49888/60000 [=======================>......] - ETA: 19s - loss: 0.1958 - categorical_accuracy: 0.9405
49920/60000 [=======================>......] - ETA: 19s - loss: 0.1958 - categorical_accuracy: 0.9405
49952/60000 [=======================>......] - ETA: 19s - loss: 0.1957 - categorical_accuracy: 0.9406
49984/60000 [=======================>......] - ETA: 19s - loss: 0.1956 - categorical_accuracy: 0.9406
50016/60000 [========================>.....] - ETA: 18s - loss: 0.1955 - categorical_accuracy: 0.9406
50048/60000 [========================>.....] - ETA: 18s - loss: 0.1954 - categorical_accuracy: 0.9407
50080/60000 [========================>.....] - ETA: 18s - loss: 0.1953 - categorical_accuracy: 0.9407
50112/60000 [========================>.....] - ETA: 18s - loss: 0.1954 - categorical_accuracy: 0.9407
50144/60000 [========================>.....] - ETA: 18s - loss: 0.1953 - categorical_accuracy: 0.9407
50176/60000 [========================>.....] - ETA: 18s - loss: 0.1952 - categorical_accuracy: 0.9407
50208/60000 [========================>.....] - ETA: 18s - loss: 0.1951 - categorical_accuracy: 0.9408
50240/60000 [========================>.....] - ETA: 18s - loss: 0.1951 - categorical_accuracy: 0.9408
50272/60000 [========================>.....] - ETA: 18s - loss: 0.1951 - categorical_accuracy: 0.9408
50304/60000 [========================>.....] - ETA: 18s - loss: 0.1950 - categorical_accuracy: 0.9408
50336/60000 [========================>.....] - ETA: 18s - loss: 0.1949 - categorical_accuracy: 0.9409
50368/60000 [========================>.....] - ETA: 18s - loss: 0.1948 - categorical_accuracy: 0.9409
50400/60000 [========================>.....] - ETA: 18s - loss: 0.1947 - categorical_accuracy: 0.9409
50432/60000 [========================>.....] - ETA: 18s - loss: 0.1946 - categorical_accuracy: 0.9410
50464/60000 [========================>.....] - ETA: 18s - loss: 0.1946 - categorical_accuracy: 0.9410
50496/60000 [========================>.....] - ETA: 18s - loss: 0.1945 - categorical_accuracy: 0.9410
50528/60000 [========================>.....] - ETA: 18s - loss: 0.1944 - categorical_accuracy: 0.9410
50560/60000 [========================>.....] - ETA: 17s - loss: 0.1945 - categorical_accuracy: 0.9410
50592/60000 [========================>.....] - ETA: 17s - loss: 0.1944 - categorical_accuracy: 0.9411
50624/60000 [========================>.....] - ETA: 17s - loss: 0.1944 - categorical_accuracy: 0.9411
50656/60000 [========================>.....] - ETA: 17s - loss: 0.1944 - categorical_accuracy: 0.9411
50688/60000 [========================>.....] - ETA: 17s - loss: 0.1943 - categorical_accuracy: 0.9411
50720/60000 [========================>.....] - ETA: 17s - loss: 0.1943 - categorical_accuracy: 0.9411
50752/60000 [========================>.....] - ETA: 17s - loss: 0.1942 - categorical_accuracy: 0.9412
50784/60000 [========================>.....] - ETA: 17s - loss: 0.1941 - categorical_accuracy: 0.9412
50816/60000 [========================>.....] - ETA: 17s - loss: 0.1940 - categorical_accuracy: 0.9412
50848/60000 [========================>.....] - ETA: 17s - loss: 0.1940 - categorical_accuracy: 0.9412
50880/60000 [========================>.....] - ETA: 17s - loss: 0.1939 - categorical_accuracy: 0.9413
50912/60000 [========================>.....] - ETA: 17s - loss: 0.1938 - categorical_accuracy: 0.9413
50944/60000 [========================>.....] - ETA: 17s - loss: 0.1938 - categorical_accuracy: 0.9413
50976/60000 [========================>.....] - ETA: 17s - loss: 0.1938 - categorical_accuracy: 0.9413
51008/60000 [========================>.....] - ETA: 17s - loss: 0.1937 - categorical_accuracy: 0.9413
51040/60000 [========================>.....] - ETA: 17s - loss: 0.1936 - categorical_accuracy: 0.9414
51072/60000 [========================>.....] - ETA: 16s - loss: 0.1935 - categorical_accuracy: 0.9414
51104/60000 [========================>.....] - ETA: 16s - loss: 0.1935 - categorical_accuracy: 0.9414
51136/60000 [========================>.....] - ETA: 16s - loss: 0.1934 - categorical_accuracy: 0.9414
51168/60000 [========================>.....] - ETA: 16s - loss: 0.1933 - categorical_accuracy: 0.9414
51200/60000 [========================>.....] - ETA: 16s - loss: 0.1932 - categorical_accuracy: 0.9414
51232/60000 [========================>.....] - ETA: 16s - loss: 0.1931 - categorical_accuracy: 0.9414
51264/60000 [========================>.....] - ETA: 16s - loss: 0.1930 - categorical_accuracy: 0.9415
51296/60000 [========================>.....] - ETA: 16s - loss: 0.1929 - categorical_accuracy: 0.9415
51328/60000 [========================>.....] - ETA: 16s - loss: 0.1930 - categorical_accuracy: 0.9415
51360/60000 [========================>.....] - ETA: 16s - loss: 0.1929 - categorical_accuracy: 0.9415
51392/60000 [========================>.....] - ETA: 16s - loss: 0.1928 - categorical_accuracy: 0.9415
51424/60000 [========================>.....] - ETA: 16s - loss: 0.1929 - categorical_accuracy: 0.9415
51456/60000 [========================>.....] - ETA: 16s - loss: 0.1928 - categorical_accuracy: 0.9416
51488/60000 [========================>.....] - ETA: 16s - loss: 0.1927 - categorical_accuracy: 0.9416
51520/60000 [========================>.....] - ETA: 16s - loss: 0.1926 - categorical_accuracy: 0.9416
51552/60000 [========================>.....] - ETA: 16s - loss: 0.1926 - categorical_accuracy: 0.9417
51584/60000 [========================>.....] - ETA: 15s - loss: 0.1925 - categorical_accuracy: 0.9417
51616/60000 [========================>.....] - ETA: 15s - loss: 0.1925 - categorical_accuracy: 0.9417
51648/60000 [========================>.....] - ETA: 15s - loss: 0.1924 - categorical_accuracy: 0.9417
51680/60000 [========================>.....] - ETA: 15s - loss: 0.1923 - categorical_accuracy: 0.9417
51712/60000 [========================>.....] - ETA: 15s - loss: 0.1922 - categorical_accuracy: 0.9418
51744/60000 [========================>.....] - ETA: 15s - loss: 0.1921 - categorical_accuracy: 0.9418
51776/60000 [========================>.....] - ETA: 15s - loss: 0.1920 - categorical_accuracy: 0.9418
51808/60000 [========================>.....] - ETA: 15s - loss: 0.1919 - categorical_accuracy: 0.9418
51840/60000 [========================>.....] - ETA: 15s - loss: 0.1920 - categorical_accuracy: 0.9418
51872/60000 [========================>.....] - ETA: 15s - loss: 0.1919 - categorical_accuracy: 0.9418
51904/60000 [========================>.....] - ETA: 15s - loss: 0.1918 - categorical_accuracy: 0.9418
51936/60000 [========================>.....] - ETA: 15s - loss: 0.1917 - categorical_accuracy: 0.9419
51968/60000 [========================>.....] - ETA: 15s - loss: 0.1916 - categorical_accuracy: 0.9419
52000/60000 [=========================>....] - ETA: 15s - loss: 0.1916 - categorical_accuracy: 0.9419
52032/60000 [=========================>....] - ETA: 15s - loss: 0.1916 - categorical_accuracy: 0.9419
52064/60000 [=========================>....] - ETA: 15s - loss: 0.1915 - categorical_accuracy: 0.9420
52096/60000 [=========================>....] - ETA: 15s - loss: 0.1914 - categorical_accuracy: 0.9420
52128/60000 [=========================>....] - ETA: 14s - loss: 0.1913 - categorical_accuracy: 0.9420
52160/60000 [=========================>....] - ETA: 14s - loss: 0.1912 - categorical_accuracy: 0.9421
52192/60000 [=========================>....] - ETA: 14s - loss: 0.1912 - categorical_accuracy: 0.9421
52224/60000 [=========================>....] - ETA: 14s - loss: 0.1912 - categorical_accuracy: 0.9421
52256/60000 [=========================>....] - ETA: 14s - loss: 0.1911 - categorical_accuracy: 0.9421
52288/60000 [=========================>....] - ETA: 14s - loss: 0.1911 - categorical_accuracy: 0.9421
52320/60000 [=========================>....] - ETA: 14s - loss: 0.1910 - categorical_accuracy: 0.9421
52352/60000 [=========================>....] - ETA: 14s - loss: 0.1910 - categorical_accuracy: 0.9421
52384/60000 [=========================>....] - ETA: 14s - loss: 0.1909 - categorical_accuracy: 0.9421
52416/60000 [=========================>....] - ETA: 14s - loss: 0.1908 - categorical_accuracy: 0.9422
52448/60000 [=========================>....] - ETA: 14s - loss: 0.1907 - categorical_accuracy: 0.9422
52480/60000 [=========================>....] - ETA: 14s - loss: 0.1906 - categorical_accuracy: 0.9422
52512/60000 [=========================>....] - ETA: 14s - loss: 0.1907 - categorical_accuracy: 0.9422
52544/60000 [=========================>....] - ETA: 14s - loss: 0.1906 - categorical_accuracy: 0.9423
52576/60000 [=========================>....] - ETA: 14s - loss: 0.1905 - categorical_accuracy: 0.9423
52608/60000 [=========================>....] - ETA: 14s - loss: 0.1907 - categorical_accuracy: 0.9423
52640/60000 [=========================>....] - ETA: 13s - loss: 0.1906 - categorical_accuracy: 0.9423
52672/60000 [=========================>....] - ETA: 13s - loss: 0.1906 - categorical_accuracy: 0.9423
52704/60000 [=========================>....] - ETA: 13s - loss: 0.1906 - categorical_accuracy: 0.9423
52736/60000 [=========================>....] - ETA: 13s - loss: 0.1905 - categorical_accuracy: 0.9423
52768/60000 [=========================>....] - ETA: 13s - loss: 0.1904 - categorical_accuracy: 0.9423
52800/60000 [=========================>....] - ETA: 13s - loss: 0.1904 - categorical_accuracy: 0.9423
52832/60000 [=========================>....] - ETA: 13s - loss: 0.1904 - categorical_accuracy: 0.9423
52864/60000 [=========================>....] - ETA: 13s - loss: 0.1903 - categorical_accuracy: 0.9424
52896/60000 [=========================>....] - ETA: 13s - loss: 0.1902 - categorical_accuracy: 0.9424
52928/60000 [=========================>....] - ETA: 13s - loss: 0.1901 - categorical_accuracy: 0.9424
52960/60000 [=========================>....] - ETA: 13s - loss: 0.1901 - categorical_accuracy: 0.9424
52992/60000 [=========================>....] - ETA: 13s - loss: 0.1900 - categorical_accuracy: 0.9425
53024/60000 [=========================>....] - ETA: 13s - loss: 0.1899 - categorical_accuracy: 0.9425
53056/60000 [=========================>....] - ETA: 13s - loss: 0.1898 - categorical_accuracy: 0.9425
53088/60000 [=========================>....] - ETA: 13s - loss: 0.1897 - categorical_accuracy: 0.9425
53120/60000 [=========================>....] - ETA: 13s - loss: 0.1897 - categorical_accuracy: 0.9425
53152/60000 [=========================>....] - ETA: 13s - loss: 0.1896 - categorical_accuracy: 0.9426
53184/60000 [=========================>....] - ETA: 12s - loss: 0.1896 - categorical_accuracy: 0.9426
53216/60000 [=========================>....] - ETA: 12s - loss: 0.1895 - categorical_accuracy: 0.9426
53248/60000 [=========================>....] - ETA: 12s - loss: 0.1895 - categorical_accuracy: 0.9426
53280/60000 [=========================>....] - ETA: 12s - loss: 0.1895 - categorical_accuracy: 0.9426
53312/60000 [=========================>....] - ETA: 12s - loss: 0.1895 - categorical_accuracy: 0.9426
53344/60000 [=========================>....] - ETA: 12s - loss: 0.1894 - categorical_accuracy: 0.9426
53376/60000 [=========================>....] - ETA: 12s - loss: 0.1894 - categorical_accuracy: 0.9427
53408/60000 [=========================>....] - ETA: 12s - loss: 0.1893 - categorical_accuracy: 0.9427
53440/60000 [=========================>....] - ETA: 12s - loss: 0.1892 - categorical_accuracy: 0.9427
53472/60000 [=========================>....] - ETA: 12s - loss: 0.1891 - categorical_accuracy: 0.9427
53504/60000 [=========================>....] - ETA: 12s - loss: 0.1890 - categorical_accuracy: 0.9428
53536/60000 [=========================>....] - ETA: 12s - loss: 0.1889 - categorical_accuracy: 0.9428
53568/60000 [=========================>....] - ETA: 12s - loss: 0.1888 - categorical_accuracy: 0.9428
53600/60000 [=========================>....] - ETA: 12s - loss: 0.1887 - categorical_accuracy: 0.9429
53632/60000 [=========================>....] - ETA: 12s - loss: 0.1886 - categorical_accuracy: 0.9429
53664/60000 [=========================>....] - ETA: 12s - loss: 0.1885 - categorical_accuracy: 0.9429
53696/60000 [=========================>....] - ETA: 11s - loss: 0.1885 - categorical_accuracy: 0.9429
53728/60000 [=========================>....] - ETA: 11s - loss: 0.1884 - categorical_accuracy: 0.9429
53760/60000 [=========================>....] - ETA: 11s - loss: 0.1883 - categorical_accuracy: 0.9430
53792/60000 [=========================>....] - ETA: 11s - loss: 0.1883 - categorical_accuracy: 0.9430
53824/60000 [=========================>....] - ETA: 11s - loss: 0.1882 - categorical_accuracy: 0.9430
53856/60000 [=========================>....] - ETA: 11s - loss: 0.1881 - categorical_accuracy: 0.9430
53888/60000 [=========================>....] - ETA: 11s - loss: 0.1880 - categorical_accuracy: 0.9430
53920/60000 [=========================>....] - ETA: 11s - loss: 0.1880 - categorical_accuracy: 0.9431
53952/60000 [=========================>....] - ETA: 11s - loss: 0.1879 - categorical_accuracy: 0.9431
53984/60000 [=========================>....] - ETA: 11s - loss: 0.1878 - categorical_accuracy: 0.9431
54016/60000 [==========================>...] - ETA: 11s - loss: 0.1877 - categorical_accuracy: 0.9431
54048/60000 [==========================>...] - ETA: 11s - loss: 0.1876 - categorical_accuracy: 0.9432
54080/60000 [==========================>...] - ETA: 11s - loss: 0.1876 - categorical_accuracy: 0.9432
54112/60000 [==========================>...] - ETA: 11s - loss: 0.1875 - categorical_accuracy: 0.9432
54144/60000 [==========================>...] - ETA: 11s - loss: 0.1874 - categorical_accuracy: 0.9432
54176/60000 [==========================>...] - ETA: 11s - loss: 0.1874 - categorical_accuracy: 0.9432
54208/60000 [==========================>...] - ETA: 11s - loss: 0.1873 - categorical_accuracy: 0.9433
54240/60000 [==========================>...] - ETA: 10s - loss: 0.1872 - categorical_accuracy: 0.9433
54272/60000 [==========================>...] - ETA: 10s - loss: 0.1871 - categorical_accuracy: 0.9433
54304/60000 [==========================>...] - ETA: 10s - loss: 0.1870 - categorical_accuracy: 0.9434
54336/60000 [==========================>...] - ETA: 10s - loss: 0.1869 - categorical_accuracy: 0.9434
54368/60000 [==========================>...] - ETA: 10s - loss: 0.1868 - categorical_accuracy: 0.9434
54400/60000 [==========================>...] - ETA: 10s - loss: 0.1867 - categorical_accuracy: 0.9435
54432/60000 [==========================>...] - ETA: 10s - loss: 0.1866 - categorical_accuracy: 0.9435
54464/60000 [==========================>...] - ETA: 10s - loss: 0.1865 - categorical_accuracy: 0.9435
54496/60000 [==========================>...] - ETA: 10s - loss: 0.1865 - categorical_accuracy: 0.9436
54528/60000 [==========================>...] - ETA: 10s - loss: 0.1864 - categorical_accuracy: 0.9436
54560/60000 [==========================>...] - ETA: 10s - loss: 0.1863 - categorical_accuracy: 0.9436
54592/60000 [==========================>...] - ETA: 10s - loss: 0.1862 - categorical_accuracy: 0.9436
54624/60000 [==========================>...] - ETA: 10s - loss: 0.1862 - categorical_accuracy: 0.9436
54656/60000 [==========================>...] - ETA: 10s - loss: 0.1861 - categorical_accuracy: 0.9436
54688/60000 [==========================>...] - ETA: 10s - loss: 0.1862 - categorical_accuracy: 0.9436
54720/60000 [==========================>...] - ETA: 10s - loss: 0.1863 - categorical_accuracy: 0.9436
54752/60000 [==========================>...] - ETA: 9s - loss: 0.1862 - categorical_accuracy: 0.9436 
54784/60000 [==========================>...] - ETA: 9s - loss: 0.1861 - categorical_accuracy: 0.9437
54816/60000 [==========================>...] - ETA: 9s - loss: 0.1862 - categorical_accuracy: 0.9436
54848/60000 [==========================>...] - ETA: 9s - loss: 0.1861 - categorical_accuracy: 0.9437
54880/60000 [==========================>...] - ETA: 9s - loss: 0.1861 - categorical_accuracy: 0.9437
54912/60000 [==========================>...] - ETA: 9s - loss: 0.1861 - categorical_accuracy: 0.9437
54944/60000 [==========================>...] - ETA: 9s - loss: 0.1860 - categorical_accuracy: 0.9437
54976/60000 [==========================>...] - ETA: 9s - loss: 0.1859 - categorical_accuracy: 0.9437
55008/60000 [==========================>...] - ETA: 9s - loss: 0.1858 - categorical_accuracy: 0.9438
55040/60000 [==========================>...] - ETA: 9s - loss: 0.1857 - categorical_accuracy: 0.9438
55072/60000 [==========================>...] - ETA: 9s - loss: 0.1856 - categorical_accuracy: 0.9438
55104/60000 [==========================>...] - ETA: 9s - loss: 0.1856 - categorical_accuracy: 0.9438
55136/60000 [==========================>...] - ETA: 9s - loss: 0.1856 - categorical_accuracy: 0.9438
55168/60000 [==========================>...] - ETA: 9s - loss: 0.1855 - categorical_accuracy: 0.9438
55200/60000 [==========================>...] - ETA: 9s - loss: 0.1855 - categorical_accuracy: 0.9439
55232/60000 [==========================>...] - ETA: 9s - loss: 0.1854 - categorical_accuracy: 0.9439
55264/60000 [==========================>...] - ETA: 8s - loss: 0.1854 - categorical_accuracy: 0.9439
55296/60000 [==========================>...] - ETA: 8s - loss: 0.1855 - categorical_accuracy: 0.9439
55328/60000 [==========================>...] - ETA: 8s - loss: 0.1854 - categorical_accuracy: 0.9439
55360/60000 [==========================>...] - ETA: 8s - loss: 0.1853 - categorical_accuracy: 0.9439
55392/60000 [==========================>...] - ETA: 8s - loss: 0.1852 - categorical_accuracy: 0.9440
55424/60000 [==========================>...] - ETA: 8s - loss: 0.1851 - categorical_accuracy: 0.9440
55456/60000 [==========================>...] - ETA: 8s - loss: 0.1850 - categorical_accuracy: 0.9440
55488/60000 [==========================>...] - ETA: 8s - loss: 0.1849 - categorical_accuracy: 0.9440
55520/60000 [==========================>...] - ETA: 8s - loss: 0.1850 - categorical_accuracy: 0.9440
55552/60000 [==========================>...] - ETA: 8s - loss: 0.1850 - categorical_accuracy: 0.9441
55584/60000 [==========================>...] - ETA: 8s - loss: 0.1849 - categorical_accuracy: 0.9441
55616/60000 [==========================>...] - ETA: 8s - loss: 0.1849 - categorical_accuracy: 0.9441
55648/60000 [==========================>...] - ETA: 8s - loss: 0.1848 - categorical_accuracy: 0.9441
55680/60000 [==========================>...] - ETA: 8s - loss: 0.1850 - categorical_accuracy: 0.9441
55712/60000 [==========================>...] - ETA: 8s - loss: 0.1849 - categorical_accuracy: 0.9441
55744/60000 [==========================>...] - ETA: 8s - loss: 0.1848 - categorical_accuracy: 0.9441
55776/60000 [==========================>...] - ETA: 8s - loss: 0.1848 - categorical_accuracy: 0.9441
55808/60000 [==========================>...] - ETA: 7s - loss: 0.1847 - categorical_accuracy: 0.9441
55840/60000 [==========================>...] - ETA: 7s - loss: 0.1847 - categorical_accuracy: 0.9442
55872/60000 [==========================>...] - ETA: 7s - loss: 0.1846 - categorical_accuracy: 0.9442
55904/60000 [==========================>...] - ETA: 7s - loss: 0.1846 - categorical_accuracy: 0.9442
55936/60000 [==========================>...] - ETA: 7s - loss: 0.1846 - categorical_accuracy: 0.9442
55968/60000 [==========================>...] - ETA: 7s - loss: 0.1845 - categorical_accuracy: 0.9443
56000/60000 [===========================>..] - ETA: 7s - loss: 0.1844 - categorical_accuracy: 0.9443
56032/60000 [===========================>..] - ETA: 7s - loss: 0.1843 - categorical_accuracy: 0.9443
56064/60000 [===========================>..] - ETA: 7s - loss: 0.1844 - categorical_accuracy: 0.9443
56096/60000 [===========================>..] - ETA: 7s - loss: 0.1843 - categorical_accuracy: 0.9444
56128/60000 [===========================>..] - ETA: 7s - loss: 0.1844 - categorical_accuracy: 0.9444
56160/60000 [===========================>..] - ETA: 7s - loss: 0.1843 - categorical_accuracy: 0.9444
56192/60000 [===========================>..] - ETA: 7s - loss: 0.1843 - categorical_accuracy: 0.9444
56224/60000 [===========================>..] - ETA: 7s - loss: 0.1842 - categorical_accuracy: 0.9444
56256/60000 [===========================>..] - ETA: 7s - loss: 0.1841 - categorical_accuracy: 0.9444
56288/60000 [===========================>..] - ETA: 7s - loss: 0.1840 - categorical_accuracy: 0.9444
56320/60000 [===========================>..] - ETA: 6s - loss: 0.1840 - categorical_accuracy: 0.9444
56352/60000 [===========================>..] - ETA: 6s - loss: 0.1840 - categorical_accuracy: 0.9444
56384/60000 [===========================>..] - ETA: 6s - loss: 0.1839 - categorical_accuracy: 0.9444
56416/60000 [===========================>..] - ETA: 6s - loss: 0.1839 - categorical_accuracy: 0.9444
56448/60000 [===========================>..] - ETA: 6s - loss: 0.1838 - categorical_accuracy: 0.9445
56480/60000 [===========================>..] - ETA: 6s - loss: 0.1838 - categorical_accuracy: 0.9445
56512/60000 [===========================>..] - ETA: 6s - loss: 0.1838 - categorical_accuracy: 0.9445
56544/60000 [===========================>..] - ETA: 6s - loss: 0.1838 - categorical_accuracy: 0.9445
56576/60000 [===========================>..] - ETA: 6s - loss: 0.1838 - categorical_accuracy: 0.9445
56608/60000 [===========================>..] - ETA: 6s - loss: 0.1837 - categorical_accuracy: 0.9445
56640/60000 [===========================>..] - ETA: 6s - loss: 0.1837 - categorical_accuracy: 0.9445
56672/60000 [===========================>..] - ETA: 6s - loss: 0.1836 - categorical_accuracy: 0.9446
56704/60000 [===========================>..] - ETA: 6s - loss: 0.1835 - categorical_accuracy: 0.9446
56736/60000 [===========================>..] - ETA: 6s - loss: 0.1836 - categorical_accuracy: 0.9446
56768/60000 [===========================>..] - ETA: 6s - loss: 0.1836 - categorical_accuracy: 0.9446
56800/60000 [===========================>..] - ETA: 6s - loss: 0.1835 - categorical_accuracy: 0.9446
56832/60000 [===========================>..] - ETA: 6s - loss: 0.1834 - categorical_accuracy: 0.9447
56864/60000 [===========================>..] - ETA: 5s - loss: 0.1834 - categorical_accuracy: 0.9447
56896/60000 [===========================>..] - ETA: 5s - loss: 0.1833 - categorical_accuracy: 0.9447
56928/60000 [===========================>..] - ETA: 5s - loss: 0.1832 - categorical_accuracy: 0.9447
56960/60000 [===========================>..] - ETA: 5s - loss: 0.1831 - categorical_accuracy: 0.9448
56992/60000 [===========================>..] - ETA: 5s - loss: 0.1830 - categorical_accuracy: 0.9448
57024/60000 [===========================>..] - ETA: 5s - loss: 0.1830 - categorical_accuracy: 0.9448
57056/60000 [===========================>..] - ETA: 5s - loss: 0.1829 - categorical_accuracy: 0.9448
57088/60000 [===========================>..] - ETA: 5s - loss: 0.1828 - categorical_accuracy: 0.9448
57120/60000 [===========================>..] - ETA: 5s - loss: 0.1828 - categorical_accuracy: 0.9449
57152/60000 [===========================>..] - ETA: 5s - loss: 0.1827 - categorical_accuracy: 0.9449
57184/60000 [===========================>..] - ETA: 5s - loss: 0.1827 - categorical_accuracy: 0.9449
57216/60000 [===========================>..] - ETA: 5s - loss: 0.1827 - categorical_accuracy: 0.9449
57248/60000 [===========================>..] - ETA: 5s - loss: 0.1826 - categorical_accuracy: 0.9449
57280/60000 [===========================>..] - ETA: 5s - loss: 0.1826 - categorical_accuracy: 0.9449
57312/60000 [===========================>..] - ETA: 5s - loss: 0.1825 - categorical_accuracy: 0.9450
57344/60000 [===========================>..] - ETA: 5s - loss: 0.1827 - categorical_accuracy: 0.9449
57376/60000 [===========================>..] - ETA: 4s - loss: 0.1826 - categorical_accuracy: 0.9450
57408/60000 [===========================>..] - ETA: 4s - loss: 0.1825 - categorical_accuracy: 0.9450
57440/60000 [===========================>..] - ETA: 4s - loss: 0.1824 - categorical_accuracy: 0.9450
57472/60000 [===========================>..] - ETA: 4s - loss: 0.1824 - categorical_accuracy: 0.9450
57504/60000 [===========================>..] - ETA: 4s - loss: 0.1824 - categorical_accuracy: 0.9450
57536/60000 [===========================>..] - ETA: 4s - loss: 0.1823 - categorical_accuracy: 0.9450
57568/60000 [===========================>..] - ETA: 4s - loss: 0.1822 - categorical_accuracy: 0.9450
57600/60000 [===========================>..] - ETA: 4s - loss: 0.1822 - categorical_accuracy: 0.9451
57632/60000 [===========================>..] - ETA: 4s - loss: 0.1821 - categorical_accuracy: 0.9451
57664/60000 [===========================>..] - ETA: 4s - loss: 0.1820 - categorical_accuracy: 0.9451
57696/60000 [===========================>..] - ETA: 4s - loss: 0.1819 - categorical_accuracy: 0.9451
57728/60000 [===========================>..] - ETA: 4s - loss: 0.1819 - categorical_accuracy: 0.9451
57760/60000 [===========================>..] - ETA: 4s - loss: 0.1818 - categorical_accuracy: 0.9452
57792/60000 [===========================>..] - ETA: 4s - loss: 0.1818 - categorical_accuracy: 0.9452
57824/60000 [===========================>..] - ETA: 4s - loss: 0.1817 - categorical_accuracy: 0.9452
57856/60000 [===========================>..] - ETA: 4s - loss: 0.1817 - categorical_accuracy: 0.9452
57888/60000 [===========================>..] - ETA: 4s - loss: 0.1816 - categorical_accuracy: 0.9452
57920/60000 [===========================>..] - ETA: 3s - loss: 0.1815 - categorical_accuracy: 0.9453
57952/60000 [===========================>..] - ETA: 3s - loss: 0.1815 - categorical_accuracy: 0.9452
57984/60000 [===========================>..] - ETA: 3s - loss: 0.1815 - categorical_accuracy: 0.9453
58016/60000 [============================>.] - ETA: 3s - loss: 0.1815 - categorical_accuracy: 0.9453
58048/60000 [============================>.] - ETA: 3s - loss: 0.1814 - categorical_accuracy: 0.9453
58080/60000 [============================>.] - ETA: 3s - loss: 0.1813 - categorical_accuracy: 0.9453
58112/60000 [============================>.] - ETA: 3s - loss: 0.1812 - categorical_accuracy: 0.9453
58144/60000 [============================>.] - ETA: 3s - loss: 0.1812 - categorical_accuracy: 0.9454
58176/60000 [============================>.] - ETA: 3s - loss: 0.1812 - categorical_accuracy: 0.9454
58208/60000 [============================>.] - ETA: 3s - loss: 0.1812 - categorical_accuracy: 0.9454
58240/60000 [============================>.] - ETA: 3s - loss: 0.1812 - categorical_accuracy: 0.9454
58272/60000 [============================>.] - ETA: 3s - loss: 0.1811 - categorical_accuracy: 0.9454
58304/60000 [============================>.] - ETA: 3s - loss: 0.1810 - categorical_accuracy: 0.9454
58336/60000 [============================>.] - ETA: 3s - loss: 0.1810 - categorical_accuracy: 0.9454
58368/60000 [============================>.] - ETA: 3s - loss: 0.1809 - categorical_accuracy: 0.9454
58400/60000 [============================>.] - ETA: 3s - loss: 0.1808 - categorical_accuracy: 0.9455
58432/60000 [============================>.] - ETA: 2s - loss: 0.1809 - categorical_accuracy: 0.9455
58464/60000 [============================>.] - ETA: 2s - loss: 0.1810 - categorical_accuracy: 0.9455
58496/60000 [============================>.] - ETA: 2s - loss: 0.1809 - categorical_accuracy: 0.9455
58528/60000 [============================>.] - ETA: 2s - loss: 0.1809 - categorical_accuracy: 0.9455
58560/60000 [============================>.] - ETA: 2s - loss: 0.1808 - categorical_accuracy: 0.9455
58592/60000 [============================>.] - ETA: 2s - loss: 0.1807 - categorical_accuracy: 0.9455
58624/60000 [============================>.] - ETA: 2s - loss: 0.1808 - categorical_accuracy: 0.9455
58656/60000 [============================>.] - ETA: 2s - loss: 0.1807 - categorical_accuracy: 0.9456
58688/60000 [============================>.] - ETA: 2s - loss: 0.1808 - categorical_accuracy: 0.9456
58720/60000 [============================>.] - ETA: 2s - loss: 0.1807 - categorical_accuracy: 0.9456
58752/60000 [============================>.] - ETA: 2s - loss: 0.1806 - categorical_accuracy: 0.9456
58784/60000 [============================>.] - ETA: 2s - loss: 0.1806 - categorical_accuracy: 0.9456
58816/60000 [============================>.] - ETA: 2s - loss: 0.1805 - categorical_accuracy: 0.9456
58848/60000 [============================>.] - ETA: 2s - loss: 0.1804 - categorical_accuracy: 0.9457
58880/60000 [============================>.] - ETA: 2s - loss: 0.1804 - categorical_accuracy: 0.9457
58912/60000 [============================>.] - ETA: 2s - loss: 0.1804 - categorical_accuracy: 0.9457
58944/60000 [============================>.] - ETA: 2s - loss: 0.1803 - categorical_accuracy: 0.9457
58976/60000 [============================>.] - ETA: 1s - loss: 0.1803 - categorical_accuracy: 0.9457
59008/60000 [============================>.] - ETA: 1s - loss: 0.1802 - categorical_accuracy: 0.9457
59040/60000 [============================>.] - ETA: 1s - loss: 0.1802 - categorical_accuracy: 0.9457
59072/60000 [============================>.] - ETA: 1s - loss: 0.1801 - categorical_accuracy: 0.9458
59104/60000 [============================>.] - ETA: 1s - loss: 0.1800 - categorical_accuracy: 0.9458
59136/60000 [============================>.] - ETA: 1s - loss: 0.1799 - categorical_accuracy: 0.9458
59168/60000 [============================>.] - ETA: 1s - loss: 0.1799 - categorical_accuracy: 0.9458
59200/60000 [============================>.] - ETA: 1s - loss: 0.1798 - categorical_accuracy: 0.9459
59232/60000 [============================>.] - ETA: 1s - loss: 0.1797 - categorical_accuracy: 0.9459
59264/60000 [============================>.] - ETA: 1s - loss: 0.1797 - categorical_accuracy: 0.9459
59296/60000 [============================>.] - ETA: 1s - loss: 0.1797 - categorical_accuracy: 0.9459
59328/60000 [============================>.] - ETA: 1s - loss: 0.1796 - categorical_accuracy: 0.9459
59360/60000 [============================>.] - ETA: 1s - loss: 0.1796 - categorical_accuracy: 0.9459
59392/60000 [============================>.] - ETA: 1s - loss: 0.1796 - categorical_accuracy: 0.9459
59424/60000 [============================>.] - ETA: 1s - loss: 0.1796 - categorical_accuracy: 0.9460
59456/60000 [============================>.] - ETA: 1s - loss: 0.1795 - categorical_accuracy: 0.9460
59488/60000 [============================>.] - ETA: 0s - loss: 0.1795 - categorical_accuracy: 0.9460
59520/60000 [============================>.] - ETA: 0s - loss: 0.1794 - categorical_accuracy: 0.9460
59552/60000 [============================>.] - ETA: 0s - loss: 0.1793 - categorical_accuracy: 0.9460
59584/60000 [============================>.] - ETA: 0s - loss: 0.1793 - categorical_accuracy: 0.9460
59616/60000 [============================>.] - ETA: 0s - loss: 0.1793 - categorical_accuracy: 0.9460
59648/60000 [============================>.] - ETA: 0s - loss: 0.1792 - categorical_accuracy: 0.9461
59680/60000 [============================>.] - ETA: 0s - loss: 0.1791 - categorical_accuracy: 0.9461
59712/60000 [============================>.] - ETA: 0s - loss: 0.1791 - categorical_accuracy: 0.9461
59744/60000 [============================>.] - ETA: 0s - loss: 0.1790 - categorical_accuracy: 0.9461
59776/60000 [============================>.] - ETA: 0s - loss: 0.1789 - categorical_accuracy: 0.9461
59808/60000 [============================>.] - ETA: 0s - loss: 0.1788 - categorical_accuracy: 0.9462
59840/60000 [============================>.] - ETA: 0s - loss: 0.1788 - categorical_accuracy: 0.9462
59872/60000 [============================>.] - ETA: 0s - loss: 0.1787 - categorical_accuracy: 0.9462
59904/60000 [============================>.] - ETA: 0s - loss: 0.1788 - categorical_accuracy: 0.9462
59936/60000 [============================>.] - ETA: 0s - loss: 0.1787 - categorical_accuracy: 0.9462
59968/60000 [============================>.] - ETA: 0s - loss: 0.1787 - categorical_accuracy: 0.9462
60000/60000 [==============================] - 118s 2ms/step - loss: 0.1786 - categorical_accuracy: 0.9462 - val_loss: 0.0437 - val_categorical_accuracy: 0.9851

  ('#### Predict   ####################################################',) 

  ('#### Path params   ################################################',) 

  ('/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/', '/home/runner/work/mlmodels/mlmodels/keras_deepAR/') 

   32/10000 [..............................] - ETA: 18s
  192/10000 [..............................] - ETA: 6s 
  352/10000 [>.............................] - ETA: 4s
  512/10000 [>.............................] - ETA: 4s
  672/10000 [=>............................] - ETA: 3s
  832/10000 [=>............................] - ETA: 3s
  992/10000 [=>............................] - ETA: 3s
 1152/10000 [==>...........................] - ETA: 3s
 1312/10000 [==>...........................] - ETA: 3s
 1440/10000 [===>..........................] - ETA: 3s
 1600/10000 [===>..........................] - ETA: 3s
 1760/10000 [====>.........................] - ETA: 3s
 1888/10000 [====>.........................] - ETA: 3s
 2048/10000 [=====>........................] - ETA: 3s
 2208/10000 [=====>........................] - ETA: 3s
 2368/10000 [======>.......................] - ETA: 2s
 2528/10000 [======>.......................] - ETA: 2s
 2656/10000 [======>.......................] - ETA: 2s
 2784/10000 [=======>......................] - ETA: 2s
 2944/10000 [=======>......................] - ETA: 2s
 3104/10000 [========>.....................] - ETA: 2s
 3264/10000 [========>.....................] - ETA: 2s
 3424/10000 [=========>....................] - ETA: 2s
 3584/10000 [=========>....................] - ETA: 2s
 3744/10000 [==========>...................] - ETA: 2s
 3904/10000 [==========>...................] - ETA: 2s
 4064/10000 [===========>..................] - ETA: 2s
 4160/10000 [===========>..................] - ETA: 2s
 4320/10000 [===========>..................] - ETA: 2s
 4480/10000 [============>.................] - ETA: 2s
 4640/10000 [============>.................] - ETA: 2s
 4800/10000 [=============>................] - ETA: 2s
 4960/10000 [=============>................] - ETA: 1s
 5120/10000 [==============>...............] - ETA: 1s
 5280/10000 [==============>...............] - ETA: 1s
 5408/10000 [===============>..............] - ETA: 1s
 5568/10000 [===============>..............] - ETA: 1s
 5728/10000 [================>.............] - ETA: 1s
 5888/10000 [================>.............] - ETA: 1s
 6048/10000 [=================>............] - ETA: 1s
 6208/10000 [=================>............] - ETA: 1s
 6368/10000 [==================>...........] - ETA: 1s
 6496/10000 [==================>...........] - ETA: 1s
 6656/10000 [==================>...........] - ETA: 1s
 6784/10000 [===================>..........] - ETA: 1s
 6944/10000 [===================>..........] - ETA: 1s
 7104/10000 [====================>.........] - ETA: 1s
 7264/10000 [====================>.........] - ETA: 1s
 7424/10000 [=====================>........] - ETA: 0s
 7584/10000 [=====================>........] - ETA: 0s
 7744/10000 [======================>.......] - ETA: 0s
 7904/10000 [======================>.......] - ETA: 0s
 8064/10000 [=======================>......] - ETA: 0s
 8192/10000 [=======================>......] - ETA: 0s
 8352/10000 [========================>.....] - ETA: 0s
 8512/10000 [========================>.....] - ETA: 0s
 8672/10000 [=========================>....] - ETA: 0s
 8832/10000 [=========================>....] - ETA: 0s
 8992/10000 [=========================>....] - ETA: 0s
 9152/10000 [==========================>...] - ETA: 0s
 9312/10000 [==========================>...] - ETA: 0s
 9472/10000 [===========================>..] - ETA: 0s
 9632/10000 [===========================>..] - ETA: 0s
 9792/10000 [============================>.] - ETA: 0s
 9952/10000 [============================>.] - ETA: 0s
10000/10000 [==============================] - 4s 375us/step
[[9.9102465e-08 1.8943064e-08 4.4475169e-07 ... 9.9998844e-01
  9.2385633e-08 6.9902135e-06]
 [2.0295251e-04 3.2658896e-05 9.9973315e-01 ... 1.9499676e-07
  1.9174418e-05 9.2839585e-09]
 [2.1683652e-06 9.9969614e-01 1.4804358e-05 ... 6.2367450e-05
  2.1167229e-05 1.4653799e-06]
 ...
 [1.1457461e-09 3.0928186e-07 1.2660194e-08 ... 4.0782828e-07
  7.1546538e-07 4.4293010e-06]
 [1.9374224e-06 9.9432185e-08 6.5457208e-08 ... 7.8982815e-08
  1.1149385e-03 6.7957581e-06]
 [9.2473401e-06 2.3158225e-06 4.2811798e-06 ... 8.8731245e-09
  5.0102353e-06 1.5010643e-07]]

  ('#### metrics   ####################################################',) 

  ('#### Path params   ################################################',) 

  ('/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/', '/home/runner/work/mlmodels/mlmodels/keras_deepAR/') 
{'loss_test:': 0.043736694176658056, 'accuracy_test:': 0.9850999712944031}

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
From github.com:arita37/mlmodels_store
   0b14cdb..1e657ec  master     -> origin/master
Updating 0b14cdb..1e657ec
Fast-forward
 deps.txt                                         |    5 +-
 error_list/20200523/list_log_json_20200523.md    | 1501 ++++++------
 error_list/20200523/list_log_testall_20200523.md |  433 ++++
 log_json/log_json.py                             | 2762 +++++++++++-----------
 4 files changed, 2584 insertions(+), 2117 deletions(-)
[master cf8c4b7] ml_store
 1 file changed, 2049 insertions(+)
To github.com:arita37/mlmodels_store.git
   1e657ec..cf8c4b7  master -> master





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
{'loss': 0.5015726685523987, 'loss_history': []}

  #### Plot   ######################################################## 

  #### Save   ######################################################## 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/'}
Model saved in path: /home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm//model//model.ckpt

  #### Load   ######################################################## 
2020-05-23 08:32:14.329421: W tensorflow/core/framework/op_kernel.cc:1651] OP_REQUIRES failed at save_restore_v2_ops.cc:184 : Not found: Key Variable not found in checkpoint
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
[master f67518c] ml_store
 2 files changed, 236 insertions(+), 3 deletions(-)
To github.com:arita37/mlmodels_store.git
   cf8c4b7..f67518c  master -> master





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
[master 59ca04b] ml_store
 1 file changed, 36 insertions(+)
To github.com:arita37/mlmodels_store.git
   f67518c..59ca04b  master -> master





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
	Data preprocessing and feature engineering runtime = 0.28s ...
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
 40%|████      | 2/5 [00:24<00:36, 12.20s/it]Saving dataset/models/LightGBMClassifier/trial_1_model.pkl
Finished Task with config: {'feature_fraction': 0.9125795839230187, 'learning_rate': 0.02753773277375454, 'min_data_in_leaf': 22, 'num_leaves': 39} and reward: 0.3906
Finished Task with config: b"\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xed3\xda\x19~J\xfbX\r\x00\x00\x00learning_rateq\x02G?\x9c2\xd9\xf6\xadSOX\x10\x00\x00\x00min_data_in_leafq\x03K\x16X\n\x00\x00\x00num_leavesq\x04K'u." and reward: 0.3906
Finished Task with config: b"\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xed3\xda\x19~J\xfbX\r\x00\x00\x00learning_rateq\x02G?\x9c2\xd9\xf6\xadSOX\x10\x00\x00\x00min_data_in_leafq\x03K\x16X\n\x00\x00\x00num_leavesq\x04K'u." and reward: 0.3906
 60%|██████    | 3/5 [00:50<00:32, 16.32s/it]Saving dataset/models/LightGBMClassifier/trial_2_model.pkl
Finished Task with config: {'feature_fraction': 0.7678990332017207, 'learning_rate': 0.016075104134041403, 'min_data_in_leaf': 7, 'num_leaves': 43} and reward: 0.3914
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xe8\x92\xa0\xfeGg\xb3X\r\x00\x00\x00learning_rateq\x02G?\x90u\xfd\xfa$Z\xb2X\x10\x00\x00\x00min_data_in_leafq\x03K\x07X\n\x00\x00\x00num_leavesq\x04K+u.' and reward: 0.3914
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xe8\x92\xa0\xfeGg\xb3X\r\x00\x00\x00learning_rateq\x02G?\x90u\xfd\xfa$Z\xb2X\x10\x00\x00\x00min_data_in_leafq\x03K\x07X\n\x00\x00\x00num_leavesq\x04K+u.' and reward: 0.3914
 80%|████████  | 4/5 [01:17<00:19, 19.58s/it] 80%|████████  | 4/5 [01:17<00:19, 19.38s/it]
Saving dataset/models/LightGBMClassifier/trial_3_model.pkl
Finished Task with config: {'feature_fraction': 0.7649409642332355, 'learning_rate': 0.008895104191957623, 'min_data_in_leaf': 5, 'num_leaves': 28} and reward: 0.3876
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xe8zey\x18\x14\x17X\r\x00\x00\x00learning_rateq\x02G?\x827\x98\xac\xca\xb1\x0bX\x10\x00\x00\x00min_data_in_leafq\x03K\x05X\n\x00\x00\x00num_leavesq\x04K\x1cu.' and reward: 0.3876
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xe8zey\x18\x14\x17X\r\x00\x00\x00learning_rateq\x02G?\x827\x98\xac\xca\xb1\x0bX\x10\x00\x00\x00min_data_in_leafq\x03K\x05X\n\x00\x00\x00num_leavesq\x04K\x1cu.' and reward: 0.3876
Time for Gradient Boosting hyperparameter optimization: 98.19172406196594
Best hyperparameter configuration for Gradient Boosting Model: 
{'feature_fraction': 0.7678990332017207, 'learning_rate': 0.016075104134041403, 'min_data_in_leaf': 7, 'num_leaves': 43}
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
 40%|████      | 2/5 [00:57<01:25, 28.60s/it] 40%|████      | 2/5 [00:57<01:25, 28.60s/it]
Loading: dataset/models/NeuralNetClassifier/train_tabNNdataset.pkl
Loading: dataset/models/NeuralNetClassifier/validation_tabNNdataset.pkl
Saving dataset/models/NeuralNetClassifier/trial_5_tabularNN.pkl
Finished Task with config: {'activation.choice': 1, 'dropout_prob': 0.41191910325518877, 'embedding_size_factor': 0.6701869386652034, 'layers.choice': 2, 'learning_rate': 0.00988466248640086, 'network_type.choice': 0, 'use_batchnorm.choice': 1, 'weight_decay': 4.946835473775766e-05} and reward: 0.3814
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x01X\x0c\x00\x00\x00dropout_probq\x02G?\xda\\\xe1\xf1E\t$X\x15\x00\x00\x00embedding_size_factorq\x03G?\xe5r+\xe0\xf8\xbf\xbfX\r\x00\x00\x00layers.choiceq\x04K\x02X\r\x00\x00\x00learning_rateq\x05G?\x84>h\xf0\xe3\x83\x04X\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x01X\x0c\x00\x00\x00weight_decayq\x08G?\t\xef\x87\xb9\xed\xccgu.' and reward: 0.3814
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x01X\x0c\x00\x00\x00dropout_probq\x02G?\xda\\\xe1\xf1E\t$X\x15\x00\x00\x00embedding_size_factorq\x03G?\xe5r+\xe0\xf8\xbf\xbfX\r\x00\x00\x00layers.choiceq\x04K\x02X\r\x00\x00\x00learning_rateq\x05G?\x84>h\xf0\xe3\x83\x04X\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x01X\x0c\x00\x00\x00weight_decayq\x08G?\t\xef\x87\xb9\xed\xccgu.' and reward: 0.3814
Please either provide filename or allow plot in get_training_curves
Time for Neural Network hyperparameter optimization: 116.29681944847107
Best hyperparameter configuration for Tabular Neural Network: 
{'activation.choice': 0, 'dropout_prob': 0.1, 'embedding_size_factor': 1.0, 'layers.choice': 0, 'learning_rate': 0.0005, 'network_type.choice': 0, 'use_batchnorm.choice': 0, 'weight_decay': 1e-06}
Saving dataset/models/trainer.pkl
Loading: dataset/models/LightGBMClassifier/trial_0_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_1_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_2_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_3_model.pkl
Loading: dataset/models/NeuralNetClassifier/trial_4_tabularNN.pkl
Loading: dataset/models/NeuralNetClassifier/trial_5_tabularNN.pkl
Fitting model: weighted_ensemble_k0_l1 ... Training model for up to 119.72s of the -98.65s of remaining time.
Ensemble size: 29
Ensemble weights: 
[0.27586207 0.13793103 0.10344828 0.31034483 0.06896552 0.10344828]
	0.3968	 = Validation accuracy score
	1.66s	 = Training runtime
	0.0s	 = Validation runtime
Saving dataset/models/weighted_ensemble_k0_l1/model.pkl
Saving dataset/models/trainer.pkl
Saving dataset/models/trainer.pkl
Saving dataset/models/trainer.pkl
AutoGluon training complete, total runtime = 220.37s ...
Loading: dataset/models/trainer.pkl

  #### save the trained model  ####################################### 

  #### Predict   #################################################### 
Loaded data from: https://autogluon.s3.amazonaws.com/datasets/Inc/test.csv | Columns = 15 / 15 | Rows = 9769 -> 9769
Loading: dataset/models/trainer.pkl
Loading: dataset/models/weighted_ensemble_k0_l1/model.pkl
Loading: dataset/models/LightGBMClassifier/trial_2_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_0_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_1_model.pkl
Loading: dataset/models/NeuralNetClassifier/trial_4_tabularNN.pkl
Loading: dataset/models/LightGBMClassifier/trial_3_model.pkl
Loading: dataset/models/NeuralNetClassifier/trial_5_tabularNN.pkl

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
Saving dataset/learner.pkl
TabularPredictor saved. To load, use: TabularPredictor.load(dataset/)
<mlmodels.model_gluon.util_autogluon.Model_empty object at 0x7f1ddc9c7ef0>

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
   59ca04b..314b65b  master     -> origin/master
Updating 59ca04b..314b65b
Fast-forward
 error_list/20200523/list_log_testall_20200523.md | 175 +++++++++++++++++++++++
 1 file changed, 175 insertions(+)
[master b7e622f] ml_store
 1 file changed, 205 insertions(+)
To github.com:arita37/mlmodels_store.git
   314b65b..b7e622f  master -> master





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
[master 29ee6bb] ml_store
 1 file changed, 36 insertions(+)
To github.com:arita37/mlmodels_store.git
   b7e622f..29ee6bb  master -> master





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
100%|██████████| 10/10 [00:03<00:00,  3.17it/s, avg_epoch_loss=5.25]
INFO:root:Epoch[0] Elapsed time 3.155 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=5.245544
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 5.245544147491455 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7fd9020b03c8>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7fd9020b03c8>

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
Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 87.04it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 1064.1292317708333,
    "abs_error": 370.6484069824219,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 2.455897746216406,
    "sMAPE": 0.5130931648760814,
    "MSIS": 98.23590499566566,
    "QuantileLoss[0.5]": 370.64842224121094,
    "Coverage[0.5]": 1.0,
    "RMSE": 32.62099372751899,
    "NRMSE": 0.6867577626846104,
    "ND": 0.6502603631270559,
    "wQuantileLoss[0.5]": 0.6502603898968613,
    "mean_wQuantileLoss": 0.6502603898968613,
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
100%|██████████| 10/10 [00:01<00:00,  6.65it/s, avg_epoch_loss=2.71e+3]
INFO:root:Epoch[0] Elapsed time 1.505 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=2713.411247
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 2713.4112467447917 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7fd8d4183780>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7fd8d4183780>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 125.11it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
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
100%|██████████| 10/10 [00:02<00:00,  4.46it/s, avg_epoch_loss=5.26]
INFO:root:Epoch[0] Elapsed time 2.245 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=5.255549
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 5.255549430847168 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7fd8d413ed68>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7fd8d413ed68>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 127.16it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 241.71036783854166,
    "abs_error": 167.4777069091797,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 1.1096988822597387,
    "sMAPE": 0.2804024022942106,
    "MSIS": 44.38795286389425,
    "QuantileLoss[0.5]": 167.47769165039062,
    "Coverage[0.5]": 0.75,
    "RMSE": 15.54703726883491,
    "NRMSE": 0.3273060477649455,
    "ND": 0.29382053843715733,
    "wQuantileLoss[0.5]": 0.29382051166735196,
    "mean_wQuantileLoss": 0.29382051166735196,
    "MAE_Coverage": 0.25
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
 30%|███       | 3/10 [00:13<00:32,  4.65s/it, avg_epoch_loss=6.93] 60%|██████    | 6/10 [00:26<00:17,  4.48s/it, avg_epoch_loss=6.91] 90%|█████████ | 9/10 [00:38<00:04,  4.35s/it, avg_epoch_loss=6.87]100%|██████████| 10/10 [00:42<00:00,  4.24s/it, avg_epoch_loss=6.86]
INFO:root:Epoch[0] Elapsed time 42.411 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=6.860415
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 6.860415363311768 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7fd8d413e2e8>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7fd8d413e2e8>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 125.85it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 53156.046875,
    "abs_error": 2709.94775390625,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 17.955977837234315,
    "sMAPE": 1.4108461040602285,
    "MSIS": 718.2389840762902,
    "QuantileLoss[0.5]": 2709.947463989258,
    "Coverage[0.5]": 1.0,
    "RMSE": 230.55595172322055,
    "NRMSE": 4.853809509962538,
    "ND": 4.754294305098684,
    "wQuantileLoss[0.5]": 4.754293796472382,
    "mean_wQuantileLoss": 4.754293796472382,
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
100%|██████████| 10/10 [00:00<00:00, 46.42it/s, avg_epoch_loss=5.18]
INFO:root:Epoch[0] Elapsed time 0.216 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=5.184513
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 5.184512948989868 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7fd8d40fa208>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7fd8d40fa208>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 111.98it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 514.2789713541666,
    "abs_error": 183.77935791015625,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 1.2177128038056189,
    "sMAPE": 0.3096148605285104,
    "MSIS": 48.708508916897685,
    "QuantileLoss[0.5]": 183.7793426513672,
    "Coverage[0.5]": 0.6666666666666666,
    "RMSE": 22.677719712399803,
    "NRMSE": 0.47742567815578535,
    "ND": 0.32241992615816883,
    "wQuantileLoss[0.5]": 0.32241989938836346,
    "mean_wQuantileLoss": 0.32241989938836346,
    "MAE_Coverage": 0.16666666666666663
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
100%|██████████| 10/10 [00:01<00:00,  7.33it/s, avg_epoch_loss=161]
INFO:root:Epoch[0] Elapsed time 1.365 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=161.108291
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 161.1082910709855 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7fd8be8f6320>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7fd8be8f6320>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 130.45it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 439.8828247741723,
    "abs_error": 223.62751574072416,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 1.4817446980843618,
    "sMAPE": 0.42600252840216285,
    "MSIS": 59.26978792337448,
    "QuantileLoss[0.5]": 223.62751574072416,
    "Coverage[0.5]": 0.3333333333333333,
    "RMSE": 20.973383722570194,
    "NRMSE": 0.441544920475162,
    "ND": 0.3923289749837266,
    "wQuantileLoss[0.5]": 0.3923289749837266,
    "mean_wQuantileLoss": 0.3923289749837266,
    "MAE_Coverage": 0.16666666666666669
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
 10%|█         | 1/10 [02:06<18:55, 126.13s/it, avg_epoch_loss=0.582] 20%|██        | 2/10 [05:07<19:02, 142.78s/it, avg_epoch_loss=0.565] 30%|███       | 3/10 [08:32<18:49, 161.30s/it, avg_epoch_loss=0.548] 40%|████      | 4/10 [12:08<17:47, 177.84s/it, avg_epoch_loss=0.531] 50%|█████     | 5/10 [15:48<15:52, 190.47s/it, avg_epoch_loss=0.515] 60%|██████    | 6/10 [19:21<13:08, 197.11s/it, avg_epoch_loss=0.499] 70%|███████   | 7/10 [22:43<09:55, 198.66s/it, avg_epoch_loss=0.484] 80%|████████  | 8/10 [26:26<06:51, 205.96s/it, avg_epoch_loss=0.47]  90%|█████████ | 9/10 [29:43<03:23, 203.14s/it, avg_epoch_loss=0.457]100%|██████████| 10/10 [33:18<00:00, 206.73s/it, avg_epoch_loss=0.447]100%|██████████| 10/10 [33:18<00:00, 199.82s/it, avg_epoch_loss=0.447]
INFO:root:Epoch[0] Elapsed time 1998.241 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=0.446552
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 0.4465524971485138 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7fd8d40a5ac8>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7fd8d40a5ac8>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 15.78it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 164.05573527018228,
    "abs_error": 114.22518920898438,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 0.7568503720907435,
    "sMAPE": 0.20283677998139085,
    "MSIS": 30.274016501293268,
    "QuantileLoss[0.5]": 114.22519302368164,
    "Coverage[0.5]": 0.4166666666666667,
    "RMSE": 12.808424386714483,
    "NRMSE": 0.2696510397203049,
    "ND": 0.2003950687876919,
    "wQuantileLoss[0.5]": 0.20039507548014324,
    "mean_wQuantileLoss": 0.20039507548014324,
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
From github.com:arita37/mlmodels_store
   29ee6bb..308e456  master     -> origin/master
Updating 29ee6bb..308e456
Fast-forward
 error_list/20200523/list_log_pullrequest_20200523.md | 2 +-
 error_list/20200523/list_log_testall_20200523.md     | 7 +++++++
 2 files changed, 8 insertions(+), 1 deletion(-)
[master 4cab533] ml_store
 1 file changed, 506 insertions(+)
To github.com:arita37/mlmodels_store.git
   308e456..4cab533  master -> master





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

  <mlmodels.model_sklearn.model_sklearn.Model object at 0x7f8e4ef65198> 

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
[master 30e8a2e] ml_store
 1 file changed, 109 insertions(+)
To github.com:arita37/mlmodels_store.git
   4cab533..30e8a2e  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_sklearn//model_lightgbm.py 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 

  #### save the trained model  ####################################### 

  #### Predict   ##################################################### 
[[ 6.25673373e-01  5.92472801e-01  6.74570707e-01  1.19783084e+00
   1.23187251e+00  1.70459417e+00 -7.67309826e-01  1.04008915e+00
  -9.18440038e-01  1.46089238e+00]
 [ 9.67037267e-01  3.82715174e-01 -8.06184817e-01 -2.88997343e-01
   9.08526041e-01 -3.91816240e-01  1.62091229e+00  6.84001328e-01
  -3.53409983e-01 -2.51674208e-01]
 [ 8.48069266e-01  4.51946037e-01  6.30195671e-01 -1.57915629e+00
   8.27987371e-01 -8.28627979e-01 -1.05344713e-01  5.28879746e-01
  -2.23708651e+00 -4.14846901e-01]
 [ 8.95510508e-01  9.20615118e-01  7.94528240e-01 -3.53679249e-02
   8.78099103e-01  2.11060505e+00 -1.02188594e+00 -1.30653407e+00
   7.63804802e-02 -1.87316098e+00]
 [ 1.13545112e+00  8.61623101e-01  4.90616924e-02 -2.08639057e+00
  -1.11469020e+00  3.61801641e-01 -8.06178212e-01  4.25920177e-01
   4.90803971e-02 -5.96086335e-01]
 [ 1.07258847e+00 -5.86523939e-01 -1.34267579e+00 -1.23685338e+00
   1.24328724e+00  8.75838928e-01 -3.26499498e-01  6.23362177e-01
  -4.34956683e-01  1.11438298e+00]
 [ 8.71225789e-01 -2.09752935e-01 -4.56987858e-01  9.35147780e-01
  -8.73535822e-01  1.81252782e+00  9.25501215e-01  1.40109881e-01
  -1.41914878e+00  1.06898597e+00]
 [ 1.21619061e+00 -1.90005215e-02  8.60891241e-01 -2.26760192e-01
  -1.36419132e+00 -1.56450785e+00  1.63169151e+00  9.31255679e-01
   9.49808815e-01 -8.80189065e-01]
 [ 6.23688521e-01  1.20660790e+00  9.03999174e-01 -2.82863552e-01
  -1.18913787e+00 -2.66326884e-01  1.42361443e+00  1.06897162e+00
   4.03714310e-02  1.57546791e+00]
 [ 8.76994650e-01  1.23225307e+00 -8.67787223e-01 -2.54179868e-01
   8.91891405e-01  1.39984394e+00 -8.77281519e-01 -7.81911683e-01
  -4.37508983e-01 -1.44087602e+00]
 [ 1.18947778e+00 -6.80678141e-01 -5.68244809e-02 -8.45080274e-02
   8.21783210e-01 -2.97361883e-01 -1.86578994e-01  4.17302005e-01
   7.84770651e-01  4.92336556e-01]
 [ 1.34728643e+00 -3.64538050e-01  8.07509886e-02 -4.59717681e-01
  -8.89487596e-01  1.70548352e+00  9.49961101e-02  2.40505552e-01
  -9.99426501e-01 -7.67803746e-01]
 [ 1.98519313e+00  6.74711526e-01 -1.39662042e+00  6.18539131e-01
   1.22382712e+00 -4.43171931e-01 -1.89148284e-03  1.81053491e+00
  -1.30572692e+00 -8.61316361e-01]
 [ 8.15836116e-01 -1.39169388e+00  2.50598029e+00  4.50217742e-01
  -8.82869820e-01  6.27437083e-01 -1.19586151e+00  7.51337235e-01
   1.40395436e-01  1.91979229e+00]
 [ 1.16755486e+00  3.53600971e-02  7.14789597e-01 -1.53879325e+00
   1.10863359e+00 -4.47895185e-01 -1.75592564e+00  6.17985534e-01
  -1.84176326e-01  8.52704062e-01]
 [ 9.97855163e-01 -6.00138799e-01  4.57947076e-01  1.46765263e-01
  -9.33557290e-01  5.71804879e-01  5.72962726e-01 -3.68176565e-02
   1.12368489e-01 -1.78175491e-02]
 [ 6.23629500e-01  9.86352180e-01  1.45391758e+00 -4.66154857e-01
   9.36403332e-01  1.38499134e+00  3.49435894e-02 -1.07296428e+00
   4.95158611e-01  6.61681076e-01]
 [ 3.45715997e-01 -4.13029310e-01 -4.68673816e-01  1.83471763e+00
   7.71514409e-01  5.64382855e-01  2.18628366e-02  2.13782807e+00
  -7.85533997e-01  8.53281222e-01]
 [ 1.05936450e-01 -7.37289628e-01  6.50323214e-01  1.64665066e-01
  -1.53556118e+00  7.78174179e-01  5.03170861e-02  3.09816759e-01
   1.05132077e+00  6.06548400e-01]
 [ 8.57296491e-01  9.56121704e-01 -8.26097432e-01 -7.05840507e-01
   1.13872896e+00  1.19268607e+00  2.82675712e-01 -2.37941936e-01
   1.15528789e+00  6.21082701e-01]
 [ 1.01177337e+00  9.57467711e-02  7.31402517e-01  1.03345080e+00
  -1.42203164e+00 -1.46273275e-01 -1.74549518e-02 -8.57496825e-01
  -9.34181843e-01  9.54495667e-01]
 [ 1.09488485e+00 -6.96245395e-02 -1.16444148e-01  3.53870427e-01
  -1.44189096e+00 -1.86955017e-01  1.29118890e+00 -1.53236162e-01
  -2.43250851e+00 -2.27729800e+00]
 [ 1.06523311e+00 -6.64867767e-01  1.00806543e+00 -1.94504696e+00
  -1.23017555e+00 -9.15424368e-01  3.37220938e-01  1.22515585e+00
  -1.05354607e+00  7.85226920e-01]
 [ 7.83440538e-01 -5.11884476e-02  8.24584625e-01 -7.25597119e-01
   9.31717197e-01 -8.67768678e-01  3.03085711e+00 -1.35977326e-01
  -7.97269785e-01  6.54580153e-01]
 [ 1.14809657e+00 -7.33271604e-01  2.62467445e-01  8.36004719e-01
   1.17353145e+00  1.54335911e+00  2.84748111e-01  7.58805660e-01
   8.84908814e-01  2.76499305e-01]]

  #### metrics   ##################################################### 
{}

  #### Plot   ######################################################## 

  #### Save/Load   ################################################### 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_sklearn/model_lightgbm/model.pkl'}
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_sklearn/model_lightgbm/model.pkl'}
<__main__.Model object at 0x7f931d933d30>

  #### Module init   ############################################ 

  <module 'mlmodels.model_sklearn.model_lightgbm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_sklearn/model_lightgbm.py'> 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Model init   ############################################ 

  <mlmodels.model_sklearn.model_lightgbm.Model object at 0x7f9337ca35c0> 

  #### Fit   ######################################################## 

  #### Predict   #################################################### 
[[ 1.01195228 -1.88141087  1.70018815  0.4972691  -0.91766462  0.2373327
  -1.09033833 -2.14444405 -0.36956243  0.60878366]
 [ 0.69174373  1.00978733 -1.21333813 -1.55694156 -1.20257258 -0.61244213
  -2.69836174 -0.13935181 -0.72853749  0.0722519 ]
 [ 0.8786438   1.03703898 -0.47712421  0.67261975 -1.04948638  2.42887697
   0.52475049  1.00568668  0.35356722 -0.03599018]
 [ 0.62153099 -1.50957268 -0.10193204 -1.08071069 -1.13742855  0.725474
   0.7980638  -0.03917826 -0.22875417  0.74335654]
 [ 1.24549398 -0.72239191  1.1181334   1.09899633  1.00277655 -0.90163449
  -0.53223402 -0.82246719  0.72171129  0.6743961 ]
 [ 1.58463774  0.057121   -0.01771832 -0.79954749  1.32970299 -0.2915946
  -1.1077125  -0.25898285  0.1892932  -1.71939447]
 [ 1.34740825  0.73302323  0.83863475 -1.89881206 -0.54245992 -1.11711069
  -1.09715436 -0.50897228 -0.16648595 -1.03918232]
 [ 1.1437713   0.7278135   0.35249436  0.51507361  1.17718111 -2.78253447
  -1.94332341  0.58464661  0.32427424 -0.23643695]
 [ 1.12062155 -0.7029204  -1.22957425  0.72555052 -1.18013412 -0.32420422
   1.10223673  0.81434313  0.78046993  1.10861676]
 [ 1.09488485 -0.06962454 -0.11644415  0.35387043 -1.44189096 -0.18695502
   1.2911889  -0.15323616 -2.43250851 -2.277298  ]
 [ 0.89551051  0.92061512  0.79452824 -0.03536792  0.8780991   2.11060505
  -1.02188594 -1.30653407  0.07638048 -1.87316098]
 [ 0.44118981  0.47985237 -0.1920037  -1.55269878 -1.88873982  0.57846442
   0.39859839 -0.9612636  -1.45832446 -3.05376438]
 [ 1.02817479 -0.50845713  1.7653351   0.77741921  0.61771419 -0.11877117
   0.45015551 -0.19899818  1.86647138  0.8709698 ]
 [ 0.77528533  1.47016034  1.03298378 -0.87000822  0.78655651  0.36919047
  -0.14319575  0.85328219 -0.13971173 -0.22241403]
 [ 1.06702918 -0.42914228  0.35016716  1.20845633  0.75148062  1.1157018
  -0.4791571   0.84086156 -0.10288722  0.01716473]
 [ 1.77547698 -0.20339445 -0.19883786  0.24266944  0.96435056  0.20183018
  -0.54577417  0.66102029  1.79215821 -0.7003985 ]
 [ 1.64661853 -1.52568032 -0.6069984   0.79502609  1.08480038 -0.37443832
   0.42952614  0.1340482   1.20205486  0.10622272]
 [ 0.84806927  0.45194604  0.63019567 -1.57915629  0.82798737 -0.82862798
  -0.10534471  0.52887975 -2.23708651 -0.4148469 ]
 [ 1.02242019  1.85300949  0.64435367  0.14225137  1.15080755  0.51350548
  -0.45994283  0.37245685 -0.1484898   0.37167029]
 [ 0.6109426  -2.79099641 -1.33520272 -0.45611756 -0.94495995 -0.97989025
  -0.15699367  0.69257435 -0.47867236 -0.10646012]
 [ 0.76170668 -1.48515645  1.30253554 -0.59246129 -1.64162479 -2.30490794
  -1.34869645 -0.03181717  0.11248774 -0.36261209]
 [ 0.5630779  -1.17598267 -0.17418034  1.01012718  1.06796368  0.92001793
  -0.16819884 -0.19505734  0.80539342  0.4611641 ]
 [ 0.96457205 -0.10679399  1.12232832  1.45142926  1.21828168 -0.61803685
   0.43816635 -2.03720123 -1.94258918 -0.9970198 ]
 [ 1.01177337  0.09574677  0.73140252  1.0334508  -1.42203164 -0.14627327
  -0.01745495 -0.85749682 -0.93418184  0.95449567]
 [ 0.99785516 -0.6001388   0.45794708  0.14676526 -0.93355729  0.57180488
   0.57296273 -0.03681766  0.11236849 -0.01781755]]
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
[[ 4.67397905e-01 -2.37875265e-01 -1.54491194e-01 -7.55662765e-01
  -5.47062239e-01  1.85143789e+00 -1.46405357e+00  2.09096677e-01
   1.55501599e+00 -9.24323185e-02]
 [ 9.67037267e-01  3.82715174e-01 -8.06184817e-01 -2.88997343e-01
   9.08526041e-01 -3.91816240e-01  1.62091229e+00  6.84001328e-01
  -3.53409983e-01 -2.51674208e-01]
 [ 1.46893146e+00 -1.47115693e+00  5.85910431e-01 -8.30171895e-01
   1.03345052e+00 -8.80577600e-01 -9.55425262e-01 -2.79097722e-01
   1.62284909e+00  2.06578332e+00]
 [ 1.21619061e+00 -1.90005215e-02  8.60891241e-01 -2.26760192e-01
  -1.36419132e+00 -1.56450785e+00  1.63169151e+00  9.31255679e-01
   9.49808815e-01 -8.80189065e-01]
 [ 1.98519313e+00  6.74711526e-01 -1.39662042e+00  6.18539131e-01
   1.22382712e+00 -4.43171931e-01 -1.89148284e-03  1.81053491e+00
  -1.30572692e+00 -8.61316361e-01]
 [ 8.95623122e-01 -2.29820588e+00 -1.95225583e-02  1.45652739e+00
  -1.85064099e+00  3.16637236e-01  1.11337266e-01 -2.66412594e+00
  -4.26428618e-01 -8.39988915e-01]
 [ 1.44682180e+00  8.07455917e-01  1.49810818e+00  3.12238689e-01
  -6.82430193e-01 -1.93321640e-01  2.88078167e-01 -2.07680202e+00
   9.47501167e-01 -3.00976154e-01]
 [ 9.26869810e-01  3.92334911e-01 -4.23478297e-01  4.48380651e-01
  -1.09230828e+00  1.12532350e+00 -9.48439656e-01  1.04053390e-01
   5.28003422e-01  1.00796648e+00]
 [ 1.14377130e+00  7.27813500e-01  3.52494364e-01  5.15073614e-01
   1.17718111e+00 -2.78253447e+00 -1.94332341e+00  5.84646610e-01
   3.24274243e-01 -2.36436952e-01]
 [ 9.97855163e-01 -6.00138799e-01  4.57947076e-01  1.46765263e-01
  -9.33557290e-01  5.71804879e-01  5.72962726e-01 -3.68176565e-02
   1.12368489e-01 -1.78175491e-02]
 [ 1.05936450e-01 -7.37289628e-01  6.50323214e-01  1.64665066e-01
  -1.53556118e+00  7.78174179e-01  5.03170861e-02  3.09816759e-01
   1.05132077e+00  6.06548400e-01]
 [ 1.01177337e+00  9.57467711e-02  7.31402517e-01  1.03345080e+00
  -1.42203164e+00 -1.46273275e-01 -1.74549518e-02 -8.57496825e-01
  -9.34181843e-01  9.54495667e-01]
 [ 1.12062155e+00 -7.02920403e-01 -1.22957425e+00  7.25550518e-01
  -1.18013412e+00 -3.24204219e-01  1.10223673e+00  8.14343129e-01
   7.80469930e-01  1.10861676e+00]
 [ 4.41189807e-01  4.79852371e-01 -1.92003697e-01 -1.55269878e+00
  -1.88873982e+00  5.78464420e-01  3.98598388e-01 -9.61263599e-01
  -1.45832446e+00 -3.05376438e+00]
 [ 1.07258847e+00 -5.86523939e-01 -1.34267579e+00 -1.23685338e+00
   1.24328724e+00  8.75838928e-01 -3.26499498e-01  6.23362177e-01
  -4.34956683e-01  1.11438298e+00]
 [ 1.16755486e+00  3.53600971e-02  7.14789597e-01 -1.53879325e+00
   1.10863359e+00 -4.47895185e-01 -1.75592564e+00  6.17985534e-01
  -1.84176326e-01  8.52704062e-01]
 [ 9.80427414e-01  1.93752881e+00 -2.30839743e-01  3.66332015e-01
   1.10018476e+00 -1.04458938e+00 -3.44987210e-01  2.05117344e+00
   5.85662000e-01 -2.79308500e+00]
 [ 6.10942600e-01 -2.79099641e+00 -1.33520272e+00 -4.56117555e-01
  -9.44959948e-01 -9.79890252e-01 -1.56993672e-01  6.92574348e-01
  -4.78672356e-01 -1.06460122e-01]
 [ 1.32857949e+00 -5.63236604e-01 -1.06179676e+00  2.39014596e+00
  -1.68450770e+00  2.45422849e-01 -5.69148654e-01  1.15259914e+00
  -2.24235772e-01  1.32247779e-01]
 [ 1.77547698e+00 -2.03394449e-01 -1.98837863e-01  2.42669441e-01
   9.64350564e-01  2.01830179e-01 -5.45774168e-01  6.61020288e-01
   1.79215821e+00 -7.00398505e-01]
 [ 6.25673373e-01  5.92472801e-01  6.74570707e-01  1.19783084e+00
   1.23187251e+00  1.70459417e+00 -7.67309826e-01  1.04008915e+00
  -9.18440038e-01  1.46089238e+00]
 [ 8.76994650e-01  1.23225307e+00 -8.67787223e-01 -2.54179868e-01
   8.91891405e-01  1.39984394e+00 -8.77281519e-01 -7.81911683e-01
  -4.37508983e-01 -1.44087602e+00]
 [ 8.72267394e-01 -2.51630386e+00 -7.75070287e-01 -5.95667881e-01
   1.02600767e+00 -3.09121319e-01  1.74643509e+00  5.10937774e-01
   1.71066184e+00  1.41640538e-01]
 [ 1.34740825e+00  7.33023232e-01  8.38634747e-01 -1.89881206e+00
  -5.42459922e-01 -1.11711069e+00 -1.09715436e+00 -5.08972278e-01
  -1.66485955e-01 -1.03918232e+00]
 [ 7.90323893e-01  1.61336137e+00 -2.09424782e+00 -3.74804687e-01
   9.15884042e-01 -7.49969617e-01  3.10272288e-01  2.05462410e+00
   5.34095368e-02 -2.28765829e-01]]
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
[master b40cd55] ml_store
 1 file changed, 297 insertions(+)
To github.com:arita37/mlmodels_store.git
   30e8a2e..b40cd55  master -> master





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
     | -- GenericBlock(units=256, thetas_dim=7, backcast_length=10, forecast_length=5, share_thetas=False) at @139919422017488
     | -- GenericBlock(units=256, thetas_dim=7, backcast_length=10, forecast_length=5, share_thetas=False) at @139919422017264
     | -- GenericBlock(units=256, thetas_dim=7, backcast_length=10, forecast_length=5, share_thetas=False) at @139919422016032
| --  Stack Generic (#1) (share_weights_in_stack=0)
     | -- GenericBlock(units=256, thetas_dim=8, backcast_length=10, forecast_length=5, share_thetas=False) at @139919422015584
     | -- GenericBlock(units=256, thetas_dim=8, backcast_length=10, forecast_length=5, share_thetas=False) at @139919422015080
     | -- GenericBlock(units=256, thetas_dim=8, backcast_length=10, forecast_length=5, share_thetas=False) at @139919422014744

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
grad_step = 000000, loss = 1.004605
plot()
Saved image to .//n_beats_0.png.
grad_step = 000001, loss = 0.837543
grad_step = 000002, loss = 0.743604
grad_step = 000003, loss = 0.634293
grad_step = 000004, loss = 0.521917
grad_step = 000005, loss = 0.430654
grad_step = 000006, loss = 0.382663
grad_step = 000007, loss = 0.350765
grad_step = 000008, loss = 0.279802
grad_step = 000009, loss = 0.200817
grad_step = 000010, loss = 0.133000
grad_step = 000011, loss = 0.085402
grad_step = 000012, loss = 0.060901
grad_step = 000013, loss = 0.058107
grad_step = 000014, loss = 0.057731
grad_step = 000015, loss = 0.042890
grad_step = 000016, loss = 0.023621
grad_step = 000017, loss = 0.014828
grad_step = 000018, loss = 0.021571
grad_step = 000019, loss = 0.031897
grad_step = 000020, loss = 0.034039
grad_step = 000021, loss = 0.028649
grad_step = 000022, loss = 0.021559
grad_step = 000023, loss = 0.017256
grad_step = 000024, loss = 0.016155
grad_step = 000025, loss = 0.015363
grad_step = 000026, loss = 0.013002
grad_step = 000027, loss = 0.010026
grad_step = 000028, loss = 0.008292
grad_step = 000029, loss = 0.008459
grad_step = 000030, loss = 0.009739
grad_step = 000031, loss = 0.010895
grad_step = 000032, loss = 0.011016
grad_step = 000033, loss = 0.010046
grad_step = 000034, loss = 0.008540
grad_step = 000035, loss = 0.007422
grad_step = 000036, loss = 0.007216
grad_step = 000037, loss = 0.007652
grad_step = 000038, loss = 0.008024
grad_step = 000039, loss = 0.007914
grad_step = 000040, loss = 0.007384
grad_step = 000041, loss = 0.006626
grad_step = 000042, loss = 0.005821
grad_step = 000043, loss = 0.005268
grad_step = 000044, loss = 0.005272
grad_step = 000045, loss = 0.005694
grad_step = 000046, loss = 0.005959
grad_step = 000047, loss = 0.005811
grad_step = 000048, loss = 0.005506
grad_step = 000049, loss = 0.005267
grad_step = 000050, loss = 0.005072
grad_step = 000051, loss = 0.004931
grad_step = 000052, loss = 0.004951
grad_step = 000053, loss = 0.005044
grad_step = 000054, loss = 0.004950
grad_step = 000055, loss = 0.004682
grad_step = 000056, loss = 0.004467
grad_step = 000057, loss = 0.004389
grad_step = 000058, loss = 0.004343
grad_step = 000059, loss = 0.004291
grad_step = 000060, loss = 0.004260
grad_step = 000061, loss = 0.004182
grad_step = 000062, loss = 0.004046
grad_step = 000063, loss = 0.003957
grad_step = 000064, loss = 0.003944
grad_step = 000065, loss = 0.003924
grad_step = 000066, loss = 0.003851
grad_step = 000067, loss = 0.003759
grad_step = 000068, loss = 0.003667
grad_step = 000069, loss = 0.003584
grad_step = 000070, loss = 0.003537
grad_step = 000071, loss = 0.003517
grad_step = 000072, loss = 0.003465
grad_step = 000073, loss = 0.003382
grad_step = 000074, loss = 0.003312
grad_step = 000075, loss = 0.003260
grad_step = 000076, loss = 0.003215
grad_step = 000077, loss = 0.003179
grad_step = 000078, loss = 0.003130
grad_step = 000079, loss = 0.003061
grad_step = 000080, loss = 0.003009
grad_step = 000081, loss = 0.002971
grad_step = 000082, loss = 0.002929
grad_step = 000083, loss = 0.002885
grad_step = 000084, loss = 0.002834
grad_step = 000085, loss = 0.002791
grad_step = 000086, loss = 0.002762
grad_step = 000087, loss = 0.002726
grad_step = 000088, loss = 0.002685
grad_step = 000089, loss = 0.002646
grad_step = 000090, loss = 0.002610
grad_step = 000091, loss = 0.002581
grad_step = 000092, loss = 0.002546
grad_step = 000093, loss = 0.002511
grad_step = 000094, loss = 0.002479
grad_step = 000095, loss = 0.002450
grad_step = 000096, loss = 0.002420
grad_step = 000097, loss = 0.002389
grad_step = 000098, loss = 0.002363
grad_step = 000099, loss = 0.002336
grad_step = 000100, loss = 0.002307
plot()
Saved image to .//n_beats_100.png.
grad_step = 000101, loss = 0.002280
grad_step = 000102, loss = 0.002255
grad_step = 000103, loss = 0.002228
grad_step = 000104, loss = 0.002202
grad_step = 000105, loss = 0.002179
grad_step = 000106, loss = 0.002152
grad_step = 000107, loss = 0.002126
grad_step = 000108, loss = 0.002104
grad_step = 000109, loss = 0.002080
grad_step = 000110, loss = 0.002056
grad_step = 000111, loss = 0.002034
grad_step = 000112, loss = 0.002010
grad_step = 000113, loss = 0.001987
grad_step = 000114, loss = 0.001964
grad_step = 000115, loss = 0.001941
grad_step = 000116, loss = 0.001919
grad_step = 000117, loss = 0.001895
grad_step = 000118, loss = 0.001872
grad_step = 000119, loss = 0.001851
grad_step = 000120, loss = 0.001829
grad_step = 000121, loss = 0.001806
grad_step = 000122, loss = 0.001783
grad_step = 000123, loss = 0.001757
grad_step = 000124, loss = 0.001734
grad_step = 000125, loss = 0.001708
grad_step = 000126, loss = 0.001684
grad_step = 000127, loss = 0.001660
grad_step = 000128, loss = 0.001635
grad_step = 000129, loss = 0.001611
grad_step = 000130, loss = 0.001586
grad_step = 000131, loss = 0.001566
grad_step = 000132, loss = 0.001555
grad_step = 000133, loss = 0.001549
grad_step = 000134, loss = 0.001519
grad_step = 000135, loss = 0.001472
grad_step = 000136, loss = 0.001453
grad_step = 000137, loss = 0.001448
grad_step = 000138, loss = 0.001418
grad_step = 000139, loss = 0.001386
grad_step = 000140, loss = 0.001376
grad_step = 000141, loss = 0.001362
grad_step = 000142, loss = 0.001331
grad_step = 000143, loss = 0.001308
grad_step = 000144, loss = 0.001297
grad_step = 000145, loss = 0.001281
grad_step = 000146, loss = 0.001255
grad_step = 000147, loss = 0.001233
grad_step = 000148, loss = 0.001220
grad_step = 000149, loss = 0.001206
grad_step = 000150, loss = 0.001186
grad_step = 000151, loss = 0.001164
grad_step = 000152, loss = 0.001147
grad_step = 000153, loss = 0.001133
grad_step = 000154, loss = 0.001120
grad_step = 000155, loss = 0.001104
grad_step = 000156, loss = 0.001086
grad_step = 000157, loss = 0.001067
grad_step = 000158, loss = 0.001050
grad_step = 000159, loss = 0.001036
grad_step = 000160, loss = 0.001025
grad_step = 000161, loss = 0.001015
grad_step = 000162, loss = 0.001005
grad_step = 000163, loss = 0.000991
grad_step = 000164, loss = 0.000975
grad_step = 000165, loss = 0.000956
grad_step = 000166, loss = 0.000937
grad_step = 000167, loss = 0.000921
grad_step = 000168, loss = 0.000909
grad_step = 000169, loss = 0.000900
grad_step = 000170, loss = 0.000891
grad_step = 000171, loss = 0.000882
grad_step = 000172, loss = 0.000871
grad_step = 000173, loss = 0.000856
grad_step = 000174, loss = 0.000838
grad_step = 000175, loss = 0.000820
grad_step = 000176, loss = 0.000805
grad_step = 000177, loss = 0.000794
grad_step = 000178, loss = 0.000785
grad_step = 000179, loss = 0.000778
grad_step = 000180, loss = 0.000772
grad_step = 000181, loss = 0.000765
grad_step = 000182, loss = 0.000755
grad_step = 000183, loss = 0.000740
grad_step = 000184, loss = 0.000723
grad_step = 000185, loss = 0.000708
grad_step = 000186, loss = 0.000697
grad_step = 000187, loss = 0.000692
grad_step = 000188, loss = 0.000688
grad_step = 000189, loss = 0.000682
grad_step = 000190, loss = 0.000675
grad_step = 000191, loss = 0.000665
grad_step = 000192, loss = 0.000654
grad_step = 000193, loss = 0.000644
grad_step = 000194, loss = 0.000637
grad_step = 000195, loss = 0.000632
grad_step = 000196, loss = 0.000628
grad_step = 000197, loss = 0.000624
grad_step = 000198, loss = 0.000619
grad_step = 000199, loss = 0.000613
grad_step = 000200, loss = 0.000607
plot()
Saved image to .//n_beats_200.png.
grad_step = 000201, loss = 0.000601
grad_step = 000202, loss = 0.000594
grad_step = 000203, loss = 0.000588
grad_step = 000204, loss = 0.000583
grad_step = 000205, loss = 0.000578
grad_step = 000206, loss = 0.000574
grad_step = 000207, loss = 0.000570
grad_step = 000208, loss = 0.000568
grad_step = 000209, loss = 0.000567
grad_step = 000210, loss = 0.000569
grad_step = 000211, loss = 0.000578
grad_step = 000212, loss = 0.000598
grad_step = 000213, loss = 0.000634
grad_step = 000214, loss = 0.000651
grad_step = 000215, loss = 0.000629
grad_step = 000216, loss = 0.000563
grad_step = 000217, loss = 0.000538
grad_step = 000218, loss = 0.000571
grad_step = 000219, loss = 0.000590
grad_step = 000220, loss = 0.000563
grad_step = 000221, loss = 0.000527
grad_step = 000222, loss = 0.000536
grad_step = 000223, loss = 0.000560
grad_step = 000224, loss = 0.000548
grad_step = 000225, loss = 0.000521
grad_step = 000226, loss = 0.000517
grad_step = 000227, loss = 0.000532
grad_step = 000228, loss = 0.000533
grad_step = 000229, loss = 0.000514
grad_step = 000230, loss = 0.000505
grad_step = 000231, loss = 0.000512
grad_step = 000232, loss = 0.000517
grad_step = 000233, loss = 0.000509
grad_step = 000234, loss = 0.000497
grad_step = 000235, loss = 0.000496
grad_step = 000236, loss = 0.000501
grad_step = 000237, loss = 0.000500
grad_step = 000238, loss = 0.000492
grad_step = 000239, loss = 0.000485
grad_step = 000240, loss = 0.000485
grad_step = 000241, loss = 0.000487
grad_step = 000242, loss = 0.000485
grad_step = 000243, loss = 0.000480
grad_step = 000244, loss = 0.000474
grad_step = 000245, loss = 0.000472
grad_step = 000246, loss = 0.000473
grad_step = 000247, loss = 0.000472
grad_step = 000248, loss = 0.000470
grad_step = 000249, loss = 0.000465
grad_step = 000250, loss = 0.000462
grad_step = 000251, loss = 0.000459
grad_step = 000252, loss = 0.000459
grad_step = 000253, loss = 0.000458
grad_step = 000254, loss = 0.000457
grad_step = 000255, loss = 0.000455
grad_step = 000256, loss = 0.000453
grad_step = 000257, loss = 0.000449
grad_step = 000258, loss = 0.000446
grad_step = 000259, loss = 0.000444
grad_step = 000260, loss = 0.000442
grad_step = 000261, loss = 0.000440
grad_step = 000262, loss = 0.000439
grad_step = 000263, loss = 0.000438
grad_step = 000264, loss = 0.000437
grad_step = 000265, loss = 0.000438
grad_step = 000266, loss = 0.000440
grad_step = 000267, loss = 0.000442
grad_step = 000268, loss = 0.000447
grad_step = 000269, loss = 0.000452
grad_step = 000270, loss = 0.000457
grad_step = 000271, loss = 0.000460
grad_step = 000272, loss = 0.000460
grad_step = 000273, loss = 0.000452
grad_step = 000274, loss = 0.000440
grad_step = 000275, loss = 0.000425
grad_step = 000276, loss = 0.000415
grad_step = 000277, loss = 0.000412
grad_step = 000278, loss = 0.000415
grad_step = 000279, loss = 0.000420
grad_step = 000280, loss = 0.000424
grad_step = 000281, loss = 0.000427
grad_step = 000282, loss = 0.000425
grad_step = 000283, loss = 0.000419
grad_step = 000284, loss = 0.000411
grad_step = 000285, loss = 0.000403
grad_step = 000286, loss = 0.000398
grad_step = 000287, loss = 0.000396
grad_step = 000288, loss = 0.000397
grad_step = 000289, loss = 0.000399
grad_step = 000290, loss = 0.000402
grad_step = 000291, loss = 0.000403
grad_step = 000292, loss = 0.000405
grad_step = 000293, loss = 0.000403
grad_step = 000294, loss = 0.000400
grad_step = 000295, loss = 0.000394
grad_step = 000296, loss = 0.000389
grad_step = 000297, loss = 0.000385
grad_step = 000298, loss = 0.000381
grad_step = 000299, loss = 0.000378
grad_step = 000300, loss = 0.000376
plot()
Saved image to .//n_beats_300.png.
grad_step = 000301, loss = 0.000375
grad_step = 000302, loss = 0.000374
grad_step = 000303, loss = 0.000373
grad_step = 000304, loss = 0.000373
grad_step = 000305, loss = 0.000374
grad_step = 000306, loss = 0.000377
grad_step = 000307, loss = 0.000384
grad_step = 000308, loss = 0.000394
grad_step = 000309, loss = 0.000412
grad_step = 000310, loss = 0.000432
grad_step = 000311, loss = 0.000458
grad_step = 000312, loss = 0.000459
grad_step = 000313, loss = 0.000440
grad_step = 000314, loss = 0.000395
grad_step = 000315, loss = 0.000361
grad_step = 000316, loss = 0.000359
grad_step = 000317, loss = 0.000382
grad_step = 000318, loss = 0.000402
grad_step = 000319, loss = 0.000398
grad_step = 000320, loss = 0.000377
grad_step = 000321, loss = 0.000355
grad_step = 000322, loss = 0.000349
grad_step = 000323, loss = 0.000359
grad_step = 000324, loss = 0.000369
grad_step = 000325, loss = 0.000368
grad_step = 000326, loss = 0.000356
grad_step = 000327, loss = 0.000344
grad_step = 000328, loss = 0.000341
grad_step = 000329, loss = 0.000347
grad_step = 000330, loss = 0.000353
grad_step = 000331, loss = 0.000353
grad_step = 000332, loss = 0.000347
grad_step = 000333, loss = 0.000339
grad_step = 000334, loss = 0.000334
grad_step = 000335, loss = 0.000334
grad_step = 000336, loss = 0.000337
grad_step = 000337, loss = 0.000339
grad_step = 000338, loss = 0.000338
grad_step = 000339, loss = 0.000337
grad_step = 000340, loss = 0.000332
grad_step = 000341, loss = 0.000328
grad_step = 000342, loss = 0.000325
grad_step = 000343, loss = 0.000325
grad_step = 000344, loss = 0.000326
grad_step = 000345, loss = 0.000326
grad_step = 000346, loss = 0.000326
grad_step = 000347, loss = 0.000326
grad_step = 000348, loss = 0.000325
grad_step = 000349, loss = 0.000322
grad_step = 000350, loss = 0.000320
grad_step = 000351, loss = 0.000317
grad_step = 000352, loss = 0.000315
grad_step = 000353, loss = 0.000314
grad_step = 000354, loss = 0.000313
grad_step = 000355, loss = 0.000312
grad_step = 000356, loss = 0.000311
grad_step = 000357, loss = 0.000311
grad_step = 000358, loss = 0.000311
grad_step = 000359, loss = 0.000313
grad_step = 000360, loss = 0.000316
grad_step = 000361, loss = 0.000324
grad_step = 000362, loss = 0.000333
grad_step = 000363, loss = 0.000345
grad_step = 000364, loss = 0.000359
grad_step = 000365, loss = 0.000379
grad_step = 000366, loss = 0.000389
grad_step = 000367, loss = 0.000391
grad_step = 000368, loss = 0.000364
grad_step = 000369, loss = 0.000331
grad_step = 000370, loss = 0.000306
grad_step = 000371, loss = 0.000300
grad_step = 000372, loss = 0.000308
grad_step = 000373, loss = 0.000320
grad_step = 000374, loss = 0.000329
grad_step = 000375, loss = 0.000328
grad_step = 000376, loss = 0.000319
grad_step = 000377, loss = 0.000306
grad_step = 000378, loss = 0.000296
grad_step = 000379, loss = 0.000290
grad_step = 000380, loss = 0.000293
grad_step = 000381, loss = 0.000299
grad_step = 000382, loss = 0.000305
grad_step = 000383, loss = 0.000306
grad_step = 000384, loss = 0.000300
grad_step = 000385, loss = 0.000291
grad_step = 000386, loss = 0.000284
grad_step = 000387, loss = 0.000281
grad_step = 000388, loss = 0.000282
grad_step = 000389, loss = 0.000287
grad_step = 000390, loss = 0.000291
grad_step = 000391, loss = 0.000291
grad_step = 000392, loss = 0.000288
grad_step = 000393, loss = 0.000282
grad_step = 000394, loss = 0.000277
grad_step = 000395, loss = 0.000276
grad_step = 000396, loss = 0.000277
grad_step = 000397, loss = 0.000281
grad_step = 000398, loss = 0.000287
grad_step = 000399, loss = 0.000293
grad_step = 000400, loss = 0.000291
plot()
Saved image to .//n_beats_400.png.
grad_step = 000401, loss = 0.000285
grad_step = 000402, loss = 0.000277
grad_step = 000403, loss = 0.000273
grad_step = 000404, loss = 0.000273
grad_step = 000405, loss = 0.000278
grad_step = 000406, loss = 0.000284
grad_step = 000407, loss = 0.000292
grad_step = 000408, loss = 0.000295
grad_step = 000409, loss = 0.000296
grad_step = 000410, loss = 0.000292
grad_step = 000411, loss = 0.000292
grad_step = 000412, loss = 0.000302
grad_step = 000413, loss = 0.000326
grad_step = 000414, loss = 0.000351
grad_step = 000415, loss = 0.000378
grad_step = 000416, loss = 0.000360
grad_step = 000417, loss = 0.000348
grad_step = 000418, loss = 0.000335
grad_step = 000419, loss = 0.000333
grad_step = 000420, loss = 0.000317
grad_step = 000421, loss = 0.000273
grad_step = 000422, loss = 0.000258
grad_step = 000423, loss = 0.000280
grad_step = 000424, loss = 0.000306
grad_step = 000425, loss = 0.000307
grad_step = 000426, loss = 0.000287
grad_step = 000427, loss = 0.000272
grad_step = 000428, loss = 0.000274
grad_step = 000429, loss = 0.000279
grad_step = 000430, loss = 0.000268
grad_step = 000431, loss = 0.000254
grad_step = 000432, loss = 0.000255
grad_step = 000433, loss = 0.000267
grad_step = 000434, loss = 0.000275
grad_step = 000435, loss = 0.000271
grad_step = 000436, loss = 0.000264
grad_step = 000437, loss = 0.000262
grad_step = 000438, loss = 0.000264
grad_step = 000439, loss = 0.000263
grad_step = 000440, loss = 0.000257
grad_step = 000441, loss = 0.000249
grad_step = 000442, loss = 0.000246
grad_step = 000443, loss = 0.000247
grad_step = 000444, loss = 0.000248
grad_step = 000445, loss = 0.000248
grad_step = 000446, loss = 0.000246
grad_step = 000447, loss = 0.000244
grad_step = 000448, loss = 0.000244
grad_step = 000449, loss = 0.000245
grad_step = 000450, loss = 0.000249
grad_step = 000451, loss = 0.000252
grad_step = 000452, loss = 0.000258
grad_step = 000453, loss = 0.000268
grad_step = 000454, loss = 0.000284
grad_step = 000455, loss = 0.000306
grad_step = 000456, loss = 0.000337
grad_step = 000457, loss = 0.000363
grad_step = 000458, loss = 0.000393
grad_step = 000459, loss = 0.000385
grad_step = 000460, loss = 0.000366
grad_step = 000461, loss = 0.000319
grad_step = 000462, loss = 0.000287
grad_step = 000463, loss = 0.000276
grad_step = 000464, loss = 0.000266
grad_step = 000465, loss = 0.000277
grad_step = 000466, loss = 0.000294
grad_step = 000467, loss = 0.000303
grad_step = 000468, loss = 0.000279
grad_step = 000469, loss = 0.000246
grad_step = 000470, loss = 0.000236
grad_step = 000471, loss = 0.000253
grad_step = 000472, loss = 0.000273
grad_step = 000473, loss = 0.000270
grad_step = 000474, loss = 0.000249
grad_step = 000475, loss = 0.000231
grad_step = 000476, loss = 0.000235
grad_step = 000477, loss = 0.000252
grad_step = 000478, loss = 0.000258
grad_step = 000479, loss = 0.000250
grad_step = 000480, loss = 0.000241
grad_step = 000481, loss = 0.000246
grad_step = 000482, loss = 0.000254
grad_step = 000483, loss = 0.000257
grad_step = 000484, loss = 0.000240
grad_step = 000485, loss = 0.000230
grad_step = 000486, loss = 0.000232
grad_step = 000487, loss = 0.000237
grad_step = 000488, loss = 0.000238
grad_step = 000489, loss = 0.000234
grad_step = 000490, loss = 0.000229
grad_step = 000491, loss = 0.000230
grad_step = 000492, loss = 0.000238
grad_step = 000493, loss = 0.000253
grad_step = 000494, loss = 0.000276
grad_step = 000495, loss = 0.000303
grad_step = 000496, loss = 0.000334
grad_step = 000497, loss = 0.000329
grad_step = 000498, loss = 0.000312
grad_step = 000499, loss = 0.000273
grad_step = 000500, loss = 0.000242
plot()
Saved image to .//n_beats_500.png.
grad_step = 000501, loss = 0.000231
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
[[0.8539784  0.8611819  0.94618404 0.962068   1.0055956 ]
 [0.86414766 0.9317067  0.9436656  1.0206062  0.9941055 ]
 [0.91005194 0.92684406 0.9928022  0.9964771  0.9476328 ]
 [0.9328622  0.98298264 0.98651505 0.9455529  0.92214286]
 [0.9822485  0.9942537  0.95372915 0.9201446  0.8600321 ]
 [0.96866626 0.95297027 0.9064746  0.8642859  0.8537821 ]
 [0.9391481  0.91424125 0.8522546  0.86478317 0.8181355 ]
 [0.89484787 0.84976566 0.84653366 0.82150406 0.8503688 ]
 [0.8239378  0.8397037  0.80728894 0.83488935 0.8638099 ]
 [0.84092957 0.8013386  0.8362471  0.86850536 0.83803433]
 [0.8115669  0.8267354  0.84327674 0.82305515 0.92320573]
 [0.8154059  0.8613895  0.819488   0.9308742  0.9297265 ]
 [0.845988   0.85967827 0.94058096 0.96325874 1.0037282 ]
 [0.86494607 0.93460935 0.94524074 1.0171884  0.9879411 ]
 [0.91983503 0.93748236 0.99287635 0.98772675 0.93012685]
 [0.94437265 0.9877475  0.9804311  0.93230236 0.8982692 ]
 [0.98870486 0.9866174  0.9400319  0.90586305 0.8297743 ]
 [0.9651787  0.9401013  0.88900566 0.8470045  0.8399289 ]
 [0.93846947 0.9067234  0.83611655 0.84911656 0.81458765]
 [0.9071166  0.8495721  0.8424161  0.8195642  0.84936863]
 [0.84128946 0.84687215 0.80818796 0.835498   0.86884964]
 [0.85757065 0.8114196  0.8360816  0.8740216  0.8444721 ]
 [0.82537764 0.8307007  0.84996665 0.8304703  0.93062556]
 [0.8304693  0.8654645  0.82386184 0.9305891  0.9304136 ]
 [0.8585692  0.86752665 0.94288504 0.9650066  1.0114    ]
 [0.87216854 0.94123966 0.9465042  1.0285279  1.0054799 ]
 [0.91980606 0.93361866 1.0006293  1.0111413  0.95886374]
 [0.9460406  0.98985684 0.99770314 0.96019024 0.9316945 ]
 [0.99258214 1.0018371  0.9646913  0.93431836 0.8651462 ]
 [0.97934127 0.96033454 0.91341823 0.8761493  0.85629165]
 [0.9481922  0.9214734  0.85756874 0.8697065  0.82535   ]]

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
