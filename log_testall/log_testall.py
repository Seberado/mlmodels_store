
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
[master 8454998] ml_store  && git pull --all
 2 files changed, 13 insertions(+), 90 deletions(-)
To github.com:arita37/mlmodels_store.git
 + 95241b7...8454998 master -> master (forced update)





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
[master ca57ce2] ml_store  && git pull --all
 1 file changed, 46 insertions(+)
Warning: Permanently added the RSA host key for IP address '140.82.113.3' to the list of known hosts.
To github.com:arita37/mlmodels_store.git
   8454998..ca57ce2  master -> master





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
sequence_sum (InputLayer)       [(None, 5)]          0                                            
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
linear0sparse_seq_emb_sequence_ (None, 5, 1)         6           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         8           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         7           sequence_max[0][0]               
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         4           sparse_feature_2[0][0]           
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
sparse_seq_emb_sequence_sum (Em (None, 5, 4)         24          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 2, 4)         32          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 9, 4)         28          sequence_max[0][0]               
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
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         32          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         16          sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer (Sequenc (None, 1, 4)         0           weighted_sequence_layer[0][0]    2020-05-24 04:15:07.793949: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2020-05-24 04:15:07.799720: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2294680000 Hz
2020-05-24 04:15:07.800501: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x55ba6533f1e0 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-24 04:15:07.800526: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version

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
Total params: 243
Trainable params: 243
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 1s - loss: 0.2500 - binary_crossentropy: 0.6931500/500 [==============================] - 1s 1ms/sample - loss: 0.2499 - binary_crossentropy: 0.6929 - val_loss: 0.2500 - val_binary_crossentropy: 0.6932

  #### metrics   #################################################### 
{'MSE': 0.24975834292867388}

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
sequence_sum (InputLayer)       [(None, 5)]          0                                            
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
linear0sparse_seq_emb_sequence_ (None, 5, 1)         6           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         8           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         7           sequence_max[0][0]               
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         4           sparse_feature_2[0][0]           
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
sparse_seq_emb_sequence_sum (Em (None, 5, 4)         24          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 2, 4)         32          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 9, 4)         28          sequence_max[0][0]               
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
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         32          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         16          sparse_feature_2[0][0]           
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
Total params: 243
Trainable params: 243
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
sequence_mean (InputLayer)      [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 6)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_3 (Weig (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 6, 4)         20          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 6, 4)         20          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 6, 4)         12          sequence_max[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         36          sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 6, 1)         5           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         5           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         3           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_5 (NoMask)              (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_12[0][0]  
                                                                 sequence_pooling_layer_13[0][0]  
                                                                 sequence_pooling_layer_14[0][0]  
                                                                 sequence_pooling_layer_15[0][0]  
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         9           sparse_feature_0[0][0]           
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
Total params: 458
Trainable params: 458
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 1s - loss: 0.2921 - binary_crossentropy: 0.7864500/500 [==============================] - 1s 2ms/sample - loss: 0.2790 - binary_crossentropy: 0.7574 - val_loss: 0.2876 - val_binary_crossentropy: 0.8023

  #### metrics   #################################################### 
{'MSE': 0.28236973155867234}

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
sequence_mean (InputLayer)      [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 6)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_3 (Weig (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 6, 4)         20          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 6, 4)         20          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 6, 4)         12          sequence_max[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_weighted_ (None, 3, 1)         2           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         36          sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 6, 1)         5           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         5           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         3           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_5 (NoMask)              (None, 1, 4)         0           sparse_emb_sparse_feature_0[0][0]
                                                                 sequence_pooling_layer_12[0][0]  
                                                                 sequence_pooling_layer_13[0][0]  
                                                                 sequence_pooling_layer_14[0][0]  
                                                                 sequence_pooling_layer_15[0][0]  
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         9           sparse_feature_0[0][0]           
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
Total params: 458
Trainable params: 458
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
sequence_sum (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 1)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 3, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 1, 4)         16          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 6, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         28          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         12          sparse_feature_1[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 3, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
conv2d_1 (Conv2D)               (None, 3, 4, 1)      5           k_max_pooling[0][0]              
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_1[0][0]           
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
Total params: 637
Trainable params: 637
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 2s - loss: 0.2500 - binary_crossentropy: 0.6931500/500 [==============================] - 1s 2ms/sample - loss: 0.2498 - binary_crossentropy: 0.6927 - val_loss: 0.2503 - val_binary_crossentropy: 0.6937

  #### metrics   #################################################### 
{'MSE': 0.24974877031266043}

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
sequence_sum (InputLayer)       [(None, 3)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 1)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 3, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 1, 4)         16          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 6, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         28          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         12          sparse_feature_1[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 3, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
conv2d_1 (Conv2D)               (None, 3, 4, 1)      5           k_max_pooling[0][0]              
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_1[0][0]           
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
Total params: 637
Trainable params: 637
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
sequence_mean (InputLayer)      [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 4)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 8, 4)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 5, 4)         24          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 4, 4)         4           sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         16          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         28          sparse_feature_1[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 8, 1)         1           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         6           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 4, 1)         1           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_4 (Flatten)             (None, 28)           0           concatenate_9[0][0]              
__________________________________________________________________________________________________
flatten_5 (Flatten)             (None, 3)            0           concatenate_10[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         4           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_1[0][0]           
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
Total params: 408
Trainable params: 408
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 2s - loss: 0.5400 - binary_crossentropy: 8.3295500/500 [==============================] - 2s 3ms/sample - loss: 0.5140 - binary_crossentropy: 7.9284 - val_loss: 0.5160 - val_binary_crossentropy: 7.9593

  #### metrics   #################################################### 
{'MSE': 0.515}

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
sequence_mean (InputLayer)      [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 4)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 8, 4)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 5, 4)         24          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 4, 4)         4           sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         16          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         28          sparse_feature_1[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 8, 1)         1           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         6           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 4, 1)         1           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_4 (Flatten)             (None, 28)           0           concatenate_9[0][0]              
__________________________________________________________________________________________________
flatten_5 (Flatten)             (None, 3)            0           concatenate_10[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         4           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_1[0][0]           
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
sequence_sum (InputLayer)       [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 1)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 5, 4)         16          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 1, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 1, 4)         4           sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 5, 1)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         7           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         1           sequence_max[0][0]               
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
Total params: 158
Trainable params: 158
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 3s - loss: 0.5400 - binary_crossentropy: 8.3295500/500 [==============================] - 2s 4ms/sample - loss: 0.5340 - binary_crossentropy: 8.2369 - val_loss: 0.4640 - val_binary_crossentropy: 7.1572

  #### metrics   #################################################### 
{'MSE': 0.499}

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
sequence_sum (InputLayer)       [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 1)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 5, 4)         16          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 1, 4)         28          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 1, 4)         4           sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 5, 1)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         7           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         1           sequence_max[0][0]               
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
Total params: 158
Trainable params: 158
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
dnn_4 (DNN)                     (None, 4)            152         concatenate_20[0][0]             2020-05-24 04:16:37.195334: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-24 04:16:37.197646: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-24 04:16:37.205609: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-24 04:16:37.218198: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-24 04:16:37.220154: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-24 04:16:37.222381: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-24 04:16:37.224174: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

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
1/1 [==============================] - 3s 3s/sample - loss: 0.2500 - binary_crossentropy: 0.6931 - val_loss: 0.2495 - val_binary_crossentropy: 0.6921
2020-05-24 04:16:38.742695: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-24 04:16:38.744904: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-24 04:16:38.749868: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-24 04:16:38.760001: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-24 04:16:38.762499: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-24 04:16:38.764215: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-24 04:16:38.765685: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

  #### metrics   #################################################### 
{'MSE': 0.24919553375677594}

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
2020-05-24 04:17:05.831190: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-24 04:17:05.832900: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-24 04:17:05.837147: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-24 04:17:05.844382: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-24 04:17:05.845541: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-24 04:17:05.846733: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-24 04:17:05.847878: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
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
1/1 [==============================] - 3s 3s/sample - loss: 0.2500 - binary_crossentropy: 0.6931 - val_loss: 0.2506 - val_binary_crossentropy: 0.6943
2020-05-24 04:17:07.601601: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-24 04:17:07.602712: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-24 04:17:07.606424: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-24 04:17:07.612760: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-24 04:17:07.614249: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-24 04:17:07.615335: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-24 04:17:07.616357: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

  #### metrics   #################################################### 
{'MSE': 0.2506463795893958}

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
concatenate_27 (Concatenate)    (None, 1, 16)        0           no_mask_36[0][0]                 2020-05-24 04:17:46.390055: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-24 04:17:46.395263: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-24 04:17:46.411805: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-24 04:17:46.439158: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-24 04:17:46.444853: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-24 04:17:46.449637: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-24 04:17:46.454328: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

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
1/1 [==============================] - 5s 5s/sample - loss: 0.7010 - binary_crossentropy: 1.8157 - val_loss: 0.2504 - val_binary_crossentropy: 0.6939
2020-05-24 04:17:48.990283: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-24 04:17:48.995181: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-24 04:17:49.008896: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-24 04:17:49.036677: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-24 04:17:49.040929: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-24 04:17:49.045659: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-24 04:17:49.049784: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

  #### metrics   #################################################### 
{'MSE': 0.25072634042965863}

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
sequence_mean (InputLayer)      [(None, 3)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 8, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 3, 4)         12          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 6, 4)         20          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         32          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         4           sparse_feature_1[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 8, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         3           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         5           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_48 (NoMask)             (None, 120)          0           flatten_19[0][0]                 
__________________________________________________________________________________________________
concatenate_39 (Concatenate)    (None, 2)            0           no_mask_49[0][0]                 
                                                                 no_mask_49[1][0]                 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         1           sparse_feature_1[0][0]           
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
Total params: 690
Trainable params: 690
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 7s - loss: 0.3056 - binary_crossentropy: 0.8205500/500 [==============================] - 5s 10ms/sample - loss: 0.2796 - binary_crossentropy: 0.7625 - val_loss: 0.2981 - val_binary_crossentropy: 0.8054

  #### metrics   #################################################### 
{'MSE': 0.2876758009737044}

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
sequence_mean (InputLayer)      [(None, 3)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 8, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 3, 4)         12          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 6, 4)         20          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         32          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         4           sparse_feature_1[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 8, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         3           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         5           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_48 (NoMask)             (None, 120)          0           flatten_19[0][0]                 
__________________________________________________________________________________________________
concatenate_39 (Concatenate)    (None, 2)            0           no_mask_49[0][0]                 
                                                                 no_mask_49[1][0]                 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         1           sparse_feature_1[0][0]           
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
Total params: 690
Trainable params: 690
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
sequence_sum (InputLayer)       [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 4)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 4)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 2, 2)         2           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 4, 2)         16          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 4, 2)         6           sequence_max[0][0]               
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
sparse_emb_sparse_feature_0 (Em (None, 1, 2)         6           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_3 (Em (None, 1, 2)         10          sparse_feature_3[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 2)         12          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_4 (Em (None, 1, 2)         8           sparse_feature_4[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 2)         8           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_5 (Em (None, 1, 2)         12          sparse_feature_5[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 2, 1)         1           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 4, 1)         8           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 4, 1)         3           sequence_max[0][0]               
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
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           sparse_feature_3[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         4           sparse_feature_4[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         4           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           sparse_feature_5[0][0]           
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
Total params: 233
Trainable params: 233
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 7s - loss: 0.2635 - binary_crossentropy: 0.7248500/500 [==============================] - 5s 10ms/sample - loss: 0.2709 - binary_crossentropy: 0.7934 - val_loss: 0.2647 - val_binary_crossentropy: 0.8555

  #### metrics   #################################################### 
{'MSE': 0.26318165606787847}

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
sequence_sum (InputLayer)       [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 4)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 4)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 2, 2)         2           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 4, 2)         16          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 4, 2)         6           sequence_max[0][0]               
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
sparse_emb_sparse_feature_0 (Em (None, 1, 2)         6           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_3 (Em (None, 1, 2)         10          sparse_feature_3[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 2)         12          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_4 (Em (None, 1, 2)         8           sparse_feature_4[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 2)         8           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_5 (Em (None, 1, 2)         12          sparse_feature_5[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 2, 1)         1           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 4, 1)         8           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 4, 1)         3           sequence_max[0][0]               
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
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           sparse_feature_3[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         4           sparse_feature_4[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         4           sparse_feature_2[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           sparse_feature_5[0][0]           
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
Total params: 233
Trainable params: 233
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
sequence_sum (InputLayer)       [(None, 7)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 7)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_21 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 7, 4)         24          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 5, 4)         20          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 7, 4)         4           sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 7, 1)         6           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         5           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 7, 1)         1           sequence_max[0][0]               
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
Total params: 1,869
Trainable params: 1,869
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 6s - loss: 0.4700 - binary_crossentropy: 7.2497500/500 [==============================] - 5s 10ms/sample - loss: 0.4900 - binary_crossentropy: 7.5582 - val_loss: 0.4440 - val_binary_crossentropy: 6.8487

  #### metrics   #################################################### 
{'MSE': 0.467}

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
sequence_sum (InputLayer)       [(None, 7)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 7)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_21 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 7, 4)         24          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 5, 4)         20          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 7, 4)         4           sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 7, 1)         6           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         5           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 7, 1)         1           sequence_max[0][0]               
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
Total params: 1,869
Trainable params: 1,869
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
regionsequence_mean (InputLayer [(None, 2)]          0                                            
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
region_10sparse_seq_emb_regions (None, 7, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 2, 1)         3           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 9, 1)         9           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_26 (Wei (None, 3, 1)         0           region_20sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 7, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 2, 1)         3           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 9, 1)         9           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_28 (Wei (None, 3, 1)         0           region_30sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 7, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 2, 1)         3           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 9, 1)         9           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_30 (Wei (None, 3, 1)         0           region_40sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 7, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 2, 1)         3           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 9, 1)         9           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_32 (Wei (None, 3, 1)         0           learner_10sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 7, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 2, 1)         3           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 9, 1)         9           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_34 (Wei (None, 3, 1)         0           learner_20sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 7, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 2, 1)         3           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 9, 1)         9           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_36 (Wei (None, 3, 1)         0           learner_30sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 7, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 2, 1)         3           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 9, 1)         9           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_38 (Wei (None, 3, 1)         0           learner_40sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 7, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 2, 1)         3           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 9, 1)         9           regionsequence_max[0][0]         
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
100/500 [=====>........................] - ETA: 9s - loss: 0.2518 - binary_crossentropy: 0.6965500/500 [==============================] - 6s 13ms/sample - loss: 0.2490 - binary_crossentropy: 0.6910 - val_loss: 0.2545 - val_binary_crossentropy: 0.7020

  #### metrics   #################################################### 
{'MSE': 0.25146868370117326}

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
regionsequence_mean (InputLayer [(None, 2)]          0                                            
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
region_10sparse_seq_emb_regions (None, 7, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 2, 1)         3           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 9, 1)         9           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_26 (Wei (None, 3, 1)         0           region_20sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 7, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 2, 1)         3           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 9, 1)         9           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_28 (Wei (None, 3, 1)         0           region_30sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 7, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 2, 1)         3           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 9, 1)         9           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_30 (Wei (None, 3, 1)         0           region_40sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 7, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 2, 1)         3           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 9, 1)         9           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_32 (Wei (None, 3, 1)         0           learner_10sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 7, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 2, 1)         3           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 9, 1)         9           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_34 (Wei (None, 3, 1)         0           learner_20sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 7, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 2, 1)         3           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 9, 1)         9           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_36 (Wei (None, 3, 1)         0           learner_30sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 7, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 2, 1)         3           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 9, 1)         9           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_38 (Wei (None, 3, 1)         0           learner_40sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 7, 1)         7           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 2, 1)         3           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 9, 1)         9           regionsequence_max[0][0]         
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
sequence_sum (InputLayer)       [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 9)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 9, 4)         16          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 9, 4)         12          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 1, 4)         16          sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 9, 1)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         3           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         4           sequence_max[0][0]               
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
Total params: 1,367
Trainable params: 1,367
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 8s - loss: 0.3588 - binary_crossentropy: 3.2724500/500 [==============================] - 6s 13ms/sample - loss: 0.3459 - binary_crossentropy: 2.7736 - val_loss: 0.3168 - val_binary_crossentropy: 2.4668

  #### metrics   #################################################### 
{'MSE': 0.3296591857291}

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
sequence_sum (InputLayer)       [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 9)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 9, 4)         16          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 9, 4)         12          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 1, 4)         16          sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 9, 1)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         3           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         4           sequence_max[0][0]               
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
Total params: 1,367
Trainable params: 1,367
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
sequence_max (InputLayer)       [(None, 2)]          0                                            
__________________________________________________________________________________________________
hash_19 (Hash)                  (None, 1)            0           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
hash_20 (Hash)                  (None, 1)            0           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
hash_21 (Hash)                  (None, 1)            0           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_spa (None, 1, 4)         20          hash_14[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_spa (None, 1, 4)         20          hash_15[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         20          hash_16[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 5, 4)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         20          hash_17[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 3, 4)         12          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         20          hash_18[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 2, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         20          hash_19[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 5, 4)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         20          hash_20[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 3, 4)         12          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         20          hash_21[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 2, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 5, 4)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 3, 4)         12          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 5, 4)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_max_sequenc (None, 2, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 3, 4)         12          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sequence_max_sequenc (None, 2, 4)         28          sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 5, 1)         1           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         3           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         7           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_29 (Flatten)            (None, 40)           0           no_mask_116[0][0]                
__________________________________________________________________________________________________
flatten_30 (Flatten)            (None, 2)            0           concatenate_81[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           hash_10[0][0]                    
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
Total params: 2,984
Trainable params: 2,904
Non-trainable params: 80
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 10s - loss: 0.3102 - binary_crossentropy: 1.0891500/500 [==============================] - 7s 14ms/sample - loss: 0.2869 - binary_crossentropy: 0.8808 - val_loss: 0.2857 - val_binary_crossentropy: 0.9006

  #### metrics   #################################################### 
{'MSE': 0.28477750435501653}

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
sequence_max (InputLayer)       [(None, 2)]          0                                            
__________________________________________________________________________________________________
hash_19 (Hash)                  (None, 1)            0           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
hash_20 (Hash)                  (None, 1)            0           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
hash_21 (Hash)                  (None, 1)            0           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_spa (None, 1, 4)         20          hash_14[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_spa (None, 1, 4)         20          hash_15[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         20          hash_16[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 5, 4)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         20          hash_17[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 3, 4)         12          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         20          hash_18[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 2, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         20          hash_19[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 5, 4)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         20          hash_20[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 3, 4)         12          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         20          hash_21[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 2, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 5, 4)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 3, 4)         12          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 5, 4)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_max_sequenc (None, 2, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 3, 4)         12          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sequence_max_sequenc (None, 2, 4)         28          sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 5, 1)         1           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         3           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         7           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_29 (Flatten)            (None, 40)           0           no_mask_116[0][0]                
__________________________________________________________________________________________________
flatten_30 (Flatten)            (None, 2)            0           concatenate_81[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           hash_10[0][0]                    
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
Total params: 2,984
Trainable params: 2,904
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
[master c27bff2] ml_store  && git pull --all
 1 file changed, 4946 insertions(+)
Warning: Permanently added the RSA host key for IP address '140.82.114.4' to the list of known hosts.
To github.com:arita37/mlmodels_store.git
 + 8fd3ef2...c27bff2 master -> master (forced update)





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
[master 34d2b15] ml_store  && git pull --all
 1 file changed, 50 insertions(+)
To github.com:arita37/mlmodels_store.git
   c27bff2..34d2b15  master -> master





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
[master bb4ce22] ml_store  && git pull --all
 1 file changed, 45 insertions(+)
To github.com:arita37/mlmodels_store.git
   34d2b15..bb4ce22  master -> master





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
[master ac6e2b0] ml_store  && git pull --all
 1 file changed, 34 insertions(+)
To github.com:arita37/mlmodels_store.git
   bb4ce22..ac6e2b0  master -> master





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
[master 82bf52d] ml_store  && git pull --all
 1 file changed, 47 insertions(+)
To github.com:arita37/mlmodels_store.git
   ac6e2b0..82bf52d  master -> master





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
[master 2b0bd1d] ml_store  && git pull --all
 1 file changed, 46 insertions(+)
Warning: Permanently added the RSA host key for IP address '140.82.114.3' to the list of known hosts.
To github.com:arita37/mlmodels_store.git
   82bf52d..2b0bd1d  master -> master





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
[master f529004] ml_store  && git pull --all
 1 file changed, 44 insertions(+)
To github.com:arita37/mlmodels_store.git
   2b0bd1d..f529004  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//textcnn.py 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Loading dataset   ############################################# 
Loading data...
Downloading data from https://s3.amazonaws.com/text-datasets/imdb.npz

    8192/17464789 [..............................] - ETA: 0s
 3620864/17464789 [=====>........................] - ETA: 0s
 8503296/17464789 [=============>................] - ETA: 0s
12607488/17464789 [====================>.........] - ETA: 0s
16818176/17464789 [===========================>..] - ETA: 0s
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
2020-05-24 04:28:39.828464: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2020-05-24 04:28:39.832888: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2294680000 Hz
2020-05-24 04:28:39.833084: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x555ef731b960 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-24 04:28:39.833100: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
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

 1000/25000 [>.............................] - ETA: 13s - loss: 7.8660 - accuracy: 0.4870
 2000/25000 [=>............................] - ETA: 10s - loss: 7.5823 - accuracy: 0.5055
 3000/25000 [==>...........................] - ETA: 8s - loss: 7.7075 - accuracy: 0.4973 
 4000/25000 [===>..........................] - ETA: 7s - loss: 7.8621 - accuracy: 0.4873
 5000/25000 [=====>........................] - ETA: 7s - loss: 7.8506 - accuracy: 0.4880
 6000/25000 [======>.......................] - ETA: 6s - loss: 7.8353 - accuracy: 0.4890
 7000/25000 [=======>......................] - ETA: 6s - loss: 7.8725 - accuracy: 0.4866
 8000/25000 [========>.....................] - ETA: 5s - loss: 7.7797 - accuracy: 0.4926
 9000/25000 [=========>....................] - ETA: 5s - loss: 7.7944 - accuracy: 0.4917
10000/25000 [===========>..................] - ETA: 5s - loss: 7.7694 - accuracy: 0.4933
11000/25000 [============>.................] - ETA: 4s - loss: 7.7405 - accuracy: 0.4952
12000/25000 [=============>................] - ETA: 4s - loss: 7.7382 - accuracy: 0.4953
13000/25000 [==============>...............] - ETA: 3s - loss: 7.7539 - accuracy: 0.4943
14000/25000 [===============>..............] - ETA: 3s - loss: 7.7203 - accuracy: 0.4965
15000/25000 [=================>............] - ETA: 3s - loss: 7.7259 - accuracy: 0.4961
16000/25000 [==================>...........] - ETA: 2s - loss: 7.7050 - accuracy: 0.4975
17000/25000 [===================>..........] - ETA: 2s - loss: 7.6955 - accuracy: 0.4981
18000/25000 [====================>.........] - ETA: 2s - loss: 7.7007 - accuracy: 0.4978
19000/25000 [=====================>........] - ETA: 1s - loss: 7.6949 - accuracy: 0.4982
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6904 - accuracy: 0.4985
21000/25000 [========================>.....] - ETA: 1s - loss: 7.6958 - accuracy: 0.4981
22000/25000 [=========================>....] - ETA: 0s - loss: 7.6722 - accuracy: 0.4996
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6766 - accuracy: 0.4993
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6717 - accuracy: 0.4997
25000/25000 [==============================] - 10s 395us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000

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
(<mlmodels.util.Model_empty object at 0x7f3a49a0c9e8>, None)

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

  <mlmodels.model_keras.textcnn.Model object at 0x7f3a42e90cc0> 

  #### Fit   ######################################################## 
Loading data...
Pad sequences (samples x time)...
Train on 25000 samples, validate on 25000 samples
Epoch 1/1

 1000/25000 [>.............................] - ETA: 13s - loss: 7.5746 - accuracy: 0.5060
 2000/25000 [=>............................] - ETA: 10s - loss: 7.6283 - accuracy: 0.5025
 3000/25000 [==>...........................] - ETA: 8s - loss: 7.7024 - accuracy: 0.4977 
 4000/25000 [===>..........................] - ETA: 7s - loss: 7.5670 - accuracy: 0.5065
 5000/25000 [=====>........................] - ETA: 7s - loss: 7.6758 - accuracy: 0.4994
 6000/25000 [======>.......................] - ETA: 6s - loss: 7.6922 - accuracy: 0.4983
 7000/25000 [=======>......................] - ETA: 6s - loss: 7.7017 - accuracy: 0.4977
 8000/25000 [========>.....................] - ETA: 5s - loss: 7.6724 - accuracy: 0.4996
 9000/25000 [=========>....................] - ETA: 5s - loss: 7.6206 - accuracy: 0.5030
10000/25000 [===========>..................] - ETA: 5s - loss: 7.6360 - accuracy: 0.5020
11000/25000 [============>.................] - ETA: 4s - loss: 7.6429 - accuracy: 0.5015
12000/25000 [=============>................] - ETA: 4s - loss: 7.6372 - accuracy: 0.5019
13000/25000 [==============>...............] - ETA: 3s - loss: 7.6395 - accuracy: 0.5018
14000/25000 [===============>..............] - ETA: 3s - loss: 7.6316 - accuracy: 0.5023
15000/25000 [=================>............] - ETA: 3s - loss: 7.6380 - accuracy: 0.5019
16000/25000 [==================>...........] - ETA: 2s - loss: 7.6292 - accuracy: 0.5024
17000/25000 [===================>..........] - ETA: 2s - loss: 7.6323 - accuracy: 0.5022
18000/25000 [====================>.........] - ETA: 2s - loss: 7.6257 - accuracy: 0.5027
19000/25000 [=====================>........] - ETA: 1s - loss: 7.6497 - accuracy: 0.5011
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6720 - accuracy: 0.4997
21000/25000 [========================>.....] - ETA: 1s - loss: 7.6871 - accuracy: 0.4987
22000/25000 [=========================>....] - ETA: 0s - loss: 7.6868 - accuracy: 0.4987
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6706 - accuracy: 0.4997
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6545 - accuracy: 0.5008
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

 1000/25000 [>.............................] - ETA: 13s - loss: 7.8200 - accuracy: 0.4900
 2000/25000 [=>............................] - ETA: 10s - loss: 7.7203 - accuracy: 0.4965
 3000/25000 [==>...........................] - ETA: 8s - loss: 7.7893 - accuracy: 0.4920 
 4000/25000 [===>..........................] - ETA: 7s - loss: 7.7778 - accuracy: 0.4927
 5000/25000 [=====>........................] - ETA: 7s - loss: 7.7648 - accuracy: 0.4936
 6000/25000 [======>.......................] - ETA: 6s - loss: 7.7458 - accuracy: 0.4948
 7000/25000 [=======>......................] - ETA: 6s - loss: 7.6622 - accuracy: 0.5003
 8000/25000 [========>.....................] - ETA: 5s - loss: 7.6762 - accuracy: 0.4994
 9000/25000 [=========>....................] - ETA: 5s - loss: 7.6666 - accuracy: 0.5000
10000/25000 [===========>..................] - ETA: 5s - loss: 7.6421 - accuracy: 0.5016
11000/25000 [============>.................] - ETA: 4s - loss: 7.6778 - accuracy: 0.4993
12000/25000 [=============>................] - ETA: 4s - loss: 7.6538 - accuracy: 0.5008
13000/25000 [==============>...............] - ETA: 3s - loss: 7.6607 - accuracy: 0.5004
14000/25000 [===============>..............] - ETA: 3s - loss: 7.6513 - accuracy: 0.5010
15000/25000 [=================>............] - ETA: 3s - loss: 7.6574 - accuracy: 0.5006
16000/25000 [==================>...........] - ETA: 2s - loss: 7.6609 - accuracy: 0.5004
17000/25000 [===================>..........] - ETA: 2s - loss: 7.6603 - accuracy: 0.5004
18000/25000 [====================>.........] - ETA: 2s - loss: 7.6487 - accuracy: 0.5012
19000/25000 [=====================>........] - ETA: 1s - loss: 7.6247 - accuracy: 0.5027
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6268 - accuracy: 0.5026
21000/25000 [========================>.....] - ETA: 1s - loss: 7.6338 - accuracy: 0.5021
22000/25000 [=========================>....] - ETA: 0s - loss: 7.6283 - accuracy: 0.5025
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6440 - accuracy: 0.5015
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6526 - accuracy: 0.5009
25000/25000 [==============================] - 10s 397us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000
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
[master 6a5c679] ml_store  && git pull --all
 1 file changed, 317 insertions(+)
Warning: Permanently added the RSA host key for IP address '140.82.112.4' to the list of known hosts.
To github.com:arita37/mlmodels_store.git
 + 73898eb...6a5c679 master -> master (forced update)





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

13/13 [==============================] - 2s 126ms/step - loss: nan
Epoch 2/10

13/13 [==============================] - 0s 6ms/step - loss: nan
Epoch 3/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 4/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 5/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 6/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 7/10

13/13 [==============================] - 0s 5ms/step - loss: nan
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
[master b923674] ml_store  && git pull --all
 1 file changed, 125 insertions(+)
To github.com:arita37/mlmodels_store.git
   6a5c679..b923674  master -> master





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
 4177920/11490434 [=========>....................] - ETA: 0s
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

   32/60000 [..............................] - ETA: 7:56 - loss: 2.3009 - categorical_accuracy: 0.0938
   64/60000 [..............................] - ETA: 4:59 - loss: 2.2821 - categorical_accuracy: 0.1562
   96/60000 [..............................] - ETA: 3:59 - loss: 2.2184 - categorical_accuracy: 0.2083
  128/60000 [..............................] - ETA: 3:27 - loss: 2.1800 - categorical_accuracy: 0.2188
  160/60000 [..............................] - ETA: 3:08 - loss: 2.2004 - categorical_accuracy: 0.2125
  192/60000 [..............................] - ETA: 2:56 - loss: 2.1870 - categorical_accuracy: 0.2396
  224/60000 [..............................] - ETA: 2:47 - loss: 2.1384 - categorical_accuracy: 0.2723
  256/60000 [..............................] - ETA: 2:40 - loss: 2.0999 - categorical_accuracy: 0.2930
  288/60000 [..............................] - ETA: 2:35 - loss: 2.0627 - categorical_accuracy: 0.3056
  320/60000 [..............................] - ETA: 2:31 - loss: 2.0240 - categorical_accuracy: 0.3156
  352/60000 [..............................] - ETA: 2:27 - loss: 1.9760 - categorical_accuracy: 0.3324
  384/60000 [..............................] - ETA: 2:24 - loss: 1.9572 - categorical_accuracy: 0.3438
  416/60000 [..............................] - ETA: 2:23 - loss: 1.9318 - categorical_accuracy: 0.3510
  448/60000 [..............................] - ETA: 2:20 - loss: 1.8881 - categorical_accuracy: 0.3705
  480/60000 [..............................] - ETA: 2:18 - loss: 1.8484 - categorical_accuracy: 0.3875
  512/60000 [..............................] - ETA: 2:17 - loss: 1.8338 - categorical_accuracy: 0.3906
  544/60000 [..............................] - ETA: 2:16 - loss: 1.8210 - categorical_accuracy: 0.3989
  576/60000 [..............................] - ETA: 2:14 - loss: 1.7924 - categorical_accuracy: 0.4080
  608/60000 [..............................] - ETA: 2:13 - loss: 1.7640 - categorical_accuracy: 0.4194
  640/60000 [..............................] - ETA: 2:12 - loss: 1.7225 - categorical_accuracy: 0.4313
  672/60000 [..............................] - ETA: 2:11 - loss: 1.6819 - categorical_accuracy: 0.4464
  704/60000 [..............................] - ETA: 2:10 - loss: 1.6606 - categorical_accuracy: 0.4545
  736/60000 [..............................] - ETA: 2:09 - loss: 1.6503 - categorical_accuracy: 0.4565
  768/60000 [..............................] - ETA: 2:08 - loss: 1.6301 - categorical_accuracy: 0.4635
  800/60000 [..............................] - ETA: 2:07 - loss: 1.5986 - categorical_accuracy: 0.4712
  832/60000 [..............................] - ETA: 2:07 - loss: 1.5816 - categorical_accuracy: 0.4772
  864/60000 [..............................] - ETA: 2:06 - loss: 1.5668 - categorical_accuracy: 0.4815
  896/60000 [..............................] - ETA: 2:05 - loss: 1.5530 - categorical_accuracy: 0.4877
  928/60000 [..............................] - ETA: 2:05 - loss: 1.5435 - categorical_accuracy: 0.4935
  960/60000 [..............................] - ETA: 2:04 - loss: 1.5268 - categorical_accuracy: 0.5010
  992/60000 [..............................] - ETA: 2:04 - loss: 1.5099 - categorical_accuracy: 0.5060
 1024/60000 [..............................] - ETA: 2:04 - loss: 1.4875 - categorical_accuracy: 0.5127
 1056/60000 [..............................] - ETA: 2:04 - loss: 1.4587 - categorical_accuracy: 0.5237
 1088/60000 [..............................] - ETA: 2:03 - loss: 1.4505 - categorical_accuracy: 0.5248
 1120/60000 [..............................] - ETA: 2:03 - loss: 1.4299 - categorical_accuracy: 0.5312
 1152/60000 [..............................] - ETA: 2:02 - loss: 1.4099 - categorical_accuracy: 0.5391
 1184/60000 [..............................] - ETA: 2:02 - loss: 1.3959 - categorical_accuracy: 0.5456
 1216/60000 [..............................] - ETA: 2:02 - loss: 1.3749 - categorical_accuracy: 0.5526
 1248/60000 [..............................] - ETA: 2:01 - loss: 1.3593 - categorical_accuracy: 0.5577
 1280/60000 [..............................] - ETA: 2:01 - loss: 1.3415 - categorical_accuracy: 0.5633
 1312/60000 [..............................] - ETA: 2:01 - loss: 1.3278 - categorical_accuracy: 0.5678
 1344/60000 [..............................] - ETA: 2:01 - loss: 1.3153 - categorical_accuracy: 0.5714
 1376/60000 [..............................] - ETA: 2:00 - loss: 1.2983 - categorical_accuracy: 0.5756
 1408/60000 [..............................] - ETA: 2:00 - loss: 1.2829 - categorical_accuracy: 0.5788
 1440/60000 [..............................] - ETA: 2:00 - loss: 1.2692 - categorical_accuracy: 0.5826
 1472/60000 [..............................] - ETA: 2:00 - loss: 1.2520 - categorical_accuracy: 0.5876
 1504/60000 [..............................] - ETA: 1:59 - loss: 1.2391 - categorical_accuracy: 0.5931
 1536/60000 [..............................] - ETA: 1:59 - loss: 1.2241 - categorical_accuracy: 0.5977
 1568/60000 [..............................] - ETA: 1:59 - loss: 1.2203 - categorical_accuracy: 0.5969
 1600/60000 [..............................] - ETA: 1:59 - loss: 1.2119 - categorical_accuracy: 0.5994
 1632/60000 [..............................] - ETA: 1:59 - loss: 1.2012 - categorical_accuracy: 0.6029
 1664/60000 [..............................] - ETA: 1:59 - loss: 1.1885 - categorical_accuracy: 0.6064
 1696/60000 [..............................] - ETA: 1:58 - loss: 1.1809 - categorical_accuracy: 0.6085
 1728/60000 [..............................] - ETA: 1:58 - loss: 1.1698 - categorical_accuracy: 0.6111
 1760/60000 [..............................] - ETA: 1:58 - loss: 1.1562 - categorical_accuracy: 0.6165
 1792/60000 [..............................] - ETA: 1:58 - loss: 1.1451 - categorical_accuracy: 0.6217
 1824/60000 [..............................] - ETA: 1:58 - loss: 1.1319 - categorical_accuracy: 0.6261
 1856/60000 [..............................] - ETA: 1:58 - loss: 1.1207 - categorical_accuracy: 0.6298
 1888/60000 [..............................] - ETA: 1:58 - loss: 1.1118 - categorical_accuracy: 0.6329
 1920/60000 [..............................] - ETA: 1:58 - loss: 1.1015 - categorical_accuracy: 0.6365
 1952/60000 [..............................] - ETA: 1:57 - loss: 1.0964 - categorical_accuracy: 0.6393
 1984/60000 [..............................] - ETA: 1:58 - loss: 1.0923 - categorical_accuracy: 0.6396
 2016/60000 [>.............................] - ETA: 1:57 - loss: 1.0829 - categorical_accuracy: 0.6429
 2048/60000 [>.............................] - ETA: 1:57 - loss: 1.0733 - categorical_accuracy: 0.6450
 2080/60000 [>.............................] - ETA: 1:57 - loss: 1.0662 - categorical_accuracy: 0.6481
 2112/60000 [>.............................] - ETA: 1:57 - loss: 1.0579 - categorical_accuracy: 0.6501
 2144/60000 [>.............................] - ETA: 1:57 - loss: 1.0520 - categorical_accuracy: 0.6525
 2176/60000 [>.............................] - ETA: 1:56 - loss: 1.0434 - categorical_accuracy: 0.6562
 2208/60000 [>.............................] - ETA: 1:56 - loss: 1.0426 - categorical_accuracy: 0.6558
 2240/60000 [>.............................] - ETA: 1:56 - loss: 1.0341 - categorical_accuracy: 0.6594
 2272/60000 [>.............................] - ETA: 1:56 - loss: 1.0253 - categorical_accuracy: 0.6629
 2304/60000 [>.............................] - ETA: 1:56 - loss: 1.0202 - categorical_accuracy: 0.6654
 2336/60000 [>.............................] - ETA: 1:55 - loss: 1.0175 - categorical_accuracy: 0.6652
 2368/60000 [>.............................] - ETA: 1:55 - loss: 1.0114 - categorical_accuracy: 0.6677
 2400/60000 [>.............................] - ETA: 1:55 - loss: 1.0030 - categorical_accuracy: 0.6708
 2432/60000 [>.............................] - ETA: 1:55 - loss: 0.9945 - categorical_accuracy: 0.6731
 2464/60000 [>.............................] - ETA: 1:55 - loss: 0.9868 - categorical_accuracy: 0.6757
 2496/60000 [>.............................] - ETA: 1:55 - loss: 0.9803 - categorical_accuracy: 0.6771
 2528/60000 [>.............................] - ETA: 1:55 - loss: 0.9745 - categorical_accuracy: 0.6788
 2560/60000 [>.............................] - ETA: 1:54 - loss: 0.9664 - categorical_accuracy: 0.6816
 2592/60000 [>.............................] - ETA: 1:54 - loss: 0.9603 - categorical_accuracy: 0.6840
 2624/60000 [>.............................] - ETA: 1:54 - loss: 0.9553 - categorical_accuracy: 0.6852
 2656/60000 [>.............................] - ETA: 1:54 - loss: 0.9546 - categorical_accuracy: 0.6849
 2688/60000 [>.............................] - ETA: 1:54 - loss: 0.9516 - categorical_accuracy: 0.6864
 2720/60000 [>.............................] - ETA: 1:54 - loss: 0.9487 - categorical_accuracy: 0.6868
 2752/60000 [>.............................] - ETA: 1:53 - loss: 0.9414 - categorical_accuracy: 0.6893
 2784/60000 [>.............................] - ETA: 1:53 - loss: 0.9360 - categorical_accuracy: 0.6915
 2816/60000 [>.............................] - ETA: 1:53 - loss: 0.9284 - categorical_accuracy: 0.6935
 2848/60000 [>.............................] - ETA: 1:53 - loss: 0.9224 - categorical_accuracy: 0.6956
 2880/60000 [>.............................] - ETA: 1:53 - loss: 0.9174 - categorical_accuracy: 0.6972
 2912/60000 [>.............................] - ETA: 1:53 - loss: 0.9101 - categorical_accuracy: 0.7002
 2944/60000 [>.............................] - ETA: 1:53 - loss: 0.9072 - categorical_accuracy: 0.7021
 2976/60000 [>.............................] - ETA: 1:53 - loss: 0.9036 - categorical_accuracy: 0.7033
 3008/60000 [>.............................] - ETA: 1:53 - loss: 0.8980 - categorical_accuracy: 0.7051
 3040/60000 [>.............................] - ETA: 1:52 - loss: 0.8945 - categorical_accuracy: 0.7063
 3072/60000 [>.............................] - ETA: 1:52 - loss: 0.8905 - categorical_accuracy: 0.7074
 3104/60000 [>.............................] - ETA: 1:52 - loss: 0.8833 - categorical_accuracy: 0.7094
 3136/60000 [>.............................] - ETA: 1:52 - loss: 0.8794 - categorical_accuracy: 0.7114
 3168/60000 [>.............................] - ETA: 1:52 - loss: 0.8767 - categorical_accuracy: 0.7121
 3200/60000 [>.............................] - ETA: 1:52 - loss: 0.8694 - categorical_accuracy: 0.7147
 3232/60000 [>.............................] - ETA: 1:52 - loss: 0.8639 - categorical_accuracy: 0.7160
 3264/60000 [>.............................] - ETA: 1:52 - loss: 0.8609 - categorical_accuracy: 0.7178
 3296/60000 [>.............................] - ETA: 1:52 - loss: 0.8580 - categorical_accuracy: 0.7191
 3328/60000 [>.............................] - ETA: 1:51 - loss: 0.8541 - categorical_accuracy: 0.7203
 3360/60000 [>.............................] - ETA: 1:51 - loss: 0.8492 - categorical_accuracy: 0.7223
 3392/60000 [>.............................] - ETA: 1:51 - loss: 0.8454 - categorical_accuracy: 0.7238
 3424/60000 [>.............................] - ETA: 1:51 - loss: 0.8398 - categorical_accuracy: 0.7261
 3456/60000 [>.............................] - ETA: 1:51 - loss: 0.8364 - categorical_accuracy: 0.7274
 3488/60000 [>.............................] - ETA: 1:51 - loss: 0.8310 - categorical_accuracy: 0.7291
 3520/60000 [>.............................] - ETA: 1:51 - loss: 0.8268 - categorical_accuracy: 0.7307
 3552/60000 [>.............................] - ETA: 1:51 - loss: 0.8214 - categorical_accuracy: 0.7325
 3584/60000 [>.............................] - ETA: 1:51 - loss: 0.8162 - categorical_accuracy: 0.7344
 3616/60000 [>.............................] - ETA: 1:51 - loss: 0.8158 - categorical_accuracy: 0.7351
 3648/60000 [>.............................] - ETA: 1:51 - loss: 0.8152 - categorical_accuracy: 0.7360
 3680/60000 [>.............................] - ETA: 1:51 - loss: 0.8122 - categorical_accuracy: 0.7375
 3712/60000 [>.............................] - ETA: 1:51 - loss: 0.8080 - categorical_accuracy: 0.7390
 3744/60000 [>.............................] - ETA: 1:51 - loss: 0.8038 - categorical_accuracy: 0.7401
 3776/60000 [>.............................] - ETA: 1:50 - loss: 0.7999 - categorical_accuracy: 0.7413
 3808/60000 [>.............................] - ETA: 1:50 - loss: 0.7965 - categorical_accuracy: 0.7421
 3840/60000 [>.............................] - ETA: 1:50 - loss: 0.7947 - categorical_accuracy: 0.7430
 3872/60000 [>.............................] - ETA: 1:50 - loss: 0.7919 - categorical_accuracy: 0.7435
 3904/60000 [>.............................] - ETA: 1:50 - loss: 0.7884 - categorical_accuracy: 0.7446
 3936/60000 [>.............................] - ETA: 1:50 - loss: 0.7853 - categorical_accuracy: 0.7449
 3968/60000 [>.............................] - ETA: 1:50 - loss: 0.7810 - categorical_accuracy: 0.7462
 4000/60000 [=>............................] - ETA: 1:50 - loss: 0.7764 - categorical_accuracy: 0.7475
 4032/60000 [=>............................] - ETA: 1:50 - loss: 0.7730 - categorical_accuracy: 0.7490
 4064/60000 [=>............................] - ETA: 1:50 - loss: 0.7706 - categorical_accuracy: 0.7500
 4096/60000 [=>............................] - ETA: 1:50 - loss: 0.7697 - categorical_accuracy: 0.7505
 4128/60000 [=>............................] - ETA: 1:49 - loss: 0.7654 - categorical_accuracy: 0.7524
 4160/60000 [=>............................] - ETA: 1:49 - loss: 0.7633 - categorical_accuracy: 0.7531
 4192/60000 [=>............................] - ETA: 1:49 - loss: 0.7601 - categorical_accuracy: 0.7541
 4224/60000 [=>............................] - ETA: 1:49 - loss: 0.7580 - categorical_accuracy: 0.7547
 4256/60000 [=>............................] - ETA: 1:49 - loss: 0.7543 - categorical_accuracy: 0.7556
 4288/60000 [=>............................] - ETA: 1:49 - loss: 0.7501 - categorical_accuracy: 0.7570
 4320/60000 [=>............................] - ETA: 1:49 - loss: 0.7459 - categorical_accuracy: 0.7583
 4352/60000 [=>............................] - ETA: 1:49 - loss: 0.7424 - categorical_accuracy: 0.7594
 4384/60000 [=>............................] - ETA: 1:49 - loss: 0.7426 - categorical_accuracy: 0.7594
 4416/60000 [=>............................] - ETA: 1:49 - loss: 0.7407 - categorical_accuracy: 0.7595
 4448/60000 [=>............................] - ETA: 1:49 - loss: 0.7398 - categorical_accuracy: 0.7601
 4480/60000 [=>............................] - ETA: 1:48 - loss: 0.7375 - categorical_accuracy: 0.7603
 4512/60000 [=>............................] - ETA: 1:48 - loss: 0.7335 - categorical_accuracy: 0.7617
 4544/60000 [=>............................] - ETA: 1:48 - loss: 0.7309 - categorical_accuracy: 0.7623
 4576/60000 [=>............................] - ETA: 1:48 - loss: 0.7275 - categorical_accuracy: 0.7635
 4608/60000 [=>............................] - ETA: 1:48 - loss: 0.7255 - categorical_accuracy: 0.7645
 4640/60000 [=>............................] - ETA: 1:48 - loss: 0.7211 - categorical_accuracy: 0.7662
 4672/60000 [=>............................] - ETA: 1:48 - loss: 0.7216 - categorical_accuracy: 0.7665
 4704/60000 [=>............................] - ETA: 1:48 - loss: 0.7178 - categorical_accuracy: 0.7681
 4736/60000 [=>............................] - ETA: 1:48 - loss: 0.7144 - categorical_accuracy: 0.7692
 4768/60000 [=>............................] - ETA: 1:48 - loss: 0.7118 - categorical_accuracy: 0.7703
 4800/60000 [=>............................] - ETA: 1:48 - loss: 0.7087 - categorical_accuracy: 0.7715
 4832/60000 [=>............................] - ETA: 1:48 - loss: 0.7093 - categorical_accuracy: 0.7711
 4864/60000 [=>............................] - ETA: 1:48 - loss: 0.7078 - categorical_accuracy: 0.7720
 4896/60000 [=>............................] - ETA: 1:48 - loss: 0.7041 - categorical_accuracy: 0.7731
 4928/60000 [=>............................] - ETA: 1:47 - loss: 0.7022 - categorical_accuracy: 0.7733
 4960/60000 [=>............................] - ETA: 1:47 - loss: 0.6990 - categorical_accuracy: 0.7742
 4992/60000 [=>............................] - ETA: 1:47 - loss: 0.6967 - categorical_accuracy: 0.7750
 5024/60000 [=>............................] - ETA: 1:47 - loss: 0.6951 - categorical_accuracy: 0.7759
 5056/60000 [=>............................] - ETA: 1:47 - loss: 0.6928 - categorical_accuracy: 0.7765
 5088/60000 [=>............................] - ETA: 1:47 - loss: 0.6898 - categorical_accuracy: 0.7777
 5120/60000 [=>............................] - ETA: 1:47 - loss: 0.6866 - categorical_accuracy: 0.7789
 5152/60000 [=>............................] - ETA: 1:47 - loss: 0.6840 - categorical_accuracy: 0.7797
 5184/60000 [=>............................] - ETA: 1:47 - loss: 0.6830 - categorical_accuracy: 0.7803
 5216/60000 [=>............................] - ETA: 1:47 - loss: 0.6812 - categorical_accuracy: 0.7811
 5248/60000 [=>............................] - ETA: 1:47 - loss: 0.6805 - categorical_accuracy: 0.7814
 5280/60000 [=>............................] - ETA: 1:47 - loss: 0.6786 - categorical_accuracy: 0.7820
 5312/60000 [=>............................] - ETA: 1:47 - loss: 0.6759 - categorical_accuracy: 0.7828
 5344/60000 [=>............................] - ETA: 1:46 - loss: 0.6734 - categorical_accuracy: 0.7837
 5376/60000 [=>............................] - ETA: 1:46 - loss: 0.6723 - categorical_accuracy: 0.7846
 5408/60000 [=>............................] - ETA: 1:46 - loss: 0.6699 - categorical_accuracy: 0.7853
 5440/60000 [=>............................] - ETA: 1:46 - loss: 0.6674 - categorical_accuracy: 0.7860
 5472/60000 [=>............................] - ETA: 1:46 - loss: 0.6667 - categorical_accuracy: 0.7862
 5504/60000 [=>............................] - ETA: 1:46 - loss: 0.6645 - categorical_accuracy: 0.7871
 5536/60000 [=>............................] - ETA: 1:46 - loss: 0.6624 - categorical_accuracy: 0.7878
 5568/60000 [=>............................] - ETA: 1:46 - loss: 0.6596 - categorical_accuracy: 0.7888
 5600/60000 [=>............................] - ETA: 1:46 - loss: 0.6577 - categorical_accuracy: 0.7893
 5632/60000 [=>............................] - ETA: 1:46 - loss: 0.6548 - categorical_accuracy: 0.7900
 5664/60000 [=>............................] - ETA: 1:46 - loss: 0.6531 - categorical_accuracy: 0.7908
 5696/60000 [=>............................] - ETA: 1:46 - loss: 0.6504 - categorical_accuracy: 0.7918
 5728/60000 [=>............................] - ETA: 1:46 - loss: 0.6482 - categorical_accuracy: 0.7924
 5760/60000 [=>............................] - ETA: 1:45 - loss: 0.6461 - categorical_accuracy: 0.7931
 5792/60000 [=>............................] - ETA: 1:45 - loss: 0.6446 - categorical_accuracy: 0.7935
 5824/60000 [=>............................] - ETA: 1:45 - loss: 0.6423 - categorical_accuracy: 0.7943
 5856/60000 [=>............................] - ETA: 1:45 - loss: 0.6395 - categorical_accuracy: 0.7953
 5888/60000 [=>............................] - ETA: 1:45 - loss: 0.6371 - categorical_accuracy: 0.7960
 5920/60000 [=>............................] - ETA: 1:45 - loss: 0.6365 - categorical_accuracy: 0.7966
 5952/60000 [=>............................] - ETA: 1:45 - loss: 0.6338 - categorical_accuracy: 0.7975
 5984/60000 [=>............................] - ETA: 1:45 - loss: 0.6312 - categorical_accuracy: 0.7985
 6016/60000 [==>...........................] - ETA: 1:45 - loss: 0.6303 - categorical_accuracy: 0.7989
 6048/60000 [==>...........................] - ETA: 1:45 - loss: 0.6290 - categorical_accuracy: 0.7994
 6080/60000 [==>...........................] - ETA: 1:45 - loss: 0.6270 - categorical_accuracy: 0.8003
 6112/60000 [==>...........................] - ETA: 1:45 - loss: 0.6245 - categorical_accuracy: 0.8010
 6144/60000 [==>...........................] - ETA: 1:45 - loss: 0.6222 - categorical_accuracy: 0.8014
 6176/60000 [==>...........................] - ETA: 1:45 - loss: 0.6206 - categorical_accuracy: 0.8018
 6208/60000 [==>...........................] - ETA: 1:44 - loss: 0.6190 - categorical_accuracy: 0.8024
 6240/60000 [==>...........................] - ETA: 1:44 - loss: 0.6182 - categorical_accuracy: 0.8027
 6272/60000 [==>...........................] - ETA: 1:44 - loss: 0.6168 - categorical_accuracy: 0.8034
 6304/60000 [==>...........................] - ETA: 1:44 - loss: 0.6157 - categorical_accuracy: 0.8039
 6336/60000 [==>...........................] - ETA: 1:44 - loss: 0.6133 - categorical_accuracy: 0.8046
 6368/60000 [==>...........................] - ETA: 1:44 - loss: 0.6109 - categorical_accuracy: 0.8056
 6400/60000 [==>...........................] - ETA: 1:44 - loss: 0.6101 - categorical_accuracy: 0.8062
 6432/60000 [==>...........................] - ETA: 1:44 - loss: 0.6081 - categorical_accuracy: 0.8067
 6464/60000 [==>...........................] - ETA: 1:44 - loss: 0.6061 - categorical_accuracy: 0.8074
 6496/60000 [==>...........................] - ETA: 1:44 - loss: 0.6055 - categorical_accuracy: 0.8076
 6528/60000 [==>...........................] - ETA: 1:44 - loss: 0.6047 - categorical_accuracy: 0.8078
 6560/60000 [==>...........................] - ETA: 1:44 - loss: 0.6055 - categorical_accuracy: 0.8076
 6592/60000 [==>...........................] - ETA: 1:44 - loss: 0.6029 - categorical_accuracy: 0.8086
 6624/60000 [==>...........................] - ETA: 1:44 - loss: 0.6016 - categorical_accuracy: 0.8090
 6656/60000 [==>...........................] - ETA: 1:44 - loss: 0.6000 - categorical_accuracy: 0.8098
 6688/60000 [==>...........................] - ETA: 1:43 - loss: 0.5987 - categorical_accuracy: 0.8103
 6720/60000 [==>...........................] - ETA: 1:43 - loss: 0.5974 - categorical_accuracy: 0.8106
 6752/60000 [==>...........................] - ETA: 1:43 - loss: 0.5955 - categorical_accuracy: 0.8113
 6784/60000 [==>...........................] - ETA: 1:43 - loss: 0.5951 - categorical_accuracy: 0.8115
 6816/60000 [==>...........................] - ETA: 1:43 - loss: 0.5938 - categorical_accuracy: 0.8118
 6848/60000 [==>...........................] - ETA: 1:43 - loss: 0.5919 - categorical_accuracy: 0.8124
 6880/60000 [==>...........................] - ETA: 1:43 - loss: 0.5901 - categorical_accuracy: 0.8129
 6912/60000 [==>...........................] - ETA: 1:43 - loss: 0.5890 - categorical_accuracy: 0.8135
 6944/60000 [==>...........................] - ETA: 1:43 - loss: 0.5875 - categorical_accuracy: 0.8137
 6976/60000 [==>...........................] - ETA: 1:43 - loss: 0.5852 - categorical_accuracy: 0.8145
 7008/60000 [==>...........................] - ETA: 1:43 - loss: 0.5839 - categorical_accuracy: 0.8151
 7040/60000 [==>...........................] - ETA: 1:43 - loss: 0.5817 - categorical_accuracy: 0.8159
 7072/60000 [==>...........................] - ETA: 1:43 - loss: 0.5808 - categorical_accuracy: 0.8163
 7104/60000 [==>...........................] - ETA: 1:43 - loss: 0.5793 - categorical_accuracy: 0.8169
 7136/60000 [==>...........................] - ETA: 1:42 - loss: 0.5773 - categorical_accuracy: 0.8175
 7168/60000 [==>...........................] - ETA: 1:42 - loss: 0.5769 - categorical_accuracy: 0.8178
 7200/60000 [==>...........................] - ETA: 1:42 - loss: 0.5755 - categorical_accuracy: 0.8182
 7232/60000 [==>...........................] - ETA: 1:42 - loss: 0.5740 - categorical_accuracy: 0.8187
 7264/60000 [==>...........................] - ETA: 1:42 - loss: 0.5718 - categorical_accuracy: 0.8195
 7296/60000 [==>...........................] - ETA: 1:42 - loss: 0.5697 - categorical_accuracy: 0.8202
 7328/60000 [==>...........................] - ETA: 1:42 - loss: 0.5681 - categorical_accuracy: 0.8207
 7360/60000 [==>...........................] - ETA: 1:42 - loss: 0.5664 - categorical_accuracy: 0.8212
 7392/60000 [==>...........................] - ETA: 1:42 - loss: 0.5646 - categorical_accuracy: 0.8217
 7424/60000 [==>...........................] - ETA: 1:42 - loss: 0.5631 - categorical_accuracy: 0.8219
 7456/60000 [==>...........................] - ETA: 1:42 - loss: 0.5611 - categorical_accuracy: 0.8224
 7488/60000 [==>...........................] - ETA: 1:42 - loss: 0.5596 - categorical_accuracy: 0.8228
 7520/60000 [==>...........................] - ETA: 1:42 - loss: 0.5580 - categorical_accuracy: 0.8231
 7552/60000 [==>...........................] - ETA: 1:42 - loss: 0.5566 - categorical_accuracy: 0.8236
 7584/60000 [==>...........................] - ETA: 1:42 - loss: 0.5567 - categorical_accuracy: 0.8237
 7616/60000 [==>...........................] - ETA: 1:41 - loss: 0.5552 - categorical_accuracy: 0.8242
 7648/60000 [==>...........................] - ETA: 1:41 - loss: 0.5538 - categorical_accuracy: 0.8247
 7680/60000 [==>...........................] - ETA: 1:41 - loss: 0.5533 - categorical_accuracy: 0.8249
 7712/60000 [==>...........................] - ETA: 1:41 - loss: 0.5518 - categorical_accuracy: 0.8253
 7744/60000 [==>...........................] - ETA: 1:41 - loss: 0.5500 - categorical_accuracy: 0.8258
 7776/60000 [==>...........................] - ETA: 1:41 - loss: 0.5507 - categorical_accuracy: 0.8255
 7808/60000 [==>...........................] - ETA: 1:41 - loss: 0.5500 - categorical_accuracy: 0.8258
 7840/60000 [==>...........................] - ETA: 1:41 - loss: 0.5485 - categorical_accuracy: 0.8263
 7872/60000 [==>...........................] - ETA: 1:41 - loss: 0.5469 - categorical_accuracy: 0.8269
 7904/60000 [==>...........................] - ETA: 1:41 - loss: 0.5457 - categorical_accuracy: 0.8273
 7936/60000 [==>...........................] - ETA: 1:41 - loss: 0.5446 - categorical_accuracy: 0.8276
 7968/60000 [==>...........................] - ETA: 1:41 - loss: 0.5434 - categorical_accuracy: 0.8282
 8000/60000 [===>..........................] - ETA: 1:41 - loss: 0.5419 - categorical_accuracy: 0.8288
 8032/60000 [===>..........................] - ETA: 1:40 - loss: 0.5410 - categorical_accuracy: 0.8291
 8064/60000 [===>..........................] - ETA: 1:40 - loss: 0.5391 - categorical_accuracy: 0.8297
 8096/60000 [===>..........................] - ETA: 1:40 - loss: 0.5390 - categorical_accuracy: 0.8299
 8128/60000 [===>..........................] - ETA: 1:40 - loss: 0.5382 - categorical_accuracy: 0.8300
 8160/60000 [===>..........................] - ETA: 1:40 - loss: 0.5378 - categorical_accuracy: 0.8300
 8192/60000 [===>..........................] - ETA: 1:40 - loss: 0.5372 - categorical_accuracy: 0.8304
 8224/60000 [===>..........................] - ETA: 1:40 - loss: 0.5365 - categorical_accuracy: 0.8310
 8256/60000 [===>..........................] - ETA: 1:40 - loss: 0.5350 - categorical_accuracy: 0.8314
 8288/60000 [===>..........................] - ETA: 1:40 - loss: 0.5342 - categorical_accuracy: 0.8317
 8320/60000 [===>..........................] - ETA: 1:40 - loss: 0.5327 - categorical_accuracy: 0.8322
 8352/60000 [===>..........................] - ETA: 1:40 - loss: 0.5313 - categorical_accuracy: 0.8326
 8384/60000 [===>..........................] - ETA: 1:40 - loss: 0.5302 - categorical_accuracy: 0.8328
 8416/60000 [===>..........................] - ETA: 1:40 - loss: 0.5285 - categorical_accuracy: 0.8333
 8448/60000 [===>..........................] - ETA: 1:40 - loss: 0.5272 - categorical_accuracy: 0.8337
 8480/60000 [===>..........................] - ETA: 1:39 - loss: 0.5264 - categorical_accuracy: 0.8338
 8512/60000 [===>..........................] - ETA: 1:39 - loss: 0.5257 - categorical_accuracy: 0.8340
 8544/60000 [===>..........................] - ETA: 1:39 - loss: 0.5247 - categorical_accuracy: 0.8340
 8576/60000 [===>..........................] - ETA: 1:39 - loss: 0.5231 - categorical_accuracy: 0.8345
 8608/60000 [===>..........................] - ETA: 1:39 - loss: 0.5214 - categorical_accuracy: 0.8352
 8640/60000 [===>..........................] - ETA: 1:39 - loss: 0.5200 - categorical_accuracy: 0.8356
 8672/60000 [===>..........................] - ETA: 1:39 - loss: 0.5186 - categorical_accuracy: 0.8361
 8704/60000 [===>..........................] - ETA: 1:39 - loss: 0.5176 - categorical_accuracy: 0.8365
 8736/60000 [===>..........................] - ETA: 1:39 - loss: 0.5161 - categorical_accuracy: 0.8370
 8768/60000 [===>..........................] - ETA: 1:39 - loss: 0.5151 - categorical_accuracy: 0.8371
 8800/60000 [===>..........................] - ETA: 1:39 - loss: 0.5139 - categorical_accuracy: 0.8375
 8832/60000 [===>..........................] - ETA: 1:39 - loss: 0.5132 - categorical_accuracy: 0.8380
 8864/60000 [===>..........................] - ETA: 1:39 - loss: 0.5124 - categorical_accuracy: 0.8384
 8896/60000 [===>..........................] - ETA: 1:39 - loss: 0.5110 - categorical_accuracy: 0.8389
 8928/60000 [===>..........................] - ETA: 1:39 - loss: 0.5099 - categorical_accuracy: 0.8392
 8960/60000 [===>..........................] - ETA: 1:39 - loss: 0.5085 - categorical_accuracy: 0.8397
 8992/60000 [===>..........................] - ETA: 1:38 - loss: 0.5079 - categorical_accuracy: 0.8400
 9024/60000 [===>..........................] - ETA: 1:38 - loss: 0.5073 - categorical_accuracy: 0.8402
 9056/60000 [===>..........................] - ETA: 1:38 - loss: 0.5058 - categorical_accuracy: 0.8407
 9088/60000 [===>..........................] - ETA: 1:38 - loss: 0.5044 - categorical_accuracy: 0.8412
 9120/60000 [===>..........................] - ETA: 1:38 - loss: 0.5041 - categorical_accuracy: 0.8413
 9152/60000 [===>..........................] - ETA: 1:38 - loss: 0.5025 - categorical_accuracy: 0.8419
 9184/60000 [===>..........................] - ETA: 1:38 - loss: 0.5014 - categorical_accuracy: 0.8422
 9216/60000 [===>..........................] - ETA: 1:38 - loss: 0.4999 - categorical_accuracy: 0.8428
 9248/60000 [===>..........................] - ETA: 1:38 - loss: 0.4987 - categorical_accuracy: 0.8431
 9280/60000 [===>..........................] - ETA: 1:38 - loss: 0.4995 - categorical_accuracy: 0.8432
 9312/60000 [===>..........................] - ETA: 1:38 - loss: 0.4980 - categorical_accuracy: 0.8438
 9344/60000 [===>..........................] - ETA: 1:38 - loss: 0.4966 - categorical_accuracy: 0.8443
 9376/60000 [===>..........................] - ETA: 1:38 - loss: 0.4959 - categorical_accuracy: 0.8445
 9408/60000 [===>..........................] - ETA: 1:38 - loss: 0.4952 - categorical_accuracy: 0.8447
 9440/60000 [===>..........................] - ETA: 1:38 - loss: 0.4956 - categorical_accuracy: 0.8447
 9472/60000 [===>..........................] - ETA: 1:37 - loss: 0.4943 - categorical_accuracy: 0.8451
 9504/60000 [===>..........................] - ETA: 1:37 - loss: 0.4931 - categorical_accuracy: 0.8454
 9536/60000 [===>..........................] - ETA: 1:37 - loss: 0.4920 - categorical_accuracy: 0.8457
 9568/60000 [===>..........................] - ETA: 1:37 - loss: 0.4913 - categorical_accuracy: 0.8458
 9600/60000 [===>..........................] - ETA: 1:37 - loss: 0.4899 - categorical_accuracy: 0.8464
 9632/60000 [===>..........................] - ETA: 1:37 - loss: 0.4892 - categorical_accuracy: 0.8467
 9664/60000 [===>..........................] - ETA: 1:37 - loss: 0.4880 - categorical_accuracy: 0.8471
 9696/60000 [===>..........................] - ETA: 1:37 - loss: 0.4871 - categorical_accuracy: 0.8472
 9728/60000 [===>..........................] - ETA: 1:37 - loss: 0.4864 - categorical_accuracy: 0.8475
 9760/60000 [===>..........................] - ETA: 1:37 - loss: 0.4852 - categorical_accuracy: 0.8478
 9792/60000 [===>..........................] - ETA: 1:37 - loss: 0.4841 - categorical_accuracy: 0.8481
 9824/60000 [===>..........................] - ETA: 1:37 - loss: 0.4841 - categorical_accuracy: 0.8482
 9856/60000 [===>..........................] - ETA: 1:37 - loss: 0.4832 - categorical_accuracy: 0.8484
 9888/60000 [===>..........................] - ETA: 1:37 - loss: 0.4819 - categorical_accuracy: 0.8489
 9920/60000 [===>..........................] - ETA: 1:36 - loss: 0.4805 - categorical_accuracy: 0.8494
 9952/60000 [===>..........................] - ETA: 1:36 - loss: 0.4794 - categorical_accuracy: 0.8497
 9984/60000 [===>..........................] - ETA: 1:36 - loss: 0.4785 - categorical_accuracy: 0.8500
10016/60000 [====>.........................] - ETA: 1:36 - loss: 0.4771 - categorical_accuracy: 0.8504
10048/60000 [====>.........................] - ETA: 1:36 - loss: 0.4764 - categorical_accuracy: 0.8507
10080/60000 [====>.........................] - ETA: 1:36 - loss: 0.4755 - categorical_accuracy: 0.8509
10112/60000 [====>.........................] - ETA: 1:36 - loss: 0.4744 - categorical_accuracy: 0.8513
10144/60000 [====>.........................] - ETA: 1:36 - loss: 0.4733 - categorical_accuracy: 0.8514
10176/60000 [====>.........................] - ETA: 1:36 - loss: 0.4721 - categorical_accuracy: 0.8518
10208/60000 [====>.........................] - ETA: 1:36 - loss: 0.4712 - categorical_accuracy: 0.8522
10240/60000 [====>.........................] - ETA: 1:36 - loss: 0.4701 - categorical_accuracy: 0.8525
10272/60000 [====>.........................] - ETA: 1:36 - loss: 0.4695 - categorical_accuracy: 0.8527
10304/60000 [====>.........................] - ETA: 1:36 - loss: 0.4689 - categorical_accuracy: 0.8530
10336/60000 [====>.........................] - ETA: 1:35 - loss: 0.4682 - categorical_accuracy: 0.8532
10368/60000 [====>.........................] - ETA: 1:35 - loss: 0.4672 - categorical_accuracy: 0.8534
10400/60000 [====>.........................] - ETA: 1:35 - loss: 0.4664 - categorical_accuracy: 0.8536
10432/60000 [====>.........................] - ETA: 1:35 - loss: 0.4656 - categorical_accuracy: 0.8538
10464/60000 [====>.........................] - ETA: 1:35 - loss: 0.4649 - categorical_accuracy: 0.8542
10496/60000 [====>.........................] - ETA: 1:35 - loss: 0.4638 - categorical_accuracy: 0.8544
10528/60000 [====>.........................] - ETA: 1:35 - loss: 0.4631 - categorical_accuracy: 0.8546
10560/60000 [====>.........................] - ETA: 1:35 - loss: 0.4639 - categorical_accuracy: 0.8545
10592/60000 [====>.........................] - ETA: 1:35 - loss: 0.4633 - categorical_accuracy: 0.8547
10624/60000 [====>.........................] - ETA: 1:35 - loss: 0.4625 - categorical_accuracy: 0.8549
10656/60000 [====>.........................] - ETA: 1:35 - loss: 0.4616 - categorical_accuracy: 0.8550
10688/60000 [====>.........................] - ETA: 1:35 - loss: 0.4609 - categorical_accuracy: 0.8552
10720/60000 [====>.........................] - ETA: 1:35 - loss: 0.4599 - categorical_accuracy: 0.8556
10752/60000 [====>.........................] - ETA: 1:35 - loss: 0.4587 - categorical_accuracy: 0.8560
10784/60000 [====>.........................] - ETA: 1:35 - loss: 0.4581 - categorical_accuracy: 0.8562
10816/60000 [====>.........................] - ETA: 1:34 - loss: 0.4576 - categorical_accuracy: 0.8563
10848/60000 [====>.........................] - ETA: 1:34 - loss: 0.4564 - categorical_accuracy: 0.8567
10880/60000 [====>.........................] - ETA: 1:34 - loss: 0.4558 - categorical_accuracy: 0.8569
10912/60000 [====>.........................] - ETA: 1:34 - loss: 0.4546 - categorical_accuracy: 0.8573
10944/60000 [====>.........................] - ETA: 1:34 - loss: 0.4540 - categorical_accuracy: 0.8575
10976/60000 [====>.........................] - ETA: 1:34 - loss: 0.4532 - categorical_accuracy: 0.8576
11008/60000 [====>.........................] - ETA: 1:34 - loss: 0.4525 - categorical_accuracy: 0.8576
11040/60000 [====>.........................] - ETA: 1:34 - loss: 0.4522 - categorical_accuracy: 0.8577
11072/60000 [====>.........................] - ETA: 1:34 - loss: 0.4513 - categorical_accuracy: 0.8580
11104/60000 [====>.........................] - ETA: 1:34 - loss: 0.4506 - categorical_accuracy: 0.8582
11136/60000 [====>.........................] - ETA: 1:34 - loss: 0.4498 - categorical_accuracy: 0.8583
11168/60000 [====>.........................] - ETA: 1:34 - loss: 0.4491 - categorical_accuracy: 0.8585
11200/60000 [====>.........................] - ETA: 1:34 - loss: 0.4488 - categorical_accuracy: 0.8586
11232/60000 [====>.........................] - ETA: 1:34 - loss: 0.4480 - categorical_accuracy: 0.8588
11264/60000 [====>.........................] - ETA: 1:34 - loss: 0.4469 - categorical_accuracy: 0.8591
11296/60000 [====>.........................] - ETA: 1:34 - loss: 0.4459 - categorical_accuracy: 0.8594
11328/60000 [====>.........................] - ETA: 1:33 - loss: 0.4453 - categorical_accuracy: 0.8596
11360/60000 [====>.........................] - ETA: 1:33 - loss: 0.4447 - categorical_accuracy: 0.8597
11392/60000 [====>.........................] - ETA: 1:33 - loss: 0.4439 - categorical_accuracy: 0.8600
11424/60000 [====>.........................] - ETA: 1:33 - loss: 0.4433 - categorical_accuracy: 0.8602
11456/60000 [====>.........................] - ETA: 1:33 - loss: 0.4432 - categorical_accuracy: 0.8602
11488/60000 [====>.........................] - ETA: 1:33 - loss: 0.4422 - categorical_accuracy: 0.8606
11520/60000 [====>.........................] - ETA: 1:33 - loss: 0.4415 - categorical_accuracy: 0.8608
11552/60000 [====>.........................] - ETA: 1:33 - loss: 0.4406 - categorical_accuracy: 0.8611
11584/60000 [====>.........................] - ETA: 1:33 - loss: 0.4399 - categorical_accuracy: 0.8613
11616/60000 [====>.........................] - ETA: 1:33 - loss: 0.4392 - categorical_accuracy: 0.8616
11648/60000 [====>.........................] - ETA: 1:33 - loss: 0.4392 - categorical_accuracy: 0.8617
11680/60000 [====>.........................] - ETA: 1:33 - loss: 0.4394 - categorical_accuracy: 0.8616
11712/60000 [====>.........................] - ETA: 1:33 - loss: 0.4385 - categorical_accuracy: 0.8619
11744/60000 [====>.........................] - ETA: 1:33 - loss: 0.4380 - categorical_accuracy: 0.8621
11776/60000 [====>.........................] - ETA: 1:33 - loss: 0.4375 - categorical_accuracy: 0.8622
11808/60000 [====>.........................] - ETA: 1:33 - loss: 0.4369 - categorical_accuracy: 0.8622
11840/60000 [====>.........................] - ETA: 1:32 - loss: 0.4368 - categorical_accuracy: 0.8623
11872/60000 [====>.........................] - ETA: 1:32 - loss: 0.4367 - categorical_accuracy: 0.8623
11904/60000 [====>.........................] - ETA: 1:32 - loss: 0.4363 - categorical_accuracy: 0.8625
11936/60000 [====>.........................] - ETA: 1:32 - loss: 0.4357 - categorical_accuracy: 0.8627
11968/60000 [====>.........................] - ETA: 1:32 - loss: 0.4348 - categorical_accuracy: 0.8630
12000/60000 [=====>........................] - ETA: 1:32 - loss: 0.4340 - categorical_accuracy: 0.8632
12032/60000 [=====>........................] - ETA: 1:32 - loss: 0.4338 - categorical_accuracy: 0.8634
12064/60000 [=====>........................] - ETA: 1:32 - loss: 0.4330 - categorical_accuracy: 0.8636
12096/60000 [=====>........................] - ETA: 1:32 - loss: 0.4322 - categorical_accuracy: 0.8638
12128/60000 [=====>........................] - ETA: 1:32 - loss: 0.4322 - categorical_accuracy: 0.8638
12160/60000 [=====>........................] - ETA: 1:32 - loss: 0.4313 - categorical_accuracy: 0.8641
12192/60000 [=====>........................] - ETA: 1:32 - loss: 0.4315 - categorical_accuracy: 0.8641
12224/60000 [=====>........................] - ETA: 1:32 - loss: 0.4310 - categorical_accuracy: 0.8643
12256/60000 [=====>........................] - ETA: 1:32 - loss: 0.4310 - categorical_accuracy: 0.8644
12288/60000 [=====>........................] - ETA: 1:32 - loss: 0.4301 - categorical_accuracy: 0.8647
12320/60000 [=====>........................] - ETA: 1:31 - loss: 0.4299 - categorical_accuracy: 0.8648
12352/60000 [=====>........................] - ETA: 1:31 - loss: 0.4295 - categorical_accuracy: 0.8650
12384/60000 [=====>........................] - ETA: 1:31 - loss: 0.4288 - categorical_accuracy: 0.8651
12416/60000 [=====>........................] - ETA: 1:31 - loss: 0.4291 - categorical_accuracy: 0.8651
12448/60000 [=====>........................] - ETA: 1:31 - loss: 0.4284 - categorical_accuracy: 0.8654
12480/60000 [=====>........................] - ETA: 1:31 - loss: 0.4279 - categorical_accuracy: 0.8655
12512/60000 [=====>........................] - ETA: 1:31 - loss: 0.4271 - categorical_accuracy: 0.8659
12544/60000 [=====>........................] - ETA: 1:31 - loss: 0.4263 - categorical_accuracy: 0.8662
12576/60000 [=====>........................] - ETA: 1:31 - loss: 0.4260 - categorical_accuracy: 0.8663
12608/60000 [=====>........................] - ETA: 1:31 - loss: 0.4250 - categorical_accuracy: 0.8666
12640/60000 [=====>........................] - ETA: 1:31 - loss: 0.4246 - categorical_accuracy: 0.8667
12672/60000 [=====>........................] - ETA: 1:31 - loss: 0.4238 - categorical_accuracy: 0.8670
12704/60000 [=====>........................] - ETA: 1:31 - loss: 0.4230 - categorical_accuracy: 0.8672
12736/60000 [=====>........................] - ETA: 1:31 - loss: 0.4221 - categorical_accuracy: 0.8675
12768/60000 [=====>........................] - ETA: 1:31 - loss: 0.4220 - categorical_accuracy: 0.8677
12800/60000 [=====>........................] - ETA: 1:30 - loss: 0.4212 - categorical_accuracy: 0.8680
12832/60000 [=====>........................] - ETA: 1:30 - loss: 0.4203 - categorical_accuracy: 0.8682
12864/60000 [=====>........................] - ETA: 1:30 - loss: 0.4197 - categorical_accuracy: 0.8684
12896/60000 [=====>........................] - ETA: 1:30 - loss: 0.4191 - categorical_accuracy: 0.8686
12928/60000 [=====>........................] - ETA: 1:30 - loss: 0.4186 - categorical_accuracy: 0.8687
12960/60000 [=====>........................] - ETA: 1:30 - loss: 0.4186 - categorical_accuracy: 0.8687
12992/60000 [=====>........................] - ETA: 1:30 - loss: 0.4182 - categorical_accuracy: 0.8688
13024/60000 [=====>........................] - ETA: 1:30 - loss: 0.4180 - categorical_accuracy: 0.8689
13056/60000 [=====>........................] - ETA: 1:30 - loss: 0.4176 - categorical_accuracy: 0.8689
13088/60000 [=====>........................] - ETA: 1:30 - loss: 0.4169 - categorical_accuracy: 0.8692
13120/60000 [=====>........................] - ETA: 1:30 - loss: 0.4162 - categorical_accuracy: 0.8694
13152/60000 [=====>........................] - ETA: 1:30 - loss: 0.4153 - categorical_accuracy: 0.8697
13184/60000 [=====>........................] - ETA: 1:30 - loss: 0.4153 - categorical_accuracy: 0.8698
13216/60000 [=====>........................] - ETA: 1:30 - loss: 0.4161 - categorical_accuracy: 0.8697
13248/60000 [=====>........................] - ETA: 1:30 - loss: 0.4153 - categorical_accuracy: 0.8700
13280/60000 [=====>........................] - ETA: 1:29 - loss: 0.4159 - categorical_accuracy: 0.8700
13312/60000 [=====>........................] - ETA: 1:29 - loss: 0.4153 - categorical_accuracy: 0.8701
13344/60000 [=====>........................] - ETA: 1:29 - loss: 0.4150 - categorical_accuracy: 0.8702
13376/60000 [=====>........................] - ETA: 1:29 - loss: 0.4145 - categorical_accuracy: 0.8703
13408/60000 [=====>........................] - ETA: 1:29 - loss: 0.4139 - categorical_accuracy: 0.8706
13440/60000 [=====>........................] - ETA: 1:29 - loss: 0.4133 - categorical_accuracy: 0.8707
13472/60000 [=====>........................] - ETA: 1:29 - loss: 0.4130 - categorical_accuracy: 0.8708
13504/60000 [=====>........................] - ETA: 1:29 - loss: 0.4123 - categorical_accuracy: 0.8711
13536/60000 [=====>........................] - ETA: 1:29 - loss: 0.4116 - categorical_accuracy: 0.8714
13568/60000 [=====>........................] - ETA: 1:29 - loss: 0.4110 - categorical_accuracy: 0.8715
13600/60000 [=====>........................] - ETA: 1:29 - loss: 0.4102 - categorical_accuracy: 0.8718
13632/60000 [=====>........................] - ETA: 1:29 - loss: 0.4096 - categorical_accuracy: 0.8719
13664/60000 [=====>........................] - ETA: 1:29 - loss: 0.4090 - categorical_accuracy: 0.8721
13696/60000 [=====>........................] - ETA: 1:29 - loss: 0.4085 - categorical_accuracy: 0.8722
13728/60000 [=====>........................] - ETA: 1:29 - loss: 0.4079 - categorical_accuracy: 0.8725
13760/60000 [=====>........................] - ETA: 1:29 - loss: 0.4072 - categorical_accuracy: 0.8726
13792/60000 [=====>........................] - ETA: 1:28 - loss: 0.4065 - categorical_accuracy: 0.8728
13824/60000 [=====>........................] - ETA: 1:28 - loss: 0.4060 - categorical_accuracy: 0.8728
13856/60000 [=====>........................] - ETA: 1:28 - loss: 0.4051 - categorical_accuracy: 0.8731
13888/60000 [=====>........................] - ETA: 1:28 - loss: 0.4043 - categorical_accuracy: 0.8734
13920/60000 [=====>........................] - ETA: 1:28 - loss: 0.4038 - categorical_accuracy: 0.8736
13952/60000 [=====>........................] - ETA: 1:28 - loss: 0.4029 - categorical_accuracy: 0.8739
13984/60000 [=====>........................] - ETA: 1:28 - loss: 0.4023 - categorical_accuracy: 0.8740
14016/60000 [======>.......................] - ETA: 1:28 - loss: 0.4021 - categorical_accuracy: 0.8741
14048/60000 [======>.......................] - ETA: 1:28 - loss: 0.4019 - categorical_accuracy: 0.8741
14080/60000 [======>.......................] - ETA: 1:28 - loss: 0.4034 - categorical_accuracy: 0.8741
14112/60000 [======>.......................] - ETA: 1:28 - loss: 0.4030 - categorical_accuracy: 0.8742
14144/60000 [======>.......................] - ETA: 1:28 - loss: 0.4028 - categorical_accuracy: 0.8743
14176/60000 [======>.......................] - ETA: 1:28 - loss: 0.4022 - categorical_accuracy: 0.8745
14208/60000 [======>.......................] - ETA: 1:28 - loss: 0.4017 - categorical_accuracy: 0.8746
14240/60000 [======>.......................] - ETA: 1:28 - loss: 0.4010 - categorical_accuracy: 0.8748
14272/60000 [======>.......................] - ETA: 1:28 - loss: 0.4006 - categorical_accuracy: 0.8749
14304/60000 [======>.......................] - ETA: 1:27 - loss: 0.3998 - categorical_accuracy: 0.8752
14336/60000 [======>.......................] - ETA: 1:27 - loss: 0.3992 - categorical_accuracy: 0.8754
14368/60000 [======>.......................] - ETA: 1:27 - loss: 0.3984 - categorical_accuracy: 0.8757
14400/60000 [======>.......................] - ETA: 1:27 - loss: 0.3976 - categorical_accuracy: 0.8760
14432/60000 [======>.......................] - ETA: 1:27 - loss: 0.3969 - categorical_accuracy: 0.8762
14464/60000 [======>.......................] - ETA: 1:27 - loss: 0.3963 - categorical_accuracy: 0.8765
14496/60000 [======>.......................] - ETA: 1:27 - loss: 0.3964 - categorical_accuracy: 0.8764
14528/60000 [======>.......................] - ETA: 1:27 - loss: 0.3957 - categorical_accuracy: 0.8767
14560/60000 [======>.......................] - ETA: 1:27 - loss: 0.3954 - categorical_accuracy: 0.8766
14592/60000 [======>.......................] - ETA: 1:27 - loss: 0.3949 - categorical_accuracy: 0.8768
14624/60000 [======>.......................] - ETA: 1:27 - loss: 0.3944 - categorical_accuracy: 0.8769
14656/60000 [======>.......................] - ETA: 1:27 - loss: 0.3940 - categorical_accuracy: 0.8770
14688/60000 [======>.......................] - ETA: 1:27 - loss: 0.3932 - categorical_accuracy: 0.8773
14720/60000 [======>.......................] - ETA: 1:27 - loss: 0.3930 - categorical_accuracy: 0.8774
14752/60000 [======>.......................] - ETA: 1:27 - loss: 0.3928 - categorical_accuracy: 0.8775
14784/60000 [======>.......................] - ETA: 1:27 - loss: 0.3923 - categorical_accuracy: 0.8776
14816/60000 [======>.......................] - ETA: 1:26 - loss: 0.3916 - categorical_accuracy: 0.8779
14848/60000 [======>.......................] - ETA: 1:26 - loss: 0.3916 - categorical_accuracy: 0.8780
14880/60000 [======>.......................] - ETA: 1:26 - loss: 0.3913 - categorical_accuracy: 0.8781
14912/60000 [======>.......................] - ETA: 1:26 - loss: 0.3910 - categorical_accuracy: 0.8781
14944/60000 [======>.......................] - ETA: 1:26 - loss: 0.3907 - categorical_accuracy: 0.8782
14976/60000 [======>.......................] - ETA: 1:26 - loss: 0.3902 - categorical_accuracy: 0.8783
15008/60000 [======>.......................] - ETA: 1:26 - loss: 0.3897 - categorical_accuracy: 0.8784
15040/60000 [======>.......................] - ETA: 1:26 - loss: 0.3893 - categorical_accuracy: 0.8785
15072/60000 [======>.......................] - ETA: 1:26 - loss: 0.3888 - categorical_accuracy: 0.8786
15104/60000 [======>.......................] - ETA: 1:26 - loss: 0.3883 - categorical_accuracy: 0.8788
15136/60000 [======>.......................] - ETA: 1:26 - loss: 0.3879 - categorical_accuracy: 0.8788
15168/60000 [======>.......................] - ETA: 1:26 - loss: 0.3876 - categorical_accuracy: 0.8789
15200/60000 [======>.......................] - ETA: 1:26 - loss: 0.3870 - categorical_accuracy: 0.8790
15232/60000 [======>.......................] - ETA: 1:26 - loss: 0.3869 - categorical_accuracy: 0.8790
15264/60000 [======>.......................] - ETA: 1:26 - loss: 0.3869 - categorical_accuracy: 0.8790
15296/60000 [======>.......................] - ETA: 1:26 - loss: 0.3864 - categorical_accuracy: 0.8791
15328/60000 [======>.......................] - ETA: 1:25 - loss: 0.3858 - categorical_accuracy: 0.8792
15360/60000 [======>.......................] - ETA: 1:25 - loss: 0.3853 - categorical_accuracy: 0.8794
15392/60000 [======>.......................] - ETA: 1:25 - loss: 0.3850 - categorical_accuracy: 0.8795
15424/60000 [======>.......................] - ETA: 1:25 - loss: 0.3845 - categorical_accuracy: 0.8797
15456/60000 [======>.......................] - ETA: 1:25 - loss: 0.3841 - categorical_accuracy: 0.8799
15488/60000 [======>.......................] - ETA: 1:25 - loss: 0.3835 - categorical_accuracy: 0.8800
15520/60000 [======>.......................] - ETA: 1:25 - loss: 0.3836 - categorical_accuracy: 0.8800
15552/60000 [======>.......................] - ETA: 1:25 - loss: 0.3832 - categorical_accuracy: 0.8800
15584/60000 [======>.......................] - ETA: 1:25 - loss: 0.3827 - categorical_accuracy: 0.8801
15616/60000 [======>.......................] - ETA: 1:25 - loss: 0.3821 - categorical_accuracy: 0.8803
15648/60000 [======>.......................] - ETA: 1:25 - loss: 0.3815 - categorical_accuracy: 0.8804
15680/60000 [======>.......................] - ETA: 1:25 - loss: 0.3808 - categorical_accuracy: 0.8807
15712/60000 [======>.......................] - ETA: 1:25 - loss: 0.3803 - categorical_accuracy: 0.8808
15744/60000 [======>.......................] - ETA: 1:25 - loss: 0.3804 - categorical_accuracy: 0.8808
15776/60000 [======>.......................] - ETA: 1:25 - loss: 0.3799 - categorical_accuracy: 0.8810
15808/60000 [======>.......................] - ETA: 1:24 - loss: 0.3793 - categorical_accuracy: 0.8812
15840/60000 [======>.......................] - ETA: 1:24 - loss: 0.3792 - categorical_accuracy: 0.8813
15872/60000 [======>.......................] - ETA: 1:24 - loss: 0.3789 - categorical_accuracy: 0.8814
15904/60000 [======>.......................] - ETA: 1:24 - loss: 0.3784 - categorical_accuracy: 0.8815
15936/60000 [======>.......................] - ETA: 1:24 - loss: 0.3779 - categorical_accuracy: 0.8817
15968/60000 [======>.......................] - ETA: 1:24 - loss: 0.3777 - categorical_accuracy: 0.8818
16000/60000 [=======>......................] - ETA: 1:24 - loss: 0.3776 - categorical_accuracy: 0.8819
16032/60000 [=======>......................] - ETA: 1:24 - loss: 0.3770 - categorical_accuracy: 0.8820
16064/60000 [=======>......................] - ETA: 1:24 - loss: 0.3765 - categorical_accuracy: 0.8822
16096/60000 [=======>......................] - ETA: 1:24 - loss: 0.3762 - categorical_accuracy: 0.8822
16128/60000 [=======>......................] - ETA: 1:24 - loss: 0.3757 - categorical_accuracy: 0.8824
16160/60000 [=======>......................] - ETA: 1:24 - loss: 0.3756 - categorical_accuracy: 0.8825
16192/60000 [=======>......................] - ETA: 1:24 - loss: 0.3751 - categorical_accuracy: 0.8827
16224/60000 [=======>......................] - ETA: 1:24 - loss: 0.3744 - categorical_accuracy: 0.8829
16256/60000 [=======>......................] - ETA: 1:24 - loss: 0.3740 - categorical_accuracy: 0.8829
16288/60000 [=======>......................] - ETA: 1:24 - loss: 0.3734 - categorical_accuracy: 0.8832
16320/60000 [=======>......................] - ETA: 1:23 - loss: 0.3729 - categorical_accuracy: 0.8833
16352/60000 [=======>......................] - ETA: 1:23 - loss: 0.3725 - categorical_accuracy: 0.8834
16384/60000 [=======>......................] - ETA: 1:23 - loss: 0.3720 - categorical_accuracy: 0.8835
16416/60000 [=======>......................] - ETA: 1:23 - loss: 0.3726 - categorical_accuracy: 0.8835
16448/60000 [=======>......................] - ETA: 1:23 - loss: 0.3720 - categorical_accuracy: 0.8837
16480/60000 [=======>......................] - ETA: 1:23 - loss: 0.3716 - categorical_accuracy: 0.8838
16512/60000 [=======>......................] - ETA: 1:23 - loss: 0.3716 - categorical_accuracy: 0.8839
16544/60000 [=======>......................] - ETA: 1:23 - loss: 0.3720 - categorical_accuracy: 0.8838
16576/60000 [=======>......................] - ETA: 1:23 - loss: 0.3714 - categorical_accuracy: 0.8839
16608/60000 [=======>......................] - ETA: 1:23 - loss: 0.3710 - categorical_accuracy: 0.8840
16640/60000 [=======>......................] - ETA: 1:23 - loss: 0.3706 - categorical_accuracy: 0.8841
16672/60000 [=======>......................] - ETA: 1:23 - loss: 0.3703 - categorical_accuracy: 0.8842
16704/60000 [=======>......................] - ETA: 1:23 - loss: 0.3700 - categorical_accuracy: 0.8843
16736/60000 [=======>......................] - ETA: 1:23 - loss: 0.3697 - categorical_accuracy: 0.8844
16768/60000 [=======>......................] - ETA: 1:23 - loss: 0.3691 - categorical_accuracy: 0.8847
16800/60000 [=======>......................] - ETA: 1:22 - loss: 0.3690 - categorical_accuracy: 0.8846
16832/60000 [=======>......................] - ETA: 1:22 - loss: 0.3697 - categorical_accuracy: 0.8845
16864/60000 [=======>......................] - ETA: 1:22 - loss: 0.3696 - categorical_accuracy: 0.8845
16896/60000 [=======>......................] - ETA: 1:22 - loss: 0.3693 - categorical_accuracy: 0.8847
16928/60000 [=======>......................] - ETA: 1:22 - loss: 0.3688 - categorical_accuracy: 0.8849
16960/60000 [=======>......................] - ETA: 1:22 - loss: 0.3681 - categorical_accuracy: 0.8851
16992/60000 [=======>......................] - ETA: 1:22 - loss: 0.3681 - categorical_accuracy: 0.8852
17024/60000 [=======>......................] - ETA: 1:22 - loss: 0.3678 - categorical_accuracy: 0.8852
17056/60000 [=======>......................] - ETA: 1:22 - loss: 0.3675 - categorical_accuracy: 0.8853
17088/60000 [=======>......................] - ETA: 1:22 - loss: 0.3674 - categorical_accuracy: 0.8853
17120/60000 [=======>......................] - ETA: 1:22 - loss: 0.3671 - categorical_accuracy: 0.8853
17152/60000 [=======>......................] - ETA: 1:22 - loss: 0.3665 - categorical_accuracy: 0.8855
17184/60000 [=======>......................] - ETA: 1:22 - loss: 0.3662 - categorical_accuracy: 0.8856
17216/60000 [=======>......................] - ETA: 1:22 - loss: 0.3661 - categorical_accuracy: 0.8857
17248/60000 [=======>......................] - ETA: 1:22 - loss: 0.3655 - categorical_accuracy: 0.8859
17280/60000 [=======>......................] - ETA: 1:21 - loss: 0.3652 - categorical_accuracy: 0.8860
17312/60000 [=======>......................] - ETA: 1:21 - loss: 0.3651 - categorical_accuracy: 0.8860
17344/60000 [=======>......................] - ETA: 1:21 - loss: 0.3647 - categorical_accuracy: 0.8862
17376/60000 [=======>......................] - ETA: 1:21 - loss: 0.3643 - categorical_accuracy: 0.8863
17408/60000 [=======>......................] - ETA: 1:21 - loss: 0.3641 - categorical_accuracy: 0.8864
17440/60000 [=======>......................] - ETA: 1:21 - loss: 0.3637 - categorical_accuracy: 0.8865
17472/60000 [=======>......................] - ETA: 1:21 - loss: 0.3635 - categorical_accuracy: 0.8865
17504/60000 [=======>......................] - ETA: 1:21 - loss: 0.3634 - categorical_accuracy: 0.8865
17536/60000 [=======>......................] - ETA: 1:21 - loss: 0.3630 - categorical_accuracy: 0.8866
17568/60000 [=======>......................] - ETA: 1:21 - loss: 0.3627 - categorical_accuracy: 0.8867
17600/60000 [=======>......................] - ETA: 1:21 - loss: 0.3621 - categorical_accuracy: 0.8869
17632/60000 [=======>......................] - ETA: 1:21 - loss: 0.3619 - categorical_accuracy: 0.8870
17664/60000 [=======>......................] - ETA: 1:21 - loss: 0.3614 - categorical_accuracy: 0.8871
17696/60000 [=======>......................] - ETA: 1:21 - loss: 0.3609 - categorical_accuracy: 0.8873
17728/60000 [=======>......................] - ETA: 1:21 - loss: 0.3607 - categorical_accuracy: 0.8874
17760/60000 [=======>......................] - ETA: 1:21 - loss: 0.3602 - categorical_accuracy: 0.8876
17792/60000 [=======>......................] - ETA: 1:20 - loss: 0.3597 - categorical_accuracy: 0.8876
17824/60000 [=======>......................] - ETA: 1:20 - loss: 0.3594 - categorical_accuracy: 0.8877
17856/60000 [=======>......................] - ETA: 1:20 - loss: 0.3590 - categorical_accuracy: 0.8879
17888/60000 [=======>......................] - ETA: 1:20 - loss: 0.3587 - categorical_accuracy: 0.8880
17920/60000 [=======>......................] - ETA: 1:20 - loss: 0.3582 - categorical_accuracy: 0.8881
17952/60000 [=======>......................] - ETA: 1:20 - loss: 0.3580 - categorical_accuracy: 0.8881
17984/60000 [=======>......................] - ETA: 1:20 - loss: 0.3582 - categorical_accuracy: 0.8882
18016/60000 [========>.....................] - ETA: 1:20 - loss: 0.3580 - categorical_accuracy: 0.8883
18048/60000 [========>.....................] - ETA: 1:20 - loss: 0.3575 - categorical_accuracy: 0.8885
18080/60000 [========>.....................] - ETA: 1:20 - loss: 0.3573 - categorical_accuracy: 0.8885
18112/60000 [========>.....................] - ETA: 1:20 - loss: 0.3569 - categorical_accuracy: 0.8886
18144/60000 [========>.....................] - ETA: 1:20 - loss: 0.3564 - categorical_accuracy: 0.8888
18176/60000 [========>.....................] - ETA: 1:20 - loss: 0.3565 - categorical_accuracy: 0.8889
18208/60000 [========>.....................] - ETA: 1:20 - loss: 0.3563 - categorical_accuracy: 0.8890
18240/60000 [========>.....................] - ETA: 1:20 - loss: 0.3561 - categorical_accuracy: 0.8891
18272/60000 [========>.....................] - ETA: 1:19 - loss: 0.3555 - categorical_accuracy: 0.8892
18304/60000 [========>.....................] - ETA: 1:19 - loss: 0.3550 - categorical_accuracy: 0.8894
18336/60000 [========>.....................] - ETA: 1:19 - loss: 0.3547 - categorical_accuracy: 0.8895
18368/60000 [========>.....................] - ETA: 1:19 - loss: 0.3543 - categorical_accuracy: 0.8896
18400/60000 [========>.....................] - ETA: 1:19 - loss: 0.3539 - categorical_accuracy: 0.8897
18432/60000 [========>.....................] - ETA: 1:19 - loss: 0.3535 - categorical_accuracy: 0.8898
18464/60000 [========>.....................] - ETA: 1:19 - loss: 0.3531 - categorical_accuracy: 0.8899
18496/60000 [========>.....................] - ETA: 1:19 - loss: 0.3528 - categorical_accuracy: 0.8900
18528/60000 [========>.....................] - ETA: 1:19 - loss: 0.3525 - categorical_accuracy: 0.8901
18560/60000 [========>.....................] - ETA: 1:19 - loss: 0.3521 - categorical_accuracy: 0.8902
18592/60000 [========>.....................] - ETA: 1:19 - loss: 0.3519 - categorical_accuracy: 0.8903
18624/60000 [========>.....................] - ETA: 1:19 - loss: 0.3515 - categorical_accuracy: 0.8904
18656/60000 [========>.....................] - ETA: 1:19 - loss: 0.3511 - categorical_accuracy: 0.8905
18688/60000 [========>.....................] - ETA: 1:19 - loss: 0.3505 - categorical_accuracy: 0.8907
18720/60000 [========>.....................] - ETA: 1:19 - loss: 0.3506 - categorical_accuracy: 0.8909
18752/60000 [========>.....................] - ETA: 1:19 - loss: 0.3504 - categorical_accuracy: 0.8909
18784/60000 [========>.....................] - ETA: 1:18 - loss: 0.3499 - categorical_accuracy: 0.8911
18816/60000 [========>.....................] - ETA: 1:18 - loss: 0.3498 - categorical_accuracy: 0.8912
18848/60000 [========>.....................] - ETA: 1:18 - loss: 0.3494 - categorical_accuracy: 0.8913
18880/60000 [========>.....................] - ETA: 1:18 - loss: 0.3493 - categorical_accuracy: 0.8913
18912/60000 [========>.....................] - ETA: 1:18 - loss: 0.3491 - categorical_accuracy: 0.8914
18944/60000 [========>.....................] - ETA: 1:18 - loss: 0.3490 - categorical_accuracy: 0.8914
18976/60000 [========>.....................] - ETA: 1:18 - loss: 0.3491 - categorical_accuracy: 0.8913
19008/60000 [========>.....................] - ETA: 1:18 - loss: 0.3488 - categorical_accuracy: 0.8914
19040/60000 [========>.....................] - ETA: 1:18 - loss: 0.3483 - categorical_accuracy: 0.8916
19072/60000 [========>.....................] - ETA: 1:18 - loss: 0.3479 - categorical_accuracy: 0.8917
19104/60000 [========>.....................] - ETA: 1:18 - loss: 0.3475 - categorical_accuracy: 0.8919
19136/60000 [========>.....................] - ETA: 1:18 - loss: 0.3473 - categorical_accuracy: 0.8919
19168/60000 [========>.....................] - ETA: 1:18 - loss: 0.3468 - categorical_accuracy: 0.8920
19200/60000 [========>.....................] - ETA: 1:18 - loss: 0.3464 - categorical_accuracy: 0.8922
19232/60000 [========>.....................] - ETA: 1:18 - loss: 0.3461 - categorical_accuracy: 0.8923
19264/60000 [========>.....................] - ETA: 1:18 - loss: 0.3457 - categorical_accuracy: 0.8924
19296/60000 [========>.....................] - ETA: 1:17 - loss: 0.3452 - categorical_accuracy: 0.8925
19328/60000 [========>.....................] - ETA: 1:17 - loss: 0.3451 - categorical_accuracy: 0.8926
19360/60000 [========>.....................] - ETA: 1:17 - loss: 0.3447 - categorical_accuracy: 0.8927
19392/60000 [========>.....................] - ETA: 1:17 - loss: 0.3442 - categorical_accuracy: 0.8928
19424/60000 [========>.....................] - ETA: 1:17 - loss: 0.3436 - categorical_accuracy: 0.8930
19456/60000 [========>.....................] - ETA: 1:17 - loss: 0.3431 - categorical_accuracy: 0.8932
19488/60000 [========>.....................] - ETA: 1:17 - loss: 0.3428 - categorical_accuracy: 0.8933
19520/60000 [========>.....................] - ETA: 1:17 - loss: 0.3424 - categorical_accuracy: 0.8934
19552/60000 [========>.....................] - ETA: 1:17 - loss: 0.3420 - categorical_accuracy: 0.8936
19584/60000 [========>.....................] - ETA: 1:17 - loss: 0.3417 - categorical_accuracy: 0.8936
19616/60000 [========>.....................] - ETA: 1:17 - loss: 0.3417 - categorical_accuracy: 0.8937
19648/60000 [========>.....................] - ETA: 1:17 - loss: 0.3413 - categorical_accuracy: 0.8937
19680/60000 [========>.....................] - ETA: 1:17 - loss: 0.3410 - categorical_accuracy: 0.8939
19712/60000 [========>.....................] - ETA: 1:17 - loss: 0.3406 - categorical_accuracy: 0.8940
19744/60000 [========>.....................] - ETA: 1:17 - loss: 0.3402 - categorical_accuracy: 0.8940
19776/60000 [========>.....................] - ETA: 1:17 - loss: 0.3401 - categorical_accuracy: 0.8940
19808/60000 [========>.....................] - ETA: 1:17 - loss: 0.3397 - categorical_accuracy: 0.8941
19840/60000 [========>.....................] - ETA: 1:16 - loss: 0.3393 - categorical_accuracy: 0.8943
19872/60000 [========>.....................] - ETA: 1:16 - loss: 0.3390 - categorical_accuracy: 0.8943
19904/60000 [========>.....................] - ETA: 1:16 - loss: 0.3385 - categorical_accuracy: 0.8944
19936/60000 [========>.....................] - ETA: 1:16 - loss: 0.3386 - categorical_accuracy: 0.8945
19968/60000 [========>.....................] - ETA: 1:16 - loss: 0.3389 - categorical_accuracy: 0.8944
20000/60000 [=========>....................] - ETA: 1:16 - loss: 0.3385 - categorical_accuracy: 0.8946
20032/60000 [=========>....................] - ETA: 1:16 - loss: 0.3382 - categorical_accuracy: 0.8946
20064/60000 [=========>....................] - ETA: 1:16 - loss: 0.3378 - categorical_accuracy: 0.8948
20096/60000 [=========>....................] - ETA: 1:16 - loss: 0.3376 - categorical_accuracy: 0.8949
20128/60000 [=========>....................] - ETA: 1:16 - loss: 0.3372 - categorical_accuracy: 0.8951
20160/60000 [=========>....................] - ETA: 1:16 - loss: 0.3372 - categorical_accuracy: 0.8950
20192/60000 [=========>....................] - ETA: 1:16 - loss: 0.3368 - categorical_accuracy: 0.8952
20224/60000 [=========>....................] - ETA: 1:16 - loss: 0.3363 - categorical_accuracy: 0.8954
20256/60000 [=========>....................] - ETA: 1:16 - loss: 0.3359 - categorical_accuracy: 0.8955
20288/60000 [=========>....................] - ETA: 1:16 - loss: 0.3354 - categorical_accuracy: 0.8957
20320/60000 [=========>....................] - ETA: 1:15 - loss: 0.3351 - categorical_accuracy: 0.8957
20352/60000 [=========>....................] - ETA: 1:15 - loss: 0.3347 - categorical_accuracy: 0.8959
20384/60000 [=========>....................] - ETA: 1:15 - loss: 0.3342 - categorical_accuracy: 0.8960
20416/60000 [=========>....................] - ETA: 1:15 - loss: 0.3338 - categorical_accuracy: 0.8962
20448/60000 [=========>....................] - ETA: 1:15 - loss: 0.3334 - categorical_accuracy: 0.8963
20480/60000 [=========>....................] - ETA: 1:15 - loss: 0.3334 - categorical_accuracy: 0.8964
20512/60000 [=========>....................] - ETA: 1:15 - loss: 0.3330 - categorical_accuracy: 0.8965
20544/60000 [=========>....................] - ETA: 1:15 - loss: 0.3325 - categorical_accuracy: 0.8967
20576/60000 [=========>....................] - ETA: 1:15 - loss: 0.3322 - categorical_accuracy: 0.8967
20608/60000 [=========>....................] - ETA: 1:15 - loss: 0.3319 - categorical_accuracy: 0.8968
20640/60000 [=========>....................] - ETA: 1:15 - loss: 0.3317 - categorical_accuracy: 0.8968
20672/60000 [=========>....................] - ETA: 1:15 - loss: 0.3312 - categorical_accuracy: 0.8969
20704/60000 [=========>....................] - ETA: 1:15 - loss: 0.3311 - categorical_accuracy: 0.8969
20736/60000 [=========>....................] - ETA: 1:15 - loss: 0.3308 - categorical_accuracy: 0.8969
20768/60000 [=========>....................] - ETA: 1:15 - loss: 0.3307 - categorical_accuracy: 0.8970
20800/60000 [=========>....................] - ETA: 1:15 - loss: 0.3308 - categorical_accuracy: 0.8970
20832/60000 [=========>....................] - ETA: 1:14 - loss: 0.3304 - categorical_accuracy: 0.8971
20864/60000 [=========>....................] - ETA: 1:14 - loss: 0.3299 - categorical_accuracy: 0.8973
20896/60000 [=========>....................] - ETA: 1:14 - loss: 0.3296 - categorical_accuracy: 0.8974
20928/60000 [=========>....................] - ETA: 1:14 - loss: 0.3292 - categorical_accuracy: 0.8976
20960/60000 [=========>....................] - ETA: 1:14 - loss: 0.3289 - categorical_accuracy: 0.8976
20992/60000 [=========>....................] - ETA: 1:14 - loss: 0.3285 - categorical_accuracy: 0.8977
21024/60000 [=========>....................] - ETA: 1:14 - loss: 0.3282 - categorical_accuracy: 0.8978
21056/60000 [=========>....................] - ETA: 1:14 - loss: 0.3277 - categorical_accuracy: 0.8979
21088/60000 [=========>....................] - ETA: 1:14 - loss: 0.3273 - categorical_accuracy: 0.8981
21120/60000 [=========>....................] - ETA: 1:14 - loss: 0.3271 - categorical_accuracy: 0.8982
21152/60000 [=========>....................] - ETA: 1:14 - loss: 0.3266 - categorical_accuracy: 0.8983
21184/60000 [=========>....................] - ETA: 1:14 - loss: 0.3265 - categorical_accuracy: 0.8984
21216/60000 [=========>....................] - ETA: 1:14 - loss: 0.3266 - categorical_accuracy: 0.8983
21248/60000 [=========>....................] - ETA: 1:14 - loss: 0.3262 - categorical_accuracy: 0.8984
21280/60000 [=========>....................] - ETA: 1:14 - loss: 0.3259 - categorical_accuracy: 0.8985
21312/60000 [=========>....................] - ETA: 1:14 - loss: 0.3257 - categorical_accuracy: 0.8986
21344/60000 [=========>....................] - ETA: 1:13 - loss: 0.3254 - categorical_accuracy: 0.8987
21376/60000 [=========>....................] - ETA: 1:13 - loss: 0.3252 - categorical_accuracy: 0.8988
21408/60000 [=========>....................] - ETA: 1:13 - loss: 0.3249 - categorical_accuracy: 0.8989
21440/60000 [=========>....................] - ETA: 1:13 - loss: 0.3246 - categorical_accuracy: 0.8989
21472/60000 [=========>....................] - ETA: 1:13 - loss: 0.3244 - categorical_accuracy: 0.8990
21504/60000 [=========>....................] - ETA: 1:13 - loss: 0.3246 - categorical_accuracy: 0.8989
21536/60000 [=========>....................] - ETA: 1:13 - loss: 0.3242 - categorical_accuracy: 0.8990
21568/60000 [=========>....................] - ETA: 1:13 - loss: 0.3238 - categorical_accuracy: 0.8992
21600/60000 [=========>....................] - ETA: 1:13 - loss: 0.3237 - categorical_accuracy: 0.8992
21632/60000 [=========>....................] - ETA: 1:13 - loss: 0.3233 - categorical_accuracy: 0.8993
21664/60000 [=========>....................] - ETA: 1:13 - loss: 0.3231 - categorical_accuracy: 0.8993
21696/60000 [=========>....................] - ETA: 1:13 - loss: 0.3227 - categorical_accuracy: 0.8994
21728/60000 [=========>....................] - ETA: 1:13 - loss: 0.3224 - categorical_accuracy: 0.8995
21760/60000 [=========>....................] - ETA: 1:13 - loss: 0.3223 - categorical_accuracy: 0.8996
21792/60000 [=========>....................] - ETA: 1:13 - loss: 0.3219 - categorical_accuracy: 0.8996
21824/60000 [=========>....................] - ETA: 1:13 - loss: 0.3216 - categorical_accuracy: 0.8997
21856/60000 [=========>....................] - ETA: 1:12 - loss: 0.3212 - categorical_accuracy: 0.8998
21888/60000 [=========>....................] - ETA: 1:12 - loss: 0.3208 - categorical_accuracy: 0.9000
21920/60000 [=========>....................] - ETA: 1:12 - loss: 0.3207 - categorical_accuracy: 0.9000
21952/60000 [=========>....................] - ETA: 1:12 - loss: 0.3204 - categorical_accuracy: 0.9001
21984/60000 [=========>....................] - ETA: 1:12 - loss: 0.3201 - categorical_accuracy: 0.9002
22016/60000 [==========>...................] - ETA: 1:12 - loss: 0.3197 - categorical_accuracy: 0.9004
22048/60000 [==========>...................] - ETA: 1:12 - loss: 0.3199 - categorical_accuracy: 0.9004
22080/60000 [==========>...................] - ETA: 1:12 - loss: 0.3197 - categorical_accuracy: 0.9005
22112/60000 [==========>...................] - ETA: 1:12 - loss: 0.3198 - categorical_accuracy: 0.9005
22144/60000 [==========>...................] - ETA: 1:12 - loss: 0.3194 - categorical_accuracy: 0.9006
22176/60000 [==========>...................] - ETA: 1:12 - loss: 0.3190 - categorical_accuracy: 0.9007
22208/60000 [==========>...................] - ETA: 1:12 - loss: 0.3191 - categorical_accuracy: 0.9006
22240/60000 [==========>...................] - ETA: 1:12 - loss: 0.3190 - categorical_accuracy: 0.9007
22272/60000 [==========>...................] - ETA: 1:12 - loss: 0.3186 - categorical_accuracy: 0.9008
22304/60000 [==========>...................] - ETA: 1:12 - loss: 0.3183 - categorical_accuracy: 0.9009
22336/60000 [==========>...................] - ETA: 1:12 - loss: 0.3179 - categorical_accuracy: 0.9011
22368/60000 [==========>...................] - ETA: 1:12 - loss: 0.3176 - categorical_accuracy: 0.9012
22400/60000 [==========>...................] - ETA: 1:11 - loss: 0.3173 - categorical_accuracy: 0.9012
22432/60000 [==========>...................] - ETA: 1:11 - loss: 0.3169 - categorical_accuracy: 0.9013
22464/60000 [==========>...................] - ETA: 1:11 - loss: 0.3168 - categorical_accuracy: 0.9013
22496/60000 [==========>...................] - ETA: 1:11 - loss: 0.3165 - categorical_accuracy: 0.9014
22528/60000 [==========>...................] - ETA: 1:11 - loss: 0.3162 - categorical_accuracy: 0.9015
22560/60000 [==========>...................] - ETA: 1:11 - loss: 0.3158 - categorical_accuracy: 0.9016
22592/60000 [==========>...................] - ETA: 1:11 - loss: 0.3155 - categorical_accuracy: 0.9018
22624/60000 [==========>...................] - ETA: 1:11 - loss: 0.3151 - categorical_accuracy: 0.9019
22656/60000 [==========>...................] - ETA: 1:11 - loss: 0.3147 - categorical_accuracy: 0.9020
22688/60000 [==========>...................] - ETA: 1:11 - loss: 0.3145 - categorical_accuracy: 0.9021
22720/60000 [==========>...................] - ETA: 1:11 - loss: 0.3144 - categorical_accuracy: 0.9022
22752/60000 [==========>...................] - ETA: 1:11 - loss: 0.3143 - categorical_accuracy: 0.9022
22784/60000 [==========>...................] - ETA: 1:11 - loss: 0.3140 - categorical_accuracy: 0.9023
22816/60000 [==========>...................] - ETA: 1:11 - loss: 0.3139 - categorical_accuracy: 0.9023
22848/60000 [==========>...................] - ETA: 1:11 - loss: 0.3135 - categorical_accuracy: 0.9024
22880/60000 [==========>...................] - ETA: 1:11 - loss: 0.3132 - categorical_accuracy: 0.9025
22912/60000 [==========>...................] - ETA: 1:10 - loss: 0.3131 - categorical_accuracy: 0.9025
22944/60000 [==========>...................] - ETA: 1:10 - loss: 0.3130 - categorical_accuracy: 0.9025
22976/60000 [==========>...................] - ETA: 1:10 - loss: 0.3126 - categorical_accuracy: 0.9027
23008/60000 [==========>...................] - ETA: 1:10 - loss: 0.3124 - categorical_accuracy: 0.9028
23040/60000 [==========>...................] - ETA: 1:10 - loss: 0.3123 - categorical_accuracy: 0.9028
23072/60000 [==========>...................] - ETA: 1:10 - loss: 0.3119 - categorical_accuracy: 0.9030
23104/60000 [==========>...................] - ETA: 1:10 - loss: 0.3116 - categorical_accuracy: 0.9030
23136/60000 [==========>...................] - ETA: 1:10 - loss: 0.3112 - categorical_accuracy: 0.9031
23168/60000 [==========>...................] - ETA: 1:10 - loss: 0.3109 - categorical_accuracy: 0.9032
23200/60000 [==========>...................] - ETA: 1:10 - loss: 0.3109 - categorical_accuracy: 0.9032
23232/60000 [==========>...................] - ETA: 1:10 - loss: 0.3106 - categorical_accuracy: 0.9033
23264/60000 [==========>...................] - ETA: 1:10 - loss: 0.3104 - categorical_accuracy: 0.9034
23296/60000 [==========>...................] - ETA: 1:10 - loss: 0.3100 - categorical_accuracy: 0.9035
23328/60000 [==========>...................] - ETA: 1:10 - loss: 0.3096 - categorical_accuracy: 0.9036
23360/60000 [==========>...................] - ETA: 1:10 - loss: 0.3095 - categorical_accuracy: 0.9036
23392/60000 [==========>...................] - ETA: 1:10 - loss: 0.3093 - categorical_accuracy: 0.9037
23424/60000 [==========>...................] - ETA: 1:09 - loss: 0.3091 - categorical_accuracy: 0.9037
23456/60000 [==========>...................] - ETA: 1:09 - loss: 0.3092 - categorical_accuracy: 0.9036
23488/60000 [==========>...................] - ETA: 1:09 - loss: 0.3090 - categorical_accuracy: 0.9037
23520/60000 [==========>...................] - ETA: 1:09 - loss: 0.3087 - categorical_accuracy: 0.9038
23552/60000 [==========>...................] - ETA: 1:09 - loss: 0.3085 - categorical_accuracy: 0.9039
23584/60000 [==========>...................] - ETA: 1:09 - loss: 0.3083 - categorical_accuracy: 0.9039
23616/60000 [==========>...................] - ETA: 1:09 - loss: 0.3080 - categorical_accuracy: 0.9040
23648/60000 [==========>...................] - ETA: 1:09 - loss: 0.3076 - categorical_accuracy: 0.9041
23680/60000 [==========>...................] - ETA: 1:09 - loss: 0.3076 - categorical_accuracy: 0.9042
23712/60000 [==========>...................] - ETA: 1:09 - loss: 0.3074 - categorical_accuracy: 0.9042
23744/60000 [==========>...................] - ETA: 1:09 - loss: 0.3073 - categorical_accuracy: 0.9042
23776/60000 [==========>...................] - ETA: 1:09 - loss: 0.3069 - categorical_accuracy: 0.9044
23808/60000 [==========>...................] - ETA: 1:09 - loss: 0.3067 - categorical_accuracy: 0.9044
23840/60000 [==========>...................] - ETA: 1:09 - loss: 0.3064 - categorical_accuracy: 0.9045
23872/60000 [==========>...................] - ETA: 1:09 - loss: 0.3060 - categorical_accuracy: 0.9046
23904/60000 [==========>...................] - ETA: 1:09 - loss: 0.3060 - categorical_accuracy: 0.9046
23936/60000 [==========>...................] - ETA: 1:08 - loss: 0.3056 - categorical_accuracy: 0.9047
23968/60000 [==========>...................] - ETA: 1:08 - loss: 0.3055 - categorical_accuracy: 0.9047
24000/60000 [===========>..................] - ETA: 1:08 - loss: 0.3052 - categorical_accuracy: 0.9048
24032/60000 [===========>..................] - ETA: 1:08 - loss: 0.3049 - categorical_accuracy: 0.9050
24064/60000 [===========>..................] - ETA: 1:08 - loss: 0.3046 - categorical_accuracy: 0.9050
24096/60000 [===========>..................] - ETA: 1:08 - loss: 0.3052 - categorical_accuracy: 0.9049
24128/60000 [===========>..................] - ETA: 1:08 - loss: 0.3050 - categorical_accuracy: 0.9049
24160/60000 [===========>..................] - ETA: 1:08 - loss: 0.3047 - categorical_accuracy: 0.9050
24192/60000 [===========>..................] - ETA: 1:08 - loss: 0.3044 - categorical_accuracy: 0.9051
24224/60000 [===========>..................] - ETA: 1:08 - loss: 0.3040 - categorical_accuracy: 0.9052
24256/60000 [===========>..................] - ETA: 1:08 - loss: 0.3037 - categorical_accuracy: 0.9053
24288/60000 [===========>..................] - ETA: 1:08 - loss: 0.3033 - categorical_accuracy: 0.9055
24320/60000 [===========>..................] - ETA: 1:08 - loss: 0.3031 - categorical_accuracy: 0.9056
24352/60000 [===========>..................] - ETA: 1:08 - loss: 0.3028 - categorical_accuracy: 0.9057
24384/60000 [===========>..................] - ETA: 1:08 - loss: 0.3025 - categorical_accuracy: 0.9057
24416/60000 [===========>..................] - ETA: 1:08 - loss: 0.3024 - categorical_accuracy: 0.9058
24448/60000 [===========>..................] - ETA: 1:07 - loss: 0.3022 - categorical_accuracy: 0.9058
24480/60000 [===========>..................] - ETA: 1:07 - loss: 0.3021 - categorical_accuracy: 0.9058
24512/60000 [===========>..................] - ETA: 1:07 - loss: 0.3018 - categorical_accuracy: 0.9059
24544/60000 [===========>..................] - ETA: 1:07 - loss: 0.3018 - categorical_accuracy: 0.9059
24576/60000 [===========>..................] - ETA: 1:07 - loss: 0.3017 - categorical_accuracy: 0.9059
24608/60000 [===========>..................] - ETA: 1:07 - loss: 0.3014 - categorical_accuracy: 0.9060
24640/60000 [===========>..................] - ETA: 1:07 - loss: 0.3011 - categorical_accuracy: 0.9061
24672/60000 [===========>..................] - ETA: 1:07 - loss: 0.3008 - categorical_accuracy: 0.9062
24704/60000 [===========>..................] - ETA: 1:07 - loss: 0.3011 - categorical_accuracy: 0.9062
24736/60000 [===========>..................] - ETA: 1:07 - loss: 0.3008 - categorical_accuracy: 0.9063
24768/60000 [===========>..................] - ETA: 1:07 - loss: 0.3004 - categorical_accuracy: 0.9064
24800/60000 [===========>..................] - ETA: 1:07 - loss: 0.3002 - categorical_accuracy: 0.9065
24832/60000 [===========>..................] - ETA: 1:07 - loss: 0.2999 - categorical_accuracy: 0.9065
24864/60000 [===========>..................] - ETA: 1:07 - loss: 0.2998 - categorical_accuracy: 0.9066
24896/60000 [===========>..................] - ETA: 1:07 - loss: 0.2997 - categorical_accuracy: 0.9065
24928/60000 [===========>..................] - ETA: 1:07 - loss: 0.2995 - categorical_accuracy: 0.9066
24960/60000 [===========>..................] - ETA: 1:06 - loss: 0.2992 - categorical_accuracy: 0.9067
24992/60000 [===========>..................] - ETA: 1:06 - loss: 0.2992 - categorical_accuracy: 0.9067
25024/60000 [===========>..................] - ETA: 1:06 - loss: 0.2989 - categorical_accuracy: 0.9068
25056/60000 [===========>..................] - ETA: 1:06 - loss: 0.2987 - categorical_accuracy: 0.9069
25088/60000 [===========>..................] - ETA: 1:06 - loss: 0.2986 - categorical_accuracy: 0.9069
25120/60000 [===========>..................] - ETA: 1:06 - loss: 0.2983 - categorical_accuracy: 0.9070
25152/60000 [===========>..................] - ETA: 1:06 - loss: 0.2981 - categorical_accuracy: 0.9070
25184/60000 [===========>..................] - ETA: 1:06 - loss: 0.2981 - categorical_accuracy: 0.9071
25216/60000 [===========>..................] - ETA: 1:06 - loss: 0.2979 - categorical_accuracy: 0.9072
25248/60000 [===========>..................] - ETA: 1:06 - loss: 0.2976 - categorical_accuracy: 0.9072
25280/60000 [===========>..................] - ETA: 1:06 - loss: 0.2979 - categorical_accuracy: 0.9072
25312/60000 [===========>..................] - ETA: 1:06 - loss: 0.2977 - categorical_accuracy: 0.9073
25344/60000 [===========>..................] - ETA: 1:06 - loss: 0.2974 - categorical_accuracy: 0.9074
25376/60000 [===========>..................] - ETA: 1:06 - loss: 0.2972 - categorical_accuracy: 0.9074
25408/60000 [===========>..................] - ETA: 1:06 - loss: 0.2970 - categorical_accuracy: 0.9075
25440/60000 [===========>..................] - ETA: 1:06 - loss: 0.2970 - categorical_accuracy: 0.9075
25472/60000 [===========>..................] - ETA: 1:05 - loss: 0.2969 - categorical_accuracy: 0.9075
25504/60000 [===========>..................] - ETA: 1:05 - loss: 0.2966 - categorical_accuracy: 0.9076
25536/60000 [===========>..................] - ETA: 1:05 - loss: 0.2968 - categorical_accuracy: 0.9075
25568/60000 [===========>..................] - ETA: 1:05 - loss: 0.2965 - categorical_accuracy: 0.9076
25600/60000 [===========>..................] - ETA: 1:05 - loss: 0.2963 - categorical_accuracy: 0.9077
25632/60000 [===========>..................] - ETA: 1:05 - loss: 0.2964 - categorical_accuracy: 0.9077
25664/60000 [===========>..................] - ETA: 1:05 - loss: 0.2962 - categorical_accuracy: 0.9078
25696/60000 [===========>..................] - ETA: 1:05 - loss: 0.2960 - categorical_accuracy: 0.9078
25728/60000 [===========>..................] - ETA: 1:05 - loss: 0.2957 - categorical_accuracy: 0.9079
25760/60000 [===========>..................] - ETA: 1:05 - loss: 0.2956 - categorical_accuracy: 0.9080
25792/60000 [===========>..................] - ETA: 1:05 - loss: 0.2953 - categorical_accuracy: 0.9081
25824/60000 [===========>..................] - ETA: 1:05 - loss: 0.2950 - categorical_accuracy: 0.9081
25856/60000 [===========>..................] - ETA: 1:05 - loss: 0.2947 - categorical_accuracy: 0.9083
25888/60000 [===========>..................] - ETA: 1:05 - loss: 0.2945 - categorical_accuracy: 0.9083
25920/60000 [===========>..................] - ETA: 1:05 - loss: 0.2947 - categorical_accuracy: 0.9083
25952/60000 [===========>..................] - ETA: 1:05 - loss: 0.2943 - categorical_accuracy: 0.9084
25984/60000 [===========>..................] - ETA: 1:04 - loss: 0.2940 - categorical_accuracy: 0.9086
26016/60000 [============>.................] - ETA: 1:04 - loss: 0.2939 - categorical_accuracy: 0.9086
26048/60000 [============>.................] - ETA: 1:04 - loss: 0.2937 - categorical_accuracy: 0.9087
26080/60000 [============>.................] - ETA: 1:04 - loss: 0.2934 - categorical_accuracy: 0.9088
26112/60000 [============>.................] - ETA: 1:04 - loss: 0.2932 - categorical_accuracy: 0.9089
26144/60000 [============>.................] - ETA: 1:04 - loss: 0.2932 - categorical_accuracy: 0.9089
26176/60000 [============>.................] - ETA: 1:04 - loss: 0.2931 - categorical_accuracy: 0.9089
26208/60000 [============>.................] - ETA: 1:04 - loss: 0.2929 - categorical_accuracy: 0.9089
26240/60000 [============>.................] - ETA: 1:04 - loss: 0.2927 - categorical_accuracy: 0.9090
26272/60000 [============>.................] - ETA: 1:04 - loss: 0.2924 - categorical_accuracy: 0.9091
26304/60000 [============>.................] - ETA: 1:04 - loss: 0.2921 - categorical_accuracy: 0.9092
26336/60000 [============>.................] - ETA: 1:04 - loss: 0.2919 - categorical_accuracy: 0.9092
26368/60000 [============>.................] - ETA: 1:04 - loss: 0.2917 - categorical_accuracy: 0.9093
26400/60000 [============>.................] - ETA: 1:04 - loss: 0.2916 - categorical_accuracy: 0.9093
26432/60000 [============>.................] - ETA: 1:04 - loss: 0.2913 - categorical_accuracy: 0.9094
26464/60000 [============>.................] - ETA: 1:04 - loss: 0.2912 - categorical_accuracy: 0.9094
26496/60000 [============>.................] - ETA: 1:03 - loss: 0.2910 - categorical_accuracy: 0.9095
26528/60000 [============>.................] - ETA: 1:03 - loss: 0.2907 - categorical_accuracy: 0.9095
26560/60000 [============>.................] - ETA: 1:03 - loss: 0.2905 - categorical_accuracy: 0.9096
26592/60000 [============>.................] - ETA: 1:03 - loss: 0.2901 - categorical_accuracy: 0.9097
26624/60000 [============>.................] - ETA: 1:03 - loss: 0.2899 - categorical_accuracy: 0.9098
26656/60000 [============>.................] - ETA: 1:03 - loss: 0.2896 - categorical_accuracy: 0.9099
26688/60000 [============>.................] - ETA: 1:03 - loss: 0.2893 - categorical_accuracy: 0.9100
26720/60000 [============>.................] - ETA: 1:03 - loss: 0.2890 - categorical_accuracy: 0.9101
26752/60000 [============>.................] - ETA: 1:03 - loss: 0.2888 - categorical_accuracy: 0.9101
26784/60000 [============>.................] - ETA: 1:03 - loss: 0.2887 - categorical_accuracy: 0.9102
26816/60000 [============>.................] - ETA: 1:03 - loss: 0.2884 - categorical_accuracy: 0.9102
26848/60000 [============>.................] - ETA: 1:03 - loss: 0.2881 - categorical_accuracy: 0.9103
26880/60000 [============>.................] - ETA: 1:03 - loss: 0.2880 - categorical_accuracy: 0.9103
26912/60000 [============>.................] - ETA: 1:03 - loss: 0.2877 - categorical_accuracy: 0.9104
26944/60000 [============>.................] - ETA: 1:03 - loss: 0.2879 - categorical_accuracy: 0.9104
26976/60000 [============>.................] - ETA: 1:02 - loss: 0.2879 - categorical_accuracy: 0.9104
27008/60000 [============>.................] - ETA: 1:02 - loss: 0.2877 - categorical_accuracy: 0.9105
27040/60000 [============>.................] - ETA: 1:02 - loss: 0.2875 - categorical_accuracy: 0.9105
27072/60000 [============>.................] - ETA: 1:02 - loss: 0.2874 - categorical_accuracy: 0.9105
27104/60000 [============>.................] - ETA: 1:02 - loss: 0.2873 - categorical_accuracy: 0.9105
27136/60000 [============>.................] - ETA: 1:02 - loss: 0.2870 - categorical_accuracy: 0.9106
27168/60000 [============>.................] - ETA: 1:02 - loss: 0.2866 - categorical_accuracy: 0.9107
27200/60000 [============>.................] - ETA: 1:02 - loss: 0.2864 - categorical_accuracy: 0.9107
27232/60000 [============>.................] - ETA: 1:02 - loss: 0.2862 - categorical_accuracy: 0.9108
27264/60000 [============>.................] - ETA: 1:02 - loss: 0.2859 - categorical_accuracy: 0.9109
27296/60000 [============>.................] - ETA: 1:02 - loss: 0.2857 - categorical_accuracy: 0.9109
27328/60000 [============>.................] - ETA: 1:02 - loss: 0.2854 - categorical_accuracy: 0.9110
27360/60000 [============>.................] - ETA: 1:02 - loss: 0.2852 - categorical_accuracy: 0.9111
27392/60000 [============>.................] - ETA: 1:02 - loss: 0.2849 - categorical_accuracy: 0.9112
27424/60000 [============>.................] - ETA: 1:02 - loss: 0.2846 - categorical_accuracy: 0.9113
27456/60000 [============>.................] - ETA: 1:02 - loss: 0.2843 - categorical_accuracy: 0.9113
27488/60000 [============>.................] - ETA: 1:02 - loss: 0.2841 - categorical_accuracy: 0.9114
27520/60000 [============>.................] - ETA: 1:01 - loss: 0.2840 - categorical_accuracy: 0.9114
27552/60000 [============>.................] - ETA: 1:01 - loss: 0.2838 - categorical_accuracy: 0.9114
27584/60000 [============>.................] - ETA: 1:01 - loss: 0.2835 - categorical_accuracy: 0.9115
27616/60000 [============>.................] - ETA: 1:01 - loss: 0.2833 - categorical_accuracy: 0.9116
27648/60000 [============>.................] - ETA: 1:01 - loss: 0.2830 - categorical_accuracy: 0.9117
27680/60000 [============>.................] - ETA: 1:01 - loss: 0.2827 - categorical_accuracy: 0.9118
27712/60000 [============>.................] - ETA: 1:01 - loss: 0.2826 - categorical_accuracy: 0.9118
27744/60000 [============>.................] - ETA: 1:01 - loss: 0.2823 - categorical_accuracy: 0.9119
27776/60000 [============>.................] - ETA: 1:01 - loss: 0.2822 - categorical_accuracy: 0.9120
27808/60000 [============>.................] - ETA: 1:01 - loss: 0.2819 - categorical_accuracy: 0.9121
27840/60000 [============>.................] - ETA: 1:01 - loss: 0.2817 - categorical_accuracy: 0.9121
27872/60000 [============>.................] - ETA: 1:01 - loss: 0.2815 - categorical_accuracy: 0.9122
27904/60000 [============>.................] - ETA: 1:01 - loss: 0.2812 - categorical_accuracy: 0.9123
27936/60000 [============>.................] - ETA: 1:01 - loss: 0.2809 - categorical_accuracy: 0.9124
27968/60000 [============>.................] - ETA: 1:01 - loss: 0.2807 - categorical_accuracy: 0.9125
28000/60000 [=============>................] - ETA: 1:01 - loss: 0.2804 - categorical_accuracy: 0.9126
28032/60000 [=============>................] - ETA: 1:00 - loss: 0.2801 - categorical_accuracy: 0.9127
28064/60000 [=============>................] - ETA: 1:00 - loss: 0.2798 - categorical_accuracy: 0.9128
28096/60000 [=============>................] - ETA: 1:00 - loss: 0.2798 - categorical_accuracy: 0.9128
28128/60000 [=============>................] - ETA: 1:00 - loss: 0.2795 - categorical_accuracy: 0.9129
28160/60000 [=============>................] - ETA: 1:00 - loss: 0.2793 - categorical_accuracy: 0.9130
28192/60000 [=============>................] - ETA: 1:00 - loss: 0.2791 - categorical_accuracy: 0.9130
28224/60000 [=============>................] - ETA: 1:00 - loss: 0.2791 - categorical_accuracy: 0.9131
28256/60000 [=============>................] - ETA: 1:00 - loss: 0.2788 - categorical_accuracy: 0.9132
28288/60000 [=============>................] - ETA: 1:00 - loss: 0.2788 - categorical_accuracy: 0.9131
28320/60000 [=============>................] - ETA: 1:00 - loss: 0.2786 - categorical_accuracy: 0.9132
28352/60000 [=============>................] - ETA: 1:00 - loss: 0.2785 - categorical_accuracy: 0.9132
28384/60000 [=============>................] - ETA: 1:00 - loss: 0.2782 - categorical_accuracy: 0.9133
28416/60000 [=============>................] - ETA: 1:00 - loss: 0.2781 - categorical_accuracy: 0.9132
28448/60000 [=============>................] - ETA: 1:00 - loss: 0.2781 - categorical_accuracy: 0.9132
28480/60000 [=============>................] - ETA: 1:00 - loss: 0.2780 - categorical_accuracy: 0.9132
28512/60000 [=============>................] - ETA: 1:00 - loss: 0.2779 - categorical_accuracy: 0.9133
28544/60000 [=============>................] - ETA: 59s - loss: 0.2778 - categorical_accuracy: 0.9133 
28576/60000 [=============>................] - ETA: 59s - loss: 0.2776 - categorical_accuracy: 0.9134
28608/60000 [=============>................] - ETA: 59s - loss: 0.2776 - categorical_accuracy: 0.9134
28640/60000 [=============>................] - ETA: 59s - loss: 0.2774 - categorical_accuracy: 0.9135
28672/60000 [=============>................] - ETA: 59s - loss: 0.2771 - categorical_accuracy: 0.9135
28704/60000 [=============>................] - ETA: 59s - loss: 0.2770 - categorical_accuracy: 0.9136
28736/60000 [=============>................] - ETA: 59s - loss: 0.2767 - categorical_accuracy: 0.9137
28768/60000 [=============>................] - ETA: 59s - loss: 0.2765 - categorical_accuracy: 0.9138
28800/60000 [=============>................] - ETA: 59s - loss: 0.2763 - categorical_accuracy: 0.9138
28832/60000 [=============>................] - ETA: 59s - loss: 0.2760 - categorical_accuracy: 0.9139
28864/60000 [=============>................] - ETA: 59s - loss: 0.2759 - categorical_accuracy: 0.9140
28896/60000 [=============>................] - ETA: 59s - loss: 0.2756 - categorical_accuracy: 0.9141
28928/60000 [=============>................] - ETA: 59s - loss: 0.2754 - categorical_accuracy: 0.9142
28960/60000 [=============>................] - ETA: 59s - loss: 0.2752 - categorical_accuracy: 0.9142
28992/60000 [=============>................] - ETA: 59s - loss: 0.2752 - categorical_accuracy: 0.9143
29024/60000 [=============>................] - ETA: 59s - loss: 0.2750 - categorical_accuracy: 0.9144
29056/60000 [=============>................] - ETA: 58s - loss: 0.2747 - categorical_accuracy: 0.9145
29088/60000 [=============>................] - ETA: 58s - loss: 0.2747 - categorical_accuracy: 0.9145
29120/60000 [=============>................] - ETA: 58s - loss: 0.2745 - categorical_accuracy: 0.9146
29152/60000 [=============>................] - ETA: 58s - loss: 0.2743 - categorical_accuracy: 0.9146
29184/60000 [=============>................] - ETA: 58s - loss: 0.2745 - categorical_accuracy: 0.9146
29216/60000 [=============>................] - ETA: 58s - loss: 0.2742 - categorical_accuracy: 0.9147
29248/60000 [=============>................] - ETA: 58s - loss: 0.2739 - categorical_accuracy: 0.9148
29280/60000 [=============>................] - ETA: 58s - loss: 0.2737 - categorical_accuracy: 0.9149
29312/60000 [=============>................] - ETA: 58s - loss: 0.2734 - categorical_accuracy: 0.9149
29344/60000 [=============>................] - ETA: 58s - loss: 0.2731 - categorical_accuracy: 0.9150
29376/60000 [=============>................] - ETA: 58s - loss: 0.2730 - categorical_accuracy: 0.9151
29408/60000 [=============>................] - ETA: 58s - loss: 0.2733 - categorical_accuracy: 0.9150
29440/60000 [=============>................] - ETA: 58s - loss: 0.2730 - categorical_accuracy: 0.9151
29472/60000 [=============>................] - ETA: 58s - loss: 0.2728 - categorical_accuracy: 0.9152
29504/60000 [=============>................] - ETA: 58s - loss: 0.2728 - categorical_accuracy: 0.9153
29536/60000 [=============>................] - ETA: 58s - loss: 0.2726 - categorical_accuracy: 0.9153
29568/60000 [=============>................] - ETA: 57s - loss: 0.2724 - categorical_accuracy: 0.9154
29600/60000 [=============>................] - ETA: 57s - loss: 0.2721 - categorical_accuracy: 0.9154
29632/60000 [=============>................] - ETA: 57s - loss: 0.2721 - categorical_accuracy: 0.9154
29664/60000 [=============>................] - ETA: 57s - loss: 0.2718 - categorical_accuracy: 0.9155
29696/60000 [=============>................] - ETA: 57s - loss: 0.2716 - categorical_accuracy: 0.9156
29728/60000 [=============>................] - ETA: 57s - loss: 0.2715 - categorical_accuracy: 0.9156
29760/60000 [=============>................] - ETA: 57s - loss: 0.2712 - categorical_accuracy: 0.9157
29792/60000 [=============>................] - ETA: 57s - loss: 0.2711 - categorical_accuracy: 0.9157
29824/60000 [=============>................] - ETA: 57s - loss: 0.2710 - categorical_accuracy: 0.9158
29856/60000 [=============>................] - ETA: 57s - loss: 0.2707 - categorical_accuracy: 0.9159
29888/60000 [=============>................] - ETA: 57s - loss: 0.2706 - categorical_accuracy: 0.9159
29920/60000 [=============>................] - ETA: 57s - loss: 0.2704 - categorical_accuracy: 0.9160
29952/60000 [=============>................] - ETA: 57s - loss: 0.2704 - categorical_accuracy: 0.9160
29984/60000 [=============>................] - ETA: 57s - loss: 0.2701 - categorical_accuracy: 0.9161
30016/60000 [==============>...............] - ETA: 57s - loss: 0.2701 - categorical_accuracy: 0.9161
30048/60000 [==============>...............] - ETA: 57s - loss: 0.2699 - categorical_accuracy: 0.9161
30080/60000 [==============>...............] - ETA: 56s - loss: 0.2700 - categorical_accuracy: 0.9162
30112/60000 [==============>...............] - ETA: 56s - loss: 0.2698 - categorical_accuracy: 0.9162
30144/60000 [==============>...............] - ETA: 56s - loss: 0.2695 - categorical_accuracy: 0.9163
30176/60000 [==============>...............] - ETA: 56s - loss: 0.2693 - categorical_accuracy: 0.9164
30208/60000 [==============>...............] - ETA: 56s - loss: 0.2691 - categorical_accuracy: 0.9164
30240/60000 [==============>...............] - ETA: 56s - loss: 0.2689 - categorical_accuracy: 0.9165
30272/60000 [==============>...............] - ETA: 56s - loss: 0.2686 - categorical_accuracy: 0.9166
30304/60000 [==============>...............] - ETA: 56s - loss: 0.2685 - categorical_accuracy: 0.9166
30336/60000 [==============>...............] - ETA: 56s - loss: 0.2682 - categorical_accuracy: 0.9167
30368/60000 [==============>...............] - ETA: 56s - loss: 0.2680 - categorical_accuracy: 0.9168
30400/60000 [==============>...............] - ETA: 56s - loss: 0.2681 - categorical_accuracy: 0.9168
30432/60000 [==============>...............] - ETA: 56s - loss: 0.2681 - categorical_accuracy: 0.9168
30464/60000 [==============>...............] - ETA: 56s - loss: 0.2680 - categorical_accuracy: 0.9169
30496/60000 [==============>...............] - ETA: 56s - loss: 0.2678 - categorical_accuracy: 0.9169
30528/60000 [==============>...............] - ETA: 56s - loss: 0.2675 - categorical_accuracy: 0.9170
30560/60000 [==============>...............] - ETA: 56s - loss: 0.2674 - categorical_accuracy: 0.9170
30592/60000 [==============>...............] - ETA: 56s - loss: 0.2673 - categorical_accuracy: 0.9170
30624/60000 [==============>...............] - ETA: 55s - loss: 0.2673 - categorical_accuracy: 0.9170
30656/60000 [==============>...............] - ETA: 55s - loss: 0.2671 - categorical_accuracy: 0.9171
30688/60000 [==============>...............] - ETA: 55s - loss: 0.2669 - categorical_accuracy: 0.9172
30720/60000 [==============>...............] - ETA: 55s - loss: 0.2670 - categorical_accuracy: 0.9172
30752/60000 [==============>...............] - ETA: 55s - loss: 0.2668 - categorical_accuracy: 0.9172
30784/60000 [==============>...............] - ETA: 55s - loss: 0.2666 - categorical_accuracy: 0.9173
30816/60000 [==============>...............] - ETA: 55s - loss: 0.2666 - categorical_accuracy: 0.9173
30848/60000 [==============>...............] - ETA: 55s - loss: 0.2664 - categorical_accuracy: 0.9174
30880/60000 [==============>...............] - ETA: 55s - loss: 0.2662 - categorical_accuracy: 0.9174
30912/60000 [==============>...............] - ETA: 55s - loss: 0.2661 - categorical_accuracy: 0.9174
30944/60000 [==============>...............] - ETA: 55s - loss: 0.2659 - categorical_accuracy: 0.9175
30976/60000 [==============>...............] - ETA: 55s - loss: 0.2657 - categorical_accuracy: 0.9175
31008/60000 [==============>...............] - ETA: 55s - loss: 0.2657 - categorical_accuracy: 0.9175
31040/60000 [==============>...............] - ETA: 55s - loss: 0.2657 - categorical_accuracy: 0.9176
31072/60000 [==============>...............] - ETA: 55s - loss: 0.2655 - categorical_accuracy: 0.9177
31104/60000 [==============>...............] - ETA: 55s - loss: 0.2652 - categorical_accuracy: 0.9178
31136/60000 [==============>...............] - ETA: 54s - loss: 0.2651 - categorical_accuracy: 0.9178
31168/60000 [==============>...............] - ETA: 54s - loss: 0.2650 - categorical_accuracy: 0.9178
31200/60000 [==============>...............] - ETA: 54s - loss: 0.2648 - categorical_accuracy: 0.9179
31232/60000 [==============>...............] - ETA: 54s - loss: 0.2646 - categorical_accuracy: 0.9180
31264/60000 [==============>...............] - ETA: 54s - loss: 0.2643 - categorical_accuracy: 0.9181
31296/60000 [==============>...............] - ETA: 54s - loss: 0.2642 - categorical_accuracy: 0.9181
31328/60000 [==============>...............] - ETA: 54s - loss: 0.2639 - categorical_accuracy: 0.9182
31360/60000 [==============>...............] - ETA: 54s - loss: 0.2638 - categorical_accuracy: 0.9183
31392/60000 [==============>...............] - ETA: 54s - loss: 0.2638 - categorical_accuracy: 0.9183
31424/60000 [==============>...............] - ETA: 54s - loss: 0.2636 - categorical_accuracy: 0.9183
31456/60000 [==============>...............] - ETA: 54s - loss: 0.2635 - categorical_accuracy: 0.9183
31488/60000 [==============>...............] - ETA: 54s - loss: 0.2634 - categorical_accuracy: 0.9184
31520/60000 [==============>...............] - ETA: 54s - loss: 0.2632 - categorical_accuracy: 0.9184
31552/60000 [==============>...............] - ETA: 54s - loss: 0.2630 - categorical_accuracy: 0.9185
31584/60000 [==============>...............] - ETA: 54s - loss: 0.2630 - categorical_accuracy: 0.9185
31616/60000 [==============>...............] - ETA: 54s - loss: 0.2632 - categorical_accuracy: 0.9184
31648/60000 [==============>...............] - ETA: 53s - loss: 0.2630 - categorical_accuracy: 0.9184
31680/60000 [==============>...............] - ETA: 53s - loss: 0.2629 - categorical_accuracy: 0.9185
31712/60000 [==============>...............] - ETA: 53s - loss: 0.2626 - categorical_accuracy: 0.9185
31744/60000 [==============>...............] - ETA: 53s - loss: 0.2624 - categorical_accuracy: 0.9186
31776/60000 [==============>...............] - ETA: 53s - loss: 0.2624 - categorical_accuracy: 0.9186
31808/60000 [==============>...............] - ETA: 53s - loss: 0.2624 - categorical_accuracy: 0.9186
31840/60000 [==============>...............] - ETA: 53s - loss: 0.2622 - categorical_accuracy: 0.9187
31872/60000 [==============>...............] - ETA: 53s - loss: 0.2620 - categorical_accuracy: 0.9187
31904/60000 [==============>...............] - ETA: 53s - loss: 0.2618 - categorical_accuracy: 0.9188
31936/60000 [==============>...............] - ETA: 53s - loss: 0.2617 - categorical_accuracy: 0.9189
31968/60000 [==============>...............] - ETA: 53s - loss: 0.2614 - categorical_accuracy: 0.9190
32000/60000 [===============>..............] - ETA: 53s - loss: 0.2614 - categorical_accuracy: 0.9190
32032/60000 [===============>..............] - ETA: 53s - loss: 0.2612 - categorical_accuracy: 0.9190
32064/60000 [===============>..............] - ETA: 53s - loss: 0.2609 - categorical_accuracy: 0.9191
32096/60000 [===============>..............] - ETA: 53s - loss: 0.2609 - categorical_accuracy: 0.9191
32128/60000 [===============>..............] - ETA: 53s - loss: 0.2607 - categorical_accuracy: 0.9192
32160/60000 [===============>..............] - ETA: 53s - loss: 0.2609 - categorical_accuracy: 0.9192
32192/60000 [===============>..............] - ETA: 52s - loss: 0.2607 - categorical_accuracy: 0.9192
32224/60000 [===============>..............] - ETA: 52s - loss: 0.2605 - categorical_accuracy: 0.9193
32256/60000 [===============>..............] - ETA: 52s - loss: 0.2604 - categorical_accuracy: 0.9193
32288/60000 [===============>..............] - ETA: 52s - loss: 0.2602 - categorical_accuracy: 0.9194
32320/60000 [===============>..............] - ETA: 52s - loss: 0.2600 - categorical_accuracy: 0.9194
32352/60000 [===============>..............] - ETA: 52s - loss: 0.2598 - categorical_accuracy: 0.9195
32384/60000 [===============>..............] - ETA: 52s - loss: 0.2597 - categorical_accuracy: 0.9195
32416/60000 [===============>..............] - ETA: 52s - loss: 0.2595 - categorical_accuracy: 0.9196
32448/60000 [===============>..............] - ETA: 52s - loss: 0.2593 - categorical_accuracy: 0.9197
32480/60000 [===============>..............] - ETA: 52s - loss: 0.2592 - categorical_accuracy: 0.9197
32512/60000 [===============>..............] - ETA: 52s - loss: 0.2593 - categorical_accuracy: 0.9197
32544/60000 [===============>..............] - ETA: 52s - loss: 0.2593 - categorical_accuracy: 0.9197
32576/60000 [===============>..............] - ETA: 52s - loss: 0.2592 - categorical_accuracy: 0.9198
32608/60000 [===============>..............] - ETA: 52s - loss: 0.2592 - categorical_accuracy: 0.9198
32640/60000 [===============>..............] - ETA: 52s - loss: 0.2591 - categorical_accuracy: 0.9198
32672/60000 [===============>..............] - ETA: 52s - loss: 0.2589 - categorical_accuracy: 0.9199
32704/60000 [===============>..............] - ETA: 51s - loss: 0.2587 - categorical_accuracy: 0.9199
32736/60000 [===============>..............] - ETA: 51s - loss: 0.2586 - categorical_accuracy: 0.9199
32768/60000 [===============>..............] - ETA: 51s - loss: 0.2585 - categorical_accuracy: 0.9200
32800/60000 [===============>..............] - ETA: 51s - loss: 0.2583 - categorical_accuracy: 0.9200
32832/60000 [===============>..............] - ETA: 51s - loss: 0.2583 - categorical_accuracy: 0.9200
32864/60000 [===============>..............] - ETA: 51s - loss: 0.2581 - categorical_accuracy: 0.9201
32896/60000 [===============>..............] - ETA: 51s - loss: 0.2580 - categorical_accuracy: 0.9201
32928/60000 [===============>..............] - ETA: 51s - loss: 0.2581 - categorical_accuracy: 0.9201
32960/60000 [===============>..............] - ETA: 51s - loss: 0.2579 - categorical_accuracy: 0.9201
32992/60000 [===============>..............] - ETA: 51s - loss: 0.2578 - categorical_accuracy: 0.9202
33024/60000 [===============>..............] - ETA: 51s - loss: 0.2578 - categorical_accuracy: 0.9202
33056/60000 [===============>..............] - ETA: 51s - loss: 0.2576 - categorical_accuracy: 0.9203
33088/60000 [===============>..............] - ETA: 51s - loss: 0.2574 - categorical_accuracy: 0.9204
33120/60000 [===============>..............] - ETA: 51s - loss: 0.2572 - categorical_accuracy: 0.9204
33152/60000 [===============>..............] - ETA: 51s - loss: 0.2570 - categorical_accuracy: 0.9205
33184/60000 [===============>..............] - ETA: 51s - loss: 0.2568 - categorical_accuracy: 0.9206
33216/60000 [===============>..............] - ETA: 51s - loss: 0.2566 - categorical_accuracy: 0.9206
33248/60000 [===============>..............] - ETA: 50s - loss: 0.2564 - categorical_accuracy: 0.9207
33280/60000 [===============>..............] - ETA: 50s - loss: 0.2562 - categorical_accuracy: 0.9208
33312/60000 [===============>..............] - ETA: 50s - loss: 0.2560 - categorical_accuracy: 0.9208
33344/60000 [===============>..............] - ETA: 50s - loss: 0.2559 - categorical_accuracy: 0.9209
33376/60000 [===============>..............] - ETA: 50s - loss: 0.2557 - categorical_accuracy: 0.9210
33408/60000 [===============>..............] - ETA: 50s - loss: 0.2555 - categorical_accuracy: 0.9210
33440/60000 [===============>..............] - ETA: 50s - loss: 0.2555 - categorical_accuracy: 0.9210
33472/60000 [===============>..............] - ETA: 50s - loss: 0.2554 - categorical_accuracy: 0.9211
33504/60000 [===============>..............] - ETA: 50s - loss: 0.2553 - categorical_accuracy: 0.9211
33536/60000 [===============>..............] - ETA: 50s - loss: 0.2551 - categorical_accuracy: 0.9211
33568/60000 [===============>..............] - ETA: 50s - loss: 0.2550 - categorical_accuracy: 0.9211
33600/60000 [===============>..............] - ETA: 50s - loss: 0.2550 - categorical_accuracy: 0.9211
33632/60000 [===============>..............] - ETA: 50s - loss: 0.2547 - categorical_accuracy: 0.9212
33664/60000 [===============>..............] - ETA: 50s - loss: 0.2545 - categorical_accuracy: 0.9213
33696/60000 [===============>..............] - ETA: 50s - loss: 0.2544 - categorical_accuracy: 0.9213
33728/60000 [===============>..............] - ETA: 50s - loss: 0.2542 - categorical_accuracy: 0.9213
33760/60000 [===============>..............] - ETA: 49s - loss: 0.2540 - categorical_accuracy: 0.9214
33792/60000 [===============>..............] - ETA: 49s - loss: 0.2539 - categorical_accuracy: 0.9214
33824/60000 [===============>..............] - ETA: 49s - loss: 0.2538 - categorical_accuracy: 0.9214
33856/60000 [===============>..............] - ETA: 49s - loss: 0.2536 - categorical_accuracy: 0.9215
33888/60000 [===============>..............] - ETA: 49s - loss: 0.2535 - categorical_accuracy: 0.9215
33920/60000 [===============>..............] - ETA: 49s - loss: 0.2536 - categorical_accuracy: 0.9216
33952/60000 [===============>..............] - ETA: 49s - loss: 0.2535 - categorical_accuracy: 0.9216
33984/60000 [===============>..............] - ETA: 49s - loss: 0.2532 - categorical_accuracy: 0.9217
34016/60000 [================>.............] - ETA: 49s - loss: 0.2531 - categorical_accuracy: 0.9217
34048/60000 [================>.............] - ETA: 49s - loss: 0.2530 - categorical_accuracy: 0.9218
34080/60000 [================>.............] - ETA: 49s - loss: 0.2530 - categorical_accuracy: 0.9218
34112/60000 [================>.............] - ETA: 49s - loss: 0.2528 - categorical_accuracy: 0.9218
34144/60000 [================>.............] - ETA: 49s - loss: 0.2526 - categorical_accuracy: 0.9219
34176/60000 [================>.............] - ETA: 49s - loss: 0.2524 - categorical_accuracy: 0.9220
34208/60000 [================>.............] - ETA: 49s - loss: 0.2522 - categorical_accuracy: 0.9220
34240/60000 [================>.............] - ETA: 49s - loss: 0.2521 - categorical_accuracy: 0.9220
34272/60000 [================>.............] - ETA: 49s - loss: 0.2520 - categorical_accuracy: 0.9221
34304/60000 [================>.............] - ETA: 48s - loss: 0.2518 - categorical_accuracy: 0.9221
34336/60000 [================>.............] - ETA: 48s - loss: 0.2516 - categorical_accuracy: 0.9222
34368/60000 [================>.............] - ETA: 48s - loss: 0.2517 - categorical_accuracy: 0.9222
34400/60000 [================>.............] - ETA: 48s - loss: 0.2515 - categorical_accuracy: 0.9222
34432/60000 [================>.............] - ETA: 48s - loss: 0.2513 - categorical_accuracy: 0.9223
34464/60000 [================>.............] - ETA: 48s - loss: 0.2511 - categorical_accuracy: 0.9224
34496/60000 [================>.............] - ETA: 48s - loss: 0.2509 - categorical_accuracy: 0.9224
34528/60000 [================>.............] - ETA: 48s - loss: 0.2507 - categorical_accuracy: 0.9224
34560/60000 [================>.............] - ETA: 48s - loss: 0.2505 - categorical_accuracy: 0.9225
34592/60000 [================>.............] - ETA: 48s - loss: 0.2503 - categorical_accuracy: 0.9226
34624/60000 [================>.............] - ETA: 48s - loss: 0.2501 - categorical_accuracy: 0.9227
34656/60000 [================>.............] - ETA: 48s - loss: 0.2499 - categorical_accuracy: 0.9227
34688/60000 [================>.............] - ETA: 48s - loss: 0.2497 - categorical_accuracy: 0.9228
34720/60000 [================>.............] - ETA: 48s - loss: 0.2496 - categorical_accuracy: 0.9228
34752/60000 [================>.............] - ETA: 48s - loss: 0.2494 - categorical_accuracy: 0.9229
34784/60000 [================>.............] - ETA: 48s - loss: 0.2492 - categorical_accuracy: 0.9230
34816/60000 [================>.............] - ETA: 47s - loss: 0.2491 - categorical_accuracy: 0.9230
34848/60000 [================>.............] - ETA: 47s - loss: 0.2489 - categorical_accuracy: 0.9230
34880/60000 [================>.............] - ETA: 47s - loss: 0.2487 - categorical_accuracy: 0.9231
34912/60000 [================>.............] - ETA: 47s - loss: 0.2486 - categorical_accuracy: 0.9231
34944/60000 [================>.............] - ETA: 47s - loss: 0.2487 - categorical_accuracy: 0.9232
34976/60000 [================>.............] - ETA: 47s - loss: 0.2486 - categorical_accuracy: 0.9232
35008/60000 [================>.............] - ETA: 47s - loss: 0.2485 - categorical_accuracy: 0.9233
35040/60000 [================>.............] - ETA: 47s - loss: 0.2483 - categorical_accuracy: 0.9233
35072/60000 [================>.............] - ETA: 47s - loss: 0.2481 - categorical_accuracy: 0.9234
35104/60000 [================>.............] - ETA: 47s - loss: 0.2482 - categorical_accuracy: 0.9234
35136/60000 [================>.............] - ETA: 47s - loss: 0.2483 - categorical_accuracy: 0.9234
35168/60000 [================>.............] - ETA: 47s - loss: 0.2482 - categorical_accuracy: 0.9235
35200/60000 [================>.............] - ETA: 47s - loss: 0.2480 - categorical_accuracy: 0.9235
35232/60000 [================>.............] - ETA: 47s - loss: 0.2480 - categorical_accuracy: 0.9235
35264/60000 [================>.............] - ETA: 47s - loss: 0.2479 - categorical_accuracy: 0.9235
35296/60000 [================>.............] - ETA: 47s - loss: 0.2478 - categorical_accuracy: 0.9236
35328/60000 [================>.............] - ETA: 46s - loss: 0.2476 - categorical_accuracy: 0.9236
35360/60000 [================>.............] - ETA: 46s - loss: 0.2474 - categorical_accuracy: 0.9237
35392/60000 [================>.............] - ETA: 46s - loss: 0.2474 - categorical_accuracy: 0.9237
35424/60000 [================>.............] - ETA: 46s - loss: 0.2472 - categorical_accuracy: 0.9238
35456/60000 [================>.............] - ETA: 46s - loss: 0.2470 - categorical_accuracy: 0.9238
35488/60000 [================>.............] - ETA: 46s - loss: 0.2469 - categorical_accuracy: 0.9238
35520/60000 [================>.............] - ETA: 46s - loss: 0.2467 - categorical_accuracy: 0.9239
35552/60000 [================>.............] - ETA: 46s - loss: 0.2465 - categorical_accuracy: 0.9239
35584/60000 [================>.............] - ETA: 46s - loss: 0.2468 - categorical_accuracy: 0.9239
35616/60000 [================>.............] - ETA: 46s - loss: 0.2466 - categorical_accuracy: 0.9240
35648/60000 [================>.............] - ETA: 46s - loss: 0.2465 - categorical_accuracy: 0.9240
35680/60000 [================>.............] - ETA: 46s - loss: 0.2466 - categorical_accuracy: 0.9240
35712/60000 [================>.............] - ETA: 46s - loss: 0.2466 - categorical_accuracy: 0.9240
35744/60000 [================>.............] - ETA: 46s - loss: 0.2465 - categorical_accuracy: 0.9240
35776/60000 [================>.............] - ETA: 46s - loss: 0.2464 - categorical_accuracy: 0.9240
35808/60000 [================>.............] - ETA: 46s - loss: 0.2463 - categorical_accuracy: 0.9241
35840/60000 [================>.............] - ETA: 45s - loss: 0.2461 - categorical_accuracy: 0.9242
35872/60000 [================>.............] - ETA: 45s - loss: 0.2459 - categorical_accuracy: 0.9242
35904/60000 [================>.............] - ETA: 45s - loss: 0.2461 - categorical_accuracy: 0.9242
35936/60000 [================>.............] - ETA: 45s - loss: 0.2460 - categorical_accuracy: 0.9242
35968/60000 [================>.............] - ETA: 45s - loss: 0.2459 - categorical_accuracy: 0.9242
36000/60000 [=================>............] - ETA: 45s - loss: 0.2459 - categorical_accuracy: 0.9242
36032/60000 [=================>............] - ETA: 45s - loss: 0.2457 - categorical_accuracy: 0.9243
36064/60000 [=================>............] - ETA: 45s - loss: 0.2455 - categorical_accuracy: 0.9244
36096/60000 [=================>............] - ETA: 45s - loss: 0.2455 - categorical_accuracy: 0.9243
36128/60000 [=================>............] - ETA: 45s - loss: 0.2453 - categorical_accuracy: 0.9244
36160/60000 [=================>............] - ETA: 45s - loss: 0.2455 - categorical_accuracy: 0.9244
36192/60000 [=================>............] - ETA: 45s - loss: 0.2453 - categorical_accuracy: 0.9245
36224/60000 [=================>............] - ETA: 45s - loss: 0.2451 - categorical_accuracy: 0.9245
36256/60000 [=================>............] - ETA: 45s - loss: 0.2450 - categorical_accuracy: 0.9246
36288/60000 [=================>............] - ETA: 45s - loss: 0.2448 - categorical_accuracy: 0.9246
36320/60000 [=================>............] - ETA: 45s - loss: 0.2446 - categorical_accuracy: 0.9246
36352/60000 [=================>............] - ETA: 45s - loss: 0.2446 - categorical_accuracy: 0.9247
36384/60000 [=================>............] - ETA: 44s - loss: 0.2450 - categorical_accuracy: 0.9247
36416/60000 [=================>............] - ETA: 44s - loss: 0.2451 - categorical_accuracy: 0.9247
36448/60000 [=================>............] - ETA: 44s - loss: 0.2450 - categorical_accuracy: 0.9248
36480/60000 [=================>............] - ETA: 44s - loss: 0.2448 - categorical_accuracy: 0.9248
36512/60000 [=================>............] - ETA: 44s - loss: 0.2446 - categorical_accuracy: 0.9248
36544/60000 [=================>............] - ETA: 44s - loss: 0.2446 - categorical_accuracy: 0.9249
36576/60000 [=================>............] - ETA: 44s - loss: 0.2444 - categorical_accuracy: 0.9249
36608/60000 [=================>............] - ETA: 44s - loss: 0.2443 - categorical_accuracy: 0.9250
36640/60000 [=================>............] - ETA: 44s - loss: 0.2442 - categorical_accuracy: 0.9250
36672/60000 [=================>............] - ETA: 44s - loss: 0.2441 - categorical_accuracy: 0.9250
36704/60000 [=================>............] - ETA: 44s - loss: 0.2439 - categorical_accuracy: 0.9251
36736/60000 [=================>............] - ETA: 44s - loss: 0.2438 - categorical_accuracy: 0.9251
36768/60000 [=================>............] - ETA: 44s - loss: 0.2436 - categorical_accuracy: 0.9252
36800/60000 [=================>............] - ETA: 44s - loss: 0.2434 - categorical_accuracy: 0.9253
36832/60000 [=================>............] - ETA: 44s - loss: 0.2432 - categorical_accuracy: 0.9253
36864/60000 [=================>............] - ETA: 44s - loss: 0.2431 - categorical_accuracy: 0.9254
36896/60000 [=================>............] - ETA: 43s - loss: 0.2429 - categorical_accuracy: 0.9254
36928/60000 [=================>............] - ETA: 43s - loss: 0.2427 - categorical_accuracy: 0.9255
36960/60000 [=================>............] - ETA: 43s - loss: 0.2425 - categorical_accuracy: 0.9256
36992/60000 [=================>............] - ETA: 43s - loss: 0.2425 - categorical_accuracy: 0.9256
37024/60000 [=================>............] - ETA: 43s - loss: 0.2423 - categorical_accuracy: 0.9256
37056/60000 [=================>............] - ETA: 43s - loss: 0.2422 - categorical_accuracy: 0.9257
37088/60000 [=================>............] - ETA: 43s - loss: 0.2422 - categorical_accuracy: 0.9257
37120/60000 [=================>............] - ETA: 43s - loss: 0.2422 - categorical_accuracy: 0.9257
37152/60000 [=================>............] - ETA: 43s - loss: 0.2420 - categorical_accuracy: 0.9257
37184/60000 [=================>............] - ETA: 43s - loss: 0.2418 - categorical_accuracy: 0.9258
37216/60000 [=================>............] - ETA: 43s - loss: 0.2416 - categorical_accuracy: 0.9258
37248/60000 [=================>............] - ETA: 43s - loss: 0.2415 - categorical_accuracy: 0.9259
37280/60000 [=================>............] - ETA: 43s - loss: 0.2413 - categorical_accuracy: 0.9259
37312/60000 [=================>............] - ETA: 43s - loss: 0.2412 - categorical_accuracy: 0.9259
37344/60000 [=================>............] - ETA: 43s - loss: 0.2410 - categorical_accuracy: 0.9260
37376/60000 [=================>............] - ETA: 43s - loss: 0.2410 - categorical_accuracy: 0.9260
37408/60000 [=================>............] - ETA: 42s - loss: 0.2408 - categorical_accuracy: 0.9261
37440/60000 [=================>............] - ETA: 42s - loss: 0.2406 - categorical_accuracy: 0.9261
37472/60000 [=================>............] - ETA: 42s - loss: 0.2404 - categorical_accuracy: 0.9262
37504/60000 [=================>............] - ETA: 42s - loss: 0.2404 - categorical_accuracy: 0.9262
37536/60000 [=================>............] - ETA: 42s - loss: 0.2405 - categorical_accuracy: 0.9263
37568/60000 [=================>............] - ETA: 42s - loss: 0.2403 - categorical_accuracy: 0.9263
37600/60000 [=================>............] - ETA: 42s - loss: 0.2402 - categorical_accuracy: 0.9263
37632/60000 [=================>............] - ETA: 42s - loss: 0.2400 - categorical_accuracy: 0.9264
37664/60000 [=================>............] - ETA: 42s - loss: 0.2398 - categorical_accuracy: 0.9265
37696/60000 [=================>............] - ETA: 42s - loss: 0.2397 - categorical_accuracy: 0.9265
37728/60000 [=================>............] - ETA: 42s - loss: 0.2395 - categorical_accuracy: 0.9265
37760/60000 [=================>............] - ETA: 42s - loss: 0.2393 - categorical_accuracy: 0.9266
37792/60000 [=================>............] - ETA: 42s - loss: 0.2395 - categorical_accuracy: 0.9266
37824/60000 [=================>............] - ETA: 42s - loss: 0.2393 - categorical_accuracy: 0.9266
37856/60000 [=================>............] - ETA: 42s - loss: 0.2392 - categorical_accuracy: 0.9266
37888/60000 [=================>............] - ETA: 42s - loss: 0.2391 - categorical_accuracy: 0.9267
37920/60000 [=================>............] - ETA: 42s - loss: 0.2390 - categorical_accuracy: 0.9267
37952/60000 [=================>............] - ETA: 41s - loss: 0.2388 - categorical_accuracy: 0.9267
37984/60000 [=================>............] - ETA: 41s - loss: 0.2387 - categorical_accuracy: 0.9268
38016/60000 [==================>...........] - ETA: 41s - loss: 0.2385 - categorical_accuracy: 0.9268
38048/60000 [==================>...........] - ETA: 41s - loss: 0.2383 - categorical_accuracy: 0.9269
38080/60000 [==================>...........] - ETA: 41s - loss: 0.2381 - categorical_accuracy: 0.9269
38112/60000 [==================>...........] - ETA: 41s - loss: 0.2380 - categorical_accuracy: 0.9270
38144/60000 [==================>...........] - ETA: 41s - loss: 0.2378 - categorical_accuracy: 0.9270
38176/60000 [==================>...........] - ETA: 41s - loss: 0.2377 - categorical_accuracy: 0.9271
38208/60000 [==================>...........] - ETA: 41s - loss: 0.2376 - categorical_accuracy: 0.9271
38240/60000 [==================>...........] - ETA: 41s - loss: 0.2375 - categorical_accuracy: 0.9271
38272/60000 [==================>...........] - ETA: 41s - loss: 0.2374 - categorical_accuracy: 0.9271
38304/60000 [==================>...........] - ETA: 41s - loss: 0.2373 - categorical_accuracy: 0.9271
38336/60000 [==================>...........] - ETA: 41s - loss: 0.2371 - categorical_accuracy: 0.9271
38368/60000 [==================>...........] - ETA: 41s - loss: 0.2369 - categorical_accuracy: 0.9272
38400/60000 [==================>...........] - ETA: 41s - loss: 0.2371 - categorical_accuracy: 0.9272
38432/60000 [==================>...........] - ETA: 41s - loss: 0.2370 - categorical_accuracy: 0.9272
38464/60000 [==================>...........] - ETA: 40s - loss: 0.2368 - categorical_accuracy: 0.9273
38496/60000 [==================>...........] - ETA: 40s - loss: 0.2367 - categorical_accuracy: 0.9273
38528/60000 [==================>...........] - ETA: 40s - loss: 0.2366 - categorical_accuracy: 0.9274
38560/60000 [==================>...........] - ETA: 40s - loss: 0.2365 - categorical_accuracy: 0.9274
38592/60000 [==================>...........] - ETA: 40s - loss: 0.2364 - categorical_accuracy: 0.9274
38624/60000 [==================>...........] - ETA: 40s - loss: 0.2362 - categorical_accuracy: 0.9275
38656/60000 [==================>...........] - ETA: 40s - loss: 0.2360 - categorical_accuracy: 0.9275
38688/60000 [==================>...........] - ETA: 40s - loss: 0.2359 - categorical_accuracy: 0.9276
38720/60000 [==================>...........] - ETA: 40s - loss: 0.2359 - categorical_accuracy: 0.9276
38752/60000 [==================>...........] - ETA: 40s - loss: 0.2358 - categorical_accuracy: 0.9276
38784/60000 [==================>...........] - ETA: 40s - loss: 0.2356 - categorical_accuracy: 0.9277
38816/60000 [==================>...........] - ETA: 40s - loss: 0.2356 - categorical_accuracy: 0.9277
38848/60000 [==================>...........] - ETA: 40s - loss: 0.2356 - categorical_accuracy: 0.9277
38880/60000 [==================>...........] - ETA: 40s - loss: 0.2354 - categorical_accuracy: 0.9277
38912/60000 [==================>...........] - ETA: 40s - loss: 0.2352 - categorical_accuracy: 0.9278
38944/60000 [==================>...........] - ETA: 40s - loss: 0.2353 - categorical_accuracy: 0.9278
38976/60000 [==================>...........] - ETA: 40s - loss: 0.2351 - categorical_accuracy: 0.9278
39008/60000 [==================>...........] - ETA: 39s - loss: 0.2350 - categorical_accuracy: 0.9278
39040/60000 [==================>...........] - ETA: 39s - loss: 0.2349 - categorical_accuracy: 0.9279
39072/60000 [==================>...........] - ETA: 39s - loss: 0.2348 - categorical_accuracy: 0.9279
39104/60000 [==================>...........] - ETA: 39s - loss: 0.2346 - categorical_accuracy: 0.9280
39136/60000 [==================>...........] - ETA: 39s - loss: 0.2345 - categorical_accuracy: 0.9280
39168/60000 [==================>...........] - ETA: 39s - loss: 0.2343 - categorical_accuracy: 0.9281
39200/60000 [==================>...........] - ETA: 39s - loss: 0.2341 - categorical_accuracy: 0.9281
39232/60000 [==================>...........] - ETA: 39s - loss: 0.2340 - categorical_accuracy: 0.9282
39264/60000 [==================>...........] - ETA: 39s - loss: 0.2339 - categorical_accuracy: 0.9282
39296/60000 [==================>...........] - ETA: 39s - loss: 0.2338 - categorical_accuracy: 0.9283
39328/60000 [==================>...........] - ETA: 39s - loss: 0.2336 - categorical_accuracy: 0.9283
39360/60000 [==================>...........] - ETA: 39s - loss: 0.2337 - categorical_accuracy: 0.9282
39392/60000 [==================>...........] - ETA: 39s - loss: 0.2335 - categorical_accuracy: 0.9283
39424/60000 [==================>...........] - ETA: 39s - loss: 0.2334 - categorical_accuracy: 0.9283
39456/60000 [==================>...........] - ETA: 39s - loss: 0.2334 - categorical_accuracy: 0.9283
39488/60000 [==================>...........] - ETA: 39s - loss: 0.2333 - categorical_accuracy: 0.9283
39520/60000 [==================>...........] - ETA: 38s - loss: 0.2332 - categorical_accuracy: 0.9283
39552/60000 [==================>...........] - ETA: 38s - loss: 0.2331 - categorical_accuracy: 0.9283
39584/60000 [==================>...........] - ETA: 38s - loss: 0.2332 - categorical_accuracy: 0.9284
39616/60000 [==================>...........] - ETA: 38s - loss: 0.2331 - categorical_accuracy: 0.9284
39648/60000 [==================>...........] - ETA: 38s - loss: 0.2330 - categorical_accuracy: 0.9285
39680/60000 [==================>...........] - ETA: 38s - loss: 0.2328 - categorical_accuracy: 0.9285
39712/60000 [==================>...........] - ETA: 38s - loss: 0.2326 - categorical_accuracy: 0.9286
39744/60000 [==================>...........] - ETA: 38s - loss: 0.2325 - categorical_accuracy: 0.9286
39776/60000 [==================>...........] - ETA: 38s - loss: 0.2324 - categorical_accuracy: 0.9287
39808/60000 [==================>...........] - ETA: 38s - loss: 0.2323 - categorical_accuracy: 0.9287
39840/60000 [==================>...........] - ETA: 38s - loss: 0.2322 - categorical_accuracy: 0.9287
39872/60000 [==================>...........] - ETA: 38s - loss: 0.2321 - categorical_accuracy: 0.9287
39904/60000 [==================>...........] - ETA: 38s - loss: 0.2320 - categorical_accuracy: 0.9288
39936/60000 [==================>...........] - ETA: 38s - loss: 0.2319 - categorical_accuracy: 0.9288
39968/60000 [==================>...........] - ETA: 38s - loss: 0.2317 - categorical_accuracy: 0.9288
40000/60000 [===================>..........] - ETA: 38s - loss: 0.2316 - categorical_accuracy: 0.9288
40032/60000 [===================>..........] - ETA: 37s - loss: 0.2315 - categorical_accuracy: 0.9289
40064/60000 [===================>..........] - ETA: 37s - loss: 0.2313 - categorical_accuracy: 0.9289
40096/60000 [===================>..........] - ETA: 37s - loss: 0.2312 - categorical_accuracy: 0.9290
40128/60000 [===================>..........] - ETA: 37s - loss: 0.2312 - categorical_accuracy: 0.9290
40160/60000 [===================>..........] - ETA: 37s - loss: 0.2312 - categorical_accuracy: 0.9290
40192/60000 [===================>..........] - ETA: 37s - loss: 0.2310 - categorical_accuracy: 0.9290
40224/60000 [===================>..........] - ETA: 37s - loss: 0.2309 - categorical_accuracy: 0.9291
40256/60000 [===================>..........] - ETA: 37s - loss: 0.2308 - categorical_accuracy: 0.9291
40288/60000 [===================>..........] - ETA: 37s - loss: 0.2307 - categorical_accuracy: 0.9291
40320/60000 [===================>..........] - ETA: 37s - loss: 0.2306 - categorical_accuracy: 0.9292
40352/60000 [===================>..........] - ETA: 37s - loss: 0.2304 - categorical_accuracy: 0.9292
40384/60000 [===================>..........] - ETA: 37s - loss: 0.2303 - categorical_accuracy: 0.9293
40416/60000 [===================>..........] - ETA: 37s - loss: 0.2301 - categorical_accuracy: 0.9293
40448/60000 [===================>..........] - ETA: 37s - loss: 0.2301 - categorical_accuracy: 0.9293
40480/60000 [===================>..........] - ETA: 37s - loss: 0.2301 - categorical_accuracy: 0.9293
40512/60000 [===================>..........] - ETA: 37s - loss: 0.2300 - categorical_accuracy: 0.9294
40544/60000 [===================>..........] - ETA: 37s - loss: 0.2298 - categorical_accuracy: 0.9294
40576/60000 [===================>..........] - ETA: 36s - loss: 0.2298 - categorical_accuracy: 0.9294
40608/60000 [===================>..........] - ETA: 36s - loss: 0.2296 - categorical_accuracy: 0.9295
40640/60000 [===================>..........] - ETA: 36s - loss: 0.2296 - categorical_accuracy: 0.9295
40672/60000 [===================>..........] - ETA: 36s - loss: 0.2294 - categorical_accuracy: 0.9296
40704/60000 [===================>..........] - ETA: 36s - loss: 0.2292 - categorical_accuracy: 0.9296
40736/60000 [===================>..........] - ETA: 36s - loss: 0.2294 - categorical_accuracy: 0.9296
40768/60000 [===================>..........] - ETA: 36s - loss: 0.2292 - categorical_accuracy: 0.9296
40800/60000 [===================>..........] - ETA: 36s - loss: 0.2291 - categorical_accuracy: 0.9297
40832/60000 [===================>..........] - ETA: 36s - loss: 0.2290 - categorical_accuracy: 0.9296
40864/60000 [===================>..........] - ETA: 36s - loss: 0.2289 - categorical_accuracy: 0.9297
40896/60000 [===================>..........] - ETA: 36s - loss: 0.2288 - categorical_accuracy: 0.9297
40928/60000 [===================>..........] - ETA: 36s - loss: 0.2287 - categorical_accuracy: 0.9297
40960/60000 [===================>..........] - ETA: 36s - loss: 0.2285 - categorical_accuracy: 0.9298
40992/60000 [===================>..........] - ETA: 36s - loss: 0.2284 - categorical_accuracy: 0.9298
41024/60000 [===================>..........] - ETA: 36s - loss: 0.2284 - categorical_accuracy: 0.9298
41056/60000 [===================>..........] - ETA: 36s - loss: 0.2283 - categorical_accuracy: 0.9299
41088/60000 [===================>..........] - ETA: 35s - loss: 0.2282 - categorical_accuracy: 0.9299
41120/60000 [===================>..........] - ETA: 35s - loss: 0.2281 - categorical_accuracy: 0.9299
41152/60000 [===================>..........] - ETA: 35s - loss: 0.2280 - categorical_accuracy: 0.9300
41184/60000 [===================>..........] - ETA: 35s - loss: 0.2279 - categorical_accuracy: 0.9300
41216/60000 [===================>..........] - ETA: 35s - loss: 0.2278 - categorical_accuracy: 0.9300
41248/60000 [===================>..........] - ETA: 35s - loss: 0.2277 - categorical_accuracy: 0.9300
41280/60000 [===================>..........] - ETA: 35s - loss: 0.2277 - categorical_accuracy: 0.9300
41312/60000 [===================>..........] - ETA: 35s - loss: 0.2277 - categorical_accuracy: 0.9300
41344/60000 [===================>..........] - ETA: 35s - loss: 0.2277 - categorical_accuracy: 0.9300
41376/60000 [===================>..........] - ETA: 35s - loss: 0.2276 - categorical_accuracy: 0.9300
41408/60000 [===================>..........] - ETA: 35s - loss: 0.2274 - categorical_accuracy: 0.9301
41440/60000 [===================>..........] - ETA: 35s - loss: 0.2273 - categorical_accuracy: 0.9301
41472/60000 [===================>..........] - ETA: 35s - loss: 0.2272 - categorical_accuracy: 0.9301
41504/60000 [===================>..........] - ETA: 35s - loss: 0.2271 - categorical_accuracy: 0.9302
41536/60000 [===================>..........] - ETA: 35s - loss: 0.2270 - categorical_accuracy: 0.9302
41568/60000 [===================>..........] - ETA: 35s - loss: 0.2270 - categorical_accuracy: 0.9302
41600/60000 [===================>..........] - ETA: 34s - loss: 0.2269 - categorical_accuracy: 0.9302
41632/60000 [===================>..........] - ETA: 34s - loss: 0.2267 - categorical_accuracy: 0.9302
41664/60000 [===================>..........] - ETA: 34s - loss: 0.2267 - categorical_accuracy: 0.9302
41696/60000 [===================>..........] - ETA: 34s - loss: 0.2265 - categorical_accuracy: 0.9303
41728/60000 [===================>..........] - ETA: 34s - loss: 0.2264 - categorical_accuracy: 0.9303
41760/60000 [===================>..........] - ETA: 34s - loss: 0.2263 - categorical_accuracy: 0.9304
41792/60000 [===================>..........] - ETA: 34s - loss: 0.2261 - categorical_accuracy: 0.9304
41824/60000 [===================>..........] - ETA: 34s - loss: 0.2261 - categorical_accuracy: 0.9304
41856/60000 [===================>..........] - ETA: 34s - loss: 0.2259 - categorical_accuracy: 0.9305
41888/60000 [===================>..........] - ETA: 34s - loss: 0.2259 - categorical_accuracy: 0.9305
41920/60000 [===================>..........] - ETA: 34s - loss: 0.2259 - categorical_accuracy: 0.9305
41952/60000 [===================>..........] - ETA: 34s - loss: 0.2258 - categorical_accuracy: 0.9306
41984/60000 [===================>..........] - ETA: 34s - loss: 0.2257 - categorical_accuracy: 0.9306
42016/60000 [====================>.........] - ETA: 34s - loss: 0.2257 - categorical_accuracy: 0.9306
42048/60000 [====================>.........] - ETA: 34s - loss: 0.2257 - categorical_accuracy: 0.9306
42080/60000 [====================>.........] - ETA: 34s - loss: 0.2256 - categorical_accuracy: 0.9306
42112/60000 [====================>.........] - ETA: 34s - loss: 0.2256 - categorical_accuracy: 0.9307
42144/60000 [====================>.........] - ETA: 33s - loss: 0.2254 - categorical_accuracy: 0.9307
42176/60000 [====================>.........] - ETA: 33s - loss: 0.2253 - categorical_accuracy: 0.9307
42208/60000 [====================>.........] - ETA: 33s - loss: 0.2252 - categorical_accuracy: 0.9308
42240/60000 [====================>.........] - ETA: 33s - loss: 0.2251 - categorical_accuracy: 0.9308
42272/60000 [====================>.........] - ETA: 33s - loss: 0.2250 - categorical_accuracy: 0.9308
42304/60000 [====================>.........] - ETA: 33s - loss: 0.2249 - categorical_accuracy: 0.9309
42336/60000 [====================>.........] - ETA: 33s - loss: 0.2247 - categorical_accuracy: 0.9309
42368/60000 [====================>.........] - ETA: 33s - loss: 0.2246 - categorical_accuracy: 0.9310
42400/60000 [====================>.........] - ETA: 33s - loss: 0.2244 - categorical_accuracy: 0.9310
42432/60000 [====================>.........] - ETA: 33s - loss: 0.2244 - categorical_accuracy: 0.9310
42464/60000 [====================>.........] - ETA: 33s - loss: 0.2243 - categorical_accuracy: 0.9310
42496/60000 [====================>.........] - ETA: 33s - loss: 0.2242 - categorical_accuracy: 0.9311
42528/60000 [====================>.........] - ETA: 33s - loss: 0.2241 - categorical_accuracy: 0.9311
42560/60000 [====================>.........] - ETA: 33s - loss: 0.2241 - categorical_accuracy: 0.9311
42592/60000 [====================>.........] - ETA: 33s - loss: 0.2240 - categorical_accuracy: 0.9312
42624/60000 [====================>.........] - ETA: 33s - loss: 0.2240 - categorical_accuracy: 0.9311
42656/60000 [====================>.........] - ETA: 32s - loss: 0.2238 - categorical_accuracy: 0.9312
42688/60000 [====================>.........] - ETA: 32s - loss: 0.2237 - categorical_accuracy: 0.9312
42720/60000 [====================>.........] - ETA: 32s - loss: 0.2237 - categorical_accuracy: 0.9313
42752/60000 [====================>.........] - ETA: 32s - loss: 0.2235 - categorical_accuracy: 0.9313
42784/60000 [====================>.........] - ETA: 32s - loss: 0.2234 - categorical_accuracy: 0.9314
42816/60000 [====================>.........] - ETA: 32s - loss: 0.2232 - categorical_accuracy: 0.9314
42848/60000 [====================>.........] - ETA: 32s - loss: 0.2232 - categorical_accuracy: 0.9314
42880/60000 [====================>.........] - ETA: 32s - loss: 0.2231 - categorical_accuracy: 0.9315
42912/60000 [====================>.........] - ETA: 32s - loss: 0.2229 - categorical_accuracy: 0.9315
42944/60000 [====================>.........] - ETA: 32s - loss: 0.2228 - categorical_accuracy: 0.9316
42976/60000 [====================>.........] - ETA: 32s - loss: 0.2226 - categorical_accuracy: 0.9316
43008/60000 [====================>.........] - ETA: 32s - loss: 0.2225 - categorical_accuracy: 0.9317
43040/60000 [====================>.........] - ETA: 32s - loss: 0.2225 - categorical_accuracy: 0.9317
43072/60000 [====================>.........] - ETA: 32s - loss: 0.2223 - categorical_accuracy: 0.9317
43104/60000 [====================>.........] - ETA: 32s - loss: 0.2223 - categorical_accuracy: 0.9317
43136/60000 [====================>.........] - ETA: 32s - loss: 0.2221 - categorical_accuracy: 0.9318
43168/60000 [====================>.........] - ETA: 32s - loss: 0.2221 - categorical_accuracy: 0.9318
43200/60000 [====================>.........] - ETA: 31s - loss: 0.2220 - categorical_accuracy: 0.9318
43232/60000 [====================>.........] - ETA: 31s - loss: 0.2218 - categorical_accuracy: 0.9319
43264/60000 [====================>.........] - ETA: 31s - loss: 0.2217 - categorical_accuracy: 0.9319
43296/60000 [====================>.........] - ETA: 31s - loss: 0.2217 - categorical_accuracy: 0.9319
43328/60000 [====================>.........] - ETA: 31s - loss: 0.2215 - categorical_accuracy: 0.9320
43360/60000 [====================>.........] - ETA: 31s - loss: 0.2218 - categorical_accuracy: 0.9320
43392/60000 [====================>.........] - ETA: 31s - loss: 0.2216 - categorical_accuracy: 0.9320
43424/60000 [====================>.........] - ETA: 31s - loss: 0.2215 - categorical_accuracy: 0.9320
43456/60000 [====================>.........] - ETA: 31s - loss: 0.2214 - categorical_accuracy: 0.9321
43488/60000 [====================>.........] - ETA: 31s - loss: 0.2213 - categorical_accuracy: 0.9321
43520/60000 [====================>.........] - ETA: 31s - loss: 0.2211 - categorical_accuracy: 0.9322
43552/60000 [====================>.........] - ETA: 31s - loss: 0.2211 - categorical_accuracy: 0.9322
43584/60000 [====================>.........] - ETA: 31s - loss: 0.2211 - categorical_accuracy: 0.9322
43616/60000 [====================>.........] - ETA: 31s - loss: 0.2209 - categorical_accuracy: 0.9322
43648/60000 [====================>.........] - ETA: 31s - loss: 0.2209 - categorical_accuracy: 0.9322
43680/60000 [====================>.........] - ETA: 31s - loss: 0.2208 - categorical_accuracy: 0.9323
43712/60000 [====================>.........] - ETA: 30s - loss: 0.2206 - categorical_accuracy: 0.9323
43744/60000 [====================>.........] - ETA: 30s - loss: 0.2206 - categorical_accuracy: 0.9323
43776/60000 [====================>.........] - ETA: 30s - loss: 0.2207 - categorical_accuracy: 0.9323
43808/60000 [====================>.........] - ETA: 30s - loss: 0.2206 - categorical_accuracy: 0.9323
43840/60000 [====================>.........] - ETA: 30s - loss: 0.2205 - categorical_accuracy: 0.9323
43872/60000 [====================>.........] - ETA: 30s - loss: 0.2203 - categorical_accuracy: 0.9324
43904/60000 [====================>.........] - ETA: 30s - loss: 0.2203 - categorical_accuracy: 0.9324
43936/60000 [====================>.........] - ETA: 30s - loss: 0.2202 - categorical_accuracy: 0.9324
43968/60000 [====================>.........] - ETA: 30s - loss: 0.2201 - categorical_accuracy: 0.9324
44000/60000 [=====================>........] - ETA: 30s - loss: 0.2199 - categorical_accuracy: 0.9325
44032/60000 [=====================>........] - ETA: 30s - loss: 0.2198 - categorical_accuracy: 0.9325
44064/60000 [=====================>........] - ETA: 30s - loss: 0.2196 - categorical_accuracy: 0.9326
44096/60000 [=====================>........] - ETA: 30s - loss: 0.2196 - categorical_accuracy: 0.9326
44128/60000 [=====================>........] - ETA: 30s - loss: 0.2195 - categorical_accuracy: 0.9326
44160/60000 [=====================>........] - ETA: 30s - loss: 0.2194 - categorical_accuracy: 0.9326
44192/60000 [=====================>........] - ETA: 30s - loss: 0.2194 - categorical_accuracy: 0.9326
44224/60000 [=====================>........] - ETA: 29s - loss: 0.2195 - categorical_accuracy: 0.9326
44256/60000 [=====================>........] - ETA: 29s - loss: 0.2193 - categorical_accuracy: 0.9327
44288/60000 [=====================>........] - ETA: 29s - loss: 0.2194 - categorical_accuracy: 0.9327
44320/60000 [=====================>........] - ETA: 29s - loss: 0.2193 - categorical_accuracy: 0.9327
44352/60000 [=====================>........] - ETA: 29s - loss: 0.2192 - categorical_accuracy: 0.9328
44384/60000 [=====================>........] - ETA: 29s - loss: 0.2191 - categorical_accuracy: 0.9328
44416/60000 [=====================>........] - ETA: 29s - loss: 0.2192 - categorical_accuracy: 0.9328
44448/60000 [=====================>........] - ETA: 29s - loss: 0.2193 - categorical_accuracy: 0.9328
44480/60000 [=====================>........] - ETA: 29s - loss: 0.2192 - categorical_accuracy: 0.9328
44512/60000 [=====================>........] - ETA: 29s - loss: 0.2191 - categorical_accuracy: 0.9328
44544/60000 [=====================>........] - ETA: 29s - loss: 0.2190 - categorical_accuracy: 0.9329
44576/60000 [=====================>........] - ETA: 29s - loss: 0.2188 - categorical_accuracy: 0.9329
44608/60000 [=====================>........] - ETA: 29s - loss: 0.2188 - categorical_accuracy: 0.9329
44640/60000 [=====================>........] - ETA: 29s - loss: 0.2188 - categorical_accuracy: 0.9329
44672/60000 [=====================>........] - ETA: 29s - loss: 0.2187 - categorical_accuracy: 0.9330
44704/60000 [=====================>........] - ETA: 29s - loss: 0.2186 - categorical_accuracy: 0.9330
44736/60000 [=====================>........] - ETA: 29s - loss: 0.2188 - categorical_accuracy: 0.9330
44768/60000 [=====================>........] - ETA: 28s - loss: 0.2187 - categorical_accuracy: 0.9330
44800/60000 [=====================>........] - ETA: 28s - loss: 0.2187 - categorical_accuracy: 0.9330
44832/60000 [=====================>........] - ETA: 28s - loss: 0.2186 - categorical_accuracy: 0.9331
44864/60000 [=====================>........] - ETA: 28s - loss: 0.2185 - categorical_accuracy: 0.9331
44896/60000 [=====================>........] - ETA: 28s - loss: 0.2184 - categorical_accuracy: 0.9331
44928/60000 [=====================>........] - ETA: 28s - loss: 0.2184 - categorical_accuracy: 0.9331
44960/60000 [=====================>........] - ETA: 28s - loss: 0.2183 - categorical_accuracy: 0.9332
44992/60000 [=====================>........] - ETA: 28s - loss: 0.2181 - categorical_accuracy: 0.9332
45024/60000 [=====================>........] - ETA: 28s - loss: 0.2181 - categorical_accuracy: 0.9332
45056/60000 [=====================>........] - ETA: 28s - loss: 0.2180 - categorical_accuracy: 0.9332
45088/60000 [=====================>........] - ETA: 28s - loss: 0.2181 - categorical_accuracy: 0.9332
45120/60000 [=====================>........] - ETA: 28s - loss: 0.2180 - categorical_accuracy: 0.9333
45152/60000 [=====================>........] - ETA: 28s - loss: 0.2179 - categorical_accuracy: 0.9333
45184/60000 [=====================>........] - ETA: 28s - loss: 0.2177 - categorical_accuracy: 0.9333
45216/60000 [=====================>........] - ETA: 28s - loss: 0.2176 - categorical_accuracy: 0.9334
45248/60000 [=====================>........] - ETA: 28s - loss: 0.2175 - categorical_accuracy: 0.9334
45280/60000 [=====================>........] - ETA: 27s - loss: 0.2174 - categorical_accuracy: 0.9335
45312/60000 [=====================>........] - ETA: 27s - loss: 0.2172 - categorical_accuracy: 0.9335
45344/60000 [=====================>........] - ETA: 27s - loss: 0.2172 - categorical_accuracy: 0.9336
45376/60000 [=====================>........] - ETA: 27s - loss: 0.2171 - categorical_accuracy: 0.9336
45408/60000 [=====================>........] - ETA: 27s - loss: 0.2170 - categorical_accuracy: 0.9336
45440/60000 [=====================>........] - ETA: 27s - loss: 0.2169 - categorical_accuracy: 0.9336
45472/60000 [=====================>........] - ETA: 27s - loss: 0.2168 - categorical_accuracy: 0.9337
45504/60000 [=====================>........] - ETA: 27s - loss: 0.2166 - categorical_accuracy: 0.9337
45536/60000 [=====================>........] - ETA: 27s - loss: 0.2165 - categorical_accuracy: 0.9337
45568/60000 [=====================>........] - ETA: 27s - loss: 0.2164 - categorical_accuracy: 0.9338
45600/60000 [=====================>........] - ETA: 27s - loss: 0.2164 - categorical_accuracy: 0.9338
45632/60000 [=====================>........] - ETA: 27s - loss: 0.2163 - categorical_accuracy: 0.9339
45664/60000 [=====================>........] - ETA: 27s - loss: 0.2162 - categorical_accuracy: 0.9339
45696/60000 [=====================>........] - ETA: 27s - loss: 0.2161 - categorical_accuracy: 0.9339
45728/60000 [=====================>........] - ETA: 27s - loss: 0.2164 - categorical_accuracy: 0.9339
45760/60000 [=====================>........] - ETA: 27s - loss: 0.2163 - categorical_accuracy: 0.9339
45792/60000 [=====================>........] - ETA: 27s - loss: 0.2162 - categorical_accuracy: 0.9340
45824/60000 [=====================>........] - ETA: 26s - loss: 0.2161 - categorical_accuracy: 0.9340
45856/60000 [=====================>........] - ETA: 26s - loss: 0.2160 - categorical_accuracy: 0.9340
45888/60000 [=====================>........] - ETA: 26s - loss: 0.2159 - categorical_accuracy: 0.9340
45920/60000 [=====================>........] - ETA: 26s - loss: 0.2158 - categorical_accuracy: 0.9341
45952/60000 [=====================>........] - ETA: 26s - loss: 0.2157 - categorical_accuracy: 0.9341
45984/60000 [=====================>........] - ETA: 26s - loss: 0.2156 - categorical_accuracy: 0.9342
46016/60000 [======================>.......] - ETA: 26s - loss: 0.2156 - categorical_accuracy: 0.9342
46048/60000 [======================>.......] - ETA: 26s - loss: 0.2155 - categorical_accuracy: 0.9342
46080/60000 [======================>.......] - ETA: 26s - loss: 0.2155 - categorical_accuracy: 0.9342
46112/60000 [======================>.......] - ETA: 26s - loss: 0.2153 - categorical_accuracy: 0.9342
46144/60000 [======================>.......] - ETA: 26s - loss: 0.2152 - categorical_accuracy: 0.9343
46176/60000 [======================>.......] - ETA: 26s - loss: 0.2151 - categorical_accuracy: 0.9343
46208/60000 [======================>.......] - ETA: 26s - loss: 0.2150 - categorical_accuracy: 0.9343
46240/60000 [======================>.......] - ETA: 26s - loss: 0.2149 - categorical_accuracy: 0.9344
46272/60000 [======================>.......] - ETA: 26s - loss: 0.2148 - categorical_accuracy: 0.9344
46304/60000 [======================>.......] - ETA: 26s - loss: 0.2147 - categorical_accuracy: 0.9344
46336/60000 [======================>.......] - ETA: 25s - loss: 0.2147 - categorical_accuracy: 0.9345
46368/60000 [======================>.......] - ETA: 25s - loss: 0.2146 - categorical_accuracy: 0.9345
46400/60000 [======================>.......] - ETA: 25s - loss: 0.2145 - categorical_accuracy: 0.9345
46432/60000 [======================>.......] - ETA: 25s - loss: 0.2143 - categorical_accuracy: 0.9345
46464/60000 [======================>.......] - ETA: 25s - loss: 0.2142 - categorical_accuracy: 0.9346
46496/60000 [======================>.......] - ETA: 25s - loss: 0.2141 - categorical_accuracy: 0.9346
46528/60000 [======================>.......] - ETA: 25s - loss: 0.2140 - categorical_accuracy: 0.9347
46560/60000 [======================>.......] - ETA: 25s - loss: 0.2139 - categorical_accuracy: 0.9347
46592/60000 [======================>.......] - ETA: 25s - loss: 0.2138 - categorical_accuracy: 0.9347
46624/60000 [======================>.......] - ETA: 25s - loss: 0.2137 - categorical_accuracy: 0.9348
46656/60000 [======================>.......] - ETA: 25s - loss: 0.2136 - categorical_accuracy: 0.9348
46688/60000 [======================>.......] - ETA: 25s - loss: 0.2134 - categorical_accuracy: 0.9348
46720/60000 [======================>.......] - ETA: 25s - loss: 0.2133 - categorical_accuracy: 0.9349
46752/60000 [======================>.......] - ETA: 25s - loss: 0.2133 - categorical_accuracy: 0.9349
46784/60000 [======================>.......] - ETA: 25s - loss: 0.2133 - categorical_accuracy: 0.9349
46816/60000 [======================>.......] - ETA: 25s - loss: 0.2132 - categorical_accuracy: 0.9349
46848/60000 [======================>.......] - ETA: 25s - loss: 0.2131 - categorical_accuracy: 0.9349
46880/60000 [======================>.......] - ETA: 24s - loss: 0.2131 - categorical_accuracy: 0.9350
46912/60000 [======================>.......] - ETA: 24s - loss: 0.2129 - categorical_accuracy: 0.9350
46944/60000 [======================>.......] - ETA: 24s - loss: 0.2128 - categorical_accuracy: 0.9351
46976/60000 [======================>.......] - ETA: 24s - loss: 0.2128 - categorical_accuracy: 0.9351
47008/60000 [======================>.......] - ETA: 24s - loss: 0.2127 - categorical_accuracy: 0.9351
47040/60000 [======================>.......] - ETA: 24s - loss: 0.2126 - categorical_accuracy: 0.9351
47072/60000 [======================>.......] - ETA: 24s - loss: 0.2127 - categorical_accuracy: 0.9351
47104/60000 [======================>.......] - ETA: 24s - loss: 0.2127 - categorical_accuracy: 0.9351
47136/60000 [======================>.......] - ETA: 24s - loss: 0.2125 - categorical_accuracy: 0.9351
47168/60000 [======================>.......] - ETA: 24s - loss: 0.2125 - categorical_accuracy: 0.9351
47200/60000 [======================>.......] - ETA: 24s - loss: 0.2124 - categorical_accuracy: 0.9352
47232/60000 [======================>.......] - ETA: 24s - loss: 0.2124 - categorical_accuracy: 0.9352
47264/60000 [======================>.......] - ETA: 24s - loss: 0.2123 - categorical_accuracy: 0.9352
47296/60000 [======================>.......] - ETA: 24s - loss: 0.2123 - categorical_accuracy: 0.9352
47328/60000 [======================>.......] - ETA: 24s - loss: 0.2125 - categorical_accuracy: 0.9352
47360/60000 [======================>.......] - ETA: 24s - loss: 0.2124 - categorical_accuracy: 0.9352
47392/60000 [======================>.......] - ETA: 23s - loss: 0.2124 - categorical_accuracy: 0.9352
47424/60000 [======================>.......] - ETA: 23s - loss: 0.2126 - categorical_accuracy: 0.9352
47456/60000 [======================>.......] - ETA: 23s - loss: 0.2126 - categorical_accuracy: 0.9352
47488/60000 [======================>.......] - ETA: 23s - loss: 0.2125 - categorical_accuracy: 0.9352
47520/60000 [======================>.......] - ETA: 23s - loss: 0.2123 - categorical_accuracy: 0.9353
47552/60000 [======================>.......] - ETA: 23s - loss: 0.2123 - categorical_accuracy: 0.9352
47584/60000 [======================>.......] - ETA: 23s - loss: 0.2123 - categorical_accuracy: 0.9353
47616/60000 [======================>.......] - ETA: 23s - loss: 0.2122 - categorical_accuracy: 0.9353
47648/60000 [======================>.......] - ETA: 23s - loss: 0.2121 - categorical_accuracy: 0.9353
47680/60000 [======================>.......] - ETA: 23s - loss: 0.2120 - categorical_accuracy: 0.9353
47712/60000 [======================>.......] - ETA: 23s - loss: 0.2119 - categorical_accuracy: 0.9353
47744/60000 [======================>.......] - ETA: 23s - loss: 0.2118 - categorical_accuracy: 0.9354
47776/60000 [======================>.......] - ETA: 23s - loss: 0.2118 - categorical_accuracy: 0.9354
47808/60000 [======================>.......] - ETA: 23s - loss: 0.2117 - categorical_accuracy: 0.9354
47840/60000 [======================>.......] - ETA: 23s - loss: 0.2116 - categorical_accuracy: 0.9355
47872/60000 [======================>.......] - ETA: 23s - loss: 0.2115 - categorical_accuracy: 0.9355
47904/60000 [======================>.......] - ETA: 22s - loss: 0.2115 - categorical_accuracy: 0.9355
47936/60000 [======================>.......] - ETA: 22s - loss: 0.2114 - categorical_accuracy: 0.9354
47968/60000 [======================>.......] - ETA: 22s - loss: 0.2114 - categorical_accuracy: 0.9354
48000/60000 [=======================>......] - ETA: 22s - loss: 0.2113 - categorical_accuracy: 0.9354
48032/60000 [=======================>......] - ETA: 22s - loss: 0.2112 - categorical_accuracy: 0.9355
48064/60000 [=======================>......] - ETA: 22s - loss: 0.2111 - categorical_accuracy: 0.9355
48096/60000 [=======================>......] - ETA: 22s - loss: 0.2109 - categorical_accuracy: 0.9355
48128/60000 [=======================>......] - ETA: 22s - loss: 0.2110 - categorical_accuracy: 0.9355
48160/60000 [=======================>......] - ETA: 22s - loss: 0.2109 - categorical_accuracy: 0.9355
48192/60000 [=======================>......] - ETA: 22s - loss: 0.2108 - categorical_accuracy: 0.9355
48224/60000 [=======================>......] - ETA: 22s - loss: 0.2108 - categorical_accuracy: 0.9356
48256/60000 [=======================>......] - ETA: 22s - loss: 0.2109 - categorical_accuracy: 0.9356
48288/60000 [=======================>......] - ETA: 22s - loss: 0.2108 - categorical_accuracy: 0.9356
48320/60000 [=======================>......] - ETA: 22s - loss: 0.2107 - categorical_accuracy: 0.9356
48352/60000 [=======================>......] - ETA: 22s - loss: 0.2105 - categorical_accuracy: 0.9356
48384/60000 [=======================>......] - ETA: 22s - loss: 0.2105 - categorical_accuracy: 0.9357
48416/60000 [=======================>......] - ETA: 22s - loss: 0.2104 - categorical_accuracy: 0.9357
48448/60000 [=======================>......] - ETA: 21s - loss: 0.2104 - categorical_accuracy: 0.9357
48480/60000 [=======================>......] - ETA: 21s - loss: 0.2103 - categorical_accuracy: 0.9357
48512/60000 [=======================>......] - ETA: 21s - loss: 0.2102 - categorical_accuracy: 0.9357
48544/60000 [=======================>......] - ETA: 21s - loss: 0.2102 - categorical_accuracy: 0.9358
48576/60000 [=======================>......] - ETA: 21s - loss: 0.2101 - categorical_accuracy: 0.9358
48608/60000 [=======================>......] - ETA: 21s - loss: 0.2100 - categorical_accuracy: 0.9359
48640/60000 [=======================>......] - ETA: 21s - loss: 0.2099 - categorical_accuracy: 0.9359
48672/60000 [=======================>......] - ETA: 21s - loss: 0.2098 - categorical_accuracy: 0.9359
48704/60000 [=======================>......] - ETA: 21s - loss: 0.2097 - categorical_accuracy: 0.9359
48736/60000 [=======================>......] - ETA: 21s - loss: 0.2097 - categorical_accuracy: 0.9359
48768/60000 [=======================>......] - ETA: 21s - loss: 0.2096 - categorical_accuracy: 0.9359
48800/60000 [=======================>......] - ETA: 21s - loss: 0.2095 - categorical_accuracy: 0.9359
48832/60000 [=======================>......] - ETA: 21s - loss: 0.2095 - categorical_accuracy: 0.9360
48864/60000 [=======================>......] - ETA: 21s - loss: 0.2094 - categorical_accuracy: 0.9360
48896/60000 [=======================>......] - ETA: 21s - loss: 0.2093 - categorical_accuracy: 0.9360
48928/60000 [=======================>......] - ETA: 21s - loss: 0.2092 - categorical_accuracy: 0.9361
48960/60000 [=======================>......] - ETA: 20s - loss: 0.2092 - categorical_accuracy: 0.9361
48992/60000 [=======================>......] - ETA: 20s - loss: 0.2092 - categorical_accuracy: 0.9361
49024/60000 [=======================>......] - ETA: 20s - loss: 0.2092 - categorical_accuracy: 0.9361
49056/60000 [=======================>......] - ETA: 20s - loss: 0.2090 - categorical_accuracy: 0.9361
49088/60000 [=======================>......] - ETA: 20s - loss: 0.2089 - categorical_accuracy: 0.9362
49120/60000 [=======================>......] - ETA: 20s - loss: 0.2088 - categorical_accuracy: 0.9362
49152/60000 [=======================>......] - ETA: 20s - loss: 0.2087 - categorical_accuracy: 0.9362
49184/60000 [=======================>......] - ETA: 20s - loss: 0.2086 - categorical_accuracy: 0.9362
49216/60000 [=======================>......] - ETA: 20s - loss: 0.2085 - categorical_accuracy: 0.9363
49248/60000 [=======================>......] - ETA: 20s - loss: 0.2084 - categorical_accuracy: 0.9363
49280/60000 [=======================>......] - ETA: 20s - loss: 0.2083 - categorical_accuracy: 0.9363
49312/60000 [=======================>......] - ETA: 20s - loss: 0.2081 - categorical_accuracy: 0.9364
49344/60000 [=======================>......] - ETA: 20s - loss: 0.2082 - categorical_accuracy: 0.9364
49376/60000 [=======================>......] - ETA: 20s - loss: 0.2081 - categorical_accuracy: 0.9364
49408/60000 [=======================>......] - ETA: 20s - loss: 0.2080 - categorical_accuracy: 0.9364
49440/60000 [=======================>......] - ETA: 20s - loss: 0.2080 - categorical_accuracy: 0.9364
49472/60000 [=======================>......] - ETA: 20s - loss: 0.2079 - categorical_accuracy: 0.9365
49504/60000 [=======================>......] - ETA: 19s - loss: 0.2079 - categorical_accuracy: 0.9364
49536/60000 [=======================>......] - ETA: 19s - loss: 0.2078 - categorical_accuracy: 0.9365
49568/60000 [=======================>......] - ETA: 19s - loss: 0.2078 - categorical_accuracy: 0.9365
49600/60000 [=======================>......] - ETA: 19s - loss: 0.2077 - categorical_accuracy: 0.9365
49632/60000 [=======================>......] - ETA: 19s - loss: 0.2076 - categorical_accuracy: 0.9365
49664/60000 [=======================>......] - ETA: 19s - loss: 0.2075 - categorical_accuracy: 0.9365
49696/60000 [=======================>......] - ETA: 19s - loss: 0.2075 - categorical_accuracy: 0.9366
49728/60000 [=======================>......] - ETA: 19s - loss: 0.2074 - categorical_accuracy: 0.9366
49760/60000 [=======================>......] - ETA: 19s - loss: 0.2074 - categorical_accuracy: 0.9366
49792/60000 [=======================>......] - ETA: 19s - loss: 0.2072 - categorical_accuracy: 0.9366
49824/60000 [=======================>......] - ETA: 19s - loss: 0.2071 - categorical_accuracy: 0.9366
49856/60000 [=======================>......] - ETA: 19s - loss: 0.2070 - categorical_accuracy: 0.9367
49888/60000 [=======================>......] - ETA: 19s - loss: 0.2070 - categorical_accuracy: 0.9367
49920/60000 [=======================>......] - ETA: 19s - loss: 0.2069 - categorical_accuracy: 0.9367
49952/60000 [=======================>......] - ETA: 19s - loss: 0.2068 - categorical_accuracy: 0.9367
49984/60000 [=======================>......] - ETA: 19s - loss: 0.2068 - categorical_accuracy: 0.9367
50016/60000 [========================>.....] - ETA: 18s - loss: 0.2068 - categorical_accuracy: 0.9367
50048/60000 [========================>.....] - ETA: 18s - loss: 0.2068 - categorical_accuracy: 0.9368
50080/60000 [========================>.....] - ETA: 18s - loss: 0.2067 - categorical_accuracy: 0.9368
50112/60000 [========================>.....] - ETA: 18s - loss: 0.2066 - categorical_accuracy: 0.9368
50144/60000 [========================>.....] - ETA: 18s - loss: 0.2066 - categorical_accuracy: 0.9368
50176/60000 [========================>.....] - ETA: 18s - loss: 0.2065 - categorical_accuracy: 0.9368
50208/60000 [========================>.....] - ETA: 18s - loss: 0.2064 - categorical_accuracy: 0.9369
50240/60000 [========================>.....] - ETA: 18s - loss: 0.2063 - categorical_accuracy: 0.9369
50272/60000 [========================>.....] - ETA: 18s - loss: 0.2063 - categorical_accuracy: 0.9369
50304/60000 [========================>.....] - ETA: 18s - loss: 0.2062 - categorical_accuracy: 0.9369
50336/60000 [========================>.....] - ETA: 18s - loss: 0.2062 - categorical_accuracy: 0.9369
50368/60000 [========================>.....] - ETA: 18s - loss: 0.2061 - categorical_accuracy: 0.9369
50400/60000 [========================>.....] - ETA: 18s - loss: 0.2061 - categorical_accuracy: 0.9369
50432/60000 [========================>.....] - ETA: 18s - loss: 0.2060 - categorical_accuracy: 0.9369
50464/60000 [========================>.....] - ETA: 18s - loss: 0.2060 - categorical_accuracy: 0.9369
50496/60000 [========================>.....] - ETA: 18s - loss: 0.2059 - categorical_accuracy: 0.9370
50528/60000 [========================>.....] - ETA: 18s - loss: 0.2057 - categorical_accuracy: 0.9370
50560/60000 [========================>.....] - ETA: 17s - loss: 0.2056 - categorical_accuracy: 0.9370
50592/60000 [========================>.....] - ETA: 17s - loss: 0.2056 - categorical_accuracy: 0.9370
50624/60000 [========================>.....] - ETA: 17s - loss: 0.2056 - categorical_accuracy: 0.9370
50656/60000 [========================>.....] - ETA: 17s - loss: 0.2055 - categorical_accuracy: 0.9371
50688/60000 [========================>.....] - ETA: 17s - loss: 0.2054 - categorical_accuracy: 0.9371
50720/60000 [========================>.....] - ETA: 17s - loss: 0.2053 - categorical_accuracy: 0.9371
50752/60000 [========================>.....] - ETA: 17s - loss: 0.2052 - categorical_accuracy: 0.9371
50784/60000 [========================>.....] - ETA: 17s - loss: 0.2051 - categorical_accuracy: 0.9372
50816/60000 [========================>.....] - ETA: 17s - loss: 0.2051 - categorical_accuracy: 0.9372
50848/60000 [========================>.....] - ETA: 17s - loss: 0.2050 - categorical_accuracy: 0.9372
50880/60000 [========================>.....] - ETA: 17s - loss: 0.2049 - categorical_accuracy: 0.9372
50912/60000 [========================>.....] - ETA: 17s - loss: 0.2049 - categorical_accuracy: 0.9372
50944/60000 [========================>.....] - ETA: 17s - loss: 0.2049 - categorical_accuracy: 0.9373
50976/60000 [========================>.....] - ETA: 17s - loss: 0.2048 - categorical_accuracy: 0.9373
51008/60000 [========================>.....] - ETA: 17s - loss: 0.2048 - categorical_accuracy: 0.9373
51040/60000 [========================>.....] - ETA: 17s - loss: 0.2047 - categorical_accuracy: 0.9373
51072/60000 [========================>.....] - ETA: 16s - loss: 0.2047 - categorical_accuracy: 0.9373
51104/60000 [========================>.....] - ETA: 16s - loss: 0.2046 - categorical_accuracy: 0.9374
51136/60000 [========================>.....] - ETA: 16s - loss: 0.2045 - categorical_accuracy: 0.9374
51168/60000 [========================>.....] - ETA: 16s - loss: 0.2044 - categorical_accuracy: 0.9374
51200/60000 [========================>.....] - ETA: 16s - loss: 0.2043 - categorical_accuracy: 0.9374
51232/60000 [========================>.....] - ETA: 16s - loss: 0.2042 - categorical_accuracy: 0.9375
51264/60000 [========================>.....] - ETA: 16s - loss: 0.2042 - categorical_accuracy: 0.9375
51296/60000 [========================>.....] - ETA: 16s - loss: 0.2041 - categorical_accuracy: 0.9375
51328/60000 [========================>.....] - ETA: 16s - loss: 0.2040 - categorical_accuracy: 0.9375
51360/60000 [========================>.....] - ETA: 16s - loss: 0.2039 - categorical_accuracy: 0.9376
51392/60000 [========================>.....] - ETA: 16s - loss: 0.2038 - categorical_accuracy: 0.9376
51424/60000 [========================>.....] - ETA: 16s - loss: 0.2037 - categorical_accuracy: 0.9376
51456/60000 [========================>.....] - ETA: 16s - loss: 0.2037 - categorical_accuracy: 0.9376
51488/60000 [========================>.....] - ETA: 16s - loss: 0.2036 - categorical_accuracy: 0.9376
51520/60000 [========================>.....] - ETA: 16s - loss: 0.2036 - categorical_accuracy: 0.9376
51552/60000 [========================>.....] - ETA: 16s - loss: 0.2036 - categorical_accuracy: 0.9376
51584/60000 [========================>.....] - ETA: 16s - loss: 0.2036 - categorical_accuracy: 0.9376
51616/60000 [========================>.....] - ETA: 15s - loss: 0.2035 - categorical_accuracy: 0.9377
51648/60000 [========================>.....] - ETA: 15s - loss: 0.2035 - categorical_accuracy: 0.9377
51680/60000 [========================>.....] - ETA: 15s - loss: 0.2034 - categorical_accuracy: 0.9377
51712/60000 [========================>.....] - ETA: 15s - loss: 0.2036 - categorical_accuracy: 0.9377
51744/60000 [========================>.....] - ETA: 15s - loss: 0.2035 - categorical_accuracy: 0.9377
51776/60000 [========================>.....] - ETA: 15s - loss: 0.2034 - categorical_accuracy: 0.9377
51808/60000 [========================>.....] - ETA: 15s - loss: 0.2033 - categorical_accuracy: 0.9378
51840/60000 [========================>.....] - ETA: 15s - loss: 0.2033 - categorical_accuracy: 0.9378
51872/60000 [========================>.....] - ETA: 15s - loss: 0.2033 - categorical_accuracy: 0.9378
51904/60000 [========================>.....] - ETA: 15s - loss: 0.2033 - categorical_accuracy: 0.9378
51936/60000 [========================>.....] - ETA: 15s - loss: 0.2032 - categorical_accuracy: 0.9378
51968/60000 [========================>.....] - ETA: 15s - loss: 0.2032 - categorical_accuracy: 0.9378
52000/60000 [=========================>....] - ETA: 15s - loss: 0.2031 - categorical_accuracy: 0.9378
52032/60000 [=========================>....] - ETA: 15s - loss: 0.2030 - categorical_accuracy: 0.9379
52064/60000 [=========================>....] - ETA: 15s - loss: 0.2029 - categorical_accuracy: 0.9379
52096/60000 [=========================>....] - ETA: 15s - loss: 0.2028 - categorical_accuracy: 0.9380
52128/60000 [=========================>....] - ETA: 14s - loss: 0.2026 - categorical_accuracy: 0.9380
52160/60000 [=========================>....] - ETA: 14s - loss: 0.2026 - categorical_accuracy: 0.9380
52192/60000 [=========================>....] - ETA: 14s - loss: 0.2025 - categorical_accuracy: 0.9381
52224/60000 [=========================>....] - ETA: 14s - loss: 0.2024 - categorical_accuracy: 0.9381
52256/60000 [=========================>....] - ETA: 14s - loss: 0.2023 - categorical_accuracy: 0.9381
52288/60000 [=========================>....] - ETA: 14s - loss: 0.2022 - categorical_accuracy: 0.9381
52320/60000 [=========================>....] - ETA: 14s - loss: 0.2022 - categorical_accuracy: 0.9381
52352/60000 [=========================>....] - ETA: 14s - loss: 0.2021 - categorical_accuracy: 0.9381
52384/60000 [=========================>....] - ETA: 14s - loss: 0.2020 - categorical_accuracy: 0.9382
52416/60000 [=========================>....] - ETA: 14s - loss: 0.2019 - categorical_accuracy: 0.9382
52448/60000 [=========================>....] - ETA: 14s - loss: 0.2018 - categorical_accuracy: 0.9382
52480/60000 [=========================>....] - ETA: 14s - loss: 0.2018 - categorical_accuracy: 0.9382
52512/60000 [=========================>....] - ETA: 14s - loss: 0.2017 - categorical_accuracy: 0.9383
52544/60000 [=========================>....] - ETA: 14s - loss: 0.2016 - categorical_accuracy: 0.9383
52576/60000 [=========================>....] - ETA: 14s - loss: 0.2015 - categorical_accuracy: 0.9383
52608/60000 [=========================>....] - ETA: 14s - loss: 0.2014 - categorical_accuracy: 0.9384
52640/60000 [=========================>....] - ETA: 13s - loss: 0.2013 - categorical_accuracy: 0.9384
52672/60000 [=========================>....] - ETA: 13s - loss: 0.2012 - categorical_accuracy: 0.9384
52704/60000 [=========================>....] - ETA: 13s - loss: 0.2011 - categorical_accuracy: 0.9385
52736/60000 [=========================>....] - ETA: 13s - loss: 0.2010 - categorical_accuracy: 0.9385
52768/60000 [=========================>....] - ETA: 13s - loss: 0.2009 - categorical_accuracy: 0.9385
52800/60000 [=========================>....] - ETA: 13s - loss: 0.2010 - categorical_accuracy: 0.9385
52832/60000 [=========================>....] - ETA: 13s - loss: 0.2008 - categorical_accuracy: 0.9386
52864/60000 [=========================>....] - ETA: 13s - loss: 0.2008 - categorical_accuracy: 0.9386
52896/60000 [=========================>....] - ETA: 13s - loss: 0.2008 - categorical_accuracy: 0.9386
52928/60000 [=========================>....] - ETA: 13s - loss: 0.2007 - categorical_accuracy: 0.9386
52960/60000 [=========================>....] - ETA: 13s - loss: 0.2006 - categorical_accuracy: 0.9387
52992/60000 [=========================>....] - ETA: 13s - loss: 0.2005 - categorical_accuracy: 0.9387
53024/60000 [=========================>....] - ETA: 13s - loss: 0.2007 - categorical_accuracy: 0.9387
53056/60000 [=========================>....] - ETA: 13s - loss: 0.2006 - categorical_accuracy: 0.9387
53088/60000 [=========================>....] - ETA: 13s - loss: 0.2005 - categorical_accuracy: 0.9387
53120/60000 [=========================>....] - ETA: 13s - loss: 0.2004 - categorical_accuracy: 0.9388
53152/60000 [=========================>....] - ETA: 13s - loss: 0.2004 - categorical_accuracy: 0.9388
53184/60000 [=========================>....] - ETA: 12s - loss: 0.2003 - categorical_accuracy: 0.9388
53216/60000 [=========================>....] - ETA: 12s - loss: 0.2002 - categorical_accuracy: 0.9388
53248/60000 [=========================>....] - ETA: 12s - loss: 0.2001 - categorical_accuracy: 0.9389
53280/60000 [=========================>....] - ETA: 12s - loss: 0.2000 - categorical_accuracy: 0.9389
53312/60000 [=========================>....] - ETA: 12s - loss: 0.2001 - categorical_accuracy: 0.9389
53344/60000 [=========================>....] - ETA: 12s - loss: 0.2001 - categorical_accuracy: 0.9389
53376/60000 [=========================>....] - ETA: 12s - loss: 0.2001 - categorical_accuracy: 0.9388
53408/60000 [=========================>....] - ETA: 12s - loss: 0.2002 - categorical_accuracy: 0.9388
53440/60000 [=========================>....] - ETA: 12s - loss: 0.2001 - categorical_accuracy: 0.9389
53472/60000 [=========================>....] - ETA: 12s - loss: 0.2001 - categorical_accuracy: 0.9389
53504/60000 [=========================>....] - ETA: 12s - loss: 0.2000 - categorical_accuracy: 0.9389
53536/60000 [=========================>....] - ETA: 12s - loss: 0.1999 - categorical_accuracy: 0.9389
53568/60000 [=========================>....] - ETA: 12s - loss: 0.1998 - categorical_accuracy: 0.9390
53600/60000 [=========================>....] - ETA: 12s - loss: 0.1997 - categorical_accuracy: 0.9390
53632/60000 [=========================>....] - ETA: 12s - loss: 0.1997 - categorical_accuracy: 0.9390
53664/60000 [=========================>....] - ETA: 12s - loss: 0.1996 - categorical_accuracy: 0.9390
53696/60000 [=========================>....] - ETA: 11s - loss: 0.1995 - categorical_accuracy: 0.9390
53728/60000 [=========================>....] - ETA: 11s - loss: 0.1994 - categorical_accuracy: 0.9391
53760/60000 [=========================>....] - ETA: 11s - loss: 0.1993 - categorical_accuracy: 0.9391
53792/60000 [=========================>....] - ETA: 11s - loss: 0.1993 - categorical_accuracy: 0.9391
53824/60000 [=========================>....] - ETA: 11s - loss: 0.1992 - categorical_accuracy: 0.9391
53856/60000 [=========================>....] - ETA: 11s - loss: 0.1991 - categorical_accuracy: 0.9392
53888/60000 [=========================>....] - ETA: 11s - loss: 0.1991 - categorical_accuracy: 0.9391
53920/60000 [=========================>....] - ETA: 11s - loss: 0.1990 - categorical_accuracy: 0.9392
53952/60000 [=========================>....] - ETA: 11s - loss: 0.1989 - categorical_accuracy: 0.9392
53984/60000 [=========================>....] - ETA: 11s - loss: 0.1988 - categorical_accuracy: 0.9392
54016/60000 [==========================>...] - ETA: 11s - loss: 0.1987 - categorical_accuracy: 0.9393
54048/60000 [==========================>...] - ETA: 11s - loss: 0.1986 - categorical_accuracy: 0.9393
54080/60000 [==========================>...] - ETA: 11s - loss: 0.1985 - categorical_accuracy: 0.9393
54112/60000 [==========================>...] - ETA: 11s - loss: 0.1985 - categorical_accuracy: 0.9393
54144/60000 [==========================>...] - ETA: 11s - loss: 0.1984 - categorical_accuracy: 0.9393
54176/60000 [==========================>...] - ETA: 11s - loss: 0.1984 - categorical_accuracy: 0.9394
54208/60000 [==========================>...] - ETA: 11s - loss: 0.1982 - categorical_accuracy: 0.9394
54240/60000 [==========================>...] - ETA: 10s - loss: 0.1981 - categorical_accuracy: 0.9394
54272/60000 [==========================>...] - ETA: 10s - loss: 0.1980 - categorical_accuracy: 0.9395
54304/60000 [==========================>...] - ETA: 10s - loss: 0.1979 - categorical_accuracy: 0.9395
54336/60000 [==========================>...] - ETA: 10s - loss: 0.1978 - categorical_accuracy: 0.9395
54368/60000 [==========================>...] - ETA: 10s - loss: 0.1978 - categorical_accuracy: 0.9395
54400/60000 [==========================>...] - ETA: 10s - loss: 0.1977 - categorical_accuracy: 0.9396
54432/60000 [==========================>...] - ETA: 10s - loss: 0.1977 - categorical_accuracy: 0.9396
54464/60000 [==========================>...] - ETA: 10s - loss: 0.1978 - categorical_accuracy: 0.9396
54496/60000 [==========================>...] - ETA: 10s - loss: 0.1977 - categorical_accuracy: 0.9396
54528/60000 [==========================>...] - ETA: 10s - loss: 0.1976 - categorical_accuracy: 0.9396
54560/60000 [==========================>...] - ETA: 10s - loss: 0.1976 - categorical_accuracy: 0.9396
54592/60000 [==========================>...] - ETA: 10s - loss: 0.1975 - categorical_accuracy: 0.9396
54624/60000 [==========================>...] - ETA: 10s - loss: 0.1974 - categorical_accuracy: 0.9396
54656/60000 [==========================>...] - ETA: 10s - loss: 0.1974 - categorical_accuracy: 0.9396
54688/60000 [==========================>...] - ETA: 10s - loss: 0.1973 - categorical_accuracy: 0.9397
54720/60000 [==========================>...] - ETA: 10s - loss: 0.1972 - categorical_accuracy: 0.9397
54752/60000 [==========================>...] - ETA: 9s - loss: 0.1971 - categorical_accuracy: 0.9397 
54784/60000 [==========================>...] - ETA: 9s - loss: 0.1970 - categorical_accuracy: 0.9397
54816/60000 [==========================>...] - ETA: 9s - loss: 0.1970 - categorical_accuracy: 0.9397
54848/60000 [==========================>...] - ETA: 9s - loss: 0.1969 - categorical_accuracy: 0.9397
54880/60000 [==========================>...] - ETA: 9s - loss: 0.1969 - categorical_accuracy: 0.9398
54912/60000 [==========================>...] - ETA: 9s - loss: 0.1968 - categorical_accuracy: 0.9398
54944/60000 [==========================>...] - ETA: 9s - loss: 0.1968 - categorical_accuracy: 0.9398
54976/60000 [==========================>...] - ETA: 9s - loss: 0.1967 - categorical_accuracy: 0.9398
55008/60000 [==========================>...] - ETA: 9s - loss: 0.1966 - categorical_accuracy: 0.9399
55040/60000 [==========================>...] - ETA: 9s - loss: 0.1965 - categorical_accuracy: 0.9399
55072/60000 [==========================>...] - ETA: 9s - loss: 0.1964 - categorical_accuracy: 0.9399
55104/60000 [==========================>...] - ETA: 9s - loss: 0.1964 - categorical_accuracy: 0.9399
55136/60000 [==========================>...] - ETA: 9s - loss: 0.1963 - categorical_accuracy: 0.9399
55168/60000 [==========================>...] - ETA: 9s - loss: 0.1963 - categorical_accuracy: 0.9399
55200/60000 [==========================>...] - ETA: 9s - loss: 0.1963 - categorical_accuracy: 0.9399
55232/60000 [==========================>...] - ETA: 9s - loss: 0.1962 - categorical_accuracy: 0.9399
55264/60000 [==========================>...] - ETA: 9s - loss: 0.1962 - categorical_accuracy: 0.9400
55296/60000 [==========================>...] - ETA: 8s - loss: 0.1961 - categorical_accuracy: 0.9400
55328/60000 [==========================>...] - ETA: 8s - loss: 0.1961 - categorical_accuracy: 0.9400
55360/60000 [==========================>...] - ETA: 8s - loss: 0.1960 - categorical_accuracy: 0.9400
55392/60000 [==========================>...] - ETA: 8s - loss: 0.1959 - categorical_accuracy: 0.9400
55424/60000 [==========================>...] - ETA: 8s - loss: 0.1958 - categorical_accuracy: 0.9401
55456/60000 [==========================>...] - ETA: 8s - loss: 0.1958 - categorical_accuracy: 0.9401
55488/60000 [==========================>...] - ETA: 8s - loss: 0.1957 - categorical_accuracy: 0.9401
55520/60000 [==========================>...] - ETA: 8s - loss: 0.1956 - categorical_accuracy: 0.9401
55552/60000 [==========================>...] - ETA: 8s - loss: 0.1956 - categorical_accuracy: 0.9401
55584/60000 [==========================>...] - ETA: 8s - loss: 0.1955 - categorical_accuracy: 0.9401
55616/60000 [==========================>...] - ETA: 8s - loss: 0.1954 - categorical_accuracy: 0.9401
55648/60000 [==========================>...] - ETA: 8s - loss: 0.1954 - categorical_accuracy: 0.9401
55680/60000 [==========================>...] - ETA: 8s - loss: 0.1953 - categorical_accuracy: 0.9402
55712/60000 [==========================>...] - ETA: 8s - loss: 0.1952 - categorical_accuracy: 0.9402
55744/60000 [==========================>...] - ETA: 8s - loss: 0.1951 - categorical_accuracy: 0.9402
55776/60000 [==========================>...] - ETA: 8s - loss: 0.1950 - categorical_accuracy: 0.9403
55808/60000 [==========================>...] - ETA: 7s - loss: 0.1949 - categorical_accuracy: 0.9403
55840/60000 [==========================>...] - ETA: 7s - loss: 0.1949 - categorical_accuracy: 0.9403
55872/60000 [==========================>...] - ETA: 7s - loss: 0.1949 - categorical_accuracy: 0.9403
55904/60000 [==========================>...] - ETA: 7s - loss: 0.1948 - categorical_accuracy: 0.9403
55936/60000 [==========================>...] - ETA: 7s - loss: 0.1947 - categorical_accuracy: 0.9404
55968/60000 [==========================>...] - ETA: 7s - loss: 0.1946 - categorical_accuracy: 0.9404
56000/60000 [===========================>..] - ETA: 7s - loss: 0.1946 - categorical_accuracy: 0.9404
56032/60000 [===========================>..] - ETA: 7s - loss: 0.1945 - categorical_accuracy: 0.9404
56064/60000 [===========================>..] - ETA: 7s - loss: 0.1944 - categorical_accuracy: 0.9405
56096/60000 [===========================>..] - ETA: 7s - loss: 0.1943 - categorical_accuracy: 0.9405
56128/60000 [===========================>..] - ETA: 7s - loss: 0.1943 - categorical_accuracy: 0.9405
56160/60000 [===========================>..] - ETA: 7s - loss: 0.1942 - categorical_accuracy: 0.9405
56192/60000 [===========================>..] - ETA: 7s - loss: 0.1941 - categorical_accuracy: 0.9405
56224/60000 [===========================>..] - ETA: 7s - loss: 0.1940 - categorical_accuracy: 0.9406
56256/60000 [===========================>..] - ETA: 7s - loss: 0.1941 - categorical_accuracy: 0.9406
56288/60000 [===========================>..] - ETA: 7s - loss: 0.1940 - categorical_accuracy: 0.9406
56320/60000 [===========================>..] - ETA: 6s - loss: 0.1939 - categorical_accuracy: 0.9406
56352/60000 [===========================>..] - ETA: 6s - loss: 0.1938 - categorical_accuracy: 0.9406
56384/60000 [===========================>..] - ETA: 6s - loss: 0.1937 - categorical_accuracy: 0.9407
56416/60000 [===========================>..] - ETA: 6s - loss: 0.1937 - categorical_accuracy: 0.9407
56448/60000 [===========================>..] - ETA: 6s - loss: 0.1937 - categorical_accuracy: 0.9407
56480/60000 [===========================>..] - ETA: 6s - loss: 0.1936 - categorical_accuracy: 0.9407
56512/60000 [===========================>..] - ETA: 6s - loss: 0.1935 - categorical_accuracy: 0.9408
56544/60000 [===========================>..] - ETA: 6s - loss: 0.1935 - categorical_accuracy: 0.9407
56576/60000 [===========================>..] - ETA: 6s - loss: 0.1934 - categorical_accuracy: 0.9408
56608/60000 [===========================>..] - ETA: 6s - loss: 0.1933 - categorical_accuracy: 0.9408
56640/60000 [===========================>..] - ETA: 6s - loss: 0.1933 - categorical_accuracy: 0.9408
56672/60000 [===========================>..] - ETA: 6s - loss: 0.1932 - categorical_accuracy: 0.9408
56704/60000 [===========================>..] - ETA: 6s - loss: 0.1932 - categorical_accuracy: 0.9409
56736/60000 [===========================>..] - ETA: 6s - loss: 0.1931 - categorical_accuracy: 0.9409
56768/60000 [===========================>..] - ETA: 6s - loss: 0.1930 - categorical_accuracy: 0.9409
56800/60000 [===========================>..] - ETA: 6s - loss: 0.1930 - categorical_accuracy: 0.9409
56832/60000 [===========================>..] - ETA: 6s - loss: 0.1929 - categorical_accuracy: 0.9409
56864/60000 [===========================>..] - ETA: 5s - loss: 0.1928 - categorical_accuracy: 0.9410
56896/60000 [===========================>..] - ETA: 5s - loss: 0.1928 - categorical_accuracy: 0.9410
56928/60000 [===========================>..] - ETA: 5s - loss: 0.1927 - categorical_accuracy: 0.9410
56960/60000 [===========================>..] - ETA: 5s - loss: 0.1926 - categorical_accuracy: 0.9410
56992/60000 [===========================>..] - ETA: 5s - loss: 0.1925 - categorical_accuracy: 0.9411
57024/60000 [===========================>..] - ETA: 5s - loss: 0.1925 - categorical_accuracy: 0.9411
57056/60000 [===========================>..] - ETA: 5s - loss: 0.1924 - categorical_accuracy: 0.9411
57088/60000 [===========================>..] - ETA: 5s - loss: 0.1924 - categorical_accuracy: 0.9411
57120/60000 [===========================>..] - ETA: 5s - loss: 0.1923 - categorical_accuracy: 0.9412
57152/60000 [===========================>..] - ETA: 5s - loss: 0.1923 - categorical_accuracy: 0.9412
57184/60000 [===========================>..] - ETA: 5s - loss: 0.1922 - categorical_accuracy: 0.9412
57216/60000 [===========================>..] - ETA: 5s - loss: 0.1922 - categorical_accuracy: 0.9412
57248/60000 [===========================>..] - ETA: 5s - loss: 0.1922 - categorical_accuracy: 0.9412
57280/60000 [===========================>..] - ETA: 5s - loss: 0.1921 - categorical_accuracy: 0.9413
57312/60000 [===========================>..] - ETA: 5s - loss: 0.1920 - categorical_accuracy: 0.9413
57344/60000 [===========================>..] - ETA: 5s - loss: 0.1919 - categorical_accuracy: 0.9413
57376/60000 [===========================>..] - ETA: 4s - loss: 0.1918 - categorical_accuracy: 0.9414
57408/60000 [===========================>..] - ETA: 4s - loss: 0.1918 - categorical_accuracy: 0.9414
57440/60000 [===========================>..] - ETA: 4s - loss: 0.1917 - categorical_accuracy: 0.9414
57472/60000 [===========================>..] - ETA: 4s - loss: 0.1916 - categorical_accuracy: 0.9414
57504/60000 [===========================>..] - ETA: 4s - loss: 0.1915 - categorical_accuracy: 0.9414
57536/60000 [===========================>..] - ETA: 4s - loss: 0.1914 - categorical_accuracy: 0.9415
57568/60000 [===========================>..] - ETA: 4s - loss: 0.1914 - categorical_accuracy: 0.9415
57600/60000 [===========================>..] - ETA: 4s - loss: 0.1913 - categorical_accuracy: 0.9415
57632/60000 [===========================>..] - ETA: 4s - loss: 0.1912 - categorical_accuracy: 0.9415
57664/60000 [===========================>..] - ETA: 4s - loss: 0.1911 - categorical_accuracy: 0.9416
57696/60000 [===========================>..] - ETA: 4s - loss: 0.1910 - categorical_accuracy: 0.9416
57728/60000 [===========================>..] - ETA: 4s - loss: 0.1910 - categorical_accuracy: 0.9416
57760/60000 [===========================>..] - ETA: 4s - loss: 0.1909 - categorical_accuracy: 0.9416
57792/60000 [===========================>..] - ETA: 4s - loss: 0.1909 - categorical_accuracy: 0.9416
57824/60000 [===========================>..] - ETA: 4s - loss: 0.1908 - categorical_accuracy: 0.9417
57856/60000 [===========================>..] - ETA: 4s - loss: 0.1907 - categorical_accuracy: 0.9417
57888/60000 [===========================>..] - ETA: 4s - loss: 0.1906 - categorical_accuracy: 0.9417
57920/60000 [===========================>..] - ETA: 3s - loss: 0.1906 - categorical_accuracy: 0.9417
57952/60000 [===========================>..] - ETA: 3s - loss: 0.1905 - categorical_accuracy: 0.9417
57984/60000 [===========================>..] - ETA: 3s - loss: 0.1904 - categorical_accuracy: 0.9418
58016/60000 [============================>.] - ETA: 3s - loss: 0.1903 - categorical_accuracy: 0.9418
58048/60000 [============================>.] - ETA: 3s - loss: 0.1902 - categorical_accuracy: 0.9418
58080/60000 [============================>.] - ETA: 3s - loss: 0.1902 - categorical_accuracy: 0.9418
58112/60000 [============================>.] - ETA: 3s - loss: 0.1902 - categorical_accuracy: 0.9419
58144/60000 [============================>.] - ETA: 3s - loss: 0.1901 - categorical_accuracy: 0.9419
58176/60000 [============================>.] - ETA: 3s - loss: 0.1900 - categorical_accuracy: 0.9419
58208/60000 [============================>.] - ETA: 3s - loss: 0.1900 - categorical_accuracy: 0.9419
58240/60000 [============================>.] - ETA: 3s - loss: 0.1899 - categorical_accuracy: 0.9420
58272/60000 [============================>.] - ETA: 3s - loss: 0.1899 - categorical_accuracy: 0.9420
58304/60000 [============================>.] - ETA: 3s - loss: 0.1898 - categorical_accuracy: 0.9420
58336/60000 [============================>.] - ETA: 3s - loss: 0.1898 - categorical_accuracy: 0.9420
58368/60000 [============================>.] - ETA: 3s - loss: 0.1898 - categorical_accuracy: 0.9420
58400/60000 [============================>.] - ETA: 3s - loss: 0.1898 - categorical_accuracy: 0.9420
58432/60000 [============================>.] - ETA: 2s - loss: 0.1897 - categorical_accuracy: 0.9420
58464/60000 [============================>.] - ETA: 2s - loss: 0.1896 - categorical_accuracy: 0.9420
58496/60000 [============================>.] - ETA: 2s - loss: 0.1895 - categorical_accuracy: 0.9421
58528/60000 [============================>.] - ETA: 2s - loss: 0.1895 - categorical_accuracy: 0.9421
58560/60000 [============================>.] - ETA: 2s - loss: 0.1895 - categorical_accuracy: 0.9421
58592/60000 [============================>.] - ETA: 2s - loss: 0.1894 - categorical_accuracy: 0.9421
58624/60000 [============================>.] - ETA: 2s - loss: 0.1894 - categorical_accuracy: 0.9422
58656/60000 [============================>.] - ETA: 2s - loss: 0.1894 - categorical_accuracy: 0.9422
58688/60000 [============================>.] - ETA: 2s - loss: 0.1893 - categorical_accuracy: 0.9422
58720/60000 [============================>.] - ETA: 2s - loss: 0.1892 - categorical_accuracy: 0.9422
58752/60000 [============================>.] - ETA: 2s - loss: 0.1891 - categorical_accuracy: 0.9422
58784/60000 [============================>.] - ETA: 2s - loss: 0.1891 - categorical_accuracy: 0.9422
58816/60000 [============================>.] - ETA: 2s - loss: 0.1890 - categorical_accuracy: 0.9422
58848/60000 [============================>.] - ETA: 2s - loss: 0.1889 - categorical_accuracy: 0.9423
58880/60000 [============================>.] - ETA: 2s - loss: 0.1889 - categorical_accuracy: 0.9423
58912/60000 [============================>.] - ETA: 2s - loss: 0.1888 - categorical_accuracy: 0.9423
58944/60000 [============================>.] - ETA: 2s - loss: 0.1888 - categorical_accuracy: 0.9423
58976/60000 [============================>.] - ETA: 1s - loss: 0.1888 - categorical_accuracy: 0.9423
59008/60000 [============================>.] - ETA: 1s - loss: 0.1887 - categorical_accuracy: 0.9423
59040/60000 [============================>.] - ETA: 1s - loss: 0.1886 - categorical_accuracy: 0.9423
59072/60000 [============================>.] - ETA: 1s - loss: 0.1885 - categorical_accuracy: 0.9424
59104/60000 [============================>.] - ETA: 1s - loss: 0.1885 - categorical_accuracy: 0.9424
59136/60000 [============================>.] - ETA: 1s - loss: 0.1885 - categorical_accuracy: 0.9424
59168/60000 [============================>.] - ETA: 1s - loss: 0.1884 - categorical_accuracy: 0.9424
59200/60000 [============================>.] - ETA: 1s - loss: 0.1883 - categorical_accuracy: 0.9424
59232/60000 [============================>.] - ETA: 1s - loss: 0.1883 - categorical_accuracy: 0.9424
59264/60000 [============================>.] - ETA: 1s - loss: 0.1882 - categorical_accuracy: 0.9424
59296/60000 [============================>.] - ETA: 1s - loss: 0.1882 - categorical_accuracy: 0.9424
59328/60000 [============================>.] - ETA: 1s - loss: 0.1882 - categorical_accuracy: 0.9424
59360/60000 [============================>.] - ETA: 1s - loss: 0.1881 - categorical_accuracy: 0.9424
59392/60000 [============================>.] - ETA: 1s - loss: 0.1881 - categorical_accuracy: 0.9424
59424/60000 [============================>.] - ETA: 1s - loss: 0.1881 - categorical_accuracy: 0.9424
59456/60000 [============================>.] - ETA: 1s - loss: 0.1880 - categorical_accuracy: 0.9424
59488/60000 [============================>.] - ETA: 0s - loss: 0.1879 - categorical_accuracy: 0.9425
59520/60000 [============================>.] - ETA: 0s - loss: 0.1879 - categorical_accuracy: 0.9425
59552/60000 [============================>.] - ETA: 0s - loss: 0.1879 - categorical_accuracy: 0.9425
59584/60000 [============================>.] - ETA: 0s - loss: 0.1878 - categorical_accuracy: 0.9425
59616/60000 [============================>.] - ETA: 0s - loss: 0.1877 - categorical_accuracy: 0.9425
59648/60000 [============================>.] - ETA: 0s - loss: 0.1876 - categorical_accuracy: 0.9426
59680/60000 [============================>.] - ETA: 0s - loss: 0.1877 - categorical_accuracy: 0.9426
59712/60000 [============================>.] - ETA: 0s - loss: 0.1876 - categorical_accuracy: 0.9426
59744/60000 [============================>.] - ETA: 0s - loss: 0.1876 - categorical_accuracy: 0.9426
59776/60000 [============================>.] - ETA: 0s - loss: 0.1875 - categorical_accuracy: 0.9426
59808/60000 [============================>.] - ETA: 0s - loss: 0.1874 - categorical_accuracy: 0.9426
59840/60000 [============================>.] - ETA: 0s - loss: 0.1874 - categorical_accuracy: 0.9426
59872/60000 [============================>.] - ETA: 0s - loss: 0.1873 - categorical_accuracy: 0.9427
59904/60000 [============================>.] - ETA: 0s - loss: 0.1873 - categorical_accuracy: 0.9427
59936/60000 [============================>.] - ETA: 0s - loss: 0.1872 - categorical_accuracy: 0.9427
59968/60000 [============================>.] - ETA: 0s - loss: 0.1871 - categorical_accuracy: 0.9428
60000/60000 [==============================] - 118s 2ms/step - loss: 0.1870 - categorical_accuracy: 0.9428 - val_loss: 0.0477 - val_categorical_accuracy: 0.9845

  ('#### Predict   ####################################################',) 

  ('#### Path params   ################################################',) 

  ('/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/', '/home/runner/work/mlmodels/mlmodels/keras_deepAR/') 

   32/10000 [..............................] - ETA: 18s
  160/10000 [..............................] - ETA: 6s 
  288/10000 [..............................] - ETA: 5s
  448/10000 [>.............................] - ETA: 4s
  608/10000 [>.............................] - ETA: 4s
  768/10000 [=>............................] - ETA: 4s
  928/10000 [=>............................] - ETA: 3s
 1088/10000 [==>...........................] - ETA: 3s
 1216/10000 [==>...........................] - ETA: 3s
 1376/10000 [===>..........................] - ETA: 3s
 1536/10000 [===>..........................] - ETA: 3s
 1696/10000 [====>.........................] - ETA: 3s
 1856/10000 [====>.........................] - ETA: 3s
 2016/10000 [=====>........................] - ETA: 3s
 2176/10000 [=====>........................] - ETA: 3s
 2336/10000 [======>.......................] - ETA: 3s
 2496/10000 [======>.......................] - ETA: 3s
 2656/10000 [======>.......................] - ETA: 2s
 2784/10000 [=======>......................] - ETA: 2s
 2912/10000 [=======>......................] - ETA: 2s
 3072/10000 [========>.....................] - ETA: 2s
 3200/10000 [========>.....................] - ETA: 2s
 3360/10000 [=========>....................] - ETA: 2s
 3520/10000 [=========>....................] - ETA: 2s
 3648/10000 [=========>....................] - ETA: 2s
 3808/10000 [==========>...................] - ETA: 2s
 3968/10000 [==========>...................] - ETA: 2s
 4128/10000 [===========>..................] - ETA: 2s
 4288/10000 [===========>..................] - ETA: 2s
 4448/10000 [============>.................] - ETA: 2s
 4576/10000 [============>.................] - ETA: 2s
 4736/10000 [=============>................] - ETA: 2s
 4896/10000 [=============>................] - ETA: 2s
 5056/10000 [==============>...............] - ETA: 1s
 5216/10000 [==============>...............] - ETA: 1s
 5344/10000 [===============>..............] - ETA: 1s
 5504/10000 [===============>..............] - ETA: 1s
 5664/10000 [===============>..............] - ETA: 1s
 5824/10000 [================>.............] - ETA: 1s
 5952/10000 [================>.............] - ETA: 1s
 6112/10000 [=================>............] - ETA: 1s
 6272/10000 [=================>............] - ETA: 1s
 6400/10000 [==================>...........] - ETA: 1s
 6528/10000 [==================>...........] - ETA: 1s
 6656/10000 [==================>...........] - ETA: 1s
 6784/10000 [===================>..........] - ETA: 1s
 6944/10000 [===================>..........] - ETA: 1s
 7104/10000 [====================>.........] - ETA: 1s
 7232/10000 [====================>.........] - ETA: 1s
 7392/10000 [=====================>........] - ETA: 1s
 7552/10000 [=====================>........] - ETA: 0s
 7712/10000 [======================>.......] - ETA: 0s
 7872/10000 [======================>.......] - ETA: 0s
 8032/10000 [=======================>......] - ETA: 0s
 8160/10000 [=======================>......] - ETA: 0s
 8288/10000 [=======================>......] - ETA: 0s
 8448/10000 [========================>.....] - ETA: 0s
 8608/10000 [========================>.....] - ETA: 0s
 8768/10000 [=========================>....] - ETA: 0s
 8896/10000 [=========================>....] - ETA: 0s
 9056/10000 [==========================>...] - ETA: 0s
 9184/10000 [==========================>...] - ETA: 0s
 9344/10000 [===========================>..] - ETA: 0s
 9504/10000 [===========================>..] - ETA: 0s
 9664/10000 [===========================>..] - ETA: 0s
 9824/10000 [============================>.] - ETA: 0s
 9984/10000 [============================>.] - ETA: 0s
10000/10000 [==============================] - 4s 390us/step
[[1.6761273e-08 6.3997119e-09 5.9408237e-08 ... 9.9999917e-01
  3.7824579e-09 4.0661942e-07]
 [5.6616454e-07 7.6670867e-06 9.9998689e-01 ... 6.7744224e-09
  1.5419037e-06 1.7265815e-10]
 [7.4624872e-08 9.9997461e-01 1.0041559e-05 ... 4.5801357e-06
  2.8479858e-06 4.8942052e-08]
 ...
 [1.5616328e-09 2.3368267e-07 1.9686330e-09 ... 2.6198175e-06
  1.0360448e-06 3.1701955e-05]
 [8.7358485e-06 1.0024041e-07 2.1761667e-07 ... 2.9657867e-08
  2.5205174e-03 1.6482220e-06]
 [3.0431509e-06 9.9773551e-08 1.6299409e-06 ... 2.2226614e-10
  7.9141921e-07 2.3889253e-09]]

  ('#### metrics   ####################################################',) 

  ('#### Path params   ################################################',) 

  ('/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/', '/home/runner/work/mlmodels/mlmodels/keras_deepAR/') 
{'loss_test:': 0.047662324998306575, 'accuracy_test:': 0.984499990940094}

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
[master 0984e65] ml_store  && git pull --all
 1 file changed, 2039 insertions(+)
To github.com:arita37/mlmodels_store.git
 + 153f369...0984e65 master -> master (forced update)





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
{'loss': 0.4525422677397728, 'loss_history': []}

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
[master 5d4c29b] ml_store  && git pull --all
 1 file changed, 111 insertions(+)
To github.com:arita37/mlmodels_store.git
   0984e65..5d4c29b  master -> master





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
[master c239b25] ml_store  && git pull --all
 1 file changed, 34 insertions(+)
To github.com:arita37/mlmodels_store.git
   5d4c29b..c239b25  master -> master





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
	Data preprocessing and feature engineering runtime = 0.26s ...
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
 40%|████      | 2/5 [00:22<00:34, 11.43s/it]Saving dataset/models/LightGBMClassifier/trial_1_model.pkl
Finished Task with config: {'feature_fraction': 0.9548765553068805, 'learning_rate': 0.14200008152063784, 'min_data_in_leaf': 16, 'num_leaves': 32} and reward: 0.3908
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xee\x8eYG\x18StX\r\x00\x00\x00learning_rateq\x02G?\xc2-\x0f\x05\x14\x8aeX\x10\x00\x00\x00min_data_in_leafq\x03K\x10X\n\x00\x00\x00num_leavesq\x04K u.' and reward: 0.3908
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xee\x8eYG\x18StX\r\x00\x00\x00learning_rateq\x02G?\xc2-\x0f\x05\x14\x8aeX\x10\x00\x00\x00min_data_in_leafq\x03K\x10X\n\x00\x00\x00num_leavesq\x04K u.' and reward: 0.3908
 60%|██████    | 3/5 [00:43<00:28, 14.23s/it]Saving dataset/models/LightGBMClassifier/trial_2_model.pkl
Finished Task with config: {'feature_fraction': 0.9295283243034723, 'learning_rate': 0.005794340851071489, 'min_data_in_leaf': 3, 'num_leaves': 38} and reward: 0.385
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xed\xbe\xb2/2\xd9\xdfX\r\x00\x00\x00learning_rateq\x02G?w\xbb\xce\x87P\xcf3X\x10\x00\x00\x00min_data_in_leafq\x03K\x03X\n\x00\x00\x00num_leavesq\x04K&u.' and reward: 0.385
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xed\xbe\xb2/2\xd9\xdfX\r\x00\x00\x00learning_rateq\x02G?w\xbb\xce\x87P\xcf3X\x10\x00\x00\x00min_data_in_leafq\x03K\x03X\n\x00\x00\x00num_leavesq\x04K&u.' and reward: 0.385
 80%|████████  | 4/5 [01:07<00:17, 17.27s/it] 80%|████████  | 4/5 [01:08<00:17, 17.00s/it]
Saving dataset/models/LightGBMClassifier/trial_3_model.pkl
Finished Task with config: {'feature_fraction': 0.9039629129955767, 'learning_rate': 0.009833622364190673, 'min_data_in_leaf': 23, 'num_leaves': 57} and reward: 0.3876
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xec\xedC\xa1\x83\x9c\xd7X\r\x00\x00\x00learning_rateq\x02G?\x84#\xa6s\xa4\xaf\xa5X\x10\x00\x00\x00min_data_in_leafq\x03K\x17X\n\x00\x00\x00num_leavesq\x04K9u.' and reward: 0.3876
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xec\xedC\xa1\x83\x9c\xd7X\r\x00\x00\x00learning_rateq\x02G?\x84#\xa6s\xa4\xaf\xa5X\x10\x00\x00\x00min_data_in_leafq\x03K\x17X\n\x00\x00\x00num_leavesq\x04K9u.' and reward: 0.3876
Time for Gradient Boosting hyperparameter optimization: 100.1417293548584
Best hyperparameter configuration for Gradient Boosting Model: 
{'feature_fraction': 1.0, 'learning_rate': 0.1, 'min_data_in_leaf': 20, 'num_leaves': 36}
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
 40%|████      | 2/5 [00:55<01:23, 27.84s/it] 40%|████      | 2/5 [00:55<01:23, 27.85s/it]
Loading: dataset/models/NeuralNetClassifier/train_tabNNdataset.pkl
Loading: dataset/models/NeuralNetClassifier/validation_tabNNdataset.pkl
Saving dataset/models/NeuralNetClassifier/trial_5_tabularNN.pkl
Finished Task with config: {'activation.choice': 1, 'dropout_prob': 0.4305919790377471, 'embedding_size_factor': 0.917445944972391, 'layers.choice': 1, 'learning_rate': 0.00048473140101954756, 'network_type.choice': 1, 'use_batchnorm.choice': 1, 'weight_decay': 0.0012890685911458467} and reward: 0.3514
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x01X\x0c\x00\x00\x00dropout_probq\x02G?\xdb\x8e\xd1\xa8\xf8\xc5IX\x15\x00\x00\x00embedding_size_factorq\x03G?\xed[\xb7\x990"\xb1X\r\x00\x00\x00layers.choiceq\x04K\x01X\r\x00\x00\x00learning_rateq\x05G??\xc4q\x83\xc4\xe6\x9bX\x13\x00\x00\x00network_type.choiceq\x06K\x01X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x01X\x0c\x00\x00\x00weight_decayq\x08G?U\x1e\xbe\xdc=\xcd\xc8u.' and reward: 0.3514
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x01X\x0c\x00\x00\x00dropout_probq\x02G?\xdb\x8e\xd1\xa8\xf8\xc5IX\x15\x00\x00\x00embedding_size_factorq\x03G?\xed[\xb7\x990"\xb1X\r\x00\x00\x00layers.choiceq\x04K\x01X\r\x00\x00\x00learning_rateq\x05G??\xc4q\x83\xc4\xe6\x9bX\x13\x00\x00\x00network_type.choiceq\x06K\x01X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x01X\x0c\x00\x00\x00weight_decayq\x08G?U\x1e\xbe\xdc=\xcd\xc8u.' and reward: 0.3514
Please either provide filename or allow plot in get_training_curves
Time for Neural Network hyperparameter optimization: 155.55453181266785
Best hyperparameter configuration for Tabular Neural Network: 
{'activation.choice': 0, 'dropout_prob': 0.1, 'embedding_size_factor': 1.0, 'layers.choice': 0, 'learning_rate': 0.0005, 'network_type.choice': 0, 'use_batchnorm.choice': 0, 'weight_decay': 1e-06}
Saving dataset/models/trainer.pkl
Loading: dataset/models/LightGBMClassifier/trial_0_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_1_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_2_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_3_model.pkl
Loading: dataset/models/NeuralNetClassifier/trial_4_tabularNN.pkl
Loading: dataset/models/NeuralNetClassifier/trial_5_tabularNN.pkl
Fitting model: weighted_ensemble_k0_l1 ... Training model for up to 119.74s of the -139.8s of remaining time.
Ensemble size: 13
Ensemble weights: 
[0.38461538 0.07692308 0.23076923 0.         0.07692308 0.23076923]
	0.4	 = Validation accuracy score
	1.59s	 = Training runtime
	0.0s	 = Validation runtime
Saving dataset/models/weighted_ensemble_k0_l1/model.pkl
Saving dataset/models/trainer.pkl
Saving dataset/models/trainer.pkl
Saving dataset/models/trainer.pkl
AutoGluon training complete, total runtime = 261.44s ...
Loading: dataset/models/trainer.pkl

  #### save the trained model  ####################################### 

  #### Predict   #################################################### 
Loaded data from: https://autogluon.s3.amazonaws.com/datasets/Inc/test.csv | Columns = 15 / 15 | Rows = 9769 -> 9769
Loading: dataset/models/trainer.pkl
Loading: dataset/models/weighted_ensemble_k0_l1/model.pkl
Loading: dataset/models/LightGBMClassifier/trial_0_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_1_model.pkl
Loading: dataset/models/NeuralNetClassifier/trial_4_tabularNN.pkl
Loading: dataset/models/LightGBMClassifier/trial_2_model.pkl
Loading: dataset/models/NeuralNetClassifier/trial_5_tabularNN.pkl

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
Saving dataset/learner.pkl
TabularPredictor saved. To load, use: TabularPredictor.load(dataset/)
<mlmodels.model_gluon.util_autogluon.Model_empty object at 0x7f1e23bcc7f0>

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
[master 97516b7] ml_store  && git pull --all
 1 file changed, 197 insertions(+)
To github.com:arita37/mlmodels_store.git
 + 6ef78f3...97516b7 master -> master (forced update)





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
[master e3a8ffc] ml_store  && git pull --all
 1 file changed, 34 insertions(+)
Warning: Permanently added the RSA host key for IP address '140.82.112.3' to the list of known hosts.
To github.com:arita37/mlmodels_store.git
   97516b7..e3a8ffc  master -> master





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
100%|██████████| 10/10 [00:02<00:00,  3.41it/s, avg_epoch_loss=5.27]
INFO:root:Epoch[0] Elapsed time 2.935 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=5.271965
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 5.271964883804321 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7eff735823c8>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7eff735823c8>

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
Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 94.21it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 1054.6168619791667,
    "abs_error": 368.46429443359375,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 2.441425926062585,
    "sMAPE": 0.5109808692462534,
    "MSIS": 97.65704674848458,
    "QuantileLoss[0.5]": 368.46431732177734,
    "Coverage[0.5]": 1.0,
    "RMSE": 32.47486508023038,
    "NRMSE": 0.6836813701101133,
    "ND": 0.6464285867256031,
    "wQuantileLoss[0.5]": 0.6464286268803111,
    "mean_wQuantileLoss": 0.6464286268803111,
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
100%|██████████| 10/10 [00:01<00:00,  7.09it/s, avg_epoch_loss=2.71e+3]
INFO:root:Epoch[0] Elapsed time 1.412 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=2713.411247
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 2713.4112467447917 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7eff6bc229e8>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7eff6bc229e8>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 139.09it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
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
100%|██████████| 10/10 [00:01<00:00,  5.14it/s, avg_epoch_loss=5.26]
INFO:root:Epoch[0] Elapsed time 1.948 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=5.263111
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 5.2631114482879635 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7eff480abd30>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7eff480abd30>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 142.08it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 283.06024169921875,
    "abs_error": 187.05648803710938,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 1.2394269035865029,
    "sMAPE": 0.3052227156271287,
    "MSIS": 49.577071290469526,
    "QuantileLoss[0.5]": 187.05647659301758,
    "Coverage[0.5]": 0.75,
    "RMSE": 16.824394244644257,
    "NRMSE": 0.35419777357145804,
    "ND": 0.32816927725808664,
    "wQuantileLoss[0.5]": 0.3281692571807326,
    "mean_wQuantileLoss": 0.3281692571807326,
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
 30%|███       | 3/10 [00:13<00:31,  4.53s/it, avg_epoch_loss=6.93] 60%|██████    | 6/10 [00:25<00:17,  4.36s/it, avg_epoch_loss=6.9]  90%|█████████ | 9/10 [00:37<00:04,  4.22s/it, avg_epoch_loss=6.87]100%|██████████| 10/10 [00:41<00:00,  4.12s/it, avg_epoch_loss=6.86]
INFO:root:Epoch[0] Elapsed time 41.184 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=6.855105
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 6.855105018615722 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7eff407bf8d0>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7eff407bf8d0>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 108.20it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 52922.223958333336,
    "abs_error": 2702.5791015625,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 17.907153516549926,
    "sMAPE": 1.4096994170755426,
    "MSIS": 716.28619242723,
    "QuantileLoss[0.5]": 2702.579345703125,
    "Coverage[0.5]": 1.0,
    "RMSE": 230.04830787974367,
    "NRMSE": 4.843122271152499,
    "ND": 4.741366844846492,
    "wQuantileLoss[0.5]": 4.741367273163378,
    "mean_wQuantileLoss": 4.741367273163378,
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
100%|██████████| 10/10 [00:00<00:00, 45.64it/s, avg_epoch_loss=5.18]
INFO:root:Epoch[0] Elapsed time 0.220 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=5.177787
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 5.177786922454834 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7eff40564f28>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7eff40564f28>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 92.55it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 521.1596272786459,
    "abs_error": 189.61862182617188,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 1.256403473509713,
    "sMAPE": 0.31833825939142657,
    "MSIS": 50.256134087397925,
    "QuantileLoss[0.5]": 189.61861419677734,
    "Coverage[0.5]": 0.6666666666666666,
    "RMSE": 22.82892085225769,
    "NRMSE": 0.4806088600475303,
    "ND": 0.3326642488178454,
    "wQuantileLoss[0.5]": 0.3326642354329427,
    "mean_wQuantileLoss": 0.3326642354329427,
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
100%|██████████| 10/10 [00:01<00:00,  7.49it/s, avg_epoch_loss=161]
INFO:root:Epoch[0] Elapsed time 1.335 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=161.108291
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 161.1082910709855 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7eff407f6eb8>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7eff407f6eb8>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 125.65it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
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
 10%|█         | 1/10 [02:05<18:47, 125.29s/it, avg_epoch_loss=0.582] 20%|██        | 2/10 [05:14<19:15, 144.38s/it, avg_epoch_loss=0.565] 30%|███       | 3/10 [08:19<18:16, 156.58s/it, avg_epoch_loss=0.548] 40%|████      | 4/10 [11:34<16:48, 168.10s/it, avg_epoch_loss=0.531] 50%|█████     | 5/10 [15:24<15:34, 186.89s/it, avg_epoch_loss=0.515] 60%|██████    | 6/10 [18:48<12:47, 191.84s/it, avg_epoch_loss=0.499] 70%|███████   | 7/10 [21:58<09:33, 191.29s/it, avg_epoch_loss=0.484] 80%|████████  | 8/10 [25:41<06:41, 200.83s/it, avg_epoch_loss=0.47]  90%|█████████ | 9/10 [29:04<03:21, 201.61s/it, avg_epoch_loss=0.457]100%|██████████| 10/10 [32:56<00:00, 210.51s/it, avg_epoch_loss=0.447]100%|██████████| 10/10 [32:56<00:00, 197.62s/it, avg_epoch_loss=0.447]
INFO:root:Epoch[0] Elapsed time 1976.235 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=0.446552
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 0.4465524971485138 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7eff404aecc0>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7eff404aecc0>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 15.91it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
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
[master e9cb669] ml_store  && git pull --all
 1 file changed, 499 insertions(+)
To github.com:arita37/mlmodels_store.git
 + 46eba0f...e9cb669 master -> master (forced update)





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

  <mlmodels.model_sklearn.model_sklearn.Model object at 0x7f30c7809470> 

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
