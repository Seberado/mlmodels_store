
  test_all /home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json Namespace(config_file='/home/runner/work/mlmodels/mlmodels/mlmodels/config/test_config.json', config_mode='test', do='test_all', folder=None, log_file=None, save_folder='ztest/') 

  ml_test --do test_all 





 ************************************************************************************************************************

 ******** TAG ::  {'github_repo_url': 'https://github.com/arita37/mlmodels/tree/dbbd1e3505a2b3043e7688c1260e13ddacd09d91', 'url_branch_file': 'https://github.com/arita37/mlmodels/blob/dev/', 'repo': 'arita37/mlmodels', 'branch': 'dev', 'sha': 'dbbd1e3505a2b3043e7688c1260e13ddacd09d91', 'workflow': 'test_all'}

 ******** GITHUB_WOKFLOW : https://github.com/arita37/mlmodels/actions?query=workflow%3Atest_all

 ******** GITHUB_REPO_BRANCH : https://github.com/arita37/mlmodels/tree/dev/

 ******** GITHUB_REPO_URL : https://github.com/arita37/mlmodels/tree/dbbd1e3505a2b3043e7688c1260e13ddacd09d91

 ******** GITHUB_COMMIT_URL : https://github.com/arita37/mlmodels/commit/dbbd1e3505a2b3043e7688c1260e13ddacd09d91

 ******** Click here for Online DEBUGGER : https://gitpod.io/#https://github.com/arita37/mlmodels/tree/dbbd1e3505a2b3043e7688c1260e13ddacd09d91

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

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git add --all &&  git commit -m "ml_store  && git pull --all"  ;            git push --all -f ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
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
[master b2d9696] ml_store  && git pull --all
 2 files changed, 1 insertion(+), 53 deletions(-)
Warning: Permanently added the RSA host key for IP address '140.82.112.3' to the list of known hosts.
To github.com:arita37/mlmodels_store.git
 + 486468f...b2d9696 master -> master (forced update)





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

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git add --all &&  git commit -m "ml_store  && git pull --all"  ;            git push --all -f ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
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
[master 53555cc] ml_store  && git pull --all
 1 file changed, 47 insertions(+)
Warning: Permanently added the RSA host key for IP address '140.82.112.4' to the list of known hosts.
To github.com:arita37/mlmodels_store.git
   b2d9696..53555cc  master -> master





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
sequence_mean (InputLayer)      [(None, 1)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 4)]          0                                            
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
linear0sparse_seq_emb_sequence_ (None, 9, 1)         2           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         5           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 4, 1)         1           sequence_max[0][0]               
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_1[0][0]           
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
sparse_seq_emb_sequence_sum (Em (None, 9, 4)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 1, 4)         20          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 4, 4)         4           sequence_max[0][0]               
__________________________________________________________________________________________________
concatenate (Concatenate)       (None, 1, 7)         0           no_mask[0][0]                    
                                                                 no_mask[1][0]                    
                                                                 no_mask[2][0]                    
                                                                 no_mask[3][0]                    
                                                                 no_mask[4][0]                    
                                                                 no_mask[5][0]                    
                                                                 no_mask[6][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         12          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         28          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         4           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer (Sequenc (None, 1, 4)         0           weighted_sequence_layer[0][0]    2020-05-26 04:14:27.581244: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2020-05-26 04:14:27.585905: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2394450000 Hz
2020-05-26 04:14:27.586153: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x5651562ba1e0 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-26 04:14:27.586210: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version

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
Total params: 158
Trainable params: 158
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 1s - loss: 0.4400 - binary_crossentropy: 6.7870500/500 [==============================] - 1s 1ms/sample - loss: 0.4760 - binary_crossentropy: 7.3423 - val_loss: 0.4820 - val_binary_crossentropy: 7.4348

  #### metrics   #################################################### 
{'MSE': 0.479}

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
sequence_mean (InputLayer)      [(None, 1)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 4)]          0                                            
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
linear0sparse_seq_emb_sequence_ (None, 9, 1)         2           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         5           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 4, 1)         1           sequence_max[0][0]               
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_1[0][0]           
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
sparse_seq_emb_sequence_sum (Em (None, 9, 4)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 1, 4)         20          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 4, 4)         4           sequence_max[0][0]               
__________________________________________________________________________________________________
concatenate (Concatenate)       (None, 1, 7)         0           no_mask[0][0]                    
                                                                 no_mask[1][0]                    
                                                                 no_mask[2][0]                    
                                                                 no_mask[3][0]                    
                                                                 no_mask[4][0]                    
                                                                 no_mask[5][0]                    
                                                                 no_mask[6][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         12          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         28          sparse_feature_1[0][0]           
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
Total params: 158
Trainable params: 158
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
sequence_sum (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 8)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_3 (Weig (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 3, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 8, 4)         32          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 3, 4)         24          sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 3, 1)         7           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 8, 1)         8           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         6           sequence_max[0][0]               
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
Total params: 493
Trainable params: 493
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 1s - loss: 0.2769 - binary_crossentropy: 0.7511500/500 [==============================] - 1s 2ms/sample - loss: 0.2690 - binary_crossentropy: 0.7599 - val_loss: 0.2618 - val_binary_crossentropy: 0.7441

  #### metrics   #################################################### 
{'MSE': 0.26473843682106374}

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
sequence_sum (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 8)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_3 (Weig (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 3, 4)         28          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 8, 4)         32          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 3, 4)         24          sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 3, 1)         7           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 8, 1)         8           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         6           sequence_max[0][0]               
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
Total params: 493
Trainable params: 493
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
sequence_sum (InputLayer)       [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 6)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 2, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 6, 4)         16          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 6, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         28          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         12          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         8           sparse_feature_2[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 2, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         7           sequence_max[0][0]               
__________________________________________________________________________________________________
conv2d_1 (Conv2D)               (None, 3, 4, 1)      5           k_max_pooling[0][0]              
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         2           sparse_feature_2[0][0]           
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
Total params: 627
Trainable params: 627
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 2s - loss: 0.2500 - binary_crossentropy: 0.6931500/500 [==============================] - 1s 2ms/sample - loss: 0.2501 - binary_crossentropy: 0.6933 - val_loss: 0.2499 - val_binary_crossentropy: 0.6930

  #### metrics   #################################################### 
{'MSE': 0.24983761949414152}

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
sequence_sum (InputLayer)       [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 6)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 2, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 6, 4)         16          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 6, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         28          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         12          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         8           sparse_feature_2[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 2, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         7           sequence_max[0][0]               
__________________________________________________________________________________________________
conv2d_1 (Conv2D)               (None, 3, 4, 1)      5           k_max_pooling[0][0]              
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         2           sparse_feature_2[0][0]           
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
Total params: 627
Trainable params: 627
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
sequence_sum (InputLayer)       [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 2)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 9, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 5, 4)         8           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 2, 4)         20          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         32          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         20          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         28          sparse_feature_2[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 9, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         2           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         5           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_4 (Flatten)             (None, 28)           0           concatenate_9[0][0]              
__________________________________________________________________________________________________
flatten_5 (Flatten)             (None, 3)            0           concatenate_10[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_2[0][0]           
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
100/500 [=====>........................] - ETA: 2s - loss: 0.2608 - binary_crossentropy: 0.9743500/500 [==============================] - 1s 3ms/sample - loss: 0.2718 - binary_crossentropy: 1.0506 - val_loss: 0.2630 - val_binary_crossentropy: 1.0582

  #### metrics   #################################################### 
{'MSE': 0.264515271235115}

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
sequence_sum (InputLayer)       [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 2)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 9, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 5, 4)         8           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 2, 4)         20          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         32          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         20          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         28          sparse_feature_2[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 9, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         2           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         5           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_4 (Flatten)             (None, 28)           0           concatenate_9[0][0]              
__________________________________________________________________________________________________
flatten_5 (Flatten)             (None, 3)            0           concatenate_10[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_2[0][0]           
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
sequence_sum (InputLayer)       [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 6)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_12 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 9, 4)         16          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 5, 4)         24          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 6, 4)         24          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         20          sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 9, 1)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         6           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         6           sequence_max[0][0]               
__________________________________________________________________________________________________
concatenate_14 (Concatenate)    (None, 1, 20)        0           no_mask_22[0][0]                 
                                                                 no_mask_22[1][0]                 
                                                                 no_mask_22[2][0]                 
                                                                 no_mask_22[3][0]                 
                                                                 no_mask_22[4][0]                 
__________________________________________________________________________________________________
no_mask_23 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           sparse_feature_0[0][0]           
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
100/500 [=====>........................] - ETA: 2s - loss: 0.2487 - binary_crossentropy: 0.6905500/500 [==============================] - 2s 3ms/sample - loss: 0.2509 - binary_crossentropy: 0.6950 - val_loss: 0.2495 - val_binary_crossentropy: 0.6922

  #### metrics   #################################################### 
{'MSE': 0.25012966387934815}

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
sequence_sum (InputLayer)       [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 6)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_12 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 9, 4)         16          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 5, 4)         24          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 6, 4)         24          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         20          sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 9, 1)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         6           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         6           sequence_max[0][0]               
__________________________________________________________________________________________________
concatenate_14 (Concatenate)    (None, 1, 20)        0           no_mask_22[0][0]                 
                                                                 no_mask_22[1][0]                 
                                                                 no_mask_22[2][0]                 
                                                                 no_mask_22[3][0]                 
                                                                 no_mask_22[4][0]                 
__________________________________________________________________________________________________
no_mask_23 (NoMask)             (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           sparse_feature_0[0][0]           
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
dnn_4 (DNN)                     (None, 4)            152         concatenate_20[0][0]             2020-05-26 04:15:48.606817: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-26 04:15:48.608981: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-26 04:15:48.614950: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-26 04:15:48.625258: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-26 04:15:48.627129: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-26 04:15:48.628657: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-26 04:15:48.630229: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

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
1/1 [==============================] - 3s 3s/sample - loss: 0.2500 - binary_crossentropy: 0.6931 - val_loss: 0.2514 - val_binary_crossentropy: 0.6960
2020-05-26 04:15:49.901331: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-26 04:15:49.903335: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-26 04:15:49.907848: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-26 04:15:49.918441: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-26 04:15:49.920244: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-26 04:15:49.921828: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-26 04:15:49.923277: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

  #### metrics   #################################################### 
{'MSE': 0.2518076973676931}

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
2020-05-26 04:16:13.624272: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-26 04:16:13.625703: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-26 04:16:13.629509: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-26 04:16:13.636097: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-26 04:16:13.637225: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-26 04:16:13.638295: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-26 04:16:13.639296: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
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
1/1 [==============================] - 3s 3s/sample - loss: 0.2500 - binary_crossentropy: 0.6931 - val_loss: 0.2501 - val_binary_crossentropy: 0.6933
2020-05-26 04:16:15.199161: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-26 04:16:15.200479: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-26 04:16:15.204590: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-26 04:16:15.211100: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-26 04:16:15.212046: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-26 04:16:15.212910: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-26 04:16:15.213711: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

  #### metrics   #################################################### 
{'MSE': 0.2500029395658793}

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
concatenate_27 (Concatenate)    (None, 1, 16)        0           no_mask_36[0][0]                 2020-05-26 04:16:49.240332: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-26 04:16:49.245276: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-26 04:16:49.259902: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-26 04:16:49.284742: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-26 04:16:49.289110: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-26 04:16:49.293048: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-26 04:16:49.297118: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

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
1/1 [==============================] - 5s 5s/sample - loss: 0.4177 - binary_crossentropy: 1.0393 - val_loss: 0.2504 - val_binary_crossentropy: 0.6939
2020-05-26 04:16:51.593550: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-26 04:16:51.598476: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-26 04:16:51.610781: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-26 04:16:51.636052: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-26 04:16:51.640485: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-26 04:16:51.644524: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-26 04:16:51.648481: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

  #### metrics   #################################################### 
{'MSE': 0.24394782665857306}

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
sequence_sum (InputLayer)       [(None, 1)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 2)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 1, 4)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 2, 4)         32          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 7, 4)         24          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         16          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         8           sparse_feature_1[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 1, 1)         2           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         8           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 7, 1)         6           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_48 (NoMask)             (None, 120)          0           flatten_19[0][0]                 
__________________________________________________________________________________________________
concatenate_39 (Concatenate)    (None, 2)            0           no_mask_49[0][0]                 
                                                                 no_mask_49[1][0]                 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         4           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         2           sparse_feature_1[0][0]           
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
Total params: 675
Trainable params: 675
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 6s - loss: 0.2708 - binary_crossentropy: 0.7367500/500 [==============================] - 4s 8ms/sample - loss: 0.2671 - binary_crossentropy: 0.7288 - val_loss: 0.2632 - val_binary_crossentropy: 0.7211

  #### metrics   #################################################### 
{'MSE': 0.2641761275660748}

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
sequence_sum (InputLayer)       [(None, 1)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 2)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 1, 4)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 2, 4)         32          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 7, 4)         24          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         16          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         8           sparse_feature_1[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 1, 1)         2           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         8           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 7, 1)         6           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_48 (NoMask)             (None, 120)          0           flatten_19[0][0]                 
__________________________________________________________________________________________________
concatenate_39 (Concatenate)    (None, 2)            0           no_mask_49[0][0]                 
                                                                 no_mask_49[1][0]                 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         4           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         2           sparse_feature_1[0][0]           
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
Total params: 675
Trainable params: 675
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
sequence_sum (InputLayer)       [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 9)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 6, 2)         2           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 9, 2)         6           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 3, 2)         6           sequence_max[0][0]               
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
sparse_emb_sparse_feature_0 (Em (None, 1, 2)         14          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_3 (Em (None, 1, 2)         4           sparse_feature_3[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 2)         16          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_4 (Em (None, 1, 2)         14          sparse_feature_4[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 2)         6           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_5 (Em (None, 1, 2)         16          sparse_feature_5[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 6, 1)         1           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         3           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         3           sequence_max[0][0]               
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
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         2           sparse_feature_3[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_4[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_5[0][0]           
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
Total params: 239
Trainable params: 239
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 6s - loss: 0.3660 - binary_crossentropy: 1.5633500/500 [==============================] - 4s 9ms/sample - loss: 0.3779 - binary_crossentropy: 1.4234 - val_loss: 0.3903 - val_binary_crossentropy: 1.4268

  #### metrics   #################################################### 
{'MSE': 0.3788723267242509}

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
sequence_sum (InputLayer)       [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 9)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 6, 2)         2           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 9, 2)         6           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 3, 2)         6           sequence_max[0][0]               
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
sparse_emb_sparse_feature_0 (Em (None, 1, 2)         14          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_3 (Em (None, 1, 2)         4           sparse_feature_3[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 2)         16          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_4 (Em (None, 1, 2)         14          sparse_feature_4[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 2)         6           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_5 (Em (None, 1, 2)         16          sparse_feature_5[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 6, 1)         1           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         3           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         3           sequence_max[0][0]               
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
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         2           sparse_feature_3[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_4[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_5[0][0]           
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
Total params: 239
Trainable params: 239
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
sequence_sum (InputLayer)       [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_21 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 6, 4)         12          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 9, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 3, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         32          sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 6, 1)         3           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         7           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_24 (Flatten)            (None, 20)           0           concatenate_55[0][0]             
__________________________________________________________________________________________________
flatten_25 (Flatten)            (None, 1)            0           no_mask_69[0][0]                 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_0[0][0]           
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
Total params: 1,934
Trainable params: 1,934
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 6s - loss: 0.2668 - binary_crossentropy: 0.7294500/500 [==============================] - 5s 9ms/sample - loss: 0.2613 - binary_crossentropy: 0.7175 - val_loss: 0.2741 - val_binary_crossentropy: 0.7446

  #### metrics   #################################################### 
{'MSE': 0.2677549764789149}

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
sequence_sum (InputLayer)       [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_21 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 6, 4)         12          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 9, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 3, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         32          sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 6, 1)         3           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         7           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_24 (Flatten)            (None, 20)           0           concatenate_55[0][0]             
__________________________________________________________________________________________________
flatten_25 (Flatten)            (None, 1)            0           no_mask_69[0][0]                 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_0[0][0]           
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
Total params: 1,934
Trainable params: 1,934
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
regionsequence_sum (InputLayer) [(None, 8)]          0                                            
__________________________________________________________________________________________________
regionsequence_mean (InputLayer [(None, 7)]          0                                            
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
region_10sparse_seq_emb_regions (None, 8, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 4, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_26 (Wei (None, 3, 1)         0           region_20sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 8, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 4, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_28 (Wei (None, 3, 1)         0           region_30sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 8, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 4, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_30 (Wei (None, 3, 1)         0           region_40sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 8, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 4, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_32 (Wei (None, 3, 1)         0           learner_10sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 8, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 4, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_34 (Wei (None, 3, 1)         0           learner_20sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 8, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 4, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_36 (Wei (None, 3, 1)         0           learner_30sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 8, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 4, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_38 (Wei (None, 3, 1)         0           learner_40sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 8, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 4, 1)         4           regionsequence_max[0][0]         
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
Total params: 128
Trainable params: 128
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 8s - loss: 0.2580 - binary_crossentropy: 0.7073500/500 [==============================] - 6s 11ms/sample - loss: 0.2511 - binary_crossentropy: 0.6949 - val_loss: 0.2550 - val_binary_crossentropy: 0.7023

  #### metrics   #################################################### 
{'MSE': 0.252674444490356}

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
regionsequence_sum (InputLayer) [(None, 8)]          0                                            
__________________________________________________________________________________________________
regionsequence_mean (InputLayer [(None, 7)]          0                                            
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
region_10sparse_seq_emb_regions (None, 8, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 4, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_26 (Wei (None, 3, 1)         0           region_20sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 8, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 4, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_28 (Wei (None, 3, 1)         0           region_30sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 8, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 4, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_30 (Wei (None, 3, 1)         0           region_40sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 8, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 4, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_32 (Wei (None, 3, 1)         0           learner_10sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 8, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 4, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_34 (Wei (None, 3, 1)         0           learner_20sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 8, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 4, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_36 (Wei (None, 3, 1)         0           learner_30sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 8, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 4, 1)         4           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_38 (Wei (None, 3, 1)         0           learner_40sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 8, 1)         3           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 7, 1)         5           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 4, 1)         4           regionsequence_max[0][0]         
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
Total params: 128
Trainable params: 128
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
sequence_sum (InputLayer)       [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_40 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 2, 4)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 6, 4)         16          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 3, 4)         24          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         28          sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 2, 1)         2           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         6           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_101 (NoMask)            (None, 1, 4)         0           bi_interaction_pooling[0][0]     
__________________________________________________________________________________________________
no_mask_102 (NoMask)            (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_0[0][0]           
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
Total params: 1,387
Trainable params: 1,387
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 7s - loss: 0.2570 - binary_crossentropy: 0.7075500/500 [==============================] - 6s 11ms/sample - loss: 0.2588 - binary_crossentropy: 0.7377 - val_loss: 0.2534 - val_binary_crossentropy: 0.7781

  #### metrics   #################################################### 
{'MSE': 0.2527094380013732}

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
sequence_sum (InputLayer)       [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_40 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 2, 4)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 6, 4)         16          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 3, 4)         24          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         28          sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 2, 1)         2           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         6           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_101 (NoMask)            (None, 1, 4)         0           bi_interaction_pooling[0][0]     
__________________________________________________________________________________________________
no_mask_102 (NoMask)            (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_0[0][0]           
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
Total params: 1,387
Trainable params: 1,387
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
sequence_mean (InputLayer)      [(None, 6)]          0                                            
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
sparse_emb_sparse_feature_0_spa (None, 1, 4)         28          hash_14[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_spa (None, 1, 4)         28          hash_15[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         28          hash_16[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 5, 4)         12          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         28          hash_17[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 6, 4)         16          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         28          hash_18[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 5, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         28          hash_19[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 5, 4)         12          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         28          hash_20[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 6, 4)         16          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         28          hash_21[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 5, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 5, 4)         12          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 6, 4)         16          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 5, 4)         12          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_max_sequenc (None, 5, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 6, 4)         16          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sequence_max_sequenc (None, 5, 4)         28          sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 5, 1)         3           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         7           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_29 (Flatten)            (None, 40)           0           no_mask_116[0][0]                
__________________________________________________________________________________________________
flatten_30 (Flatten)            (None, 2)            0           concatenate_81[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           hash_10[0][0]                    
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
Total params: 3,103
Trainable params: 3,023
Non-trainable params: 80
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 8s - loss: 0.3413 - binary_crossentropy: 0.9260500/500 [==============================] - 6s 12ms/sample - loss: 0.3298 - binary_crossentropy: 0.8917 - val_loss: 0.2959 - val_binary_crossentropy: 0.8072

  #### metrics   #################################################### 
{'MSE': 0.3106366878668254}

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
sequence_mean (InputLayer)      [(None, 6)]          0                                            
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
sparse_emb_sparse_feature_0_spa (None, 1, 4)         28          hash_14[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_spa (None, 1, 4)         28          hash_15[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         28          hash_16[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 5, 4)         12          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         28          hash_17[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 6, 4)         16          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         28          hash_18[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 5, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         28          hash_19[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 5, 4)         12          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         28          hash_20[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 6, 4)         16          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         28          hash_21[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 5, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 5, 4)         12          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 6, 4)         16          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 5, 4)         12          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_max_sequenc (None, 5, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 6, 4)         16          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sequence_max_sequenc (None, 5, 4)         28          sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 5, 1)         3           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         7           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_29 (Flatten)            (None, 40)           0           no_mask_116[0][0]                
__________________________________________________________________________________________________
flatten_30 (Flatten)            (None, 2)            0           concatenate_81[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           hash_10[0][0]                    
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
Total params: 3,103
Trainable params: 3,023
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

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git add --all &&  git commit -m "ml_store  && git pull --all"  ;            git push --all -f ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
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
[master adbfa3e] ml_store  && git pull --all
 1 file changed, 4946 insertions(+)
To github.com:arita37/mlmodels_store.git
 + f9e6d11...adbfa3e master -> master (forced update)





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

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git add --all &&  git commit -m "ml_store  && git pull --all"  ;            git push --all -f ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
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
[master ee3392c] ml_store  && git pull --all
 1 file changed, 49 insertions(+)
To github.com:arita37/mlmodels_store.git
   adbfa3e..ee3392c  master -> master





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

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git add --all &&  git commit -m "ml_store  && git pull --all"  ;            git push --all -f ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
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
[master 6203a31] ml_store  && git pull --all
 1 file changed, 45 insertions(+)
Warning: Permanently added the RSA host key for IP address '140.82.114.4' to the list of known hosts.
To github.com:arita37/mlmodels_store.git
   ee3392c..6203a31  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//Autokeras.py 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//Autokeras.py", line 12, in <module>
    import autokeras as ak
ModuleNotFoundError: No module named 'autokeras'

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git add --all &&  git commit -m "ml_store  && git pull --all"  ;            git push --all -f ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
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
[master 712b6eb] ml_store  && git pull --all
 1 file changed, 35 insertions(+)
To github.com:arita37/mlmodels_store.git
   6203a31..712b6eb  master -> master





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

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git add --all &&  git commit -m "ml_store  && git pull --all"  ;            git push --all -f ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
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
[master fea0628] ml_store  && git pull --all
 1 file changed, 47 insertions(+)
To github.com:arita37/mlmodels_store.git
   712b6eb..fea0628  master -> master





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

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git add --all &&  git commit -m "ml_store  && git pull --all"  ;            git push --all -f ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
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
[master 6f11c91] ml_store  && git pull --all
 1 file changed, 46 insertions(+)
To github.com:arita37/mlmodels_store.git
   fea0628..6f11c91  master -> master





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

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git add --all &&  git commit -m "ml_store  && git pull --all"  ;            git push --all -f ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
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
[master d9aef85] ml_store  && git pull --all
 1 file changed, 43 insertions(+)
To github.com:arita37/mlmodels_store.git
   6f11c91..d9aef85  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//textcnn.py 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Loading dataset   ############################################# 
Loading data...
Downloading data from https://s3.amazonaws.com/text-datasets/imdb.npz

    8192/17464789 [..............................] - ETA: 0s
 3301376/17464789 [====>.........................] - ETA: 0s
 9388032/17464789 [===============>..............] - ETA: 0s
16900096/17464789 [============================>.] - ETA: 0s
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
2020-05-26 04:26:30.876597: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2020-05-26 04:26:30.881033: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2394450000 Hz
2020-05-26 04:26:30.881197: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x55a31f6daaf0 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-26 04:26:30.881214: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
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

 1000/25000 [>.............................] - ETA: 12s - loss: 8.0193 - accuracy: 0.4770
 2000/25000 [=>............................] - ETA: 9s - loss: 7.8583 - accuracy: 0.4875 
 3000/25000 [==>...........................] - ETA: 7s - loss: 7.7177 - accuracy: 0.4967
 4000/25000 [===>..........................] - ETA: 7s - loss: 7.6935 - accuracy: 0.4983
 5000/25000 [=====>........................] - ETA: 6s - loss: 7.7341 - accuracy: 0.4956
 6000/25000 [======>.......................] - ETA: 5s - loss: 7.7280 - accuracy: 0.4960
 7000/25000 [=======>......................] - ETA: 5s - loss: 7.7389 - accuracy: 0.4953
 8000/25000 [========>.....................] - ETA: 5s - loss: 7.7395 - accuracy: 0.4952
 9000/25000 [=========>....................] - ETA: 4s - loss: 7.7535 - accuracy: 0.4943
10000/25000 [===========>..................] - ETA: 4s - loss: 7.7295 - accuracy: 0.4959
11000/25000 [============>.................] - ETA: 4s - loss: 7.7084 - accuracy: 0.4973
12000/25000 [=============>................] - ETA: 3s - loss: 7.7152 - accuracy: 0.4968
13000/25000 [==============>...............] - ETA: 3s - loss: 7.7303 - accuracy: 0.4958
14000/25000 [===============>..............] - ETA: 3s - loss: 7.7071 - accuracy: 0.4974
15000/25000 [=================>............] - ETA: 2s - loss: 7.7147 - accuracy: 0.4969
16000/25000 [==================>...........] - ETA: 2s - loss: 7.6944 - accuracy: 0.4982
17000/25000 [===================>..........] - ETA: 2s - loss: 7.6856 - accuracy: 0.4988
18000/25000 [====================>.........] - ETA: 2s - loss: 7.6888 - accuracy: 0.4986
19000/25000 [=====================>........] - ETA: 1s - loss: 7.6739 - accuracy: 0.4995
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6613 - accuracy: 0.5003
21000/25000 [========================>.....] - ETA: 1s - loss: 7.6893 - accuracy: 0.4985
22000/25000 [=========================>....] - ETA: 0s - loss: 7.6987 - accuracy: 0.4979
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6946 - accuracy: 0.4982
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6749 - accuracy: 0.4995
25000/25000 [==============================] - 9s 343us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000

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
(<mlmodels.util.Model_empty object at 0x7f80ee56dbe0>, None)

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

  <mlmodels.model_keras.textcnn.Model object at 0x7f8113f902b0> 

  #### Fit   ######################################################## 
Loading data...
Pad sequences (samples x time)...
Train on 25000 samples, validate on 25000 samples
Epoch 1/1

 1000/25000 [>.............................] - ETA: 12s - loss: 7.8813 - accuracy: 0.4860
 2000/25000 [=>............................] - ETA: 8s - loss: 7.9350 - accuracy: 0.4825 
 3000/25000 [==>...........................] - ETA: 7s - loss: 7.9222 - accuracy: 0.4833
 4000/25000 [===>..........................] - ETA: 6s - loss: 7.8621 - accuracy: 0.4873
 5000/25000 [=====>........................] - ETA: 6s - loss: 7.8782 - accuracy: 0.4862
 6000/25000 [======>.......................] - ETA: 5s - loss: 7.8711 - accuracy: 0.4867
 7000/25000 [=======>......................] - ETA: 5s - loss: 7.8660 - accuracy: 0.4870
 8000/25000 [========>.....................] - ETA: 5s - loss: 7.8238 - accuracy: 0.4897
 9000/25000 [=========>....................] - ETA: 4s - loss: 7.8131 - accuracy: 0.4904
10000/25000 [===========>..................] - ETA: 4s - loss: 7.7893 - accuracy: 0.4920
11000/25000 [============>.................] - ETA: 4s - loss: 7.7391 - accuracy: 0.4953
12000/25000 [=============>................] - ETA: 3s - loss: 7.7075 - accuracy: 0.4973
13000/25000 [==============>...............] - ETA: 3s - loss: 7.6902 - accuracy: 0.4985
14000/25000 [===============>..............] - ETA: 3s - loss: 7.6984 - accuracy: 0.4979
15000/25000 [=================>............] - ETA: 2s - loss: 7.6799 - accuracy: 0.4991
16000/25000 [==================>...........] - ETA: 2s - loss: 7.6752 - accuracy: 0.4994
17000/25000 [===================>..........] - ETA: 2s - loss: 7.6756 - accuracy: 0.4994
18000/25000 [====================>.........] - ETA: 2s - loss: 7.6530 - accuracy: 0.5009
19000/25000 [=====================>........] - ETA: 1s - loss: 7.6303 - accuracy: 0.5024
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6314 - accuracy: 0.5023
21000/25000 [========================>.....] - ETA: 1s - loss: 7.6411 - accuracy: 0.5017
22000/25000 [=========================>....] - ETA: 0s - loss: 7.6471 - accuracy: 0.5013
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6593 - accuracy: 0.5005
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6487 - accuracy: 0.5012
25000/25000 [==============================] - 9s 346us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000

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

 1000/25000 [>.............................] - ETA: 12s - loss: 7.4060 - accuracy: 0.5170
 2000/25000 [=>............................] - ETA: 9s - loss: 7.5823 - accuracy: 0.5055 
 3000/25000 [==>...........................] - ETA: 7s - loss: 7.5593 - accuracy: 0.5070
 4000/25000 [===>..........................] - ETA: 7s - loss: 7.7203 - accuracy: 0.4965
 5000/25000 [=====>........................] - ETA: 6s - loss: 7.7494 - accuracy: 0.4946
 6000/25000 [======>.......................] - ETA: 6s - loss: 7.7203 - accuracy: 0.4965
 7000/25000 [=======>......................] - ETA: 5s - loss: 7.6951 - accuracy: 0.4981
 8000/25000 [========>.....................] - ETA: 5s - loss: 7.6398 - accuracy: 0.5017
 9000/25000 [=========>....................] - ETA: 4s - loss: 7.6479 - accuracy: 0.5012
10000/25000 [===========>..................] - ETA: 4s - loss: 7.6452 - accuracy: 0.5014
11000/25000 [============>.................] - ETA: 4s - loss: 7.6360 - accuracy: 0.5020
12000/25000 [=============>................] - ETA: 3s - loss: 7.6257 - accuracy: 0.5027
13000/25000 [==============>...............] - ETA: 3s - loss: 7.6301 - accuracy: 0.5024
14000/25000 [===============>..............] - ETA: 3s - loss: 7.6644 - accuracy: 0.5001
15000/25000 [=================>............] - ETA: 2s - loss: 7.7004 - accuracy: 0.4978
16000/25000 [==================>...........] - ETA: 2s - loss: 7.6848 - accuracy: 0.4988
17000/25000 [===================>..........] - ETA: 2s - loss: 7.7108 - accuracy: 0.4971
18000/25000 [====================>.........] - ETA: 2s - loss: 7.6990 - accuracy: 0.4979
19000/25000 [=====================>........] - ETA: 1s - loss: 7.7062 - accuracy: 0.4974
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6965 - accuracy: 0.4981
21000/25000 [========================>.....] - ETA: 1s - loss: 7.6878 - accuracy: 0.4986
22000/25000 [=========================>....] - ETA: 0s - loss: 7.6889 - accuracy: 0.4985
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6926 - accuracy: 0.4983
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6858 - accuracy: 0.4988
25000/25000 [==============================] - 9s 349us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000
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

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git add --all &&  git commit -m "ml_store  && git pull --all"  ;            git push --all -f ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
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
[master 6b8482e] ml_store  && git pull --all
 1 file changed, 316 insertions(+)
Warning: Permanently added the RSA host key for IP address '140.82.113.4' to the list of known hosts.
To github.com:arita37/mlmodels_store.git
   d9aef85..6b8482e  master -> master





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

13/13 [==============================] - 1s 115ms/step - loss: nan
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

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git add --all &&  git commit -m "ml_store  && git pull --all"  ;            git push --all -f ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
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
[master 53f6a4a] ml_store  && git pull --all
 1 file changed, 125 insertions(+)
To github.com:arita37/mlmodels_store.git
   6b8482e..53f6a4a  master -> master





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
 3497984/11490434 [========>.....................] - ETA: 0s
10297344/11490434 [=========================>....] - ETA: 0s
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

   32/60000 [..............................] - ETA: 7:05 - loss: 2.3033 - categorical_accuracy: 0.1250
   64/60000 [..............................] - ETA: 4:22 - loss: 2.2678 - categorical_accuracy: 0.1562
   96/60000 [..............................] - ETA: 3:27 - loss: 2.3033 - categorical_accuracy: 0.1458
  128/60000 [..............................] - ETA: 2:59 - loss: 2.2940 - categorical_accuracy: 0.1250
  160/60000 [..............................] - ETA: 2:44 - loss: 2.2639 - categorical_accuracy: 0.1562
  192/60000 [..............................] - ETA: 2:34 - loss: 2.2480 - categorical_accuracy: 0.1823
  224/60000 [..............................] - ETA: 2:25 - loss: 2.2390 - categorical_accuracy: 0.1741
  256/60000 [..............................] - ETA: 2:20 - loss: 2.2079 - categorical_accuracy: 0.2070
  288/60000 [..............................] - ETA: 2:17 - loss: 2.1785 - categorical_accuracy: 0.2326
  320/60000 [..............................] - ETA: 2:13 - loss: 2.1371 - categorical_accuracy: 0.2562
  352/60000 [..............................] - ETA: 2:09 - loss: 2.1340 - categorical_accuracy: 0.2614
  416/60000 [..............................] - ETA: 2:03 - loss: 2.0807 - categorical_accuracy: 0.2933
  448/60000 [..............................] - ETA: 2:01 - loss: 2.0480 - categorical_accuracy: 0.3058
  480/60000 [..............................] - ETA: 1:59 - loss: 2.0291 - categorical_accuracy: 0.3063
  512/60000 [..............................] - ETA: 1:58 - loss: 2.0170 - categorical_accuracy: 0.3164
  544/60000 [..............................] - ETA: 1:57 - loss: 1.9794 - categorical_accuracy: 0.3309
  576/60000 [..............................] - ETA: 1:56 - loss: 1.9500 - categorical_accuracy: 0.3385
  640/60000 [..............................] - ETA: 1:53 - loss: 1.9030 - categorical_accuracy: 0.3500
  672/60000 [..............................] - ETA: 1:52 - loss: 1.8665 - categorical_accuracy: 0.3646
  736/60000 [..............................] - ETA: 1:51 - loss: 1.8156 - categorical_accuracy: 0.3832
  768/60000 [..............................] - ETA: 1:50 - loss: 1.7846 - categorical_accuracy: 0.3919
  800/60000 [..............................] - ETA: 1:50 - loss: 1.7643 - categorical_accuracy: 0.4000
  832/60000 [..............................] - ETA: 1:49 - loss: 1.7522 - categorical_accuracy: 0.4026
  864/60000 [..............................] - ETA: 1:48 - loss: 1.7352 - categorical_accuracy: 0.4120
  896/60000 [..............................] - ETA: 1:48 - loss: 1.7075 - categorical_accuracy: 0.4241
  928/60000 [..............................] - ETA: 1:48 - loss: 1.6851 - categorical_accuracy: 0.4332
  992/60000 [..............................] - ETA: 1:47 - loss: 1.6837 - categorical_accuracy: 0.4365
 1056/60000 [..............................] - ETA: 1:46 - loss: 1.6470 - categorical_accuracy: 0.4517
 1088/60000 [..............................] - ETA: 1:45 - loss: 1.6283 - categorical_accuracy: 0.4577
 1120/60000 [..............................] - ETA: 1:45 - loss: 1.6038 - categorical_accuracy: 0.4643
 1152/60000 [..............................] - ETA: 1:45 - loss: 1.5821 - categorical_accuracy: 0.4714
 1184/60000 [..............................] - ETA: 1:44 - loss: 1.5761 - categorical_accuracy: 0.4747
 1216/60000 [..............................] - ETA: 1:44 - loss: 1.5611 - categorical_accuracy: 0.4794
 1248/60000 [..............................] - ETA: 1:44 - loss: 1.5553 - categorical_accuracy: 0.4840
 1280/60000 [..............................] - ETA: 1:43 - loss: 1.5375 - categorical_accuracy: 0.4898
 1344/60000 [..............................] - ETA: 1:42 - loss: 1.5014 - categorical_accuracy: 0.5007
 1376/60000 [..............................] - ETA: 1:42 - loss: 1.4828 - categorical_accuracy: 0.5051
 1440/60000 [..............................] - ETA: 1:42 - loss: 1.4549 - categorical_accuracy: 0.5167
 1472/60000 [..............................] - ETA: 1:41 - loss: 1.4420 - categorical_accuracy: 0.5211
 1504/60000 [..............................] - ETA: 1:41 - loss: 1.4308 - categorical_accuracy: 0.5239
 1536/60000 [..............................] - ETA: 1:41 - loss: 1.4138 - categorical_accuracy: 0.5293
 1568/60000 [..............................] - ETA: 1:41 - loss: 1.4026 - categorical_accuracy: 0.5319
 1600/60000 [..............................] - ETA: 1:40 - loss: 1.3868 - categorical_accuracy: 0.5369
 1664/60000 [..............................] - ETA: 1:40 - loss: 1.3511 - categorical_accuracy: 0.5517
 1696/60000 [..............................] - ETA: 1:40 - loss: 1.3397 - categorical_accuracy: 0.5548
 1728/60000 [..............................] - ETA: 1:40 - loss: 1.3309 - categorical_accuracy: 0.5579
 1760/60000 [..............................] - ETA: 1:40 - loss: 1.3185 - categorical_accuracy: 0.5619
 1824/60000 [..............................] - ETA: 1:39 - loss: 1.3001 - categorical_accuracy: 0.5674
 1888/60000 [..............................] - ETA: 1:39 - loss: 1.2755 - categorical_accuracy: 0.5747
 1920/60000 [..............................] - ETA: 1:39 - loss: 1.2662 - categorical_accuracy: 0.5781
 1952/60000 [..............................] - ETA: 1:39 - loss: 1.2553 - categorical_accuracy: 0.5809
 2016/60000 [>.............................] - ETA: 1:38 - loss: 1.2419 - categorical_accuracy: 0.5868
 2048/60000 [>.............................] - ETA: 1:38 - loss: 1.2323 - categorical_accuracy: 0.5894
 2080/60000 [>.............................] - ETA: 1:38 - loss: 1.2243 - categorical_accuracy: 0.5928
 2112/60000 [>.............................] - ETA: 1:38 - loss: 1.2210 - categorical_accuracy: 0.5938
 2144/60000 [>.............................] - ETA: 1:38 - loss: 1.2103 - categorical_accuracy: 0.5984
 2176/60000 [>.............................] - ETA: 1:38 - loss: 1.2025 - categorical_accuracy: 0.6006
 2208/60000 [>.............................] - ETA: 1:38 - loss: 1.1919 - categorical_accuracy: 0.6024
 2272/60000 [>.............................] - ETA: 1:38 - loss: 1.1752 - categorical_accuracy: 0.6074
 2336/60000 [>.............................] - ETA: 1:37 - loss: 1.1571 - categorical_accuracy: 0.6147
 2368/60000 [>.............................] - ETA: 1:37 - loss: 1.1529 - categorical_accuracy: 0.6170
 2400/60000 [>.............................] - ETA: 1:37 - loss: 1.1440 - categorical_accuracy: 0.6200
 2432/60000 [>.............................] - ETA: 1:37 - loss: 1.1344 - categorical_accuracy: 0.6238
 2464/60000 [>.............................] - ETA: 1:37 - loss: 1.1283 - categorical_accuracy: 0.6254
 2496/60000 [>.............................] - ETA: 1:37 - loss: 1.1176 - categorical_accuracy: 0.6290
 2528/60000 [>.............................] - ETA: 1:37 - loss: 1.1081 - categorical_accuracy: 0.6321
 2560/60000 [>.............................] - ETA: 1:37 - loss: 1.0985 - categorical_accuracy: 0.6348
 2592/60000 [>.............................] - ETA: 1:36 - loss: 1.0929 - categorical_accuracy: 0.6366
 2624/60000 [>.............................] - ETA: 1:36 - loss: 1.0856 - categorical_accuracy: 0.6387
 2656/60000 [>.............................] - ETA: 1:36 - loss: 1.0789 - categorical_accuracy: 0.6412
 2688/60000 [>.............................] - ETA: 1:36 - loss: 1.0692 - categorical_accuracy: 0.6440
 2720/60000 [>.............................] - ETA: 1:36 - loss: 1.0618 - categorical_accuracy: 0.6463
 2752/60000 [>.............................] - ETA: 1:36 - loss: 1.0552 - categorical_accuracy: 0.6486
 2784/60000 [>.............................] - ETA: 1:36 - loss: 1.0500 - categorical_accuracy: 0.6505
 2816/60000 [>.............................] - ETA: 1:36 - loss: 1.0471 - categorical_accuracy: 0.6516
 2880/60000 [>.............................] - ETA: 1:36 - loss: 1.0415 - categorical_accuracy: 0.6542
 2944/60000 [>.............................] - ETA: 1:35 - loss: 1.0294 - categorical_accuracy: 0.6583
 3008/60000 [>.............................] - ETA: 1:35 - loss: 1.0200 - categorical_accuracy: 0.6616
 3040/60000 [>.............................] - ETA: 1:35 - loss: 1.0135 - categorical_accuracy: 0.6641
 3072/60000 [>.............................] - ETA: 1:35 - loss: 1.0087 - categorical_accuracy: 0.6660
 3104/60000 [>.............................] - ETA: 1:35 - loss: 1.0035 - categorical_accuracy: 0.6688
 3136/60000 [>.............................] - ETA: 1:35 - loss: 0.9973 - categorical_accuracy: 0.6709
 3168/60000 [>.............................] - ETA: 1:35 - loss: 0.9897 - categorical_accuracy: 0.6739
 3200/60000 [>.............................] - ETA: 1:35 - loss: 0.9871 - categorical_accuracy: 0.6737
 3264/60000 [>.............................] - ETA: 1:34 - loss: 0.9739 - categorical_accuracy: 0.6780
 3328/60000 [>.............................] - ETA: 1:34 - loss: 0.9629 - categorical_accuracy: 0.6827
 3392/60000 [>.............................] - ETA: 1:34 - loss: 0.9531 - categorical_accuracy: 0.6860
 3456/60000 [>.............................] - ETA: 1:34 - loss: 0.9481 - categorical_accuracy: 0.6884
 3520/60000 [>.............................] - ETA: 1:33 - loss: 0.9369 - categorical_accuracy: 0.6920
 3584/60000 [>.............................] - ETA: 1:33 - loss: 0.9273 - categorical_accuracy: 0.6953
 3616/60000 [>.............................] - ETA: 1:33 - loss: 0.9219 - categorical_accuracy: 0.6969
 3648/60000 [>.............................] - ETA: 1:33 - loss: 0.9162 - categorical_accuracy: 0.6990
 3680/60000 [>.............................] - ETA: 1:33 - loss: 0.9108 - categorical_accuracy: 0.7011
 3712/60000 [>.............................] - ETA: 1:33 - loss: 0.9047 - categorical_accuracy: 0.7029
 3744/60000 [>.............................] - ETA: 1:33 - loss: 0.9017 - categorical_accuracy: 0.7038
 3808/60000 [>.............................] - ETA: 1:33 - loss: 0.8958 - categorical_accuracy: 0.7054
 3840/60000 [>.............................] - ETA: 1:33 - loss: 0.8906 - categorical_accuracy: 0.7070
 3872/60000 [>.............................] - ETA: 1:33 - loss: 0.8858 - categorical_accuracy: 0.7089
 3904/60000 [>.............................] - ETA: 1:33 - loss: 0.8814 - categorical_accuracy: 0.7106
 3936/60000 [>.............................] - ETA: 1:32 - loss: 0.8765 - categorical_accuracy: 0.7121
 3968/60000 [>.............................] - ETA: 1:32 - loss: 0.8717 - categorical_accuracy: 0.7137
 4000/60000 [=>............................] - ETA: 1:32 - loss: 0.8669 - categorical_accuracy: 0.7153
 4032/60000 [=>............................] - ETA: 1:32 - loss: 0.8636 - categorical_accuracy: 0.7168
 4064/60000 [=>............................] - ETA: 1:32 - loss: 0.8608 - categorical_accuracy: 0.7178
 4096/60000 [=>............................] - ETA: 1:32 - loss: 0.8565 - categorical_accuracy: 0.7192
 4128/60000 [=>............................] - ETA: 1:32 - loss: 0.8534 - categorical_accuracy: 0.7202
 4160/60000 [=>............................] - ETA: 1:32 - loss: 0.8501 - categorical_accuracy: 0.7212
 4192/60000 [=>............................] - ETA: 1:32 - loss: 0.8507 - categorical_accuracy: 0.7211
 4224/60000 [=>............................] - ETA: 1:32 - loss: 0.8465 - categorical_accuracy: 0.7225
 4256/60000 [=>............................] - ETA: 1:32 - loss: 0.8419 - categorical_accuracy: 0.7239
 4288/60000 [=>............................] - ETA: 1:32 - loss: 0.8376 - categorical_accuracy: 0.7257
 4320/60000 [=>............................] - ETA: 1:32 - loss: 0.8350 - categorical_accuracy: 0.7271
 4352/60000 [=>............................] - ETA: 1:32 - loss: 0.8322 - categorical_accuracy: 0.7284
 4384/60000 [=>............................] - ETA: 1:32 - loss: 0.8287 - categorical_accuracy: 0.7295
 4416/60000 [=>............................] - ETA: 1:32 - loss: 0.8260 - categorical_accuracy: 0.7301
 4448/60000 [=>............................] - ETA: 1:32 - loss: 0.8217 - categorical_accuracy: 0.7316
 4480/60000 [=>............................] - ETA: 1:31 - loss: 0.8186 - categorical_accuracy: 0.7328
 4544/60000 [=>............................] - ETA: 1:31 - loss: 0.8116 - categorical_accuracy: 0.7355
 4576/60000 [=>............................] - ETA: 1:31 - loss: 0.8090 - categorical_accuracy: 0.7369
 4608/60000 [=>............................] - ETA: 1:31 - loss: 0.8067 - categorical_accuracy: 0.7381
 4640/60000 [=>............................] - ETA: 1:31 - loss: 0.8022 - categorical_accuracy: 0.7397
 4704/60000 [=>............................] - ETA: 1:31 - loss: 0.7958 - categorical_accuracy: 0.7423
 4768/60000 [=>............................] - ETA: 1:31 - loss: 0.7883 - categorical_accuracy: 0.7450
 4832/60000 [=>............................] - ETA: 1:31 - loss: 0.7805 - categorical_accuracy: 0.7473
 4896/60000 [=>............................] - ETA: 1:30 - loss: 0.7742 - categorical_accuracy: 0.7496
 4928/60000 [=>............................] - ETA: 1:30 - loss: 0.7700 - categorical_accuracy: 0.7510
 4960/60000 [=>............................] - ETA: 1:30 - loss: 0.7664 - categorical_accuracy: 0.7524
 4992/60000 [=>............................] - ETA: 1:30 - loss: 0.7629 - categorical_accuracy: 0.7534
 5024/60000 [=>............................] - ETA: 1:30 - loss: 0.7608 - categorical_accuracy: 0.7542
 5088/60000 [=>............................] - ETA: 1:30 - loss: 0.7544 - categorical_accuracy: 0.7563
 5120/60000 [=>............................] - ETA: 1:30 - loss: 0.7510 - categorical_accuracy: 0.7574
 5184/60000 [=>............................] - ETA: 1:30 - loss: 0.7456 - categorical_accuracy: 0.7595
 5216/60000 [=>............................] - ETA: 1:30 - loss: 0.7432 - categorical_accuracy: 0.7600
 5248/60000 [=>............................] - ETA: 1:30 - loss: 0.7407 - categorical_accuracy: 0.7611
 5280/60000 [=>............................] - ETA: 1:30 - loss: 0.7380 - categorical_accuracy: 0.7617
 5312/60000 [=>............................] - ETA: 1:30 - loss: 0.7354 - categorical_accuracy: 0.7624
 5376/60000 [=>............................] - ETA: 1:29 - loss: 0.7282 - categorical_accuracy: 0.7647
 5440/60000 [=>............................] - ETA: 1:29 - loss: 0.7244 - categorical_accuracy: 0.7660
 5472/60000 [=>............................] - ETA: 1:29 - loss: 0.7208 - categorical_accuracy: 0.7674
 5504/60000 [=>............................] - ETA: 1:29 - loss: 0.7208 - categorical_accuracy: 0.7674
 5536/60000 [=>............................] - ETA: 1:29 - loss: 0.7178 - categorical_accuracy: 0.7682
 5568/60000 [=>............................] - ETA: 1:29 - loss: 0.7155 - categorical_accuracy: 0.7692
 5600/60000 [=>............................] - ETA: 1:29 - loss: 0.7138 - categorical_accuracy: 0.7698
 5632/60000 [=>............................] - ETA: 1:29 - loss: 0.7112 - categorical_accuracy: 0.7704
 5664/60000 [=>............................] - ETA: 1:29 - loss: 0.7089 - categorical_accuracy: 0.7712
 5696/60000 [=>............................] - ETA: 1:29 - loss: 0.7071 - categorical_accuracy: 0.7719
 5728/60000 [=>............................] - ETA: 1:29 - loss: 0.7043 - categorical_accuracy: 0.7727
 5760/60000 [=>............................] - ETA: 1:29 - loss: 0.7024 - categorical_accuracy: 0.7736
 5792/60000 [=>............................] - ETA: 1:29 - loss: 0.7000 - categorical_accuracy: 0.7745
 5856/60000 [=>............................] - ETA: 1:29 - loss: 0.6945 - categorical_accuracy: 0.7763
 5920/60000 [=>............................] - ETA: 1:28 - loss: 0.6900 - categorical_accuracy: 0.7780
 5952/60000 [=>............................] - ETA: 1:28 - loss: 0.6892 - categorical_accuracy: 0.7786
 5984/60000 [=>............................] - ETA: 1:28 - loss: 0.6863 - categorical_accuracy: 0.7796
 6048/60000 [==>...........................] - ETA: 1:28 - loss: 0.6821 - categorical_accuracy: 0.7809
 6080/60000 [==>...........................] - ETA: 1:28 - loss: 0.6800 - categorical_accuracy: 0.7816
 6144/60000 [==>...........................] - ETA: 1:28 - loss: 0.6772 - categorical_accuracy: 0.7822
 6176/60000 [==>...........................] - ETA: 1:28 - loss: 0.6743 - categorical_accuracy: 0.7832
 6208/60000 [==>...........................] - ETA: 1:28 - loss: 0.6714 - categorical_accuracy: 0.7841
 6272/60000 [==>...........................] - ETA: 1:28 - loss: 0.6693 - categorical_accuracy: 0.7849
 6304/60000 [==>...........................] - ETA: 1:28 - loss: 0.6681 - categorical_accuracy: 0.7854
 6368/60000 [==>...........................] - ETA: 1:28 - loss: 0.6627 - categorical_accuracy: 0.7875
 6400/60000 [==>...........................] - ETA: 1:28 - loss: 0.6613 - categorical_accuracy: 0.7878
 6432/60000 [==>...........................] - ETA: 1:27 - loss: 0.6594 - categorical_accuracy: 0.7881
 6464/60000 [==>...........................] - ETA: 1:27 - loss: 0.6579 - categorical_accuracy: 0.7885
 6496/60000 [==>...........................] - ETA: 1:27 - loss: 0.6562 - categorical_accuracy: 0.7891
 6528/60000 [==>...........................] - ETA: 1:27 - loss: 0.6536 - categorical_accuracy: 0.7898
 6592/60000 [==>...........................] - ETA: 1:27 - loss: 0.6506 - categorical_accuracy: 0.7907
 6624/60000 [==>...........................] - ETA: 1:27 - loss: 0.6479 - categorical_accuracy: 0.7915
 6656/60000 [==>...........................] - ETA: 1:27 - loss: 0.6453 - categorical_accuracy: 0.7922
 6688/60000 [==>...........................] - ETA: 1:27 - loss: 0.6450 - categorical_accuracy: 0.7923
 6752/60000 [==>...........................] - ETA: 1:27 - loss: 0.6408 - categorical_accuracy: 0.7937
 6784/60000 [==>...........................] - ETA: 1:27 - loss: 0.6388 - categorical_accuracy: 0.7944
 6816/60000 [==>...........................] - ETA: 1:27 - loss: 0.6371 - categorical_accuracy: 0.7947
 6848/60000 [==>...........................] - ETA: 1:27 - loss: 0.6358 - categorical_accuracy: 0.7948
 6912/60000 [==>...........................] - ETA: 1:27 - loss: 0.6333 - categorical_accuracy: 0.7960
 6944/60000 [==>...........................] - ETA: 1:26 - loss: 0.6310 - categorical_accuracy: 0.7967
 7008/60000 [==>...........................] - ETA: 1:26 - loss: 0.6271 - categorical_accuracy: 0.7982
 7040/60000 [==>...........................] - ETA: 1:26 - loss: 0.6253 - categorical_accuracy: 0.7987
 7104/60000 [==>...........................] - ETA: 1:26 - loss: 0.6218 - categorical_accuracy: 0.8003
 7136/60000 [==>...........................] - ETA: 1:26 - loss: 0.6201 - categorical_accuracy: 0.8007
 7168/60000 [==>...........................] - ETA: 1:26 - loss: 0.6184 - categorical_accuracy: 0.8015
 7200/60000 [==>...........................] - ETA: 1:26 - loss: 0.6177 - categorical_accuracy: 0.8019
 7232/60000 [==>...........................] - ETA: 1:26 - loss: 0.6151 - categorical_accuracy: 0.8028
 7264/60000 [==>...........................] - ETA: 1:26 - loss: 0.6149 - categorical_accuracy: 0.8031
 7328/60000 [==>...........................] - ETA: 1:26 - loss: 0.6103 - categorical_accuracy: 0.8047
 7392/60000 [==>...........................] - ETA: 1:26 - loss: 0.6085 - categorical_accuracy: 0.8053
 7456/60000 [==>...........................] - ETA: 1:26 - loss: 0.6057 - categorical_accuracy: 0.8065
 7488/60000 [==>...........................] - ETA: 1:25 - loss: 0.6034 - categorical_accuracy: 0.8073
 7520/60000 [==>...........................] - ETA: 1:25 - loss: 0.6019 - categorical_accuracy: 0.8078
 7584/60000 [==>...........................] - ETA: 1:25 - loss: 0.6007 - categorical_accuracy: 0.8085
 7648/60000 [==>...........................] - ETA: 1:25 - loss: 0.5986 - categorical_accuracy: 0.8095
 7712/60000 [==>...........................] - ETA: 1:25 - loss: 0.5951 - categorical_accuracy: 0.8106
 7744/60000 [==>...........................] - ETA: 1:25 - loss: 0.5933 - categorical_accuracy: 0.8111
 7776/60000 [==>...........................] - ETA: 1:25 - loss: 0.5917 - categorical_accuracy: 0.8116
 7808/60000 [==>...........................] - ETA: 1:25 - loss: 0.5915 - categorical_accuracy: 0.8117
 7872/60000 [==>...........................] - ETA: 1:25 - loss: 0.5886 - categorical_accuracy: 0.8128
 7904/60000 [==>...........................] - ETA: 1:25 - loss: 0.5873 - categorical_accuracy: 0.8131
 7936/60000 [==>...........................] - ETA: 1:25 - loss: 0.5854 - categorical_accuracy: 0.8138
 7968/60000 [==>...........................] - ETA: 1:25 - loss: 0.5841 - categorical_accuracy: 0.8141
 8032/60000 [===>..........................] - ETA: 1:24 - loss: 0.5810 - categorical_accuracy: 0.8151
 8064/60000 [===>..........................] - ETA: 1:24 - loss: 0.5800 - categorical_accuracy: 0.8155
 8096/60000 [===>..........................] - ETA: 1:24 - loss: 0.5786 - categorical_accuracy: 0.8161
 8128/60000 [===>..........................] - ETA: 1:24 - loss: 0.5770 - categorical_accuracy: 0.8166
 8160/60000 [===>..........................] - ETA: 1:24 - loss: 0.5760 - categorical_accuracy: 0.8168
 8192/60000 [===>..........................] - ETA: 1:24 - loss: 0.5745 - categorical_accuracy: 0.8171
 8256/60000 [===>..........................] - ETA: 1:24 - loss: 0.5718 - categorical_accuracy: 0.8180
 8320/60000 [===>..........................] - ETA: 1:24 - loss: 0.5696 - categorical_accuracy: 0.8188
 8384/60000 [===>..........................] - ETA: 1:24 - loss: 0.5669 - categorical_accuracy: 0.8194
 8416/60000 [===>..........................] - ETA: 1:24 - loss: 0.5660 - categorical_accuracy: 0.8195
 8480/60000 [===>..........................] - ETA: 1:24 - loss: 0.5634 - categorical_accuracy: 0.8203
 8544/60000 [===>..........................] - ETA: 1:24 - loss: 0.5608 - categorical_accuracy: 0.8212
 8576/60000 [===>..........................] - ETA: 1:23 - loss: 0.5603 - categorical_accuracy: 0.8212
 8640/60000 [===>..........................] - ETA: 1:23 - loss: 0.5579 - categorical_accuracy: 0.8216
 8704/60000 [===>..........................] - ETA: 1:23 - loss: 0.5558 - categorical_accuracy: 0.8225
 8768/60000 [===>..........................] - ETA: 1:23 - loss: 0.5537 - categorical_accuracy: 0.8232
 8800/60000 [===>..........................] - ETA: 1:23 - loss: 0.5534 - categorical_accuracy: 0.8234
 8832/60000 [===>..........................] - ETA: 1:23 - loss: 0.5521 - categorical_accuracy: 0.8239
 8864/60000 [===>..........................] - ETA: 1:23 - loss: 0.5506 - categorical_accuracy: 0.8245
 8896/60000 [===>..........................] - ETA: 1:23 - loss: 0.5493 - categorical_accuracy: 0.8249
 8960/60000 [===>..........................] - ETA: 1:23 - loss: 0.5463 - categorical_accuracy: 0.8259
 9024/60000 [===>..........................] - ETA: 1:23 - loss: 0.5435 - categorical_accuracy: 0.8267
 9056/60000 [===>..........................] - ETA: 1:23 - loss: 0.5419 - categorical_accuracy: 0.8272
 9088/60000 [===>..........................] - ETA: 1:23 - loss: 0.5417 - categorical_accuracy: 0.8272
 9152/60000 [===>..........................] - ETA: 1:22 - loss: 0.5398 - categorical_accuracy: 0.8281
 9216/60000 [===>..........................] - ETA: 1:22 - loss: 0.5378 - categorical_accuracy: 0.8289
 9248/60000 [===>..........................] - ETA: 1:22 - loss: 0.5362 - categorical_accuracy: 0.8295
 9280/60000 [===>..........................] - ETA: 1:22 - loss: 0.5353 - categorical_accuracy: 0.8297
 9312/60000 [===>..........................] - ETA: 1:22 - loss: 0.5342 - categorical_accuracy: 0.8302
 9344/60000 [===>..........................] - ETA: 1:22 - loss: 0.5328 - categorical_accuracy: 0.8306
 9408/60000 [===>..........................] - ETA: 1:22 - loss: 0.5304 - categorical_accuracy: 0.8315
 9440/60000 [===>..........................] - ETA: 1:22 - loss: 0.5292 - categorical_accuracy: 0.8318
 9504/60000 [===>..........................] - ETA: 1:22 - loss: 0.5270 - categorical_accuracy: 0.8325
 9568/60000 [===>..........................] - ETA: 1:22 - loss: 0.5257 - categorical_accuracy: 0.8330
 9632/60000 [===>..........................] - ETA: 1:21 - loss: 0.5236 - categorical_accuracy: 0.8334
 9664/60000 [===>..........................] - ETA: 1:21 - loss: 0.5231 - categorical_accuracy: 0.8336
 9696/60000 [===>..........................] - ETA: 1:21 - loss: 0.5221 - categorical_accuracy: 0.8340
 9728/60000 [===>..........................] - ETA: 1:21 - loss: 0.5211 - categorical_accuracy: 0.8343
 9760/60000 [===>..........................] - ETA: 1:21 - loss: 0.5201 - categorical_accuracy: 0.8347
 9792/60000 [===>..........................] - ETA: 1:21 - loss: 0.5195 - categorical_accuracy: 0.8349
 9856/60000 [===>..........................] - ETA: 1:21 - loss: 0.5174 - categorical_accuracy: 0.8355
 9888/60000 [===>..........................] - ETA: 1:21 - loss: 0.5162 - categorical_accuracy: 0.8359
 9920/60000 [===>..........................] - ETA: 1:21 - loss: 0.5148 - categorical_accuracy: 0.8363
 9984/60000 [===>..........................] - ETA: 1:21 - loss: 0.5127 - categorical_accuracy: 0.8369
10016/60000 [====>.........................] - ETA: 1:21 - loss: 0.5117 - categorical_accuracy: 0.8372
10048/60000 [====>.........................] - ETA: 1:21 - loss: 0.5108 - categorical_accuracy: 0.8374
10080/60000 [====>.........................] - ETA: 1:21 - loss: 0.5101 - categorical_accuracy: 0.8377
10112/60000 [====>.........................] - ETA: 1:21 - loss: 0.5086 - categorical_accuracy: 0.8382
10176/60000 [====>.........................] - ETA: 1:21 - loss: 0.5060 - categorical_accuracy: 0.8390
10240/60000 [====>.........................] - ETA: 1:21 - loss: 0.5046 - categorical_accuracy: 0.8396
10272/60000 [====>.........................] - ETA: 1:20 - loss: 0.5034 - categorical_accuracy: 0.8401
10304/60000 [====>.........................] - ETA: 1:20 - loss: 0.5027 - categorical_accuracy: 0.8405
10336/60000 [====>.........................] - ETA: 1:20 - loss: 0.5015 - categorical_accuracy: 0.8408
10400/60000 [====>.........................] - ETA: 1:20 - loss: 0.4992 - categorical_accuracy: 0.8416
10432/60000 [====>.........................] - ETA: 1:20 - loss: 0.4979 - categorical_accuracy: 0.8420
10464/60000 [====>.........................] - ETA: 1:20 - loss: 0.4972 - categorical_accuracy: 0.8423
10496/60000 [====>.........................] - ETA: 1:20 - loss: 0.4962 - categorical_accuracy: 0.8426
10528/60000 [====>.........................] - ETA: 1:20 - loss: 0.4949 - categorical_accuracy: 0.8431
10560/60000 [====>.........................] - ETA: 1:20 - loss: 0.4939 - categorical_accuracy: 0.8435
10592/60000 [====>.........................] - ETA: 1:20 - loss: 0.4925 - categorical_accuracy: 0.8439
10624/60000 [====>.........................] - ETA: 1:20 - loss: 0.4913 - categorical_accuracy: 0.8443
10656/60000 [====>.........................] - ETA: 1:20 - loss: 0.4902 - categorical_accuracy: 0.8447
10688/60000 [====>.........................] - ETA: 1:20 - loss: 0.4894 - categorical_accuracy: 0.8449
10720/60000 [====>.........................] - ETA: 1:20 - loss: 0.4885 - categorical_accuracy: 0.8451
10784/60000 [====>.........................] - ETA: 1:20 - loss: 0.4869 - categorical_accuracy: 0.8456
10848/60000 [====>.........................] - ETA: 1:19 - loss: 0.4866 - categorical_accuracy: 0.8460
10880/60000 [====>.........................] - ETA: 1:19 - loss: 0.4859 - categorical_accuracy: 0.8462
10912/60000 [====>.........................] - ETA: 1:19 - loss: 0.4860 - categorical_accuracy: 0.8463
10944/60000 [====>.........................] - ETA: 1:19 - loss: 0.4853 - categorical_accuracy: 0.8466
10976/60000 [====>.........................] - ETA: 1:19 - loss: 0.4841 - categorical_accuracy: 0.8470
11008/60000 [====>.........................] - ETA: 1:19 - loss: 0.4835 - categorical_accuracy: 0.8473
11040/60000 [====>.........................] - ETA: 1:19 - loss: 0.4833 - categorical_accuracy: 0.8474
11104/60000 [====>.........................] - ETA: 1:19 - loss: 0.4811 - categorical_accuracy: 0.8482
11168/60000 [====>.........................] - ETA: 1:19 - loss: 0.4794 - categorical_accuracy: 0.8488
11200/60000 [====>.........................] - ETA: 1:19 - loss: 0.4782 - categorical_accuracy: 0.8492
11232/60000 [====>.........................] - ETA: 1:19 - loss: 0.4771 - categorical_accuracy: 0.8495
11264/60000 [====>.........................] - ETA: 1:19 - loss: 0.4761 - categorical_accuracy: 0.8499
11296/60000 [====>.........................] - ETA: 1:19 - loss: 0.4751 - categorical_accuracy: 0.8501
11328/60000 [====>.........................] - ETA: 1:19 - loss: 0.4741 - categorical_accuracy: 0.8504
11360/60000 [====>.........................] - ETA: 1:19 - loss: 0.4736 - categorical_accuracy: 0.8505
11392/60000 [====>.........................] - ETA: 1:19 - loss: 0.4726 - categorical_accuracy: 0.8509
11456/60000 [====>.........................] - ETA: 1:18 - loss: 0.4705 - categorical_accuracy: 0.8513
11520/60000 [====>.........................] - ETA: 1:18 - loss: 0.4697 - categorical_accuracy: 0.8516
11552/60000 [====>.........................] - ETA: 1:18 - loss: 0.4685 - categorical_accuracy: 0.8521
11584/60000 [====>.........................] - ETA: 1:18 - loss: 0.4677 - categorical_accuracy: 0.8524
11616/60000 [====>.........................] - ETA: 1:18 - loss: 0.4668 - categorical_accuracy: 0.8527
11680/60000 [====>.........................] - ETA: 1:18 - loss: 0.4650 - categorical_accuracy: 0.8532
11712/60000 [====>.........................] - ETA: 1:18 - loss: 0.4644 - categorical_accuracy: 0.8534
11744/60000 [====>.........................] - ETA: 1:18 - loss: 0.4646 - categorical_accuracy: 0.8535
11776/60000 [====>.........................] - ETA: 1:18 - loss: 0.4636 - categorical_accuracy: 0.8539
11808/60000 [====>.........................] - ETA: 1:18 - loss: 0.4627 - categorical_accuracy: 0.8542
11840/60000 [====>.........................] - ETA: 1:18 - loss: 0.4619 - categorical_accuracy: 0.8545
11872/60000 [====>.........................] - ETA: 1:18 - loss: 0.4610 - categorical_accuracy: 0.8547
11904/60000 [====>.........................] - ETA: 1:18 - loss: 0.4603 - categorical_accuracy: 0.8549
11936/60000 [====>.........................] - ETA: 1:18 - loss: 0.4595 - categorical_accuracy: 0.8551
11968/60000 [====>.........................] - ETA: 1:18 - loss: 0.4595 - categorical_accuracy: 0.8550
12000/60000 [=====>........................] - ETA: 1:18 - loss: 0.4589 - categorical_accuracy: 0.8553
12032/60000 [=====>........................] - ETA: 1:18 - loss: 0.4582 - categorical_accuracy: 0.8555
12064/60000 [=====>........................] - ETA: 1:17 - loss: 0.4573 - categorical_accuracy: 0.8556
12096/60000 [=====>........................] - ETA: 1:17 - loss: 0.4567 - categorical_accuracy: 0.8559
12160/60000 [=====>........................] - ETA: 1:17 - loss: 0.4551 - categorical_accuracy: 0.8562
12224/60000 [=====>........................] - ETA: 1:17 - loss: 0.4555 - categorical_accuracy: 0.8563
12288/60000 [=====>........................] - ETA: 1:17 - loss: 0.4541 - categorical_accuracy: 0.8568
12320/60000 [=====>........................] - ETA: 1:17 - loss: 0.4532 - categorical_accuracy: 0.8570
12352/60000 [=====>........................] - ETA: 1:17 - loss: 0.4525 - categorical_accuracy: 0.8572
12384/60000 [=====>........................] - ETA: 1:17 - loss: 0.4516 - categorical_accuracy: 0.8576
12416/60000 [=====>........................] - ETA: 1:17 - loss: 0.4512 - categorical_accuracy: 0.8577
12448/60000 [=====>........................] - ETA: 1:17 - loss: 0.4507 - categorical_accuracy: 0.8578
12480/60000 [=====>........................] - ETA: 1:17 - loss: 0.4497 - categorical_accuracy: 0.8582
12544/60000 [=====>........................] - ETA: 1:17 - loss: 0.4486 - categorical_accuracy: 0.8585
12576/60000 [=====>........................] - ETA: 1:17 - loss: 0.4477 - categorical_accuracy: 0.8588
12608/60000 [=====>........................] - ETA: 1:17 - loss: 0.4468 - categorical_accuracy: 0.8591
12640/60000 [=====>........................] - ETA: 1:17 - loss: 0.4462 - categorical_accuracy: 0.8593
12672/60000 [=====>........................] - ETA: 1:16 - loss: 0.4452 - categorical_accuracy: 0.8596
12736/60000 [=====>........................] - ETA: 1:16 - loss: 0.4440 - categorical_accuracy: 0.8598
12768/60000 [=====>........................] - ETA: 1:16 - loss: 0.4442 - categorical_accuracy: 0.8598
12800/60000 [=====>........................] - ETA: 1:16 - loss: 0.4436 - categorical_accuracy: 0.8600
12832/60000 [=====>........................] - ETA: 1:16 - loss: 0.4430 - categorical_accuracy: 0.8603
12864/60000 [=====>........................] - ETA: 1:16 - loss: 0.4425 - categorical_accuracy: 0.8605
12896/60000 [=====>........................] - ETA: 1:16 - loss: 0.4418 - categorical_accuracy: 0.8606
12928/60000 [=====>........................] - ETA: 1:16 - loss: 0.4411 - categorical_accuracy: 0.8608
12960/60000 [=====>........................] - ETA: 1:16 - loss: 0.4402 - categorical_accuracy: 0.8611
12992/60000 [=====>........................] - ETA: 1:16 - loss: 0.4394 - categorical_accuracy: 0.8613
13024/60000 [=====>........................] - ETA: 1:16 - loss: 0.4385 - categorical_accuracy: 0.8615
13056/60000 [=====>........................] - ETA: 1:16 - loss: 0.4381 - categorical_accuracy: 0.8616
13088/60000 [=====>........................] - ETA: 1:16 - loss: 0.4379 - categorical_accuracy: 0.8617
13120/60000 [=====>........................] - ETA: 1:16 - loss: 0.4374 - categorical_accuracy: 0.8619
13152/60000 [=====>........................] - ETA: 1:16 - loss: 0.4368 - categorical_accuracy: 0.8622
13184/60000 [=====>........................] - ETA: 1:16 - loss: 0.4360 - categorical_accuracy: 0.8624
13248/60000 [=====>........................] - ETA: 1:16 - loss: 0.4346 - categorical_accuracy: 0.8628
13280/60000 [=====>........................] - ETA: 1:16 - loss: 0.4338 - categorical_accuracy: 0.8630
13312/60000 [=====>........................] - ETA: 1:16 - loss: 0.4340 - categorical_accuracy: 0.8631
13344/60000 [=====>........................] - ETA: 1:15 - loss: 0.4333 - categorical_accuracy: 0.8632
13408/60000 [=====>........................] - ETA: 1:15 - loss: 0.4318 - categorical_accuracy: 0.8637
13440/60000 [=====>........................] - ETA: 1:15 - loss: 0.4314 - categorical_accuracy: 0.8639
13472/60000 [=====>........................] - ETA: 1:15 - loss: 0.4304 - categorical_accuracy: 0.8642
13504/60000 [=====>........................] - ETA: 1:15 - loss: 0.4296 - categorical_accuracy: 0.8645
13536/60000 [=====>........................] - ETA: 1:15 - loss: 0.4290 - categorical_accuracy: 0.8647
13568/60000 [=====>........................] - ETA: 1:15 - loss: 0.4284 - categorical_accuracy: 0.8649
13600/60000 [=====>........................] - ETA: 1:15 - loss: 0.4278 - categorical_accuracy: 0.8651
13664/60000 [=====>........................] - ETA: 1:15 - loss: 0.4264 - categorical_accuracy: 0.8657
13696/60000 [=====>........................] - ETA: 1:15 - loss: 0.4257 - categorical_accuracy: 0.8659
13728/60000 [=====>........................] - ETA: 1:15 - loss: 0.4249 - categorical_accuracy: 0.8663
13760/60000 [=====>........................] - ETA: 1:15 - loss: 0.4244 - categorical_accuracy: 0.8664
13792/60000 [=====>........................] - ETA: 1:15 - loss: 0.4237 - categorical_accuracy: 0.8666
13824/60000 [=====>........................] - ETA: 1:15 - loss: 0.4229 - categorical_accuracy: 0.8668
13888/60000 [=====>........................] - ETA: 1:15 - loss: 0.4219 - categorical_accuracy: 0.8671
13952/60000 [=====>........................] - ETA: 1:14 - loss: 0.4214 - categorical_accuracy: 0.8674
13984/60000 [=====>........................] - ETA: 1:14 - loss: 0.4209 - categorical_accuracy: 0.8676
14016/60000 [======>.......................] - ETA: 1:14 - loss: 0.4208 - categorical_accuracy: 0.8677
14048/60000 [======>.......................] - ETA: 1:14 - loss: 0.4200 - categorical_accuracy: 0.8679
14080/60000 [======>.......................] - ETA: 1:14 - loss: 0.4196 - categorical_accuracy: 0.8680
14112/60000 [======>.......................] - ETA: 1:14 - loss: 0.4188 - categorical_accuracy: 0.8683
14176/60000 [======>.......................] - ETA: 1:14 - loss: 0.4173 - categorical_accuracy: 0.8687
14208/60000 [======>.......................] - ETA: 1:14 - loss: 0.4170 - categorical_accuracy: 0.8687
14240/60000 [======>.......................] - ETA: 1:14 - loss: 0.4162 - categorical_accuracy: 0.8690
14304/60000 [======>.......................] - ETA: 1:14 - loss: 0.4155 - categorical_accuracy: 0.8693
14368/60000 [======>.......................] - ETA: 1:14 - loss: 0.4143 - categorical_accuracy: 0.8698
14400/60000 [======>.......................] - ETA: 1:14 - loss: 0.4139 - categorical_accuracy: 0.8699
14432/60000 [======>.......................] - ETA: 1:14 - loss: 0.4132 - categorical_accuracy: 0.8700
14496/60000 [======>.......................] - ETA: 1:13 - loss: 0.4120 - categorical_accuracy: 0.8703
14528/60000 [======>.......................] - ETA: 1:13 - loss: 0.4113 - categorical_accuracy: 0.8705
14560/60000 [======>.......................] - ETA: 1:13 - loss: 0.4105 - categorical_accuracy: 0.8707
14592/60000 [======>.......................] - ETA: 1:13 - loss: 0.4097 - categorical_accuracy: 0.8710
14624/60000 [======>.......................] - ETA: 1:13 - loss: 0.4090 - categorical_accuracy: 0.8712
14688/60000 [======>.......................] - ETA: 1:13 - loss: 0.4079 - categorical_accuracy: 0.8715
14720/60000 [======>.......................] - ETA: 1:13 - loss: 0.4072 - categorical_accuracy: 0.8718
14752/60000 [======>.......................] - ETA: 1:13 - loss: 0.4066 - categorical_accuracy: 0.8719
14784/60000 [======>.......................] - ETA: 1:13 - loss: 0.4060 - categorical_accuracy: 0.8721
14816/60000 [======>.......................] - ETA: 1:13 - loss: 0.4062 - categorical_accuracy: 0.8720
14848/60000 [======>.......................] - ETA: 1:13 - loss: 0.4060 - categorical_accuracy: 0.8722
14912/60000 [======>.......................] - ETA: 1:13 - loss: 0.4047 - categorical_accuracy: 0.8726
14944/60000 [======>.......................] - ETA: 1:13 - loss: 0.4039 - categorical_accuracy: 0.8729
14976/60000 [======>.......................] - ETA: 1:13 - loss: 0.4033 - categorical_accuracy: 0.8730
15008/60000 [======>.......................] - ETA: 1:13 - loss: 0.4035 - categorical_accuracy: 0.8730
15040/60000 [======>.......................] - ETA: 1:13 - loss: 0.4031 - categorical_accuracy: 0.8731
15072/60000 [======>.......................] - ETA: 1:13 - loss: 0.4026 - categorical_accuracy: 0.8733
15104/60000 [======>.......................] - ETA: 1:12 - loss: 0.4019 - categorical_accuracy: 0.8735
15168/60000 [======>.......................] - ETA: 1:12 - loss: 0.4009 - categorical_accuracy: 0.8738
15232/60000 [======>.......................] - ETA: 1:12 - loss: 0.3997 - categorical_accuracy: 0.8743
15264/60000 [======>.......................] - ETA: 1:12 - loss: 0.3995 - categorical_accuracy: 0.8745
15296/60000 [======>.......................] - ETA: 1:12 - loss: 0.3998 - categorical_accuracy: 0.8744
15328/60000 [======>.......................] - ETA: 1:12 - loss: 0.3991 - categorical_accuracy: 0.8747
15392/60000 [======>.......................] - ETA: 1:12 - loss: 0.3982 - categorical_accuracy: 0.8749
15456/60000 [======>.......................] - ETA: 1:12 - loss: 0.3968 - categorical_accuracy: 0.8754
15520/60000 [======>.......................] - ETA: 1:12 - loss: 0.3960 - categorical_accuracy: 0.8756
15584/60000 [======>.......................] - ETA: 1:12 - loss: 0.3947 - categorical_accuracy: 0.8760
15616/60000 [======>.......................] - ETA: 1:12 - loss: 0.3940 - categorical_accuracy: 0.8763
15680/60000 [======>.......................] - ETA: 1:12 - loss: 0.3928 - categorical_accuracy: 0.8767
15712/60000 [======>.......................] - ETA: 1:11 - loss: 0.3921 - categorical_accuracy: 0.8769
15744/60000 [======>.......................] - ETA: 1:11 - loss: 0.3913 - categorical_accuracy: 0.8771
15776/60000 [======>.......................] - ETA: 1:11 - loss: 0.3908 - categorical_accuracy: 0.8773
15808/60000 [======>.......................] - ETA: 1:11 - loss: 0.3906 - categorical_accuracy: 0.8773
15840/60000 [======>.......................] - ETA: 1:11 - loss: 0.3901 - categorical_accuracy: 0.8775
15872/60000 [======>.......................] - ETA: 1:11 - loss: 0.3898 - categorical_accuracy: 0.8776
15904/60000 [======>.......................] - ETA: 1:11 - loss: 0.3892 - categorical_accuracy: 0.8778
15936/60000 [======>.......................] - ETA: 1:11 - loss: 0.3886 - categorical_accuracy: 0.8780
15968/60000 [======>.......................] - ETA: 1:11 - loss: 0.3880 - categorical_accuracy: 0.8782
16000/60000 [=======>......................] - ETA: 1:11 - loss: 0.3876 - categorical_accuracy: 0.8784
16064/60000 [=======>......................] - ETA: 1:11 - loss: 0.3866 - categorical_accuracy: 0.8787
16096/60000 [=======>......................] - ETA: 1:11 - loss: 0.3863 - categorical_accuracy: 0.8789
16128/60000 [=======>......................] - ETA: 1:11 - loss: 0.3858 - categorical_accuracy: 0.8790
16160/60000 [=======>......................] - ETA: 1:11 - loss: 0.3853 - categorical_accuracy: 0.8791
16192/60000 [=======>......................] - ETA: 1:11 - loss: 0.3846 - categorical_accuracy: 0.8794
16224/60000 [=======>......................] - ETA: 1:11 - loss: 0.3840 - categorical_accuracy: 0.8796
16256/60000 [=======>......................] - ETA: 1:11 - loss: 0.3835 - categorical_accuracy: 0.8797
16288/60000 [=======>......................] - ETA: 1:11 - loss: 0.3830 - categorical_accuracy: 0.8799
16320/60000 [=======>......................] - ETA: 1:10 - loss: 0.3823 - categorical_accuracy: 0.8801
16384/60000 [=======>......................] - ETA: 1:10 - loss: 0.3818 - categorical_accuracy: 0.8804
16448/60000 [=======>......................] - ETA: 1:10 - loss: 0.3813 - categorical_accuracy: 0.8806
16512/60000 [=======>......................] - ETA: 1:10 - loss: 0.3805 - categorical_accuracy: 0.8808
16576/60000 [=======>......................] - ETA: 1:10 - loss: 0.3797 - categorical_accuracy: 0.8810
16640/60000 [=======>......................] - ETA: 1:10 - loss: 0.3787 - categorical_accuracy: 0.8813
16672/60000 [=======>......................] - ETA: 1:10 - loss: 0.3781 - categorical_accuracy: 0.8815
16704/60000 [=======>......................] - ETA: 1:10 - loss: 0.3780 - categorical_accuracy: 0.8815
16768/60000 [=======>......................] - ETA: 1:10 - loss: 0.3776 - categorical_accuracy: 0.8817
16800/60000 [=======>......................] - ETA: 1:10 - loss: 0.3773 - categorical_accuracy: 0.8818
16832/60000 [=======>......................] - ETA: 1:10 - loss: 0.3771 - categorical_accuracy: 0.8819
16864/60000 [=======>......................] - ETA: 1:10 - loss: 0.3767 - categorical_accuracy: 0.8819
16896/60000 [=======>......................] - ETA: 1:09 - loss: 0.3769 - categorical_accuracy: 0.8819
16928/60000 [=======>......................] - ETA: 1:09 - loss: 0.3767 - categorical_accuracy: 0.8819
16960/60000 [=======>......................] - ETA: 1:09 - loss: 0.3762 - categorical_accuracy: 0.8821
17024/60000 [=======>......................] - ETA: 1:09 - loss: 0.3751 - categorical_accuracy: 0.8825
17088/60000 [=======>......................] - ETA: 1:09 - loss: 0.3743 - categorical_accuracy: 0.8825
17120/60000 [=======>......................] - ETA: 1:09 - loss: 0.3742 - categorical_accuracy: 0.8826
17152/60000 [=======>......................] - ETA: 1:09 - loss: 0.3738 - categorical_accuracy: 0.8827
17216/60000 [=======>......................] - ETA: 1:09 - loss: 0.3728 - categorical_accuracy: 0.8830
17280/60000 [=======>......................] - ETA: 1:09 - loss: 0.3719 - categorical_accuracy: 0.8833
17344/60000 [=======>......................] - ETA: 1:09 - loss: 0.3716 - categorical_accuracy: 0.8835
17376/60000 [=======>......................] - ETA: 1:09 - loss: 0.3711 - categorical_accuracy: 0.8837
17408/60000 [=======>......................] - ETA: 1:09 - loss: 0.3708 - categorical_accuracy: 0.8837
17472/60000 [=======>......................] - ETA: 1:09 - loss: 0.3697 - categorical_accuracy: 0.8841
17536/60000 [=======>......................] - ETA: 1:08 - loss: 0.3693 - categorical_accuracy: 0.8842
17568/60000 [=======>......................] - ETA: 1:08 - loss: 0.3689 - categorical_accuracy: 0.8843
17600/60000 [=======>......................] - ETA: 1:08 - loss: 0.3685 - categorical_accuracy: 0.8845
17632/60000 [=======>......................] - ETA: 1:08 - loss: 0.3681 - categorical_accuracy: 0.8846
17696/60000 [=======>......................] - ETA: 1:08 - loss: 0.3670 - categorical_accuracy: 0.8850
17728/60000 [=======>......................] - ETA: 1:08 - loss: 0.3668 - categorical_accuracy: 0.8851
17760/60000 [=======>......................] - ETA: 1:08 - loss: 0.3666 - categorical_accuracy: 0.8852
17792/60000 [=======>......................] - ETA: 1:08 - loss: 0.3662 - categorical_accuracy: 0.8852
17824/60000 [=======>......................] - ETA: 1:08 - loss: 0.3656 - categorical_accuracy: 0.8854
17888/60000 [=======>......................] - ETA: 1:08 - loss: 0.3645 - categorical_accuracy: 0.8857
17920/60000 [=======>......................] - ETA: 1:08 - loss: 0.3640 - categorical_accuracy: 0.8859
17952/60000 [=======>......................] - ETA: 1:08 - loss: 0.3634 - categorical_accuracy: 0.8861
18016/60000 [========>.....................] - ETA: 1:08 - loss: 0.3626 - categorical_accuracy: 0.8863
18080/60000 [========>.....................] - ETA: 1:08 - loss: 0.3615 - categorical_accuracy: 0.8866
18112/60000 [========>.....................] - ETA: 1:08 - loss: 0.3624 - categorical_accuracy: 0.8865
18144/60000 [========>.....................] - ETA: 1:07 - loss: 0.3620 - categorical_accuracy: 0.8867
18176/60000 [========>.....................] - ETA: 1:07 - loss: 0.3614 - categorical_accuracy: 0.8869
18240/60000 [========>.....................] - ETA: 1:07 - loss: 0.3606 - categorical_accuracy: 0.8872
18272/60000 [========>.....................] - ETA: 1:07 - loss: 0.3602 - categorical_accuracy: 0.8873
18336/60000 [========>.....................] - ETA: 1:07 - loss: 0.3600 - categorical_accuracy: 0.8873
18368/60000 [========>.....................] - ETA: 1:07 - loss: 0.3595 - categorical_accuracy: 0.8875
18432/60000 [========>.....................] - ETA: 1:07 - loss: 0.3587 - categorical_accuracy: 0.8877
18464/60000 [========>.....................] - ETA: 1:07 - loss: 0.3582 - categorical_accuracy: 0.8879
18496/60000 [========>.....................] - ETA: 1:07 - loss: 0.3579 - categorical_accuracy: 0.8880
18528/60000 [========>.....................] - ETA: 1:07 - loss: 0.3574 - categorical_accuracy: 0.8881
18560/60000 [========>.....................] - ETA: 1:07 - loss: 0.3574 - categorical_accuracy: 0.8881
18624/60000 [========>.....................] - ETA: 1:07 - loss: 0.3569 - categorical_accuracy: 0.8884
18688/60000 [========>.....................] - ETA: 1:07 - loss: 0.3562 - categorical_accuracy: 0.8886
18752/60000 [========>.....................] - ETA: 1:06 - loss: 0.3552 - categorical_accuracy: 0.8889
18784/60000 [========>.....................] - ETA: 1:06 - loss: 0.3553 - categorical_accuracy: 0.8890
18816/60000 [========>.....................] - ETA: 1:06 - loss: 0.3549 - categorical_accuracy: 0.8891
18848/60000 [========>.....................] - ETA: 1:06 - loss: 0.3545 - categorical_accuracy: 0.8893
18880/60000 [========>.....................] - ETA: 1:06 - loss: 0.3541 - categorical_accuracy: 0.8894
18912/60000 [========>.....................] - ETA: 1:06 - loss: 0.3537 - categorical_accuracy: 0.8895
18944/60000 [========>.....................] - ETA: 1:06 - loss: 0.3531 - categorical_accuracy: 0.8897
18976/60000 [========>.....................] - ETA: 1:06 - loss: 0.3530 - categorical_accuracy: 0.8898
19040/60000 [========>.....................] - ETA: 1:06 - loss: 0.3523 - categorical_accuracy: 0.8900
19072/60000 [========>.....................] - ETA: 1:06 - loss: 0.3519 - categorical_accuracy: 0.8901
19136/60000 [========>.....................] - ETA: 1:06 - loss: 0.3511 - categorical_accuracy: 0.8904
19168/60000 [========>.....................] - ETA: 1:06 - loss: 0.3507 - categorical_accuracy: 0.8905
19200/60000 [========>.....................] - ETA: 1:06 - loss: 0.3503 - categorical_accuracy: 0.8906
19232/60000 [========>.....................] - ETA: 1:06 - loss: 0.3500 - categorical_accuracy: 0.8907
19264/60000 [========>.....................] - ETA: 1:06 - loss: 0.3497 - categorical_accuracy: 0.8908
19296/60000 [========>.....................] - ETA: 1:06 - loss: 0.3495 - categorical_accuracy: 0.8909
19328/60000 [========>.....................] - ETA: 1:05 - loss: 0.3492 - categorical_accuracy: 0.8910
19360/60000 [========>.....................] - ETA: 1:05 - loss: 0.3487 - categorical_accuracy: 0.8912
19424/60000 [========>.....................] - ETA: 1:05 - loss: 0.3477 - categorical_accuracy: 0.8915
19488/60000 [========>.....................] - ETA: 1:05 - loss: 0.3475 - categorical_accuracy: 0.8916
19520/60000 [========>.....................] - ETA: 1:05 - loss: 0.3471 - categorical_accuracy: 0.8916
19584/60000 [========>.....................] - ETA: 1:05 - loss: 0.3465 - categorical_accuracy: 0.8919
19616/60000 [========>.....................] - ETA: 1:05 - loss: 0.3466 - categorical_accuracy: 0.8919
19648/60000 [========>.....................] - ETA: 1:05 - loss: 0.3462 - categorical_accuracy: 0.8921
19680/60000 [========>.....................] - ETA: 1:05 - loss: 0.3464 - categorical_accuracy: 0.8920
19744/60000 [========>.....................] - ETA: 1:05 - loss: 0.3455 - categorical_accuracy: 0.8923
19808/60000 [========>.....................] - ETA: 1:05 - loss: 0.3446 - categorical_accuracy: 0.8926
19872/60000 [========>.....................] - ETA: 1:05 - loss: 0.3438 - categorical_accuracy: 0.8929
19936/60000 [========>.....................] - ETA: 1:04 - loss: 0.3428 - categorical_accuracy: 0.8932
19968/60000 [========>.....................] - ETA: 1:04 - loss: 0.3425 - categorical_accuracy: 0.8933
20032/60000 [=========>....................] - ETA: 1:04 - loss: 0.3418 - categorical_accuracy: 0.8936
20064/60000 [=========>....................] - ETA: 1:04 - loss: 0.3413 - categorical_accuracy: 0.8937
20096/60000 [=========>....................] - ETA: 1:04 - loss: 0.3409 - categorical_accuracy: 0.8939
20160/60000 [=========>....................] - ETA: 1:04 - loss: 0.3401 - categorical_accuracy: 0.8941
20224/60000 [=========>....................] - ETA: 1:04 - loss: 0.3396 - categorical_accuracy: 0.8943
20288/60000 [=========>....................] - ETA: 1:04 - loss: 0.3389 - categorical_accuracy: 0.8946
20352/60000 [=========>....................] - ETA: 1:04 - loss: 0.3381 - categorical_accuracy: 0.8949
20384/60000 [=========>....................] - ETA: 1:04 - loss: 0.3381 - categorical_accuracy: 0.8949
20416/60000 [=========>....................] - ETA: 1:04 - loss: 0.3377 - categorical_accuracy: 0.8950
20448/60000 [=========>....................] - ETA: 1:04 - loss: 0.3372 - categorical_accuracy: 0.8952
20480/60000 [=========>....................] - ETA: 1:03 - loss: 0.3367 - categorical_accuracy: 0.8954
20512/60000 [=========>....................] - ETA: 1:03 - loss: 0.3364 - categorical_accuracy: 0.8954
20544/60000 [=========>....................] - ETA: 1:03 - loss: 0.3359 - categorical_accuracy: 0.8956
20576/60000 [=========>....................] - ETA: 1:03 - loss: 0.3356 - categorical_accuracy: 0.8957
20608/60000 [=========>....................] - ETA: 1:03 - loss: 0.3351 - categorical_accuracy: 0.8959
20672/60000 [=========>....................] - ETA: 1:03 - loss: 0.3348 - categorical_accuracy: 0.8959
20736/60000 [=========>....................] - ETA: 1:03 - loss: 0.3344 - categorical_accuracy: 0.8961
20768/60000 [=========>....................] - ETA: 1:03 - loss: 0.3340 - categorical_accuracy: 0.8961
20832/60000 [=========>....................] - ETA: 1:03 - loss: 0.3342 - categorical_accuracy: 0.8960
20896/60000 [=========>....................] - ETA: 1:03 - loss: 0.3337 - categorical_accuracy: 0.8962
20960/60000 [=========>....................] - ETA: 1:03 - loss: 0.3332 - categorical_accuracy: 0.8963
20992/60000 [=========>....................] - ETA: 1:03 - loss: 0.3328 - categorical_accuracy: 0.8965
21024/60000 [=========>....................] - ETA: 1:03 - loss: 0.3327 - categorical_accuracy: 0.8965
21056/60000 [=========>....................] - ETA: 1:03 - loss: 0.3323 - categorical_accuracy: 0.8966
21088/60000 [=========>....................] - ETA: 1:03 - loss: 0.3321 - categorical_accuracy: 0.8967
21120/60000 [=========>....................] - ETA: 1:02 - loss: 0.3317 - categorical_accuracy: 0.8968
21152/60000 [=========>....................] - ETA: 1:02 - loss: 0.3316 - categorical_accuracy: 0.8968
21184/60000 [=========>....................] - ETA: 1:02 - loss: 0.3313 - categorical_accuracy: 0.8970
21248/60000 [=========>....................] - ETA: 1:02 - loss: 0.3306 - categorical_accuracy: 0.8972
21312/60000 [=========>....................] - ETA: 1:02 - loss: 0.3304 - categorical_accuracy: 0.8974
21344/60000 [=========>....................] - ETA: 1:02 - loss: 0.3306 - categorical_accuracy: 0.8974
21376/60000 [=========>....................] - ETA: 1:02 - loss: 0.3301 - categorical_accuracy: 0.8976
21408/60000 [=========>....................] - ETA: 1:02 - loss: 0.3302 - categorical_accuracy: 0.8976
21440/60000 [=========>....................] - ETA: 1:02 - loss: 0.3299 - categorical_accuracy: 0.8977
21472/60000 [=========>....................] - ETA: 1:02 - loss: 0.3295 - categorical_accuracy: 0.8978
21504/60000 [=========>....................] - ETA: 1:02 - loss: 0.3291 - categorical_accuracy: 0.8980
21568/60000 [=========>....................] - ETA: 1:02 - loss: 0.3286 - categorical_accuracy: 0.8982
21632/60000 [=========>....................] - ETA: 1:02 - loss: 0.3280 - categorical_accuracy: 0.8983
21664/60000 [=========>....................] - ETA: 1:02 - loss: 0.3279 - categorical_accuracy: 0.8984
21696/60000 [=========>....................] - ETA: 1:02 - loss: 0.3279 - categorical_accuracy: 0.8984
21728/60000 [=========>....................] - ETA: 1:01 - loss: 0.3278 - categorical_accuracy: 0.8984
21760/60000 [=========>....................] - ETA: 1:01 - loss: 0.3274 - categorical_accuracy: 0.8985
21824/60000 [=========>....................] - ETA: 1:01 - loss: 0.3266 - categorical_accuracy: 0.8988
21888/60000 [=========>....................] - ETA: 1:01 - loss: 0.3261 - categorical_accuracy: 0.8991
21920/60000 [=========>....................] - ETA: 1:01 - loss: 0.3260 - categorical_accuracy: 0.8991
21952/60000 [=========>....................] - ETA: 1:01 - loss: 0.3257 - categorical_accuracy: 0.8992
21984/60000 [=========>....................] - ETA: 1:01 - loss: 0.3254 - categorical_accuracy: 0.8993
22048/60000 [==========>...................] - ETA: 1:01 - loss: 0.3248 - categorical_accuracy: 0.8995
22112/60000 [==========>...................] - ETA: 1:01 - loss: 0.3246 - categorical_accuracy: 0.8996
22176/60000 [==========>...................] - ETA: 1:01 - loss: 0.3239 - categorical_accuracy: 0.8998
22240/60000 [==========>...................] - ETA: 1:01 - loss: 0.3233 - categorical_accuracy: 0.8999
22304/60000 [==========>...................] - ETA: 1:01 - loss: 0.3231 - categorical_accuracy: 0.9000
22336/60000 [==========>...................] - ETA: 1:00 - loss: 0.3228 - categorical_accuracy: 0.9001
22368/60000 [==========>...................] - ETA: 1:00 - loss: 0.3229 - categorical_accuracy: 0.9001
22432/60000 [==========>...................] - ETA: 1:00 - loss: 0.3223 - categorical_accuracy: 0.9003
22464/60000 [==========>...................] - ETA: 1:00 - loss: 0.3219 - categorical_accuracy: 0.9005
22496/60000 [==========>...................] - ETA: 1:00 - loss: 0.3220 - categorical_accuracy: 0.9005
22560/60000 [==========>...................] - ETA: 1:00 - loss: 0.3214 - categorical_accuracy: 0.9006
22592/60000 [==========>...................] - ETA: 1:00 - loss: 0.3213 - categorical_accuracy: 0.9007
22624/60000 [==========>...................] - ETA: 1:00 - loss: 0.3210 - categorical_accuracy: 0.9008
22656/60000 [==========>...................] - ETA: 1:00 - loss: 0.3208 - categorical_accuracy: 0.9008
22688/60000 [==========>...................] - ETA: 1:00 - loss: 0.3206 - categorical_accuracy: 0.9009
22720/60000 [==========>...................] - ETA: 1:00 - loss: 0.3204 - categorical_accuracy: 0.9010
22784/60000 [==========>...................] - ETA: 1:00 - loss: 0.3203 - categorical_accuracy: 0.9010
22848/60000 [==========>...................] - ETA: 1:00 - loss: 0.3198 - categorical_accuracy: 0.9011
22912/60000 [==========>...................] - ETA: 59s - loss: 0.3194 - categorical_accuracy: 0.9012 
22944/60000 [==========>...................] - ETA: 59s - loss: 0.3191 - categorical_accuracy: 0.9013
22976/60000 [==========>...................] - ETA: 59s - loss: 0.3189 - categorical_accuracy: 0.9013
23040/60000 [==========>...................] - ETA: 59s - loss: 0.3184 - categorical_accuracy: 0.9015
23072/60000 [==========>...................] - ETA: 59s - loss: 0.3181 - categorical_accuracy: 0.9016
23104/60000 [==========>...................] - ETA: 59s - loss: 0.3179 - categorical_accuracy: 0.9017
23136/60000 [==========>...................] - ETA: 59s - loss: 0.3176 - categorical_accuracy: 0.9018
23200/60000 [==========>...................] - ETA: 59s - loss: 0.3168 - categorical_accuracy: 0.9020
23264/60000 [==========>...................] - ETA: 59s - loss: 0.3162 - categorical_accuracy: 0.9023
23328/60000 [==========>...................] - ETA: 59s - loss: 0.3158 - categorical_accuracy: 0.9023
23360/60000 [==========>...................] - ETA: 59s - loss: 0.3155 - categorical_accuracy: 0.9024
23392/60000 [==========>...................] - ETA: 59s - loss: 0.3156 - categorical_accuracy: 0.9024
23424/60000 [==========>...................] - ETA: 59s - loss: 0.3153 - categorical_accuracy: 0.9025
23456/60000 [==========>...................] - ETA: 59s - loss: 0.3150 - categorical_accuracy: 0.9027
23488/60000 [==========>...................] - ETA: 59s - loss: 0.3147 - categorical_accuracy: 0.9027
23520/60000 [==========>...................] - ETA: 58s - loss: 0.3148 - categorical_accuracy: 0.9027
23552/60000 [==========>...................] - ETA: 58s - loss: 0.3145 - categorical_accuracy: 0.9028
23584/60000 [==========>...................] - ETA: 58s - loss: 0.3143 - categorical_accuracy: 0.9029
23648/60000 [==========>...................] - ETA: 58s - loss: 0.3140 - categorical_accuracy: 0.9030
23680/60000 [==========>...................] - ETA: 58s - loss: 0.3139 - categorical_accuracy: 0.9031
23712/60000 [==========>...................] - ETA: 58s - loss: 0.3136 - categorical_accuracy: 0.9032
23744/60000 [==========>...................] - ETA: 58s - loss: 0.3133 - categorical_accuracy: 0.9033
23776/60000 [==========>...................] - ETA: 58s - loss: 0.3131 - categorical_accuracy: 0.9034
23840/60000 [==========>...................] - ETA: 58s - loss: 0.3126 - categorical_accuracy: 0.9035
23872/60000 [==========>...................] - ETA: 58s - loss: 0.3123 - categorical_accuracy: 0.9036
23904/60000 [==========>...................] - ETA: 58s - loss: 0.3122 - categorical_accuracy: 0.9036
23968/60000 [==========>...................] - ETA: 58s - loss: 0.3118 - categorical_accuracy: 0.9036
24032/60000 [===========>..................] - ETA: 58s - loss: 0.3120 - categorical_accuracy: 0.9035
24096/60000 [===========>..................] - ETA: 58s - loss: 0.3119 - categorical_accuracy: 0.9036
24128/60000 [===========>..................] - ETA: 57s - loss: 0.3118 - categorical_accuracy: 0.9036
24192/60000 [===========>..................] - ETA: 57s - loss: 0.3113 - categorical_accuracy: 0.9037
24224/60000 [===========>..................] - ETA: 57s - loss: 0.3110 - categorical_accuracy: 0.9038
24288/60000 [===========>..................] - ETA: 57s - loss: 0.3109 - categorical_accuracy: 0.9039
24320/60000 [===========>..................] - ETA: 57s - loss: 0.3105 - categorical_accuracy: 0.9040
24384/60000 [===========>..................] - ETA: 57s - loss: 0.3099 - categorical_accuracy: 0.9042
24416/60000 [===========>..................] - ETA: 57s - loss: 0.3096 - categorical_accuracy: 0.9043
24480/60000 [===========>..................] - ETA: 57s - loss: 0.3091 - categorical_accuracy: 0.9045
24512/60000 [===========>..................] - ETA: 57s - loss: 0.3088 - categorical_accuracy: 0.9046
24544/60000 [===========>..................] - ETA: 57s - loss: 0.3084 - categorical_accuracy: 0.9047
24608/60000 [===========>..................] - ETA: 57s - loss: 0.3080 - categorical_accuracy: 0.9048
24640/60000 [===========>..................] - ETA: 57s - loss: 0.3079 - categorical_accuracy: 0.9048
24672/60000 [===========>..................] - ETA: 57s - loss: 0.3075 - categorical_accuracy: 0.9049
24736/60000 [===========>..................] - ETA: 56s - loss: 0.3071 - categorical_accuracy: 0.9050
24800/60000 [===========>..................] - ETA: 56s - loss: 0.3070 - categorical_accuracy: 0.9052
24864/60000 [===========>..................] - ETA: 56s - loss: 0.3063 - categorical_accuracy: 0.9054
24928/60000 [===========>..................] - ETA: 56s - loss: 0.3058 - categorical_accuracy: 0.9056
24992/60000 [===========>..................] - ETA: 56s - loss: 0.3051 - categorical_accuracy: 0.9058
25024/60000 [===========>..................] - ETA: 56s - loss: 0.3049 - categorical_accuracy: 0.9058
25088/60000 [===========>..................] - ETA: 56s - loss: 0.3046 - categorical_accuracy: 0.9058
25120/60000 [===========>..................] - ETA: 56s - loss: 0.3045 - categorical_accuracy: 0.9059
25152/60000 [===========>..................] - ETA: 56s - loss: 0.3045 - categorical_accuracy: 0.9059
25216/60000 [===========>..................] - ETA: 56s - loss: 0.3039 - categorical_accuracy: 0.9060
25280/60000 [===========>..................] - ETA: 56s - loss: 0.3034 - categorical_accuracy: 0.9061
25344/60000 [===========>..................] - ETA: 56s - loss: 0.3028 - categorical_accuracy: 0.9064
25376/60000 [===========>..................] - ETA: 55s - loss: 0.3027 - categorical_accuracy: 0.9064
25440/60000 [===========>..................] - ETA: 55s - loss: 0.3021 - categorical_accuracy: 0.9066
25472/60000 [===========>..................] - ETA: 55s - loss: 0.3019 - categorical_accuracy: 0.9066
25504/60000 [===========>..................] - ETA: 55s - loss: 0.3017 - categorical_accuracy: 0.9067
25536/60000 [===========>..................] - ETA: 55s - loss: 0.3013 - categorical_accuracy: 0.9068
25568/60000 [===========>..................] - ETA: 55s - loss: 0.3010 - categorical_accuracy: 0.9069
25600/60000 [===========>..................] - ETA: 55s - loss: 0.3007 - categorical_accuracy: 0.9070
25632/60000 [===========>..................] - ETA: 55s - loss: 0.3005 - categorical_accuracy: 0.9071
25696/60000 [===========>..................] - ETA: 55s - loss: 0.3006 - categorical_accuracy: 0.9071
25760/60000 [===========>..................] - ETA: 55s - loss: 0.3000 - categorical_accuracy: 0.9073
25792/60000 [===========>..................] - ETA: 55s - loss: 0.2997 - categorical_accuracy: 0.9074
25856/60000 [===========>..................] - ETA: 55s - loss: 0.2992 - categorical_accuracy: 0.9075
25920/60000 [===========>..................] - ETA: 55s - loss: 0.2989 - categorical_accuracy: 0.9076
25984/60000 [===========>..................] - ETA: 54s - loss: 0.2984 - categorical_accuracy: 0.9078
26048/60000 [============>.................] - ETA: 54s - loss: 0.2982 - categorical_accuracy: 0.9077
26112/60000 [============>.................] - ETA: 54s - loss: 0.2981 - categorical_accuracy: 0.9077
26176/60000 [============>.................] - ETA: 54s - loss: 0.2979 - categorical_accuracy: 0.9078
26208/60000 [============>.................] - ETA: 54s - loss: 0.2977 - categorical_accuracy: 0.9079
26240/60000 [============>.................] - ETA: 54s - loss: 0.2975 - categorical_accuracy: 0.9079
26272/60000 [============>.................] - ETA: 54s - loss: 0.2973 - categorical_accuracy: 0.9080
26304/60000 [============>.................] - ETA: 54s - loss: 0.2973 - categorical_accuracy: 0.9081
26336/60000 [============>.................] - ETA: 54s - loss: 0.2971 - categorical_accuracy: 0.9081
26400/60000 [============>.................] - ETA: 54s - loss: 0.2965 - categorical_accuracy: 0.9083
26432/60000 [============>.................] - ETA: 54s - loss: 0.2961 - categorical_accuracy: 0.9084
26496/60000 [============>.................] - ETA: 54s - loss: 0.2958 - categorical_accuracy: 0.9085
26528/60000 [============>.................] - ETA: 54s - loss: 0.2955 - categorical_accuracy: 0.9085
26560/60000 [============>.................] - ETA: 53s - loss: 0.2953 - categorical_accuracy: 0.9086
26592/60000 [============>.................] - ETA: 53s - loss: 0.2951 - categorical_accuracy: 0.9087
26624/60000 [============>.................] - ETA: 53s - loss: 0.2952 - categorical_accuracy: 0.9087
26656/60000 [============>.................] - ETA: 53s - loss: 0.2950 - categorical_accuracy: 0.9087
26720/60000 [============>.................] - ETA: 53s - loss: 0.2947 - categorical_accuracy: 0.9089
26752/60000 [============>.................] - ETA: 53s - loss: 0.2945 - categorical_accuracy: 0.9089
26784/60000 [============>.................] - ETA: 53s - loss: 0.2942 - categorical_accuracy: 0.9090
26848/60000 [============>.................] - ETA: 53s - loss: 0.2936 - categorical_accuracy: 0.9092
26880/60000 [============>.................] - ETA: 53s - loss: 0.2935 - categorical_accuracy: 0.9093
26944/60000 [============>.................] - ETA: 53s - loss: 0.2932 - categorical_accuracy: 0.9093
27008/60000 [============>.................] - ETA: 53s - loss: 0.2926 - categorical_accuracy: 0.9095
27072/60000 [============>.................] - ETA: 53s - loss: 0.2922 - categorical_accuracy: 0.9096
27104/60000 [============>.................] - ETA: 53s - loss: 0.2921 - categorical_accuracy: 0.9096
27168/60000 [============>.................] - ETA: 52s - loss: 0.2918 - categorical_accuracy: 0.9096
27232/60000 [============>.................] - ETA: 52s - loss: 0.2914 - categorical_accuracy: 0.9098
27296/60000 [============>.................] - ETA: 52s - loss: 0.2914 - categorical_accuracy: 0.9098
27328/60000 [============>.................] - ETA: 52s - loss: 0.2911 - categorical_accuracy: 0.9099
27392/60000 [============>.................] - ETA: 52s - loss: 0.2906 - categorical_accuracy: 0.9101
27424/60000 [============>.................] - ETA: 52s - loss: 0.2905 - categorical_accuracy: 0.9101
27456/60000 [============>.................] - ETA: 52s - loss: 0.2902 - categorical_accuracy: 0.9102
27488/60000 [============>.................] - ETA: 52s - loss: 0.2899 - categorical_accuracy: 0.9103
27520/60000 [============>.................] - ETA: 52s - loss: 0.2898 - categorical_accuracy: 0.9103
27552/60000 [============>.................] - ETA: 52s - loss: 0.2896 - categorical_accuracy: 0.9104
27584/60000 [============>.................] - ETA: 52s - loss: 0.2895 - categorical_accuracy: 0.9104
27648/60000 [============>.................] - ETA: 52s - loss: 0.2894 - categorical_accuracy: 0.9104
27680/60000 [============>.................] - ETA: 52s - loss: 0.2893 - categorical_accuracy: 0.9105
27712/60000 [============>.................] - ETA: 52s - loss: 0.2891 - categorical_accuracy: 0.9105
27744/60000 [============>.................] - ETA: 52s - loss: 0.2888 - categorical_accuracy: 0.9106
27776/60000 [============>.................] - ETA: 52s - loss: 0.2886 - categorical_accuracy: 0.9106
27808/60000 [============>.................] - ETA: 51s - loss: 0.2884 - categorical_accuracy: 0.9107
27872/60000 [============>.................] - ETA: 51s - loss: 0.2880 - categorical_accuracy: 0.9108
27936/60000 [============>.................] - ETA: 51s - loss: 0.2875 - categorical_accuracy: 0.9109
27968/60000 [============>.................] - ETA: 51s - loss: 0.2873 - categorical_accuracy: 0.9110
28000/60000 [=============>................] - ETA: 51s - loss: 0.2871 - categorical_accuracy: 0.9110
28064/60000 [=============>................] - ETA: 51s - loss: 0.2869 - categorical_accuracy: 0.9111
28128/60000 [=============>................] - ETA: 51s - loss: 0.2865 - categorical_accuracy: 0.9113
28160/60000 [=============>................] - ETA: 51s - loss: 0.2862 - categorical_accuracy: 0.9114
28224/60000 [=============>................] - ETA: 51s - loss: 0.2857 - categorical_accuracy: 0.9115
28256/60000 [=============>................] - ETA: 51s - loss: 0.2854 - categorical_accuracy: 0.9116
28288/60000 [=============>................] - ETA: 51s - loss: 0.2851 - categorical_accuracy: 0.9117
28320/60000 [=============>................] - ETA: 51s - loss: 0.2849 - categorical_accuracy: 0.9118
28352/60000 [=============>................] - ETA: 51s - loss: 0.2846 - categorical_accuracy: 0.9119
28384/60000 [=============>................] - ETA: 50s - loss: 0.2845 - categorical_accuracy: 0.9120
28448/60000 [=============>................] - ETA: 50s - loss: 0.2841 - categorical_accuracy: 0.9121
28512/60000 [=============>................] - ETA: 50s - loss: 0.2835 - categorical_accuracy: 0.9122
28576/60000 [=============>................] - ETA: 50s - loss: 0.2832 - categorical_accuracy: 0.9123
28640/60000 [=============>................] - ETA: 50s - loss: 0.2831 - categorical_accuracy: 0.9124
28672/60000 [=============>................] - ETA: 50s - loss: 0.2830 - categorical_accuracy: 0.9125
28704/60000 [=============>................] - ETA: 50s - loss: 0.2827 - categorical_accuracy: 0.9125
28736/60000 [=============>................] - ETA: 50s - loss: 0.2826 - categorical_accuracy: 0.9125
28768/60000 [=============>................] - ETA: 50s - loss: 0.2823 - categorical_accuracy: 0.9126
28800/60000 [=============>................] - ETA: 50s - loss: 0.2820 - categorical_accuracy: 0.9127
28832/60000 [=============>................] - ETA: 50s - loss: 0.2818 - categorical_accuracy: 0.9128
28864/60000 [=============>................] - ETA: 50s - loss: 0.2817 - categorical_accuracy: 0.9128
28896/60000 [=============>................] - ETA: 50s - loss: 0.2815 - categorical_accuracy: 0.9129
28928/60000 [=============>................] - ETA: 50s - loss: 0.2813 - categorical_accuracy: 0.9129
28960/60000 [=============>................] - ETA: 50s - loss: 0.2811 - categorical_accuracy: 0.9129
28992/60000 [=============>................] - ETA: 50s - loss: 0.2809 - categorical_accuracy: 0.9130
29024/60000 [=============>................] - ETA: 49s - loss: 0.2808 - categorical_accuracy: 0.9131
29088/60000 [=============>................] - ETA: 49s - loss: 0.2808 - categorical_accuracy: 0.9130
29120/60000 [=============>................] - ETA: 49s - loss: 0.2805 - categorical_accuracy: 0.9131
29152/60000 [=============>................] - ETA: 49s - loss: 0.2804 - categorical_accuracy: 0.9131
29216/60000 [=============>................] - ETA: 49s - loss: 0.2799 - categorical_accuracy: 0.9133
29280/60000 [=============>................] - ETA: 49s - loss: 0.2798 - categorical_accuracy: 0.9134
29344/60000 [=============>................] - ETA: 49s - loss: 0.2794 - categorical_accuracy: 0.9135
29376/60000 [=============>................] - ETA: 49s - loss: 0.2793 - categorical_accuracy: 0.9135
29440/60000 [=============>................] - ETA: 49s - loss: 0.2790 - categorical_accuracy: 0.9137
29504/60000 [=============>................] - ETA: 49s - loss: 0.2787 - categorical_accuracy: 0.9137
29568/60000 [=============>................] - ETA: 49s - loss: 0.2785 - categorical_accuracy: 0.9138
29632/60000 [=============>................] - ETA: 48s - loss: 0.2783 - categorical_accuracy: 0.9138
29696/60000 [=============>................] - ETA: 48s - loss: 0.2779 - categorical_accuracy: 0.9140
29728/60000 [=============>................] - ETA: 48s - loss: 0.2776 - categorical_accuracy: 0.9141
29792/60000 [=============>................] - ETA: 48s - loss: 0.2774 - categorical_accuracy: 0.9142
29824/60000 [=============>................] - ETA: 48s - loss: 0.2771 - categorical_accuracy: 0.9143
29856/60000 [=============>................] - ETA: 48s - loss: 0.2770 - categorical_accuracy: 0.9143
29920/60000 [=============>................] - ETA: 48s - loss: 0.2767 - categorical_accuracy: 0.9144
29952/60000 [=============>................] - ETA: 48s - loss: 0.2766 - categorical_accuracy: 0.9144
29984/60000 [=============>................] - ETA: 48s - loss: 0.2764 - categorical_accuracy: 0.9145
30016/60000 [==============>...............] - ETA: 48s - loss: 0.2762 - categorical_accuracy: 0.9145
30048/60000 [==============>...............] - ETA: 48s - loss: 0.2761 - categorical_accuracy: 0.9146
30080/60000 [==============>...............] - ETA: 48s - loss: 0.2758 - categorical_accuracy: 0.9147
30112/60000 [==============>...............] - ETA: 48s - loss: 0.2756 - categorical_accuracy: 0.9147
30176/60000 [==============>...............] - ETA: 48s - loss: 0.2752 - categorical_accuracy: 0.9148
30208/60000 [==============>...............] - ETA: 48s - loss: 0.2751 - categorical_accuracy: 0.9148
30240/60000 [==============>...............] - ETA: 47s - loss: 0.2751 - categorical_accuracy: 0.9148
30304/60000 [==============>...............] - ETA: 47s - loss: 0.2749 - categorical_accuracy: 0.9149
30368/60000 [==============>...............] - ETA: 47s - loss: 0.2746 - categorical_accuracy: 0.9149
30432/60000 [==============>...............] - ETA: 47s - loss: 0.2742 - categorical_accuracy: 0.9150
30496/60000 [==============>...............] - ETA: 47s - loss: 0.2738 - categorical_accuracy: 0.9152
30560/60000 [==============>...............] - ETA: 47s - loss: 0.2734 - categorical_accuracy: 0.9152
30624/60000 [==============>...............] - ETA: 47s - loss: 0.2731 - categorical_accuracy: 0.9153
30656/60000 [==============>...............] - ETA: 47s - loss: 0.2730 - categorical_accuracy: 0.9154
30720/60000 [==============>...............] - ETA: 47s - loss: 0.2727 - categorical_accuracy: 0.9154
30752/60000 [==============>...............] - ETA: 47s - loss: 0.2725 - categorical_accuracy: 0.9155
30784/60000 [==============>...............] - ETA: 47s - loss: 0.2722 - categorical_accuracy: 0.9156
30816/60000 [==============>...............] - ETA: 47s - loss: 0.2720 - categorical_accuracy: 0.9157
30848/60000 [==============>...............] - ETA: 47s - loss: 0.2717 - categorical_accuracy: 0.9158
30880/60000 [==============>...............] - ETA: 46s - loss: 0.2715 - categorical_accuracy: 0.9159
30912/60000 [==============>...............] - ETA: 46s - loss: 0.2714 - categorical_accuracy: 0.9159
30944/60000 [==============>...............] - ETA: 46s - loss: 0.2712 - categorical_accuracy: 0.9159
30976/60000 [==============>...............] - ETA: 46s - loss: 0.2709 - categorical_accuracy: 0.9160
31040/60000 [==============>...............] - ETA: 46s - loss: 0.2709 - categorical_accuracy: 0.9161
31104/60000 [==============>...............] - ETA: 46s - loss: 0.2704 - categorical_accuracy: 0.9162
31168/60000 [==============>...............] - ETA: 46s - loss: 0.2702 - categorical_accuracy: 0.9163
31200/60000 [==============>...............] - ETA: 46s - loss: 0.2701 - categorical_accuracy: 0.9163
31232/60000 [==============>...............] - ETA: 46s - loss: 0.2699 - categorical_accuracy: 0.9164
31264/60000 [==============>...............] - ETA: 46s - loss: 0.2699 - categorical_accuracy: 0.9164
31296/60000 [==============>...............] - ETA: 46s - loss: 0.2697 - categorical_accuracy: 0.9164
31360/60000 [==============>...............] - ETA: 46s - loss: 0.2693 - categorical_accuracy: 0.9165
31392/60000 [==============>...............] - ETA: 46s - loss: 0.2692 - categorical_accuracy: 0.9165
31424/60000 [==============>...............] - ETA: 46s - loss: 0.2690 - categorical_accuracy: 0.9166
31456/60000 [==============>...............] - ETA: 46s - loss: 0.2688 - categorical_accuracy: 0.9167
31488/60000 [==============>...............] - ETA: 45s - loss: 0.2686 - categorical_accuracy: 0.9167
31552/60000 [==============>...............] - ETA: 45s - loss: 0.2684 - categorical_accuracy: 0.9168
31584/60000 [==============>...............] - ETA: 45s - loss: 0.2682 - categorical_accuracy: 0.9168
31648/60000 [==============>...............] - ETA: 45s - loss: 0.2677 - categorical_accuracy: 0.9170
31680/60000 [==============>...............] - ETA: 45s - loss: 0.2675 - categorical_accuracy: 0.9171
31712/60000 [==============>...............] - ETA: 45s - loss: 0.2674 - categorical_accuracy: 0.9171
31744/60000 [==============>...............] - ETA: 45s - loss: 0.2672 - categorical_accuracy: 0.9171
31808/60000 [==============>...............] - ETA: 45s - loss: 0.2669 - categorical_accuracy: 0.9172
31840/60000 [==============>...............] - ETA: 45s - loss: 0.2667 - categorical_accuracy: 0.9172
31904/60000 [==============>...............] - ETA: 45s - loss: 0.2663 - categorical_accuracy: 0.9173
31968/60000 [==============>...............] - ETA: 45s - loss: 0.2660 - categorical_accuracy: 0.9175
32032/60000 [===============>..............] - ETA: 45s - loss: 0.2659 - categorical_accuracy: 0.9175
32096/60000 [===============>..............] - ETA: 44s - loss: 0.2655 - categorical_accuracy: 0.9177
32160/60000 [===============>..............] - ETA: 44s - loss: 0.2652 - categorical_accuracy: 0.9178
32224/60000 [===============>..............] - ETA: 44s - loss: 0.2648 - categorical_accuracy: 0.9179
32256/60000 [===============>..............] - ETA: 44s - loss: 0.2646 - categorical_accuracy: 0.9180
32288/60000 [===============>..............] - ETA: 44s - loss: 0.2645 - categorical_accuracy: 0.9180
32320/60000 [===============>..............] - ETA: 44s - loss: 0.2643 - categorical_accuracy: 0.9181
32384/60000 [===============>..............] - ETA: 44s - loss: 0.2644 - categorical_accuracy: 0.9181
32448/60000 [===============>..............] - ETA: 44s - loss: 0.2644 - categorical_accuracy: 0.9182
32512/60000 [===============>..............] - ETA: 44s - loss: 0.2640 - categorical_accuracy: 0.9183
32544/60000 [===============>..............] - ETA: 44s - loss: 0.2638 - categorical_accuracy: 0.9184
32608/60000 [===============>..............] - ETA: 44s - loss: 0.2636 - categorical_accuracy: 0.9185
32640/60000 [===============>..............] - ETA: 44s - loss: 0.2634 - categorical_accuracy: 0.9186
32672/60000 [===============>..............] - ETA: 44s - loss: 0.2632 - categorical_accuracy: 0.9186
32704/60000 [===============>..............] - ETA: 44s - loss: 0.2631 - categorical_accuracy: 0.9187
32768/60000 [===============>..............] - ETA: 43s - loss: 0.2627 - categorical_accuracy: 0.9188
32832/60000 [===============>..............] - ETA: 43s - loss: 0.2625 - categorical_accuracy: 0.9188
32864/60000 [===============>..............] - ETA: 43s - loss: 0.2623 - categorical_accuracy: 0.9189
32896/60000 [===============>..............] - ETA: 43s - loss: 0.2622 - categorical_accuracy: 0.9190
32960/60000 [===============>..............] - ETA: 43s - loss: 0.2619 - categorical_accuracy: 0.9190
33024/60000 [===============>..............] - ETA: 43s - loss: 0.2615 - categorical_accuracy: 0.9192
33056/60000 [===============>..............] - ETA: 43s - loss: 0.2613 - categorical_accuracy: 0.9192
33120/60000 [===============>..............] - ETA: 43s - loss: 0.2609 - categorical_accuracy: 0.9193
33152/60000 [===============>..............] - ETA: 43s - loss: 0.2607 - categorical_accuracy: 0.9194
33184/60000 [===============>..............] - ETA: 43s - loss: 0.2604 - categorical_accuracy: 0.9194
33248/60000 [===============>..............] - ETA: 43s - loss: 0.2603 - categorical_accuracy: 0.9195
33312/60000 [===============>..............] - ETA: 43s - loss: 0.2601 - categorical_accuracy: 0.9196
33376/60000 [===============>..............] - ETA: 42s - loss: 0.2598 - categorical_accuracy: 0.9197
33408/60000 [===============>..............] - ETA: 42s - loss: 0.2596 - categorical_accuracy: 0.9198
33472/60000 [===============>..............] - ETA: 42s - loss: 0.2595 - categorical_accuracy: 0.9198
33504/60000 [===============>..............] - ETA: 42s - loss: 0.2593 - categorical_accuracy: 0.9199
33536/60000 [===============>..............] - ETA: 42s - loss: 0.2591 - categorical_accuracy: 0.9199
33568/60000 [===============>..............] - ETA: 42s - loss: 0.2589 - categorical_accuracy: 0.9200
33600/60000 [===============>..............] - ETA: 42s - loss: 0.2589 - categorical_accuracy: 0.9200
33632/60000 [===============>..............] - ETA: 42s - loss: 0.2588 - categorical_accuracy: 0.9200
33696/60000 [===============>..............] - ETA: 42s - loss: 0.2586 - categorical_accuracy: 0.9201
33760/60000 [===============>..............] - ETA: 42s - loss: 0.2583 - categorical_accuracy: 0.9202
33824/60000 [===============>..............] - ETA: 42s - loss: 0.2579 - categorical_accuracy: 0.9203
33856/60000 [===============>..............] - ETA: 42s - loss: 0.2578 - categorical_accuracy: 0.9203
33920/60000 [===============>..............] - ETA: 42s - loss: 0.2574 - categorical_accuracy: 0.9205
33984/60000 [===============>..............] - ETA: 41s - loss: 0.2570 - categorical_accuracy: 0.9206
34016/60000 [================>.............] - ETA: 41s - loss: 0.2569 - categorical_accuracy: 0.9206
34048/60000 [================>.............] - ETA: 41s - loss: 0.2567 - categorical_accuracy: 0.9207
34080/60000 [================>.............] - ETA: 41s - loss: 0.2567 - categorical_accuracy: 0.9206
34144/60000 [================>.............] - ETA: 41s - loss: 0.2563 - categorical_accuracy: 0.9207
34208/60000 [================>.............] - ETA: 41s - loss: 0.2559 - categorical_accuracy: 0.9209
34240/60000 [================>.............] - ETA: 41s - loss: 0.2558 - categorical_accuracy: 0.9209
34272/60000 [================>.............] - ETA: 41s - loss: 0.2556 - categorical_accuracy: 0.9210
34336/60000 [================>.............] - ETA: 41s - loss: 0.2552 - categorical_accuracy: 0.9211
34368/60000 [================>.............] - ETA: 41s - loss: 0.2550 - categorical_accuracy: 0.9212
34400/60000 [================>.............] - ETA: 41s - loss: 0.2548 - categorical_accuracy: 0.9212
34464/60000 [================>.............] - ETA: 41s - loss: 0.2544 - categorical_accuracy: 0.9214
34496/60000 [================>.............] - ETA: 41s - loss: 0.2543 - categorical_accuracy: 0.9214
34528/60000 [================>.............] - ETA: 41s - loss: 0.2541 - categorical_accuracy: 0.9215
34560/60000 [================>.............] - ETA: 40s - loss: 0.2539 - categorical_accuracy: 0.9215
34592/60000 [================>.............] - ETA: 40s - loss: 0.2539 - categorical_accuracy: 0.9216
34624/60000 [================>.............] - ETA: 40s - loss: 0.2537 - categorical_accuracy: 0.9216
34656/60000 [================>.............] - ETA: 40s - loss: 0.2537 - categorical_accuracy: 0.9217
34688/60000 [================>.............] - ETA: 40s - loss: 0.2537 - categorical_accuracy: 0.9217
34720/60000 [================>.............] - ETA: 40s - loss: 0.2535 - categorical_accuracy: 0.9217
34784/60000 [================>.............] - ETA: 40s - loss: 0.2533 - categorical_accuracy: 0.9218
34816/60000 [================>.............] - ETA: 40s - loss: 0.2531 - categorical_accuracy: 0.9218
34848/60000 [================>.............] - ETA: 40s - loss: 0.2530 - categorical_accuracy: 0.9218
34912/60000 [================>.............] - ETA: 40s - loss: 0.2530 - categorical_accuracy: 0.9218
34944/60000 [================>.............] - ETA: 40s - loss: 0.2529 - categorical_accuracy: 0.9219
35008/60000 [================>.............] - ETA: 40s - loss: 0.2528 - categorical_accuracy: 0.9219
35072/60000 [================>.............] - ETA: 40s - loss: 0.2524 - categorical_accuracy: 0.9220
35104/60000 [================>.............] - ETA: 40s - loss: 0.2523 - categorical_accuracy: 0.9221
35168/60000 [================>.............] - ETA: 39s - loss: 0.2519 - categorical_accuracy: 0.9222
35232/60000 [================>.............] - ETA: 39s - loss: 0.2517 - categorical_accuracy: 0.9223
35264/60000 [================>.............] - ETA: 39s - loss: 0.2516 - categorical_accuracy: 0.9223
35296/60000 [================>.............] - ETA: 39s - loss: 0.2514 - categorical_accuracy: 0.9224
35328/60000 [================>.............] - ETA: 39s - loss: 0.2513 - categorical_accuracy: 0.9224
35360/60000 [================>.............] - ETA: 39s - loss: 0.2511 - categorical_accuracy: 0.9224
35392/60000 [================>.............] - ETA: 39s - loss: 0.2509 - categorical_accuracy: 0.9225
35424/60000 [================>.............] - ETA: 39s - loss: 0.2507 - categorical_accuracy: 0.9226
35488/60000 [================>.............] - ETA: 39s - loss: 0.2503 - categorical_accuracy: 0.9227
35552/60000 [================>.............] - ETA: 39s - loss: 0.2498 - categorical_accuracy: 0.9228
35584/60000 [================>.............] - ETA: 39s - loss: 0.2498 - categorical_accuracy: 0.9229
35648/60000 [================>.............] - ETA: 39s - loss: 0.2496 - categorical_accuracy: 0.9229
35680/60000 [================>.............] - ETA: 39s - loss: 0.2499 - categorical_accuracy: 0.9229
35712/60000 [================>.............] - ETA: 39s - loss: 0.2498 - categorical_accuracy: 0.9229
35744/60000 [================>.............] - ETA: 39s - loss: 0.2498 - categorical_accuracy: 0.9230
35808/60000 [================>.............] - ETA: 38s - loss: 0.2494 - categorical_accuracy: 0.9231
35872/60000 [================>.............] - ETA: 38s - loss: 0.2492 - categorical_accuracy: 0.9231
35936/60000 [================>.............] - ETA: 38s - loss: 0.2488 - categorical_accuracy: 0.9233
36000/60000 [=================>............] - ETA: 38s - loss: 0.2485 - categorical_accuracy: 0.9233
36032/60000 [=================>............] - ETA: 38s - loss: 0.2483 - categorical_accuracy: 0.9234
36064/60000 [=================>............] - ETA: 38s - loss: 0.2482 - categorical_accuracy: 0.9234
36096/60000 [=================>............] - ETA: 38s - loss: 0.2480 - categorical_accuracy: 0.9235
36128/60000 [=================>............] - ETA: 38s - loss: 0.2479 - categorical_accuracy: 0.9235
36192/60000 [=================>............] - ETA: 38s - loss: 0.2480 - categorical_accuracy: 0.9235
36224/60000 [=================>............] - ETA: 38s - loss: 0.2478 - categorical_accuracy: 0.9235
36288/60000 [=================>............] - ETA: 38s - loss: 0.2474 - categorical_accuracy: 0.9237
36320/60000 [=================>............] - ETA: 38s - loss: 0.2472 - categorical_accuracy: 0.9237
36352/60000 [=================>............] - ETA: 38s - loss: 0.2471 - categorical_accuracy: 0.9238
36416/60000 [=================>............] - ETA: 37s - loss: 0.2469 - categorical_accuracy: 0.9239
36448/60000 [=================>............] - ETA: 37s - loss: 0.2468 - categorical_accuracy: 0.9239
36512/60000 [=================>............] - ETA: 37s - loss: 0.2464 - categorical_accuracy: 0.9240
36544/60000 [=================>............] - ETA: 37s - loss: 0.2462 - categorical_accuracy: 0.9240
36576/60000 [=================>............] - ETA: 37s - loss: 0.2461 - categorical_accuracy: 0.9241
36640/60000 [=================>............] - ETA: 37s - loss: 0.2458 - categorical_accuracy: 0.9241
36672/60000 [=================>............] - ETA: 37s - loss: 0.2456 - categorical_accuracy: 0.9242
36704/60000 [=================>............] - ETA: 37s - loss: 0.2454 - categorical_accuracy: 0.9243
36768/60000 [=================>............] - ETA: 37s - loss: 0.2454 - categorical_accuracy: 0.9243
36832/60000 [=================>............] - ETA: 37s - loss: 0.2452 - categorical_accuracy: 0.9244
36896/60000 [=================>............] - ETA: 37s - loss: 0.2451 - categorical_accuracy: 0.9244
36960/60000 [=================>............] - ETA: 37s - loss: 0.2451 - categorical_accuracy: 0.9245
36992/60000 [=================>............] - ETA: 37s - loss: 0.2450 - categorical_accuracy: 0.9245
37024/60000 [=================>............] - ETA: 36s - loss: 0.2449 - categorical_accuracy: 0.9245
37056/60000 [=================>............] - ETA: 36s - loss: 0.2448 - categorical_accuracy: 0.9246
37088/60000 [=================>............] - ETA: 36s - loss: 0.2447 - categorical_accuracy: 0.9246
37152/60000 [=================>............] - ETA: 36s - loss: 0.2443 - categorical_accuracy: 0.9247
37216/60000 [=================>............] - ETA: 36s - loss: 0.2439 - categorical_accuracy: 0.9248
37280/60000 [=================>............] - ETA: 36s - loss: 0.2440 - categorical_accuracy: 0.9248
37312/60000 [=================>............] - ETA: 36s - loss: 0.2439 - categorical_accuracy: 0.9249
37344/60000 [=================>............] - ETA: 36s - loss: 0.2437 - categorical_accuracy: 0.9249
37408/60000 [=================>............] - ETA: 36s - loss: 0.2436 - categorical_accuracy: 0.9249
37472/60000 [=================>............] - ETA: 36s - loss: 0.2435 - categorical_accuracy: 0.9250
37504/60000 [=================>............] - ETA: 36s - loss: 0.2434 - categorical_accuracy: 0.9250
37568/60000 [=================>............] - ETA: 36s - loss: 0.2432 - categorical_accuracy: 0.9251
37632/60000 [=================>............] - ETA: 35s - loss: 0.2431 - categorical_accuracy: 0.9251
37664/60000 [=================>............] - ETA: 35s - loss: 0.2429 - categorical_accuracy: 0.9252
37696/60000 [=================>............] - ETA: 35s - loss: 0.2427 - categorical_accuracy: 0.9252
37760/60000 [=================>............] - ETA: 35s - loss: 0.2427 - categorical_accuracy: 0.9252
37824/60000 [=================>............] - ETA: 35s - loss: 0.2428 - categorical_accuracy: 0.9253
37888/60000 [=================>............] - ETA: 35s - loss: 0.2425 - categorical_accuracy: 0.9253
37920/60000 [=================>............] - ETA: 35s - loss: 0.2424 - categorical_accuracy: 0.9254
37952/60000 [=================>............] - ETA: 35s - loss: 0.2424 - categorical_accuracy: 0.9254
37984/60000 [=================>............] - ETA: 35s - loss: 0.2423 - categorical_accuracy: 0.9254
38016/60000 [==================>...........] - ETA: 35s - loss: 0.2421 - categorical_accuracy: 0.9255
38048/60000 [==================>...........] - ETA: 35s - loss: 0.2421 - categorical_accuracy: 0.9255
38080/60000 [==================>...........] - ETA: 35s - loss: 0.2419 - categorical_accuracy: 0.9255
38112/60000 [==================>...........] - ETA: 35s - loss: 0.2417 - categorical_accuracy: 0.9256
38144/60000 [==================>...........] - ETA: 35s - loss: 0.2416 - categorical_accuracy: 0.9256
38176/60000 [==================>...........] - ETA: 35s - loss: 0.2416 - categorical_accuracy: 0.9256
38240/60000 [==================>...........] - ETA: 35s - loss: 0.2412 - categorical_accuracy: 0.9257
38304/60000 [==================>...........] - ETA: 34s - loss: 0.2410 - categorical_accuracy: 0.9258
38336/60000 [==================>...........] - ETA: 34s - loss: 0.2408 - categorical_accuracy: 0.9258
38400/60000 [==================>...........] - ETA: 34s - loss: 0.2407 - categorical_accuracy: 0.9259
38432/60000 [==================>...........] - ETA: 34s - loss: 0.2405 - categorical_accuracy: 0.9259
38464/60000 [==================>...........] - ETA: 34s - loss: 0.2404 - categorical_accuracy: 0.9259
38528/60000 [==================>...........] - ETA: 34s - loss: 0.2401 - categorical_accuracy: 0.9260
38592/60000 [==================>...........] - ETA: 34s - loss: 0.2398 - categorical_accuracy: 0.9261
38624/60000 [==================>...........] - ETA: 34s - loss: 0.2397 - categorical_accuracy: 0.9261
38688/60000 [==================>...........] - ETA: 34s - loss: 0.2393 - categorical_accuracy: 0.9262
38720/60000 [==================>...........] - ETA: 34s - loss: 0.2392 - categorical_accuracy: 0.9263
38784/60000 [==================>...........] - ETA: 34s - loss: 0.2392 - categorical_accuracy: 0.9263
38816/60000 [==================>...........] - ETA: 34s - loss: 0.2393 - categorical_accuracy: 0.9263
38880/60000 [==================>...........] - ETA: 33s - loss: 0.2390 - categorical_accuracy: 0.9264
38944/60000 [==================>...........] - ETA: 33s - loss: 0.2390 - categorical_accuracy: 0.9264
38976/60000 [==================>...........] - ETA: 33s - loss: 0.2389 - categorical_accuracy: 0.9264
39040/60000 [==================>...........] - ETA: 33s - loss: 0.2387 - categorical_accuracy: 0.9265
39104/60000 [==================>...........] - ETA: 33s - loss: 0.2385 - categorical_accuracy: 0.9266
39136/60000 [==================>...........] - ETA: 33s - loss: 0.2384 - categorical_accuracy: 0.9266
39168/60000 [==================>...........] - ETA: 33s - loss: 0.2383 - categorical_accuracy: 0.9266
39200/60000 [==================>...........] - ETA: 33s - loss: 0.2382 - categorical_accuracy: 0.9267
39264/60000 [==================>...........] - ETA: 33s - loss: 0.2382 - categorical_accuracy: 0.9267
39296/60000 [==================>...........] - ETA: 33s - loss: 0.2380 - categorical_accuracy: 0.9267
39360/60000 [==================>...........] - ETA: 33s - loss: 0.2377 - categorical_accuracy: 0.9268
39392/60000 [==================>...........] - ETA: 33s - loss: 0.2376 - categorical_accuracy: 0.9269
39424/60000 [==================>...........] - ETA: 33s - loss: 0.2375 - categorical_accuracy: 0.9269
39456/60000 [==================>...........] - ETA: 33s - loss: 0.2373 - categorical_accuracy: 0.9270
39520/60000 [==================>...........] - ETA: 32s - loss: 0.2371 - categorical_accuracy: 0.9270
39552/60000 [==================>...........] - ETA: 32s - loss: 0.2369 - categorical_accuracy: 0.9271
39584/60000 [==================>...........] - ETA: 32s - loss: 0.2369 - categorical_accuracy: 0.9271
39648/60000 [==================>...........] - ETA: 32s - loss: 0.2366 - categorical_accuracy: 0.9272
39680/60000 [==================>...........] - ETA: 32s - loss: 0.2366 - categorical_accuracy: 0.9272
39712/60000 [==================>...........] - ETA: 32s - loss: 0.2365 - categorical_accuracy: 0.9273
39776/60000 [==================>...........] - ETA: 32s - loss: 0.2363 - categorical_accuracy: 0.9273
39840/60000 [==================>...........] - ETA: 32s - loss: 0.2360 - categorical_accuracy: 0.9274
39872/60000 [==================>...........] - ETA: 32s - loss: 0.2360 - categorical_accuracy: 0.9274
39904/60000 [==================>...........] - ETA: 32s - loss: 0.2358 - categorical_accuracy: 0.9275
39936/60000 [==================>...........] - ETA: 32s - loss: 0.2357 - categorical_accuracy: 0.9275
39968/60000 [==================>...........] - ETA: 32s - loss: 0.2356 - categorical_accuracy: 0.9275
40000/60000 [===================>..........] - ETA: 32s - loss: 0.2357 - categorical_accuracy: 0.9276
40032/60000 [===================>..........] - ETA: 32s - loss: 0.2355 - categorical_accuracy: 0.9276
40096/60000 [===================>..........] - ETA: 32s - loss: 0.2354 - categorical_accuracy: 0.9276
40160/60000 [===================>..........] - ETA: 31s - loss: 0.2352 - categorical_accuracy: 0.9277
40192/60000 [===================>..........] - ETA: 31s - loss: 0.2352 - categorical_accuracy: 0.9277
40224/60000 [===================>..........] - ETA: 31s - loss: 0.2351 - categorical_accuracy: 0.9278
40256/60000 [===================>..........] - ETA: 31s - loss: 0.2350 - categorical_accuracy: 0.9278
40288/60000 [===================>..........] - ETA: 31s - loss: 0.2348 - categorical_accuracy: 0.9278
40352/60000 [===================>..........] - ETA: 31s - loss: 0.2346 - categorical_accuracy: 0.9279
40384/60000 [===================>..........] - ETA: 31s - loss: 0.2345 - categorical_accuracy: 0.9279
40416/60000 [===================>..........] - ETA: 31s - loss: 0.2345 - categorical_accuracy: 0.9279
40480/60000 [===================>..........] - ETA: 31s - loss: 0.2343 - categorical_accuracy: 0.9280
40512/60000 [===================>..........] - ETA: 31s - loss: 0.2342 - categorical_accuracy: 0.9280
40544/60000 [===================>..........] - ETA: 31s - loss: 0.2341 - categorical_accuracy: 0.9281
40576/60000 [===================>..........] - ETA: 31s - loss: 0.2340 - categorical_accuracy: 0.9281
40608/60000 [===================>..........] - ETA: 31s - loss: 0.2338 - categorical_accuracy: 0.9281
40672/60000 [===================>..........] - ETA: 31s - loss: 0.2335 - categorical_accuracy: 0.9282
40704/60000 [===================>..........] - ETA: 31s - loss: 0.2334 - categorical_accuracy: 0.9283
40768/60000 [===================>..........] - ETA: 30s - loss: 0.2331 - categorical_accuracy: 0.9284
40800/60000 [===================>..........] - ETA: 30s - loss: 0.2329 - categorical_accuracy: 0.9284
40832/60000 [===================>..........] - ETA: 30s - loss: 0.2328 - categorical_accuracy: 0.9285
40896/60000 [===================>..........] - ETA: 30s - loss: 0.2325 - categorical_accuracy: 0.9286
40960/60000 [===================>..........] - ETA: 30s - loss: 0.2323 - categorical_accuracy: 0.9286
40992/60000 [===================>..........] - ETA: 30s - loss: 0.2322 - categorical_accuracy: 0.9286
41056/60000 [===================>..........] - ETA: 30s - loss: 0.2319 - categorical_accuracy: 0.9287
41120/60000 [===================>..........] - ETA: 30s - loss: 0.2319 - categorical_accuracy: 0.9287
41152/60000 [===================>..........] - ETA: 30s - loss: 0.2318 - categorical_accuracy: 0.9288
41216/60000 [===================>..........] - ETA: 30s - loss: 0.2315 - categorical_accuracy: 0.9289
41280/60000 [===================>..........] - ETA: 30s - loss: 0.2312 - categorical_accuracy: 0.9290
41312/60000 [===================>..........] - ETA: 30s - loss: 0.2310 - categorical_accuracy: 0.9290
41376/60000 [===================>..........] - ETA: 29s - loss: 0.2308 - categorical_accuracy: 0.9291
41440/60000 [===================>..........] - ETA: 29s - loss: 0.2304 - categorical_accuracy: 0.9292
41472/60000 [===================>..........] - ETA: 29s - loss: 0.2304 - categorical_accuracy: 0.9293
41536/60000 [===================>..........] - ETA: 29s - loss: 0.2302 - categorical_accuracy: 0.9293
41600/60000 [===================>..........] - ETA: 29s - loss: 0.2301 - categorical_accuracy: 0.9293
41664/60000 [===================>..........] - ETA: 29s - loss: 0.2298 - categorical_accuracy: 0.9293
41728/60000 [===================>..........] - ETA: 29s - loss: 0.2297 - categorical_accuracy: 0.9294
41792/60000 [===================>..........] - ETA: 29s - loss: 0.2294 - categorical_accuracy: 0.9295
41824/60000 [===================>..........] - ETA: 29s - loss: 0.2293 - categorical_accuracy: 0.9295
41856/60000 [===================>..........] - ETA: 29s - loss: 0.2291 - categorical_accuracy: 0.9295
41888/60000 [===================>..........] - ETA: 29s - loss: 0.2290 - categorical_accuracy: 0.9296
41952/60000 [===================>..........] - ETA: 28s - loss: 0.2287 - categorical_accuracy: 0.9296
41984/60000 [===================>..........] - ETA: 28s - loss: 0.2285 - categorical_accuracy: 0.9297
42048/60000 [====================>.........] - ETA: 28s - loss: 0.2284 - categorical_accuracy: 0.9297
42112/60000 [====================>.........] - ETA: 28s - loss: 0.2282 - categorical_accuracy: 0.9298
42144/60000 [====================>.........] - ETA: 28s - loss: 0.2281 - categorical_accuracy: 0.9298
42176/60000 [====================>.........] - ETA: 28s - loss: 0.2280 - categorical_accuracy: 0.9299
42240/60000 [====================>.........] - ETA: 28s - loss: 0.2278 - categorical_accuracy: 0.9299
42304/60000 [====================>.........] - ETA: 28s - loss: 0.2276 - categorical_accuracy: 0.9300
42336/60000 [====================>.........] - ETA: 28s - loss: 0.2275 - categorical_accuracy: 0.9300
42368/60000 [====================>.........] - ETA: 28s - loss: 0.2273 - categorical_accuracy: 0.9301
42432/60000 [====================>.........] - ETA: 28s - loss: 0.2272 - categorical_accuracy: 0.9301
42464/60000 [====================>.........] - ETA: 28s - loss: 0.2271 - categorical_accuracy: 0.9301
42528/60000 [====================>.........] - ETA: 28s - loss: 0.2271 - categorical_accuracy: 0.9301
42592/60000 [====================>.........] - ETA: 27s - loss: 0.2268 - categorical_accuracy: 0.9302
42624/60000 [====================>.........] - ETA: 27s - loss: 0.2267 - categorical_accuracy: 0.9303
42688/60000 [====================>.........] - ETA: 27s - loss: 0.2264 - categorical_accuracy: 0.9304
42752/60000 [====================>.........] - ETA: 27s - loss: 0.2261 - categorical_accuracy: 0.9304
42784/60000 [====================>.........] - ETA: 27s - loss: 0.2260 - categorical_accuracy: 0.9304
42848/60000 [====================>.........] - ETA: 27s - loss: 0.2260 - categorical_accuracy: 0.9304
42912/60000 [====================>.........] - ETA: 27s - loss: 0.2257 - categorical_accuracy: 0.9305
42944/60000 [====================>.........] - ETA: 27s - loss: 0.2257 - categorical_accuracy: 0.9305
42976/60000 [====================>.........] - ETA: 27s - loss: 0.2258 - categorical_accuracy: 0.9305
43008/60000 [====================>.........] - ETA: 27s - loss: 0.2258 - categorical_accuracy: 0.9305
43072/60000 [====================>.........] - ETA: 27s - loss: 0.2256 - categorical_accuracy: 0.9306
43104/60000 [====================>.........] - ETA: 27s - loss: 0.2255 - categorical_accuracy: 0.9306
43136/60000 [====================>.........] - ETA: 27s - loss: 0.2255 - categorical_accuracy: 0.9306
43200/60000 [====================>.........] - ETA: 26s - loss: 0.2252 - categorical_accuracy: 0.9307
43232/60000 [====================>.........] - ETA: 26s - loss: 0.2251 - categorical_accuracy: 0.9307
43264/60000 [====================>.........] - ETA: 26s - loss: 0.2250 - categorical_accuracy: 0.9308
43296/60000 [====================>.........] - ETA: 26s - loss: 0.2248 - categorical_accuracy: 0.9308
43328/60000 [====================>.........] - ETA: 26s - loss: 0.2247 - categorical_accuracy: 0.9309
43360/60000 [====================>.........] - ETA: 26s - loss: 0.2248 - categorical_accuracy: 0.9309
43392/60000 [====================>.........] - ETA: 26s - loss: 0.2247 - categorical_accuracy: 0.9309
43424/60000 [====================>.........] - ETA: 26s - loss: 0.2247 - categorical_accuracy: 0.9309
43488/60000 [====================>.........] - ETA: 26s - loss: 0.2245 - categorical_accuracy: 0.9309
43520/60000 [====================>.........] - ETA: 26s - loss: 0.2245 - categorical_accuracy: 0.9310
43552/60000 [====================>.........] - ETA: 26s - loss: 0.2244 - categorical_accuracy: 0.9310
43616/60000 [====================>.........] - ETA: 26s - loss: 0.2244 - categorical_accuracy: 0.9310
43680/60000 [====================>.........] - ETA: 26s - loss: 0.2242 - categorical_accuracy: 0.9311
43712/60000 [====================>.........] - ETA: 26s - loss: 0.2241 - categorical_accuracy: 0.9311
43744/60000 [====================>.........] - ETA: 26s - loss: 0.2240 - categorical_accuracy: 0.9311
43776/60000 [====================>.........] - ETA: 26s - loss: 0.2239 - categorical_accuracy: 0.9312
43808/60000 [====================>.........] - ETA: 26s - loss: 0.2238 - categorical_accuracy: 0.9312
43840/60000 [====================>.........] - ETA: 25s - loss: 0.2238 - categorical_accuracy: 0.9312
43872/60000 [====================>.........] - ETA: 25s - loss: 0.2236 - categorical_accuracy: 0.9313
43904/60000 [====================>.........] - ETA: 25s - loss: 0.2237 - categorical_accuracy: 0.9313
43936/60000 [====================>.........] - ETA: 25s - loss: 0.2236 - categorical_accuracy: 0.9313
43968/60000 [====================>.........] - ETA: 25s - loss: 0.2235 - categorical_accuracy: 0.9313
44000/60000 [=====================>........] - ETA: 25s - loss: 0.2234 - categorical_accuracy: 0.9313
44032/60000 [=====================>........] - ETA: 25s - loss: 0.2233 - categorical_accuracy: 0.9313
44064/60000 [=====================>........] - ETA: 25s - loss: 0.2233 - categorical_accuracy: 0.9314
44096/60000 [=====================>........] - ETA: 25s - loss: 0.2231 - categorical_accuracy: 0.9314
44160/60000 [=====================>........] - ETA: 25s - loss: 0.2230 - categorical_accuracy: 0.9314
44192/60000 [=====================>........] - ETA: 25s - loss: 0.2229 - categorical_accuracy: 0.9314
44224/60000 [=====================>........] - ETA: 25s - loss: 0.2228 - categorical_accuracy: 0.9315
44256/60000 [=====================>........] - ETA: 25s - loss: 0.2227 - categorical_accuracy: 0.9315
44320/60000 [=====================>........] - ETA: 25s - loss: 0.2224 - categorical_accuracy: 0.9316
44352/60000 [=====================>........] - ETA: 25s - loss: 0.2225 - categorical_accuracy: 0.9316
44384/60000 [=====================>........] - ETA: 25s - loss: 0.2225 - categorical_accuracy: 0.9316
44416/60000 [=====================>........] - ETA: 25s - loss: 0.2225 - categorical_accuracy: 0.9316
44448/60000 [=====================>........] - ETA: 24s - loss: 0.2224 - categorical_accuracy: 0.9316
44480/60000 [=====================>........] - ETA: 24s - loss: 0.2223 - categorical_accuracy: 0.9316
44544/60000 [=====================>........] - ETA: 24s - loss: 0.2222 - categorical_accuracy: 0.9317
44576/60000 [=====================>........] - ETA: 24s - loss: 0.2220 - categorical_accuracy: 0.9317
44640/60000 [=====================>........] - ETA: 24s - loss: 0.2218 - categorical_accuracy: 0.9318
44704/60000 [=====================>........] - ETA: 24s - loss: 0.2215 - categorical_accuracy: 0.9319
44736/60000 [=====================>........] - ETA: 24s - loss: 0.2214 - categorical_accuracy: 0.9319
44800/60000 [=====================>........] - ETA: 24s - loss: 0.2212 - categorical_accuracy: 0.9320
44864/60000 [=====================>........] - ETA: 24s - loss: 0.2211 - categorical_accuracy: 0.9321
44896/60000 [=====================>........] - ETA: 24s - loss: 0.2210 - categorical_accuracy: 0.9321
44928/60000 [=====================>........] - ETA: 24s - loss: 0.2209 - categorical_accuracy: 0.9322
44992/60000 [=====================>........] - ETA: 24s - loss: 0.2208 - categorical_accuracy: 0.9322
45024/60000 [=====================>........] - ETA: 24s - loss: 0.2207 - categorical_accuracy: 0.9322
45056/60000 [=====================>........] - ETA: 24s - loss: 0.2207 - categorical_accuracy: 0.9322
45088/60000 [=====================>........] - ETA: 23s - loss: 0.2206 - categorical_accuracy: 0.9323
45152/60000 [=====================>........] - ETA: 23s - loss: 0.2205 - categorical_accuracy: 0.9323
45216/60000 [=====================>........] - ETA: 23s - loss: 0.2205 - categorical_accuracy: 0.9323
45280/60000 [=====================>........] - ETA: 23s - loss: 0.2204 - categorical_accuracy: 0.9324
45312/60000 [=====================>........] - ETA: 23s - loss: 0.2204 - categorical_accuracy: 0.9324
45344/60000 [=====================>........] - ETA: 23s - loss: 0.2205 - categorical_accuracy: 0.9324
45408/60000 [=====================>........] - ETA: 23s - loss: 0.2204 - categorical_accuracy: 0.9324
45440/60000 [=====================>........] - ETA: 23s - loss: 0.2203 - categorical_accuracy: 0.9324
45472/60000 [=====================>........] - ETA: 23s - loss: 0.2203 - categorical_accuracy: 0.9324
45536/60000 [=====================>........] - ETA: 23s - loss: 0.2201 - categorical_accuracy: 0.9324
45568/60000 [=====================>........] - ETA: 23s - loss: 0.2200 - categorical_accuracy: 0.9325
45600/60000 [=====================>........] - ETA: 23s - loss: 0.2199 - categorical_accuracy: 0.9325
45632/60000 [=====================>........] - ETA: 23s - loss: 0.2198 - categorical_accuracy: 0.9325
45664/60000 [=====================>........] - ETA: 23s - loss: 0.2197 - categorical_accuracy: 0.9326
45728/60000 [=====================>........] - ETA: 22s - loss: 0.2195 - categorical_accuracy: 0.9326
45792/60000 [=====================>........] - ETA: 22s - loss: 0.2193 - categorical_accuracy: 0.9327
45856/60000 [=====================>........] - ETA: 22s - loss: 0.2191 - categorical_accuracy: 0.9327
45920/60000 [=====================>........] - ETA: 22s - loss: 0.2190 - categorical_accuracy: 0.9328
45952/60000 [=====================>........] - ETA: 22s - loss: 0.2189 - categorical_accuracy: 0.9328
45984/60000 [=====================>........] - ETA: 22s - loss: 0.2187 - categorical_accuracy: 0.9329
46048/60000 [======================>.......] - ETA: 22s - loss: 0.2185 - categorical_accuracy: 0.9329
46112/60000 [======================>.......] - ETA: 22s - loss: 0.2183 - categorical_accuracy: 0.9330
46144/60000 [======================>.......] - ETA: 22s - loss: 0.2182 - categorical_accuracy: 0.9331
46176/60000 [======================>.......] - ETA: 22s - loss: 0.2181 - categorical_accuracy: 0.9331
46240/60000 [======================>.......] - ETA: 22s - loss: 0.2179 - categorical_accuracy: 0.9331
46272/60000 [======================>.......] - ETA: 22s - loss: 0.2178 - categorical_accuracy: 0.9332
46304/60000 [======================>.......] - ETA: 22s - loss: 0.2176 - categorical_accuracy: 0.9332
46368/60000 [======================>.......] - ETA: 21s - loss: 0.2175 - categorical_accuracy: 0.9333
46432/60000 [======================>.......] - ETA: 21s - loss: 0.2173 - categorical_accuracy: 0.9333
46496/60000 [======================>.......] - ETA: 21s - loss: 0.2171 - categorical_accuracy: 0.9334
46528/60000 [======================>.......] - ETA: 21s - loss: 0.2170 - categorical_accuracy: 0.9335
46560/60000 [======================>.......] - ETA: 21s - loss: 0.2169 - categorical_accuracy: 0.9335
46592/60000 [======================>.......] - ETA: 21s - loss: 0.2169 - categorical_accuracy: 0.9334
46624/60000 [======================>.......] - ETA: 21s - loss: 0.2168 - categorical_accuracy: 0.9334
46656/60000 [======================>.......] - ETA: 21s - loss: 0.2167 - categorical_accuracy: 0.9335
46688/60000 [======================>.......] - ETA: 21s - loss: 0.2166 - categorical_accuracy: 0.9335
46720/60000 [======================>.......] - ETA: 21s - loss: 0.2165 - categorical_accuracy: 0.9336
46752/60000 [======================>.......] - ETA: 21s - loss: 0.2164 - categorical_accuracy: 0.9336
46784/60000 [======================>.......] - ETA: 21s - loss: 0.2164 - categorical_accuracy: 0.9336
46816/60000 [======================>.......] - ETA: 21s - loss: 0.2165 - categorical_accuracy: 0.9335
46848/60000 [======================>.......] - ETA: 21s - loss: 0.2165 - categorical_accuracy: 0.9335
46880/60000 [======================>.......] - ETA: 21s - loss: 0.2166 - categorical_accuracy: 0.9335
46912/60000 [======================>.......] - ETA: 21s - loss: 0.2165 - categorical_accuracy: 0.9335
46944/60000 [======================>.......] - ETA: 20s - loss: 0.2164 - categorical_accuracy: 0.9335
46976/60000 [======================>.......] - ETA: 20s - loss: 0.2164 - categorical_accuracy: 0.9335
47040/60000 [======================>.......] - ETA: 20s - loss: 0.2162 - categorical_accuracy: 0.9336
47072/60000 [======================>.......] - ETA: 20s - loss: 0.2162 - categorical_accuracy: 0.9336
47104/60000 [======================>.......] - ETA: 20s - loss: 0.2161 - categorical_accuracy: 0.9336
47136/60000 [======================>.......] - ETA: 20s - loss: 0.2160 - categorical_accuracy: 0.9336
47168/60000 [======================>.......] - ETA: 20s - loss: 0.2159 - categorical_accuracy: 0.9337
47200/60000 [======================>.......] - ETA: 20s - loss: 0.2158 - categorical_accuracy: 0.9337
47264/60000 [======================>.......] - ETA: 20s - loss: 0.2156 - categorical_accuracy: 0.9338
47296/60000 [======================>.......] - ETA: 20s - loss: 0.2155 - categorical_accuracy: 0.9338
47360/60000 [======================>.......] - ETA: 20s - loss: 0.2154 - categorical_accuracy: 0.9339
47392/60000 [======================>.......] - ETA: 20s - loss: 0.2153 - categorical_accuracy: 0.9339
47424/60000 [======================>.......] - ETA: 20s - loss: 0.2152 - categorical_accuracy: 0.9339
47456/60000 [======================>.......] - ETA: 20s - loss: 0.2152 - categorical_accuracy: 0.9339
47520/60000 [======================>.......] - ETA: 20s - loss: 0.2150 - categorical_accuracy: 0.9340
47552/60000 [======================>.......] - ETA: 19s - loss: 0.2150 - categorical_accuracy: 0.9339
47584/60000 [======================>.......] - ETA: 19s - loss: 0.2149 - categorical_accuracy: 0.9339
47648/60000 [======================>.......] - ETA: 19s - loss: 0.2147 - categorical_accuracy: 0.9340
47712/60000 [======================>.......] - ETA: 19s - loss: 0.2146 - categorical_accuracy: 0.9340
47744/60000 [======================>.......] - ETA: 19s - loss: 0.2146 - categorical_accuracy: 0.9340
47776/60000 [======================>.......] - ETA: 19s - loss: 0.2145 - categorical_accuracy: 0.9341
47808/60000 [======================>.......] - ETA: 19s - loss: 0.2145 - categorical_accuracy: 0.9341
47840/60000 [======================>.......] - ETA: 19s - loss: 0.2144 - categorical_accuracy: 0.9341
47872/60000 [======================>.......] - ETA: 19s - loss: 0.2143 - categorical_accuracy: 0.9341
47936/60000 [======================>.......] - ETA: 19s - loss: 0.2141 - categorical_accuracy: 0.9342
48000/60000 [=======================>......] - ETA: 19s - loss: 0.2138 - categorical_accuracy: 0.9343
48032/60000 [=======================>......] - ETA: 19s - loss: 0.2137 - categorical_accuracy: 0.9343
48064/60000 [=======================>......] - ETA: 19s - loss: 0.2138 - categorical_accuracy: 0.9343
48128/60000 [=======================>......] - ETA: 19s - loss: 0.2136 - categorical_accuracy: 0.9344
48160/60000 [=======================>......] - ETA: 19s - loss: 0.2135 - categorical_accuracy: 0.9344
48224/60000 [=======================>......] - ETA: 18s - loss: 0.2134 - categorical_accuracy: 0.9344
48288/60000 [=======================>......] - ETA: 18s - loss: 0.2135 - categorical_accuracy: 0.9345
48320/60000 [=======================>......] - ETA: 18s - loss: 0.2133 - categorical_accuracy: 0.9345
48352/60000 [=======================>......] - ETA: 18s - loss: 0.2133 - categorical_accuracy: 0.9345
48416/60000 [=======================>......] - ETA: 18s - loss: 0.2130 - categorical_accuracy: 0.9346
48448/60000 [=======================>......] - ETA: 18s - loss: 0.2129 - categorical_accuracy: 0.9346
48480/60000 [=======================>......] - ETA: 18s - loss: 0.2129 - categorical_accuracy: 0.9346
48544/60000 [=======================>......] - ETA: 18s - loss: 0.2129 - categorical_accuracy: 0.9346
48576/60000 [=======================>......] - ETA: 18s - loss: 0.2127 - categorical_accuracy: 0.9346
48608/60000 [=======================>......] - ETA: 18s - loss: 0.2126 - categorical_accuracy: 0.9347
48640/60000 [=======================>......] - ETA: 18s - loss: 0.2125 - categorical_accuracy: 0.9347
48672/60000 [=======================>......] - ETA: 18s - loss: 0.2125 - categorical_accuracy: 0.9347
48704/60000 [=======================>......] - ETA: 18s - loss: 0.2127 - categorical_accuracy: 0.9347
48736/60000 [=======================>......] - ETA: 18s - loss: 0.2126 - categorical_accuracy: 0.9347
48768/60000 [=======================>......] - ETA: 18s - loss: 0.2126 - categorical_accuracy: 0.9347
48800/60000 [=======================>......] - ETA: 17s - loss: 0.2126 - categorical_accuracy: 0.9347
48832/60000 [=======================>......] - ETA: 17s - loss: 0.2125 - categorical_accuracy: 0.9347
48864/60000 [=======================>......] - ETA: 17s - loss: 0.2125 - categorical_accuracy: 0.9347
48896/60000 [=======================>......] - ETA: 17s - loss: 0.2125 - categorical_accuracy: 0.9347
48928/60000 [=======================>......] - ETA: 17s - loss: 0.2124 - categorical_accuracy: 0.9348
48960/60000 [=======================>......] - ETA: 17s - loss: 0.2123 - categorical_accuracy: 0.9348
48992/60000 [=======================>......] - ETA: 17s - loss: 0.2121 - categorical_accuracy: 0.9349
49024/60000 [=======================>......] - ETA: 17s - loss: 0.2122 - categorical_accuracy: 0.9349
49056/60000 [=======================>......] - ETA: 17s - loss: 0.2121 - categorical_accuracy: 0.9349
49088/60000 [=======================>......] - ETA: 17s - loss: 0.2120 - categorical_accuracy: 0.9350
49120/60000 [=======================>......] - ETA: 17s - loss: 0.2119 - categorical_accuracy: 0.9350
49152/60000 [=======================>......] - ETA: 17s - loss: 0.2117 - categorical_accuracy: 0.9350
49216/60000 [=======================>......] - ETA: 17s - loss: 0.2117 - categorical_accuracy: 0.9351
49248/60000 [=======================>......] - ETA: 17s - loss: 0.2116 - categorical_accuracy: 0.9351
49312/60000 [=======================>......] - ETA: 17s - loss: 0.2114 - categorical_accuracy: 0.9351
49376/60000 [=======================>......] - ETA: 17s - loss: 0.2112 - categorical_accuracy: 0.9352
49408/60000 [=======================>......] - ETA: 17s - loss: 0.2111 - categorical_accuracy: 0.9352
49440/60000 [=======================>......] - ETA: 16s - loss: 0.2110 - categorical_accuracy: 0.9353
49472/60000 [=======================>......] - ETA: 16s - loss: 0.2109 - categorical_accuracy: 0.9353
49504/60000 [=======================>......] - ETA: 16s - loss: 0.2108 - categorical_accuracy: 0.9353
49536/60000 [=======================>......] - ETA: 16s - loss: 0.2108 - categorical_accuracy: 0.9353
49568/60000 [=======================>......] - ETA: 16s - loss: 0.2107 - categorical_accuracy: 0.9354
49600/60000 [=======================>......] - ETA: 16s - loss: 0.2106 - categorical_accuracy: 0.9354
49632/60000 [=======================>......] - ETA: 16s - loss: 0.2105 - categorical_accuracy: 0.9354
49664/60000 [=======================>......] - ETA: 16s - loss: 0.2104 - categorical_accuracy: 0.9354
49696/60000 [=======================>......] - ETA: 16s - loss: 0.2103 - categorical_accuracy: 0.9355
49728/60000 [=======================>......] - ETA: 16s - loss: 0.2102 - categorical_accuracy: 0.9355
49760/60000 [=======================>......] - ETA: 16s - loss: 0.2102 - categorical_accuracy: 0.9355
49824/60000 [=======================>......] - ETA: 16s - loss: 0.2102 - categorical_accuracy: 0.9356
49888/60000 [=======================>......] - ETA: 16s - loss: 0.2100 - categorical_accuracy: 0.9356
49920/60000 [=======================>......] - ETA: 16s - loss: 0.2100 - categorical_accuracy: 0.9356
49952/60000 [=======================>......] - ETA: 16s - loss: 0.2099 - categorical_accuracy: 0.9356
50016/60000 [========================>.....] - ETA: 16s - loss: 0.2098 - categorical_accuracy: 0.9357
50048/60000 [========================>.....] - ETA: 15s - loss: 0.2097 - categorical_accuracy: 0.9357
50112/60000 [========================>.....] - ETA: 15s - loss: 0.2097 - categorical_accuracy: 0.9357
50144/60000 [========================>.....] - ETA: 15s - loss: 0.2096 - categorical_accuracy: 0.9357
50176/60000 [========================>.....] - ETA: 15s - loss: 0.2095 - categorical_accuracy: 0.9357
50208/60000 [========================>.....] - ETA: 15s - loss: 0.2094 - categorical_accuracy: 0.9358
50240/60000 [========================>.....] - ETA: 15s - loss: 0.2094 - categorical_accuracy: 0.9358
50304/60000 [========================>.....] - ETA: 15s - loss: 0.2095 - categorical_accuracy: 0.9358
50336/60000 [========================>.....] - ETA: 15s - loss: 0.2094 - categorical_accuracy: 0.9358
50368/60000 [========================>.....] - ETA: 15s - loss: 0.2094 - categorical_accuracy: 0.9358
50432/60000 [========================>.....] - ETA: 15s - loss: 0.2092 - categorical_accuracy: 0.9359
50496/60000 [========================>.....] - ETA: 15s - loss: 0.2092 - categorical_accuracy: 0.9359
50560/60000 [========================>.....] - ETA: 15s - loss: 0.2090 - categorical_accuracy: 0.9359
50592/60000 [========================>.....] - ETA: 15s - loss: 0.2089 - categorical_accuracy: 0.9359
50656/60000 [========================>.....] - ETA: 15s - loss: 0.2091 - categorical_accuracy: 0.9359
50688/60000 [========================>.....] - ETA: 14s - loss: 0.2090 - categorical_accuracy: 0.9359
50720/60000 [========================>.....] - ETA: 14s - loss: 0.2089 - categorical_accuracy: 0.9360
50752/60000 [========================>.....] - ETA: 14s - loss: 0.2090 - categorical_accuracy: 0.9359
50784/60000 [========================>.....] - ETA: 14s - loss: 0.2089 - categorical_accuracy: 0.9359
50848/60000 [========================>.....] - ETA: 14s - loss: 0.2088 - categorical_accuracy: 0.9360
50880/60000 [========================>.....] - ETA: 14s - loss: 0.2087 - categorical_accuracy: 0.9360
50912/60000 [========================>.....] - ETA: 14s - loss: 0.2086 - categorical_accuracy: 0.9360
50976/60000 [========================>.....] - ETA: 14s - loss: 0.2086 - categorical_accuracy: 0.9361
51008/60000 [========================>.....] - ETA: 14s - loss: 0.2084 - categorical_accuracy: 0.9361
51072/60000 [========================>.....] - ETA: 14s - loss: 0.2082 - categorical_accuracy: 0.9362
51136/60000 [========================>.....] - ETA: 14s - loss: 0.2080 - categorical_accuracy: 0.9363
51168/60000 [========================>.....] - ETA: 14s - loss: 0.2079 - categorical_accuracy: 0.9363
51232/60000 [========================>.....] - ETA: 14s - loss: 0.2078 - categorical_accuracy: 0.9364
51264/60000 [========================>.....] - ETA: 14s - loss: 0.2077 - categorical_accuracy: 0.9364
51328/60000 [========================>.....] - ETA: 13s - loss: 0.2074 - categorical_accuracy: 0.9365
51360/60000 [========================>.....] - ETA: 13s - loss: 0.2074 - categorical_accuracy: 0.9365
51392/60000 [========================>.....] - ETA: 13s - loss: 0.2074 - categorical_accuracy: 0.9365
51456/60000 [========================>.....] - ETA: 13s - loss: 0.2074 - categorical_accuracy: 0.9365
51520/60000 [========================>.....] - ETA: 13s - loss: 0.2072 - categorical_accuracy: 0.9366
51552/60000 [========================>.....] - ETA: 13s - loss: 0.2071 - categorical_accuracy: 0.9366
51584/60000 [========================>.....] - ETA: 13s - loss: 0.2070 - categorical_accuracy: 0.9366
51616/60000 [========================>.....] - ETA: 13s - loss: 0.2069 - categorical_accuracy: 0.9367
51648/60000 [========================>.....] - ETA: 13s - loss: 0.2070 - categorical_accuracy: 0.9367
51680/60000 [========================>.....] - ETA: 13s - loss: 0.2069 - categorical_accuracy: 0.9367
51712/60000 [========================>.....] - ETA: 13s - loss: 0.2068 - categorical_accuracy: 0.9367
51776/60000 [========================>.....] - ETA: 13s - loss: 0.2067 - categorical_accuracy: 0.9367
51840/60000 [========================>.....] - ETA: 13s - loss: 0.2066 - categorical_accuracy: 0.9368
51872/60000 [========================>.....] - ETA: 13s - loss: 0.2065 - categorical_accuracy: 0.9368
51904/60000 [========================>.....] - ETA: 13s - loss: 0.2063 - categorical_accuracy: 0.9368
51936/60000 [========================>.....] - ETA: 12s - loss: 0.2062 - categorical_accuracy: 0.9369
52000/60000 [=========================>....] - ETA: 12s - loss: 0.2063 - categorical_accuracy: 0.9369
52032/60000 [=========================>....] - ETA: 12s - loss: 0.2062 - categorical_accuracy: 0.9369
52064/60000 [=========================>....] - ETA: 12s - loss: 0.2061 - categorical_accuracy: 0.9370
52128/60000 [=========================>....] - ETA: 12s - loss: 0.2059 - categorical_accuracy: 0.9370
52192/60000 [=========================>....] - ETA: 12s - loss: 0.2057 - categorical_accuracy: 0.9371
52224/60000 [=========================>....] - ETA: 12s - loss: 0.2058 - categorical_accuracy: 0.9371
52256/60000 [=========================>....] - ETA: 12s - loss: 0.2057 - categorical_accuracy: 0.9371
52288/60000 [=========================>....] - ETA: 12s - loss: 0.2057 - categorical_accuracy: 0.9371
52352/60000 [=========================>....] - ETA: 12s - loss: 0.2054 - categorical_accuracy: 0.9372
52416/60000 [=========================>....] - ETA: 12s - loss: 0.2053 - categorical_accuracy: 0.9372
52480/60000 [=========================>....] - ETA: 12s - loss: 0.2052 - categorical_accuracy: 0.9372
52544/60000 [=========================>....] - ETA: 11s - loss: 0.2051 - categorical_accuracy: 0.9372
52608/60000 [=========================>....] - ETA: 11s - loss: 0.2050 - categorical_accuracy: 0.9372
52672/60000 [=========================>....] - ETA: 11s - loss: 0.2049 - categorical_accuracy: 0.9373
52704/60000 [=========================>....] - ETA: 11s - loss: 0.2049 - categorical_accuracy: 0.9373
52736/60000 [=========================>....] - ETA: 11s - loss: 0.2051 - categorical_accuracy: 0.9373
52768/60000 [=========================>....] - ETA: 11s - loss: 0.2051 - categorical_accuracy: 0.9373
52832/60000 [=========================>....] - ETA: 11s - loss: 0.2049 - categorical_accuracy: 0.9373
52864/60000 [=========================>....] - ETA: 11s - loss: 0.2048 - categorical_accuracy: 0.9373
52896/60000 [=========================>....] - ETA: 11s - loss: 0.2047 - categorical_accuracy: 0.9374
52928/60000 [=========================>....] - ETA: 11s - loss: 0.2046 - categorical_accuracy: 0.9374
52960/60000 [=========================>....] - ETA: 11s - loss: 0.2046 - categorical_accuracy: 0.9374
52992/60000 [=========================>....] - ETA: 11s - loss: 0.2045 - categorical_accuracy: 0.9375
53024/60000 [=========================>....] - ETA: 11s - loss: 0.2046 - categorical_accuracy: 0.9374
53056/60000 [=========================>....] - ETA: 11s - loss: 0.2046 - categorical_accuracy: 0.9374
53088/60000 [=========================>....] - ETA: 11s - loss: 0.2045 - categorical_accuracy: 0.9374
53152/60000 [=========================>....] - ETA: 10s - loss: 0.2043 - categorical_accuracy: 0.9375
53184/60000 [=========================>....] - ETA: 10s - loss: 0.2042 - categorical_accuracy: 0.9375
53216/60000 [=========================>....] - ETA: 10s - loss: 0.2041 - categorical_accuracy: 0.9375
53248/60000 [=========================>....] - ETA: 10s - loss: 0.2040 - categorical_accuracy: 0.9376
53280/60000 [=========================>....] - ETA: 10s - loss: 0.2039 - categorical_accuracy: 0.9376
53312/60000 [=========================>....] - ETA: 10s - loss: 0.2038 - categorical_accuracy: 0.9377
53344/60000 [=========================>....] - ETA: 10s - loss: 0.2038 - categorical_accuracy: 0.9377
53376/60000 [=========================>....] - ETA: 10s - loss: 0.2037 - categorical_accuracy: 0.9377
53408/60000 [=========================>....] - ETA: 10s - loss: 0.2036 - categorical_accuracy: 0.9377
53472/60000 [=========================>....] - ETA: 10s - loss: 0.2035 - categorical_accuracy: 0.9377
53504/60000 [=========================>....] - ETA: 10s - loss: 0.2034 - categorical_accuracy: 0.9378
53568/60000 [=========================>....] - ETA: 10s - loss: 0.2032 - categorical_accuracy: 0.9378
53600/60000 [=========================>....] - ETA: 10s - loss: 0.2032 - categorical_accuracy: 0.9379
53632/60000 [=========================>....] - ETA: 10s - loss: 0.2032 - categorical_accuracy: 0.9379
53664/60000 [=========================>....] - ETA: 10s - loss: 0.2031 - categorical_accuracy: 0.9379
53696/60000 [=========================>....] - ETA: 10s - loss: 0.2030 - categorical_accuracy: 0.9379
53728/60000 [=========================>....] - ETA: 10s - loss: 0.2030 - categorical_accuracy: 0.9379
53760/60000 [=========================>....] - ETA: 10s - loss: 0.2029 - categorical_accuracy: 0.9379
53792/60000 [=========================>....] - ETA: 9s - loss: 0.2028 - categorical_accuracy: 0.9379 
53824/60000 [=========================>....] - ETA: 9s - loss: 0.2027 - categorical_accuracy: 0.9380
53856/60000 [=========================>....] - ETA: 9s - loss: 0.2026 - categorical_accuracy: 0.9380
53888/60000 [=========================>....] - ETA: 9s - loss: 0.2025 - categorical_accuracy: 0.9380
53920/60000 [=========================>....] - ETA: 9s - loss: 0.2025 - categorical_accuracy: 0.9381
53984/60000 [=========================>....] - ETA: 9s - loss: 0.2022 - categorical_accuracy: 0.9381
54016/60000 [==========================>...] - ETA: 9s - loss: 0.2021 - categorical_accuracy: 0.9381
54048/60000 [==========================>...] - ETA: 9s - loss: 0.2021 - categorical_accuracy: 0.9381
54080/60000 [==========================>...] - ETA: 9s - loss: 0.2021 - categorical_accuracy: 0.9381
54112/60000 [==========================>...] - ETA: 9s - loss: 0.2022 - categorical_accuracy: 0.9381
54176/60000 [==========================>...] - ETA: 9s - loss: 0.2022 - categorical_accuracy: 0.9381
54208/60000 [==========================>...] - ETA: 9s - loss: 0.2022 - categorical_accuracy: 0.9381
54272/60000 [==========================>...] - ETA: 9s - loss: 0.2021 - categorical_accuracy: 0.9382
54336/60000 [==========================>...] - ETA: 9s - loss: 0.2020 - categorical_accuracy: 0.9382
54400/60000 [==========================>...] - ETA: 8s - loss: 0.2018 - categorical_accuracy: 0.9382
54464/60000 [==========================>...] - ETA: 8s - loss: 0.2017 - categorical_accuracy: 0.9382
54496/60000 [==========================>...] - ETA: 8s - loss: 0.2017 - categorical_accuracy: 0.9382
54528/60000 [==========================>...] - ETA: 8s - loss: 0.2016 - categorical_accuracy: 0.9383
54560/60000 [==========================>...] - ETA: 8s - loss: 0.2016 - categorical_accuracy: 0.9383
54624/60000 [==========================>...] - ETA: 8s - loss: 0.2016 - categorical_accuracy: 0.9383
54656/60000 [==========================>...] - ETA: 8s - loss: 0.2016 - categorical_accuracy: 0.9383
54688/60000 [==========================>...] - ETA: 8s - loss: 0.2015 - categorical_accuracy: 0.9383
54752/60000 [==========================>...] - ETA: 8s - loss: 0.2013 - categorical_accuracy: 0.9384
54816/60000 [==========================>...] - ETA: 8s - loss: 0.2012 - categorical_accuracy: 0.9384
54848/60000 [==========================>...] - ETA: 8s - loss: 0.2011 - categorical_accuracy: 0.9384
54880/60000 [==========================>...] - ETA: 8s - loss: 0.2011 - categorical_accuracy: 0.9384
54912/60000 [==========================>...] - ETA: 8s - loss: 0.2010 - categorical_accuracy: 0.9384
54976/60000 [==========================>...] - ETA: 8s - loss: 0.2008 - categorical_accuracy: 0.9385
55040/60000 [==========================>...] - ETA: 7s - loss: 0.2007 - categorical_accuracy: 0.9385
55104/60000 [==========================>...] - ETA: 7s - loss: 0.2006 - categorical_accuracy: 0.9385
55168/60000 [==========================>...] - ETA: 7s - loss: 0.2005 - categorical_accuracy: 0.9385
55200/60000 [==========================>...] - ETA: 7s - loss: 0.2004 - categorical_accuracy: 0.9386
55232/60000 [==========================>...] - ETA: 7s - loss: 0.2004 - categorical_accuracy: 0.9386
55264/60000 [==========================>...] - ETA: 7s - loss: 0.2003 - categorical_accuracy: 0.9386
55296/60000 [==========================>...] - ETA: 7s - loss: 0.2002 - categorical_accuracy: 0.9386
55360/60000 [==========================>...] - ETA: 7s - loss: 0.2003 - categorical_accuracy: 0.9386
55424/60000 [==========================>...] - ETA: 7s - loss: 0.2003 - categorical_accuracy: 0.9387
55456/60000 [==========================>...] - ETA: 7s - loss: 0.2002 - categorical_accuracy: 0.9387
55488/60000 [==========================>...] - ETA: 7s - loss: 0.2001 - categorical_accuracy: 0.9387
55520/60000 [==========================>...] - ETA: 7s - loss: 0.2000 - categorical_accuracy: 0.9388
55552/60000 [==========================>...] - ETA: 7s - loss: 0.1999 - categorical_accuracy: 0.9388
55616/60000 [==========================>...] - ETA: 7s - loss: 0.1997 - categorical_accuracy: 0.9388
55648/60000 [==========================>...] - ETA: 6s - loss: 0.1997 - categorical_accuracy: 0.9388
55680/60000 [==========================>...] - ETA: 6s - loss: 0.1996 - categorical_accuracy: 0.9389
55712/60000 [==========================>...] - ETA: 6s - loss: 0.1995 - categorical_accuracy: 0.9389
55744/60000 [==========================>...] - ETA: 6s - loss: 0.1994 - categorical_accuracy: 0.9389
55776/60000 [==========================>...] - ETA: 6s - loss: 0.1994 - categorical_accuracy: 0.9389
55808/60000 [==========================>...] - ETA: 6s - loss: 0.1993 - categorical_accuracy: 0.9389
55840/60000 [==========================>...] - ETA: 6s - loss: 0.1992 - categorical_accuracy: 0.9390
55904/60000 [==========================>...] - ETA: 6s - loss: 0.1992 - categorical_accuracy: 0.9389
55936/60000 [==========================>...] - ETA: 6s - loss: 0.1992 - categorical_accuracy: 0.9389
55968/60000 [==========================>...] - ETA: 6s - loss: 0.1991 - categorical_accuracy: 0.9390
56000/60000 [===========================>..] - ETA: 6s - loss: 0.1990 - categorical_accuracy: 0.9390
56032/60000 [===========================>..] - ETA: 6s - loss: 0.1990 - categorical_accuracy: 0.9390
56096/60000 [===========================>..] - ETA: 6s - loss: 0.1988 - categorical_accuracy: 0.9391
56128/60000 [===========================>..] - ETA: 6s - loss: 0.1987 - categorical_accuracy: 0.9391
56192/60000 [===========================>..] - ETA: 6s - loss: 0.1987 - categorical_accuracy: 0.9391
56224/60000 [===========================>..] - ETA: 6s - loss: 0.1986 - categorical_accuracy: 0.9391
56256/60000 [===========================>..] - ETA: 6s - loss: 0.1985 - categorical_accuracy: 0.9392
56288/60000 [===========================>..] - ETA: 5s - loss: 0.1985 - categorical_accuracy: 0.9392
56320/60000 [===========================>..] - ETA: 5s - loss: 0.1984 - categorical_accuracy: 0.9392
56384/60000 [===========================>..] - ETA: 5s - loss: 0.1982 - categorical_accuracy: 0.9393
56416/60000 [===========================>..] - ETA: 5s - loss: 0.1981 - categorical_accuracy: 0.9393
56480/60000 [===========================>..] - ETA: 5s - loss: 0.1979 - categorical_accuracy: 0.9394
56544/60000 [===========================>..] - ETA: 5s - loss: 0.1979 - categorical_accuracy: 0.9394
56576/60000 [===========================>..] - ETA: 5s - loss: 0.1979 - categorical_accuracy: 0.9394
56608/60000 [===========================>..] - ETA: 5s - loss: 0.1978 - categorical_accuracy: 0.9394
56640/60000 [===========================>..] - ETA: 5s - loss: 0.1978 - categorical_accuracy: 0.9394
56704/60000 [===========================>..] - ETA: 5s - loss: 0.1977 - categorical_accuracy: 0.9395
56736/60000 [===========================>..] - ETA: 5s - loss: 0.1977 - categorical_accuracy: 0.9395
56800/60000 [===========================>..] - ETA: 5s - loss: 0.1975 - categorical_accuracy: 0.9395
56864/60000 [===========================>..] - ETA: 5s - loss: 0.1975 - categorical_accuracy: 0.9395
56896/60000 [===========================>..] - ETA: 4s - loss: 0.1974 - categorical_accuracy: 0.9396
56928/60000 [===========================>..] - ETA: 4s - loss: 0.1973 - categorical_accuracy: 0.9396
56960/60000 [===========================>..] - ETA: 4s - loss: 0.1972 - categorical_accuracy: 0.9396
56992/60000 [===========================>..] - ETA: 4s - loss: 0.1971 - categorical_accuracy: 0.9396
57024/60000 [===========================>..] - ETA: 4s - loss: 0.1971 - categorical_accuracy: 0.9397
57056/60000 [===========================>..] - ETA: 4s - loss: 0.1970 - categorical_accuracy: 0.9397
57088/60000 [===========================>..] - ETA: 4s - loss: 0.1969 - categorical_accuracy: 0.9397
57152/60000 [===========================>..] - ETA: 4s - loss: 0.1967 - categorical_accuracy: 0.9398
57184/60000 [===========================>..] - ETA: 4s - loss: 0.1967 - categorical_accuracy: 0.9398
57248/60000 [===========================>..] - ETA: 4s - loss: 0.1967 - categorical_accuracy: 0.9398
57312/60000 [===========================>..] - ETA: 4s - loss: 0.1965 - categorical_accuracy: 0.9398
57344/60000 [===========================>..] - ETA: 4s - loss: 0.1964 - categorical_accuracy: 0.9399
57376/60000 [===========================>..] - ETA: 4s - loss: 0.1963 - categorical_accuracy: 0.9399
57408/60000 [===========================>..] - ETA: 4s - loss: 0.1963 - categorical_accuracy: 0.9399
57472/60000 [===========================>..] - ETA: 4s - loss: 0.1963 - categorical_accuracy: 0.9399
57504/60000 [===========================>..] - ETA: 4s - loss: 0.1962 - categorical_accuracy: 0.9400
57568/60000 [===========================>..] - ETA: 3s - loss: 0.1961 - categorical_accuracy: 0.9400
57600/60000 [===========================>..] - ETA: 3s - loss: 0.1960 - categorical_accuracy: 0.9400
57632/60000 [===========================>..] - ETA: 3s - loss: 0.1959 - categorical_accuracy: 0.9401
57696/60000 [===========================>..] - ETA: 3s - loss: 0.1957 - categorical_accuracy: 0.9401
57728/60000 [===========================>..] - ETA: 3s - loss: 0.1957 - categorical_accuracy: 0.9401
57760/60000 [===========================>..] - ETA: 3s - loss: 0.1956 - categorical_accuracy: 0.9401
57792/60000 [===========================>..] - ETA: 3s - loss: 0.1956 - categorical_accuracy: 0.9401
57824/60000 [===========================>..] - ETA: 3s - loss: 0.1955 - categorical_accuracy: 0.9401
57888/60000 [===========================>..] - ETA: 3s - loss: 0.1954 - categorical_accuracy: 0.9402
57920/60000 [===========================>..] - ETA: 3s - loss: 0.1953 - categorical_accuracy: 0.9402
57952/60000 [===========================>..] - ETA: 3s - loss: 0.1952 - categorical_accuracy: 0.9402
57984/60000 [===========================>..] - ETA: 3s - loss: 0.1951 - categorical_accuracy: 0.9403
58016/60000 [============================>.] - ETA: 3s - loss: 0.1950 - categorical_accuracy: 0.9403
58048/60000 [============================>.] - ETA: 3s - loss: 0.1949 - categorical_accuracy: 0.9403
58080/60000 [============================>.] - ETA: 3s - loss: 0.1949 - categorical_accuracy: 0.9403
58112/60000 [============================>.] - ETA: 3s - loss: 0.1948 - categorical_accuracy: 0.9404
58144/60000 [============================>.] - ETA: 2s - loss: 0.1947 - categorical_accuracy: 0.9404
58208/60000 [============================>.] - ETA: 2s - loss: 0.1948 - categorical_accuracy: 0.9404
58272/60000 [============================>.] - ETA: 2s - loss: 0.1947 - categorical_accuracy: 0.9404
58304/60000 [============================>.] - ETA: 2s - loss: 0.1946 - categorical_accuracy: 0.9405
58336/60000 [============================>.] - ETA: 2s - loss: 0.1946 - categorical_accuracy: 0.9405
58368/60000 [============================>.] - ETA: 2s - loss: 0.1946 - categorical_accuracy: 0.9405
58400/60000 [============================>.] - ETA: 2s - loss: 0.1946 - categorical_accuracy: 0.9405
58464/60000 [============================>.] - ETA: 2s - loss: 0.1944 - categorical_accuracy: 0.9405
58496/60000 [============================>.] - ETA: 2s - loss: 0.1944 - categorical_accuracy: 0.9405
58560/60000 [============================>.] - ETA: 2s - loss: 0.1942 - categorical_accuracy: 0.9406
58624/60000 [============================>.] - ETA: 2s - loss: 0.1941 - categorical_accuracy: 0.9406
58688/60000 [============================>.] - ETA: 2s - loss: 0.1940 - categorical_accuracy: 0.9406
58752/60000 [============================>.] - ETA: 2s - loss: 0.1939 - categorical_accuracy: 0.9407
58816/60000 [============================>.] - ETA: 1s - loss: 0.1940 - categorical_accuracy: 0.9407
58880/60000 [============================>.] - ETA: 1s - loss: 0.1938 - categorical_accuracy: 0.9408
58912/60000 [============================>.] - ETA: 1s - loss: 0.1940 - categorical_accuracy: 0.9407
58944/60000 [============================>.] - ETA: 1s - loss: 0.1940 - categorical_accuracy: 0.9407
58976/60000 [============================>.] - ETA: 1s - loss: 0.1939 - categorical_accuracy: 0.9408
59040/60000 [============================>.] - ETA: 1s - loss: 0.1939 - categorical_accuracy: 0.9408
59104/60000 [============================>.] - ETA: 1s - loss: 0.1938 - categorical_accuracy: 0.9408
59136/60000 [============================>.] - ETA: 1s - loss: 0.1938 - categorical_accuracy: 0.9408
59168/60000 [============================>.] - ETA: 1s - loss: 0.1938 - categorical_accuracy: 0.9407
59232/60000 [============================>.] - ETA: 1s - loss: 0.1936 - categorical_accuracy: 0.9408
59264/60000 [============================>.] - ETA: 1s - loss: 0.1936 - categorical_accuracy: 0.9408
59296/60000 [============================>.] - ETA: 1s - loss: 0.1935 - categorical_accuracy: 0.9408
59328/60000 [============================>.] - ETA: 1s - loss: 0.1935 - categorical_accuracy: 0.9409
59360/60000 [============================>.] - ETA: 1s - loss: 0.1935 - categorical_accuracy: 0.9409
59392/60000 [============================>.] - ETA: 0s - loss: 0.1934 - categorical_accuracy: 0.9409
59424/60000 [============================>.] - ETA: 0s - loss: 0.1933 - categorical_accuracy: 0.9409
59488/60000 [============================>.] - ETA: 0s - loss: 0.1932 - categorical_accuracy: 0.9409
59520/60000 [============================>.] - ETA: 0s - loss: 0.1931 - categorical_accuracy: 0.9409
59584/60000 [============================>.] - ETA: 0s - loss: 0.1931 - categorical_accuracy: 0.9410
59648/60000 [============================>.] - ETA: 0s - loss: 0.1930 - categorical_accuracy: 0.9410
59712/60000 [============================>.] - ETA: 0s - loss: 0.1930 - categorical_accuracy: 0.9410
59744/60000 [============================>.] - ETA: 0s - loss: 0.1929 - categorical_accuracy: 0.9410
59776/60000 [============================>.] - ETA: 0s - loss: 0.1929 - categorical_accuracy: 0.9410
59840/60000 [============================>.] - ETA: 0s - loss: 0.1929 - categorical_accuracy: 0.9410
59904/60000 [============================>.] - ETA: 0s - loss: 0.1927 - categorical_accuracy: 0.9410
59968/60000 [============================>.] - ETA: 0s - loss: 0.1925 - categorical_accuracy: 0.9411
60000/60000 [==============================] - 100s 2ms/step - loss: 0.1925 - categorical_accuracy: 0.9411 - val_loss: 0.0464 - val_categorical_accuracy: 0.9844

  ('#### Predict   ####################################################',) 

  ('#### Path params   ################################################',) 

  ('/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/', '/home/runner/work/mlmodels/mlmodels/keras_deepAR/') 

   32/10000 [..............................] - ETA: 15s
  224/10000 [..............................] - ETA: 4s 
  384/10000 [>.............................] - ETA: 4s
  576/10000 [>.............................] - ETA: 3s
  768/10000 [=>............................] - ETA: 3s
  960/10000 [=>............................] - ETA: 3s
 1152/10000 [==>...........................] - ETA: 3s
 1344/10000 [===>..........................] - ETA: 2s
 1536/10000 [===>..........................] - ETA: 2s
 1728/10000 [====>.........................] - ETA: 2s
 1920/10000 [====>.........................] - ETA: 2s
 2080/10000 [=====>........................] - ETA: 2s
 2240/10000 [=====>........................] - ETA: 2s
 2400/10000 [======>.......................] - ETA: 2s
 2592/10000 [======>.......................] - ETA: 2s
 2752/10000 [=======>......................] - ETA: 2s
 2912/10000 [=======>......................] - ETA: 2s
 3072/10000 [========>.....................] - ETA: 2s
 3264/10000 [========>.....................] - ETA: 2s
 3456/10000 [=========>....................] - ETA: 2s
 3648/10000 [=========>....................] - ETA: 2s
 3808/10000 [==========>...................] - ETA: 1s
 4000/10000 [===========>..................] - ETA: 1s
 4160/10000 [===========>..................] - ETA: 1s
 4352/10000 [============>.................] - ETA: 1s
 4544/10000 [============>.................] - ETA: 1s
 4704/10000 [=============>................] - ETA: 1s
 4896/10000 [=============>................] - ETA: 1s
 5056/10000 [==============>...............] - ETA: 1s
 5216/10000 [==============>...............] - ETA: 1s
 5376/10000 [===============>..............] - ETA: 1s
 5568/10000 [===============>..............] - ETA: 1s
 5760/10000 [================>.............] - ETA: 1s
 5952/10000 [================>.............] - ETA: 1s
 6144/10000 [=================>............] - ETA: 1s
 6336/10000 [==================>...........] - ETA: 1s
 6528/10000 [==================>...........] - ETA: 1s
 6720/10000 [===================>..........] - ETA: 1s
 6912/10000 [===================>..........] - ETA: 0s
 7072/10000 [====================>.........] - ETA: 0s
 7264/10000 [====================>.........] - ETA: 0s
 7456/10000 [=====================>........] - ETA: 0s
 7648/10000 [=====================>........] - ETA: 0s
 7840/10000 [======================>.......] - ETA: 0s
 8032/10000 [=======================>......] - ETA: 0s
 8224/10000 [=======================>......] - ETA: 0s
 8416/10000 [========================>.....] - ETA: 0s
 8608/10000 [========================>.....] - ETA: 0s
 8768/10000 [=========================>....] - ETA: 0s
 8960/10000 [=========================>....] - ETA: 0s
 9152/10000 [==========================>...] - ETA: 0s
 9344/10000 [===========================>..] - ETA: 0s
 9536/10000 [===========================>..] - ETA: 0s
 9696/10000 [============================>.] - ETA: 0s
 9888/10000 [============================>.] - ETA: 0s
10000/10000 [==============================] - 3s 314us/step
[[3.19320236e-07 1.09672103e-08 1.91400932e-06 ... 9.99996066e-01
  4.65409720e-08 1.31248942e-06]
 [1.90175542e-05 2.04097869e-05 9.99875665e-01 ... 4.76808060e-09
  9.44065232e-06 1.84129778e-09]
 [5.64145921e-06 9.99412060e-01 4.31497720e-05 ... 1.48438092e-04
  5.96657192e-05 6.06731783e-06]
 ...
 [2.65356306e-07 2.43573982e-06 3.51304720e-07 ... 4.65282028e-05
  1.22824385e-05 1.13492795e-04]
 [6.65049229e-05 3.62377705e-07 3.37900104e-07 ... 1.42374859e-06
  6.95338054e-03 9.13977510e-06]
 [3.60986155e-06 1.27533553e-07 4.64704681e-06 ... 4.67096861e-10
  1.95092539e-07 5.52357182e-09]]

  ('#### metrics   ####################################################',) 

  ('#### Path params   ################################################',) 

  ('/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/', '/home/runner/work/mlmodels/mlmodels/keras_deepAR/') 
{'loss_test:': 0.046417724947468375, 'accuracy_test:': 0.9843999743461609}

  ('#### Save   #######################################################',) 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_keras/charcnn/result'}

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git add --all &&  git commit -m "ml_store  && git pull --all"  ;            git push --all -f ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
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
[master 57ac7fb] ml_store  && git pull --all
 1 file changed, 1553 insertions(+)
Warning: Permanently added the RSA host key for IP address '140.82.114.3' to the list of known hosts.
To github.com:arita37/mlmodels_store.git
 + 29b5ff0...57ac7fb master -> master (forced update)





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
{'loss': 0.5992859676480293, 'loss_history': []}

  #### Plot   ######################################################## 

  #### Save   ######################################################## 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/'}
Model saved in path: /home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm//model//model.ckpt

  ['model_pars.pkl', 'model.ckpt.index', 'model.ckpt.data-00000-of-00001', 'checkpoint', 'model.ckpt.meta'] 

  #### Load   ######################################################## 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/', 'model_path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/model'}
Loaded saved model from /home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/model
Loaded saved model from /home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/model

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git add --all &&  git commit -m "ml_store  && git pull --all"  ;            git push --all -f ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
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
[master d260ba9] ml_store  && git pull --all
 1 file changed, 112 insertions(+)
To github.com:arita37/mlmodels_store.git
   57ac7fb..d260ba9  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//temporal_fusion_google.py 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tf//temporal_fusion_google.py", line 17, in <module>
    from mlmodels.mode_tf.raw  import temporal_fusion_google
ModuleNotFoundError: No module named 'mlmodels.mode_tf'

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git add --all &&  git commit -m "ml_store  && git pull --all"  ;            git push --all -f ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
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
[master ec4b5b6] ml_store  && git pull --all
 1 file changed, 34 insertions(+)
To github.com:arita37/mlmodels_store.git
   d260ba9..ec4b5b6  master -> master





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
 40%|████      | 2/5 [00:16<00:24,  8.19s/it]Saving dataset/models/LightGBMClassifier/trial_1_model.pkl
Finished Task with config: {'feature_fraction': 0.836410624931228, 'learning_rate': 0.05630740844181091, 'min_data_in_leaf': 4, 'num_leaves': 41} and reward: 0.39
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xea\xc3\xe07\x03h\xd4X\r\x00\x00\x00learning_rateq\x02G?\xac\xd4S\x1b\x8fh>X\x10\x00\x00\x00min_data_in_leafq\x03K\x04X\n\x00\x00\x00num_leavesq\x04K)u.' and reward: 0.39
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xea\xc3\xe07\x03h\xd4X\r\x00\x00\x00learning_rateq\x02G?\xac\xd4S\x1b\x8fh>X\x10\x00\x00\x00min_data_in_leafq\x03K\x04X\n\x00\x00\x00num_leavesq\x04K)u.' and reward: 0.39
 60%|██████    | 3/5 [00:33<00:21, 10.94s/it]Saving dataset/models/LightGBMClassifier/trial_2_model.pkl
Finished Task with config: {'feature_fraction': 0.8383740059165958, 'learning_rate': 0.1870983263161547, 'min_data_in_leaf': 6, 'num_leaves': 49} and reward: 0.3842
Finished Task with config: b"\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xea\xd3\xf5\xb9'N&X\r\x00\x00\x00learning_rateq\x02G?\xc7\xf2\xd6\x84U\x05.X\x10\x00\x00\x00min_data_in_leafq\x03K\x06X\n\x00\x00\x00num_leavesq\x04K1u." and reward: 0.3842
Finished Task with config: b"\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xea\xd3\xf5\xb9'N&X\r\x00\x00\x00learning_rateq\x02G?\xc7\xf2\xd6\x84U\x05.X\x10\x00\x00\x00min_data_in_leafq\x03K\x06X\n\x00\x00\x00num_leavesq\x04K1u." and reward: 0.3842
 80%|████████  | 4/5 [00:51<00:13, 13.05s/it]Saving dataset/models/LightGBMClassifier/trial_3_model.pkl
Finished Task with config: {'feature_fraction': 0.7573883042933204, 'learning_rate': 0.0578798384253015, 'min_data_in_leaf': 11, 'num_leaves': 37} and reward: 0.3934
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xe8<\x86e\xaa\x01\xb3X\r\x00\x00\x00learning_rateq\x02G?\xad\xa2m\x1aD\xd4\x8bX\x10\x00\x00\x00min_data_in_leafq\x03K\x0bX\n\x00\x00\x00num_leavesq\x04K%u.' and reward: 0.3934
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xe8<\x86e\xaa\x01\xb3X\r\x00\x00\x00learning_rateq\x02G?\xad\xa2m\x1aD\xd4\x8bX\x10\x00\x00\x00min_data_in_leafq\x03K\x0bX\n\x00\x00\x00num_leavesq\x04K%u.' and reward: 0.3934
100%|██████████| 5/5 [01:08<00:00, 14.17s/it]100%|██████████| 5/5 [01:08<00:00, 13.70s/it]
Saving dataset/models/LightGBMClassifier/trial_4_model.pkl
Finished Task with config: {'feature_fraction': 0.882769422403265, 'learning_rate': 0.03134612719929234, 'min_data_in_leaf': 18, 'num_leaves': 31} and reward: 0.3928
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xec?\xa5\xa8\xe4/\xc8X\r\x00\x00\x00learning_rateq\x02G?\xa0\x0c\x99~Z\xbc%X\x10\x00\x00\x00min_data_in_leafq\x03K\x12X\n\x00\x00\x00num_leavesq\x04K\x1fu.' and reward: 0.3928
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xec?\xa5\xa8\xe4/\xc8X\r\x00\x00\x00learning_rateq\x02G?\xa0\x0c\x99~Z\xbc%X\x10\x00\x00\x00min_data_in_leafq\x03K\x12X\n\x00\x00\x00num_leavesq\x04K\x1fu.' and reward: 0.3928
Time for Gradient Boosting hyperparameter optimization: 84.0520396232605
Best hyperparameter configuration for Gradient Boosting Model: 
{'feature_fraction': 0.7573883042933204, 'learning_rate': 0.0578798384253015, 'min_data_in_leaf': 11, 'num_leaves': 37}
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
Saving dataset/models/NeuralNetClassifier/trial_5_tabularNN.pkl
Finished Task with config: {'activation.choice': 0, 'dropout_prob': 0.1, 'embedding_size_factor': 1.0, 'layers.choice': 0, 'learning_rate': 0.0005, 'network_type.choice': 0, 'use_batchnorm.choice': 0, 'weight_decay': 1e-06} and reward: 0.3868
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\xb9\x99\x99\x99\x99\x99\x9aX\x15\x00\x00\x00embedding_size_factorq\x03G?\xf0\x00\x00\x00\x00\x00\x00X\r\x00\x00\x00layers.choiceq\x04K\x00X\r\x00\x00\x00learning_rateq\x05G?@bM\xd2\xf1\xa9\xfcX\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G>\xb0\xc6\xf7\xa0\xb5\xed\x8du.' and reward: 0.3868
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\xb9\x99\x99\x99\x99\x99\x9aX\x15\x00\x00\x00embedding_size_factorq\x03G?\xf0\x00\x00\x00\x00\x00\x00X\r\x00\x00\x00layers.choiceq\x04K\x00X\r\x00\x00\x00learning_rateq\x05G?@bM\xd2\xf1\xa9\xfcX\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G>\xb0\xc6\xf7\xa0\xb5\xed\x8du.' and reward: 0.3868
 40%|████      | 2/5 [00:54<01:22, 27.36s/it] 40%|████      | 2/5 [00:54<01:22, 27.36s/it]
Loading: dataset/models/NeuralNetClassifier/train_tabNNdataset.pkl
Loading: dataset/models/NeuralNetClassifier/validation_tabNNdataset.pkl
Saving dataset/models/NeuralNetClassifier/trial_6_tabularNN.pkl
Finished Task with config: {'activation.choice': 0, 'dropout_prob': 0.41987053767945476, 'embedding_size_factor': 1.1297824276777326, 'layers.choice': 1, 'learning_rate': 0.000151382609152199, 'network_type.choice': 1, 'use_batchnorm.choice': 0, 'weight_decay': 0.00013824588954361938} and reward: 0.375
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\xda\xdf(\xac\xf8\xc7\xc9X\x15\x00\x00\x00embedding_size_factorq\x03G?\xf2\x13\x96\xbd\'\x8a\xa3X\r\x00\x00\x00layers.choiceq\x04K\x01X\r\x00\x00\x00learning_rateq\x05G?#\xd7\x8e\xb6\x03\x06\xf0X\x13\x00\x00\x00network_type.choiceq\x06K\x01X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G?"\x1e\xc3&\x17D\xb4u.' and reward: 0.375
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x00X\x0c\x00\x00\x00dropout_probq\x02G?\xda\xdf(\xac\xf8\xc7\xc9X\x15\x00\x00\x00embedding_size_factorq\x03G?\xf2\x13\x96\xbd\'\x8a\xa3X\r\x00\x00\x00layers.choiceq\x04K\x01X\r\x00\x00\x00learning_rateq\x05G?#\xd7\x8e\xb6\x03\x06\xf0X\x13\x00\x00\x00network_type.choiceq\x06K\x01X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x00X\x0c\x00\x00\x00weight_decayq\x08G?"\x1e\xc3&\x17D\xb4u.' and reward: 0.375
Please either provide filename or allow plot in get_training_curves
Time for Neural Network hyperparameter optimization: 152.96902346611023
Best hyperparameter configuration for Tabular Neural Network: 
{'activation.choice': 0, 'dropout_prob': 0.1, 'embedding_size_factor': 1.0, 'layers.choice': 0, 'learning_rate': 0.0005, 'network_type.choice': 0, 'use_batchnorm.choice': 0, 'weight_decay': 1e-06}
Saving dataset/models/trainer.pkl
Loading: dataset/models/LightGBMClassifier/trial_0_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_1_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_2_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_3_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_4_model.pkl
Loading: dataset/models/NeuralNetClassifier/trial_5_tabularNN.pkl
Loading: dataset/models/NeuralNetClassifier/trial_6_tabularNN.pkl
Fitting model: weighted_ensemble_k0_l1 ... Training model for up to 119.76s of the -121.22s of remaining time.
Ensemble size: 96
Ensemble weights: 
[0.1875     0.125      0.13541667 0.11458333 0.41666667 0.
 0.02083333]
	0.3966	 = Validation accuracy score
	1.69s	 = Training runtime
	0.0s	 = Validation runtime
Saving dataset/models/weighted_ensemble_k0_l1/model.pkl
Saving dataset/models/trainer.pkl
Saving dataset/models/trainer.pkl
Saving dataset/models/trainer.pkl
AutoGluon training complete, total runtime = 242.97s ...
Loading: dataset/models/trainer.pkl

  #### save the trained model  ####################################### 

  #### Predict   #################################################### 
Loaded data from: https://autogluon.s3.amazonaws.com/datasets/Inc/test.csv | Columns = 15 / 15 | Rows = 9769 -> 9769
Loading: dataset/models/trainer.pkl
Loading: dataset/models/weighted_ensemble_k0_l1/model.pkl
Loading: dataset/models/LightGBMClassifier/trial_3_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_4_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_0_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_1_model.pkl
Loading: dataset/models/NeuralNetClassifier/trial_5_tabularNN.pkl
Loading: dataset/models/NeuralNetClassifier/trial_6_tabularNN.pkl

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
Saving dataset/learner.pkl
TabularPredictor saved. To load, use: TabularPredictor.load(dataset/)
<mlmodels.model_gluon.util_autogluon.Model_empty object at 0x7f940d083940>

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git add --all &&  git commit -m "ml_store  && git pull --all"  ;            git push --all -f ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
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
[master f9e8a43] ml_store  && git pull --all
 1 file changed, 204 insertions(+)
To github.com:arita37/mlmodels_store.git
 + e1139bc...f9e8a43 master -> master (forced update)





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon//fb_prophet.py 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon//fb_prophet.py", line 160, in <module>
    test(data_path = "model_fb/fbprophet.json", choice="json" )
TypeError: test() got an unexpected keyword argument 'choice'

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git add --all &&  git commit -m "ml_store  && git pull --all"  ;            git push --all -f ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
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
[master 238b077] ml_store  && git pull --all
 1 file changed, 34 insertions(+)
To github.com:arita37/mlmodels_store.git
   f9e8a43..238b077  master -> master





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
100%|██████████| 10/10 [00:02<00:00,  3.45it/s, avg_epoch_loss=5.24]
INFO:root:Epoch[0] Elapsed time 2.899 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=5.235034
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 5.235034370422364 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7f4b8f4583c8>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7f4b8f4583c8>

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
Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 99.03it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 1040.9512532552083,
    "abs_error": 365.74871826171875,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 2.4234326546103135,
    "sMAPE": 0.5083014916109209,
    "MSIS": 96.93730941973959,
    "QuantileLoss[0.5]": 365.7487030029297,
    "Coverage[0.5]": 1.0,
    "RMSE": 32.26377617786251,
    "NRMSE": 0.6792373932181581,
    "ND": 0.6416644180030153,
    "wQuantileLoss[0.5]": 0.64166439123321,
    "mean_wQuantileLoss": 0.64166439123321,
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
100%|██████████| 10/10 [00:01<00:00,  7.34it/s, avg_epoch_loss=2.71e+3]
INFO:root:Epoch[0] Elapsed time 1.363 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=2713.411247
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 2713.4112467447917 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7f4b5ee4d8d0>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7f4b5ee4d8d0>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 152.39it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
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
100%|██████████| 10/10 [00:01<00:00,  5.13it/s, avg_epoch_loss=5.21]
INFO:root:Epoch[0] Elapsed time 1.950 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=5.210828
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 5.210828447341919 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7f4b5c6ccac8>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7f4b5c6ccac8>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 148.76it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 263.09228515625,
    "abs_error": 170.82232666015625,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 1.1318601649028979,
    "sMAPE": 0.28359530441357556,
    "MSIS": 45.27440659611592,
    "QuantileLoss[0.5]": 170.82231903076172,
    "Coverage[0.5]": 0.75,
    "RMSE": 16.220119763930537,
    "NRMSE": 0.3414762055564324,
    "ND": 0.299688292386239,
    "wQuantileLoss[0.5]": 0.2996882790013363,
    "mean_wQuantileLoss": 0.2996882790013363,
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
 30%|███       | 3/10 [00:12<00:29,  4.21s/it, avg_epoch_loss=6.93] 60%|██████    | 6/10 [00:23<00:16,  4.05s/it, avg_epoch_loss=6.91] 90%|█████████ | 9/10 [00:34<00:03,  3.94s/it, avg_epoch_loss=6.87]100%|██████████| 10/10 [00:38<00:00,  3.84s/it, avg_epoch_loss=6.86]
INFO:root:Epoch[0] Elapsed time 38.397 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=6.862630
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 6.862630081176758 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7f4b5ef58588>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7f4b5ef58588>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 127.59it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 54519.984375,
    "abs_error": 2758.123779296875,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 18.27518976408906,
    "sMAPE": 1.4181537548030982,
    "MSIS": 731.0074999744046,
    "QuantileLoss[0.5]": 2758.1235961914062,
    "Coverage[0.5]": 1.0,
    "RMSE": 233.4951485042034,
    "NRMSE": 4.915687336930598,
    "ND": 4.838813647889254,
    "wQuantileLoss[0.5]": 4.83881332665159,
    "mean_wQuantileLoss": 4.83881332665159,
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
100%|██████████| 10/10 [00:00<00:00, 46.34it/s, avg_epoch_loss=5.06]
INFO:root:Epoch[0] Elapsed time 0.216 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=5.057605
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 5.057605314254761 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7f4b5c575fd0>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7f4b5c575fd0>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 148.06it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 333.7436930338542,
    "abs_error": 200.84359741210938,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 1.3307795984936939,
    "sMAPE": 0.32928199150545306,
    "MSIS": 53.2311758514301,
    "QuantileLoss[0.5]": 200.84357833862305,
    "Coverage[0.5]": 0.75,
    "RMSE": 18.26865329009925,
    "NRMSE": 0.38460322715998424,
    "ND": 0.35235718844229713,
    "wQuantileLoss[0.5]": 0.35235715498004044,
    "mean_wQuantileLoss": 0.35235715498004044,
    "MAE_Coverage": 0.25
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
100%|██████████| 10/10 [00:01<00:00,  7.95it/s, avg_epoch_loss=144]
INFO:root:Epoch[0] Elapsed time 1.259 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=144.412806
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 144.41280616614463 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7f4b5c643ef0>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7f4b5c643ef0>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 149.38it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 2434.5670123443265,
    "abs_error": 573.7377910258112,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 3.8015578142395565,
    "sMAPE": 1.9586154749802402,
    "MSIS": 152.0623125695823,
    "QuantileLoss[0.5]": 573.7377910258112,
    "Coverage[0.5]": 0.0,
    "RMSE": 49.34133168393742,
    "NRMSE": 1.0387648775565772,
    "ND": 1.0065575281154584,
    "wQuantileLoss[0.5]": 1.0065575281154584,
    "mean_wQuantileLoss": 1.0065575281154584,
    "MAE_Coverage": 0.5
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
 10%|█         | 1/10 [01:53<17:02, 113.63s/it, avg_epoch_loss=0.488] 20%|██        | 2/10 [04:39<17:14, 129.34s/it, avg_epoch_loss=0.47]  30%|███       | 3/10 [07:38<16:49, 144.18s/it, avg_epoch_loss=0.453] 40%|████      | 4/10 [10:22<14:59, 150.00s/it, avg_epoch_loss=0.437] 50%|█████     | 5/10 [13:57<14:07, 169.53s/it, avg_epoch_loss=0.424] 60%|██████    | 6/10 [17:10<11:46, 176.71s/it, avg_epoch_loss=0.414] 70%|███████   | 7/10 [20:22<09:03, 181.33s/it, avg_epoch_loss=0.407] 80%|████████  | 8/10 [23:51<06:19, 189.69s/it, avg_epoch_loss=0.404] 90%|█████████ | 9/10 [27:04<03:10, 190.65s/it, avg_epoch_loss=0.401]100%|██████████| 10/10 [30:23<00:00, 193.03s/it, avg_epoch_loss=0.399]100%|██████████| 10/10 [30:23<00:00, 182.34s/it, avg_epoch_loss=0.399]
INFO:root:Epoch[0] Elapsed time 1823.429 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=0.398938
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 0.3989381194114685 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7f4b5c6b4f98>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7f4b5c6b4f98>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 20.36it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 137.49435424804688,
    "abs_error": 102.26634979248047,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 0.6776117021893543,
    "sMAPE": 0.177204681090722,
    "MSIS": 27.104465256662994,
    "QuantileLoss[0.5]": 102.26634216308594,
    "Coverage[0.5]": 0.4166666666666667,
    "RMSE": 11.725798661415217,
    "NRMSE": 0.2468589191876888,
    "ND": 0.17941464875873767,
    "wQuantileLoss[0.5]": 0.17941463537383498,
    "mean_wQuantileLoss": 0.17941463537383498,
    "MAE_Coverage": 0.08333333333333331
}

  #### Plot   ####################################################### 


   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git add --all &&  git commit -m "ml_store  && git pull --all"  ;            git push --all -f ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
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
[master bd869c3] ml_store  && git pull --all
 1 file changed, 498 insertions(+)
To github.com:arita37/mlmodels_store.git
 + 4959fb0...bd869c3 master -> master (forced update)





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

  <mlmodels.model_sklearn.model_sklearn.Model object at 0x7fe688046748> 

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

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git add --all &&  git commit -m "ml_store  && git pull --all"  ;            git push --all -f ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
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
[master 4c11d8b] ml_store  && git pull --all
 1 file changed, 107 insertions(+)
To github.com:arita37/mlmodels_store.git
   bd869c3..4c11d8b  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_sklearn//model_lightgbm.py 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 

  #### save the trained model  ####################################### 

  #### Predict   ##################################################### 
[[ 1.01177337e+00  9.57467711e-02  7.31402517e-01  1.03345080e+00
  -1.42203164e+00 -1.46273275e-01 -1.74549518e-02 -8.57496825e-01
  -9.34181843e-01  9.54495667e-01]
 [ 6.81889336e-01 -1.15498263e+00  1.22895559e+00 -1.77632196e-01
   9.98545187e-01 -1.51045638e+00 -2.75846063e-01  1.01120706e+00
  -1.47656266e+00  1.30970591e+00]
 [ 9.71395338e-01  7.13049050e-01  1.76041518e+00  1.30620607e+00
   1.05765490e+00 -6.04602969e-01  1.28376990e-01  6.36583409e-01
   1.40925339e+00  9.66539250e-01]
 [ 8.61462558e-01  7.43205537e-02 -1.34501002e+00 -1.99560718e-01
  -1.47533915e+00 -6.54603169e-01 -3.14563862e-01  3.18014296e-01
  -8.90271552e-01 -1.29525789e+00]
 [ 1.13545112e+00  8.61623101e-01  4.90616924e-02 -2.08639057e+00
  -1.11469020e+00  3.61801641e-01 -8.06178212e-01  4.25920177e-01
   4.90803971e-02 -5.96086335e-01]
 [ 7.61706684e-01 -1.48515645e+00  1.30253554e+00 -5.92461285e-01
  -1.64162479e+00 -2.30490794e+00 -1.34869645e+00 -3.18171727e-02
   1.12487742e-01 -3.62612088e-01]
 [ 8.95623122e-01 -2.29820588e+00 -1.95225583e-02  1.45652739e+00
  -1.85064099e+00  3.16637236e-01  1.11337266e-01 -2.66412594e+00
  -4.26428618e-01 -8.39988915e-01]
 [ 6.18390447e-01 -7.25214926e-01  4.00084198e-03  1.53653633e+00
  -1.03048932e+00 -3.75008758e-04  5.31163793e-01  1.29354962e+00
  -4.38997664e-01  3.21265914e-01]
 [ 7.83440538e-01 -5.11884476e-02  8.24584625e-01 -7.25597119e-01
   9.31717197e-01 -8.67768678e-01  3.03085711e+00 -1.35977326e-01
  -7.97269785e-01  6.54580153e-01]
 [ 6.13636707e-01  3.16658895e-01  1.34710546e+00 -1.89526695e+00
  -7.60458095e-01  8.97291174e-02 -3.29051549e-01  4.10265745e-01
   8.59870972e-01 -1.04906775e+00]
 [ 1.12062155e+00 -7.02920403e-01 -1.22957425e+00  7.25550518e-01
  -1.18013412e+00 -3.24204219e-01  1.10223673e+00  8.14343129e-01
   7.80469930e-01  1.10861676e+00]
 [ 1.36586461e+00  3.95860270e+00  5.48129585e-01  6.48643644e-01
   8.49176066e-01  1.07343294e-01  1.38631426e+00 -1.39881282e+00
   8.17678188e-02 -1.63744959e+00]
 [ 6.91743730e-01  1.00978733e+00 -1.21333813e+00 -1.55694156e+00
  -1.20257258e+00 -6.12442128e-01 -2.69836174e+00 -1.39351805e-01
  -7.28537489e-01  7.22518992e-02]
 [ 8.53355545e-01 -7.04350332e-01 -6.79383783e-01 -4.58666861e-02
  -1.29936179e+00 -2.18733459e-01  5.90039464e-01  1.53920701e+00
  -1.14870423e+00 -9.50909251e-01]
 [ 1.07258847e+00 -5.86523939e-01 -1.34267579e+00 -1.23685338e+00
   1.24328724e+00  8.75838928e-01 -3.26499498e-01  6.23362177e-01
  -4.34956683e-01  1.11438298e+00]
 [ 9.29250600e-01 -1.10657307e+00 -1.95816909e+00 -3.59224096e-01
  -1.21258781e+00  5.05381903e-01  5.42645295e-01  1.21794090e+00
  -1.94068096e+00  6.77807571e-01]
 [ 7.22978007e-01  1.85535621e-01  9.15499268e-01  3.94428030e-01
  -8.49830738e-01  7.25522558e-01 -1.50504326e-01  1.49588477e+00
   6.75453809e-01 -4.38200267e-01]
 [ 1.22867367e+00  1.34373116e-01 -1.82420406e-01 -2.68371304e-01
  -1.73963799e+00 -1.31675626e-01 -9.26871939e-01  1.01855247e+00
   1.23055820e+00 -4.91125138e-01]
 [ 1.21619061e+00 -1.90005215e-02  8.60891241e-01 -2.26760192e-01
  -1.36419132e+00 -1.56450785e+00  1.63169151e+00  9.31255679e-01
   9.49808815e-01 -8.80189065e-01]
 [ 8.95510508e-01  9.20615118e-01  7.94528240e-01 -3.53679249e-02
   8.78099103e-01  2.11060505e+00 -1.02188594e+00 -1.30653407e+00
   7.63804802e-02 -1.87316098e+00]
 [ 1.34740825e+00  7.33023232e-01  8.38634747e-01 -1.89881206e+00
  -5.42459922e-01 -1.11711069e+00 -1.09715436e+00 -5.08972278e-01
  -1.66485955e-01 -1.03918232e+00]
 [ 7.73703613e-01  1.27852808e+00 -2.11416392e+00 -4.42229280e-01
   1.06821044e+00  3.23527354e-01 -2.50644065e+00 -1.09991490e-01
   8.54894544e-03 -4.11639163e-01]
 [ 7.88018455e-01  3.01960045e-01  7.00982122e-01 -3.94689681e-01
  -1.20376927e+00 -1.17181338e+00  7.55392029e-01  9.84012237e-01
  -5.59681422e-01 -1.98937450e-01]
 [ 1.12641981e+00 -6.29441604e-01  1.10100020e+00 -1.11343610e+00
   9.44595066e-01 -6.74100249e-02 -1.83400197e-01  1.16143998e+00
  -2.75293863e-02  7.80027135e-01]
 [ 7.75285326e-01  1.47016034e+00  1.03298378e+00 -8.70008223e-01
   7.86556511e-01  3.69190470e-01 -1.43195745e-01  8.53282186e-01
  -1.39711730e-01 -2.22414029e-01]]

  #### metrics   ##################################################### 
{}

  #### Plot   ######################################################## 

  #### Save/Load   ################################################### 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_sklearn/model_lightgbm/model.pkl'}
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_sklearn/model_lightgbm/model.pkl'}
<__main__.Model object at 0x7fa169124cf8>

  #### Module init   ############################################ 

  <module 'mlmodels.model_sklearn.model_lightgbm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_sklearn/model_lightgbm.py'> 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Model init   ############################################ 

  <mlmodels.model_sklearn.model_lightgbm.Model object at 0x7fa169afa240> 

  #### Fit   ######################################################## 

  #### Predict   #################################################### 
[[ 8.58774962e-01  2.29371761e+00 -1.47023709e+00 -8.30010986e-01
  -6.72049816e-01 -1.01951985e+00  5.99213235e-01 -2.14653842e-01
   1.02124813e+00  6.06403944e-01]
 [ 1.98519313e+00  6.74711526e-01 -1.39662042e+00  6.18539131e-01
   1.22382712e+00 -4.43171931e-01 -1.89148284e-03  1.81053491e+00
  -1.30572692e+00 -8.61316361e-01]
 [ 2.07582971e+00 -1.40232915e+00 -4.79184915e-01  4.51122939e-01
   1.03436581e+00 -6.94920901e-01 -4.18937898e-01  5.15413802e-01
  -1.11487105e+00 -1.95210529e+00]
 [ 5.69983848e-01 -5.33020326e-01 -1.75458969e-01 -1.42655542e+00
   6.06604307e-01  1.76795995e+00 -1.15985185e-01 -4.75372875e-01
   4.77610182e-01 -9.33914656e-01]
 [ 1.25704434e+00 -1.82391985e+00 -6.12406973e-01  1.16707517e+00
  -6.23732812e-01 -3.96687001e-02  8.16043684e-01  8.85825799e-01
   1.89861649e-01  3.93109245e-01]
 [ 1.37661405e+00 -6.00225330e-01  7.25916853e-01 -3.79517516e-01
  -6.27546260e-01 -1.01480369e+00  9.66220863e-01  4.35986196e-01
  -6.87487393e-01  3.32107876e+00]
 [ 1.34740825e+00  7.33023232e-01  8.38634747e-01 -1.89881206e+00
  -5.42459922e-01 -1.11711069e+00 -1.09715436e+00 -5.08972278e-01
  -1.66485955e-01 -1.03918232e+00]
 [ 1.36586461e+00  3.95860270e+00  5.48129585e-01  6.48643644e-01
   8.49176066e-01  1.07343294e-01  1.38631426e+00 -1.39881282e+00
   8.17678188e-02 -1.63744959e+00]
 [ 1.02242019e+00  1.85300949e+00  6.44353666e-01  1.42251373e-01
   1.15080755e+00  5.13505480e-01 -4.59942831e-01  3.72456852e-01
  -1.48489803e-01  3.71670291e-01]
 [ 9.36211246e-01  2.04377395e-01 -1.49419377e+00  6.12232523e-01
  -9.84377246e-01  7.44884536e-01  4.94341651e-01 -3.62812886e-02
  -8.32395348e-01 -4.46699203e-01]
 [ 8.57719529e-01  9.81122462e-02 -2.60466059e-01  1.06032751e+00
  -1.39003042e+00 -1.71116766e+00  2.65642403e-01  1.65712464e+00
   1.41767401e+00  4.45096710e-01]
 [ 1.83829400e+00  5.02740882e-01  1.29101580e-01  1.55880554e+00
   1.32551412e+00  1.09402696e-01  1.40754000e+00 -1.21974440e+00
   2.44936865e+00  1.61694960e+00]
 [ 1.64661853e+00 -1.52568032e+00 -6.06998398e-01  7.95026094e-01
   1.08480038e+00 -3.74438319e-01  4.29526140e-01  1.34048197e-01
   1.20205486e+00  1.06222724e-01]
 [ 6.23688521e-01  1.20660790e+00  9.03999174e-01 -2.82863552e-01
  -1.18913787e+00 -2.66326884e-01  1.42361443e+00  1.06897162e+00
   4.03714310e-02  1.57546791e+00]
 [ 1.12641981e+00 -6.29441604e-01  1.10100020e+00 -1.11343610e+00
   9.44595066e-01 -6.74100249e-02 -1.83400197e-01  1.16143998e+00
  -2.75293863e-02  7.80027135e-01]
 [ 7.61706684e-01 -1.48515645e+00  1.30253554e+00 -5.92461285e-01
  -1.64162479e+00 -2.30490794e+00 -1.34869645e+00 -3.18171727e-02
   1.12487742e-01 -3.62612088e-01]
 [ 1.06523311e+00 -6.64867767e-01  1.00806543e+00 -1.94504696e+00
  -1.23017555e+00 -9.15424368e-01  3.37220938e-01  1.22515585e+00
  -1.05354607e+00  7.85226920e-01]
 [ 1.06040861e+00  5.10307597e-01  5.01725109e-01 -9.15791849e-01
  -9.07318361e-01 -4.07252043e-01 -1.79612295e-01  9.84951672e-01
   1.07125243e+00 -5.93343754e-01]
 [ 8.61462558e-01  7.43205537e-02 -1.34501002e+00 -1.99560718e-01
  -1.47533915e+00 -6.54603169e-01 -3.14563862e-01  3.18014296e-01
  -8.90271552e-01 -1.29525789e+00]
 [ 9.71395338e-01  7.13049050e-01  1.76041518e+00  1.30620607e+00
   1.05765490e+00 -6.04602969e-01  1.28376990e-01  6.36583409e-01
   1.40925339e+00  9.66539250e-01]
 [ 8.76994650e-01  1.23225307e+00 -8.67787223e-01 -2.54179868e-01
   8.91891405e-01  1.39984394e+00 -8.77281519e-01 -7.81911683e-01
  -4.37508983e-01 -1.44087602e+00]
 [ 1.58463774e+00  5.71209961e-02 -1.77183179e-02 -7.99547491e-01
   1.32970299e+00 -2.91594596e-01 -1.10771250e+00 -2.58982853e-01
   1.89293198e-01 -1.71939447e+00]
 [ 9.80427414e-01  1.93752881e+00 -2.30839743e-01  3.66332015e-01
   1.10018476e+00 -1.04458938e+00 -3.44987210e-01  2.05117344e+00
   5.85662000e-01 -2.79308500e+00]
 [ 8.48069266e-01  4.51946037e-01  6.30195671e-01 -1.57915629e+00
   8.27987371e-01 -8.28627979e-01 -1.05344713e-01  5.28879746e-01
  -2.23708651e+00 -4.14846901e-01]
 [ 8.59823751e-01  1.71957132e-01 -3.48984191e-01  4.90561044e-01
  -1.15649503e+00 -1.39528303e+00  6.14726276e-01 -5.22356465e-01
  -3.69255902e-01 -9.77773002e-01]]
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
[[ 1.01177337  0.09574677  0.73140252  1.0334508  -1.42203164 -0.14627327
  -0.01745495 -0.85749682 -0.93418184  0.95449567]
 [ 0.89891716  0.55743945 -0.75806733  0.18103874  0.84146721  1.10717545
   0.69336623  1.44287693 -0.53968156 -0.8088472 ]
 [ 1.02817479 -0.50845713  1.7653351   0.77741921  0.61771419 -0.11877117
   0.45015551 -0.19899818  1.86647138  0.8709698 ]
 [ 0.44118981  0.47985237 -0.1920037  -1.55269878 -1.88873982  0.57846442
   0.39859839 -0.9612636  -1.45832446 -3.05376438]
 [ 1.36586461  3.9586027   0.54812958  0.64864364  0.84917607  0.10734329
   1.38631426 -1.39881282  0.08176782 -1.63744959]
 [ 0.92686981  0.39233491 -0.4234783   0.44838065 -1.09230828  1.1253235
  -0.94843966  0.10405339  0.52800342  1.00796648]
 [ 1.21619061 -0.01900052  0.86089124 -0.22676019 -1.36419132 -1.56450785
   1.63169151  0.93125568  0.94980882 -0.88018906]
 [ 0.96703727  0.38271517 -0.80618482 -0.28899734  0.90852604 -0.39181624
   1.62091229  0.68400133 -0.35340998 -0.25167421]
 [ 0.87874071 -0.01923163  0.31965694  0.15001628 -1.46662161  0.46353432
  -0.89868319  0.39788042 -0.99601089  0.3181542 ]
 [ 0.10593645 -0.73728963  0.65032321  0.16466507 -1.53556118  0.77817418
   0.05031709  0.30981676  1.05132077  0.6065484 ]
 [ 1.16755486  0.0353601   0.7147896  -1.53879325  1.10863359 -0.44789518
  -1.75592564  0.61798553 -0.18417633  0.85270406]
 [ 1.58463774  0.057121   -0.01771832 -0.79954749  1.32970299 -0.2915946
  -1.1077125  -0.25898285  0.1892932  -1.71939447]
 [ 0.6109426  -2.79099641 -1.33520272 -0.45611756 -0.94495995 -0.97989025
  -0.15699367  0.69257435 -0.47867236 -0.10646012]
 [ 0.88883881  1.03368687 -0.04970258  0.80884436  0.81405135  1.78975468
   1.14690038  0.45128402 -1.68405999  0.46664327]
 [ 1.03967316 -0.73153098  0.36184732 -1.56573815  0.95928819  1.01382247
  -1.78791289 -2.22711263 -1.6993336  -0.42449279]
 [ 1.18559003  0.08646441  1.23289919 -2.14246673  1.033341   -0.83016886
   0.36723181  0.45161595  1.10417433 -0.42285696]
 [ 0.55853873 -0.51634791 -0.51814555  0.3511169   0.82550695 -0.06877046
  -0.9520621  -1.34776494  1.47073986 -1.4614036 ]
 [ 1.25704434 -1.82391985 -0.61240697  1.16707517 -0.62373281 -0.0396687
   0.81604368  0.8858258   0.18986165  0.39310924]
 [ 0.69174373  1.00978733 -1.21333813 -1.55694156 -1.20257258 -0.61244213
  -2.69836174 -0.13935181 -0.72853749  0.0722519 ]
 [ 1.66752297  1.22372221 -0.4599301  -0.0593679  -0.493857    1.4489894
  -1.18110317 -0.47758085  0.02599999 -0.79079995]
 [ 0.85729649  0.9561217  -0.82609743 -0.70584051  1.13872896  1.19268607
   0.28267571 -0.23794194  1.15528789  0.6210827 ]
 [ 0.62153099 -1.50957268 -0.10193204 -1.08071069 -1.13742855  0.725474
   0.7980638  -0.03917826 -0.22875417  0.74335654]
 [ 0.94781411 -1.13379204  0.64098587 -0.1905483  -1.23912256  0.23333913
  -0.3169012   0.43499832  0.9104236   1.21987438]
 [ 0.87699465  1.23225307 -0.86778722 -0.25417987  0.89189141  1.39984394
  -0.87728152 -0.78191168 -0.43750898 -1.44087602]
 [ 0.96457205 -0.10679399  1.12232832  1.45142926  1.21828168 -0.61803685
   0.43816635 -2.03720123 -1.94258918 -0.9970198 ]]
None

  ############ Save/ Load ############################################ 

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git add --all &&  git commit -m "ml_store  && git pull --all"  ;            git push --all -f ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
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
[master f8c53c4] ml_store  && git pull --all
 1 file changed, 295 insertions(+)
To github.com:arita37/mlmodels_store.git
   4c11d8b..f8c53c4  master -> master





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
     | -- GenericBlock(units=256, thetas_dim=7, backcast_length=10, forecast_length=5, share_thetas=False) at @140427255562192
     | -- GenericBlock(units=256, thetas_dim=7, backcast_length=10, forecast_length=5, share_thetas=False) at @140427255561968
     | -- GenericBlock(units=256, thetas_dim=7, backcast_length=10, forecast_length=5, share_thetas=False) at @140427255560736
| --  Stack Generic (#1) (share_weights_in_stack=0)
     | -- GenericBlock(units=256, thetas_dim=8, backcast_length=10, forecast_length=5, share_thetas=False) at @140427255560288
     | -- GenericBlock(units=256, thetas_dim=8, backcast_length=10, forecast_length=5, share_thetas=False) at @140427255559784
     | -- GenericBlock(units=256, thetas_dim=8, backcast_length=10, forecast_length=5, share_thetas=False) at @140427255559448

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
grad_step = 000000, loss = 0.489215
plot()
Saved image to .//n_beats_0.png.
grad_step = 000001, loss = 0.359931
grad_step = 000002, loss = 0.276999
grad_step = 000003, loss = 0.190979
grad_step = 000004, loss = 0.106268
grad_step = 000005, loss = 0.047497
grad_step = 000006, loss = 0.056676
grad_step = 000007, loss = 0.080754
grad_step = 000008, loss = 0.064058
grad_step = 000009, loss = 0.031581
grad_step = 000010, loss = 0.012965
grad_step = 000011, loss = 0.011934
grad_step = 000012, loss = 0.019217
grad_step = 000013, loss = 0.026241
grad_step = 000014, loss = 0.029475
grad_step = 000015, loss = 0.028501
grad_step = 000016, loss = 0.024478
grad_step = 000017, loss = 0.019210
grad_step = 000018, loss = 0.014490
grad_step = 000019, loss = 0.011506
grad_step = 000020, loss = 0.010033
grad_step = 000021, loss = 0.009345
grad_step = 000022, loss = 0.008822
grad_step = 000023, loss = 0.008465
grad_step = 000024, loss = 0.008123
grad_step = 000025, loss = 0.007954
grad_step = 000026, loss = 0.008126
grad_step = 000027, loss = 0.008489
grad_step = 000028, loss = 0.008735
grad_step = 000029, loss = 0.008610
grad_step = 000030, loss = 0.008055
grad_step = 000031, loss = 0.007220
grad_step = 000032, loss = 0.006381
grad_step = 000033, loss = 0.005802
grad_step = 000034, loss = 0.005609
grad_step = 000035, loss = 0.005716
grad_step = 000036, loss = 0.005873
grad_step = 000037, loss = 0.005851
grad_step = 000038, loss = 0.005661
grad_step = 000039, loss = 0.005471
grad_step = 000040, loss = 0.005426
grad_step = 000041, loss = 0.005531
grad_step = 000042, loss = 0.005659
grad_step = 000043, loss = 0.005671
grad_step = 000044, loss = 0.005523
grad_step = 000045, loss = 0.005275
grad_step = 000046, loss = 0.005046
grad_step = 000047, loss = 0.004921
grad_step = 000048, loss = 0.004893
grad_step = 000049, loss = 0.004885
grad_step = 000050, loss = 0.004839
grad_step = 000051, loss = 0.004758
grad_step = 000052, loss = 0.004680
grad_step = 000053, loss = 0.004626
grad_step = 000054, loss = 0.004585
grad_step = 000055, loss = 0.004536
grad_step = 000056, loss = 0.004476
grad_step = 000057, loss = 0.004416
grad_step = 000058, loss = 0.004355
grad_step = 000059, loss = 0.004284
grad_step = 000060, loss = 0.004201
grad_step = 000061, loss = 0.004129
grad_step = 000062, loss = 0.004076
grad_step = 000063, loss = 0.004032
grad_step = 000064, loss = 0.003974
grad_step = 000065, loss = 0.003898
grad_step = 000066, loss = 0.003822
grad_step = 000067, loss = 0.003754
grad_step = 000068, loss = 0.003690
grad_step = 000069, loss = 0.003621
grad_step = 000070, loss = 0.003555
grad_step = 000071, loss = 0.003497
grad_step = 000072, loss = 0.003430
grad_step = 000073, loss = 0.003356
grad_step = 000074, loss = 0.003291
grad_step = 000075, loss = 0.003234
grad_step = 000076, loss = 0.003170
grad_step = 000077, loss = 0.003105
grad_step = 000078, loss = 0.003043
grad_step = 000079, loss = 0.002980
grad_step = 000080, loss = 0.002920
grad_step = 000081, loss = 0.002864
grad_step = 000082, loss = 0.002806
grad_step = 000083, loss = 0.002752
grad_step = 000084, loss = 0.002701
grad_step = 000085, loss = 0.002647
grad_step = 000086, loss = 0.002596
grad_step = 000087, loss = 0.002544
grad_step = 000088, loss = 0.002495
grad_step = 000089, loss = 0.002449
grad_step = 000090, loss = 0.002402
grad_step = 000091, loss = 0.002357
grad_step = 000092, loss = 0.002309
grad_step = 000093, loss = 0.002262
grad_step = 000094, loss = 0.002215
grad_step = 000095, loss = 0.002168
grad_step = 000096, loss = 0.002119
grad_step = 000097, loss = 0.002071
grad_step = 000098, loss = 0.002023
grad_step = 000099, loss = 0.001975
grad_step = 000100, loss = 0.001926
plot()
Saved image to .//n_beats_100.png.
grad_step = 000101, loss = 0.001880
grad_step = 000102, loss = 0.001834
grad_step = 000103, loss = 0.001789
grad_step = 000104, loss = 0.001747
grad_step = 000105, loss = 0.001706
grad_step = 000106, loss = 0.001667
grad_step = 000107, loss = 0.001629
grad_step = 000108, loss = 0.001593
grad_step = 000109, loss = 0.001557
grad_step = 000110, loss = 0.001523
grad_step = 000111, loss = 0.001489
grad_step = 000112, loss = 0.001456
grad_step = 000113, loss = 0.001422
grad_step = 000114, loss = 0.001388
grad_step = 000115, loss = 0.001354
grad_step = 000116, loss = 0.001320
grad_step = 000117, loss = 0.001287
grad_step = 000118, loss = 0.001255
grad_step = 000119, loss = 0.001224
grad_step = 000120, loss = 0.001194
grad_step = 000121, loss = 0.001166
grad_step = 000122, loss = 0.001138
grad_step = 000123, loss = 0.001113
grad_step = 000124, loss = 0.001091
grad_step = 000125, loss = 0.001069
grad_step = 000126, loss = 0.001052
grad_step = 000127, loss = 0.001048
grad_step = 000128, loss = 0.001044
grad_step = 000129, loss = 0.001007
grad_step = 000130, loss = 0.000987
grad_step = 000131, loss = 0.000979
grad_step = 000132, loss = 0.000974
grad_step = 000133, loss = 0.000942
grad_step = 000134, loss = 0.000937
grad_step = 000135, loss = 0.000933
grad_step = 000136, loss = 0.000908
grad_step = 000137, loss = 0.000903
grad_step = 000138, loss = 0.000893
grad_step = 000139, loss = 0.000886
grad_step = 000140, loss = 0.000870
grad_step = 000141, loss = 0.000862
grad_step = 000142, loss = 0.000860
grad_step = 000143, loss = 0.000847
grad_step = 000144, loss = 0.000837
grad_step = 000145, loss = 0.000832
grad_step = 000146, loss = 0.000825
grad_step = 000147, loss = 0.000819
grad_step = 000148, loss = 0.000807
grad_step = 000149, loss = 0.000803
grad_step = 000150, loss = 0.000799
grad_step = 000151, loss = 0.000790
grad_step = 000152, loss = 0.000784
grad_step = 000153, loss = 0.000778
grad_step = 000154, loss = 0.000773
grad_step = 000155, loss = 0.000770
grad_step = 000156, loss = 0.000762
grad_step = 000157, loss = 0.000755
grad_step = 000158, loss = 0.000752
grad_step = 000159, loss = 0.000747
grad_step = 000160, loss = 0.000741
grad_step = 000161, loss = 0.000737
grad_step = 000162, loss = 0.000730
grad_step = 000163, loss = 0.000725
grad_step = 000164, loss = 0.000721
grad_step = 000165, loss = 0.000715
grad_step = 000166, loss = 0.000711
grad_step = 000167, loss = 0.000706
grad_step = 000168, loss = 0.000700
grad_step = 000169, loss = 0.000696
grad_step = 000170, loss = 0.000692
grad_step = 000171, loss = 0.000687
grad_step = 000172, loss = 0.000682
grad_step = 000173, loss = 0.000678
grad_step = 000174, loss = 0.000676
grad_step = 000175, loss = 0.000675
grad_step = 000176, loss = 0.000677
grad_step = 000177, loss = 0.000685
grad_step = 000178, loss = 0.000689
grad_step = 000179, loss = 0.000683
grad_step = 000180, loss = 0.000660
grad_step = 000181, loss = 0.000640
grad_step = 000182, loss = 0.000640
grad_step = 000183, loss = 0.000648
grad_step = 000184, loss = 0.000647
grad_step = 000185, loss = 0.000631
grad_step = 000186, loss = 0.000619
grad_step = 000187, loss = 0.000618
grad_step = 000188, loss = 0.000622
grad_step = 000189, loss = 0.000620
grad_step = 000190, loss = 0.000608
grad_step = 000191, loss = 0.000598
grad_step = 000192, loss = 0.000595
grad_step = 000193, loss = 0.000596
grad_step = 000194, loss = 0.000594
grad_step = 000195, loss = 0.000587
grad_step = 000196, loss = 0.000578
grad_step = 000197, loss = 0.000572
grad_step = 000198, loss = 0.000568
grad_step = 000199, loss = 0.000567
grad_step = 000200, loss = 0.000566
plot()
Saved image to .//n_beats_200.png.
grad_step = 000201, loss = 0.000565
grad_step = 000202, loss = 0.000562
grad_step = 000203, loss = 0.000558
grad_step = 000204, loss = 0.000553
grad_step = 000205, loss = 0.000547
grad_step = 000206, loss = 0.000541
grad_step = 000207, loss = 0.000536
grad_step = 000208, loss = 0.000531
grad_step = 000209, loss = 0.000528
grad_step = 000210, loss = 0.000524
grad_step = 000211, loss = 0.000522
grad_step = 000212, loss = 0.000522
grad_step = 000213, loss = 0.000526
grad_step = 000214, loss = 0.000541
grad_step = 000215, loss = 0.000577
grad_step = 000216, loss = 0.000622
grad_step = 000217, loss = 0.000637
grad_step = 000218, loss = 0.000557
grad_step = 000219, loss = 0.000493
grad_step = 000220, loss = 0.000523
grad_step = 000221, loss = 0.000561
grad_step = 000222, loss = 0.000526
grad_step = 000223, loss = 0.000484
grad_step = 000224, loss = 0.000509
grad_step = 000225, loss = 0.000522
grad_step = 000226, loss = 0.000490
grad_step = 000227, loss = 0.000478
grad_step = 000228, loss = 0.000494
grad_step = 000229, loss = 0.000489
grad_step = 000230, loss = 0.000471
grad_step = 000231, loss = 0.000470
grad_step = 000232, loss = 0.000476
grad_step = 000233, loss = 0.000467
grad_step = 000234, loss = 0.000459
grad_step = 000235, loss = 0.000460
grad_step = 000236, loss = 0.000457
grad_step = 000237, loss = 0.000452
grad_step = 000238, loss = 0.000451
grad_step = 000239, loss = 0.000447
grad_step = 000240, loss = 0.000441
grad_step = 000241, loss = 0.000440
grad_step = 000242, loss = 0.000442
grad_step = 000243, loss = 0.000438
grad_step = 000244, loss = 0.000429
grad_step = 000245, loss = 0.000425
grad_step = 000246, loss = 0.000428
grad_step = 000247, loss = 0.000428
grad_step = 000248, loss = 0.000423
grad_step = 000249, loss = 0.000418
grad_step = 000250, loss = 0.000417
grad_step = 000251, loss = 0.000415
grad_step = 000252, loss = 0.000411
grad_step = 000253, loss = 0.000407
grad_step = 000254, loss = 0.000405
grad_step = 000255, loss = 0.000405
grad_step = 000256, loss = 0.000404
grad_step = 000257, loss = 0.000403
grad_step = 000258, loss = 0.000402
grad_step = 000259, loss = 0.000406
grad_step = 000260, loss = 0.000416
grad_step = 000261, loss = 0.000436
grad_step = 000262, loss = 0.000464
grad_step = 000263, loss = 0.000500
grad_step = 000264, loss = 0.000497
grad_step = 000265, loss = 0.000463
grad_step = 000266, loss = 0.000402
grad_step = 000267, loss = 0.000388
grad_step = 000268, loss = 0.000417
grad_step = 000269, loss = 0.000435
grad_step = 000270, loss = 0.000421
grad_step = 000271, loss = 0.000387
grad_step = 000272, loss = 0.000380
grad_step = 000273, loss = 0.000396
grad_step = 000274, loss = 0.000403
grad_step = 000275, loss = 0.000394
grad_step = 000276, loss = 0.000376
grad_step = 000277, loss = 0.000374
grad_step = 000278, loss = 0.000382
grad_step = 000279, loss = 0.000379
grad_step = 000280, loss = 0.000368
grad_step = 000281, loss = 0.000362
grad_step = 000282, loss = 0.000367
grad_step = 000283, loss = 0.000370
grad_step = 000284, loss = 0.000364
grad_step = 000285, loss = 0.000356
grad_step = 000286, loss = 0.000354
grad_step = 000287, loss = 0.000358
grad_step = 000288, loss = 0.000359
grad_step = 000289, loss = 0.000354
grad_step = 000290, loss = 0.000347
grad_step = 000291, loss = 0.000345
grad_step = 000292, loss = 0.000347
grad_step = 000293, loss = 0.000349
grad_step = 000294, loss = 0.000346
grad_step = 000295, loss = 0.000342
grad_step = 000296, loss = 0.000338
grad_step = 000297, loss = 0.000336
grad_step = 000298, loss = 0.000336
grad_step = 000299, loss = 0.000337
grad_step = 000300, loss = 0.000336
plot()
Saved image to .//n_beats_300.png.
grad_step = 000301, loss = 0.000333
grad_step = 000302, loss = 0.000331
grad_step = 000303, loss = 0.000329
grad_step = 000304, loss = 0.000327
grad_step = 000305, loss = 0.000327
grad_step = 000306, loss = 0.000327
grad_step = 000307, loss = 0.000328
grad_step = 000308, loss = 0.000328
grad_step = 000309, loss = 0.000328
grad_step = 000310, loss = 0.000327
grad_step = 000311, loss = 0.000326
grad_step = 000312, loss = 0.000326
grad_step = 000313, loss = 0.000325
grad_step = 000314, loss = 0.000327
grad_step = 000315, loss = 0.000331
grad_step = 000316, loss = 0.000342
grad_step = 000317, loss = 0.000360
grad_step = 000318, loss = 0.000394
grad_step = 000319, loss = 0.000417
grad_step = 000320, loss = 0.000429
grad_step = 000321, loss = 0.000378
grad_step = 000322, loss = 0.000326
grad_step = 000323, loss = 0.000308
grad_step = 000324, loss = 0.000330
grad_step = 000325, loss = 0.000354
grad_step = 000326, loss = 0.000347
grad_step = 000327, loss = 0.000334
grad_step = 000328, loss = 0.000325
grad_step = 000329, loss = 0.000314
grad_step = 000330, loss = 0.000306
grad_step = 000331, loss = 0.000309
grad_step = 000332, loss = 0.000320
grad_step = 000333, loss = 0.000320
grad_step = 000334, loss = 0.000301
grad_step = 000335, loss = 0.000293
grad_step = 000336, loss = 0.000300
grad_step = 000337, loss = 0.000306
grad_step = 000338, loss = 0.000301
grad_step = 000339, loss = 0.000295
grad_step = 000340, loss = 0.000294
grad_step = 000341, loss = 0.000292
grad_step = 000342, loss = 0.000288
grad_step = 000343, loss = 0.000287
grad_step = 000344, loss = 0.000292
grad_step = 000345, loss = 0.000293
grad_step = 000346, loss = 0.000289
grad_step = 000347, loss = 0.000284
grad_step = 000348, loss = 0.000282
grad_step = 000349, loss = 0.000282
grad_step = 000350, loss = 0.000281
grad_step = 000351, loss = 0.000279
grad_step = 000352, loss = 0.000277
grad_step = 000353, loss = 0.000279
grad_step = 000354, loss = 0.000280
grad_step = 000355, loss = 0.000280
grad_step = 000356, loss = 0.000279
grad_step = 000357, loss = 0.000278
grad_step = 000358, loss = 0.000278
grad_step = 000359, loss = 0.000279
grad_step = 000360, loss = 0.000280
grad_step = 000361, loss = 0.000280
grad_step = 000362, loss = 0.000279
grad_step = 000363, loss = 0.000280
grad_step = 000364, loss = 0.000281
grad_step = 000365, loss = 0.000284
grad_step = 000366, loss = 0.000285
grad_step = 000367, loss = 0.000287
grad_step = 000368, loss = 0.000285
grad_step = 000369, loss = 0.000286
grad_step = 000370, loss = 0.000283
grad_step = 000371, loss = 0.000282
grad_step = 000372, loss = 0.000278
grad_step = 000373, loss = 0.000273
grad_step = 000374, loss = 0.000267
grad_step = 000375, loss = 0.000262
grad_step = 000376, loss = 0.000258
grad_step = 000377, loss = 0.000256
grad_step = 000378, loss = 0.000257
grad_step = 000379, loss = 0.000258
grad_step = 000380, loss = 0.000261
grad_step = 000381, loss = 0.000265
grad_step = 000382, loss = 0.000271
grad_step = 000383, loss = 0.000277
grad_step = 000384, loss = 0.000290
grad_step = 000385, loss = 0.000298
grad_step = 000386, loss = 0.000313
grad_step = 000387, loss = 0.000306
grad_step = 000388, loss = 0.000296
grad_step = 000389, loss = 0.000269
grad_step = 000390, loss = 0.000252
grad_step = 000391, loss = 0.000251
grad_step = 000392, loss = 0.000261
grad_step = 000393, loss = 0.000276
grad_step = 000394, loss = 0.000279
grad_step = 000395, loss = 0.000277
grad_step = 000396, loss = 0.000265
grad_step = 000397, loss = 0.000255
grad_step = 000398, loss = 0.000247
grad_step = 000399, loss = 0.000247
grad_step = 000400, loss = 0.000250
plot()
Saved image to .//n_beats_400.png.
grad_step = 000401, loss = 0.000252
grad_step = 000402, loss = 0.000254
grad_step = 000403, loss = 0.000252
grad_step = 000404, loss = 0.000250
grad_step = 000405, loss = 0.000247
grad_step = 000406, loss = 0.000246
grad_step = 000407, loss = 0.000244
grad_step = 000408, loss = 0.000245
grad_step = 000409, loss = 0.000244
grad_step = 000410, loss = 0.000243
grad_step = 000411, loss = 0.000240
grad_step = 000412, loss = 0.000238
grad_step = 000413, loss = 0.000237
grad_step = 000414, loss = 0.000237
grad_step = 000415, loss = 0.000238
grad_step = 000416, loss = 0.000238
grad_step = 000417, loss = 0.000239
grad_step = 000418, loss = 0.000238
grad_step = 000419, loss = 0.000238
grad_step = 000420, loss = 0.000235
grad_step = 000421, loss = 0.000233
grad_step = 000422, loss = 0.000231
grad_step = 000423, loss = 0.000230
grad_step = 000424, loss = 0.000229
grad_step = 000425, loss = 0.000230
grad_step = 000426, loss = 0.000232
grad_step = 000427, loss = 0.000235
grad_step = 000428, loss = 0.000237
grad_step = 000429, loss = 0.000241
grad_step = 000430, loss = 0.000245
grad_step = 000431, loss = 0.000253
grad_step = 000432, loss = 0.000259
grad_step = 000433, loss = 0.000277
grad_step = 000434, loss = 0.000297
grad_step = 000435, loss = 0.000340
grad_step = 000436, loss = 0.000353
grad_step = 000437, loss = 0.000351
grad_step = 000438, loss = 0.000279
grad_step = 000439, loss = 0.000228
grad_step = 000440, loss = 0.000236
grad_step = 000441, loss = 0.000269
grad_step = 000442, loss = 0.000272
grad_step = 000443, loss = 0.000239
grad_step = 000444, loss = 0.000232
grad_step = 000445, loss = 0.000252
grad_step = 000446, loss = 0.000245
grad_step = 000447, loss = 0.000224
grad_step = 000448, loss = 0.000223
grad_step = 000449, loss = 0.000237
grad_step = 000450, loss = 0.000238
grad_step = 000451, loss = 0.000224
grad_step = 000452, loss = 0.000218
grad_step = 000453, loss = 0.000225
grad_step = 000454, loss = 0.000227
grad_step = 000455, loss = 0.000220
grad_step = 000456, loss = 0.000214
grad_step = 000457, loss = 0.000218
grad_step = 000458, loss = 0.000224
grad_step = 000459, loss = 0.000221
grad_step = 000460, loss = 0.000215
grad_step = 000461, loss = 0.000212
grad_step = 000462, loss = 0.000214
grad_step = 000463, loss = 0.000216
grad_step = 000464, loss = 0.000214
grad_step = 000465, loss = 0.000210
grad_step = 000466, loss = 0.000209
grad_step = 000467, loss = 0.000211
grad_step = 000468, loss = 0.000213
grad_step = 000469, loss = 0.000211
grad_step = 000470, loss = 0.000209
grad_step = 000471, loss = 0.000208
grad_step = 000472, loss = 0.000209
grad_step = 000473, loss = 0.000211
grad_step = 000474, loss = 0.000211
grad_step = 000475, loss = 0.000211
grad_step = 000476, loss = 0.000210
grad_step = 000477, loss = 0.000211
grad_step = 000478, loss = 0.000214
grad_step = 000479, loss = 0.000219
grad_step = 000480, loss = 0.000222
grad_step = 000481, loss = 0.000227
grad_step = 000482, loss = 0.000228
grad_step = 000483, loss = 0.000231
grad_step = 000484, loss = 0.000229
grad_step = 000485, loss = 0.000228
grad_step = 000486, loss = 0.000220
grad_step = 000487, loss = 0.000213
grad_step = 000488, loss = 0.000205
grad_step = 000489, loss = 0.000200
grad_step = 000490, loss = 0.000199
grad_step = 000491, loss = 0.000202
grad_step = 000492, loss = 0.000207
grad_step = 000493, loss = 0.000211
grad_step = 000494, loss = 0.000215
grad_step = 000495, loss = 0.000215
grad_step = 000496, loss = 0.000216
grad_step = 000497, loss = 0.000214
grad_step = 000498, loss = 0.000212
grad_step = 000499, loss = 0.000207
grad_step = 000500, loss = 0.000201
plot()
Saved image to .//n_beats_500.png.
grad_step = 000501, loss = 0.000196
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
[[0.83439326 0.8423114  0.9525229  0.9391364  1.0107028 ]
 [0.849957   0.9236617  0.9505254  1.0070246  1.0016263 ]
 [0.88140243 0.9097667  1.008378   0.961799   0.9437683 ]
 [0.92025006 0.98475474 0.98761886 0.9516516  0.9150318 ]
 [0.973662   0.99311703 0.94714737 0.9121011  0.856979  ]
 [0.97901136 0.9480179  0.90590477 0.854812   0.8665466 ]
 [0.93252915 0.8986135  0.8615557  0.86238515 0.8203217 ]
 [0.8903549  0.82918423 0.8541627  0.81799746 0.8431995 ]
 [0.81055236 0.82782495 0.80647886 0.8356404  0.8477283 ]
 [0.81087434 0.7973732  0.85038805 0.8538366  0.8220197 ]
 [0.78731334 0.8066845  0.854485   0.8193767  0.9147875 ]
 [0.81621754 0.86480933 0.8217528  0.9214308  0.95270836]
 [0.83122826 0.840271   0.9455011  0.9406134  1.0122143 ]
 [0.8563172  0.9351022  0.95125496 1.0084869  0.9943505 ]
 [0.89490634 0.92395836 1.005424   0.9600079  0.93174034]
 [0.93275344 0.99460673 0.97742814 0.93891364 0.89657986]
 [0.975363   0.9886523  0.9300108  0.89325523 0.83319104]
 [0.9721005  0.9302828  0.88676625 0.8349589  0.85458404]
 [0.9322446  0.89263195 0.8428587  0.84451467 0.81681365]
 [0.8988526  0.83966196 0.83932996 0.81638205 0.84993404]
 [0.8287593  0.8406942  0.8090937  0.8348619  0.857729  ]
 [0.83033574 0.81435287 0.8511938  0.86168295 0.82849807]
 [0.79753643 0.8168411  0.8579384  0.8249458  0.91502804]
 [0.8222305  0.8709316  0.8286525  0.92374617 0.952596  ]
 [0.8390177  0.8479024  0.95196784 0.9412538  1.0192626 ]
 [0.8581599  0.9315158  0.9548046  1.016778   1.0172982 ]
 [0.89139354 0.9226973  1.0169414  0.97234493 0.9574285 ]
 [0.92915845 0.9960932  0.99986374 0.9629573  0.9262144 ]
 [0.9792479  1.0058874  0.957432   0.92409915 0.86297077]
 [0.9842745  0.9584592  0.91303504 0.86194545 0.8719011 ]
 [0.9410578  0.9085324  0.86673594 0.86711234 0.8297949 ]]

  #### Plot     ############################################### 
Saved image to ztest/model_tch/nbeats//n_beats_test.png.

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git add --all &&  git commit -m "ml_store  && git pull --all"  ;            git push --all -f ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
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
[master ef59435] ml_store  && git pull --all
 1 file changed, 1121 insertions(+)
To github.com:arita37/mlmodels_store.git
   f8c53c4..ef59435  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//transformer_classifier.py 
Traceback (most recent call last):
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//transformer_classifier.py", line 522, in <module>
    model_pars, data_pars, compute_pars, out_pars = get_params(param_pars)
  File "/home/runner/work/mlmodels/mlmodels/mlmodels/model_tch//transformer_classifier.py", line 418, in get_params
    cf = json.load(open(data_path, mode='r'))
FileNotFoundError: [Errno 2] No such file or directory: 'model_tch/transformer_classifier.json'

   cd /home/runner/work/mlmodels/mlmodels_store/ ;            pip3 freeze > deps.txt ;            ls ;            git config --local user.email "noelkev0@gmail.com" && git config --local user.name "arita37"         ;            git add --all &&  git commit -m "ml_store  && git pull --all"  ;            git push --all -f ;            cd /home/runner/work/mlmodels/mlmodels/ ;         
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
