
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
Already up to date.
[master 08c9b66] ml_store
 2 files changed, 63 insertions(+), 10194 deletions(-)
 rewrite log_testall/log_testall.py (99%)
To github.com:arita37/mlmodels_store.git
   6abdc20..08c9b66  master -> master





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
[master 934e06b] ml_store
 1 file changed, 48 insertions(+)
To github.com:arita37/mlmodels_store.git
   08c9b66..934e06b  master -> master





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
[master e7fa9c8] ml_store
 1 file changed, 48 insertions(+)
To github.com:arita37/mlmodels_store.git
   934e06b..e7fa9c8  master -> master





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
sequence_mean (InputLayer)      [(None, 8)]          0                                            
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
linear0sparse_seq_emb_sequence_ (None, 6, 1)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 8, 1)         2           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         9           sequence_max[0][0]               
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           sparse_feature_2[0][0]           
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
sparse_seq_emb_sequence_sum (Em (None, 6, 4)         16          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 8, 4)         8           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 9, 4)         36          sequence_max[0][0]               
__________________________________________________________________________________________________
concatenate (Concatenate)       (None, 1, 7)         0           no_mask[0][0]                    
                                                                 no_mask[1][0]                    
                                                                 no_mask[2][0]                    
                                                                 no_mask[3][0]                    
                                                                 no_mask[4][0]                    
                                                                 no_mask[5][0]                    
                                                                 no_mask[6][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         32          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         28          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         24          sparse_feature_2[0][0]           
__________________________________________________________________________________________________
sequence_pooling_layer (Sequenc (None, 1, 4)         0           weighted_sequence_layer[0][0]    2020-05-19 08:12:53.511527: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2020-05-19 08:12:53.526082: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2294685000 Hz
2020-05-19 08:12:53.526311: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x5584fd923240 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-19 08:12:53.526332: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version

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
100/500 [=====>........................] - ETA: 2s - loss: 0.2500 - binary_crossentropy: 0.6932500/500 [==============================] - 1s 2ms/sample - loss: 0.2500 - binary_crossentropy: 0.6930 - val_loss: 0.2500 - val_binary_crossentropy: 0.6931

  #### metrics   #################################################### 
{'MSE': 0.24976768545612418}

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
sequence_mean (InputLayer)      [(None, 8)]          0                                            
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
linear0sparse_seq_emb_sequence_ (None, 6, 1)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 8, 1)         2           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         9           sequence_max[0][0]               
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           sparse_feature_2[0][0]           
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
sparse_seq_emb_sequence_sum (Em (None, 6, 4)         16          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 8, 4)         8           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 9, 4)         36          sequence_max[0][0]               
__________________________________________________________________________________________________
concatenate (Concatenate)       (None, 1, 7)         0           no_mask[0][0]                    
                                                                 no_mask[1][0]                    
                                                                 no_mask[2][0]                    
                                                                 no_mask[3][0]                    
                                                                 no_mask[4][0]                    
                                                                 no_mask[5][0]                    
                                                                 no_mask[6][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         32          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         28          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         24          sparse_feature_2[0][0]           
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
sequence_sum (InputLayer)       [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 9)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_3 (Weig (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 9, 4)         24          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 9, 4)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 9, 4)         12          sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 9, 1)         6           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         1           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         3           sequence_max[0][0]               
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
100/500 [=====>........................] - ETA: 1s - loss: 0.2503 - binary_crossentropy: 0.6937500/500 [==============================] - 1s 2ms/sample - loss: 0.2504 - binary_crossentropy: 0.6940 - val_loss: 0.2542 - val_binary_crossentropy: 0.7016

  #### metrics   #################################################### 
{'MSE': 0.2521058173315698}

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
sequence_sum (InputLayer)       [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 9)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_3 (Weig (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 9, 4)         24          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 9, 4)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 9, 4)         12          sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 9, 1)         6           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         1           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         3           sequence_max[0][0]               
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
sequence_sum (InputLayer)       [(None, 1)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 8)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 1, 4)         24          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 9, 4)         8           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 8, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         32          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         36          sparse_feature_1[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 1, 1)         6           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         2           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 8, 1)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
conv2d_1 (Conv2D)               (None, 3, 4, 1)      5           k_max_pooling[0][0]              
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         9           sparse_feature_1[0][0]           
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
Total params: 652
Trainable params: 652
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 2s - loss: 0.2500 - binary_crossentropy: 0.6931500/500 [==============================] - 1s 2ms/sample - loss: 0.2500 - binary_crossentropy: 0.6932 - val_loss: 0.2500 - val_binary_crossentropy: 0.6931

  #### metrics   #################################################### 
{'MSE': 0.24984502641970213}

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
sequence_sum (InputLayer)       [(None, 1)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 9)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 8)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 1, 4)         24          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 9, 4)         8           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 8, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         32          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         36          sparse_feature_1[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 1, 1)         6           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         2           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 8, 1)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
conv2d_1 (Conv2D)               (None, 3, 4, 1)      5           k_max_pooling[0][0]              
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         9           sparse_feature_1[0][0]           
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
Total params: 652
Trainable params: 652
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
sequence_sum (InputLayer)       [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 5)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 2, 4)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 6, 4)         24          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 5, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         32          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         24          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         8           sparse_feature_2[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 2, 1)         2           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         6           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_4 (Flatten)             (None, 28)           0           concatenate_9[0][0]              
__________________________________________________________________________________________________
flatten_5 (Flatten)             (None, 3)            0           concatenate_10[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         2           sparse_feature_2[0][0]           
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
Total params: 438
Trainable params: 438
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 2s - loss: 0.2725 - binary_crossentropy: 0.7411500/500 [==============================] - 1s 3ms/sample - loss: 0.2586 - binary_crossentropy: 0.7112 - val_loss: 0.2495 - val_binary_crossentropy: 0.6923

  #### metrics   #################################################### 
{'MSE': 0.2522076103373604}

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
sequence_sum (InputLayer)       [(None, 2)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 6)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 5)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 2, 4)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 6, 4)         24          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 5, 4)         32          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         32          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         24          sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 4)         8           sparse_feature_2[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 2, 1)         2           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         6           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         8           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_4 (Flatten)             (None, 28)           0           concatenate_9[0][0]              
__________________________________________________________________________________________________
flatten_5 (Flatten)             (None, 3)            0           concatenate_10[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         2           sparse_feature_2[0][0]           
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
Total params: 438
Trainable params: 438
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
sequence_mean (InputLayer)      [(None, 6)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 9, 4)         24          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 6, 4)         36          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 9, 4)         12          sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 9, 1)         6           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         9           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         3           sequence_max[0][0]               
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
Total params: 188
Trainable params: 188
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 2s - loss: 0.2594 - binary_crossentropy: 0.7167500/500 [==============================] - 2s 4ms/sample - loss: 0.2634 - binary_crossentropy: 0.7244 - val_loss: 0.2966 - val_binary_crossentropy: 0.7970

  #### metrics   #################################################### 
{'MSE': 0.27912580307103446}

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
sequence_mean (InputLayer)      [(None, 6)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 9, 4)         24          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 6, 4)         36          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 9, 4)         12          sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 9, 1)         6           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 6, 1)         9           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 9, 1)         3           sequence_max[0][0]               
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
Total params: 188
Trainable params: 188
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
dnn_4 (DNN)                     (None, 4)            152         concatenate_20[0][0]             2020-05-19 08:14:21.495396: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 08:14:21.497675: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 08:14:21.504307: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-19 08:14:21.516521: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-19 08:14:21.518697: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-19 08:14:21.520689: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 08:14:21.522475: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

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
1/1 [==============================] - 3s 3s/sample - loss: 0.2500 - binary_crossentropy: 0.6931 - val_loss: 0.2551 - val_binary_crossentropy: 0.7033
2020-05-19 08:14:23.041222: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 08:14:23.043192: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 08:14:23.048075: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-19 08:14:23.058182: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer/local_activation_unit/concat' has self cycle fanin 'attention_sequence_pooling_layer/local_activation_unit/concat'.
2020-05-19 08:14:23.059944: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-19 08:14:23.061529: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 08:14:23.063039: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

  #### metrics   #################################################### 
{'MSE': 0.2563813698784904}

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
2020-05-19 08:14:50.345501: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 08:14:50.347084: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 08:14:50.351410: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-19 08:14:50.358890: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-19 08:14:50.360140: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-19 08:14:50.361385: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 08:14:50.362450: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
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
2020-05-19 08:14:52.109553: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 08:14:52.111046: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 08:14:52.114132: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-19 08:14:52.120280: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat' has self cycle fanin 'attention_sequence_pooling_layer_1_1/local_activation_unit_2/concat'.
2020-05-19 08:14:52.121327: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-19 08:14:52.122299: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 08:14:52.123172: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

  #### metrics   #################################################### 
{'MSE': 0.2493006864314419}

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
concatenate_27 (Concatenate)    (None, 1, 16)        0           no_mask_36[0][0]                 2020-05-19 08:15:31.447243: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 08:15:31.452767: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 08:15:31.471043: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-19 08:15:31.520541: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-19 08:15:31.525744: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-19 08:15:31.530404: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 08:15:31.534868: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

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
1/1 [==============================] - 6s 6s/sample - loss: 0.1053 - binary_crossentropy: 0.3922 - val_loss: 0.3232 - val_binary_crossentropy: 0.8665
2020-05-19 08:15:34.183770: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 08:15:34.189107: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 08:15:34.204609: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] model_pruner failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-19 08:15:34.234539: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] remapper failed: Invalid argument: MutableGraphView::MutableGraphView error: node 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat' has self cycle fanin 'attention_sequence_pooling_layer_3/local_activation_unit_5/concat'.
2020-05-19 08:15:34.239632: E tensorflow/core/grappler/optimizers/meta_optimizer.cc:533] arithmetic_optimizer failed: Invalid argument: The graph couldn't be sorted in topological order.
2020-05-19 08:15:34.244178: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 0, topological sort failed with message: The graph couldn't be sorted in topological order.
2020-05-19 08:15:34.248336: E tensorflow/core/grappler/optimizers/dependency_optimizer.cc:697] Iteration = 1, topological sort failed with message: The graph couldn't be sorted in topological order.

  #### metrics   #################################################### 
{'MSE': 0.23302774224966902}

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
sequence_sum (InputLayer)       [(None, 7)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 3)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 7, 4)         36          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 5, 4)         24          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 3, 4)         16          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         12          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         12          sparse_feature_1[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 7, 1)         9           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         6           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         4           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_48 (NoMask)             (None, 120)          0           flatten_19[0][0]                 
__________________________________________________________________________________________________
concatenate_39 (Concatenate)    (None, 2)            0           no_mask_49[0][0]                 
                                                                 no_mask_49[1][0]                 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_1[0][0]           
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
100/500 [=====>........................] - ETA: 8s - loss: 0.2570 - binary_crossentropy: 0.7077500/500 [==============================] - 5s 10ms/sample - loss: 0.2605 - binary_crossentropy: 0.8212 - val_loss: 0.2801 - val_binary_crossentropy: 0.9137

  #### metrics   #################################################### 
{'MSE': 0.2697781242019961}

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
sequence_sum (InputLayer)       [(None, 7)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 5)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 3)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 7, 4)         36          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 5, 4)         24          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 3, 4)         16          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         12          sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 4)         12          sparse_feature_1[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 7, 1)         9           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         6           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         4           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_48 (NoMask)             (None, 120)          0           flatten_19[0][0]                 
__________________________________________________________________________________________________
concatenate_39 (Concatenate)    (None, 2)            0           no_mask_49[0][0]                 
                                                                 no_mask_49[1][0]                 
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_1[0][0]           
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
sequence_sum (InputLayer)       [(None, 7)]          0                                            
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 1)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 7)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 7, 2)         16          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 1, 2)         2           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 7, 2)         6           sequence_max[0][0]               
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
sparse_emb_sparse_feature_3 (Em (None, 1, 2)         6           sparse_feature_3[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 2)         6           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_4 (Em (None, 1, 2)         14          sparse_feature_4[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 2)         16          sparse_feature_2[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 7, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         1           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 7, 1)         3           sequence_max[0][0]               
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
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_3[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_4[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_2[0][0]           
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
Total params: 260
Trainable params: 260
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 8s - loss: 0.2945 - binary_crossentropy: 0.8166500/500 [==============================] - 5s 11ms/sample - loss: 0.2943 - binary_crossentropy: 0.8020 - val_loss: 0.2767 - val_binary_crossentropy: 0.7532

  #### metrics   #################################################### 
{'MSE': 0.2780173544481015}

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
sequence_mean (InputLayer)      [(None, 1)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 7)]          0                                            
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
sparse_seq_emb_sequence_sum (Em (None, 7, 2)         16          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 1, 2)         2           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 7, 2)         6           sequence_max[0][0]               
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
sparse_emb_sparse_feature_3 (Em (None, 1, 2)         6           sparse_feature_3[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1 (Em (None, 1, 2)         6           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_4 (Em (None, 1, 2)         14          sparse_feature_4[0][0]           
__________________________________________________________________________________________________
sparse_emb_sparse_feature_2 (Em (None, 1, 2)         16          sparse_feature_2[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 7, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 1, 1)         1           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 7, 1)         3           sequence_max[0][0]               
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
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_3[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         3           sparse_feature_1[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         7           sparse_feature_4[0][0]           
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         8           sparse_feature_2[0][0]           
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
Total params: 260
Trainable params: 260
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
sequence_mean (InputLayer)      [(None, 8)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 7)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_21 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 6, 4)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 8, 4)         24          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 7, 4)         8           sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 6, 1)         1           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 8, 1)         6           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 7, 1)         2           sequence_max[0][0]               
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
Total params: 1,874
Trainable params: 1,874
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 7s - loss: 0.2788 - binary_crossentropy: 1.0164500/500 [==============================] - 6s 11ms/sample - loss: 0.2748 - binary_crossentropy: 0.8512 - val_loss: 0.2739 - val_binary_crossentropy: 0.7960

  #### metrics   #################################################### 
{'MSE': 0.272116579686632}

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
sequence_mean (InputLayer)      [(None, 8)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 7)]          0                                            
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_21 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 6, 4)         4           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 8, 4)         24          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 7, 4)         8           sequence_max[0][0]               
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
linear0sparse_seq_emb_sequence_ (None, 6, 1)         1           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 8, 1)         6           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 7, 1)         2           sequence_max[0][0]               
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
Total params: 1,874
Trainable params: 1,874
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
regionsequence_mean (InputLayer [(None, 4)]          0                                            
__________________________________________________________________________________________________
regionsequence_max (InputLayer) [(None, 8)]          0                                            
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
region_10sparse_seq_emb_regions (None, 7, 1)         9           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 4, 1)         9           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 8, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_26 (Wei (None, 3, 1)         0           region_20sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 7, 1)         9           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 4, 1)         9           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 8, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_28 (Wei (None, 3, 1)         0           region_30sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 7, 1)         9           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 4, 1)         9           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 8, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_30 (Wei (None, 3, 1)         0           region_40sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 7, 1)         9           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 4, 1)         9           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 8, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_32 (Wei (None, 3, 1)         0           learner_10sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 7, 1)         9           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 4, 1)         9           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 8, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_34 (Wei (None, 3, 1)         0           learner_20sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 7, 1)         9           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 4, 1)         9           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 8, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_36 (Wei (None, 3, 1)         0           learner_30sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 7, 1)         9           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 4, 1)         9           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 8, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_38 (Wei (None, 3, 1)         0           learner_40sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 7, 1)         9           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 4, 1)         9           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 8, 1)         2           regionsequence_max[0][0]         
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
Total params: 192
Trainable params: 192
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 11s - loss: 0.2540 - binary_crossentropy: 0.6990500/500 [==============================] - 7s 14ms/sample - loss: 0.2519 - binary_crossentropy: 0.7228 - val_loss: 0.2498 - val_binary_crossentropy: 0.7183

  #### metrics   #################################################### 
{'MSE': 0.2505605763357448}

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
regionsequence_mean (InputLayer [(None, 4)]          0                                            
__________________________________________________________________________________________________
regionsequence_max (InputLayer) [(None, 8)]          0                                            
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
region_10sparse_seq_emb_regions (None, 7, 1)         9           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 4, 1)         9           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_10sparse_seq_emb_regions (None, 8, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_26 (Wei (None, 3, 1)         0           region_20sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 7, 1)         9           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 4, 1)         9           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_20sparse_seq_emb_regions (None, 8, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_28 (Wei (None, 3, 1)         0           region_30sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 7, 1)         9           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 4, 1)         9           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_30sparse_seq_emb_regions (None, 8, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_30 (Wei (None, 3, 1)         0           region_40sparse_seq_emb_regionwei
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 7, 1)         9           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 4, 1)         9           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
region_40sparse_seq_emb_regions (None, 8, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_32 (Wei (None, 3, 1)         0           learner_10sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 7, 1)         9           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 4, 1)         9           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_10sparse_seq_emb_region (None, 8, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_34 (Wei (None, 3, 1)         0           learner_20sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 7, 1)         9           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 4, 1)         9           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_20sparse_seq_emb_region (None, 8, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_36 (Wei (None, 3, 1)         0           learner_30sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 7, 1)         9           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 4, 1)         9           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_30sparse_seq_emb_region (None, 8, 1)         2           regionsequence_max[0][0]         
__________________________________________________________________________________________________
weighted_sequence_layer_38 (Wei (None, 3, 1)         0           learner_40sparse_seq_emb_regionwe
                                                                 regionweighted_seq_seq_length[0][
                                                                 regionweight[0][0]               
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 7, 1)         9           regionsequence_sum[0][0]         
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 4, 1)         9           regionsequence_mean[0][0]        
__________________________________________________________________________________________________
learner_40sparse_seq_emb_region (None, 8, 1)         2           regionsequence_max[0][0]         
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
Total params: 192
Trainable params: 192
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
sequence_mean (InputLayer)      [(None, 3)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 5)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_40 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 6, 4)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 3, 4)         12          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 5, 4)         24          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         4           sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 6, 1)         2           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         3           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         6           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_101 (NoMask)            (None, 1, 4)         0           bi_interaction_pooling[0][0]     
__________________________________________________________________________________________________
no_mask_102 (NoMask)            (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         1           sparse_feature_0[0][0]           
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
Total params: 1,352
Trainable params: 1,352
Non-trainable params: 0
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 9s - loss: 0.2530 - binary_crossentropy: 0.7002500/500 [==============================] - 7s 14ms/sample - loss: 0.2560 - binary_crossentropy: 0.7062 - val_loss: 0.2553 - val_binary_crossentropy: 0.7039

  #### metrics   #################################################### 
{'MSE': 0.2538068337701093}

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
sequence_mean (InputLayer)      [(None, 3)]          0                                            
__________________________________________________________________________________________________
sequence_max (InputLayer)       [(None, 5)]          0                                            
__________________________________________________________________________________________________
sparse_seq_emb_weighted_seq (Em (None, 3, 4)         8           weighted_seq[0][0]               
__________________________________________________________________________________________________
sparse_feature_0 (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
weighted_sequence_layer_40 (Wei (None, 3, 4)         0           sparse_seq_emb_weighted_seq[0][0]
                                                                 weighted_seq_seq_length[0][0]    
                                                                 weight[0][0]                     
__________________________________________________________________________________________________
sparse_seq_emb_sequence_sum (Em (None, 6, 4)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_seq_emb_sequence_mean (E (None, 3, 4)         12          sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_seq_emb_sequence_max (Em (None, 5, 4)         24          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0 (Em (None, 1, 4)         4           sparse_feature_0[0][0]           
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
linear0sparse_seq_emb_sequence_ (None, 6, 1)         2           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 3, 1)         3           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         6           sequence_max[0][0]               
__________________________________________________________________________________________________
no_mask_101 (NoMask)            (None, 1, 4)         0           bi_interaction_pooling[0][0]     
__________________________________________________________________________________________________
no_mask_102 (NoMask)            (None, 1)            0           dense_feature_0[0][0]            
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         1           sparse_feature_0[0][0]           
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
Total params: 1,352
Trainable params: 1,352
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
sequence_sum (InputLayer)       [(None, 7)]          0                                            
__________________________________________________________________________________________________
hash_17 (Hash)                  (None, 1)            0           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 5)]          0                                            
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
sparse_emb_sparse_feature_1_spa (None, 1, 4)         24          hash_15[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         20          hash_16[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 7, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         20          hash_17[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 5, 4)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         20          hash_18[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 2, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         24          hash_19[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 7, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         24          hash_20[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 5, 4)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         24          hash_21[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 2, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 7, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 5, 4)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 7, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_max_sequenc (None, 2, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 5, 4)         4           sequence_mean[0][0]              
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
linear0sparse_seq_emb_sequence_ (None, 7, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         1           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         7           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_29 (Flatten)            (None, 40)           0           no_mask_116[0][0]                
__________________________________________________________________________________________________
flatten_30 (Flatten)            (None, 2)            0           concatenate_81[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           hash_10[0][0]                    
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           hash_11[0][0]                    
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
Total params: 3,086
Trainable params: 3,006
Non-trainable params: 80
__________________________________________________________________________________________________
Train on 500 samples, validate on 500 samples
100/500 [=====>........................] - ETA: 10s - loss: 0.2682 - binary_crossentropy: 0.8591500/500 [==============================] - 7s 15ms/sample - loss: 0.2615 - binary_crossentropy: 0.8474 - val_loss: 0.2526 - val_binary_crossentropy: 0.7235

  #### metrics   #################################################### 
{'MSE': 0.2568580110419908}

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
sequence_sum (InputLayer)       [(None, 7)]          0                                            
__________________________________________________________________________________________________
hash_17 (Hash)                  (None, 1)            0           sparse_feature_0[0][0]           
__________________________________________________________________________________________________
sequence_mean (InputLayer)      [(None, 5)]          0                                            
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
sparse_emb_sparse_feature_1_spa (None, 1, 4)         24          hash_15[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         20          hash_16[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 7, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         20          hash_17[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 5, 4)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_0_seq (None, 1, 4)         20          hash_18[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 2, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         24          hash_19[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sparse_ (None, 7, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         24          hash_20[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sparse (None, 5, 4)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sparse_feature_1_seq (None, 1, 4)         24          hash_21[0][0]                    
__________________________________________________________________________________________________
sparse_emb_sequence_max_sparse_ (None, 2, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 7, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 5, 4)         4           sequence_mean[0][0]              
__________________________________________________________________________________________________
sparse_emb_sequence_sum_sequenc (None, 7, 4)         32          sequence_sum[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_max_sequenc (None, 2, 4)         28          sequence_max[0][0]               
__________________________________________________________________________________________________
sparse_emb_sequence_mean_sequen (None, 5, 4)         4           sequence_mean[0][0]              
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
linear0sparse_seq_emb_sequence_ (None, 7, 1)         8           sequence_sum[0][0]               
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 5, 1)         1           sequence_mean[0][0]              
__________________________________________________________________________________________________
linear0sparse_seq_emb_sequence_ (None, 2, 1)         7           sequence_max[0][0]               
__________________________________________________________________________________________________
flatten_29 (Flatten)            (None, 40)           0           no_mask_116[0][0]                
__________________________________________________________________________________________________
flatten_30 (Flatten)            (None, 2)            0           concatenate_81[0][0]             
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         5           hash_10[0][0]                    
__________________________________________________________________________________________________
linear0sparse_emb_sparse_featur (None, 1, 1)         6           hash_11[0][0]                    
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
Total params: 3,086
Trainable params: 3,006
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
Warning: Permanently added the RSA host key for IP address '192.30.255.112' to the list of known hosts.
From github.com:arita37/mlmodels_store
   e7fa9c8..20f7166  master     -> origin/master
Updating e7fa9c8..20f7166
Fast-forward
 error_list/20200519/list_log_testall_20200519.md   | 774 +--------------------
 ...-10_73f54da32a5da4768415eb9105ad096255137679.py | 627 +++++++++++++++++
 2 files changed, 629 insertions(+), 772 deletions(-)
 create mode 100644 log_pullrequest/log_pr_2020-05-19-08-10_73f54da32a5da4768415eb9105ad096255137679.py
[master 51c233d] ml_store
 1 file changed, 4955 insertions(+)
To github.com:arita37/mlmodels_store.git
   20f7166..51c233d  master -> master





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
[master 9522820] ml_store
 1 file changed, 51 insertions(+)
To github.com:arita37/mlmodels_store.git
   51c233d..9522820  master -> master





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
[master 49b70f5] ml_store
 1 file changed, 47 insertions(+)
To github.com:arita37/mlmodels_store.git
   9522820..49b70f5  master -> master





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
[master 8c3342e] ml_store
 1 file changed, 36 insertions(+)
To github.com:arita37/mlmodels_store.git
   49b70f5..8c3342e  master -> master





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

2020-05-19 08:25:55.687909: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2020-05-19 08:25:55.693647: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2294685000 Hz
2020-05-19 08:25:55.693887: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x56480e6b0e90 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-19 08:25:55.693908: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
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

128/354 [=========>....................] - ETA: 9s - loss: 1.3871
256/354 [====================>.........] - ETA: 3s - loss: 1.2040
354/354 [==============================] - 16s 45ms/step - loss: 1.2537 - val_loss: 2.4564

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
From github.com:arita37/mlmodels_store
   8c3342e..552ce2b  master     -> origin/master
Updating 8c3342e..552ce2b
Fast-forward
 deps.txt             |   5 +-
 log_json/log_json.py | 304 ++++++++++++++++++++++++++-------------------------
 2 files changed, 156 insertions(+), 153 deletions(-)
[master 3a9642a] ml_store
 1 file changed, 156 insertions(+)
To github.com:arita37/mlmodels_store.git
   552ce2b..3a9642a  master -> master





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
[master a011dbe] ml_store
 2 files changed, 50 insertions(+), 3 deletions(-)
To github.com:arita37/mlmodels_store.git
   3a9642a..a011dbe  master -> master





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
[master bef535a] ml_store
 1 file changed, 45 insertions(+)
To github.com:arita37/mlmodels_store.git
   a011dbe..bef535a  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_keras//textcnn.py 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Loading dataset   ############################################# 
Loading data...
Downloading data from https://s3.amazonaws.com/text-datasets/imdb.npz

    8192/17464789 [..............................] - ETA: 0s
   24576/17464789 [..............................] - ETA: 43s
   57344/17464789 [..............................] - ETA: 37s
   90112/17464789 [..............................] - ETA: 35s
  180224/17464789 [..............................] - ETA: 23s
  335872/17464789 [..............................] - ETA: 15s
  647168/17464789 [>.............................] - ETA: 9s 
 1294336/17464789 [=>............................] - ETA: 5s
 2572288/17464789 [===>..........................] - ETA: 2s
 5128192/17464789 [=======>......................] - ETA: 1s
 8142848/17464789 [============>.................] - ETA: 0s
11108352/17464789 [==================>...........] - ETA: 0s
14090240/17464789 [=======================>......] - ETA: 0s
17055744/17464789 [============================>.] - ETA: 0s
17465344/17464789 [==============================] - 1s 0us/step
Pad sequences (samples x time)...

  #### Model init, fit   ############################################# 
Using TensorFlow backend.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/resource_variable_ops.py:1630: calling BaseResourceVariable.__init__ (from tensorflow.python.ops.resource_variable_ops) with constraint is deprecated and will be removed in a future version.
Instructions for updating:
If using Keras pass *_constraint arguments to layers.
WARNING:tensorflow:From /opt/hostedtoolcache/Python/3.6.10/x64/lib/python3.6/site-packages/tensorflow_core/python/ops/math_grad.py:1424: where (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
2020-05-19 08:27:06.247265: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2020-05-19 08:27:06.252097: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2294685000 Hz
2020-05-19 08:27:06.252623: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x5563a6682330 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
2020-05-19 08:27:06.252643: I tensorflow/compiler/xla/service/service.cc:176]   StreamExecutor device (0): Host, Default Version
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

 1000/25000 [>.............................] - ETA: 14s - loss: 7.5133 - accuracy: 0.5100
 2000/25000 [=>............................] - ETA: 10s - loss: 7.4366 - accuracy: 0.5150
 3000/25000 [==>...........................] - ETA: 9s - loss: 7.5031 - accuracy: 0.5107 
 4000/25000 [===>..........................] - ETA: 8s - loss: 7.6053 - accuracy: 0.5040
 5000/25000 [=====>........................] - ETA: 7s - loss: 7.6390 - accuracy: 0.5018
 6000/25000 [======>.......................] - ETA: 7s - loss: 7.6845 - accuracy: 0.4988
 7000/25000 [=======>......................] - ETA: 6s - loss: 7.7148 - accuracy: 0.4969
 8000/25000 [========>.....................] - ETA: 6s - loss: 7.7337 - accuracy: 0.4956
 9000/25000 [=========>....................] - ETA: 5s - loss: 7.7467 - accuracy: 0.4948
10000/25000 [===========>..................] - ETA: 5s - loss: 7.7172 - accuracy: 0.4967
11000/25000 [============>.................] - ETA: 4s - loss: 7.7321 - accuracy: 0.4957
12000/25000 [=============>................] - ETA: 4s - loss: 7.7254 - accuracy: 0.4962
13000/25000 [==============>...............] - ETA: 4s - loss: 7.7150 - accuracy: 0.4968
14000/25000 [===============>..............] - ETA: 3s - loss: 7.7148 - accuracy: 0.4969
15000/25000 [=================>............] - ETA: 3s - loss: 7.6983 - accuracy: 0.4979
16000/25000 [==================>...........] - ETA: 3s - loss: 7.7059 - accuracy: 0.4974
17000/25000 [===================>..........] - ETA: 2s - loss: 7.6883 - accuracy: 0.4986
18000/25000 [====================>.........] - ETA: 2s - loss: 7.7024 - accuracy: 0.4977
19000/25000 [=====================>........] - ETA: 2s - loss: 7.6941 - accuracy: 0.4982
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6804 - accuracy: 0.4991
21000/25000 [========================>.....] - ETA: 1s - loss: 7.6841 - accuracy: 0.4989
22000/25000 [=========================>....] - ETA: 1s - loss: 7.6882 - accuracy: 0.4986
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6833 - accuracy: 0.4989
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6794 - accuracy: 0.4992
25000/25000 [==============================] - 10s 404us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000

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
(<mlmodels.util.Model_empty object at 0x7f788bad3cf8>, None)

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

  <mlmodels.model_keras.textcnn.Model object at 0x7f78a6a90828> 

  #### Fit   ######################################################## 
Loading data...
Pad sequences (samples x time)...
Train on 25000 samples, validate on 25000 samples
Epoch 1/1

 1000/25000 [>.............................] - ETA: 15s - loss: 7.7433 - accuracy: 0.4950
 2000/25000 [=>............................] - ETA: 11s - loss: 7.7203 - accuracy: 0.4965
 3000/25000 [==>...........................] - ETA: 9s - loss: 7.7177 - accuracy: 0.4967 
 4000/25000 [===>..........................] - ETA: 8s - loss: 7.7318 - accuracy: 0.4958
 5000/25000 [=====>........................] - ETA: 7s - loss: 7.7065 - accuracy: 0.4974
 6000/25000 [======>.......................] - ETA: 7s - loss: 7.6436 - accuracy: 0.5015
 7000/25000 [=======>......................] - ETA: 6s - loss: 7.7126 - accuracy: 0.4970
 8000/25000 [========>.....................] - ETA: 6s - loss: 7.6705 - accuracy: 0.4997
 9000/25000 [=========>....................] - ETA: 5s - loss: 7.6598 - accuracy: 0.5004
10000/25000 [===========>..................] - ETA: 5s - loss: 7.6835 - accuracy: 0.4989
11000/25000 [============>.................] - ETA: 4s - loss: 7.6610 - accuracy: 0.5004
12000/25000 [=============>................] - ETA: 4s - loss: 7.6551 - accuracy: 0.5008
13000/25000 [==============>...............] - ETA: 4s - loss: 7.6454 - accuracy: 0.5014
14000/25000 [===============>..............] - ETA: 3s - loss: 7.6436 - accuracy: 0.5015
15000/25000 [=================>............] - ETA: 3s - loss: 7.6584 - accuracy: 0.5005
16000/25000 [==================>...........] - ETA: 3s - loss: 7.6455 - accuracy: 0.5014
17000/25000 [===================>..........] - ETA: 2s - loss: 7.6396 - accuracy: 0.5018
18000/25000 [====================>.........] - ETA: 2s - loss: 7.6394 - accuracy: 0.5018
19000/25000 [=====================>........] - ETA: 2s - loss: 7.6497 - accuracy: 0.5011
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6467 - accuracy: 0.5013
21000/25000 [========================>.....] - ETA: 1s - loss: 7.6476 - accuracy: 0.5012
22000/25000 [=========================>....] - ETA: 1s - loss: 7.6457 - accuracy: 0.5014
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6626 - accuracy: 0.5003
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6596 - accuracy: 0.5005
25000/25000 [==============================] - 10s 414us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000

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

 1000/25000 [>.............................] - ETA: 15s - loss: 7.7893 - accuracy: 0.4920
 2000/25000 [=>............................] - ETA: 11s - loss: 7.5823 - accuracy: 0.5055
 3000/25000 [==>...........................] - ETA: 9s - loss: 7.5900 - accuracy: 0.5050 
 4000/25000 [===>..........................] - ETA: 8s - loss: 7.4903 - accuracy: 0.5115
 5000/25000 [=====>........................] - ETA: 7s - loss: 7.4765 - accuracy: 0.5124
 6000/25000 [======>.......................] - ETA: 7s - loss: 7.5184 - accuracy: 0.5097
 7000/25000 [=======>......................] - ETA: 6s - loss: 7.5461 - accuracy: 0.5079
 8000/25000 [========>.....................] - ETA: 6s - loss: 7.6015 - accuracy: 0.5042
 9000/25000 [=========>....................] - ETA: 5s - loss: 7.6206 - accuracy: 0.5030
10000/25000 [===========>..................] - ETA: 5s - loss: 7.6114 - accuracy: 0.5036
11000/25000 [============>.................] - ETA: 4s - loss: 7.6555 - accuracy: 0.5007
12000/25000 [=============>................] - ETA: 4s - loss: 7.6423 - accuracy: 0.5016
13000/25000 [==============>...............] - ETA: 4s - loss: 7.6761 - accuracy: 0.4994
14000/25000 [===============>..............] - ETA: 3s - loss: 7.6721 - accuracy: 0.4996
15000/25000 [=================>............] - ETA: 3s - loss: 7.6748 - accuracy: 0.4995
16000/25000 [==================>...........] - ETA: 3s - loss: 7.6705 - accuracy: 0.4997
17000/25000 [===================>..........] - ETA: 2s - loss: 7.6522 - accuracy: 0.5009
18000/25000 [====================>.........] - ETA: 2s - loss: 7.6734 - accuracy: 0.4996
19000/25000 [=====================>........] - ETA: 2s - loss: 7.6481 - accuracy: 0.5012
20000/25000 [=======================>......] - ETA: 1s - loss: 7.6528 - accuracy: 0.5009
21000/25000 [========================>.....] - ETA: 1s - loss: 7.6454 - accuracy: 0.5014
22000/25000 [=========================>....] - ETA: 1s - loss: 7.6408 - accuracy: 0.5017
23000/25000 [==========================>...] - ETA: 0s - loss: 7.6546 - accuracy: 0.5008
24000/25000 [===========================>..] - ETA: 0s - loss: 7.6641 - accuracy: 0.5002
25000/25000 [==============================] - 10s 407us/step - loss: 7.6666 - accuracy: 0.5000 - val_loss: 7.6246 - val_accuracy: 0.5000
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
From github.com:arita37/mlmodels_store
   bef535a..37064ae  master     -> origin/master
Updating bef535a..37064ae
Fast-forward
 error_list/20200519/list_log_json_20200519.md    | 1036 +++++++++++-----------
 error_list/20200519/list_log_testall_20200519.md |  103 +++
 2 files changed, 621 insertions(+), 518 deletions(-)
[master b63baed] ml_store
 1 file changed, 334 insertions(+)
To github.com:arita37/mlmodels_store.git
   37064ae..b63baed  master -> master





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

13/13 [==============================] - 2s 168ms/step - loss: nan
Epoch 2/10

13/13 [==============================] - 0s 6ms/step - loss: nan
Epoch 3/10

13/13 [==============================] - 0s 5ms/step - loss: nan
Epoch 4/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 5/10

13/13 [==============================] - 0s 5ms/step - loss: nan
Epoch 6/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 7/10

13/13 [==============================] - 0s 4ms/step - loss: nan
Epoch 8/10

13/13 [==============================] - 0s 5ms/step - loss: nan
Epoch 9/10

13/13 [==============================] - 0s 5ms/step - loss: nan
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
[master 404e938] ml_store
 1 file changed, 126 insertions(+)
To github.com:arita37/mlmodels_store.git
   b63baed..404e938  master -> master





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
   24576/11490434 [..............................] - ETA: 30s
   57344/11490434 [..............................] - ETA: 25s
   90112/11490434 [..............................] - ETA: 24s
  196608/11490434 [..............................] - ETA: 14s
  385024/11490434 [>.............................] - ETA: 9s 
  786432/11490434 [=>............................] - ETA: 5s
 1572864/11490434 [===>..........................] - ETA: 2s
 3145728/11490434 [=======>......................] - ETA: 1s
 6242304/11490434 [===============>..............] - ETA: 0s
 9240576/11490434 [=======================>......] - ETA: 0s
11493376/11490434 [==============================] - 1s 0us/step

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

   32/60000 [..............................] - ETA: 8:20 - loss: 2.2901 - categorical_accuracy: 0.0938
   64/60000 [..............................] - ETA: 5:10 - loss: 2.2660 - categorical_accuracy: 0.1719
   96/60000 [..............................] - ETA: 4:03 - loss: 2.2591 - categorical_accuracy: 0.1771
  128/60000 [..............................] - ETA: 3:32 - loss: 2.2370 - categorical_accuracy: 0.1797
  160/60000 [..............................] - ETA: 3:13 - loss: 2.2416 - categorical_accuracy: 0.1750
  192/60000 [..............................] - ETA: 3:02 - loss: 2.2399 - categorical_accuracy: 0.1667
  224/60000 [..............................] - ETA: 2:51 - loss: 2.2121 - categorical_accuracy: 0.2054
  256/60000 [..............................] - ETA: 2:43 - loss: 2.1720 - categorical_accuracy: 0.2344
  288/60000 [..............................] - ETA: 2:38 - loss: 2.1473 - categorical_accuracy: 0.2465
  320/60000 [..............................] - ETA: 2:34 - loss: 2.1114 - categorical_accuracy: 0.2625
  352/60000 [..............................] - ETA: 2:30 - loss: 2.0843 - categorical_accuracy: 0.2699
  384/60000 [..............................] - ETA: 2:28 - loss: 2.0300 - categorical_accuracy: 0.2995
  416/60000 [..............................] - ETA: 2:25 - loss: 2.0065 - categorical_accuracy: 0.3101
  448/60000 [..............................] - ETA: 2:23 - loss: 1.9806 - categorical_accuracy: 0.3192
  480/60000 [..............................] - ETA: 2:20 - loss: 1.9520 - categorical_accuracy: 0.3250
  512/60000 [..............................] - ETA: 2:18 - loss: 1.9388 - categorical_accuracy: 0.3281
  544/60000 [..............................] - ETA: 2:16 - loss: 1.9022 - categorical_accuracy: 0.3401
  576/60000 [..............................] - ETA: 2:15 - loss: 1.8716 - categorical_accuracy: 0.3576
  608/60000 [..............................] - ETA: 2:14 - loss: 1.8345 - categorical_accuracy: 0.3750
  640/60000 [..............................] - ETA: 2:12 - loss: 1.8165 - categorical_accuracy: 0.3859
  672/60000 [..............................] - ETA: 2:11 - loss: 1.7846 - categorical_accuracy: 0.4003
  704/60000 [..............................] - ETA: 2:11 - loss: 1.7590 - categorical_accuracy: 0.4105
  736/60000 [..............................] - ETA: 2:10 - loss: 1.7546 - categorical_accuracy: 0.4117
  768/60000 [..............................] - ETA: 2:09 - loss: 1.7245 - categorical_accuracy: 0.4206
  800/60000 [..............................] - ETA: 2:08 - loss: 1.6833 - categorical_accuracy: 0.4350
  832/60000 [..............................] - ETA: 2:07 - loss: 1.6605 - categorical_accuracy: 0.4423
  864/60000 [..............................] - ETA: 2:06 - loss: 1.6402 - categorical_accuracy: 0.4468
  896/60000 [..............................] - ETA: 2:06 - loss: 1.6169 - categorical_accuracy: 0.4587
  928/60000 [..............................] - ETA: 2:05 - loss: 1.5991 - categorical_accuracy: 0.4666
  960/60000 [..............................] - ETA: 2:04 - loss: 1.5811 - categorical_accuracy: 0.4740
  992/60000 [..............................] - ETA: 2:04 - loss: 1.5593 - categorical_accuracy: 0.4798
 1024/60000 [..............................] - ETA: 2:03 - loss: 1.5275 - categorical_accuracy: 0.4922
 1056/60000 [..............................] - ETA: 2:03 - loss: 1.5201 - categorical_accuracy: 0.4953
 1088/60000 [..............................] - ETA: 2:02 - loss: 1.5005 - categorical_accuracy: 0.5028
 1120/60000 [..............................] - ETA: 2:02 - loss: 1.4787 - categorical_accuracy: 0.5098
 1152/60000 [..............................] - ETA: 2:01 - loss: 1.4561 - categorical_accuracy: 0.5148
 1184/60000 [..............................] - ETA: 2:01 - loss: 1.4370 - categorical_accuracy: 0.5211
 1216/60000 [..............................] - ETA: 2:01 - loss: 1.4159 - categorical_accuracy: 0.5263
 1248/60000 [..............................] - ETA: 2:01 - loss: 1.4065 - categorical_accuracy: 0.5288
 1280/60000 [..............................] - ETA: 2:00 - loss: 1.3877 - categorical_accuracy: 0.5359
 1312/60000 [..............................] - ETA: 2:00 - loss: 1.3716 - categorical_accuracy: 0.5427
 1344/60000 [..............................] - ETA: 2:00 - loss: 1.3535 - categorical_accuracy: 0.5491
 1376/60000 [..............................] - ETA: 1:59 - loss: 1.3347 - categorical_accuracy: 0.5552
 1408/60000 [..............................] - ETA: 1:59 - loss: 1.3188 - categorical_accuracy: 0.5611
 1440/60000 [..............................] - ETA: 1:59 - loss: 1.3031 - categorical_accuracy: 0.5667
 1472/60000 [..............................] - ETA: 1:58 - loss: 1.2876 - categorical_accuracy: 0.5720
 1504/60000 [..............................] - ETA: 1:58 - loss: 1.2696 - categorical_accuracy: 0.5778
 1536/60000 [..............................] - ETA: 1:58 - loss: 1.2542 - categorical_accuracy: 0.5827
 1568/60000 [..............................] - ETA: 1:58 - loss: 1.2404 - categorical_accuracy: 0.5861
 1600/60000 [..............................] - ETA: 1:58 - loss: 1.2251 - categorical_accuracy: 0.5913
 1632/60000 [..............................] - ETA: 1:57 - loss: 1.2156 - categorical_accuracy: 0.5950
 1664/60000 [..............................] - ETA: 1:57 - loss: 1.2050 - categorical_accuracy: 0.5992
 1696/60000 [..............................] - ETA: 1:57 - loss: 1.1915 - categorical_accuracy: 0.6032
 1728/60000 [..............................] - ETA: 1:57 - loss: 1.1762 - categorical_accuracy: 0.6076
 1760/60000 [..............................] - ETA: 1:56 - loss: 1.1690 - categorical_accuracy: 0.6097
 1792/60000 [..............................] - ETA: 1:56 - loss: 1.1589 - categorical_accuracy: 0.6110
 1824/60000 [..............................] - ETA: 1:56 - loss: 1.1484 - categorical_accuracy: 0.6140
 1856/60000 [..............................] - ETA: 1:56 - loss: 1.1376 - categorical_accuracy: 0.6175
 1888/60000 [..............................] - ETA: 1:56 - loss: 1.1311 - categorical_accuracy: 0.6197
 1920/60000 [..............................] - ETA: 1:56 - loss: 1.1200 - categorical_accuracy: 0.6229
 1952/60000 [..............................] - ETA: 1:55 - loss: 1.1110 - categorical_accuracy: 0.6260
 1984/60000 [..............................] - ETA: 1:55 - loss: 1.1039 - categorical_accuracy: 0.6280
 2016/60000 [>.............................] - ETA: 1:55 - loss: 1.1013 - categorical_accuracy: 0.6290
 2048/60000 [>.............................] - ETA: 1:55 - loss: 1.0902 - categorical_accuracy: 0.6333
 2080/60000 [>.............................] - ETA: 1:55 - loss: 1.0822 - categorical_accuracy: 0.6370
 2112/60000 [>.............................] - ETA: 1:55 - loss: 1.0748 - categorical_accuracy: 0.6402
 2144/60000 [>.............................] - ETA: 1:55 - loss: 1.0639 - categorical_accuracy: 0.6446
 2176/60000 [>.............................] - ETA: 1:54 - loss: 1.0566 - categorical_accuracy: 0.6466
 2208/60000 [>.............................] - ETA: 1:54 - loss: 1.0477 - categorical_accuracy: 0.6495
 2240/60000 [>.............................] - ETA: 1:54 - loss: 1.0354 - categorical_accuracy: 0.6536
 2272/60000 [>.............................] - ETA: 1:54 - loss: 1.0269 - categorical_accuracy: 0.6567
 2304/60000 [>.............................] - ETA: 1:54 - loss: 1.0202 - categorical_accuracy: 0.6584
 2336/60000 [>.............................] - ETA: 1:54 - loss: 1.0127 - categorical_accuracy: 0.6605
 2368/60000 [>.............................] - ETA: 1:54 - loss: 1.0133 - categorical_accuracy: 0.6617
 2400/60000 [>.............................] - ETA: 1:54 - loss: 1.0091 - categorical_accuracy: 0.6637
 2432/60000 [>.............................] - ETA: 1:54 - loss: 1.0015 - categorical_accuracy: 0.6657
 2464/60000 [>.............................] - ETA: 1:53 - loss: 0.9944 - categorical_accuracy: 0.6680
 2496/60000 [>.............................] - ETA: 1:53 - loss: 0.9878 - categorical_accuracy: 0.6707
 2528/60000 [>.............................] - ETA: 1:53 - loss: 0.9822 - categorical_accuracy: 0.6729
 2560/60000 [>.............................] - ETA: 1:53 - loss: 0.9761 - categorical_accuracy: 0.6750
 2592/60000 [>.............................] - ETA: 1:53 - loss: 0.9735 - categorical_accuracy: 0.6775
 2624/60000 [>.............................] - ETA: 1:53 - loss: 0.9680 - categorical_accuracy: 0.6791
 2656/60000 [>.............................] - ETA: 1:53 - loss: 0.9632 - categorical_accuracy: 0.6800
 2688/60000 [>.............................] - ETA: 1:52 - loss: 0.9572 - categorical_accuracy: 0.6819
 2720/60000 [>.............................] - ETA: 1:52 - loss: 0.9512 - categorical_accuracy: 0.6849
 2752/60000 [>.............................] - ETA: 1:52 - loss: 0.9427 - categorical_accuracy: 0.6879
 2784/60000 [>.............................] - ETA: 1:52 - loss: 0.9372 - categorical_accuracy: 0.6893
 2816/60000 [>.............................] - ETA: 1:52 - loss: 0.9353 - categorical_accuracy: 0.6893
 2848/60000 [>.............................] - ETA: 1:52 - loss: 0.9300 - categorical_accuracy: 0.6907
 2880/60000 [>.............................] - ETA: 1:52 - loss: 0.9265 - categorical_accuracy: 0.6927
 2912/60000 [>.............................] - ETA: 1:51 - loss: 0.9210 - categorical_accuracy: 0.6940
 2944/60000 [>.............................] - ETA: 1:51 - loss: 0.9169 - categorical_accuracy: 0.6957
 2976/60000 [>.............................] - ETA: 1:51 - loss: 0.9091 - categorical_accuracy: 0.6983
 3008/60000 [>.............................] - ETA: 1:51 - loss: 0.9024 - categorical_accuracy: 0.7001
 3040/60000 [>.............................] - ETA: 1:51 - loss: 0.8979 - categorical_accuracy: 0.7013
 3072/60000 [>.............................] - ETA: 1:51 - loss: 0.8911 - categorical_accuracy: 0.7031
 3104/60000 [>.............................] - ETA: 1:51 - loss: 0.8838 - categorical_accuracy: 0.7055
 3136/60000 [>.............................] - ETA: 1:51 - loss: 0.8784 - categorical_accuracy: 0.7079
 3168/60000 [>.............................] - ETA: 1:51 - loss: 0.8729 - categorical_accuracy: 0.7093
 3200/60000 [>.............................] - ETA: 1:51 - loss: 0.8703 - categorical_accuracy: 0.7103
 3232/60000 [>.............................] - ETA: 1:51 - loss: 0.8639 - categorical_accuracy: 0.7132
 3264/60000 [>.............................] - ETA: 1:50 - loss: 0.8586 - categorical_accuracy: 0.7151
 3296/60000 [>.............................] - ETA: 1:50 - loss: 0.8533 - categorical_accuracy: 0.7169
 3328/60000 [>.............................] - ETA: 1:50 - loss: 0.8484 - categorical_accuracy: 0.7184
 3360/60000 [>.............................] - ETA: 1:50 - loss: 0.8443 - categorical_accuracy: 0.7199
 3392/60000 [>.............................] - ETA: 1:50 - loss: 0.8446 - categorical_accuracy: 0.7199
 3424/60000 [>.............................] - ETA: 1:50 - loss: 0.8397 - categorical_accuracy: 0.7214
 3456/60000 [>.............................] - ETA: 1:50 - loss: 0.8390 - categorical_accuracy: 0.7219
 3488/60000 [>.............................] - ETA: 1:50 - loss: 0.8335 - categorical_accuracy: 0.7236
 3520/60000 [>.............................] - ETA: 1:50 - loss: 0.8290 - categorical_accuracy: 0.7253
 3552/60000 [>.............................] - ETA: 1:50 - loss: 0.8276 - categorical_accuracy: 0.7261
 3584/60000 [>.............................] - ETA: 1:50 - loss: 0.8223 - categorical_accuracy: 0.7277
 3616/60000 [>.............................] - ETA: 1:50 - loss: 0.8177 - categorical_accuracy: 0.7293
 3648/60000 [>.............................] - ETA: 1:49 - loss: 0.8150 - categorical_accuracy: 0.7300
 3680/60000 [>.............................] - ETA: 1:49 - loss: 0.8115 - categorical_accuracy: 0.7318
 3712/60000 [>.............................] - ETA: 1:49 - loss: 0.8081 - categorical_accuracy: 0.7328
 3744/60000 [>.............................] - ETA: 1:49 - loss: 0.8034 - categorical_accuracy: 0.7342
 3776/60000 [>.............................] - ETA: 1:49 - loss: 0.7979 - categorical_accuracy: 0.7362
 3808/60000 [>.............................] - ETA: 1:49 - loss: 0.7937 - categorical_accuracy: 0.7374
 3840/60000 [>.............................] - ETA: 1:49 - loss: 0.7908 - categorical_accuracy: 0.7383
 3872/60000 [>.............................] - ETA: 1:49 - loss: 0.7876 - categorical_accuracy: 0.7394
 3904/60000 [>.............................] - ETA: 1:49 - loss: 0.7820 - categorical_accuracy: 0.7413
 3936/60000 [>.............................] - ETA: 1:49 - loss: 0.7781 - categorical_accuracy: 0.7429
 3968/60000 [>.............................] - ETA: 1:49 - loss: 0.7748 - categorical_accuracy: 0.7434
 4000/60000 [=>............................] - ETA: 1:49 - loss: 0.7706 - categorical_accuracy: 0.7448
 4032/60000 [=>............................] - ETA: 1:48 - loss: 0.7656 - categorical_accuracy: 0.7463
 4064/60000 [=>............................] - ETA: 1:48 - loss: 0.7610 - categorical_accuracy: 0.7480
 4096/60000 [=>............................] - ETA: 1:48 - loss: 0.7591 - categorical_accuracy: 0.7488
 4128/60000 [=>............................] - ETA: 1:48 - loss: 0.7543 - categorical_accuracy: 0.7505
 4160/60000 [=>............................] - ETA: 1:48 - loss: 0.7510 - categorical_accuracy: 0.7517
 4192/60000 [=>............................] - ETA: 1:48 - loss: 0.7477 - categorical_accuracy: 0.7529
 4224/60000 [=>............................] - ETA: 1:48 - loss: 0.7446 - categorical_accuracy: 0.7538
 4256/60000 [=>............................] - ETA: 1:48 - loss: 0.7402 - categorical_accuracy: 0.7554
 4288/60000 [=>............................] - ETA: 1:48 - loss: 0.7375 - categorical_accuracy: 0.7561
 4320/60000 [=>............................] - ETA: 1:47 - loss: 0.7365 - categorical_accuracy: 0.7563
 4352/60000 [=>............................] - ETA: 1:47 - loss: 0.7339 - categorical_accuracy: 0.7569
 4384/60000 [=>............................] - ETA: 1:47 - loss: 0.7301 - categorical_accuracy: 0.7582
 4416/60000 [=>............................] - ETA: 1:47 - loss: 0.7270 - categorical_accuracy: 0.7591
 4448/60000 [=>............................] - ETA: 1:47 - loss: 0.7233 - categorical_accuracy: 0.7601
 4480/60000 [=>............................] - ETA: 1:47 - loss: 0.7209 - categorical_accuracy: 0.7609
 4512/60000 [=>............................] - ETA: 1:47 - loss: 0.7172 - categorical_accuracy: 0.7622
 4544/60000 [=>............................] - ETA: 1:47 - loss: 0.7139 - categorical_accuracy: 0.7634
 4576/60000 [=>............................] - ETA: 1:47 - loss: 0.7105 - categorical_accuracy: 0.7646
 4608/60000 [=>............................] - ETA: 1:47 - loss: 0.7083 - categorical_accuracy: 0.7656
 4640/60000 [=>............................] - ETA: 1:47 - loss: 0.7054 - categorical_accuracy: 0.7666
 4672/60000 [=>............................] - ETA: 1:47 - loss: 0.7022 - categorical_accuracy: 0.7678
 4704/60000 [=>............................] - ETA: 1:46 - loss: 0.6984 - categorical_accuracy: 0.7689
 4736/60000 [=>............................] - ETA: 1:47 - loss: 0.6953 - categorical_accuracy: 0.7701
 4768/60000 [=>............................] - ETA: 1:46 - loss: 0.6934 - categorical_accuracy: 0.7710
 4800/60000 [=>............................] - ETA: 1:47 - loss: 0.6900 - categorical_accuracy: 0.7721
 4832/60000 [=>............................] - ETA: 1:47 - loss: 0.6884 - categorical_accuracy: 0.7730
 4864/60000 [=>............................] - ETA: 1:46 - loss: 0.6916 - categorical_accuracy: 0.7722
 4896/60000 [=>............................] - ETA: 1:46 - loss: 0.6887 - categorical_accuracy: 0.7733
 4928/60000 [=>............................] - ETA: 1:46 - loss: 0.6856 - categorical_accuracy: 0.7741
 4960/60000 [=>............................] - ETA: 1:46 - loss: 0.6831 - categorical_accuracy: 0.7748
 4992/60000 [=>............................] - ETA: 1:46 - loss: 0.6802 - categorical_accuracy: 0.7754
 5024/60000 [=>............................] - ETA: 1:46 - loss: 0.6766 - categorical_accuracy: 0.7767
 5056/60000 [=>............................] - ETA: 1:46 - loss: 0.6763 - categorical_accuracy: 0.7775
 5088/60000 [=>............................] - ETA: 1:46 - loss: 0.6734 - categorical_accuracy: 0.7783
 5120/60000 [=>............................] - ETA: 1:46 - loss: 0.6728 - categorical_accuracy: 0.7789
 5152/60000 [=>............................] - ETA: 1:46 - loss: 0.6706 - categorical_accuracy: 0.7793
 5184/60000 [=>............................] - ETA: 1:46 - loss: 0.6687 - categorical_accuracy: 0.7799
 5216/60000 [=>............................] - ETA: 1:46 - loss: 0.6655 - categorical_accuracy: 0.7809
 5248/60000 [=>............................] - ETA: 1:46 - loss: 0.6629 - categorical_accuracy: 0.7816
 5280/60000 [=>............................] - ETA: 1:46 - loss: 0.6609 - categorical_accuracy: 0.7820
 5312/60000 [=>............................] - ETA: 1:45 - loss: 0.6602 - categorical_accuracy: 0.7820
 5344/60000 [=>............................] - ETA: 1:45 - loss: 0.6578 - categorical_accuracy: 0.7826
 5376/60000 [=>............................] - ETA: 1:45 - loss: 0.6550 - categorical_accuracy: 0.7833
 5408/60000 [=>............................] - ETA: 1:45 - loss: 0.6530 - categorical_accuracy: 0.7842
 5440/60000 [=>............................] - ETA: 1:45 - loss: 0.6515 - categorical_accuracy: 0.7847
 5472/60000 [=>............................] - ETA: 1:45 - loss: 0.6490 - categorical_accuracy: 0.7856
 5504/60000 [=>............................] - ETA: 1:45 - loss: 0.6468 - categorical_accuracy: 0.7862
 5536/60000 [=>............................] - ETA: 1:45 - loss: 0.6451 - categorical_accuracy: 0.7868
 5568/60000 [=>............................] - ETA: 1:45 - loss: 0.6435 - categorical_accuracy: 0.7874
 5600/60000 [=>............................] - ETA: 1:45 - loss: 0.6417 - categorical_accuracy: 0.7879
 5632/60000 [=>............................] - ETA: 1:45 - loss: 0.6405 - categorical_accuracy: 0.7880
 5664/60000 [=>............................] - ETA: 1:45 - loss: 0.6399 - categorical_accuracy: 0.7883
 5696/60000 [=>............................] - ETA: 1:45 - loss: 0.6384 - categorical_accuracy: 0.7890
 5728/60000 [=>............................] - ETA: 1:44 - loss: 0.6369 - categorical_accuracy: 0.7895
 5760/60000 [=>............................] - ETA: 1:44 - loss: 0.6347 - categorical_accuracy: 0.7901
 5792/60000 [=>............................] - ETA: 1:44 - loss: 0.6327 - categorical_accuracy: 0.7906
 5824/60000 [=>............................] - ETA: 1:44 - loss: 0.6298 - categorical_accuracy: 0.7916
 5856/60000 [=>............................] - ETA: 1:44 - loss: 0.6270 - categorical_accuracy: 0.7925
 5888/60000 [=>............................] - ETA: 1:44 - loss: 0.6251 - categorical_accuracy: 0.7931
 5920/60000 [=>............................] - ETA: 1:44 - loss: 0.6232 - categorical_accuracy: 0.7939
 5952/60000 [=>............................] - ETA: 1:44 - loss: 0.6204 - categorical_accuracy: 0.7949
 5984/60000 [=>............................] - ETA: 1:44 - loss: 0.6179 - categorical_accuracy: 0.7956
 6016/60000 [==>...........................] - ETA: 1:44 - loss: 0.6161 - categorical_accuracy: 0.7964
 6048/60000 [==>...........................] - ETA: 1:44 - loss: 0.6153 - categorical_accuracy: 0.7968
 6080/60000 [==>...........................] - ETA: 1:44 - loss: 0.6135 - categorical_accuracy: 0.7975
 6112/60000 [==>...........................] - ETA: 1:44 - loss: 0.6133 - categorical_accuracy: 0.7974
 6144/60000 [==>...........................] - ETA: 1:44 - loss: 0.6120 - categorical_accuracy: 0.7980
 6176/60000 [==>...........................] - ETA: 1:44 - loss: 0.6107 - categorical_accuracy: 0.7981
 6208/60000 [==>...........................] - ETA: 1:43 - loss: 0.6086 - categorical_accuracy: 0.7986
 6240/60000 [==>...........................] - ETA: 1:43 - loss: 0.6075 - categorical_accuracy: 0.7990
 6272/60000 [==>...........................] - ETA: 1:43 - loss: 0.6057 - categorical_accuracy: 0.7994
 6304/60000 [==>...........................] - ETA: 1:43 - loss: 0.6054 - categorical_accuracy: 0.7998
 6336/60000 [==>...........................] - ETA: 1:43 - loss: 0.6032 - categorical_accuracy: 0.8007
 6368/60000 [==>...........................] - ETA: 1:43 - loss: 0.6028 - categorical_accuracy: 0.8006
 6400/60000 [==>...........................] - ETA: 1:43 - loss: 0.6017 - categorical_accuracy: 0.8008
 6432/60000 [==>...........................] - ETA: 1:43 - loss: 0.6006 - categorical_accuracy: 0.8008
 6464/60000 [==>...........................] - ETA: 1:43 - loss: 0.5988 - categorical_accuracy: 0.8015
 6496/60000 [==>...........................] - ETA: 1:43 - loss: 0.5976 - categorical_accuracy: 0.8020
 6528/60000 [==>...........................] - ETA: 1:43 - loss: 0.5959 - categorical_accuracy: 0.8024
 6560/60000 [==>...........................] - ETA: 1:43 - loss: 0.5947 - categorical_accuracy: 0.8032
 6592/60000 [==>...........................] - ETA: 1:43 - loss: 0.5929 - categorical_accuracy: 0.8039
 6624/60000 [==>...........................] - ETA: 1:43 - loss: 0.5931 - categorical_accuracy: 0.8039
 6656/60000 [==>...........................] - ETA: 1:42 - loss: 0.5910 - categorical_accuracy: 0.8047
 6688/60000 [==>...........................] - ETA: 1:42 - loss: 0.5887 - categorical_accuracy: 0.8055
 6720/60000 [==>...........................] - ETA: 1:42 - loss: 0.5889 - categorical_accuracy: 0.8054
 6752/60000 [==>...........................] - ETA: 1:42 - loss: 0.5879 - categorical_accuracy: 0.8055
 6784/60000 [==>...........................] - ETA: 1:42 - loss: 0.5854 - categorical_accuracy: 0.8065
 6816/60000 [==>...........................] - ETA: 1:42 - loss: 0.5839 - categorical_accuracy: 0.8069
 6848/60000 [==>...........................] - ETA: 1:42 - loss: 0.5818 - categorical_accuracy: 0.8075
 6880/60000 [==>...........................] - ETA: 1:42 - loss: 0.5811 - categorical_accuracy: 0.8078
 6912/60000 [==>...........................] - ETA: 1:42 - loss: 0.5797 - categorical_accuracy: 0.8084
 6944/60000 [==>...........................] - ETA: 1:42 - loss: 0.5775 - categorical_accuracy: 0.8092
 6976/60000 [==>...........................] - ETA: 1:42 - loss: 0.5754 - categorical_accuracy: 0.8099
 7008/60000 [==>...........................] - ETA: 1:42 - loss: 0.5748 - categorical_accuracy: 0.8102
 7040/60000 [==>...........................] - ETA: 1:42 - loss: 0.5735 - categorical_accuracy: 0.8104
 7072/60000 [==>...........................] - ETA: 1:42 - loss: 0.5715 - categorical_accuracy: 0.8111
 7104/60000 [==>...........................] - ETA: 1:42 - loss: 0.5694 - categorical_accuracy: 0.8118
 7136/60000 [==>...........................] - ETA: 1:41 - loss: 0.5674 - categorical_accuracy: 0.8125
 7168/60000 [==>...........................] - ETA: 1:41 - loss: 0.5657 - categorical_accuracy: 0.8132
 7200/60000 [==>...........................] - ETA: 1:41 - loss: 0.5642 - categorical_accuracy: 0.8136
 7232/60000 [==>...........................] - ETA: 1:41 - loss: 0.5639 - categorical_accuracy: 0.8140
 7264/60000 [==>...........................] - ETA: 1:41 - loss: 0.5633 - categorical_accuracy: 0.8144
 7296/60000 [==>...........................] - ETA: 1:41 - loss: 0.5617 - categorical_accuracy: 0.8150
 7328/60000 [==>...........................] - ETA: 1:41 - loss: 0.5599 - categorical_accuracy: 0.8156
 7360/60000 [==>...........................] - ETA: 1:41 - loss: 0.5588 - categorical_accuracy: 0.8158
 7392/60000 [==>...........................] - ETA: 1:41 - loss: 0.5581 - categorical_accuracy: 0.8157
 7424/60000 [==>...........................] - ETA: 1:41 - loss: 0.5563 - categorical_accuracy: 0.8163
 7456/60000 [==>...........................] - ETA: 1:41 - loss: 0.5559 - categorical_accuracy: 0.8164
 7488/60000 [==>...........................] - ETA: 1:41 - loss: 0.5541 - categorical_accuracy: 0.8170
 7520/60000 [==>...........................] - ETA: 1:40 - loss: 0.5543 - categorical_accuracy: 0.8172
 7552/60000 [==>...........................] - ETA: 1:40 - loss: 0.5529 - categorical_accuracy: 0.8175
 7584/60000 [==>...........................] - ETA: 1:40 - loss: 0.5522 - categorical_accuracy: 0.8179
 7616/60000 [==>...........................] - ETA: 1:40 - loss: 0.5505 - categorical_accuracy: 0.8184
 7648/60000 [==>...........................] - ETA: 1:40 - loss: 0.5488 - categorical_accuracy: 0.8189
 7680/60000 [==>...........................] - ETA: 1:40 - loss: 0.5483 - categorical_accuracy: 0.8194
 7712/60000 [==>...........................] - ETA: 1:40 - loss: 0.5468 - categorical_accuracy: 0.8199
 7744/60000 [==>...........................] - ETA: 1:40 - loss: 0.5451 - categorical_accuracy: 0.8206
 7776/60000 [==>...........................] - ETA: 1:40 - loss: 0.5437 - categorical_accuracy: 0.8211
 7808/60000 [==>...........................] - ETA: 1:40 - loss: 0.5422 - categorical_accuracy: 0.8216
 7840/60000 [==>...........................] - ETA: 1:40 - loss: 0.5407 - categorical_accuracy: 0.8221
 7872/60000 [==>...........................] - ETA: 1:40 - loss: 0.5398 - categorical_accuracy: 0.8225
 7904/60000 [==>...........................] - ETA: 1:39 - loss: 0.5379 - categorical_accuracy: 0.8233
 7936/60000 [==>...........................] - ETA: 1:39 - loss: 0.5362 - categorical_accuracy: 0.8238
 7968/60000 [==>...........................] - ETA: 1:39 - loss: 0.5358 - categorical_accuracy: 0.8239
 8000/60000 [===>..........................] - ETA: 1:39 - loss: 0.5367 - categorical_accuracy: 0.8240
 8032/60000 [===>..........................] - ETA: 1:39 - loss: 0.5353 - categorical_accuracy: 0.8246
 8064/60000 [===>..........................] - ETA: 1:39 - loss: 0.5355 - categorical_accuracy: 0.8244
 8096/60000 [===>..........................] - ETA: 1:39 - loss: 0.5337 - categorical_accuracy: 0.8251
 8128/60000 [===>..........................] - ETA: 1:39 - loss: 0.5324 - categorical_accuracy: 0.8255
 8160/60000 [===>..........................] - ETA: 1:39 - loss: 0.5308 - categorical_accuracy: 0.8262
 8192/60000 [===>..........................] - ETA: 1:39 - loss: 0.5301 - categorical_accuracy: 0.8268
 8224/60000 [===>..........................] - ETA: 1:39 - loss: 0.5289 - categorical_accuracy: 0.8271
 8256/60000 [===>..........................] - ETA: 1:39 - loss: 0.5271 - categorical_accuracy: 0.8278
 8288/60000 [===>..........................] - ETA: 1:39 - loss: 0.5261 - categorical_accuracy: 0.8282
 8320/60000 [===>..........................] - ETA: 1:39 - loss: 0.5249 - categorical_accuracy: 0.8287
 8352/60000 [===>..........................] - ETA: 1:38 - loss: 0.5239 - categorical_accuracy: 0.8293
 8384/60000 [===>..........................] - ETA: 1:38 - loss: 0.5223 - categorical_accuracy: 0.8298
 8416/60000 [===>..........................] - ETA: 1:38 - loss: 0.5218 - categorical_accuracy: 0.8301
 8448/60000 [===>..........................] - ETA: 1:38 - loss: 0.5215 - categorical_accuracy: 0.8303
 8480/60000 [===>..........................] - ETA: 1:38 - loss: 0.5202 - categorical_accuracy: 0.8308
 8512/60000 [===>..........................] - ETA: 1:38 - loss: 0.5192 - categorical_accuracy: 0.8309
 8544/60000 [===>..........................] - ETA: 1:38 - loss: 0.5178 - categorical_accuracy: 0.8313
 8576/60000 [===>..........................] - ETA: 1:38 - loss: 0.5180 - categorical_accuracy: 0.8312
 8608/60000 [===>..........................] - ETA: 1:38 - loss: 0.5164 - categorical_accuracy: 0.8317
 8640/60000 [===>..........................] - ETA: 1:38 - loss: 0.5150 - categorical_accuracy: 0.8322
 8672/60000 [===>..........................] - ETA: 1:38 - loss: 0.5157 - categorical_accuracy: 0.8322
 8704/60000 [===>..........................] - ETA: 1:38 - loss: 0.5143 - categorical_accuracy: 0.8326
 8736/60000 [===>..........................] - ETA: 1:38 - loss: 0.5135 - categorical_accuracy: 0.8331
 8768/60000 [===>..........................] - ETA: 1:38 - loss: 0.5126 - categorical_accuracy: 0.8335
 8800/60000 [===>..........................] - ETA: 1:38 - loss: 0.5111 - categorical_accuracy: 0.8339
 8832/60000 [===>..........................] - ETA: 1:37 - loss: 0.5113 - categorical_accuracy: 0.8338
 8864/60000 [===>..........................] - ETA: 1:37 - loss: 0.5104 - categorical_accuracy: 0.8340
 8896/60000 [===>..........................] - ETA: 1:37 - loss: 0.5089 - categorical_accuracy: 0.8346
 8928/60000 [===>..........................] - ETA: 1:37 - loss: 0.5079 - categorical_accuracy: 0.8349
 8960/60000 [===>..........................] - ETA: 1:37 - loss: 0.5073 - categorical_accuracy: 0.8350
 8992/60000 [===>..........................] - ETA: 1:37 - loss: 0.5064 - categorical_accuracy: 0.8354
 9024/60000 [===>..........................] - ETA: 1:37 - loss: 0.5055 - categorical_accuracy: 0.8359
 9056/60000 [===>..........................] - ETA: 1:37 - loss: 0.5043 - categorical_accuracy: 0.8361
 9088/60000 [===>..........................] - ETA: 1:37 - loss: 0.5033 - categorical_accuracy: 0.8365
 9120/60000 [===>..........................] - ETA: 1:37 - loss: 0.5026 - categorical_accuracy: 0.8365
 9152/60000 [===>..........................] - ETA: 1:37 - loss: 0.5015 - categorical_accuracy: 0.8368
 9184/60000 [===>..........................] - ETA: 1:37 - loss: 0.5004 - categorical_accuracy: 0.8371
 9216/60000 [===>..........................] - ETA: 1:37 - loss: 0.4998 - categorical_accuracy: 0.8371
 9248/60000 [===>..........................] - ETA: 1:36 - loss: 0.4983 - categorical_accuracy: 0.8377
 9280/60000 [===>..........................] - ETA: 1:36 - loss: 0.4975 - categorical_accuracy: 0.8378
 9312/60000 [===>..........................] - ETA: 1:36 - loss: 0.4973 - categorical_accuracy: 0.8377
 9344/60000 [===>..........................] - ETA: 1:36 - loss: 0.4966 - categorical_accuracy: 0.8380
 9376/60000 [===>..........................] - ETA: 1:36 - loss: 0.4959 - categorical_accuracy: 0.8382
 9408/60000 [===>..........................] - ETA: 1:36 - loss: 0.4948 - categorical_accuracy: 0.8386
 9440/60000 [===>..........................] - ETA: 1:36 - loss: 0.4943 - categorical_accuracy: 0.8387
 9472/60000 [===>..........................] - ETA: 1:36 - loss: 0.4929 - categorical_accuracy: 0.8392
 9504/60000 [===>..........................] - ETA: 1:36 - loss: 0.4925 - categorical_accuracy: 0.8393
 9536/60000 [===>..........................] - ETA: 1:36 - loss: 0.4914 - categorical_accuracy: 0.8397
 9568/60000 [===>..........................] - ETA: 1:36 - loss: 0.4901 - categorical_accuracy: 0.8401
 9600/60000 [===>..........................] - ETA: 1:36 - loss: 0.4887 - categorical_accuracy: 0.8405
 9632/60000 [===>..........................] - ETA: 1:36 - loss: 0.4881 - categorical_accuracy: 0.8407
 9664/60000 [===>..........................] - ETA: 1:36 - loss: 0.4871 - categorical_accuracy: 0.8412
 9696/60000 [===>..........................] - ETA: 1:36 - loss: 0.4859 - categorical_accuracy: 0.8415
 9728/60000 [===>..........................] - ETA: 1:36 - loss: 0.4849 - categorical_accuracy: 0.8418
 9760/60000 [===>..........................] - ETA: 1:36 - loss: 0.4840 - categorical_accuracy: 0.8420
 9792/60000 [===>..........................] - ETA: 1:35 - loss: 0.4826 - categorical_accuracy: 0.8425
 9824/60000 [===>..........................] - ETA: 1:35 - loss: 0.4821 - categorical_accuracy: 0.8428
 9856/60000 [===>..........................] - ETA: 1:35 - loss: 0.4812 - categorical_accuracy: 0.8431
 9888/60000 [===>..........................] - ETA: 1:35 - loss: 0.4801 - categorical_accuracy: 0.8435
 9920/60000 [===>..........................] - ETA: 1:35 - loss: 0.4814 - categorical_accuracy: 0.8435
 9952/60000 [===>..........................] - ETA: 1:35 - loss: 0.4811 - categorical_accuracy: 0.8435
 9984/60000 [===>..........................] - ETA: 1:35 - loss: 0.4804 - categorical_accuracy: 0.8438
10016/60000 [====>.........................] - ETA: 1:35 - loss: 0.4798 - categorical_accuracy: 0.8438
10048/60000 [====>.........................] - ETA: 1:35 - loss: 0.4795 - categorical_accuracy: 0.8438
10080/60000 [====>.........................] - ETA: 1:35 - loss: 0.4787 - categorical_accuracy: 0.8439
10112/60000 [====>.........................] - ETA: 1:35 - loss: 0.4786 - categorical_accuracy: 0.8442
10144/60000 [====>.........................] - ETA: 1:35 - loss: 0.4775 - categorical_accuracy: 0.8447
10176/60000 [====>.........................] - ETA: 1:35 - loss: 0.4769 - categorical_accuracy: 0.8450
10208/60000 [====>.........................] - ETA: 1:35 - loss: 0.4765 - categorical_accuracy: 0.8451
10240/60000 [====>.........................] - ETA: 1:35 - loss: 0.4754 - categorical_accuracy: 0.8455
10272/60000 [====>.........................] - ETA: 1:35 - loss: 0.4744 - categorical_accuracy: 0.8458
10304/60000 [====>.........................] - ETA: 1:34 - loss: 0.4738 - categorical_accuracy: 0.8461
10336/60000 [====>.........................] - ETA: 1:34 - loss: 0.4730 - categorical_accuracy: 0.8463
10368/60000 [====>.........................] - ETA: 1:34 - loss: 0.4718 - categorical_accuracy: 0.8467
10400/60000 [====>.........................] - ETA: 1:34 - loss: 0.4713 - categorical_accuracy: 0.8469
10432/60000 [====>.........................] - ETA: 1:34 - loss: 0.4701 - categorical_accuracy: 0.8473
10464/60000 [====>.........................] - ETA: 1:34 - loss: 0.4690 - categorical_accuracy: 0.8477
10496/60000 [====>.........................] - ETA: 1:34 - loss: 0.4690 - categorical_accuracy: 0.8478
10528/60000 [====>.........................] - ETA: 1:34 - loss: 0.4685 - categorical_accuracy: 0.8480
10560/60000 [====>.........................] - ETA: 1:34 - loss: 0.4675 - categorical_accuracy: 0.8484
10592/60000 [====>.........................] - ETA: 1:34 - loss: 0.4663 - categorical_accuracy: 0.8488
10624/60000 [====>.........................] - ETA: 1:34 - loss: 0.4653 - categorical_accuracy: 0.8492
10656/60000 [====>.........................] - ETA: 1:34 - loss: 0.4644 - categorical_accuracy: 0.8496
10688/60000 [====>.........................] - ETA: 1:34 - loss: 0.4632 - categorical_accuracy: 0.8500
10720/60000 [====>.........................] - ETA: 1:34 - loss: 0.4629 - categorical_accuracy: 0.8504
10752/60000 [====>.........................] - ETA: 1:34 - loss: 0.4616 - categorical_accuracy: 0.8508
10784/60000 [====>.........................] - ETA: 1:33 - loss: 0.4606 - categorical_accuracy: 0.8511
10816/60000 [====>.........................] - ETA: 1:33 - loss: 0.4602 - categorical_accuracy: 0.8511
10848/60000 [====>.........................] - ETA: 1:33 - loss: 0.4591 - categorical_accuracy: 0.8515
10880/60000 [====>.........................] - ETA: 1:33 - loss: 0.4586 - categorical_accuracy: 0.8516
10912/60000 [====>.........................] - ETA: 1:33 - loss: 0.4578 - categorical_accuracy: 0.8519
10944/60000 [====>.........................] - ETA: 1:33 - loss: 0.4566 - categorical_accuracy: 0.8523
10976/60000 [====>.........................] - ETA: 1:33 - loss: 0.4555 - categorical_accuracy: 0.8526
11008/60000 [====>.........................] - ETA: 1:33 - loss: 0.4545 - categorical_accuracy: 0.8530
11040/60000 [====>.........................] - ETA: 1:33 - loss: 0.4536 - categorical_accuracy: 0.8533
11072/60000 [====>.........................] - ETA: 1:33 - loss: 0.4524 - categorical_accuracy: 0.8537
11104/60000 [====>.........................] - ETA: 1:33 - loss: 0.4516 - categorical_accuracy: 0.8539
11136/60000 [====>.........................] - ETA: 1:33 - loss: 0.4514 - categorical_accuracy: 0.8540
11168/60000 [====>.........................] - ETA: 1:33 - loss: 0.4513 - categorical_accuracy: 0.8540
11200/60000 [====>.........................] - ETA: 1:33 - loss: 0.4505 - categorical_accuracy: 0.8544
11232/60000 [====>.........................] - ETA: 1:33 - loss: 0.4496 - categorical_accuracy: 0.8546
11264/60000 [====>.........................] - ETA: 1:32 - loss: 0.4490 - categorical_accuracy: 0.8548
11296/60000 [====>.........................] - ETA: 1:32 - loss: 0.4481 - categorical_accuracy: 0.8551
11328/60000 [====>.........................] - ETA: 1:32 - loss: 0.4481 - categorical_accuracy: 0.8553
11360/60000 [====>.........................] - ETA: 1:32 - loss: 0.4472 - categorical_accuracy: 0.8556
11392/60000 [====>.........................] - ETA: 1:32 - loss: 0.4463 - categorical_accuracy: 0.8559
11424/60000 [====>.........................] - ETA: 1:32 - loss: 0.4459 - categorical_accuracy: 0.8561
11456/60000 [====>.........................] - ETA: 1:32 - loss: 0.4450 - categorical_accuracy: 0.8563
11488/60000 [====>.........................] - ETA: 1:32 - loss: 0.4440 - categorical_accuracy: 0.8566
11520/60000 [====>.........................] - ETA: 1:32 - loss: 0.4438 - categorical_accuracy: 0.8567
11552/60000 [====>.........................] - ETA: 1:32 - loss: 0.4428 - categorical_accuracy: 0.8570
11584/60000 [====>.........................] - ETA: 1:32 - loss: 0.4422 - categorical_accuracy: 0.8571
11616/60000 [====>.........................] - ETA: 1:32 - loss: 0.4414 - categorical_accuracy: 0.8574
11648/60000 [====>.........................] - ETA: 1:32 - loss: 0.4409 - categorical_accuracy: 0.8577
11680/60000 [====>.........................] - ETA: 1:32 - loss: 0.4406 - categorical_accuracy: 0.8578
11712/60000 [====>.........................] - ETA: 1:32 - loss: 0.4404 - categorical_accuracy: 0.8581
11744/60000 [====>.........................] - ETA: 1:31 - loss: 0.4400 - categorical_accuracy: 0.8583
11776/60000 [====>.........................] - ETA: 1:31 - loss: 0.4394 - categorical_accuracy: 0.8584
11808/60000 [====>.........................] - ETA: 1:31 - loss: 0.4386 - categorical_accuracy: 0.8587
11840/60000 [====>.........................] - ETA: 1:31 - loss: 0.4380 - categorical_accuracy: 0.8590
11872/60000 [====>.........................] - ETA: 1:31 - loss: 0.4376 - categorical_accuracy: 0.8592
11904/60000 [====>.........................] - ETA: 1:31 - loss: 0.4373 - categorical_accuracy: 0.8594
11936/60000 [====>.........................] - ETA: 1:31 - loss: 0.4369 - categorical_accuracy: 0.8596
11968/60000 [====>.........................] - ETA: 1:31 - loss: 0.4362 - categorical_accuracy: 0.8597
12000/60000 [=====>........................] - ETA: 1:31 - loss: 0.4354 - categorical_accuracy: 0.8599
12032/60000 [=====>........................] - ETA: 1:31 - loss: 0.4357 - categorical_accuracy: 0.8600
12064/60000 [=====>........................] - ETA: 1:31 - loss: 0.4350 - categorical_accuracy: 0.8602
12096/60000 [=====>........................] - ETA: 1:31 - loss: 0.4344 - categorical_accuracy: 0.8604
12128/60000 [=====>........................] - ETA: 1:31 - loss: 0.4341 - categorical_accuracy: 0.8605
12160/60000 [=====>........................] - ETA: 1:31 - loss: 0.4342 - categorical_accuracy: 0.8606
12192/60000 [=====>........................] - ETA: 1:31 - loss: 0.4337 - categorical_accuracy: 0.8607
12224/60000 [=====>........................] - ETA: 1:30 - loss: 0.4329 - categorical_accuracy: 0.8611
12256/60000 [=====>........................] - ETA: 1:30 - loss: 0.4322 - categorical_accuracy: 0.8614
12288/60000 [=====>........................] - ETA: 1:30 - loss: 0.4314 - categorical_accuracy: 0.8617
12320/60000 [=====>........................] - ETA: 1:30 - loss: 0.4305 - categorical_accuracy: 0.8620
12352/60000 [=====>........................] - ETA: 1:30 - loss: 0.4297 - categorical_accuracy: 0.8622
12384/60000 [=====>........................] - ETA: 1:30 - loss: 0.4293 - categorical_accuracy: 0.8625
12416/60000 [=====>........................] - ETA: 1:30 - loss: 0.4283 - categorical_accuracy: 0.8628
12448/60000 [=====>........................] - ETA: 1:30 - loss: 0.4278 - categorical_accuracy: 0.8629
12480/60000 [=====>........................] - ETA: 1:30 - loss: 0.4269 - categorical_accuracy: 0.8631
12512/60000 [=====>........................] - ETA: 1:30 - loss: 0.4261 - categorical_accuracy: 0.8633
12544/60000 [=====>........................] - ETA: 1:30 - loss: 0.4252 - categorical_accuracy: 0.8636
12576/60000 [=====>........................] - ETA: 1:30 - loss: 0.4246 - categorical_accuracy: 0.8639
12608/60000 [=====>........................] - ETA: 1:30 - loss: 0.4241 - categorical_accuracy: 0.8640
12640/60000 [=====>........................] - ETA: 1:30 - loss: 0.4234 - categorical_accuracy: 0.8642
12672/60000 [=====>........................] - ETA: 1:30 - loss: 0.4227 - categorical_accuracy: 0.8645
12704/60000 [=====>........................] - ETA: 1:30 - loss: 0.4220 - categorical_accuracy: 0.8648
12736/60000 [=====>........................] - ETA: 1:29 - loss: 0.4213 - categorical_accuracy: 0.8649
12768/60000 [=====>........................] - ETA: 1:29 - loss: 0.4205 - categorical_accuracy: 0.8652
12800/60000 [=====>........................] - ETA: 1:29 - loss: 0.4198 - categorical_accuracy: 0.8653
12832/60000 [=====>........................] - ETA: 1:29 - loss: 0.4191 - categorical_accuracy: 0.8656
12864/60000 [=====>........................] - ETA: 1:29 - loss: 0.4184 - categorical_accuracy: 0.8658
12896/60000 [=====>........................] - ETA: 1:29 - loss: 0.4184 - categorical_accuracy: 0.8658
12928/60000 [=====>........................] - ETA: 1:29 - loss: 0.4177 - categorical_accuracy: 0.8661
12960/60000 [=====>........................] - ETA: 1:29 - loss: 0.4169 - categorical_accuracy: 0.8664
12992/60000 [=====>........................] - ETA: 1:29 - loss: 0.4164 - categorical_accuracy: 0.8667
13024/60000 [=====>........................] - ETA: 1:29 - loss: 0.4157 - categorical_accuracy: 0.8669
13056/60000 [=====>........................] - ETA: 1:29 - loss: 0.4149 - categorical_accuracy: 0.8672
13088/60000 [=====>........................] - ETA: 1:29 - loss: 0.4142 - categorical_accuracy: 0.8674
13120/60000 [=====>........................] - ETA: 1:29 - loss: 0.4142 - categorical_accuracy: 0.8675
13152/60000 [=====>........................] - ETA: 1:29 - loss: 0.4133 - categorical_accuracy: 0.8677
13184/60000 [=====>........................] - ETA: 1:29 - loss: 0.4132 - categorical_accuracy: 0.8679
13216/60000 [=====>........................] - ETA: 1:29 - loss: 0.4126 - categorical_accuracy: 0.8681
13248/60000 [=====>........................] - ETA: 1:28 - loss: 0.4121 - categorical_accuracy: 0.8682
13280/60000 [=====>........................] - ETA: 1:28 - loss: 0.4114 - categorical_accuracy: 0.8684
13312/60000 [=====>........................] - ETA: 1:28 - loss: 0.4108 - categorical_accuracy: 0.8686
13344/60000 [=====>........................] - ETA: 1:28 - loss: 0.4100 - categorical_accuracy: 0.8689
13376/60000 [=====>........................] - ETA: 1:28 - loss: 0.4093 - categorical_accuracy: 0.8691
13408/60000 [=====>........................] - ETA: 1:28 - loss: 0.4086 - categorical_accuracy: 0.8694
13440/60000 [=====>........................] - ETA: 1:28 - loss: 0.4079 - categorical_accuracy: 0.8696
13472/60000 [=====>........................] - ETA: 1:28 - loss: 0.4081 - categorical_accuracy: 0.8697
13504/60000 [=====>........................] - ETA: 1:28 - loss: 0.4076 - categorical_accuracy: 0.8698
13536/60000 [=====>........................] - ETA: 1:28 - loss: 0.4069 - categorical_accuracy: 0.8701
13568/60000 [=====>........................] - ETA: 1:28 - loss: 0.4061 - categorical_accuracy: 0.8703
13600/60000 [=====>........................] - ETA: 1:28 - loss: 0.4052 - categorical_accuracy: 0.8706
13632/60000 [=====>........................] - ETA: 1:28 - loss: 0.4046 - categorical_accuracy: 0.8708
13664/60000 [=====>........................] - ETA: 1:28 - loss: 0.4037 - categorical_accuracy: 0.8710
13696/60000 [=====>........................] - ETA: 1:28 - loss: 0.4032 - categorical_accuracy: 0.8711
13728/60000 [=====>........................] - ETA: 1:27 - loss: 0.4026 - categorical_accuracy: 0.8712
13760/60000 [=====>........................] - ETA: 1:27 - loss: 0.4017 - categorical_accuracy: 0.8714
13792/60000 [=====>........................] - ETA: 1:27 - loss: 0.4010 - categorical_accuracy: 0.8717
13824/60000 [=====>........................] - ETA: 1:27 - loss: 0.4008 - categorical_accuracy: 0.8717
13856/60000 [=====>........................] - ETA: 1:27 - loss: 0.4008 - categorical_accuracy: 0.8718
13888/60000 [=====>........................] - ETA: 1:27 - loss: 0.4008 - categorical_accuracy: 0.8719
13920/60000 [=====>........................] - ETA: 1:27 - loss: 0.4005 - categorical_accuracy: 0.8718
13952/60000 [=====>........................] - ETA: 1:27 - loss: 0.3999 - categorical_accuracy: 0.8719
13984/60000 [=====>........................] - ETA: 1:27 - loss: 0.3995 - categorical_accuracy: 0.8721
14016/60000 [======>.......................] - ETA: 1:27 - loss: 0.3989 - categorical_accuracy: 0.8722
14048/60000 [======>.......................] - ETA: 1:27 - loss: 0.3981 - categorical_accuracy: 0.8725
14080/60000 [======>.......................] - ETA: 1:27 - loss: 0.3974 - categorical_accuracy: 0.8728
14112/60000 [======>.......................] - ETA: 1:27 - loss: 0.3973 - categorical_accuracy: 0.8728
14144/60000 [======>.......................] - ETA: 1:27 - loss: 0.3967 - categorical_accuracy: 0.8730
14176/60000 [======>.......................] - ETA: 1:27 - loss: 0.3960 - categorical_accuracy: 0.8732
14208/60000 [======>.......................] - ETA: 1:27 - loss: 0.3956 - categorical_accuracy: 0.8735
14240/60000 [======>.......................] - ETA: 1:26 - loss: 0.3960 - categorical_accuracy: 0.8733
14272/60000 [======>.......................] - ETA: 1:26 - loss: 0.3960 - categorical_accuracy: 0.8734
14304/60000 [======>.......................] - ETA: 1:26 - loss: 0.3953 - categorical_accuracy: 0.8736
14336/60000 [======>.......................] - ETA: 1:26 - loss: 0.3945 - categorical_accuracy: 0.8739
14368/60000 [======>.......................] - ETA: 1:26 - loss: 0.3937 - categorical_accuracy: 0.8742
14400/60000 [======>.......................] - ETA: 1:26 - loss: 0.3933 - categorical_accuracy: 0.8742
14432/60000 [======>.......................] - ETA: 1:26 - loss: 0.3926 - categorical_accuracy: 0.8745
14464/60000 [======>.......................] - ETA: 1:26 - loss: 0.3919 - categorical_accuracy: 0.8747
14496/60000 [======>.......................] - ETA: 1:26 - loss: 0.3913 - categorical_accuracy: 0.8749
14528/60000 [======>.......................] - ETA: 1:26 - loss: 0.3910 - categorical_accuracy: 0.8751
14560/60000 [======>.......................] - ETA: 1:26 - loss: 0.3902 - categorical_accuracy: 0.8753
14592/60000 [======>.......................] - ETA: 1:26 - loss: 0.3898 - categorical_accuracy: 0.8755
14624/60000 [======>.......................] - ETA: 1:26 - loss: 0.3895 - categorical_accuracy: 0.8756
14656/60000 [======>.......................] - ETA: 1:26 - loss: 0.3892 - categorical_accuracy: 0.8758
14688/60000 [======>.......................] - ETA: 1:26 - loss: 0.3887 - categorical_accuracy: 0.8760
14720/60000 [======>.......................] - ETA: 1:26 - loss: 0.3883 - categorical_accuracy: 0.8761
14752/60000 [======>.......................] - ETA: 1:25 - loss: 0.3876 - categorical_accuracy: 0.8764
14784/60000 [======>.......................] - ETA: 1:25 - loss: 0.3873 - categorical_accuracy: 0.8764
14816/60000 [======>.......................] - ETA: 1:25 - loss: 0.3866 - categorical_accuracy: 0.8766
14848/60000 [======>.......................] - ETA: 1:25 - loss: 0.3860 - categorical_accuracy: 0.8768
14880/60000 [======>.......................] - ETA: 1:25 - loss: 0.3855 - categorical_accuracy: 0.8769
14912/60000 [======>.......................] - ETA: 1:25 - loss: 0.3861 - categorical_accuracy: 0.8769
14944/60000 [======>.......................] - ETA: 1:25 - loss: 0.3859 - categorical_accuracy: 0.8769
14976/60000 [======>.......................] - ETA: 1:25 - loss: 0.3855 - categorical_accuracy: 0.8770
15008/60000 [======>.......................] - ETA: 1:25 - loss: 0.3850 - categorical_accuracy: 0.8773
15040/60000 [======>.......................] - ETA: 1:25 - loss: 0.3844 - categorical_accuracy: 0.8773
15072/60000 [======>.......................] - ETA: 1:25 - loss: 0.3839 - categorical_accuracy: 0.8775
15104/60000 [======>.......................] - ETA: 1:25 - loss: 0.3836 - categorical_accuracy: 0.8775
15136/60000 [======>.......................] - ETA: 1:25 - loss: 0.3831 - categorical_accuracy: 0.8776
15168/60000 [======>.......................] - ETA: 1:25 - loss: 0.3828 - categorical_accuracy: 0.8777
15200/60000 [======>.......................] - ETA: 1:25 - loss: 0.3823 - categorical_accuracy: 0.8779
15232/60000 [======>.......................] - ETA: 1:25 - loss: 0.3822 - categorical_accuracy: 0.8778
15264/60000 [======>.......................] - ETA: 1:24 - loss: 0.3818 - categorical_accuracy: 0.8779
15296/60000 [======>.......................] - ETA: 1:24 - loss: 0.3814 - categorical_accuracy: 0.8781
15328/60000 [======>.......................] - ETA: 1:24 - loss: 0.3807 - categorical_accuracy: 0.8783
15360/60000 [======>.......................] - ETA: 1:24 - loss: 0.3802 - categorical_accuracy: 0.8784
15392/60000 [======>.......................] - ETA: 1:24 - loss: 0.3796 - categorical_accuracy: 0.8786
15424/60000 [======>.......................] - ETA: 1:24 - loss: 0.3789 - categorical_accuracy: 0.8788
15456/60000 [======>.......................] - ETA: 1:24 - loss: 0.3784 - categorical_accuracy: 0.8789
15488/60000 [======>.......................] - ETA: 1:24 - loss: 0.3778 - categorical_accuracy: 0.8791
15520/60000 [======>.......................] - ETA: 1:24 - loss: 0.3774 - categorical_accuracy: 0.8792
15552/60000 [======>.......................] - ETA: 1:24 - loss: 0.3769 - categorical_accuracy: 0.8794
15584/60000 [======>.......................] - ETA: 1:24 - loss: 0.3761 - categorical_accuracy: 0.8796
15616/60000 [======>.......................] - ETA: 1:24 - loss: 0.3757 - categorical_accuracy: 0.8797
15648/60000 [======>.......................] - ETA: 1:24 - loss: 0.3750 - categorical_accuracy: 0.8800
15680/60000 [======>.......................] - ETA: 1:24 - loss: 0.3747 - categorical_accuracy: 0.8801
15712/60000 [======>.......................] - ETA: 1:24 - loss: 0.3740 - categorical_accuracy: 0.8803
15744/60000 [======>.......................] - ETA: 1:24 - loss: 0.3735 - categorical_accuracy: 0.8805
15776/60000 [======>.......................] - ETA: 1:24 - loss: 0.3734 - categorical_accuracy: 0.8806
15808/60000 [======>.......................] - ETA: 1:24 - loss: 0.3730 - categorical_accuracy: 0.8808
15840/60000 [======>.......................] - ETA: 1:24 - loss: 0.3723 - categorical_accuracy: 0.8810
15872/60000 [======>.......................] - ETA: 1:23 - loss: 0.3720 - categorical_accuracy: 0.8810
15904/60000 [======>.......................] - ETA: 1:23 - loss: 0.3716 - categorical_accuracy: 0.8812
15936/60000 [======>.......................] - ETA: 1:23 - loss: 0.3709 - categorical_accuracy: 0.8814
15968/60000 [======>.......................] - ETA: 1:23 - loss: 0.3703 - categorical_accuracy: 0.8816
16000/60000 [=======>......................] - ETA: 1:23 - loss: 0.3700 - categorical_accuracy: 0.8818
16032/60000 [=======>......................] - ETA: 1:23 - loss: 0.3696 - categorical_accuracy: 0.8819
16064/60000 [=======>......................] - ETA: 1:23 - loss: 0.3690 - categorical_accuracy: 0.8822
16096/60000 [=======>......................] - ETA: 1:23 - loss: 0.3683 - categorical_accuracy: 0.8824
16128/60000 [=======>......................] - ETA: 1:23 - loss: 0.3679 - categorical_accuracy: 0.8824
16160/60000 [=======>......................] - ETA: 1:23 - loss: 0.3680 - categorical_accuracy: 0.8824
16192/60000 [=======>......................] - ETA: 1:23 - loss: 0.3679 - categorical_accuracy: 0.8823
16224/60000 [=======>......................] - ETA: 1:23 - loss: 0.3674 - categorical_accuracy: 0.8825
16256/60000 [=======>......................] - ETA: 1:23 - loss: 0.3669 - categorical_accuracy: 0.8826
16288/60000 [=======>......................] - ETA: 1:23 - loss: 0.3667 - categorical_accuracy: 0.8826
16320/60000 [=======>......................] - ETA: 1:23 - loss: 0.3668 - categorical_accuracy: 0.8827
16352/60000 [=======>......................] - ETA: 1:23 - loss: 0.3664 - categorical_accuracy: 0.8828
16384/60000 [=======>......................] - ETA: 1:22 - loss: 0.3661 - categorical_accuracy: 0.8829
16416/60000 [=======>......................] - ETA: 1:22 - loss: 0.3654 - categorical_accuracy: 0.8832
16448/60000 [=======>......................] - ETA: 1:22 - loss: 0.3648 - categorical_accuracy: 0.8834
16480/60000 [=======>......................] - ETA: 1:22 - loss: 0.3645 - categorical_accuracy: 0.8836
16512/60000 [=======>......................] - ETA: 1:22 - loss: 0.3642 - categorical_accuracy: 0.8837
16544/60000 [=======>......................] - ETA: 1:22 - loss: 0.3638 - categorical_accuracy: 0.8838
16576/60000 [=======>......................] - ETA: 1:22 - loss: 0.3636 - categorical_accuracy: 0.8839
16608/60000 [=======>......................] - ETA: 1:22 - loss: 0.3636 - categorical_accuracy: 0.8840
16640/60000 [=======>......................] - ETA: 1:22 - loss: 0.3631 - categorical_accuracy: 0.8841
16672/60000 [=======>......................] - ETA: 1:22 - loss: 0.3630 - categorical_accuracy: 0.8842
16704/60000 [=======>......................] - ETA: 1:22 - loss: 0.3625 - categorical_accuracy: 0.8844
16736/60000 [=======>......................] - ETA: 1:22 - loss: 0.3620 - categorical_accuracy: 0.8846
16768/60000 [=======>......................] - ETA: 1:22 - loss: 0.3616 - categorical_accuracy: 0.8847
16800/60000 [=======>......................] - ETA: 1:22 - loss: 0.3611 - categorical_accuracy: 0.8848
16832/60000 [=======>......................] - ETA: 1:22 - loss: 0.3605 - categorical_accuracy: 0.8850
16864/60000 [=======>......................] - ETA: 1:22 - loss: 0.3604 - categorical_accuracy: 0.8850
16896/60000 [=======>......................] - ETA: 1:21 - loss: 0.3599 - categorical_accuracy: 0.8852
16928/60000 [=======>......................] - ETA: 1:21 - loss: 0.3595 - categorical_accuracy: 0.8853
16960/60000 [=======>......................] - ETA: 1:21 - loss: 0.3592 - categorical_accuracy: 0.8854
16992/60000 [=======>......................] - ETA: 1:21 - loss: 0.3590 - categorical_accuracy: 0.8855
17024/60000 [=======>......................] - ETA: 1:21 - loss: 0.3587 - categorical_accuracy: 0.8856
17056/60000 [=======>......................] - ETA: 1:21 - loss: 0.3581 - categorical_accuracy: 0.8858
17088/60000 [=======>......................] - ETA: 1:21 - loss: 0.3576 - categorical_accuracy: 0.8860
17120/60000 [=======>......................] - ETA: 1:21 - loss: 0.3572 - categorical_accuracy: 0.8861
17152/60000 [=======>......................] - ETA: 1:21 - loss: 0.3572 - categorical_accuracy: 0.8861
17184/60000 [=======>......................] - ETA: 1:21 - loss: 0.3566 - categorical_accuracy: 0.8863
17216/60000 [=======>......................] - ETA: 1:21 - loss: 0.3562 - categorical_accuracy: 0.8864
17248/60000 [=======>......................] - ETA: 1:21 - loss: 0.3557 - categorical_accuracy: 0.8866
17280/60000 [=======>......................] - ETA: 1:21 - loss: 0.3550 - categorical_accuracy: 0.8868
17312/60000 [=======>......................] - ETA: 1:21 - loss: 0.3549 - categorical_accuracy: 0.8869
17344/60000 [=======>......................] - ETA: 1:21 - loss: 0.3544 - categorical_accuracy: 0.8871
17376/60000 [=======>......................] - ETA: 1:21 - loss: 0.3539 - categorical_accuracy: 0.8872
17408/60000 [=======>......................] - ETA: 1:20 - loss: 0.3533 - categorical_accuracy: 0.8874
17440/60000 [=======>......................] - ETA: 1:20 - loss: 0.3533 - categorical_accuracy: 0.8873
17472/60000 [=======>......................] - ETA: 1:20 - loss: 0.3528 - categorical_accuracy: 0.8875
17504/60000 [=======>......................] - ETA: 1:20 - loss: 0.3524 - categorical_accuracy: 0.8876
17536/60000 [=======>......................] - ETA: 1:20 - loss: 0.3521 - categorical_accuracy: 0.8877
17568/60000 [=======>......................] - ETA: 1:20 - loss: 0.3518 - categorical_accuracy: 0.8877
17600/60000 [=======>......................] - ETA: 1:20 - loss: 0.3518 - categorical_accuracy: 0.8877
17632/60000 [=======>......................] - ETA: 1:20 - loss: 0.3516 - categorical_accuracy: 0.8877
17664/60000 [=======>......................] - ETA: 1:20 - loss: 0.3512 - categorical_accuracy: 0.8879
17696/60000 [=======>......................] - ETA: 1:20 - loss: 0.3506 - categorical_accuracy: 0.8881
17728/60000 [=======>......................] - ETA: 1:20 - loss: 0.3501 - categorical_accuracy: 0.8883
17760/60000 [=======>......................] - ETA: 1:20 - loss: 0.3497 - categorical_accuracy: 0.8883
17792/60000 [=======>......................] - ETA: 1:20 - loss: 0.3495 - categorical_accuracy: 0.8883
17824/60000 [=======>......................] - ETA: 1:20 - loss: 0.3493 - categorical_accuracy: 0.8884
17856/60000 [=======>......................] - ETA: 1:20 - loss: 0.3490 - categorical_accuracy: 0.8885
17888/60000 [=======>......................] - ETA: 1:20 - loss: 0.3488 - categorical_accuracy: 0.8885
17920/60000 [=======>......................] - ETA: 1:19 - loss: 0.3486 - categorical_accuracy: 0.8886
17952/60000 [=======>......................] - ETA: 1:19 - loss: 0.3483 - categorical_accuracy: 0.8887
17984/60000 [=======>......................] - ETA: 1:19 - loss: 0.3478 - categorical_accuracy: 0.8889
18016/60000 [========>.....................] - ETA: 1:19 - loss: 0.3478 - categorical_accuracy: 0.8889
18048/60000 [========>.....................] - ETA: 1:19 - loss: 0.3474 - categorical_accuracy: 0.8891
18080/60000 [========>.....................] - ETA: 1:19 - loss: 0.3469 - categorical_accuracy: 0.8893
18112/60000 [========>.....................] - ETA: 1:19 - loss: 0.3463 - categorical_accuracy: 0.8895
18144/60000 [========>.....................] - ETA: 1:19 - loss: 0.3459 - categorical_accuracy: 0.8896
18176/60000 [========>.....................] - ETA: 1:19 - loss: 0.3455 - categorical_accuracy: 0.8897
18208/60000 [========>.....................] - ETA: 1:19 - loss: 0.3449 - categorical_accuracy: 0.8899
18240/60000 [========>.....................] - ETA: 1:19 - loss: 0.3448 - categorical_accuracy: 0.8900
18272/60000 [========>.....................] - ETA: 1:19 - loss: 0.3443 - categorical_accuracy: 0.8902
18304/60000 [========>.....................] - ETA: 1:19 - loss: 0.3441 - categorical_accuracy: 0.8902
18336/60000 [========>.....................] - ETA: 1:19 - loss: 0.3439 - categorical_accuracy: 0.8903
18368/60000 [========>.....................] - ETA: 1:19 - loss: 0.3435 - categorical_accuracy: 0.8904
18400/60000 [========>.....................] - ETA: 1:19 - loss: 0.3430 - categorical_accuracy: 0.8905
18432/60000 [========>.....................] - ETA: 1:18 - loss: 0.3426 - categorical_accuracy: 0.8907
18464/60000 [========>.....................] - ETA: 1:18 - loss: 0.3421 - categorical_accuracy: 0.8908
18496/60000 [========>.....................] - ETA: 1:18 - loss: 0.3418 - categorical_accuracy: 0.8908
18528/60000 [========>.....................] - ETA: 1:18 - loss: 0.3414 - categorical_accuracy: 0.8910
18560/60000 [========>.....................] - ETA: 1:18 - loss: 0.3409 - categorical_accuracy: 0.8912
18592/60000 [========>.....................] - ETA: 1:18 - loss: 0.3404 - categorical_accuracy: 0.8913
18624/60000 [========>.....................] - ETA: 1:18 - loss: 0.3401 - categorical_accuracy: 0.8913
18656/60000 [========>.....................] - ETA: 1:18 - loss: 0.3398 - categorical_accuracy: 0.8914
18688/60000 [========>.....................] - ETA: 1:18 - loss: 0.3396 - categorical_accuracy: 0.8915
18720/60000 [========>.....................] - ETA: 1:18 - loss: 0.3392 - categorical_accuracy: 0.8916
18752/60000 [========>.....................] - ETA: 1:18 - loss: 0.3390 - categorical_accuracy: 0.8917
18784/60000 [========>.....................] - ETA: 1:18 - loss: 0.3386 - categorical_accuracy: 0.8918
18816/60000 [========>.....................] - ETA: 1:18 - loss: 0.3384 - categorical_accuracy: 0.8917
18848/60000 [========>.....................] - ETA: 1:18 - loss: 0.3379 - categorical_accuracy: 0.8919
18880/60000 [========>.....................] - ETA: 1:18 - loss: 0.3382 - categorical_accuracy: 0.8918
18912/60000 [========>.....................] - ETA: 1:18 - loss: 0.3382 - categorical_accuracy: 0.8919
18944/60000 [========>.....................] - ETA: 1:18 - loss: 0.3379 - categorical_accuracy: 0.8920
18976/60000 [========>.....................] - ETA: 1:17 - loss: 0.3378 - categorical_accuracy: 0.8920
19008/60000 [========>.....................] - ETA: 1:17 - loss: 0.3378 - categorical_accuracy: 0.8920
19040/60000 [========>.....................] - ETA: 1:17 - loss: 0.3373 - categorical_accuracy: 0.8921
19072/60000 [========>.....................] - ETA: 1:17 - loss: 0.3374 - categorical_accuracy: 0.8922
19104/60000 [========>.....................] - ETA: 1:17 - loss: 0.3372 - categorical_accuracy: 0.8923
19136/60000 [========>.....................] - ETA: 1:17 - loss: 0.3367 - categorical_accuracy: 0.8925
19168/60000 [========>.....................] - ETA: 1:17 - loss: 0.3363 - categorical_accuracy: 0.8927
19200/60000 [========>.....................] - ETA: 1:17 - loss: 0.3361 - categorical_accuracy: 0.8928
19232/60000 [========>.....................] - ETA: 1:17 - loss: 0.3356 - categorical_accuracy: 0.8929
19264/60000 [========>.....................] - ETA: 1:17 - loss: 0.3354 - categorical_accuracy: 0.8930
19296/60000 [========>.....................] - ETA: 1:17 - loss: 0.3352 - categorical_accuracy: 0.8931
19328/60000 [========>.....................] - ETA: 1:17 - loss: 0.3348 - categorical_accuracy: 0.8932
19360/60000 [========>.....................] - ETA: 1:17 - loss: 0.3343 - categorical_accuracy: 0.8934
19392/60000 [========>.....................] - ETA: 1:17 - loss: 0.3339 - categorical_accuracy: 0.8935
19424/60000 [========>.....................] - ETA: 1:17 - loss: 0.3339 - categorical_accuracy: 0.8935
19456/60000 [========>.....................] - ETA: 1:17 - loss: 0.3335 - categorical_accuracy: 0.8937
19488/60000 [========>.....................] - ETA: 1:17 - loss: 0.3332 - categorical_accuracy: 0.8938
19520/60000 [========>.....................] - ETA: 1:16 - loss: 0.3331 - categorical_accuracy: 0.8939
19552/60000 [========>.....................] - ETA: 1:16 - loss: 0.3327 - categorical_accuracy: 0.8940
19584/60000 [========>.....................] - ETA: 1:16 - loss: 0.3328 - categorical_accuracy: 0.8940
19616/60000 [========>.....................] - ETA: 1:16 - loss: 0.3325 - categorical_accuracy: 0.8942
19648/60000 [========>.....................] - ETA: 1:16 - loss: 0.3323 - categorical_accuracy: 0.8943
19680/60000 [========>.....................] - ETA: 1:16 - loss: 0.3319 - categorical_accuracy: 0.8944
19712/60000 [========>.....................] - ETA: 1:16 - loss: 0.3317 - categorical_accuracy: 0.8944
19744/60000 [========>.....................] - ETA: 1:16 - loss: 0.3319 - categorical_accuracy: 0.8943
19776/60000 [========>.....................] - ETA: 1:16 - loss: 0.3316 - categorical_accuracy: 0.8944
19808/60000 [========>.....................] - ETA: 1:16 - loss: 0.3312 - categorical_accuracy: 0.8945
19840/60000 [========>.....................] - ETA: 1:16 - loss: 0.3313 - categorical_accuracy: 0.8946
19872/60000 [========>.....................] - ETA: 1:16 - loss: 0.3315 - categorical_accuracy: 0.8946
19904/60000 [========>.....................] - ETA: 1:16 - loss: 0.3311 - categorical_accuracy: 0.8948
19936/60000 [========>.....................] - ETA: 1:16 - loss: 0.3306 - categorical_accuracy: 0.8950
19968/60000 [========>.....................] - ETA: 1:16 - loss: 0.3302 - categorical_accuracy: 0.8951
20000/60000 [=========>....................] - ETA: 1:15 - loss: 0.3299 - categorical_accuracy: 0.8953
20032/60000 [=========>....................] - ETA: 1:15 - loss: 0.3295 - categorical_accuracy: 0.8953
20064/60000 [=========>....................] - ETA: 1:15 - loss: 0.3291 - categorical_accuracy: 0.8954
20096/60000 [=========>....................] - ETA: 1:15 - loss: 0.3290 - categorical_accuracy: 0.8955
20128/60000 [=========>....................] - ETA: 1:15 - loss: 0.3286 - categorical_accuracy: 0.8957
20160/60000 [=========>....................] - ETA: 1:15 - loss: 0.3282 - categorical_accuracy: 0.8958
20192/60000 [=========>....................] - ETA: 1:15 - loss: 0.3278 - categorical_accuracy: 0.8959
20224/60000 [=========>....................] - ETA: 1:15 - loss: 0.3276 - categorical_accuracy: 0.8960
20256/60000 [=========>....................] - ETA: 1:15 - loss: 0.3273 - categorical_accuracy: 0.8960
20288/60000 [=========>....................] - ETA: 1:15 - loss: 0.3275 - categorical_accuracy: 0.8960
20320/60000 [=========>....................] - ETA: 1:15 - loss: 0.3272 - categorical_accuracy: 0.8960
20352/60000 [=========>....................] - ETA: 1:15 - loss: 0.3268 - categorical_accuracy: 0.8961
20384/60000 [=========>....................] - ETA: 1:15 - loss: 0.3265 - categorical_accuracy: 0.8962
20416/60000 [=========>....................] - ETA: 1:15 - loss: 0.3261 - categorical_accuracy: 0.8963
20448/60000 [=========>....................] - ETA: 1:15 - loss: 0.3263 - categorical_accuracy: 0.8964
20480/60000 [=========>....................] - ETA: 1:15 - loss: 0.3258 - categorical_accuracy: 0.8965
20512/60000 [=========>....................] - ETA: 1:15 - loss: 0.3255 - categorical_accuracy: 0.8966
20544/60000 [=========>....................] - ETA: 1:14 - loss: 0.3251 - categorical_accuracy: 0.8968
20576/60000 [=========>....................] - ETA: 1:14 - loss: 0.3248 - categorical_accuracy: 0.8969
20608/60000 [=========>....................] - ETA: 1:14 - loss: 0.3244 - categorical_accuracy: 0.8970
20640/60000 [=========>....................] - ETA: 1:14 - loss: 0.3242 - categorical_accuracy: 0.8970
20672/60000 [=========>....................] - ETA: 1:14 - loss: 0.3237 - categorical_accuracy: 0.8972
20704/60000 [=========>....................] - ETA: 1:14 - loss: 0.3234 - categorical_accuracy: 0.8973
20736/60000 [=========>....................] - ETA: 1:14 - loss: 0.3230 - categorical_accuracy: 0.8974
20768/60000 [=========>....................] - ETA: 1:14 - loss: 0.3229 - categorical_accuracy: 0.8974
20800/60000 [=========>....................] - ETA: 1:14 - loss: 0.3228 - categorical_accuracy: 0.8974
20832/60000 [=========>....................] - ETA: 1:14 - loss: 0.3223 - categorical_accuracy: 0.8976
20864/60000 [=========>....................] - ETA: 1:14 - loss: 0.3221 - categorical_accuracy: 0.8977
20896/60000 [=========>....................] - ETA: 1:14 - loss: 0.3226 - categorical_accuracy: 0.8976
20928/60000 [=========>....................] - ETA: 1:14 - loss: 0.3225 - categorical_accuracy: 0.8976
20960/60000 [=========>....................] - ETA: 1:14 - loss: 0.3224 - categorical_accuracy: 0.8977
20992/60000 [=========>....................] - ETA: 1:14 - loss: 0.3221 - categorical_accuracy: 0.8977
21024/60000 [=========>....................] - ETA: 1:14 - loss: 0.3217 - categorical_accuracy: 0.8979
21056/60000 [=========>....................] - ETA: 1:13 - loss: 0.3213 - categorical_accuracy: 0.8980
21088/60000 [=========>....................] - ETA: 1:13 - loss: 0.3214 - categorical_accuracy: 0.8981
21120/60000 [=========>....................] - ETA: 1:13 - loss: 0.3214 - categorical_accuracy: 0.8981
21152/60000 [=========>....................] - ETA: 1:13 - loss: 0.3212 - categorical_accuracy: 0.8982
21184/60000 [=========>....................] - ETA: 1:13 - loss: 0.3212 - categorical_accuracy: 0.8981
21216/60000 [=========>....................] - ETA: 1:13 - loss: 0.3210 - categorical_accuracy: 0.8982
21248/60000 [=========>....................] - ETA: 1:13 - loss: 0.3206 - categorical_accuracy: 0.8984
21280/60000 [=========>....................] - ETA: 1:13 - loss: 0.3202 - categorical_accuracy: 0.8985
21312/60000 [=========>....................] - ETA: 1:13 - loss: 0.3199 - categorical_accuracy: 0.8986
21344/60000 [=========>....................] - ETA: 1:13 - loss: 0.3195 - categorical_accuracy: 0.8987
21376/60000 [=========>....................] - ETA: 1:13 - loss: 0.3196 - categorical_accuracy: 0.8987
21408/60000 [=========>....................] - ETA: 1:13 - loss: 0.3194 - categorical_accuracy: 0.8987
21440/60000 [=========>....................] - ETA: 1:13 - loss: 0.3191 - categorical_accuracy: 0.8988
21472/60000 [=========>....................] - ETA: 1:13 - loss: 0.3187 - categorical_accuracy: 0.8990
21504/60000 [=========>....................] - ETA: 1:13 - loss: 0.3182 - categorical_accuracy: 0.8991
21536/60000 [=========>....................] - ETA: 1:13 - loss: 0.3179 - categorical_accuracy: 0.8992
21568/60000 [=========>....................] - ETA: 1:13 - loss: 0.3176 - categorical_accuracy: 0.8992
21600/60000 [=========>....................] - ETA: 1:12 - loss: 0.3174 - categorical_accuracy: 0.8993
21632/60000 [=========>....................] - ETA: 1:12 - loss: 0.3173 - categorical_accuracy: 0.8993
21664/60000 [=========>....................] - ETA: 1:12 - loss: 0.3168 - categorical_accuracy: 0.8994
21696/60000 [=========>....................] - ETA: 1:12 - loss: 0.3166 - categorical_accuracy: 0.8995
21728/60000 [=========>....................] - ETA: 1:12 - loss: 0.3165 - categorical_accuracy: 0.8995
21760/60000 [=========>....................] - ETA: 1:12 - loss: 0.3162 - categorical_accuracy: 0.8996
21792/60000 [=========>....................] - ETA: 1:12 - loss: 0.3158 - categorical_accuracy: 0.8997
21824/60000 [=========>....................] - ETA: 1:12 - loss: 0.3155 - categorical_accuracy: 0.8998
21856/60000 [=========>....................] - ETA: 1:12 - loss: 0.3152 - categorical_accuracy: 0.8999
21888/60000 [=========>....................] - ETA: 1:12 - loss: 0.3149 - categorical_accuracy: 0.8999
21920/60000 [=========>....................] - ETA: 1:12 - loss: 0.3145 - categorical_accuracy: 0.9001
21952/60000 [=========>....................] - ETA: 1:12 - loss: 0.3142 - categorical_accuracy: 0.9002
21984/60000 [=========>....................] - ETA: 1:12 - loss: 0.3138 - categorical_accuracy: 0.9003
22016/60000 [==========>...................] - ETA: 1:12 - loss: 0.3135 - categorical_accuracy: 0.9004
22048/60000 [==========>...................] - ETA: 1:12 - loss: 0.3133 - categorical_accuracy: 0.9004
22080/60000 [==========>...................] - ETA: 1:12 - loss: 0.3129 - categorical_accuracy: 0.9006
22112/60000 [==========>...................] - ETA: 1:11 - loss: 0.3129 - categorical_accuracy: 0.9006
22144/60000 [==========>...................] - ETA: 1:11 - loss: 0.3125 - categorical_accuracy: 0.9007
22176/60000 [==========>...................] - ETA: 1:11 - loss: 0.3122 - categorical_accuracy: 0.9008
22208/60000 [==========>...................] - ETA: 1:11 - loss: 0.3118 - categorical_accuracy: 0.9009
22240/60000 [==========>...................] - ETA: 1:11 - loss: 0.3114 - categorical_accuracy: 0.9011
22272/60000 [==========>...................] - ETA: 1:11 - loss: 0.3111 - categorical_accuracy: 0.9012
22304/60000 [==========>...................] - ETA: 1:11 - loss: 0.3110 - categorical_accuracy: 0.9011
22336/60000 [==========>...................] - ETA: 1:11 - loss: 0.3106 - categorical_accuracy: 0.9012
22368/60000 [==========>...................] - ETA: 1:11 - loss: 0.3103 - categorical_accuracy: 0.9013
22400/60000 [==========>...................] - ETA: 1:11 - loss: 0.3101 - categorical_accuracy: 0.9014
22432/60000 [==========>...................] - ETA: 1:11 - loss: 0.3098 - categorical_accuracy: 0.9015
22464/60000 [==========>...................] - ETA: 1:11 - loss: 0.3094 - categorical_accuracy: 0.9016
22496/60000 [==========>...................] - ETA: 1:11 - loss: 0.3091 - categorical_accuracy: 0.9017
22528/60000 [==========>...................] - ETA: 1:11 - loss: 0.3096 - categorical_accuracy: 0.9016
22560/60000 [==========>...................] - ETA: 1:11 - loss: 0.3092 - categorical_accuracy: 0.9018
22592/60000 [==========>...................] - ETA: 1:11 - loss: 0.3089 - categorical_accuracy: 0.9019
22624/60000 [==========>...................] - ETA: 1:10 - loss: 0.3087 - categorical_accuracy: 0.9020
22656/60000 [==========>...................] - ETA: 1:10 - loss: 0.3083 - categorical_accuracy: 0.9021
22688/60000 [==========>...................] - ETA: 1:10 - loss: 0.3084 - categorical_accuracy: 0.9021
22720/60000 [==========>...................] - ETA: 1:10 - loss: 0.3082 - categorical_accuracy: 0.9021
22752/60000 [==========>...................] - ETA: 1:10 - loss: 0.3082 - categorical_accuracy: 0.9022
22784/60000 [==========>...................] - ETA: 1:10 - loss: 0.3082 - categorical_accuracy: 0.9022
22816/60000 [==========>...................] - ETA: 1:10 - loss: 0.3079 - categorical_accuracy: 0.9023
22848/60000 [==========>...................] - ETA: 1:10 - loss: 0.3078 - categorical_accuracy: 0.9023
22880/60000 [==========>...................] - ETA: 1:10 - loss: 0.3076 - categorical_accuracy: 0.9024
22912/60000 [==========>...................] - ETA: 1:10 - loss: 0.3073 - categorical_accuracy: 0.9025
22944/60000 [==========>...................] - ETA: 1:10 - loss: 0.3071 - categorical_accuracy: 0.9025
22976/60000 [==========>...................] - ETA: 1:10 - loss: 0.3068 - categorical_accuracy: 0.9026
23008/60000 [==========>...................] - ETA: 1:10 - loss: 0.3065 - categorical_accuracy: 0.9027
23040/60000 [==========>...................] - ETA: 1:10 - loss: 0.3063 - categorical_accuracy: 0.9028
23072/60000 [==========>...................] - ETA: 1:10 - loss: 0.3061 - categorical_accuracy: 0.9028
23104/60000 [==========>...................] - ETA: 1:10 - loss: 0.3057 - categorical_accuracy: 0.9029
23136/60000 [==========>...................] - ETA: 1:10 - loss: 0.3055 - categorical_accuracy: 0.9030
23168/60000 [==========>...................] - ETA: 1:09 - loss: 0.3054 - categorical_accuracy: 0.9030
23200/60000 [==========>...................] - ETA: 1:09 - loss: 0.3051 - categorical_accuracy: 0.9031
23232/60000 [==========>...................] - ETA: 1:09 - loss: 0.3049 - categorical_accuracy: 0.9032
23264/60000 [==========>...................] - ETA: 1:09 - loss: 0.3045 - categorical_accuracy: 0.9032
23296/60000 [==========>...................] - ETA: 1:09 - loss: 0.3041 - categorical_accuracy: 0.9034
23328/60000 [==========>...................] - ETA: 1:09 - loss: 0.3038 - categorical_accuracy: 0.9035
23360/60000 [==========>...................] - ETA: 1:09 - loss: 0.3040 - categorical_accuracy: 0.9035
23392/60000 [==========>...................] - ETA: 1:09 - loss: 0.3037 - categorical_accuracy: 0.9036
23424/60000 [==========>...................] - ETA: 1:09 - loss: 0.3034 - categorical_accuracy: 0.9037
23456/60000 [==========>...................] - ETA: 1:09 - loss: 0.3031 - categorical_accuracy: 0.9038
23488/60000 [==========>...................] - ETA: 1:09 - loss: 0.3028 - categorical_accuracy: 0.9039
23520/60000 [==========>...................] - ETA: 1:09 - loss: 0.3028 - categorical_accuracy: 0.9039
23552/60000 [==========>...................] - ETA: 1:09 - loss: 0.3025 - categorical_accuracy: 0.9040
23584/60000 [==========>...................] - ETA: 1:09 - loss: 0.3023 - categorical_accuracy: 0.9040
23616/60000 [==========>...................] - ETA: 1:09 - loss: 0.3020 - categorical_accuracy: 0.9041
23648/60000 [==========>...................] - ETA: 1:09 - loss: 0.3017 - categorical_accuracy: 0.9042
23680/60000 [==========>...................] - ETA: 1:08 - loss: 0.3015 - categorical_accuracy: 0.9042
23712/60000 [==========>...................] - ETA: 1:08 - loss: 0.3011 - categorical_accuracy: 0.9044
23744/60000 [==========>...................] - ETA: 1:08 - loss: 0.3009 - categorical_accuracy: 0.9044
23776/60000 [==========>...................] - ETA: 1:08 - loss: 0.3007 - categorical_accuracy: 0.9045
23808/60000 [==========>...................] - ETA: 1:08 - loss: 0.3004 - categorical_accuracy: 0.9046
23840/60000 [==========>...................] - ETA: 1:08 - loss: 0.3006 - categorical_accuracy: 0.9046
23872/60000 [==========>...................] - ETA: 1:08 - loss: 0.3002 - categorical_accuracy: 0.9047
23904/60000 [==========>...................] - ETA: 1:08 - loss: 0.2999 - categorical_accuracy: 0.9048
23936/60000 [==========>...................] - ETA: 1:08 - loss: 0.2996 - categorical_accuracy: 0.9050
23968/60000 [==========>...................] - ETA: 1:08 - loss: 0.2993 - categorical_accuracy: 0.9051
24000/60000 [===========>..................] - ETA: 1:08 - loss: 0.2989 - categorical_accuracy: 0.9052
24032/60000 [===========>..................] - ETA: 1:08 - loss: 0.2989 - categorical_accuracy: 0.9052
24064/60000 [===========>..................] - ETA: 1:08 - loss: 0.2987 - categorical_accuracy: 0.9053
24096/60000 [===========>..................] - ETA: 1:08 - loss: 0.2986 - categorical_accuracy: 0.9053
24128/60000 [===========>..................] - ETA: 1:08 - loss: 0.2985 - categorical_accuracy: 0.9053
24160/60000 [===========>..................] - ETA: 1:08 - loss: 0.2984 - categorical_accuracy: 0.9054
24192/60000 [===========>..................] - ETA: 1:07 - loss: 0.2987 - categorical_accuracy: 0.9054
24224/60000 [===========>..................] - ETA: 1:07 - loss: 0.2984 - categorical_accuracy: 0.9055
24256/60000 [===========>..................] - ETA: 1:07 - loss: 0.2982 - categorical_accuracy: 0.9055
24288/60000 [===========>..................] - ETA: 1:07 - loss: 0.2981 - categorical_accuracy: 0.9056
24320/60000 [===========>..................] - ETA: 1:07 - loss: 0.2978 - categorical_accuracy: 0.9056
24352/60000 [===========>..................] - ETA: 1:07 - loss: 0.2977 - categorical_accuracy: 0.9057
24384/60000 [===========>..................] - ETA: 1:07 - loss: 0.2976 - categorical_accuracy: 0.9057
24416/60000 [===========>..................] - ETA: 1:07 - loss: 0.2973 - categorical_accuracy: 0.9058
24448/60000 [===========>..................] - ETA: 1:07 - loss: 0.2972 - categorical_accuracy: 0.9058
24480/60000 [===========>..................] - ETA: 1:07 - loss: 0.2969 - categorical_accuracy: 0.9059
24512/60000 [===========>..................] - ETA: 1:07 - loss: 0.2967 - categorical_accuracy: 0.9060
24544/60000 [===========>..................] - ETA: 1:07 - loss: 0.2964 - categorical_accuracy: 0.9061
24576/60000 [===========>..................] - ETA: 1:07 - loss: 0.2964 - categorical_accuracy: 0.9061
24608/60000 [===========>..................] - ETA: 1:07 - loss: 0.2961 - categorical_accuracy: 0.9062
24640/60000 [===========>..................] - ETA: 1:07 - loss: 0.2959 - categorical_accuracy: 0.9062
24672/60000 [===========>..................] - ETA: 1:07 - loss: 0.2956 - categorical_accuracy: 0.9064
24704/60000 [===========>..................] - ETA: 1:06 - loss: 0.2953 - categorical_accuracy: 0.9065
24736/60000 [===========>..................] - ETA: 1:06 - loss: 0.2950 - categorical_accuracy: 0.9066
24768/60000 [===========>..................] - ETA: 1:06 - loss: 0.2950 - categorical_accuracy: 0.9067
24800/60000 [===========>..................] - ETA: 1:06 - loss: 0.2947 - categorical_accuracy: 0.9067
24832/60000 [===========>..................] - ETA: 1:06 - loss: 0.2946 - categorical_accuracy: 0.9067
24864/60000 [===========>..................] - ETA: 1:06 - loss: 0.2945 - categorical_accuracy: 0.9067
24896/60000 [===========>..................] - ETA: 1:06 - loss: 0.2942 - categorical_accuracy: 0.9068
24928/60000 [===========>..................] - ETA: 1:06 - loss: 0.2939 - categorical_accuracy: 0.9069
24960/60000 [===========>..................] - ETA: 1:06 - loss: 0.2936 - categorical_accuracy: 0.9071
24992/60000 [===========>..................] - ETA: 1:06 - loss: 0.2933 - categorical_accuracy: 0.9071
25024/60000 [===========>..................] - ETA: 1:06 - loss: 0.2929 - categorical_accuracy: 0.9072
25056/60000 [===========>..................] - ETA: 1:06 - loss: 0.2926 - categorical_accuracy: 0.9074
25088/60000 [===========>..................] - ETA: 1:06 - loss: 0.2924 - categorical_accuracy: 0.9074
25120/60000 [===========>..................] - ETA: 1:06 - loss: 0.2924 - categorical_accuracy: 0.9075
25152/60000 [===========>..................] - ETA: 1:06 - loss: 0.2921 - categorical_accuracy: 0.9076
25184/60000 [===========>..................] - ETA: 1:06 - loss: 0.2918 - categorical_accuracy: 0.9077
25216/60000 [===========>..................] - ETA: 1:05 - loss: 0.2916 - categorical_accuracy: 0.9078
25248/60000 [===========>..................] - ETA: 1:05 - loss: 0.2913 - categorical_accuracy: 0.9079
25280/60000 [===========>..................] - ETA: 1:05 - loss: 0.2910 - categorical_accuracy: 0.9080
25312/60000 [===========>..................] - ETA: 1:05 - loss: 0.2907 - categorical_accuracy: 0.9080
25344/60000 [===========>..................] - ETA: 1:05 - loss: 0.2906 - categorical_accuracy: 0.9080
25376/60000 [===========>..................] - ETA: 1:05 - loss: 0.2906 - categorical_accuracy: 0.9081
25408/60000 [===========>..................] - ETA: 1:05 - loss: 0.2902 - categorical_accuracy: 0.9082
25440/60000 [===========>..................] - ETA: 1:05 - loss: 0.2900 - categorical_accuracy: 0.9082
25472/60000 [===========>..................] - ETA: 1:05 - loss: 0.2898 - categorical_accuracy: 0.9083
25504/60000 [===========>..................] - ETA: 1:05 - loss: 0.2895 - categorical_accuracy: 0.9084
25536/60000 [===========>..................] - ETA: 1:05 - loss: 0.2894 - categorical_accuracy: 0.9085
25568/60000 [===========>..................] - ETA: 1:05 - loss: 0.2892 - categorical_accuracy: 0.9086
25600/60000 [===========>..................] - ETA: 1:05 - loss: 0.2893 - categorical_accuracy: 0.9086
25632/60000 [===========>..................] - ETA: 1:05 - loss: 0.2890 - categorical_accuracy: 0.9087
25664/60000 [===========>..................] - ETA: 1:05 - loss: 0.2886 - categorical_accuracy: 0.9088
25696/60000 [===========>..................] - ETA: 1:05 - loss: 0.2883 - categorical_accuracy: 0.9089
25728/60000 [===========>..................] - ETA: 1:05 - loss: 0.2881 - categorical_accuracy: 0.9090
25760/60000 [===========>..................] - ETA: 1:04 - loss: 0.2879 - categorical_accuracy: 0.9090
25792/60000 [===========>..................] - ETA: 1:04 - loss: 0.2876 - categorical_accuracy: 0.9091
25824/60000 [===========>..................] - ETA: 1:04 - loss: 0.2873 - categorical_accuracy: 0.9092
25856/60000 [===========>..................] - ETA: 1:04 - loss: 0.2871 - categorical_accuracy: 0.9093
25888/60000 [===========>..................] - ETA: 1:04 - loss: 0.2868 - categorical_accuracy: 0.9094
25920/60000 [===========>..................] - ETA: 1:04 - loss: 0.2865 - categorical_accuracy: 0.9094
25952/60000 [===========>..................] - ETA: 1:04 - loss: 0.2864 - categorical_accuracy: 0.9094
25984/60000 [===========>..................] - ETA: 1:04 - loss: 0.2861 - categorical_accuracy: 0.9096
26016/60000 [============>.................] - ETA: 1:04 - loss: 0.2860 - categorical_accuracy: 0.9096
26048/60000 [============>.................] - ETA: 1:04 - loss: 0.2857 - categorical_accuracy: 0.9097
26080/60000 [============>.................] - ETA: 1:04 - loss: 0.2854 - categorical_accuracy: 0.9097
26112/60000 [============>.................] - ETA: 1:04 - loss: 0.2850 - categorical_accuracy: 0.9098
26144/60000 [============>.................] - ETA: 1:04 - loss: 0.2847 - categorical_accuracy: 0.9100
26176/60000 [============>.................] - ETA: 1:04 - loss: 0.2846 - categorical_accuracy: 0.9100
26208/60000 [============>.................] - ETA: 1:04 - loss: 0.2845 - categorical_accuracy: 0.9100
26240/60000 [============>.................] - ETA: 1:04 - loss: 0.2844 - categorical_accuracy: 0.9100
26272/60000 [============>.................] - ETA: 1:04 - loss: 0.2845 - categorical_accuracy: 0.9100
26304/60000 [============>.................] - ETA: 1:03 - loss: 0.2843 - categorical_accuracy: 0.9100
26336/60000 [============>.................] - ETA: 1:03 - loss: 0.2841 - categorical_accuracy: 0.9101
26368/60000 [============>.................] - ETA: 1:03 - loss: 0.2841 - categorical_accuracy: 0.9101
26400/60000 [============>.................] - ETA: 1:03 - loss: 0.2838 - categorical_accuracy: 0.9102
26432/60000 [============>.................] - ETA: 1:03 - loss: 0.2836 - categorical_accuracy: 0.9103
26464/60000 [============>.................] - ETA: 1:03 - loss: 0.2838 - categorical_accuracy: 0.9103
26496/60000 [============>.................] - ETA: 1:03 - loss: 0.2835 - categorical_accuracy: 0.9104
26528/60000 [============>.................] - ETA: 1:03 - loss: 0.2833 - categorical_accuracy: 0.9104
26560/60000 [============>.................] - ETA: 1:03 - loss: 0.2832 - categorical_accuracy: 0.9105
26592/60000 [============>.................] - ETA: 1:03 - loss: 0.2830 - categorical_accuracy: 0.9105
26624/60000 [============>.................] - ETA: 1:03 - loss: 0.2829 - categorical_accuracy: 0.9106
26656/60000 [============>.................] - ETA: 1:03 - loss: 0.2826 - categorical_accuracy: 0.9107
26688/60000 [============>.................] - ETA: 1:03 - loss: 0.2823 - categorical_accuracy: 0.9108
26720/60000 [============>.................] - ETA: 1:03 - loss: 0.2821 - categorical_accuracy: 0.9109
26752/60000 [============>.................] - ETA: 1:03 - loss: 0.2818 - categorical_accuracy: 0.9110
26784/60000 [============>.................] - ETA: 1:03 - loss: 0.2816 - categorical_accuracy: 0.9111
26816/60000 [============>.................] - ETA: 1:03 - loss: 0.2815 - categorical_accuracy: 0.9111
26848/60000 [============>.................] - ETA: 1:02 - loss: 0.2812 - categorical_accuracy: 0.9112
26880/60000 [============>.................] - ETA: 1:02 - loss: 0.2810 - categorical_accuracy: 0.9113
26912/60000 [============>.................] - ETA: 1:02 - loss: 0.2806 - categorical_accuracy: 0.9114
26944/60000 [============>.................] - ETA: 1:02 - loss: 0.2804 - categorical_accuracy: 0.9114
26976/60000 [============>.................] - ETA: 1:02 - loss: 0.2802 - categorical_accuracy: 0.9115
27008/60000 [============>.................] - ETA: 1:02 - loss: 0.2800 - categorical_accuracy: 0.9116
27040/60000 [============>.................] - ETA: 1:02 - loss: 0.2798 - categorical_accuracy: 0.9116
27072/60000 [============>.................] - ETA: 1:02 - loss: 0.2795 - categorical_accuracy: 0.9118
27104/60000 [============>.................] - ETA: 1:02 - loss: 0.2794 - categorical_accuracy: 0.9118
27136/60000 [============>.................] - ETA: 1:02 - loss: 0.2795 - categorical_accuracy: 0.9118
27168/60000 [============>.................] - ETA: 1:02 - loss: 0.2796 - categorical_accuracy: 0.9118
27200/60000 [============>.................] - ETA: 1:02 - loss: 0.2794 - categorical_accuracy: 0.9118
27232/60000 [============>.................] - ETA: 1:02 - loss: 0.2791 - categorical_accuracy: 0.9119
27264/60000 [============>.................] - ETA: 1:02 - loss: 0.2791 - categorical_accuracy: 0.9120
27296/60000 [============>.................] - ETA: 1:02 - loss: 0.2790 - categorical_accuracy: 0.9120
27328/60000 [============>.................] - ETA: 1:02 - loss: 0.2788 - categorical_accuracy: 0.9121
27360/60000 [============>.................] - ETA: 1:01 - loss: 0.2786 - categorical_accuracy: 0.9121
27392/60000 [============>.................] - ETA: 1:01 - loss: 0.2782 - categorical_accuracy: 0.9122
27424/60000 [============>.................] - ETA: 1:01 - loss: 0.2780 - categorical_accuracy: 0.9123
27456/60000 [============>.................] - ETA: 1:01 - loss: 0.2778 - categorical_accuracy: 0.9124
27488/60000 [============>.................] - ETA: 1:01 - loss: 0.2776 - categorical_accuracy: 0.9124
27520/60000 [============>.................] - ETA: 1:01 - loss: 0.2778 - categorical_accuracy: 0.9124
27552/60000 [============>.................] - ETA: 1:01 - loss: 0.2777 - categorical_accuracy: 0.9125
27584/60000 [============>.................] - ETA: 1:01 - loss: 0.2774 - categorical_accuracy: 0.9126
27616/60000 [============>.................] - ETA: 1:01 - loss: 0.2772 - categorical_accuracy: 0.9127
27648/60000 [============>.................] - ETA: 1:01 - loss: 0.2769 - categorical_accuracy: 0.9128
27680/60000 [============>.................] - ETA: 1:01 - loss: 0.2766 - categorical_accuracy: 0.9129
27712/60000 [============>.................] - ETA: 1:01 - loss: 0.2764 - categorical_accuracy: 0.9129
27744/60000 [============>.................] - ETA: 1:01 - loss: 0.2764 - categorical_accuracy: 0.9129
27776/60000 [============>.................] - ETA: 1:01 - loss: 0.2763 - categorical_accuracy: 0.9129
27808/60000 [============>.................] - ETA: 1:01 - loss: 0.2761 - categorical_accuracy: 0.9130
27840/60000 [============>.................] - ETA: 1:01 - loss: 0.2760 - categorical_accuracy: 0.9130
27872/60000 [============>.................] - ETA: 1:00 - loss: 0.2757 - categorical_accuracy: 0.9131
27904/60000 [============>.................] - ETA: 1:00 - loss: 0.2756 - categorical_accuracy: 0.9132
27936/60000 [============>.................] - ETA: 1:00 - loss: 0.2754 - categorical_accuracy: 0.9132
27968/60000 [============>.................] - ETA: 1:00 - loss: 0.2751 - categorical_accuracy: 0.9133
28000/60000 [=============>................] - ETA: 1:00 - loss: 0.2753 - categorical_accuracy: 0.9133
28032/60000 [=============>................] - ETA: 1:00 - loss: 0.2752 - categorical_accuracy: 0.9133
28064/60000 [=============>................] - ETA: 1:00 - loss: 0.2750 - categorical_accuracy: 0.9134
28096/60000 [=============>................] - ETA: 1:00 - loss: 0.2748 - categorical_accuracy: 0.9135
28128/60000 [=============>................] - ETA: 1:00 - loss: 0.2746 - categorical_accuracy: 0.9136
28160/60000 [=============>................] - ETA: 1:00 - loss: 0.2746 - categorical_accuracy: 0.9136
28192/60000 [=============>................] - ETA: 1:00 - loss: 0.2747 - categorical_accuracy: 0.9137
28224/60000 [=============>................] - ETA: 1:00 - loss: 0.2746 - categorical_accuracy: 0.9137
28256/60000 [=============>................] - ETA: 1:00 - loss: 0.2743 - categorical_accuracy: 0.9138
28288/60000 [=============>................] - ETA: 1:00 - loss: 0.2742 - categorical_accuracy: 0.9139
28320/60000 [=============>................] - ETA: 1:00 - loss: 0.2740 - categorical_accuracy: 0.9139
28352/60000 [=============>................] - ETA: 1:00 - loss: 0.2737 - categorical_accuracy: 0.9140
28384/60000 [=============>................] - ETA: 59s - loss: 0.2736 - categorical_accuracy: 0.9140 
28416/60000 [=============>................] - ETA: 59s - loss: 0.2734 - categorical_accuracy: 0.9141
28448/60000 [=============>................] - ETA: 59s - loss: 0.2731 - categorical_accuracy: 0.9142
28480/60000 [=============>................] - ETA: 59s - loss: 0.2729 - categorical_accuracy: 0.9143
28512/60000 [=============>................] - ETA: 59s - loss: 0.2727 - categorical_accuracy: 0.9144
28544/60000 [=============>................] - ETA: 59s - loss: 0.2726 - categorical_accuracy: 0.9143
28576/60000 [=============>................] - ETA: 59s - loss: 0.2726 - categorical_accuracy: 0.9143
28608/60000 [=============>................] - ETA: 59s - loss: 0.2726 - categorical_accuracy: 0.9144
28640/60000 [=============>................] - ETA: 59s - loss: 0.2723 - categorical_accuracy: 0.9145
28672/60000 [=============>................] - ETA: 59s - loss: 0.2720 - categorical_accuracy: 0.9146
28704/60000 [=============>................] - ETA: 59s - loss: 0.2718 - categorical_accuracy: 0.9146
28736/60000 [=============>................] - ETA: 59s - loss: 0.2715 - categorical_accuracy: 0.9147
28768/60000 [=============>................] - ETA: 59s - loss: 0.2714 - categorical_accuracy: 0.9147
28800/60000 [=============>................] - ETA: 59s - loss: 0.2714 - categorical_accuracy: 0.9148
28832/60000 [=============>................] - ETA: 59s - loss: 0.2711 - categorical_accuracy: 0.9149
28864/60000 [=============>................] - ETA: 59s - loss: 0.2709 - categorical_accuracy: 0.9149
28896/60000 [=============>................] - ETA: 58s - loss: 0.2707 - categorical_accuracy: 0.9150
28928/60000 [=============>................] - ETA: 58s - loss: 0.2705 - categorical_accuracy: 0.9151
28960/60000 [=============>................] - ETA: 58s - loss: 0.2703 - categorical_accuracy: 0.9151
28992/60000 [=============>................] - ETA: 58s - loss: 0.2703 - categorical_accuracy: 0.9151
29024/60000 [=============>................] - ETA: 58s - loss: 0.2703 - categorical_accuracy: 0.9152
29056/60000 [=============>................] - ETA: 58s - loss: 0.2703 - categorical_accuracy: 0.9152
29088/60000 [=============>................] - ETA: 58s - loss: 0.2700 - categorical_accuracy: 0.9153
29120/60000 [=============>................] - ETA: 58s - loss: 0.2698 - categorical_accuracy: 0.9154
29152/60000 [=============>................] - ETA: 58s - loss: 0.2695 - categorical_accuracy: 0.9155
29184/60000 [=============>................] - ETA: 58s - loss: 0.2694 - categorical_accuracy: 0.9155
29216/60000 [=============>................] - ETA: 58s - loss: 0.2691 - categorical_accuracy: 0.9156
29248/60000 [=============>................] - ETA: 58s - loss: 0.2692 - categorical_accuracy: 0.9156
29280/60000 [=============>................] - ETA: 58s - loss: 0.2694 - categorical_accuracy: 0.9155
29312/60000 [=============>................] - ETA: 58s - loss: 0.2693 - categorical_accuracy: 0.9155
29344/60000 [=============>................] - ETA: 58s - loss: 0.2692 - categorical_accuracy: 0.9155
29376/60000 [=============>................] - ETA: 58s - loss: 0.2692 - categorical_accuracy: 0.9155
29408/60000 [=============>................] - ETA: 58s - loss: 0.2692 - categorical_accuracy: 0.9155
29440/60000 [=============>................] - ETA: 57s - loss: 0.2690 - categorical_accuracy: 0.9155
29472/60000 [=============>................] - ETA: 57s - loss: 0.2688 - categorical_accuracy: 0.9155
29504/60000 [=============>................] - ETA: 57s - loss: 0.2686 - categorical_accuracy: 0.9156
29536/60000 [=============>................] - ETA: 57s - loss: 0.2683 - categorical_accuracy: 0.9157
29568/60000 [=============>................] - ETA: 57s - loss: 0.2681 - categorical_accuracy: 0.9158
29600/60000 [=============>................] - ETA: 57s - loss: 0.2678 - categorical_accuracy: 0.9159
29632/60000 [=============>................] - ETA: 57s - loss: 0.2676 - categorical_accuracy: 0.9160
29664/60000 [=============>................] - ETA: 57s - loss: 0.2674 - categorical_accuracy: 0.9161
29696/60000 [=============>................] - ETA: 57s - loss: 0.2672 - categorical_accuracy: 0.9160
29728/60000 [=============>................] - ETA: 57s - loss: 0.2672 - categorical_accuracy: 0.9161
29760/60000 [=============>................] - ETA: 57s - loss: 0.2670 - categorical_accuracy: 0.9162
29792/60000 [=============>................] - ETA: 57s - loss: 0.2668 - categorical_accuracy: 0.9163
29824/60000 [=============>................] - ETA: 57s - loss: 0.2665 - categorical_accuracy: 0.9163
29856/60000 [=============>................] - ETA: 57s - loss: 0.2665 - categorical_accuracy: 0.9163
29888/60000 [=============>................] - ETA: 57s - loss: 0.2663 - categorical_accuracy: 0.9164
29920/60000 [=============>................] - ETA: 57s - loss: 0.2662 - categorical_accuracy: 0.9164
29952/60000 [=============>................] - ETA: 56s - loss: 0.2661 - categorical_accuracy: 0.9164
29984/60000 [=============>................] - ETA: 56s - loss: 0.2659 - categorical_accuracy: 0.9165
30016/60000 [==============>...............] - ETA: 56s - loss: 0.2660 - categorical_accuracy: 0.9165
30048/60000 [==============>...............] - ETA: 56s - loss: 0.2657 - categorical_accuracy: 0.9166
30080/60000 [==============>...............] - ETA: 56s - loss: 0.2656 - categorical_accuracy: 0.9167
30112/60000 [==============>...............] - ETA: 56s - loss: 0.2655 - categorical_accuracy: 0.9166
30144/60000 [==============>...............] - ETA: 56s - loss: 0.2653 - categorical_accuracy: 0.9167
30176/60000 [==============>...............] - ETA: 56s - loss: 0.2650 - categorical_accuracy: 0.9168
30208/60000 [==============>...............] - ETA: 56s - loss: 0.2648 - categorical_accuracy: 0.9169
30240/60000 [==============>...............] - ETA: 56s - loss: 0.2650 - categorical_accuracy: 0.9168
30272/60000 [==============>...............] - ETA: 56s - loss: 0.2647 - categorical_accuracy: 0.9169
30304/60000 [==============>...............] - ETA: 56s - loss: 0.2645 - categorical_accuracy: 0.9170
30336/60000 [==============>...............] - ETA: 56s - loss: 0.2643 - categorical_accuracy: 0.9171
30368/60000 [==============>...............] - ETA: 56s - loss: 0.2644 - categorical_accuracy: 0.9171
30400/60000 [==============>...............] - ETA: 56s - loss: 0.2641 - categorical_accuracy: 0.9172
30432/60000 [==============>...............] - ETA: 56s - loss: 0.2640 - categorical_accuracy: 0.9172
30464/60000 [==============>...............] - ETA: 55s - loss: 0.2638 - categorical_accuracy: 0.9173
30496/60000 [==============>...............] - ETA: 55s - loss: 0.2636 - categorical_accuracy: 0.9173
30528/60000 [==============>...............] - ETA: 55s - loss: 0.2635 - categorical_accuracy: 0.9174
30560/60000 [==============>...............] - ETA: 55s - loss: 0.2633 - categorical_accuracy: 0.9174
30592/60000 [==============>...............] - ETA: 55s - loss: 0.2631 - categorical_accuracy: 0.9175
30624/60000 [==============>...............] - ETA: 55s - loss: 0.2629 - categorical_accuracy: 0.9175
30656/60000 [==============>...............] - ETA: 55s - loss: 0.2627 - categorical_accuracy: 0.9176
30688/60000 [==============>...............] - ETA: 55s - loss: 0.2625 - categorical_accuracy: 0.9177
30720/60000 [==============>...............] - ETA: 55s - loss: 0.2624 - categorical_accuracy: 0.9176
30752/60000 [==============>...............] - ETA: 55s - loss: 0.2622 - categorical_accuracy: 0.9177
30784/60000 [==============>...............] - ETA: 55s - loss: 0.2620 - categorical_accuracy: 0.9178
30816/60000 [==============>...............] - ETA: 55s - loss: 0.2620 - categorical_accuracy: 0.9178
30848/60000 [==============>...............] - ETA: 55s - loss: 0.2618 - categorical_accuracy: 0.9179
30880/60000 [==============>...............] - ETA: 55s - loss: 0.2617 - categorical_accuracy: 0.9179
30912/60000 [==============>...............] - ETA: 55s - loss: 0.2619 - categorical_accuracy: 0.9179
30944/60000 [==============>...............] - ETA: 55s - loss: 0.2619 - categorical_accuracy: 0.9179
30976/60000 [==============>...............] - ETA: 54s - loss: 0.2617 - categorical_accuracy: 0.9180
31008/60000 [==============>...............] - ETA: 54s - loss: 0.2617 - categorical_accuracy: 0.9180
31040/60000 [==============>...............] - ETA: 54s - loss: 0.2614 - categorical_accuracy: 0.9181
31072/60000 [==============>...............] - ETA: 54s - loss: 0.2612 - categorical_accuracy: 0.9182
31104/60000 [==============>...............] - ETA: 54s - loss: 0.2611 - categorical_accuracy: 0.9182
31136/60000 [==============>...............] - ETA: 54s - loss: 0.2611 - categorical_accuracy: 0.9182
31168/60000 [==============>...............] - ETA: 54s - loss: 0.2611 - categorical_accuracy: 0.9182
31200/60000 [==============>...............] - ETA: 54s - loss: 0.2609 - categorical_accuracy: 0.9182
31232/60000 [==============>...............] - ETA: 54s - loss: 0.2607 - categorical_accuracy: 0.9183
31264/60000 [==============>...............] - ETA: 54s - loss: 0.2606 - categorical_accuracy: 0.9183
31296/60000 [==============>...............] - ETA: 54s - loss: 0.2604 - categorical_accuracy: 0.9184
31328/60000 [==============>...............] - ETA: 54s - loss: 0.2602 - categorical_accuracy: 0.9184
31360/60000 [==============>...............] - ETA: 54s - loss: 0.2599 - categorical_accuracy: 0.9185
31392/60000 [==============>...............] - ETA: 54s - loss: 0.2601 - categorical_accuracy: 0.9185
31424/60000 [==============>...............] - ETA: 54s - loss: 0.2599 - categorical_accuracy: 0.9186
31456/60000 [==============>...............] - ETA: 54s - loss: 0.2598 - categorical_accuracy: 0.9187
31488/60000 [==============>...............] - ETA: 54s - loss: 0.2597 - categorical_accuracy: 0.9187
31520/60000 [==============>...............] - ETA: 53s - loss: 0.2597 - categorical_accuracy: 0.9187
31552/60000 [==============>...............] - ETA: 53s - loss: 0.2598 - categorical_accuracy: 0.9187
31584/60000 [==============>...............] - ETA: 53s - loss: 0.2596 - categorical_accuracy: 0.9188
31616/60000 [==============>...............] - ETA: 53s - loss: 0.2597 - categorical_accuracy: 0.9188
31648/60000 [==============>...............] - ETA: 53s - loss: 0.2595 - categorical_accuracy: 0.9189
31680/60000 [==============>...............] - ETA: 53s - loss: 0.2593 - categorical_accuracy: 0.9189
31712/60000 [==============>...............] - ETA: 53s - loss: 0.2593 - categorical_accuracy: 0.9189
31744/60000 [==============>...............] - ETA: 53s - loss: 0.2593 - categorical_accuracy: 0.9189
31776/60000 [==============>...............] - ETA: 53s - loss: 0.2592 - categorical_accuracy: 0.9190
31808/60000 [==============>...............] - ETA: 53s - loss: 0.2590 - categorical_accuracy: 0.9190
31840/60000 [==============>...............] - ETA: 53s - loss: 0.2588 - categorical_accuracy: 0.9191
31872/60000 [==============>...............] - ETA: 53s - loss: 0.2588 - categorical_accuracy: 0.9190
31904/60000 [==============>...............] - ETA: 53s - loss: 0.2590 - categorical_accuracy: 0.9190
31936/60000 [==============>...............] - ETA: 53s - loss: 0.2588 - categorical_accuracy: 0.9191
31968/60000 [==============>...............] - ETA: 53s - loss: 0.2587 - categorical_accuracy: 0.9191
32000/60000 [===============>..............] - ETA: 53s - loss: 0.2586 - categorical_accuracy: 0.9191
32032/60000 [===============>..............] - ETA: 52s - loss: 0.2584 - categorical_accuracy: 0.9192
32064/60000 [===============>..............] - ETA: 52s - loss: 0.2582 - categorical_accuracy: 0.9193
32096/60000 [===============>..............] - ETA: 52s - loss: 0.2580 - categorical_accuracy: 0.9193
32128/60000 [===============>..............] - ETA: 52s - loss: 0.2578 - categorical_accuracy: 0.9194
32160/60000 [===============>..............] - ETA: 52s - loss: 0.2577 - categorical_accuracy: 0.9194
32192/60000 [===============>..............] - ETA: 52s - loss: 0.2575 - categorical_accuracy: 0.9195
32224/60000 [===============>..............] - ETA: 52s - loss: 0.2573 - categorical_accuracy: 0.9196
32256/60000 [===============>..............] - ETA: 52s - loss: 0.2572 - categorical_accuracy: 0.9196
32288/60000 [===============>..............] - ETA: 52s - loss: 0.2571 - categorical_accuracy: 0.9196
32320/60000 [===============>..............] - ETA: 52s - loss: 0.2570 - categorical_accuracy: 0.9196
32352/60000 [===============>..............] - ETA: 52s - loss: 0.2570 - categorical_accuracy: 0.9197
32384/60000 [===============>..............] - ETA: 52s - loss: 0.2568 - categorical_accuracy: 0.9197
32416/60000 [===============>..............] - ETA: 52s - loss: 0.2566 - categorical_accuracy: 0.9198
32448/60000 [===============>..............] - ETA: 52s - loss: 0.2564 - categorical_accuracy: 0.9199
32480/60000 [===============>..............] - ETA: 52s - loss: 0.2562 - categorical_accuracy: 0.9199
32512/60000 [===============>..............] - ETA: 52s - loss: 0.2560 - categorical_accuracy: 0.9199
32544/60000 [===============>..............] - ETA: 51s - loss: 0.2559 - categorical_accuracy: 0.9200
32576/60000 [===============>..............] - ETA: 51s - loss: 0.2558 - categorical_accuracy: 0.9200
32608/60000 [===============>..............] - ETA: 51s - loss: 0.2556 - categorical_accuracy: 0.9201
32640/60000 [===============>..............] - ETA: 51s - loss: 0.2555 - categorical_accuracy: 0.9201
32672/60000 [===============>..............] - ETA: 51s - loss: 0.2553 - categorical_accuracy: 0.9202
32704/60000 [===============>..............] - ETA: 51s - loss: 0.2551 - categorical_accuracy: 0.9203
32736/60000 [===============>..............] - ETA: 51s - loss: 0.2550 - categorical_accuracy: 0.9203
32768/60000 [===============>..............] - ETA: 51s - loss: 0.2548 - categorical_accuracy: 0.9204
32800/60000 [===============>..............] - ETA: 51s - loss: 0.2547 - categorical_accuracy: 0.9204
32832/60000 [===============>..............] - ETA: 51s - loss: 0.2544 - categorical_accuracy: 0.9205
32864/60000 [===============>..............] - ETA: 51s - loss: 0.2543 - categorical_accuracy: 0.9205
32896/60000 [===============>..............] - ETA: 51s - loss: 0.2541 - categorical_accuracy: 0.9206
32928/60000 [===============>..............] - ETA: 51s - loss: 0.2541 - categorical_accuracy: 0.9206
32960/60000 [===============>..............] - ETA: 51s - loss: 0.2544 - categorical_accuracy: 0.9207
32992/60000 [===============>..............] - ETA: 51s - loss: 0.2544 - categorical_accuracy: 0.9206
33024/60000 [===============>..............] - ETA: 51s - loss: 0.2542 - categorical_accuracy: 0.9207
33056/60000 [===============>..............] - ETA: 51s - loss: 0.2541 - categorical_accuracy: 0.9207
33088/60000 [===============>..............] - ETA: 50s - loss: 0.2539 - categorical_accuracy: 0.9207
33120/60000 [===============>..............] - ETA: 50s - loss: 0.2538 - categorical_accuracy: 0.9208
33152/60000 [===============>..............] - ETA: 50s - loss: 0.2536 - categorical_accuracy: 0.9208
33184/60000 [===============>..............] - ETA: 50s - loss: 0.2537 - categorical_accuracy: 0.9208
33216/60000 [===============>..............] - ETA: 50s - loss: 0.2535 - categorical_accuracy: 0.9209
33248/60000 [===============>..............] - ETA: 50s - loss: 0.2533 - categorical_accuracy: 0.9209
33280/60000 [===============>..............] - ETA: 50s - loss: 0.2534 - categorical_accuracy: 0.9209
33312/60000 [===============>..............] - ETA: 50s - loss: 0.2532 - categorical_accuracy: 0.9210
33344/60000 [===============>..............] - ETA: 50s - loss: 0.2531 - categorical_accuracy: 0.9211
33376/60000 [===============>..............] - ETA: 50s - loss: 0.2531 - categorical_accuracy: 0.9210
33408/60000 [===============>..............] - ETA: 50s - loss: 0.2530 - categorical_accuracy: 0.9211
33440/60000 [===============>..............] - ETA: 50s - loss: 0.2528 - categorical_accuracy: 0.9212
33472/60000 [===============>..............] - ETA: 50s - loss: 0.2527 - categorical_accuracy: 0.9212
33504/60000 [===============>..............] - ETA: 50s - loss: 0.2525 - categorical_accuracy: 0.9212
33536/60000 [===============>..............] - ETA: 50s - loss: 0.2523 - categorical_accuracy: 0.9213
33568/60000 [===============>..............] - ETA: 50s - loss: 0.2522 - categorical_accuracy: 0.9213
33600/60000 [===============>..............] - ETA: 49s - loss: 0.2520 - categorical_accuracy: 0.9214
33632/60000 [===============>..............] - ETA: 49s - loss: 0.2518 - categorical_accuracy: 0.9214
33664/60000 [===============>..............] - ETA: 49s - loss: 0.2519 - categorical_accuracy: 0.9214
33696/60000 [===============>..............] - ETA: 49s - loss: 0.2519 - categorical_accuracy: 0.9214
33728/60000 [===============>..............] - ETA: 49s - loss: 0.2520 - categorical_accuracy: 0.9214
33760/60000 [===============>..............] - ETA: 49s - loss: 0.2518 - categorical_accuracy: 0.9215
33792/60000 [===============>..............] - ETA: 49s - loss: 0.2517 - categorical_accuracy: 0.9215
33824/60000 [===============>..............] - ETA: 49s - loss: 0.2515 - categorical_accuracy: 0.9216
33856/60000 [===============>..............] - ETA: 49s - loss: 0.2514 - categorical_accuracy: 0.9216
33888/60000 [===============>..............] - ETA: 49s - loss: 0.2512 - categorical_accuracy: 0.9217
33920/60000 [===============>..............] - ETA: 49s - loss: 0.2510 - categorical_accuracy: 0.9218
33952/60000 [===============>..............] - ETA: 49s - loss: 0.2508 - categorical_accuracy: 0.9218
33984/60000 [===============>..............] - ETA: 49s - loss: 0.2507 - categorical_accuracy: 0.9218
34016/60000 [================>.............] - ETA: 49s - loss: 0.2505 - categorical_accuracy: 0.9219
34048/60000 [================>.............] - ETA: 49s - loss: 0.2505 - categorical_accuracy: 0.9219
34080/60000 [================>.............] - ETA: 49s - loss: 0.2504 - categorical_accuracy: 0.9219
34112/60000 [================>.............] - ETA: 49s - loss: 0.2504 - categorical_accuracy: 0.9219
34144/60000 [================>.............] - ETA: 48s - loss: 0.2502 - categorical_accuracy: 0.9219
34176/60000 [================>.............] - ETA: 48s - loss: 0.2503 - categorical_accuracy: 0.9219
34208/60000 [================>.............] - ETA: 48s - loss: 0.2501 - categorical_accuracy: 0.9219
34240/60000 [================>.............] - ETA: 48s - loss: 0.2501 - categorical_accuracy: 0.9220
34272/60000 [================>.............] - ETA: 48s - loss: 0.2500 - categorical_accuracy: 0.9219
34304/60000 [================>.............] - ETA: 48s - loss: 0.2499 - categorical_accuracy: 0.9220
34336/60000 [================>.............] - ETA: 48s - loss: 0.2497 - categorical_accuracy: 0.9221
34368/60000 [================>.............] - ETA: 48s - loss: 0.2498 - categorical_accuracy: 0.9221
34400/60000 [================>.............] - ETA: 48s - loss: 0.2498 - categorical_accuracy: 0.9222
34432/60000 [================>.............] - ETA: 48s - loss: 0.2498 - categorical_accuracy: 0.9222
34464/60000 [================>.............] - ETA: 48s - loss: 0.2496 - categorical_accuracy: 0.9222
34496/60000 [================>.............] - ETA: 48s - loss: 0.2496 - categorical_accuracy: 0.9223
34528/60000 [================>.............] - ETA: 48s - loss: 0.2496 - categorical_accuracy: 0.9223
34560/60000 [================>.............] - ETA: 48s - loss: 0.2494 - categorical_accuracy: 0.9223
34592/60000 [================>.............] - ETA: 48s - loss: 0.2493 - categorical_accuracy: 0.9224
34624/60000 [================>.............] - ETA: 48s - loss: 0.2493 - categorical_accuracy: 0.9224
34656/60000 [================>.............] - ETA: 47s - loss: 0.2491 - categorical_accuracy: 0.9225
34688/60000 [================>.............] - ETA: 47s - loss: 0.2489 - categorical_accuracy: 0.9225
34720/60000 [================>.............] - ETA: 47s - loss: 0.2487 - categorical_accuracy: 0.9226
34752/60000 [================>.............] - ETA: 47s - loss: 0.2489 - categorical_accuracy: 0.9226
34784/60000 [================>.............] - ETA: 47s - loss: 0.2488 - categorical_accuracy: 0.9226
34816/60000 [================>.............] - ETA: 47s - loss: 0.2487 - categorical_accuracy: 0.9227
34848/60000 [================>.............] - ETA: 47s - loss: 0.2484 - categorical_accuracy: 0.9227
34880/60000 [================>.............] - ETA: 47s - loss: 0.2483 - categorical_accuracy: 0.9228
34912/60000 [================>.............] - ETA: 47s - loss: 0.2482 - categorical_accuracy: 0.9228
34944/60000 [================>.............] - ETA: 47s - loss: 0.2480 - categorical_accuracy: 0.9229
34976/60000 [================>.............] - ETA: 47s - loss: 0.2479 - categorical_accuracy: 0.9229
35008/60000 [================>.............] - ETA: 47s - loss: 0.2483 - categorical_accuracy: 0.9228
35040/60000 [================>.............] - ETA: 47s - loss: 0.2483 - categorical_accuracy: 0.9228
35072/60000 [================>.............] - ETA: 47s - loss: 0.2483 - categorical_accuracy: 0.9228
35104/60000 [================>.............] - ETA: 47s - loss: 0.2481 - categorical_accuracy: 0.9228
35136/60000 [================>.............] - ETA: 47s - loss: 0.2479 - categorical_accuracy: 0.9229
35168/60000 [================>.............] - ETA: 47s - loss: 0.2477 - categorical_accuracy: 0.9230
35200/60000 [================>.............] - ETA: 46s - loss: 0.2476 - categorical_accuracy: 0.9230
35232/60000 [================>.............] - ETA: 46s - loss: 0.2475 - categorical_accuracy: 0.9231
35264/60000 [================>.............] - ETA: 46s - loss: 0.2473 - categorical_accuracy: 0.9231
35296/60000 [================>.............] - ETA: 46s - loss: 0.2472 - categorical_accuracy: 0.9232
35328/60000 [================>.............] - ETA: 46s - loss: 0.2470 - categorical_accuracy: 0.9233
35360/60000 [================>.............] - ETA: 46s - loss: 0.2468 - categorical_accuracy: 0.9233
35392/60000 [================>.............] - ETA: 46s - loss: 0.2467 - categorical_accuracy: 0.9233
35424/60000 [================>.............] - ETA: 46s - loss: 0.2468 - categorical_accuracy: 0.9233
35456/60000 [================>.............] - ETA: 46s - loss: 0.2467 - categorical_accuracy: 0.9233
35488/60000 [================>.............] - ETA: 46s - loss: 0.2467 - categorical_accuracy: 0.9234
35520/60000 [================>.............] - ETA: 46s - loss: 0.2466 - categorical_accuracy: 0.9234
35552/60000 [================>.............] - ETA: 46s - loss: 0.2464 - categorical_accuracy: 0.9234
35584/60000 [================>.............] - ETA: 46s - loss: 0.2463 - categorical_accuracy: 0.9235
35616/60000 [================>.............] - ETA: 46s - loss: 0.2462 - categorical_accuracy: 0.9235
35648/60000 [================>.............] - ETA: 46s - loss: 0.2460 - categorical_accuracy: 0.9236
35680/60000 [================>.............] - ETA: 46s - loss: 0.2460 - categorical_accuracy: 0.9236
35712/60000 [================>.............] - ETA: 45s - loss: 0.2458 - categorical_accuracy: 0.9236
35744/60000 [================>.............] - ETA: 45s - loss: 0.2457 - categorical_accuracy: 0.9236
35776/60000 [================>.............] - ETA: 45s - loss: 0.2456 - categorical_accuracy: 0.9237
35808/60000 [================>.............] - ETA: 45s - loss: 0.2455 - categorical_accuracy: 0.9237
35840/60000 [================>.............] - ETA: 45s - loss: 0.2453 - categorical_accuracy: 0.9238
35872/60000 [================>.............] - ETA: 45s - loss: 0.2451 - categorical_accuracy: 0.9238
35904/60000 [================>.............] - ETA: 45s - loss: 0.2450 - categorical_accuracy: 0.9239
35936/60000 [================>.............] - ETA: 45s - loss: 0.2448 - categorical_accuracy: 0.9239
35968/60000 [================>.............] - ETA: 45s - loss: 0.2448 - categorical_accuracy: 0.9240
36000/60000 [=================>............] - ETA: 45s - loss: 0.2447 - categorical_accuracy: 0.9240
36032/60000 [=================>............] - ETA: 45s - loss: 0.2445 - categorical_accuracy: 0.9241
36064/60000 [=================>............] - ETA: 45s - loss: 0.2443 - categorical_accuracy: 0.9241
36096/60000 [=================>............] - ETA: 45s - loss: 0.2441 - categorical_accuracy: 0.9242
36128/60000 [=================>............] - ETA: 45s - loss: 0.2440 - categorical_accuracy: 0.9242
36160/60000 [=================>............] - ETA: 45s - loss: 0.2439 - categorical_accuracy: 0.9243
36192/60000 [=================>............] - ETA: 45s - loss: 0.2438 - categorical_accuracy: 0.9243
36224/60000 [=================>............] - ETA: 44s - loss: 0.2437 - categorical_accuracy: 0.9243
36256/60000 [=================>............] - ETA: 44s - loss: 0.2436 - categorical_accuracy: 0.9243
36288/60000 [=================>............] - ETA: 44s - loss: 0.2434 - categorical_accuracy: 0.9244
36320/60000 [=================>............] - ETA: 44s - loss: 0.2432 - categorical_accuracy: 0.9245
36352/60000 [=================>............] - ETA: 44s - loss: 0.2432 - categorical_accuracy: 0.9245
36384/60000 [=================>............] - ETA: 44s - loss: 0.2431 - categorical_accuracy: 0.9245
36416/60000 [=================>............] - ETA: 44s - loss: 0.2429 - categorical_accuracy: 0.9246
36448/60000 [=================>............] - ETA: 44s - loss: 0.2427 - categorical_accuracy: 0.9247
36480/60000 [=================>............] - ETA: 44s - loss: 0.2426 - categorical_accuracy: 0.9247
36512/60000 [=================>............] - ETA: 44s - loss: 0.2425 - categorical_accuracy: 0.9247
36544/60000 [=================>............] - ETA: 44s - loss: 0.2423 - categorical_accuracy: 0.9248
36576/60000 [=================>............] - ETA: 44s - loss: 0.2421 - categorical_accuracy: 0.9248
36608/60000 [=================>............] - ETA: 44s - loss: 0.2419 - categorical_accuracy: 0.9249
36640/60000 [=================>............] - ETA: 44s - loss: 0.2419 - categorical_accuracy: 0.9249
36672/60000 [=================>............] - ETA: 44s - loss: 0.2421 - categorical_accuracy: 0.9249
36704/60000 [=================>............] - ETA: 44s - loss: 0.2420 - categorical_accuracy: 0.9249
36736/60000 [=================>............] - ETA: 44s - loss: 0.2419 - categorical_accuracy: 0.9250
36768/60000 [=================>............] - ETA: 43s - loss: 0.2418 - categorical_accuracy: 0.9250
36800/60000 [=================>............] - ETA: 43s - loss: 0.2416 - categorical_accuracy: 0.9251
36832/60000 [=================>............] - ETA: 43s - loss: 0.2414 - categorical_accuracy: 0.9251
36864/60000 [=================>............] - ETA: 43s - loss: 0.2413 - categorical_accuracy: 0.9252
36896/60000 [=================>............] - ETA: 43s - loss: 0.2411 - categorical_accuracy: 0.9252
36928/60000 [=================>............] - ETA: 43s - loss: 0.2411 - categorical_accuracy: 0.9252
36960/60000 [=================>............] - ETA: 43s - loss: 0.2410 - categorical_accuracy: 0.9253
36992/60000 [=================>............] - ETA: 43s - loss: 0.2408 - categorical_accuracy: 0.9253
37024/60000 [=================>............] - ETA: 43s - loss: 0.2408 - categorical_accuracy: 0.9253
37056/60000 [=================>............] - ETA: 43s - loss: 0.2406 - categorical_accuracy: 0.9254
37088/60000 [=================>............] - ETA: 43s - loss: 0.2404 - categorical_accuracy: 0.9254
37120/60000 [=================>............] - ETA: 43s - loss: 0.2403 - categorical_accuracy: 0.9255
37152/60000 [=================>............] - ETA: 43s - loss: 0.2401 - categorical_accuracy: 0.9255
37184/60000 [=================>............] - ETA: 43s - loss: 0.2402 - categorical_accuracy: 0.9255
37216/60000 [=================>............] - ETA: 43s - loss: 0.2401 - categorical_accuracy: 0.9255
37248/60000 [=================>............] - ETA: 43s - loss: 0.2400 - categorical_accuracy: 0.9256
37280/60000 [=================>............] - ETA: 43s - loss: 0.2398 - categorical_accuracy: 0.9256
37312/60000 [=================>............] - ETA: 42s - loss: 0.2397 - categorical_accuracy: 0.9256
37344/60000 [=================>............] - ETA: 42s - loss: 0.2398 - categorical_accuracy: 0.9256
37376/60000 [=================>............] - ETA: 42s - loss: 0.2396 - categorical_accuracy: 0.9257
37408/60000 [=================>............] - ETA: 42s - loss: 0.2395 - categorical_accuracy: 0.9257
37440/60000 [=================>............] - ETA: 42s - loss: 0.2394 - categorical_accuracy: 0.9257
37472/60000 [=================>............] - ETA: 42s - loss: 0.2394 - categorical_accuracy: 0.9258
37504/60000 [=================>............] - ETA: 42s - loss: 0.2392 - categorical_accuracy: 0.9258
37536/60000 [=================>............] - ETA: 42s - loss: 0.2390 - categorical_accuracy: 0.9259
37568/60000 [=================>............] - ETA: 42s - loss: 0.2389 - categorical_accuracy: 0.9259
37600/60000 [=================>............] - ETA: 42s - loss: 0.2388 - categorical_accuracy: 0.9259
37632/60000 [=================>............] - ETA: 42s - loss: 0.2387 - categorical_accuracy: 0.9260
37664/60000 [=================>............] - ETA: 42s - loss: 0.2387 - categorical_accuracy: 0.9260
37696/60000 [=================>............] - ETA: 42s - loss: 0.2386 - categorical_accuracy: 0.9260
37728/60000 [=================>............] - ETA: 42s - loss: 0.2385 - categorical_accuracy: 0.9260
37760/60000 [=================>............] - ETA: 42s - loss: 0.2383 - categorical_accuracy: 0.9261
37792/60000 [=================>............] - ETA: 42s - loss: 0.2381 - categorical_accuracy: 0.9261
37824/60000 [=================>............] - ETA: 41s - loss: 0.2380 - categorical_accuracy: 0.9262
37856/60000 [=================>............] - ETA: 41s - loss: 0.2379 - categorical_accuracy: 0.9262
37888/60000 [=================>............] - ETA: 41s - loss: 0.2378 - categorical_accuracy: 0.9263
37920/60000 [=================>............] - ETA: 41s - loss: 0.2376 - categorical_accuracy: 0.9263
37952/60000 [=================>............] - ETA: 41s - loss: 0.2374 - categorical_accuracy: 0.9264
37984/60000 [=================>............] - ETA: 41s - loss: 0.2373 - categorical_accuracy: 0.9264
38016/60000 [==================>...........] - ETA: 41s - loss: 0.2373 - categorical_accuracy: 0.9264
38048/60000 [==================>...........] - ETA: 41s - loss: 0.2371 - categorical_accuracy: 0.9265
38080/60000 [==================>...........] - ETA: 41s - loss: 0.2370 - categorical_accuracy: 0.9265
38112/60000 [==================>...........] - ETA: 41s - loss: 0.2371 - categorical_accuracy: 0.9265
38144/60000 [==================>...........] - ETA: 41s - loss: 0.2369 - categorical_accuracy: 0.9265
38176/60000 [==================>...........] - ETA: 41s - loss: 0.2368 - categorical_accuracy: 0.9266
38208/60000 [==================>...........] - ETA: 41s - loss: 0.2367 - categorical_accuracy: 0.9266
38240/60000 [==================>...........] - ETA: 41s - loss: 0.2365 - categorical_accuracy: 0.9267
38272/60000 [==================>...........] - ETA: 41s - loss: 0.2365 - categorical_accuracy: 0.9267
38304/60000 [==================>...........] - ETA: 41s - loss: 0.2364 - categorical_accuracy: 0.9267
38336/60000 [==================>...........] - ETA: 41s - loss: 0.2363 - categorical_accuracy: 0.9267
38368/60000 [==================>...........] - ETA: 40s - loss: 0.2364 - categorical_accuracy: 0.9267
38400/60000 [==================>...........] - ETA: 40s - loss: 0.2365 - categorical_accuracy: 0.9267
38432/60000 [==================>...........] - ETA: 40s - loss: 0.2363 - categorical_accuracy: 0.9267
38464/60000 [==================>...........] - ETA: 40s - loss: 0.2361 - categorical_accuracy: 0.9268
38496/60000 [==================>...........] - ETA: 40s - loss: 0.2362 - categorical_accuracy: 0.9268
38528/60000 [==================>...........] - ETA: 40s - loss: 0.2361 - categorical_accuracy: 0.9268
38560/60000 [==================>...........] - ETA: 40s - loss: 0.2359 - categorical_accuracy: 0.9268
38592/60000 [==================>...........] - ETA: 40s - loss: 0.2357 - categorical_accuracy: 0.9269
38624/60000 [==================>...........] - ETA: 40s - loss: 0.2357 - categorical_accuracy: 0.9269
38656/60000 [==================>...........] - ETA: 40s - loss: 0.2356 - categorical_accuracy: 0.9269
38688/60000 [==================>...........] - ETA: 40s - loss: 0.2354 - categorical_accuracy: 0.9270
38720/60000 [==================>...........] - ETA: 40s - loss: 0.2352 - categorical_accuracy: 0.9270
38752/60000 [==================>...........] - ETA: 40s - loss: 0.2351 - categorical_accuracy: 0.9270
38784/60000 [==================>...........] - ETA: 40s - loss: 0.2351 - categorical_accuracy: 0.9271
38816/60000 [==================>...........] - ETA: 40s - loss: 0.2350 - categorical_accuracy: 0.9271
38848/60000 [==================>...........] - ETA: 40s - loss: 0.2348 - categorical_accuracy: 0.9271
38880/60000 [==================>...........] - ETA: 39s - loss: 0.2346 - categorical_accuracy: 0.9272
38912/60000 [==================>...........] - ETA: 39s - loss: 0.2346 - categorical_accuracy: 0.9272
38944/60000 [==================>...........] - ETA: 39s - loss: 0.2344 - categorical_accuracy: 0.9272
38976/60000 [==================>...........] - ETA: 39s - loss: 0.2343 - categorical_accuracy: 0.9273
39008/60000 [==================>...........] - ETA: 39s - loss: 0.2341 - categorical_accuracy: 0.9273
39040/60000 [==================>...........] - ETA: 39s - loss: 0.2342 - categorical_accuracy: 0.9274
39072/60000 [==================>...........] - ETA: 39s - loss: 0.2341 - categorical_accuracy: 0.9274
39104/60000 [==================>...........] - ETA: 39s - loss: 0.2340 - categorical_accuracy: 0.9274
39136/60000 [==================>...........] - ETA: 39s - loss: 0.2339 - categorical_accuracy: 0.9274
39168/60000 [==================>...........] - ETA: 39s - loss: 0.2338 - categorical_accuracy: 0.9274
39200/60000 [==================>...........] - ETA: 39s - loss: 0.2337 - categorical_accuracy: 0.9275
39232/60000 [==================>...........] - ETA: 39s - loss: 0.2336 - categorical_accuracy: 0.9275
39264/60000 [==================>...........] - ETA: 39s - loss: 0.2335 - categorical_accuracy: 0.9275
39296/60000 [==================>...........] - ETA: 39s - loss: 0.2335 - categorical_accuracy: 0.9276
39328/60000 [==================>...........] - ETA: 39s - loss: 0.2333 - categorical_accuracy: 0.9276
39360/60000 [==================>...........] - ETA: 39s - loss: 0.2331 - categorical_accuracy: 0.9277
39392/60000 [==================>...........] - ETA: 39s - loss: 0.2330 - categorical_accuracy: 0.9278
39424/60000 [==================>...........] - ETA: 38s - loss: 0.2328 - categorical_accuracy: 0.9278
39456/60000 [==================>...........] - ETA: 38s - loss: 0.2327 - categorical_accuracy: 0.9279
39488/60000 [==================>...........] - ETA: 38s - loss: 0.2327 - categorical_accuracy: 0.9279
39520/60000 [==================>...........] - ETA: 38s - loss: 0.2326 - categorical_accuracy: 0.9279
39552/60000 [==================>...........] - ETA: 38s - loss: 0.2324 - categorical_accuracy: 0.9280
39584/60000 [==================>...........] - ETA: 38s - loss: 0.2326 - categorical_accuracy: 0.9280
39616/60000 [==================>...........] - ETA: 38s - loss: 0.2324 - categorical_accuracy: 0.9281
39648/60000 [==================>...........] - ETA: 38s - loss: 0.2323 - categorical_accuracy: 0.9281
39680/60000 [==================>...........] - ETA: 38s - loss: 0.2322 - categorical_accuracy: 0.9282
39712/60000 [==================>...........] - ETA: 38s - loss: 0.2320 - categorical_accuracy: 0.9282
39744/60000 [==================>...........] - ETA: 38s - loss: 0.2319 - categorical_accuracy: 0.9282
39776/60000 [==================>...........] - ETA: 38s - loss: 0.2318 - categorical_accuracy: 0.9282
39808/60000 [==================>...........] - ETA: 38s - loss: 0.2317 - categorical_accuracy: 0.9283
39840/60000 [==================>...........] - ETA: 38s - loss: 0.2319 - categorical_accuracy: 0.9283
39872/60000 [==================>...........] - ETA: 38s - loss: 0.2319 - categorical_accuracy: 0.9282
39904/60000 [==================>...........] - ETA: 38s - loss: 0.2318 - categorical_accuracy: 0.9283
39936/60000 [==================>...........] - ETA: 37s - loss: 0.2317 - categorical_accuracy: 0.9283
39968/60000 [==================>...........] - ETA: 37s - loss: 0.2317 - categorical_accuracy: 0.9283
40000/60000 [===================>..........] - ETA: 37s - loss: 0.2315 - categorical_accuracy: 0.9283
40032/60000 [===================>..........] - ETA: 37s - loss: 0.2314 - categorical_accuracy: 0.9284
40064/60000 [===================>..........] - ETA: 37s - loss: 0.2314 - categorical_accuracy: 0.9284
40096/60000 [===================>..........] - ETA: 37s - loss: 0.2312 - categorical_accuracy: 0.9284
40128/60000 [===================>..........] - ETA: 37s - loss: 0.2311 - categorical_accuracy: 0.9285
40160/60000 [===================>..........] - ETA: 37s - loss: 0.2309 - categorical_accuracy: 0.9285
40192/60000 [===================>..........] - ETA: 37s - loss: 0.2309 - categorical_accuracy: 0.9285
40224/60000 [===================>..........] - ETA: 37s - loss: 0.2309 - categorical_accuracy: 0.9286
40256/60000 [===================>..........] - ETA: 37s - loss: 0.2307 - categorical_accuracy: 0.9286
40288/60000 [===================>..........] - ETA: 37s - loss: 0.2306 - categorical_accuracy: 0.9287
40320/60000 [===================>..........] - ETA: 37s - loss: 0.2304 - categorical_accuracy: 0.9287
40352/60000 [===================>..........] - ETA: 37s - loss: 0.2303 - categorical_accuracy: 0.9288
40384/60000 [===================>..........] - ETA: 37s - loss: 0.2301 - categorical_accuracy: 0.9288
40416/60000 [===================>..........] - ETA: 37s - loss: 0.2300 - categorical_accuracy: 0.9289
40448/60000 [===================>..........] - ETA: 36s - loss: 0.2299 - categorical_accuracy: 0.9289
40480/60000 [===================>..........] - ETA: 36s - loss: 0.2299 - categorical_accuracy: 0.9289
40512/60000 [===================>..........] - ETA: 36s - loss: 0.2298 - categorical_accuracy: 0.9290
40544/60000 [===================>..........] - ETA: 36s - loss: 0.2297 - categorical_accuracy: 0.9290
40576/60000 [===================>..........] - ETA: 36s - loss: 0.2295 - categorical_accuracy: 0.9290
40608/60000 [===================>..........] - ETA: 36s - loss: 0.2294 - categorical_accuracy: 0.9291
40640/60000 [===================>..........] - ETA: 36s - loss: 0.2293 - categorical_accuracy: 0.9291
40672/60000 [===================>..........] - ETA: 36s - loss: 0.2291 - categorical_accuracy: 0.9291
40704/60000 [===================>..........] - ETA: 36s - loss: 0.2289 - categorical_accuracy: 0.9292
40736/60000 [===================>..........] - ETA: 36s - loss: 0.2289 - categorical_accuracy: 0.9292
40768/60000 [===================>..........] - ETA: 36s - loss: 0.2288 - categorical_accuracy: 0.9292
40800/60000 [===================>..........] - ETA: 36s - loss: 0.2287 - categorical_accuracy: 0.9292
40832/60000 [===================>..........] - ETA: 36s - loss: 0.2288 - categorical_accuracy: 0.9292
40864/60000 [===================>..........] - ETA: 36s - loss: 0.2290 - categorical_accuracy: 0.9292
40896/60000 [===================>..........] - ETA: 36s - loss: 0.2288 - categorical_accuracy: 0.9293
40928/60000 [===================>..........] - ETA: 36s - loss: 0.2289 - categorical_accuracy: 0.9292
40960/60000 [===================>..........] - ETA: 36s - loss: 0.2289 - categorical_accuracy: 0.9293
40992/60000 [===================>..........] - ETA: 35s - loss: 0.2289 - categorical_accuracy: 0.9293
41024/60000 [===================>..........] - ETA: 35s - loss: 0.2288 - categorical_accuracy: 0.9293
41056/60000 [===================>..........] - ETA: 35s - loss: 0.2287 - categorical_accuracy: 0.9293
41088/60000 [===================>..........] - ETA: 35s - loss: 0.2288 - categorical_accuracy: 0.9293
41120/60000 [===================>..........] - ETA: 35s - loss: 0.2287 - categorical_accuracy: 0.9294
41152/60000 [===================>..........] - ETA: 35s - loss: 0.2286 - categorical_accuracy: 0.9294
41184/60000 [===================>..........] - ETA: 35s - loss: 0.2285 - categorical_accuracy: 0.9295
41216/60000 [===================>..........] - ETA: 35s - loss: 0.2285 - categorical_accuracy: 0.9294
41248/60000 [===================>..........] - ETA: 35s - loss: 0.2284 - categorical_accuracy: 0.9295
41280/60000 [===================>..........] - ETA: 35s - loss: 0.2284 - categorical_accuracy: 0.9294
41312/60000 [===================>..........] - ETA: 35s - loss: 0.2283 - categorical_accuracy: 0.9295
41344/60000 [===================>..........] - ETA: 35s - loss: 0.2282 - categorical_accuracy: 0.9295
41376/60000 [===================>..........] - ETA: 35s - loss: 0.2280 - categorical_accuracy: 0.9295
41408/60000 [===================>..........] - ETA: 35s - loss: 0.2279 - categorical_accuracy: 0.9296
41440/60000 [===================>..........] - ETA: 35s - loss: 0.2277 - categorical_accuracy: 0.9297
41472/60000 [===================>..........] - ETA: 35s - loss: 0.2277 - categorical_accuracy: 0.9297
41504/60000 [===================>..........] - ETA: 34s - loss: 0.2276 - categorical_accuracy: 0.9297
41536/60000 [===================>..........] - ETA: 34s - loss: 0.2274 - categorical_accuracy: 0.9298
41568/60000 [===================>..........] - ETA: 34s - loss: 0.2273 - categorical_accuracy: 0.9298
41600/60000 [===================>..........] - ETA: 34s - loss: 0.2274 - categorical_accuracy: 0.9298
41632/60000 [===================>..........] - ETA: 34s - loss: 0.2274 - categorical_accuracy: 0.9297
41664/60000 [===================>..........] - ETA: 34s - loss: 0.2274 - categorical_accuracy: 0.9297
41696/60000 [===================>..........] - ETA: 34s - loss: 0.2273 - categorical_accuracy: 0.9298
41728/60000 [===================>..........] - ETA: 34s - loss: 0.2272 - categorical_accuracy: 0.9298
41760/60000 [===================>..........] - ETA: 34s - loss: 0.2270 - categorical_accuracy: 0.9299
41792/60000 [===================>..........] - ETA: 34s - loss: 0.2269 - categorical_accuracy: 0.9299
41824/60000 [===================>..........] - ETA: 34s - loss: 0.2269 - categorical_accuracy: 0.9299
41856/60000 [===================>..........] - ETA: 34s - loss: 0.2267 - categorical_accuracy: 0.9299
41888/60000 [===================>..........] - ETA: 34s - loss: 0.2267 - categorical_accuracy: 0.9300
41920/60000 [===================>..........] - ETA: 34s - loss: 0.2266 - categorical_accuracy: 0.9300
41952/60000 [===================>..........] - ETA: 34s - loss: 0.2265 - categorical_accuracy: 0.9300
41984/60000 [===================>..........] - ETA: 34s - loss: 0.2263 - categorical_accuracy: 0.9301
42016/60000 [====================>.........] - ETA: 34s - loss: 0.2262 - categorical_accuracy: 0.9301
42048/60000 [====================>.........] - ETA: 33s - loss: 0.2262 - categorical_accuracy: 0.9301
42080/60000 [====================>.........] - ETA: 33s - loss: 0.2260 - categorical_accuracy: 0.9302
42112/60000 [====================>.........] - ETA: 33s - loss: 0.2259 - categorical_accuracy: 0.9302
42144/60000 [====================>.........] - ETA: 33s - loss: 0.2260 - categorical_accuracy: 0.9302
42176/60000 [====================>.........] - ETA: 33s - loss: 0.2259 - categorical_accuracy: 0.9302
42208/60000 [====================>.........] - ETA: 33s - loss: 0.2258 - categorical_accuracy: 0.9302
42240/60000 [====================>.........] - ETA: 33s - loss: 0.2257 - categorical_accuracy: 0.9303
42272/60000 [====================>.........] - ETA: 33s - loss: 0.2256 - categorical_accuracy: 0.9303
42304/60000 [====================>.........] - ETA: 33s - loss: 0.2254 - categorical_accuracy: 0.9303
42336/60000 [====================>.........] - ETA: 33s - loss: 0.2254 - categorical_accuracy: 0.9303
42368/60000 [====================>.........] - ETA: 33s - loss: 0.2254 - categorical_accuracy: 0.9304
42400/60000 [====================>.........] - ETA: 33s - loss: 0.2254 - categorical_accuracy: 0.9303
42432/60000 [====================>.........] - ETA: 33s - loss: 0.2255 - categorical_accuracy: 0.9303
42464/60000 [====================>.........] - ETA: 33s - loss: 0.2255 - categorical_accuracy: 0.9303
42496/60000 [====================>.........] - ETA: 33s - loss: 0.2253 - categorical_accuracy: 0.9303
42528/60000 [====================>.........] - ETA: 33s - loss: 0.2252 - categorical_accuracy: 0.9304
42560/60000 [====================>.........] - ETA: 32s - loss: 0.2251 - categorical_accuracy: 0.9304
42592/60000 [====================>.........] - ETA: 32s - loss: 0.2249 - categorical_accuracy: 0.9305
42624/60000 [====================>.........] - ETA: 32s - loss: 0.2247 - categorical_accuracy: 0.9305
42656/60000 [====================>.........] - ETA: 32s - loss: 0.2246 - categorical_accuracy: 0.9306
42688/60000 [====================>.........] - ETA: 32s - loss: 0.2244 - categorical_accuracy: 0.9306
42720/60000 [====================>.........] - ETA: 32s - loss: 0.2243 - categorical_accuracy: 0.9307
42752/60000 [====================>.........] - ETA: 32s - loss: 0.2242 - categorical_accuracy: 0.9306
42784/60000 [====================>.........] - ETA: 32s - loss: 0.2240 - categorical_accuracy: 0.9307
42816/60000 [====================>.........] - ETA: 32s - loss: 0.2239 - categorical_accuracy: 0.9308
42848/60000 [====================>.........] - ETA: 32s - loss: 0.2238 - categorical_accuracy: 0.9308
42880/60000 [====================>.........] - ETA: 32s - loss: 0.2238 - categorical_accuracy: 0.9308
42912/60000 [====================>.........] - ETA: 32s - loss: 0.2236 - categorical_accuracy: 0.9308
42944/60000 [====================>.........] - ETA: 32s - loss: 0.2237 - categorical_accuracy: 0.9308
42976/60000 [====================>.........] - ETA: 32s - loss: 0.2236 - categorical_accuracy: 0.9308
43008/60000 [====================>.........] - ETA: 32s - loss: 0.2235 - categorical_accuracy: 0.9309
43040/60000 [====================>.........] - ETA: 32s - loss: 0.2234 - categorical_accuracy: 0.9309
43072/60000 [====================>.........] - ETA: 31s - loss: 0.2234 - categorical_accuracy: 0.9309
43104/60000 [====================>.........] - ETA: 31s - loss: 0.2233 - categorical_accuracy: 0.9309
43136/60000 [====================>.........] - ETA: 31s - loss: 0.2232 - categorical_accuracy: 0.9309
43168/60000 [====================>.........] - ETA: 31s - loss: 0.2233 - categorical_accuracy: 0.9309
43200/60000 [====================>.........] - ETA: 31s - loss: 0.2234 - categorical_accuracy: 0.9309
43232/60000 [====================>.........] - ETA: 31s - loss: 0.2233 - categorical_accuracy: 0.9310
43264/60000 [====================>.........] - ETA: 31s - loss: 0.2231 - categorical_accuracy: 0.9310
43296/60000 [====================>.........] - ETA: 31s - loss: 0.2231 - categorical_accuracy: 0.9310
43328/60000 [====================>.........] - ETA: 31s - loss: 0.2230 - categorical_accuracy: 0.9311
43360/60000 [====================>.........] - ETA: 31s - loss: 0.2228 - categorical_accuracy: 0.9311
43392/60000 [====================>.........] - ETA: 31s - loss: 0.2227 - categorical_accuracy: 0.9312
43424/60000 [====================>.........] - ETA: 31s - loss: 0.2226 - categorical_accuracy: 0.9312
43456/60000 [====================>.........] - ETA: 31s - loss: 0.2227 - categorical_accuracy: 0.9311
43488/60000 [====================>.........] - ETA: 31s - loss: 0.2226 - categorical_accuracy: 0.9312
43520/60000 [====================>.........] - ETA: 31s - loss: 0.2226 - categorical_accuracy: 0.9312
43552/60000 [====================>.........] - ETA: 31s - loss: 0.2228 - categorical_accuracy: 0.9312
43584/60000 [====================>.........] - ETA: 31s - loss: 0.2227 - categorical_accuracy: 0.9312
43616/60000 [====================>.........] - ETA: 30s - loss: 0.2226 - categorical_accuracy: 0.9312
43648/60000 [====================>.........] - ETA: 30s - loss: 0.2224 - categorical_accuracy: 0.9312
43680/60000 [====================>.........] - ETA: 30s - loss: 0.2224 - categorical_accuracy: 0.9313
43712/60000 [====================>.........] - ETA: 30s - loss: 0.2223 - categorical_accuracy: 0.9313
43744/60000 [====================>.........] - ETA: 30s - loss: 0.2222 - categorical_accuracy: 0.9313
43776/60000 [====================>.........] - ETA: 30s - loss: 0.2222 - categorical_accuracy: 0.9313
43808/60000 [====================>.........] - ETA: 30s - loss: 0.2221 - categorical_accuracy: 0.9314
43840/60000 [====================>.........] - ETA: 30s - loss: 0.2220 - categorical_accuracy: 0.9314
43872/60000 [====================>.........] - ETA: 30s - loss: 0.2219 - categorical_accuracy: 0.9314
43904/60000 [====================>.........] - ETA: 30s - loss: 0.2218 - categorical_accuracy: 0.9315
43936/60000 [====================>.........] - ETA: 30s - loss: 0.2218 - categorical_accuracy: 0.9315
43968/60000 [====================>.........] - ETA: 30s - loss: 0.2217 - categorical_accuracy: 0.9315
44000/60000 [=====================>........] - ETA: 30s - loss: 0.2216 - categorical_accuracy: 0.9315
44032/60000 [=====================>........] - ETA: 30s - loss: 0.2216 - categorical_accuracy: 0.9315
44064/60000 [=====================>........] - ETA: 30s - loss: 0.2215 - categorical_accuracy: 0.9316
44096/60000 [=====================>........] - ETA: 30s - loss: 0.2214 - categorical_accuracy: 0.9316
44128/60000 [=====================>........] - ETA: 29s - loss: 0.2212 - categorical_accuracy: 0.9316
44160/60000 [=====================>........] - ETA: 29s - loss: 0.2211 - categorical_accuracy: 0.9317
44192/60000 [=====================>........] - ETA: 29s - loss: 0.2210 - categorical_accuracy: 0.9317
44224/60000 [=====================>........] - ETA: 29s - loss: 0.2209 - categorical_accuracy: 0.9317
44256/60000 [=====================>........] - ETA: 29s - loss: 0.2209 - categorical_accuracy: 0.9317
44288/60000 [=====================>........] - ETA: 29s - loss: 0.2209 - categorical_accuracy: 0.9317
44320/60000 [=====================>........] - ETA: 29s - loss: 0.2208 - categorical_accuracy: 0.9317
44352/60000 [=====================>........] - ETA: 29s - loss: 0.2207 - categorical_accuracy: 0.9318
44384/60000 [=====================>........] - ETA: 29s - loss: 0.2205 - categorical_accuracy: 0.9318
44416/60000 [=====================>........] - ETA: 29s - loss: 0.2204 - categorical_accuracy: 0.9318
44448/60000 [=====================>........] - ETA: 29s - loss: 0.2203 - categorical_accuracy: 0.9319
44480/60000 [=====================>........] - ETA: 29s - loss: 0.2202 - categorical_accuracy: 0.9319
44512/60000 [=====================>........] - ETA: 29s - loss: 0.2200 - categorical_accuracy: 0.9320
44544/60000 [=====================>........] - ETA: 29s - loss: 0.2200 - categorical_accuracy: 0.9320
44576/60000 [=====================>........] - ETA: 29s - loss: 0.2199 - categorical_accuracy: 0.9320
44608/60000 [=====================>........] - ETA: 29s - loss: 0.2198 - categorical_accuracy: 0.9320
44640/60000 [=====================>........] - ETA: 29s - loss: 0.2197 - categorical_accuracy: 0.9321
44672/60000 [=====================>........] - ETA: 28s - loss: 0.2197 - categorical_accuracy: 0.9321
44704/60000 [=====================>........] - ETA: 28s - loss: 0.2197 - categorical_accuracy: 0.9321
44736/60000 [=====================>........] - ETA: 28s - loss: 0.2195 - categorical_accuracy: 0.9321
44768/60000 [=====================>........] - ETA: 28s - loss: 0.2194 - categorical_accuracy: 0.9322
44800/60000 [=====================>........] - ETA: 28s - loss: 0.2193 - categorical_accuracy: 0.9322
44832/60000 [=====================>........] - ETA: 28s - loss: 0.2191 - categorical_accuracy: 0.9323
44864/60000 [=====================>........] - ETA: 28s - loss: 0.2191 - categorical_accuracy: 0.9323
44896/60000 [=====================>........] - ETA: 28s - loss: 0.2190 - categorical_accuracy: 0.9323
44928/60000 [=====================>........] - ETA: 28s - loss: 0.2189 - categorical_accuracy: 0.9323
44960/60000 [=====================>........] - ETA: 28s - loss: 0.2189 - categorical_accuracy: 0.9323
44992/60000 [=====================>........] - ETA: 28s - loss: 0.2188 - categorical_accuracy: 0.9324
45024/60000 [=====================>........] - ETA: 28s - loss: 0.2188 - categorical_accuracy: 0.9324
45056/60000 [=====================>........] - ETA: 28s - loss: 0.2187 - categorical_accuracy: 0.9324
45088/60000 [=====================>........] - ETA: 28s - loss: 0.2186 - categorical_accuracy: 0.9324
45120/60000 [=====================>........] - ETA: 28s - loss: 0.2184 - categorical_accuracy: 0.9325
45152/60000 [=====================>........] - ETA: 28s - loss: 0.2183 - categorical_accuracy: 0.9325
45184/60000 [=====================>........] - ETA: 27s - loss: 0.2181 - categorical_accuracy: 0.9326
45216/60000 [=====================>........] - ETA: 27s - loss: 0.2182 - categorical_accuracy: 0.9326
45248/60000 [=====================>........] - ETA: 27s - loss: 0.2181 - categorical_accuracy: 0.9325
45280/60000 [=====================>........] - ETA: 27s - loss: 0.2180 - categorical_accuracy: 0.9326
45312/60000 [=====================>........] - ETA: 27s - loss: 0.2179 - categorical_accuracy: 0.9326
45344/60000 [=====================>........] - ETA: 27s - loss: 0.2179 - categorical_accuracy: 0.9326
45376/60000 [=====================>........] - ETA: 27s - loss: 0.2178 - categorical_accuracy: 0.9327
45408/60000 [=====================>........] - ETA: 27s - loss: 0.2178 - categorical_accuracy: 0.9327
45440/60000 [=====================>........] - ETA: 27s - loss: 0.2176 - categorical_accuracy: 0.9327
45472/60000 [=====================>........] - ETA: 27s - loss: 0.2176 - categorical_accuracy: 0.9327
45504/60000 [=====================>........] - ETA: 27s - loss: 0.2175 - categorical_accuracy: 0.9327
45536/60000 [=====================>........] - ETA: 27s - loss: 0.2174 - categorical_accuracy: 0.9327
45568/60000 [=====================>........] - ETA: 27s - loss: 0.2173 - categorical_accuracy: 0.9328
45600/60000 [=====================>........] - ETA: 27s - loss: 0.2172 - categorical_accuracy: 0.9328
45632/60000 [=====================>........] - ETA: 27s - loss: 0.2171 - categorical_accuracy: 0.9328
45664/60000 [=====================>........] - ETA: 27s - loss: 0.2170 - categorical_accuracy: 0.9328
45696/60000 [=====================>........] - ETA: 27s - loss: 0.2169 - categorical_accuracy: 0.9329
45728/60000 [=====================>........] - ETA: 26s - loss: 0.2168 - categorical_accuracy: 0.9329
45760/60000 [=====================>........] - ETA: 26s - loss: 0.2167 - categorical_accuracy: 0.9329
45792/60000 [=====================>........] - ETA: 26s - loss: 0.2166 - categorical_accuracy: 0.9330
45824/60000 [=====================>........] - ETA: 26s - loss: 0.2165 - categorical_accuracy: 0.9330
45856/60000 [=====================>........] - ETA: 26s - loss: 0.2164 - categorical_accuracy: 0.9330
45888/60000 [=====================>........] - ETA: 26s - loss: 0.2162 - categorical_accuracy: 0.9331
45920/60000 [=====================>........] - ETA: 26s - loss: 0.2161 - categorical_accuracy: 0.9331
45952/60000 [=====================>........] - ETA: 26s - loss: 0.2160 - categorical_accuracy: 0.9331
45984/60000 [=====================>........] - ETA: 26s - loss: 0.2159 - categorical_accuracy: 0.9332
46016/60000 [======================>.......] - ETA: 26s - loss: 0.2158 - categorical_accuracy: 0.9332
46048/60000 [======================>.......] - ETA: 26s - loss: 0.2156 - categorical_accuracy: 0.9333
46080/60000 [======================>.......] - ETA: 26s - loss: 0.2155 - categorical_accuracy: 0.9333
46112/60000 [======================>.......] - ETA: 26s - loss: 0.2154 - categorical_accuracy: 0.9333
46144/60000 [======================>.......] - ETA: 26s - loss: 0.2153 - categorical_accuracy: 0.9334
46176/60000 [======================>.......] - ETA: 26s - loss: 0.2152 - categorical_accuracy: 0.9334
46208/60000 [======================>.......] - ETA: 26s - loss: 0.2151 - categorical_accuracy: 0.9334
46240/60000 [======================>.......] - ETA: 25s - loss: 0.2150 - categorical_accuracy: 0.9334
46272/60000 [======================>.......] - ETA: 25s - loss: 0.2150 - categorical_accuracy: 0.9334
46304/60000 [======================>.......] - ETA: 25s - loss: 0.2149 - categorical_accuracy: 0.9335
46336/60000 [======================>.......] - ETA: 25s - loss: 0.2147 - categorical_accuracy: 0.9335
46368/60000 [======================>.......] - ETA: 25s - loss: 0.2147 - categorical_accuracy: 0.9335
46400/60000 [======================>.......] - ETA: 25s - loss: 0.2145 - categorical_accuracy: 0.9336
46432/60000 [======================>.......] - ETA: 25s - loss: 0.2144 - categorical_accuracy: 0.9336
46464/60000 [======================>.......] - ETA: 25s - loss: 0.2144 - categorical_accuracy: 0.9336
46496/60000 [======================>.......] - ETA: 25s - loss: 0.2144 - categorical_accuracy: 0.9336
46528/60000 [======================>.......] - ETA: 25s - loss: 0.2144 - categorical_accuracy: 0.9336
46560/60000 [======================>.......] - ETA: 25s - loss: 0.2144 - categorical_accuracy: 0.9336
46592/60000 [======================>.......] - ETA: 25s - loss: 0.2142 - categorical_accuracy: 0.9336
46624/60000 [======================>.......] - ETA: 25s - loss: 0.2141 - categorical_accuracy: 0.9337
46656/60000 [======================>.......] - ETA: 25s - loss: 0.2140 - categorical_accuracy: 0.9337
46688/60000 [======================>.......] - ETA: 25s - loss: 0.2139 - categorical_accuracy: 0.9337
46720/60000 [======================>.......] - ETA: 25s - loss: 0.2138 - categorical_accuracy: 0.9338
46752/60000 [======================>.......] - ETA: 25s - loss: 0.2138 - categorical_accuracy: 0.9338
46784/60000 [======================>.......] - ETA: 24s - loss: 0.2137 - categorical_accuracy: 0.9338
46816/60000 [======================>.......] - ETA: 24s - loss: 0.2137 - categorical_accuracy: 0.9338
46848/60000 [======================>.......] - ETA: 24s - loss: 0.2137 - categorical_accuracy: 0.9338
46880/60000 [======================>.......] - ETA: 24s - loss: 0.2136 - categorical_accuracy: 0.9338
46912/60000 [======================>.......] - ETA: 24s - loss: 0.2135 - categorical_accuracy: 0.9339
46944/60000 [======================>.......] - ETA: 24s - loss: 0.2135 - categorical_accuracy: 0.9339
46976/60000 [======================>.......] - ETA: 24s - loss: 0.2134 - categorical_accuracy: 0.9339
47008/60000 [======================>.......] - ETA: 24s - loss: 0.2136 - categorical_accuracy: 0.9338
47040/60000 [======================>.......] - ETA: 24s - loss: 0.2136 - categorical_accuracy: 0.9338
47072/60000 [======================>.......] - ETA: 24s - loss: 0.2136 - categorical_accuracy: 0.9338
47104/60000 [======================>.......] - ETA: 24s - loss: 0.2135 - categorical_accuracy: 0.9339
47136/60000 [======================>.......] - ETA: 24s - loss: 0.2134 - categorical_accuracy: 0.9339
47168/60000 [======================>.......] - ETA: 24s - loss: 0.2133 - categorical_accuracy: 0.9339
47200/60000 [======================>.......] - ETA: 24s - loss: 0.2132 - categorical_accuracy: 0.9340
47232/60000 [======================>.......] - ETA: 24s - loss: 0.2130 - categorical_accuracy: 0.9340
47264/60000 [======================>.......] - ETA: 24s - loss: 0.2129 - categorical_accuracy: 0.9341
47296/60000 [======================>.......] - ETA: 23s - loss: 0.2128 - categorical_accuracy: 0.9341
47328/60000 [======================>.......] - ETA: 23s - loss: 0.2127 - categorical_accuracy: 0.9341
47360/60000 [======================>.......] - ETA: 23s - loss: 0.2126 - categorical_accuracy: 0.9342
47392/60000 [======================>.......] - ETA: 23s - loss: 0.2125 - categorical_accuracy: 0.9342
47424/60000 [======================>.......] - ETA: 23s - loss: 0.2123 - categorical_accuracy: 0.9343
47456/60000 [======================>.......] - ETA: 23s - loss: 0.2123 - categorical_accuracy: 0.9343
47488/60000 [======================>.......] - ETA: 23s - loss: 0.2124 - categorical_accuracy: 0.9343
47520/60000 [======================>.......] - ETA: 23s - loss: 0.2122 - categorical_accuracy: 0.9343
47552/60000 [======================>.......] - ETA: 23s - loss: 0.2121 - categorical_accuracy: 0.9343
47584/60000 [======================>.......] - ETA: 23s - loss: 0.2120 - categorical_accuracy: 0.9344
47616/60000 [======================>.......] - ETA: 23s - loss: 0.2119 - categorical_accuracy: 0.9344
47648/60000 [======================>.......] - ETA: 23s - loss: 0.2118 - categorical_accuracy: 0.9344
47680/60000 [======================>.......] - ETA: 23s - loss: 0.2117 - categorical_accuracy: 0.9344
47712/60000 [======================>.......] - ETA: 23s - loss: 0.2116 - categorical_accuracy: 0.9345
47744/60000 [======================>.......] - ETA: 23s - loss: 0.2115 - categorical_accuracy: 0.9345
47776/60000 [======================>.......] - ETA: 23s - loss: 0.2114 - categorical_accuracy: 0.9345
47808/60000 [======================>.......] - ETA: 23s - loss: 0.2113 - categorical_accuracy: 0.9346
47840/60000 [======================>.......] - ETA: 22s - loss: 0.2113 - categorical_accuracy: 0.9346
47872/60000 [======================>.......] - ETA: 22s - loss: 0.2112 - categorical_accuracy: 0.9346
47904/60000 [======================>.......] - ETA: 22s - loss: 0.2111 - categorical_accuracy: 0.9347
47936/60000 [======================>.......] - ETA: 22s - loss: 0.2110 - categorical_accuracy: 0.9347
47968/60000 [======================>.......] - ETA: 22s - loss: 0.2109 - categorical_accuracy: 0.9347
48000/60000 [=======================>......] - ETA: 22s - loss: 0.2108 - categorical_accuracy: 0.9347
48032/60000 [=======================>......] - ETA: 22s - loss: 0.2107 - categorical_accuracy: 0.9348
48064/60000 [=======================>......] - ETA: 22s - loss: 0.2107 - categorical_accuracy: 0.9348
48096/60000 [=======================>......] - ETA: 22s - loss: 0.2107 - categorical_accuracy: 0.9348
48128/60000 [=======================>......] - ETA: 22s - loss: 0.2106 - categorical_accuracy: 0.9348
48160/60000 [=======================>......] - ETA: 22s - loss: 0.2106 - categorical_accuracy: 0.9348
48192/60000 [=======================>......] - ETA: 22s - loss: 0.2105 - categorical_accuracy: 0.9348
48224/60000 [=======================>......] - ETA: 22s - loss: 0.2104 - categorical_accuracy: 0.9349
48256/60000 [=======================>......] - ETA: 22s - loss: 0.2104 - categorical_accuracy: 0.9349
48288/60000 [=======================>......] - ETA: 22s - loss: 0.2103 - categorical_accuracy: 0.9349
48320/60000 [=======================>......] - ETA: 22s - loss: 0.2102 - categorical_accuracy: 0.9350
48352/60000 [=======================>......] - ETA: 21s - loss: 0.2101 - categorical_accuracy: 0.9350
48384/60000 [=======================>......] - ETA: 21s - loss: 0.2102 - categorical_accuracy: 0.9350
48416/60000 [=======================>......] - ETA: 21s - loss: 0.2101 - categorical_accuracy: 0.9350
48448/60000 [=======================>......] - ETA: 21s - loss: 0.2099 - categorical_accuracy: 0.9350
48480/60000 [=======================>......] - ETA: 21s - loss: 0.2098 - categorical_accuracy: 0.9351
48512/60000 [=======================>......] - ETA: 21s - loss: 0.2100 - categorical_accuracy: 0.9351
48544/60000 [=======================>......] - ETA: 21s - loss: 0.2100 - categorical_accuracy: 0.9351
48576/60000 [=======================>......] - ETA: 21s - loss: 0.2099 - categorical_accuracy: 0.9351
48608/60000 [=======================>......] - ETA: 21s - loss: 0.2098 - categorical_accuracy: 0.9351
48640/60000 [=======================>......] - ETA: 21s - loss: 0.2097 - categorical_accuracy: 0.9352
48672/60000 [=======================>......] - ETA: 21s - loss: 0.2096 - categorical_accuracy: 0.9352
48704/60000 [=======================>......] - ETA: 21s - loss: 0.2096 - categorical_accuracy: 0.9352
48736/60000 [=======================>......] - ETA: 21s - loss: 0.2095 - categorical_accuracy: 0.9352
48768/60000 [=======================>......] - ETA: 21s - loss: 0.2094 - categorical_accuracy: 0.9353
48800/60000 [=======================>......] - ETA: 21s - loss: 0.2093 - categorical_accuracy: 0.9353
48832/60000 [=======================>......] - ETA: 21s - loss: 0.2093 - categorical_accuracy: 0.9353
48864/60000 [=======================>......] - ETA: 21s - loss: 0.2092 - categorical_accuracy: 0.9354
48896/60000 [=======================>......] - ETA: 20s - loss: 0.2091 - categorical_accuracy: 0.9354
48928/60000 [=======================>......] - ETA: 20s - loss: 0.2089 - categorical_accuracy: 0.9354
48960/60000 [=======================>......] - ETA: 20s - loss: 0.2088 - categorical_accuracy: 0.9355
48992/60000 [=======================>......] - ETA: 20s - loss: 0.2087 - categorical_accuracy: 0.9355
49024/60000 [=======================>......] - ETA: 20s - loss: 0.2087 - categorical_accuracy: 0.9355
49056/60000 [=======================>......] - ETA: 20s - loss: 0.2086 - categorical_accuracy: 0.9355
49088/60000 [=======================>......] - ETA: 20s - loss: 0.2085 - categorical_accuracy: 0.9356
49120/60000 [=======================>......] - ETA: 20s - loss: 0.2084 - categorical_accuracy: 0.9356
49152/60000 [=======================>......] - ETA: 20s - loss: 0.2084 - categorical_accuracy: 0.9356
49184/60000 [=======================>......] - ETA: 20s - loss: 0.2084 - categorical_accuracy: 0.9356
49216/60000 [=======================>......] - ETA: 20s - loss: 0.2083 - categorical_accuracy: 0.9356
49248/60000 [=======================>......] - ETA: 20s - loss: 0.2084 - categorical_accuracy: 0.9356
49280/60000 [=======================>......] - ETA: 20s - loss: 0.2083 - categorical_accuracy: 0.9356
49312/60000 [=======================>......] - ETA: 20s - loss: 0.2082 - categorical_accuracy: 0.9357
49344/60000 [=======================>......] - ETA: 20s - loss: 0.2082 - categorical_accuracy: 0.9357
49376/60000 [=======================>......] - ETA: 20s - loss: 0.2080 - categorical_accuracy: 0.9357
49408/60000 [=======================>......] - ETA: 20s - loss: 0.2080 - categorical_accuracy: 0.9357
49440/60000 [=======================>......] - ETA: 19s - loss: 0.2079 - categorical_accuracy: 0.9358
49472/60000 [=======================>......] - ETA: 19s - loss: 0.2079 - categorical_accuracy: 0.9358
49504/60000 [=======================>......] - ETA: 19s - loss: 0.2077 - categorical_accuracy: 0.9358
49536/60000 [=======================>......] - ETA: 19s - loss: 0.2076 - categorical_accuracy: 0.9358
49568/60000 [=======================>......] - ETA: 19s - loss: 0.2076 - categorical_accuracy: 0.9358
49600/60000 [=======================>......] - ETA: 19s - loss: 0.2075 - categorical_accuracy: 0.9359
49632/60000 [=======================>......] - ETA: 19s - loss: 0.2074 - categorical_accuracy: 0.9359
49664/60000 [=======================>......] - ETA: 19s - loss: 0.2073 - categorical_accuracy: 0.9359
49696/60000 [=======================>......] - ETA: 19s - loss: 0.2072 - categorical_accuracy: 0.9360
49728/60000 [=======================>......] - ETA: 19s - loss: 0.2071 - categorical_accuracy: 0.9360
49760/60000 [=======================>......] - ETA: 19s - loss: 0.2070 - categorical_accuracy: 0.9360
49792/60000 [=======================>......] - ETA: 19s - loss: 0.2069 - categorical_accuracy: 0.9361
49824/60000 [=======================>......] - ETA: 19s - loss: 0.2068 - categorical_accuracy: 0.9361
49856/60000 [=======================>......] - ETA: 19s - loss: 0.2067 - categorical_accuracy: 0.9361
49888/60000 [=======================>......] - ETA: 19s - loss: 0.2066 - categorical_accuracy: 0.9362
49920/60000 [=======================>......] - ETA: 19s - loss: 0.2065 - categorical_accuracy: 0.9362
49952/60000 [=======================>......] - ETA: 18s - loss: 0.2065 - categorical_accuracy: 0.9362
49984/60000 [=======================>......] - ETA: 18s - loss: 0.2065 - categorical_accuracy: 0.9362
50016/60000 [========================>.....] - ETA: 18s - loss: 0.2064 - categorical_accuracy: 0.9362
50048/60000 [========================>.....] - ETA: 18s - loss: 0.2063 - categorical_accuracy: 0.9362
50080/60000 [========================>.....] - ETA: 18s - loss: 0.2062 - categorical_accuracy: 0.9363
50112/60000 [========================>.....] - ETA: 18s - loss: 0.2061 - categorical_accuracy: 0.9363
50144/60000 [========================>.....] - ETA: 18s - loss: 0.2060 - categorical_accuracy: 0.9363
50176/60000 [========================>.....] - ETA: 18s - loss: 0.2059 - categorical_accuracy: 0.9364
50208/60000 [========================>.....] - ETA: 18s - loss: 0.2058 - categorical_accuracy: 0.9364
50240/60000 [========================>.....] - ETA: 18s - loss: 0.2057 - categorical_accuracy: 0.9364
50272/60000 [========================>.....] - ETA: 18s - loss: 0.2056 - categorical_accuracy: 0.9365
50304/60000 [========================>.....] - ETA: 18s - loss: 0.2055 - categorical_accuracy: 0.9365
50336/60000 [========================>.....] - ETA: 18s - loss: 0.2057 - categorical_accuracy: 0.9365
50368/60000 [========================>.....] - ETA: 18s - loss: 0.2057 - categorical_accuracy: 0.9365
50400/60000 [========================>.....] - ETA: 18s - loss: 0.2056 - categorical_accuracy: 0.9365
50432/60000 [========================>.....] - ETA: 18s - loss: 0.2055 - categorical_accuracy: 0.9365
50464/60000 [========================>.....] - ETA: 18s - loss: 0.2055 - categorical_accuracy: 0.9365
50496/60000 [========================>.....] - ETA: 17s - loss: 0.2054 - categorical_accuracy: 0.9365
50528/60000 [========================>.....] - ETA: 17s - loss: 0.2053 - categorical_accuracy: 0.9366
50560/60000 [========================>.....] - ETA: 17s - loss: 0.2052 - categorical_accuracy: 0.9366
50592/60000 [========================>.....] - ETA: 17s - loss: 0.2051 - categorical_accuracy: 0.9367
50624/60000 [========================>.....] - ETA: 17s - loss: 0.2051 - categorical_accuracy: 0.9367
50656/60000 [========================>.....] - ETA: 17s - loss: 0.2050 - categorical_accuracy: 0.9367
50688/60000 [========================>.....] - ETA: 17s - loss: 0.2049 - categorical_accuracy: 0.9367
50720/60000 [========================>.....] - ETA: 17s - loss: 0.2048 - categorical_accuracy: 0.9367
50752/60000 [========================>.....] - ETA: 17s - loss: 0.2049 - categorical_accuracy: 0.9367
50784/60000 [========================>.....] - ETA: 17s - loss: 0.2049 - categorical_accuracy: 0.9368
50816/60000 [========================>.....] - ETA: 17s - loss: 0.2048 - categorical_accuracy: 0.9368
50848/60000 [========================>.....] - ETA: 17s - loss: 0.2047 - categorical_accuracy: 0.9368
50880/60000 [========================>.....] - ETA: 17s - loss: 0.2046 - categorical_accuracy: 0.9368
50912/60000 [========================>.....] - ETA: 17s - loss: 0.2046 - categorical_accuracy: 0.9369
50944/60000 [========================>.....] - ETA: 17s - loss: 0.2046 - categorical_accuracy: 0.9369
50976/60000 [========================>.....] - ETA: 17s - loss: 0.2045 - categorical_accuracy: 0.9369
51008/60000 [========================>.....] - ETA: 16s - loss: 0.2044 - categorical_accuracy: 0.9369
51040/60000 [========================>.....] - ETA: 16s - loss: 0.2044 - categorical_accuracy: 0.9370
51072/60000 [========================>.....] - ETA: 16s - loss: 0.2043 - categorical_accuracy: 0.9370
51104/60000 [========================>.....] - ETA: 16s - loss: 0.2042 - categorical_accuracy: 0.9370
51136/60000 [========================>.....] - ETA: 16s - loss: 0.2041 - categorical_accuracy: 0.9371
51168/60000 [========================>.....] - ETA: 16s - loss: 0.2042 - categorical_accuracy: 0.9371
51200/60000 [========================>.....] - ETA: 16s - loss: 0.2041 - categorical_accuracy: 0.9371
51232/60000 [========================>.....] - ETA: 16s - loss: 0.2040 - categorical_accuracy: 0.9372
51264/60000 [========================>.....] - ETA: 16s - loss: 0.2040 - categorical_accuracy: 0.9371
51296/60000 [========================>.....] - ETA: 16s - loss: 0.2039 - categorical_accuracy: 0.9372
51328/60000 [========================>.....] - ETA: 16s - loss: 0.2038 - categorical_accuracy: 0.9372
51360/60000 [========================>.....] - ETA: 16s - loss: 0.2037 - categorical_accuracy: 0.9372
51392/60000 [========================>.....] - ETA: 16s - loss: 0.2036 - categorical_accuracy: 0.9373
51424/60000 [========================>.....] - ETA: 16s - loss: 0.2035 - categorical_accuracy: 0.9373
51456/60000 [========================>.....] - ETA: 16s - loss: 0.2033 - categorical_accuracy: 0.9374
51488/60000 [========================>.....] - ETA: 16s - loss: 0.2033 - categorical_accuracy: 0.9374
51520/60000 [========================>.....] - ETA: 16s - loss: 0.2032 - categorical_accuracy: 0.9374
51552/60000 [========================>.....] - ETA: 15s - loss: 0.2032 - categorical_accuracy: 0.9374
51584/60000 [========================>.....] - ETA: 15s - loss: 0.2031 - categorical_accuracy: 0.9374
51616/60000 [========================>.....] - ETA: 15s - loss: 0.2031 - categorical_accuracy: 0.9374
51648/60000 [========================>.....] - ETA: 15s - loss: 0.2032 - categorical_accuracy: 0.9375
51680/60000 [========================>.....] - ETA: 15s - loss: 0.2032 - categorical_accuracy: 0.9375
51712/60000 [========================>.....] - ETA: 15s - loss: 0.2031 - categorical_accuracy: 0.9375
51744/60000 [========================>.....] - ETA: 15s - loss: 0.2030 - categorical_accuracy: 0.9375
51776/60000 [========================>.....] - ETA: 15s - loss: 0.2029 - categorical_accuracy: 0.9376
51808/60000 [========================>.....] - ETA: 15s - loss: 0.2029 - categorical_accuracy: 0.9376
51840/60000 [========================>.....] - ETA: 15s - loss: 0.2030 - categorical_accuracy: 0.9376
51872/60000 [========================>.....] - ETA: 15s - loss: 0.2029 - categorical_accuracy: 0.9376
51904/60000 [========================>.....] - ETA: 15s - loss: 0.2028 - categorical_accuracy: 0.9376
51936/60000 [========================>.....] - ETA: 15s - loss: 0.2027 - categorical_accuracy: 0.9376
51968/60000 [========================>.....] - ETA: 15s - loss: 0.2026 - categorical_accuracy: 0.9377
52000/60000 [=========================>....] - ETA: 15s - loss: 0.2026 - categorical_accuracy: 0.9376
52032/60000 [=========================>....] - ETA: 15s - loss: 0.2025 - categorical_accuracy: 0.9377
52064/60000 [=========================>....] - ETA: 14s - loss: 0.2024 - categorical_accuracy: 0.9377
52096/60000 [=========================>....] - ETA: 14s - loss: 0.2023 - categorical_accuracy: 0.9377
52128/60000 [=========================>....] - ETA: 14s - loss: 0.2023 - categorical_accuracy: 0.9377
52160/60000 [=========================>....] - ETA: 14s - loss: 0.2022 - categorical_accuracy: 0.9378
52192/60000 [=========================>....] - ETA: 14s - loss: 0.2020 - categorical_accuracy: 0.9378
52224/60000 [=========================>....] - ETA: 14s - loss: 0.2021 - categorical_accuracy: 0.9378
52256/60000 [=========================>....] - ETA: 14s - loss: 0.2020 - categorical_accuracy: 0.9378
52288/60000 [=========================>....] - ETA: 14s - loss: 0.2020 - categorical_accuracy: 0.9379
52320/60000 [=========================>....] - ETA: 14s - loss: 0.2019 - categorical_accuracy: 0.9379
52352/60000 [=========================>....] - ETA: 14s - loss: 0.2018 - categorical_accuracy: 0.9379
52384/60000 [=========================>....] - ETA: 14s - loss: 0.2017 - categorical_accuracy: 0.9380
52416/60000 [=========================>....] - ETA: 14s - loss: 0.2017 - categorical_accuracy: 0.9380
52448/60000 [=========================>....] - ETA: 14s - loss: 0.2016 - categorical_accuracy: 0.9380
52480/60000 [=========================>....] - ETA: 14s - loss: 0.2016 - categorical_accuracy: 0.9380
52512/60000 [=========================>....] - ETA: 14s - loss: 0.2016 - categorical_accuracy: 0.9380
52544/60000 [=========================>....] - ETA: 14s - loss: 0.2016 - categorical_accuracy: 0.9380
52576/60000 [=========================>....] - ETA: 14s - loss: 0.2015 - categorical_accuracy: 0.9380
52608/60000 [=========================>....] - ETA: 13s - loss: 0.2014 - categorical_accuracy: 0.9381
52640/60000 [=========================>....] - ETA: 13s - loss: 0.2013 - categorical_accuracy: 0.9381
52672/60000 [=========================>....] - ETA: 13s - loss: 0.2012 - categorical_accuracy: 0.9381
52704/60000 [=========================>....] - ETA: 13s - loss: 0.2011 - categorical_accuracy: 0.9381
52736/60000 [=========================>....] - ETA: 13s - loss: 0.2011 - categorical_accuracy: 0.9381
52768/60000 [=========================>....] - ETA: 13s - loss: 0.2010 - categorical_accuracy: 0.9382
52800/60000 [=========================>....] - ETA: 13s - loss: 0.2009 - categorical_accuracy: 0.9382
52832/60000 [=========================>....] - ETA: 13s - loss: 0.2008 - categorical_accuracy: 0.9382
52864/60000 [=========================>....] - ETA: 13s - loss: 0.2008 - categorical_accuracy: 0.9383
52896/60000 [=========================>....] - ETA: 13s - loss: 0.2007 - categorical_accuracy: 0.9383
52928/60000 [=========================>....] - ETA: 13s - loss: 0.2006 - categorical_accuracy: 0.9383
52960/60000 [=========================>....] - ETA: 13s - loss: 0.2005 - categorical_accuracy: 0.9383
52992/60000 [=========================>....] - ETA: 13s - loss: 0.2005 - categorical_accuracy: 0.9383
53024/60000 [=========================>....] - ETA: 13s - loss: 0.2004 - categorical_accuracy: 0.9384
53056/60000 [=========================>....] - ETA: 13s - loss: 0.2003 - categorical_accuracy: 0.9384
53088/60000 [=========================>....] - ETA: 13s - loss: 0.2003 - categorical_accuracy: 0.9384
53120/60000 [=========================>....] - ETA: 12s - loss: 0.2002 - categorical_accuracy: 0.9384
53152/60000 [=========================>....] - ETA: 12s - loss: 0.2002 - categorical_accuracy: 0.9384
53184/60000 [=========================>....] - ETA: 12s - loss: 0.2000 - categorical_accuracy: 0.9385
53216/60000 [=========================>....] - ETA: 12s - loss: 0.2000 - categorical_accuracy: 0.9385
53248/60000 [=========================>....] - ETA: 12s - loss: 0.2001 - categorical_accuracy: 0.9385
53280/60000 [=========================>....] - ETA: 12s - loss: 0.2002 - categorical_accuracy: 0.9385
53312/60000 [=========================>....] - ETA: 12s - loss: 0.2000 - categorical_accuracy: 0.9385
53344/60000 [=========================>....] - ETA: 12s - loss: 0.2000 - categorical_accuracy: 0.9385
53376/60000 [=========================>....] - ETA: 12s - loss: 0.1999 - categorical_accuracy: 0.9385
53408/60000 [=========================>....] - ETA: 12s - loss: 0.2000 - categorical_accuracy: 0.9385
53440/60000 [=========================>....] - ETA: 12s - loss: 0.1999 - categorical_accuracy: 0.9385
53472/60000 [=========================>....] - ETA: 12s - loss: 0.1999 - categorical_accuracy: 0.9386
53504/60000 [=========================>....] - ETA: 12s - loss: 0.1998 - categorical_accuracy: 0.9386
53536/60000 [=========================>....] - ETA: 12s - loss: 0.1997 - categorical_accuracy: 0.9386
53568/60000 [=========================>....] - ETA: 12s - loss: 0.1996 - categorical_accuracy: 0.9386
53600/60000 [=========================>....] - ETA: 12s - loss: 0.1997 - categorical_accuracy: 0.9386
53632/60000 [=========================>....] - ETA: 12s - loss: 0.1996 - categorical_accuracy: 0.9387
53664/60000 [=========================>....] - ETA: 11s - loss: 0.1995 - categorical_accuracy: 0.9387
53696/60000 [=========================>....] - ETA: 11s - loss: 0.1995 - categorical_accuracy: 0.9387
53728/60000 [=========================>....] - ETA: 11s - loss: 0.1993 - categorical_accuracy: 0.9387
53760/60000 [=========================>....] - ETA: 11s - loss: 0.1993 - categorical_accuracy: 0.9387
53792/60000 [=========================>....] - ETA: 11s - loss: 0.1992 - categorical_accuracy: 0.9388
53824/60000 [=========================>....] - ETA: 11s - loss: 0.1994 - categorical_accuracy: 0.9388
53856/60000 [=========================>....] - ETA: 11s - loss: 0.1994 - categorical_accuracy: 0.9387
53888/60000 [=========================>....] - ETA: 11s - loss: 0.1995 - categorical_accuracy: 0.9387
53920/60000 [=========================>....] - ETA: 11s - loss: 0.1994 - categorical_accuracy: 0.9387
53952/60000 [=========================>....] - ETA: 11s - loss: 0.1993 - categorical_accuracy: 0.9388
53984/60000 [=========================>....] - ETA: 11s - loss: 0.1992 - categorical_accuracy: 0.9388
54016/60000 [==========================>...] - ETA: 11s - loss: 0.1991 - categorical_accuracy: 0.9388
54048/60000 [==========================>...] - ETA: 11s - loss: 0.1990 - categorical_accuracy: 0.9389
54080/60000 [==========================>...] - ETA: 11s - loss: 0.1989 - categorical_accuracy: 0.9389
54112/60000 [==========================>...] - ETA: 11s - loss: 0.1988 - categorical_accuracy: 0.9389
54144/60000 [==========================>...] - ETA: 11s - loss: 0.1987 - categorical_accuracy: 0.9390
54176/60000 [==========================>...] - ETA: 10s - loss: 0.1986 - categorical_accuracy: 0.9390
54208/60000 [==========================>...] - ETA: 10s - loss: 0.1985 - categorical_accuracy: 0.9390
54240/60000 [==========================>...] - ETA: 10s - loss: 0.1984 - categorical_accuracy: 0.9391
54272/60000 [==========================>...] - ETA: 10s - loss: 0.1983 - categorical_accuracy: 0.9391
54304/60000 [==========================>...] - ETA: 10s - loss: 0.1982 - categorical_accuracy: 0.9391
54336/60000 [==========================>...] - ETA: 10s - loss: 0.1982 - categorical_accuracy: 0.9391
54368/60000 [==========================>...] - ETA: 10s - loss: 0.1981 - categorical_accuracy: 0.9392
54400/60000 [==========================>...] - ETA: 10s - loss: 0.1980 - categorical_accuracy: 0.9392
54432/60000 [==========================>...] - ETA: 10s - loss: 0.1980 - categorical_accuracy: 0.9392
54464/60000 [==========================>...] - ETA: 10s - loss: 0.1979 - categorical_accuracy: 0.9392
54496/60000 [==========================>...] - ETA: 10s - loss: 0.1978 - categorical_accuracy: 0.9392
54528/60000 [==========================>...] - ETA: 10s - loss: 0.1977 - categorical_accuracy: 0.9393
54560/60000 [==========================>...] - ETA: 10s - loss: 0.1976 - categorical_accuracy: 0.9393
54592/60000 [==========================>...] - ETA: 10s - loss: 0.1975 - categorical_accuracy: 0.9393
54624/60000 [==========================>...] - ETA: 10s - loss: 0.1974 - categorical_accuracy: 0.9393
54656/60000 [==========================>...] - ETA: 10s - loss: 0.1973 - categorical_accuracy: 0.9394
54688/60000 [==========================>...] - ETA: 10s - loss: 0.1974 - categorical_accuracy: 0.9393
54720/60000 [==========================>...] - ETA: 9s - loss: 0.1973 - categorical_accuracy: 0.9394 
54752/60000 [==========================>...] - ETA: 9s - loss: 0.1972 - categorical_accuracy: 0.9394
54784/60000 [==========================>...] - ETA: 9s - loss: 0.1972 - categorical_accuracy: 0.9394
54816/60000 [==========================>...] - ETA: 9s - loss: 0.1972 - categorical_accuracy: 0.9395
54848/60000 [==========================>...] - ETA: 9s - loss: 0.1970 - categorical_accuracy: 0.9395
54880/60000 [==========================>...] - ETA: 9s - loss: 0.1969 - categorical_accuracy: 0.9395
54912/60000 [==========================>...] - ETA: 9s - loss: 0.1969 - categorical_accuracy: 0.9395
54944/60000 [==========================>...] - ETA: 9s - loss: 0.1969 - categorical_accuracy: 0.9395
54976/60000 [==========================>...] - ETA: 9s - loss: 0.1969 - categorical_accuracy: 0.9396
55008/60000 [==========================>...] - ETA: 9s - loss: 0.1968 - categorical_accuracy: 0.9396
55040/60000 [==========================>...] - ETA: 9s - loss: 0.1968 - categorical_accuracy: 0.9396
55072/60000 [==========================>...] - ETA: 9s - loss: 0.1967 - categorical_accuracy: 0.9396
55104/60000 [==========================>...] - ETA: 9s - loss: 0.1967 - categorical_accuracy: 0.9396
55136/60000 [==========================>...] - ETA: 9s - loss: 0.1967 - categorical_accuracy: 0.9396
55168/60000 [==========================>...] - ETA: 9s - loss: 0.1967 - categorical_accuracy: 0.9396
55200/60000 [==========================>...] - ETA: 9s - loss: 0.1966 - categorical_accuracy: 0.9397
55232/60000 [==========================>...] - ETA: 8s - loss: 0.1965 - categorical_accuracy: 0.9397
55264/60000 [==========================>...] - ETA: 8s - loss: 0.1964 - categorical_accuracy: 0.9397
55296/60000 [==========================>...] - ETA: 8s - loss: 0.1963 - categorical_accuracy: 0.9398
55328/60000 [==========================>...] - ETA: 8s - loss: 0.1963 - categorical_accuracy: 0.9398
55360/60000 [==========================>...] - ETA: 8s - loss: 0.1962 - categorical_accuracy: 0.9398
55392/60000 [==========================>...] - ETA: 8s - loss: 0.1961 - categorical_accuracy: 0.9398
55424/60000 [==========================>...] - ETA: 8s - loss: 0.1961 - categorical_accuracy: 0.9399
55456/60000 [==========================>...] - ETA: 8s - loss: 0.1960 - categorical_accuracy: 0.9399
55488/60000 [==========================>...] - ETA: 8s - loss: 0.1959 - categorical_accuracy: 0.9399
55520/60000 [==========================>...] - ETA: 8s - loss: 0.1958 - categorical_accuracy: 0.9399
55552/60000 [==========================>...] - ETA: 8s - loss: 0.1957 - categorical_accuracy: 0.9400
55584/60000 [==========================>...] - ETA: 8s - loss: 0.1957 - categorical_accuracy: 0.9400
55616/60000 [==========================>...] - ETA: 8s - loss: 0.1956 - categorical_accuracy: 0.9400
55648/60000 [==========================>...] - ETA: 8s - loss: 0.1955 - categorical_accuracy: 0.9400
55680/60000 [==========================>...] - ETA: 8s - loss: 0.1954 - categorical_accuracy: 0.9401
55712/60000 [==========================>...] - ETA: 8s - loss: 0.1954 - categorical_accuracy: 0.9401
55744/60000 [==========================>...] - ETA: 8s - loss: 0.1953 - categorical_accuracy: 0.9401
55776/60000 [==========================>...] - ETA: 7s - loss: 0.1952 - categorical_accuracy: 0.9401
55808/60000 [==========================>...] - ETA: 7s - loss: 0.1951 - categorical_accuracy: 0.9402
55840/60000 [==========================>...] - ETA: 7s - loss: 0.1950 - categorical_accuracy: 0.9402
55872/60000 [==========================>...] - ETA: 7s - loss: 0.1949 - categorical_accuracy: 0.9402
55904/60000 [==========================>...] - ETA: 7s - loss: 0.1949 - categorical_accuracy: 0.9402
55936/60000 [==========================>...] - ETA: 7s - loss: 0.1948 - categorical_accuracy: 0.9402
55968/60000 [==========================>...] - ETA: 7s - loss: 0.1948 - categorical_accuracy: 0.9403
56000/60000 [===========================>..] - ETA: 7s - loss: 0.1947 - categorical_accuracy: 0.9403
56032/60000 [===========================>..] - ETA: 7s - loss: 0.1946 - categorical_accuracy: 0.9403
56064/60000 [===========================>..] - ETA: 7s - loss: 0.1946 - categorical_accuracy: 0.9403
56096/60000 [===========================>..] - ETA: 7s - loss: 0.1945 - categorical_accuracy: 0.9403
56128/60000 [===========================>..] - ETA: 7s - loss: 0.1944 - categorical_accuracy: 0.9404
56160/60000 [===========================>..] - ETA: 7s - loss: 0.1943 - categorical_accuracy: 0.9404
56192/60000 [===========================>..] - ETA: 7s - loss: 0.1943 - categorical_accuracy: 0.9404
56224/60000 [===========================>..] - ETA: 7s - loss: 0.1942 - categorical_accuracy: 0.9404
56256/60000 [===========================>..] - ETA: 7s - loss: 0.1942 - categorical_accuracy: 0.9405
56288/60000 [===========================>..] - ETA: 6s - loss: 0.1941 - categorical_accuracy: 0.9405
56320/60000 [===========================>..] - ETA: 6s - loss: 0.1940 - categorical_accuracy: 0.9405
56352/60000 [===========================>..] - ETA: 6s - loss: 0.1939 - categorical_accuracy: 0.9405
56384/60000 [===========================>..] - ETA: 6s - loss: 0.1939 - categorical_accuracy: 0.9406
56416/60000 [===========================>..] - ETA: 6s - loss: 0.1939 - categorical_accuracy: 0.9405
56448/60000 [===========================>..] - ETA: 6s - loss: 0.1938 - categorical_accuracy: 0.9406
56480/60000 [===========================>..] - ETA: 6s - loss: 0.1937 - categorical_accuracy: 0.9406
56512/60000 [===========================>..] - ETA: 6s - loss: 0.1936 - categorical_accuracy: 0.9406
56544/60000 [===========================>..] - ETA: 6s - loss: 0.1935 - categorical_accuracy: 0.9406
56576/60000 [===========================>..] - ETA: 6s - loss: 0.1934 - categorical_accuracy: 0.9406
56608/60000 [===========================>..] - ETA: 6s - loss: 0.1935 - categorical_accuracy: 0.9406
56640/60000 [===========================>..] - ETA: 6s - loss: 0.1935 - categorical_accuracy: 0.9407
56672/60000 [===========================>..] - ETA: 6s - loss: 0.1935 - categorical_accuracy: 0.9407
56704/60000 [===========================>..] - ETA: 6s - loss: 0.1934 - categorical_accuracy: 0.9407
56736/60000 [===========================>..] - ETA: 6s - loss: 0.1935 - categorical_accuracy: 0.9407
56768/60000 [===========================>..] - ETA: 6s - loss: 0.1935 - categorical_accuracy: 0.9407
56800/60000 [===========================>..] - ETA: 6s - loss: 0.1935 - categorical_accuracy: 0.9407
56832/60000 [===========================>..] - ETA: 5s - loss: 0.1934 - categorical_accuracy: 0.9407
56864/60000 [===========================>..] - ETA: 5s - loss: 0.1934 - categorical_accuracy: 0.9407
56896/60000 [===========================>..] - ETA: 5s - loss: 0.1933 - categorical_accuracy: 0.9407
56928/60000 [===========================>..] - ETA: 5s - loss: 0.1933 - categorical_accuracy: 0.9407
56960/60000 [===========================>..] - ETA: 5s - loss: 0.1932 - categorical_accuracy: 0.9407
56992/60000 [===========================>..] - ETA: 5s - loss: 0.1931 - categorical_accuracy: 0.9408
57024/60000 [===========================>..] - ETA: 5s - loss: 0.1931 - categorical_accuracy: 0.9408
57056/60000 [===========================>..] - ETA: 5s - loss: 0.1931 - categorical_accuracy: 0.9408
57088/60000 [===========================>..] - ETA: 5s - loss: 0.1930 - categorical_accuracy: 0.9408
57120/60000 [===========================>..] - ETA: 5s - loss: 0.1929 - categorical_accuracy: 0.9409
57152/60000 [===========================>..] - ETA: 5s - loss: 0.1929 - categorical_accuracy: 0.9409
57184/60000 [===========================>..] - ETA: 5s - loss: 0.1928 - categorical_accuracy: 0.9409
57216/60000 [===========================>..] - ETA: 5s - loss: 0.1927 - categorical_accuracy: 0.9409
57248/60000 [===========================>..] - ETA: 5s - loss: 0.1926 - categorical_accuracy: 0.9410
57280/60000 [===========================>..] - ETA: 5s - loss: 0.1925 - categorical_accuracy: 0.9410
57312/60000 [===========================>..] - ETA: 5s - loss: 0.1925 - categorical_accuracy: 0.9410
57344/60000 [===========================>..] - ETA: 5s - loss: 0.1925 - categorical_accuracy: 0.9410
57376/60000 [===========================>..] - ETA: 4s - loss: 0.1925 - categorical_accuracy: 0.9410
57408/60000 [===========================>..] - ETA: 4s - loss: 0.1925 - categorical_accuracy: 0.9410
57440/60000 [===========================>..] - ETA: 4s - loss: 0.1924 - categorical_accuracy: 0.9410
57472/60000 [===========================>..] - ETA: 4s - loss: 0.1923 - categorical_accuracy: 0.9410
57504/60000 [===========================>..] - ETA: 4s - loss: 0.1922 - categorical_accuracy: 0.9411
57536/60000 [===========================>..] - ETA: 4s - loss: 0.1921 - categorical_accuracy: 0.9411
57568/60000 [===========================>..] - ETA: 4s - loss: 0.1921 - categorical_accuracy: 0.9411
57600/60000 [===========================>..] - ETA: 4s - loss: 0.1920 - categorical_accuracy: 0.9411
57632/60000 [===========================>..] - ETA: 4s - loss: 0.1919 - categorical_accuracy: 0.9412
57664/60000 [===========================>..] - ETA: 4s - loss: 0.1919 - categorical_accuracy: 0.9412
57696/60000 [===========================>..] - ETA: 4s - loss: 0.1919 - categorical_accuracy: 0.9412
57728/60000 [===========================>..] - ETA: 4s - loss: 0.1918 - categorical_accuracy: 0.9412
57760/60000 [===========================>..] - ETA: 4s - loss: 0.1918 - categorical_accuracy: 0.9413
57792/60000 [===========================>..] - ETA: 4s - loss: 0.1917 - categorical_accuracy: 0.9413
57824/60000 [===========================>..] - ETA: 4s - loss: 0.1916 - categorical_accuracy: 0.9413
57856/60000 [===========================>..] - ETA: 4s - loss: 0.1915 - categorical_accuracy: 0.9413
57888/60000 [===========================>..] - ETA: 3s - loss: 0.1914 - categorical_accuracy: 0.9414
57920/60000 [===========================>..] - ETA: 3s - loss: 0.1913 - categorical_accuracy: 0.9414
57952/60000 [===========================>..] - ETA: 3s - loss: 0.1913 - categorical_accuracy: 0.9414
57984/60000 [===========================>..] - ETA: 3s - loss: 0.1912 - categorical_accuracy: 0.9414
58016/60000 [============================>.] - ETA: 3s - loss: 0.1911 - categorical_accuracy: 0.9414
58048/60000 [============================>.] - ETA: 3s - loss: 0.1910 - categorical_accuracy: 0.9415
58080/60000 [============================>.] - ETA: 3s - loss: 0.1910 - categorical_accuracy: 0.9415
58112/60000 [============================>.] - ETA: 3s - loss: 0.1909 - categorical_accuracy: 0.9415
58144/60000 [============================>.] - ETA: 3s - loss: 0.1909 - categorical_accuracy: 0.9415
58176/60000 [============================>.] - ETA: 3s - loss: 0.1908 - categorical_accuracy: 0.9415
58208/60000 [============================>.] - ETA: 3s - loss: 0.1908 - categorical_accuracy: 0.9415
58240/60000 [============================>.] - ETA: 3s - loss: 0.1907 - categorical_accuracy: 0.9416
58272/60000 [============================>.] - ETA: 3s - loss: 0.1906 - categorical_accuracy: 0.9416
58304/60000 [============================>.] - ETA: 3s - loss: 0.1906 - categorical_accuracy: 0.9416
58336/60000 [============================>.] - ETA: 3s - loss: 0.1906 - categorical_accuracy: 0.9416
58368/60000 [============================>.] - ETA: 3s - loss: 0.1905 - categorical_accuracy: 0.9416
58400/60000 [============================>.] - ETA: 3s - loss: 0.1904 - categorical_accuracy: 0.9416
58432/60000 [============================>.] - ETA: 2s - loss: 0.1903 - categorical_accuracy: 0.9417
58464/60000 [============================>.] - ETA: 2s - loss: 0.1902 - categorical_accuracy: 0.9417
58496/60000 [============================>.] - ETA: 2s - loss: 0.1902 - categorical_accuracy: 0.9417
58528/60000 [============================>.] - ETA: 2s - loss: 0.1901 - categorical_accuracy: 0.9417
58560/60000 [============================>.] - ETA: 2s - loss: 0.1900 - categorical_accuracy: 0.9418
58592/60000 [============================>.] - ETA: 2s - loss: 0.1899 - categorical_accuracy: 0.9418
58624/60000 [============================>.] - ETA: 2s - loss: 0.1898 - categorical_accuracy: 0.9418
58656/60000 [============================>.] - ETA: 2s - loss: 0.1898 - categorical_accuracy: 0.9418
58688/60000 [============================>.] - ETA: 2s - loss: 0.1897 - categorical_accuracy: 0.9418
58720/60000 [============================>.] - ETA: 2s - loss: 0.1896 - categorical_accuracy: 0.9419
58752/60000 [============================>.] - ETA: 2s - loss: 0.1895 - categorical_accuracy: 0.9419
58784/60000 [============================>.] - ETA: 2s - loss: 0.1894 - categorical_accuracy: 0.9419
58816/60000 [============================>.] - ETA: 2s - loss: 0.1894 - categorical_accuracy: 0.9419
58848/60000 [============================>.] - ETA: 2s - loss: 0.1893 - categorical_accuracy: 0.9420
58880/60000 [============================>.] - ETA: 2s - loss: 0.1892 - categorical_accuracy: 0.9420
58912/60000 [============================>.] - ETA: 2s - loss: 0.1892 - categorical_accuracy: 0.9420
58944/60000 [============================>.] - ETA: 1s - loss: 0.1892 - categorical_accuracy: 0.9420
58976/60000 [============================>.] - ETA: 1s - loss: 0.1892 - categorical_accuracy: 0.9420
59008/60000 [============================>.] - ETA: 1s - loss: 0.1891 - categorical_accuracy: 0.9420
59040/60000 [============================>.] - ETA: 1s - loss: 0.1890 - categorical_accuracy: 0.9421
59072/60000 [============================>.] - ETA: 1s - loss: 0.1890 - categorical_accuracy: 0.9421
59104/60000 [============================>.] - ETA: 1s - loss: 0.1889 - categorical_accuracy: 0.9421
59136/60000 [============================>.] - ETA: 1s - loss: 0.1888 - categorical_accuracy: 0.9422
59168/60000 [============================>.] - ETA: 1s - loss: 0.1888 - categorical_accuracy: 0.9422
59200/60000 [============================>.] - ETA: 1s - loss: 0.1887 - categorical_accuracy: 0.9422
59232/60000 [============================>.] - ETA: 1s - loss: 0.1887 - categorical_accuracy: 0.9422
59264/60000 [============================>.] - ETA: 1s - loss: 0.1886 - categorical_accuracy: 0.9422
59296/60000 [============================>.] - ETA: 1s - loss: 0.1885 - categorical_accuracy: 0.9423
59328/60000 [============================>.] - ETA: 1s - loss: 0.1884 - categorical_accuracy: 0.9423
59360/60000 [============================>.] - ETA: 1s - loss: 0.1884 - categorical_accuracy: 0.9423
59392/60000 [============================>.] - ETA: 1s - loss: 0.1884 - categorical_accuracy: 0.9423
59424/60000 [============================>.] - ETA: 1s - loss: 0.1885 - categorical_accuracy: 0.9423
59456/60000 [============================>.] - ETA: 1s - loss: 0.1885 - categorical_accuracy: 0.9423
59488/60000 [============================>.] - ETA: 0s - loss: 0.1884 - categorical_accuracy: 0.9423
59520/60000 [============================>.] - ETA: 0s - loss: 0.1884 - categorical_accuracy: 0.9423
59552/60000 [============================>.] - ETA: 0s - loss: 0.1883 - categorical_accuracy: 0.9423
59584/60000 [============================>.] - ETA: 0s - loss: 0.1882 - categorical_accuracy: 0.9424
59616/60000 [============================>.] - ETA: 0s - loss: 0.1882 - categorical_accuracy: 0.9424
59648/60000 [============================>.] - ETA: 0s - loss: 0.1881 - categorical_accuracy: 0.9424
59680/60000 [============================>.] - ETA: 0s - loss: 0.1881 - categorical_accuracy: 0.9424
59712/60000 [============================>.] - ETA: 0s - loss: 0.1881 - categorical_accuracy: 0.9424
59744/60000 [============================>.] - ETA: 0s - loss: 0.1880 - categorical_accuracy: 0.9424
59776/60000 [============================>.] - ETA: 0s - loss: 0.1880 - categorical_accuracy: 0.9424
59808/60000 [============================>.] - ETA: 0s - loss: 0.1881 - categorical_accuracy: 0.9424
59840/60000 [============================>.] - ETA: 0s - loss: 0.1880 - categorical_accuracy: 0.9424
59872/60000 [============================>.] - ETA: 0s - loss: 0.1880 - categorical_accuracy: 0.9424
59904/60000 [============================>.] - ETA: 0s - loss: 0.1880 - categorical_accuracy: 0.9424
59936/60000 [============================>.] - ETA: 0s - loss: 0.1879 - categorical_accuracy: 0.9424
59968/60000 [============================>.] - ETA: 0s - loss: 0.1878 - categorical_accuracy: 0.9424
60000/60000 [==============================] - 117s 2ms/step - loss: 0.1878 - categorical_accuracy: 0.9424 - val_loss: 0.0455 - val_categorical_accuracy: 0.9849

  ('#### Predict   ####################################################',) 

  ('#### Path params   ################################################',) 

  ('/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/', '/home/runner/work/mlmodels/mlmodels/keras_deepAR/') 

   32/10000 [..............................] - ETA: 18s
  192/10000 [..............................] - ETA: 5s 
  352/10000 [>.............................] - ETA: 4s
  512/10000 [>.............................] - ETA: 4s
  672/10000 [=>............................] - ETA: 3s
  832/10000 [=>............................] - ETA: 3s
  992/10000 [=>............................] - ETA: 3s
 1152/10000 [==>...........................] - ETA: 3s
 1312/10000 [==>...........................] - ETA: 3s
 1440/10000 [===>..........................] - ETA: 3s
 1600/10000 [===>..........................] - ETA: 3s
 1728/10000 [====>.........................] - ETA: 3s
 1856/10000 [====>.........................] - ETA: 3s
 2016/10000 [=====>........................] - ETA: 3s
 2176/10000 [=====>........................] - ETA: 3s
 2336/10000 [======>.......................] - ETA: 3s
 2496/10000 [======>.......................] - ETA: 2s
 2656/10000 [======>.......................] - ETA: 2s
 2816/10000 [=======>......................] - ETA: 2s
 2976/10000 [=======>......................] - ETA: 2s
 3136/10000 [========>.....................] - ETA: 2s
 3296/10000 [========>.....................] - ETA: 2s
 3456/10000 [=========>....................] - ETA: 2s
 3616/10000 [=========>....................] - ETA: 2s
 3776/10000 [==========>...................] - ETA: 2s
 3936/10000 [==========>...................] - ETA: 2s
 4096/10000 [===========>..................] - ETA: 2s
 4224/10000 [===========>..................] - ETA: 2s
 4384/10000 [============>.................] - ETA: 2s
 4544/10000 [============>.................] - ETA: 2s
 4672/10000 [=============>................] - ETA: 2s
 4832/10000 [=============>................] - ETA: 1s
 4992/10000 [=============>................] - ETA: 1s
 5152/10000 [==============>...............] - ETA: 1s
 5280/10000 [==============>...............] - ETA: 1s
 5408/10000 [===============>..............] - ETA: 1s
 5536/10000 [===============>..............] - ETA: 1s
 5696/10000 [================>.............] - ETA: 1s
 5856/10000 [================>.............] - ETA: 1s
 6016/10000 [=================>............] - ETA: 1s
 6176/10000 [=================>............] - ETA: 1s
 6336/10000 [==================>...........] - ETA: 1s
 6496/10000 [==================>...........] - ETA: 1s
 6656/10000 [==================>...........] - ETA: 1s
 6816/10000 [===================>..........] - ETA: 1s
 6976/10000 [===================>..........] - ETA: 1s
 7104/10000 [====================>.........] - ETA: 1s
 7264/10000 [====================>.........] - ETA: 1s
 7392/10000 [=====================>........] - ETA: 0s
 7552/10000 [=====================>........] - ETA: 0s
 7712/10000 [======================>.......] - ETA: 0s
 7840/10000 [======================>.......] - ETA: 0s
 8000/10000 [=======================>......] - ETA: 0s
 8160/10000 [=======================>......] - ETA: 0s
 8288/10000 [=======================>......] - ETA: 0s
 8448/10000 [========================>.....] - ETA: 0s
 8608/10000 [========================>.....] - ETA: 0s
 8768/10000 [=========================>....] - ETA: 0s
 8928/10000 [=========================>....] - ETA: 0s
 9088/10000 [==========================>...] - ETA: 0s
 9248/10000 [==========================>...] - ETA: 0s
 9376/10000 [===========================>..] - ETA: 0s
 9536/10000 [===========================>..] - ETA: 0s
 9696/10000 [============================>.] - ETA: 0s
 9824/10000 [============================>.] - ETA: 0s
 9952/10000 [============================>.] - ETA: 0s
10000/10000 [==============================] - 4s 382us/step
[[8.9360803e-09 1.1348142e-07 3.6235213e-07 ... 9.9999809e-01
  3.3907138e-08 1.0953112e-06]
 [9.3788140e-06 3.0993269e-06 9.9998438e-01 ... 1.6702657e-08
  3.1007181e-07 3.4632677e-10]
 [6.4106734e-07 9.9988604e-01 1.8770179e-05 ... 2.6192165e-05
  4.7014501e-06 1.4298288e-06]
 ...
 [3.4928929e-09 5.8084544e-07 5.8124376e-09 ... 2.6512615e-07
  1.0785116e-06 2.1923437e-05]
 [7.7396116e-06 2.6167701e-08 1.6343057e-07 ... 2.7395558e-07
  3.2013343e-03 2.7254202e-06]
 [9.7809803e-05 5.7311468e-07 2.5297775e-05 ... 1.0675756e-08
  2.0905368e-06 1.0888067e-07]]

  ('#### metrics   ####################################################',) 

  ('#### Path params   ################################################',) 

  ('/home/runner/work/mlmodels/mlmodels/mlmodels/model_keras/', '/home/runner/work/mlmodels/mlmodels/keras_deepAR/') 
{'loss_test:': 0.04550655927534681, 'accuracy_test:': 0.9848999977111816}

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
   404e938..5b86377  master     -> origin/master
Updating 404e938..5b86377
Fast-forward
 error_list/20200519/list_log_testall_20200519.md | 443 +++++++++++++++++++++++
 1 file changed, 443 insertions(+)
[master 8bdb006] ml_store
 1 file changed, 2054 insertions(+)
To github.com:arita37/mlmodels_store.git
   5b86377..8bdb006  master -> master





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
{'loss': 0.6203163713216782, 'loss_history': []}

  #### Plot   ######################################################## 

  #### Save   ######################################################## 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm/'}
Model saved in path: /home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_tf/1_lstm//model//model.ckpt

  #### Load   ######################################################## 
2020-05-19 08:31:14.737992: W tensorflow/core/framework/op_kernel.cc:1651] OP_REQUIRES failed at save_restore_v2_ops.cc:184 : Not found: Key Variable not found in checkpoint
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
[master e60f211] ml_store
 1 file changed, 234 insertions(+)
To github.com:arita37/mlmodels_store.git
   8bdb006..e60f211  master -> master





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
[master 3318768] ml_store
 1 file changed, 36 insertions(+)
To github.com:arita37/mlmodels_store.git
   e60f211..3318768  master -> master





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
 40%|████      | 2/5 [00:22<00:34, 11.38s/it]Saving dataset/models/LightGBMClassifier/trial_1_model.pkl
Finished Task with config: {'feature_fraction': 0.8854705977006152, 'learning_rate': 0.1546734776439802, 'min_data_in_leaf': 28, 'num_leaves': 40} and reward: 0.3928
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xecU\xc6oV2\xeaX\r\x00\x00\x00learning_rateq\x02G?\xc3\xccW,\x05\r\xc0X\x10\x00\x00\x00min_data_in_leafq\x03K\x1cX\n\x00\x00\x00num_leavesq\x04K(u.' and reward: 0.3928
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xecU\xc6oV2\xeaX\r\x00\x00\x00learning_rateq\x02G?\xc3\xccW,\x05\r\xc0X\x10\x00\x00\x00min_data_in_leafq\x03K\x1cX\n\x00\x00\x00num_leavesq\x04K(u.' and reward: 0.3928
 60%|██████    | 3/5 [00:46<00:30, 15.16s/it]Saving dataset/models/LightGBMClassifier/trial_2_model.pkl
Finished Task with config: {'feature_fraction': 0.9609574249080043, 'learning_rate': 0.01669332091825964, 'min_data_in_leaf': 11, 'num_leaves': 60} and reward: 0.392
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xee\xc0)\xc9\x1a\x81\x0fX\r\x00\x00\x00learning_rateq\x02G?\x91\x18\r\xcd\x9fJ\x8eX\x10\x00\x00\x00min_data_in_leafq\x03K\x0bX\n\x00\x00\x00num_leavesq\x04K<u.' and reward: 0.392
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xee\xc0)\xc9\x1a\x81\x0fX\r\x00\x00\x00learning_rateq\x02G?\x91\x18\r\xcd\x9fJ\x8eX\x10\x00\x00\x00min_data_in_leafq\x03K\x0bX\n\x00\x00\x00num_leavesq\x04K<u.' and reward: 0.392
 80%|████████  | 4/5 [01:19<00:20, 20.53s/it] 80%|████████  | 4/5 [01:19<00:19, 19.95s/it]
Saving dataset/models/LightGBMClassifier/trial_3_model.pkl
Finished Task with config: {'feature_fraction': 0.9388182938898345, 'learning_rate': 0.008135834586851923, 'min_data_in_leaf': 9, 'num_leaves': 27} and reward: 0.386
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xee\n\xcc\xa9\xa4\x96_X\r\x00\x00\x00learning_rateq\x02G?\x80\xa9\x85;\xcf?(X\x10\x00\x00\x00min_data_in_leafq\x03K\tX\n\x00\x00\x00num_leavesq\x04K\x1bu.' and reward: 0.386
Finished Task with config: b'\x80\x03}q\x00(X\x10\x00\x00\x00feature_fractionq\x01G?\xee\n\xcc\xa9\xa4\x96_X\r\x00\x00\x00learning_rateq\x02G?\x80\xa9\x85;\xcf?(X\x10\x00\x00\x00min_data_in_leafq\x03K\tX\n\x00\x00\x00num_leavesq\x04K\x1bu.' and reward: 0.386
Time for Gradient Boosting hyperparameter optimization: 99.78276991844177
Best hyperparameter configuration for Gradient Boosting Model: 
{'feature_fraction': 0.8854705977006152, 'learning_rate': 0.1546734776439802, 'min_data_in_leaf': 28, 'num_leaves': 40}
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
 40%|████      | 2/5 [00:59<01:28, 29.66s/it] 40%|████      | 2/5 [00:59<01:28, 29.66s/it]
Loading: dataset/models/NeuralNetClassifier/train_tabNNdataset.pkl
Loading: dataset/models/NeuralNetClassifier/validation_tabNNdataset.pkl
Saving dataset/models/NeuralNetClassifier/trial_5_tabularNN.pkl
Finished Task with config: {'activation.choice': 1, 'dropout_prob': 0.1741875470241843, 'embedding_size_factor': 0.7863941179625642, 'layers.choice': 2, 'learning_rate': 0.00014687582724152577, 'network_type.choice': 0, 'use_batchnorm.choice': 1, 'weight_decay': 4.3836464731078486e-11} and reward: 0.2928
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x01X\x0c\x00\x00\x00dropout_probq\x02G?\xc6K\xc7\x0c\xeboIX\x15\x00\x00\x00embedding_size_factorq\x03G?\xe9*#\xffMO\xb4X\r\x00\x00\x00layers.choiceq\x04K\x02X\r\x00\x00\x00learning_rateq\x05G?#@U\xbf\xc8UgX\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x01X\x0c\x00\x00\x00weight_decayq\x08G=\xc8\x19o\x16\xfe\xc5lu.' and reward: 0.2928
Finished Task with config: b'\x80\x03}q\x00(X\x11\x00\x00\x00activation.choiceq\x01K\x01X\x0c\x00\x00\x00dropout_probq\x02G?\xc6K\xc7\x0c\xeboIX\x15\x00\x00\x00embedding_size_factorq\x03G?\xe9*#\xffMO\xb4X\r\x00\x00\x00layers.choiceq\x04K\x02X\r\x00\x00\x00learning_rateq\x05G?#@U\xbf\xc8UgX\x13\x00\x00\x00network_type.choiceq\x06K\x00X\x14\x00\x00\x00use_batchnorm.choiceq\x07K\x01X\x0c\x00\x00\x00weight_decayq\x08G=\xc8\x19o\x16\xfe\xc5lu.' and reward: 0.2928
Please either provide filename or allow plot in get_training_curves
Time for Neural Network hyperparameter optimization: 120.49212908744812
Best hyperparameter configuration for Tabular Neural Network: 
{'activation.choice': 0, 'dropout_prob': 0.1, 'embedding_size_factor': 1.0, 'layers.choice': 0, 'learning_rate': 0.0005, 'network_type.choice': 0, 'use_batchnorm.choice': 0, 'weight_decay': 1e-06}
Saving dataset/models/trainer.pkl
Loading: dataset/models/LightGBMClassifier/trial_0_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_1_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_2_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_3_model.pkl
Loading: dataset/models/NeuralNetClassifier/trial_4_tabularNN.pkl
Loading: dataset/models/NeuralNetClassifier/trial_5_tabularNN.pkl
Fitting model: weighted_ensemble_k0_l1 ... Training model for up to 119.73s of the -104.3s of remaining time.
Ensemble size: 43
Ensemble weights: 
[0.65116279 0.11627907 0.06976744 0.02325581 0.06976744 0.06976744]
	0.393	 = Validation accuracy score
	1.69s	 = Training runtime
	0.0s	 = Validation runtime
Saving dataset/models/weighted_ensemble_k0_l1/model.pkl
Saving dataset/models/trainer.pkl
Saving dataset/models/trainer.pkl
Saving dataset/models/trainer.pkl
AutoGluon training complete, total runtime = 226.04s ...
Loading: dataset/models/trainer.pkl

  #### save the trained model  ####################################### 

  #### Predict   #################################################### 
Loaded data from: https://autogluon.s3.amazonaws.com/datasets/Inc/test.csv | Columns = 15 / 15 | Rows = 9769 -> 9769
Loading: dataset/models/trainer.pkl
Loading: dataset/models/weighted_ensemble_k0_l1/model.pkl
Loading: dataset/models/LightGBMClassifier/trial_1_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_2_model.pkl
Loading: dataset/models/LightGBMClassifier/trial_0_model.pkl
Loading: dataset/models/NeuralNetClassifier/trial_4_tabularNN.pkl
Loading: dataset/models/LightGBMClassifier/trial_3_model.pkl
Loading: dataset/models/NeuralNetClassifier/trial_5_tabularNN.pkl

  #### Plot   ####################################################### 

  #### Save/Load   ################################################## 
Saving dataset/learner.pkl
TabularPredictor saved. To load, use: TabularPredictor.load(dataset/)
<mlmodels.model_gluon.util_autogluon.Model_empty object at 0x7fa044466908>

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
   3318768..1924086  master     -> origin/master
Updating 3318768..1924086
Fast-forward
 .../20200519/list_log_pullrequest_20200519.md      |   2 +-
 error_list/20200519/list_log_testall_20200519.md   | 175 +++++++++++++++++++++
 2 files changed, 176 insertions(+), 1 deletion(-)
[master e26951e] ml_store
 1 file changed, 206 insertions(+)
To github.com:arita37/mlmodels_store.git
   1924086..e26951e  master -> master





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
[master 115a5f2] ml_store
 1 file changed, 36 insertions(+)
To github.com:arita37/mlmodels_store.git
   e26951e..115a5f2  master -> master





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
100%|██████████| 10/10 [00:03<00:00,  3.22it/s, avg_epoch_loss=5.25]
INFO:root:Epoch[0] Elapsed time 3.105 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=5.254978
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 5.2549779415130615 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7fdcdc03a400>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7fdcdc03a400>

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
Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 81.43it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 1100.671142578125,
    "abs_error": 377.4593200683594,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 2.501026514564851,
    "sMAPE": 0.5197233088050784,
    "MSIS": 100.04106220025757,
    "QuantileLoss[0.5]": 377.45933532714844,
    "Coverage[0.5]": 1.0,
    "RMSE": 33.17636421578056,
    "NRMSE": 0.6984497729638013,
    "ND": 0.662209333453262,
    "wQuantileLoss[0.5]": 0.6622093602230674,
    "mean_wQuantileLoss": 0.6622093602230674,
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
100%|██████████| 10/10 [00:01<00:00,  6.76it/s, avg_epoch_loss=2.71e+3]
INFO:root:Epoch[0] Elapsed time 1.481 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=2713.411247
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 2713.4112467447917 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7fdcb020ef98>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7fdcb020ef98>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 132.07it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
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
100%|██████████| 10/10 [00:02<00:00,  4.81it/s, avg_epoch_loss=5.31]
INFO:root:Epoch[0] Elapsed time 2.079 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=5.313393
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 5.313393020629883 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7fdcb01200b8>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7fdcb01200b8>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 119.82it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 227.48236083984375,
    "abs_error": 155.89569091796875,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 1.0329570254660407,
    "sMAPE": 0.2653467858801288,
    "MSIS": 41.31828101864163,
    "QuantileLoss[0.5]": 155.89569854736328,
    "Coverage[0.5]": 0.6666666666666666,
    "RMSE": 15.082518385198266,
    "NRMSE": 0.3175267028462793,
    "ND": 0.2735012121367873,
    "wQuantileLoss[0.5]": 0.27350122552169,
    "mean_wQuantileLoss": 0.27350122552169,
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
 30%|███       | 3/10 [00:13<00:31,  4.52s/it, avg_epoch_loss=6.93] 60%|██████    | 6/10 [00:25<00:17,  4.34s/it, avg_epoch_loss=6.9]  90%|█████████ | 9/10 [00:37<00:04,  4.23s/it, avg_epoch_loss=6.87]100%|██████████| 10/10 [00:41<00:00,  4.11s/it, avg_epoch_loss=6.86]
INFO:root:Epoch[0] Elapsed time 41.146 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=6.863251
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 6.863251399993897 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7fdcb020eef0>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7fdcb020eef0>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 131.72it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 52680.3125,
    "abs_error": 2698.045166015625,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 17.8771118871208,
    "sMAPE": 1.4090189125002157,
    "MSIS": 715.0845143087569,
    "QuantileLoss[0.5]": 2698.045135498047,
    "Coverage[0.5]": 1.0,
    "RMSE": 229.52192161098688,
    "NRMSE": 4.832040454968145,
    "ND": 4.733412571957237,
    "wQuantileLoss[0.5]": 4.733412518417626,
    "mean_wQuantileLoss": 4.733412518417626,
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
100%|██████████| 10/10 [00:00<00:00, 45.57it/s, avg_epoch_loss=5.19]
INFO:root:Epoch[0] Elapsed time 0.220 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=5.191721
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 5.191720581054687 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7fdcb004f0f0>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7fdcb004f0f0>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 126.03it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
{
    "MSE": 542.9668375651041,
    "abs_error": 192.26612854003906,
    "abs_target_sum": 570.0,
    "abs_target_mean": 47.5,
    "seasonal_error": 12.576813222830921,
    "MASE": 1.273945720148824,
    "sMAPE": 0.32104468688023063,
    "MSIS": 50.95783123244825,
    "QuantileLoss[0.5]": 192.2661247253418,
    "Coverage[0.5]": 0.6666666666666666,
    "RMSE": 23.30164881644868,
    "NRMSE": 0.49056102771470905,
    "ND": 0.33730899743866505,
    "wQuantileLoss[0.5]": 0.3373089907462137,
    "mean_wQuantileLoss": 0.3373089907462137,
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
100%|██████████| 10/10 [00:01<00:00,  7.27it/s, avg_epoch_loss=161]
INFO:root:Epoch[0] Elapsed time 1.376 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=161.108291
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 161.1082910709855 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7fdcb020ef98>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7fdcb020ef98>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 126.67it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
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
 10%|█         | 1/10 [02:08<19:15, 128.36s/it, avg_epoch_loss=0.582] 20%|██        | 2/10 [05:15<19:28, 146.04s/it, avg_epoch_loss=0.565] 30%|███       | 3/10 [08:22<18:27, 158.16s/it, avg_epoch_loss=0.548] 40%|████      | 4/10 [11:51<17:20, 173.47s/it, avg_epoch_loss=0.531] 50%|█████     | 5/10 [15:30<15:34, 186.86s/it, avg_epoch_loss=0.515] 60%|██████    | 6/10 [19:15<13:14, 198.68s/it, avg_epoch_loss=0.499] 70%|███████   | 7/10 [22:57<10:17, 205.74s/it, avg_epoch_loss=0.484] 80%|████████  | 8/10 [26:27<06:54, 207.00s/it, avg_epoch_loss=0.47]  90%|█████████ | 9/10 [29:31<03:20, 200.14s/it, avg_epoch_loss=0.457]100%|██████████| 10/10 [32:56<00:00, 201.35s/it, avg_epoch_loss=0.447]100%|██████████| 10/10 [32:56<00:00, 197.62s/it, avg_epoch_loss=0.447]
INFO:root:Epoch[0] Elapsed time 1976.180 seconds
INFO:root:Epoch[0] Evaluation metric 'epoch_loss'=0.446552
INFO:root:Loading parameters from best epoch (0)
INFO:root:Final loss: 0.4465524971485138 (occurred at epoch 0)
INFO:root:End model training
<module 'mlmodels.model_gluon.gluonts_model' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_gluon/gluonts_model.py'> <mlmodels.model_gluon.gluonts_model.Model object at 0x7fdca882de10>
[array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
{'target': array([57., 43., 55., ..., 44., 61., 59.]), 'start': Timestamp('2015-02-26 21:42:53', freq='5T')}
learning rate from ``lr_scheduler`` has been overwritten by ``learning_rate`` in optimizer.
<mlmodels.model_gluon.gluonts_model.Model object at 0x7fdca882de10>

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
Running evaluation:   0%|          | 0/1 [00:00<?, ?it/s]Running evaluation: 100%|██████████| 1/1 [00:00<00:00, 18.22it/s][array([57., 43., 55., ..., 44., 61., 59.])] [Timestamp('2015-02-26 21:42:53', freq='5T')] [] []
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
   115a5f2..93a190b  master     -> origin/master
Updating 115a5f2..93a190b
Fast-forward
 error_list/20200519/list_log_pullrequest_20200519.md | 2 +-
 error_list/20200519/list_log_testall_20200519.md     | 7 +++++++
 2 files changed, 8 insertions(+), 1 deletion(-)
[master 7d67659] ml_store
 1 file changed, 506 insertions(+)
To github.com:arita37/mlmodels_store.git
   93a190b..7d67659  master -> master





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

  <mlmodels.model_sklearn.model_sklearn.Model object at 0x7f1442b43518> 

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
[master 332014f] ml_store
 1 file changed, 109 insertions(+)
To github.com:arita37/mlmodels_store.git
   7d67659..332014f  master -> master





 ************************************************************************************************************************

  python /home/runner/work/mlmodels/mlmodels/mlmodels/model_sklearn//model_lightgbm.py 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Loading dataset   ############################################# 

  #### Model init, fit   ############################################# 

  #### save the trained model  ####################################### 

  #### Predict   ##################################################### 
[[ 1.24549398 -0.72239191  1.1181334   1.09899633  1.00277655 -0.90163449
  -0.53223402 -0.82246719  0.72171129  0.6743961 ]
 [ 1.46893146 -1.47115693  0.58591043 -0.8301719   1.03345052 -0.8805776
  -0.95542526 -0.27909772  1.62284909  2.06578332]
 [ 1.25704434 -1.82391985 -0.61240697  1.16707517 -0.62373281 -0.0396687
   0.81604368  0.8858258   0.18986165  0.39310924]
 [ 0.87226739 -2.51630386 -0.77507029 -0.59566788  1.02600767 -0.30912132
   1.74643509  0.51093777  1.71066184  0.14164054]
 [ 0.77528533  1.47016034  1.03298378 -0.87000822  0.78655651  0.36919047
  -0.14319575  0.85328219 -0.13971173 -0.22241403]
 [ 0.46739791 -0.23787527 -0.15449119 -0.75566277 -0.54706224  1.85143789
  -1.46405357  0.20909668  1.55501599 -0.09243232]
 [ 1.01195228 -1.88141087  1.70018815  0.4972691  -0.91766462  0.2373327
  -1.09033833 -2.14444405 -0.36956243  0.60878366]
 [ 0.89562312 -2.29820588 -0.01952256  1.45652739 -1.85064099  0.31663724
   0.11133727 -2.66412594 -0.42642862 -0.83998891]
 [ 0.68188934 -1.15498263  1.22895559 -0.1776322   0.99854519 -1.51045638
  -0.27584606  1.01120706 -1.47656266  1.30970591]
 [ 0.99785516 -0.6001388   0.45794708  0.14676526 -0.93355729  0.57180488
   0.57296273 -0.03681766  0.11236849 -0.01781755]
 [ 1.18947778 -0.68067814 -0.05682448 -0.08450803  0.82178321 -0.29736188
  -0.18657899  0.417302    0.78477065  0.49233656]
 [ 0.88838944  0.28299553  0.01795589  0.10803082 -0.84967187  0.02941762
  -0.50397395 -0.13479313  1.04921829 -1.27046078]
 [ 1.37661405 -0.60022533  0.72591685 -0.37951752 -0.62754626 -1.01480369
   0.96622086  0.4359862  -0.68748739  3.32107876]
 [ 0.5630779  -1.17598267 -0.17418034  1.01012718  1.06796368  0.92001793
  -0.16819884 -0.19505734  0.80539342  0.4611641 ]
 [ 0.6109426  -2.79099641 -1.33520272 -0.45611756 -0.94495995 -0.97989025
  -0.15699367  0.69257435 -0.47867236 -0.10646012]
 [ 1.21619061 -0.01900052  0.86089124 -0.22676019 -1.36419132 -1.56450785
   1.63169151  0.93125568  0.94980882 -0.88018906]
 [ 0.81583612 -1.39169388  2.50598029  0.45021774 -0.88286982  0.62743708
  -1.19586151  0.75133724  0.14039544  1.91979229]
 [ 1.27991386 -0.87142207 -0.32403233 -0.86482994 -0.96853969  0.60874908
   0.50798434  0.5616381   1.51475038 -1.51107661]
 [ 0.84806927  0.45194604  0.63019567 -1.57915629  0.82798737 -0.82862798
  -0.10534471  0.52887975 -2.23708651 -0.4148469 ]
 [ 1.13545112  0.8616231   0.04906169 -2.08639057 -1.1146902   0.36180164
  -0.80617821  0.42592018  0.0490804  -0.59608633]
 [ 0.78801845  0.30196005  0.70098212 -0.39468968 -1.20376927 -1.17181338
   0.75539203  0.98401224 -0.55968142 -0.19893745]
 [ 0.94781411 -1.13379204  0.64098587 -0.1905483  -1.23912256  0.23333913
  -0.3169012   0.43499832  0.9104236   1.21987438]
 [ 0.87874071 -0.01923163  0.31965694  0.15001628 -1.46662161  0.46353432
  -0.89868319  0.39788042 -0.99601089  0.3181542 ]
 [ 0.85877496  2.29371761 -1.47023709 -0.83001099 -0.67204982 -1.01951985
   0.59921324 -0.21465384  1.02124813  0.60640394]
 [ 1.14809657 -0.7332716   0.26246745  0.83600472  1.17353145  1.54335911
   0.28474811  0.75880566  0.88490881  0.2764993 ]]

  #### metrics   ##################################################### 
{}

  #### Plot   ######################################################## 

  #### Save/Load   ################################################### 
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_sklearn/model_lightgbm/model.pkl'}
{'path': '/home/runner/work/mlmodels/mlmodels/mlmodels/ztest/model_sklearn/model_lightgbm/model.pkl'}
<__main__.Model object at 0x7fd23e0f4d68>

  #### Module init   ############################################ 

  <module 'mlmodels.model_sklearn.model_lightgbm' from '/home/runner/work/mlmodels/mlmodels/mlmodels/model_sklearn/model_lightgbm.py'> 

  #### Loading params   ############################################## 

  #### Path params   ########################################## 

  #### Model init   ############################################ 

  <mlmodels.model_sklearn.model_lightgbm.Model object at 0x7fd2584725c0> 

  #### Fit   ######################################################## 

  #### Predict   #################################################### 
[[ 0.99785516 -0.6001388   0.45794708  0.14676526 -0.93355729  0.57180488
   0.57296273 -0.03681766  0.11236849 -0.01781755]
 [ 0.6675918  -0.45252497 -0.60598132  1.16128569 -1.44620987  1.06996554
   1.92381543 -1.04553425  0.35528451  1.80358898]
 [ 0.84806927  0.45194604  0.63019567 -1.57915629  0.82798737 -0.82862798
  -0.10534471  0.52887975 -2.23708651 -0.4148469 ]
 [ 1.58463774  0.057121   -0.01771832 -0.79954749  1.32970299 -0.2915946
  -1.1077125  -0.25898285  0.1892932  -1.71939447]
 [ 0.10593645 -0.73728963  0.65032321  0.16466507 -1.53556118  0.77817418
   0.05031709  0.30981676  1.05132077  0.6065484 ]
 [ 1.64661853 -1.52568032 -0.6069984   0.79502609  1.08480038 -0.37443832
   0.42952614  0.1340482   1.20205486  0.10622272]
 [ 0.62567337  0.5924728   0.67457071  1.19783084  1.23187251  1.70459417
  -0.76730983  1.04008915 -0.91844004  1.46089238]
 [ 1.838294    0.50274088  0.12910158  1.55880554  1.32551412  0.1094027
   1.40754    -1.2197444   2.44936865  1.6169496 ]
 [ 1.03967316 -0.73153098  0.36184732 -1.56573815  0.95928819  1.01382247
  -1.78791289 -2.22711263 -1.6993336  -0.42449279]
 [ 0.98379959 -0.40724002  0.93272141  0.16056499 -1.278618   -0.12014998
   0.19975956  0.38560229  0.71829074 -0.5301198 ]
 [ 1.14809657 -0.7332716   0.26246745  0.83600472  1.17353145  1.54335911
   0.28474811  0.75880566  0.88490881  0.2764993 ]
 [ 0.345716   -0.41302931 -0.46867382  1.83471763  0.77151441  0.56438286
   0.02186284  2.13782807 -0.785534    0.85328122]
 [ 1.18559003  0.08646441  1.23289919 -2.14246673  1.033341   -0.83016886
   0.36723181  0.45161595  1.10417433 -0.42285696]
 [ 1.01177337  0.09574677  0.73140252  1.0334508  -1.42203164 -0.14627327
  -0.01745495 -0.85749682 -0.93418184  0.95449567]
 [ 1.07258847 -0.58652394 -1.34267579 -1.23685338  1.24328724  0.87583893
  -0.3264995   0.62336218 -0.43495668  1.11438298]
 [ 1.06040861  0.5103076   0.50172511 -0.91579185 -0.90731836 -0.40725204
  -0.17961229  0.98495167  1.07125243 -0.59334375]
 [ 0.89891716  0.55743945 -0.75806733  0.18103874  0.84146721  1.10717545
   0.69336623  1.44287693 -0.53968156 -0.8088472 ]
 [ 1.18468624 -1.00016919 -0.59384307  1.04499441  0.96548233  0.6085147
  -0.625342   -0.0693287  -0.10839207 -0.34390071]
 [ 0.78344054 -0.05118845  0.82458463 -0.72559712  0.9317172  -0.86776868
   3.03085711 -0.13597733 -0.79726979  0.65458015]
 [ 1.01195228 -1.88141087  1.70018815  0.4972691  -0.91766462  0.2373327
  -1.09033833 -2.14444405 -0.36956243  0.60878366]
 [ 0.85335555 -0.70435033 -0.67938378 -0.04586669 -1.29936179 -0.21873346
   0.59003946  1.53920701 -1.14870423 -0.95090925]
 [ 2.07582971 -1.40232915 -0.47918492  0.45112294  1.03436581 -0.6949209
  -0.4189379   0.5154138  -1.11487105 -1.95210529]
 [ 1.06702918 -0.42914228  0.35016716  1.20845633  0.75148062  1.1157018
  -0.4791571   0.84086156 -0.10288722  0.01716473]
 [ 1.16755486  0.0353601   0.7147896  -1.53879325  1.10863359 -0.44789518
  -1.75592564  0.61798553 -0.18417633  0.85270406]
 [ 0.76170668 -1.48515645  1.30253554 -0.59246129 -1.64162479 -2.30490794
  -1.34869645 -0.03181717  0.11248774 -0.36261209]]
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
[[ 1.66752297e+00  1.22372221e+00 -4.59930104e-01 -5.93679025e-02
  -4.93856997e-01  1.44898940e+00 -1.18110317e+00 -4.77580855e-01
   2.59999942e-02 -7.90799954e-01]
 [ 1.18947778e+00 -6.80678141e-01 -5.68244809e-02 -8.45080274e-02
   8.21783210e-01 -2.97361883e-01 -1.86578994e-01  4.17302005e-01
   7.84770651e-01  4.92336556e-01]
 [ 6.25673373e-01  5.92472801e-01  6.74570707e-01  1.19783084e+00
   1.23187251e+00  1.70459417e+00 -7.67309826e-01  1.04008915e+00
  -9.18440038e-01  1.46089238e+00]
 [ 1.98519313e+00  6.74711526e-01 -1.39662042e+00  6.18539131e-01
   1.22382712e+00 -4.43171931e-01 -1.89148284e-03  1.81053491e+00
  -1.30572692e+00 -8.61316361e-01]
 [ 9.83799588e-01 -4.07240024e-01  9.32721414e-01  1.60564992e-01
  -1.27861800e+00 -1.20149976e-01  1.99759555e-01  3.85602292e-01
   7.18290736e-01 -5.30119800e-01]
 [ 8.53355545e-01 -7.04350332e-01 -6.79383783e-01 -4.58666861e-02
  -1.29936179e+00 -2.18733459e-01  5.90039464e-01  1.53920701e+00
  -1.14870423e+00 -9.50909251e-01]
 [ 8.57296491e-01  9.56121704e-01 -8.26097432e-01 -7.05840507e-01
   1.13872896e+00  1.19268607e+00  2.82675712e-01 -2.37941936e-01
   1.15528789e+00  6.21082701e-01]
 [ 9.71395338e-01  7.13049050e-01  1.76041518e+00  1.30620607e+00
   1.05765490e+00 -6.04602969e-01  1.28376990e-01  6.36583409e-01
   1.40925339e+00  9.66539250e-01]
 [ 1.34728643e+00 -3.64538050e-01  8.07509886e-02 -4.59717681e-01
  -8.89487596e-01  1.70548352e+00  9.49961101e-02  2.40505552e-01
  -9.99426501e-01 -7.67803746e-01]
 [ 1.06040861e+00  5.10307597e-01  5.01725109e-01 -9.15791849e-01
  -9.07318361e-01 -4.07252043e-01 -1.79612295e-01  9.84951672e-01
   1.07125243e+00 -5.93343754e-01]
 [ 1.14377130e+00  7.27813500e-01  3.52494364e-01  5.15073614e-01
   1.17718111e+00 -2.78253447e+00 -1.94332341e+00  5.84646610e-01
   3.24274243e-01 -2.36436952e-01]
 [ 1.03967316e+00 -7.31530982e-01  3.61847316e-01 -1.56573815e+00
   9.59288190e-01  1.01382247e+00 -1.78791289e+00 -2.22711263e+00
  -1.69933360e+00 -4.24492791e-01]
 [ 6.23629500e-01  9.86352180e-01  1.45391758e+00 -4.66154857e-01
   9.36403332e-01  1.38499134e+00  3.49435894e-02 -1.07296428e+00
   4.95158611e-01  6.61681076e-01]
 [ 1.25704434e+00 -1.82391985e+00 -6.12406973e-01  1.16707517e+00
  -6.23732812e-01 -3.96687001e-02  8.16043684e-01  8.85825799e-01
   1.89861649e-01  3.93109245e-01]
 [ 2.07582971e+00 -1.40232915e+00 -4.79184915e-01  4.51122939e-01
   1.03436581e+00 -6.94920901e-01 -4.18937898e-01  5.15413802e-01
  -1.11487105e+00 -1.95210529e+00]
 [ 8.72267394e-01 -2.51630386e+00 -7.75070287e-01 -5.95667881e-01
   1.02600767e+00 -3.09121319e-01  1.74643509e+00  5.10937774e-01
   1.71066184e+00  1.41640538e-01]
 [ 1.06523311e+00 -6.64867767e-01  1.00806543e+00 -1.94504696e+00
  -1.23017555e+00 -9.15424368e-01  3.37220938e-01  1.22515585e+00
  -1.05354607e+00  7.85226920e-01]
 [ 1.18559003e+00  8.64644065e-02  1.23289919e+00 -2.14246673e+00
   1.03334100e+00 -8.30168864e-01  3.67231814e-01  4.51615951e-01
   1.10417433e+00 -4.22856961e-01]
 [ 9.64572049e-01 -1.06793987e-01  1.12232832e+00  1.45142926e+00
   1.21828168e+00 -6.18036848e-01  4.38166347e-01 -2.03720123e+00
  -1.94258918e+00 -9.97019796e-01]
 [ 6.81889336e-01 -1.15498263e+00  1.22895559e+00 -1.77632196e-01
   9.98545187e-01 -1.51045638e+00 -2.75846063e-01  1.01120706e+00
  -1.47656266e+00  1.30970591e+00]
 [ 6.18390447e-01 -7.25214926e-01  4.00084198e-03  1.53653633e+00
  -1.03048932e+00 -3.75008758e-04  5.31163793e-01  1.29354962e+00
  -4.38997664e-01  3.21265914e-01]
 [ 1.32857949e+00 -5.63236604e-01 -1.06179676e+00  2.39014596e+00
  -1.68450770e+00  2.45422849e-01 -5.69148654e-01  1.15259914e+00
  -2.24235772e-01  1.32247779e-01]
 [ 9.97855163e-01 -6.00138799e-01  4.57947076e-01  1.46765263e-01
  -9.33557290e-01  5.71804879e-01  5.72962726e-01 -3.68176565e-02
   1.12368489e-01 -1.78175491e-02]
 [ 1.37661405e+00 -6.00225330e-01  7.25916853e-01 -3.79517516e-01
  -6.27546260e-01 -1.01480369e+00  9.66220863e-01  4.35986196e-01
  -6.87487393e-01  3.32107876e+00]
 [ 9.47814113e-01 -1.13379204e+00  6.40985866e-01 -1.90548298e-01
  -1.23912256e+00  2.33339126e-01 -3.16901197e-01  4.34998324e-01
   9.10423603e-01  1.21987438e+00]]
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
[master 60dafa1] ml_store
 1 file changed, 272 insertions(+)
To github.com:arita37/mlmodels_store.git
   332014f..60dafa1  master -> master





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
     | -- GenericBlock(units=256, thetas_dim=7, backcast_length=10, forecast_length=5, share_thetas=False) at @139684496080848
     | -- GenericBlock(units=256, thetas_dim=7, backcast_length=10, forecast_length=5, share_thetas=False) at @139684496080624
     | -- GenericBlock(units=256, thetas_dim=7, backcast_length=10, forecast_length=5, share_thetas=False) at @139684496079392
| --  Stack Generic (#1) (share_weights_in_stack=0)
     | -- GenericBlock(units=256, thetas_dim=8, backcast_length=10, forecast_length=5, share_thetas=False) at @139684496078944
     | -- GenericBlock(units=256, thetas_dim=8, backcast_length=10, forecast_length=5, share_thetas=False) at @139684496078440
     | -- GenericBlock(units=256, thetas_dim=8, backcast_length=10, forecast_length=5, share_thetas=False) at @139684496078104

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
grad_step = 000000, loss = 0.449248
plot()
Saved image to .//n_beats_0.png.
grad_step = 000001, loss = 0.320078
grad_step = 000002, loss = 0.244262
grad_step = 000003, loss = 0.165616
grad_step = 000004, loss = 0.087714
grad_step = 000005, loss = 0.037241
grad_step = 000006, loss = 0.043177
grad_step = 000007, loss = 0.059305
grad_step = 000008, loss = 0.044832
grad_step = 000009, loss = 0.025718
grad_step = 000010, loss = 0.018824
grad_step = 000011, loss = 0.021198
grad_step = 000012, loss = 0.025203
grad_step = 000013, loss = 0.026564
grad_step = 000014, loss = 0.024965
grad_step = 000015, loss = 0.021034
grad_step = 000016, loss = 0.016148
grad_step = 000017, loss = 0.012118
grad_step = 000018, loss = 0.010430
grad_step = 000019, loss = 0.011299
grad_step = 000020, loss = 0.013120
grad_step = 000021, loss = 0.013697
grad_step = 000022, loss = 0.012224
grad_step = 000023, loss = 0.009723
grad_step = 000024, loss = 0.007772
grad_step = 000025, loss = 0.007227
grad_step = 000026, loss = 0.007880
grad_step = 000027, loss = 0.008902
grad_step = 000028, loss = 0.009508
grad_step = 000029, loss = 0.009340
grad_step = 000030, loss = 0.008496
grad_step = 000031, loss = 0.007355
grad_step = 000032, loss = 0.006392
grad_step = 000033, loss = 0.005966
grad_step = 000034, loss = 0.006152
grad_step = 000035, loss = 0.006695
grad_step = 000036, loss = 0.007141
grad_step = 000037, loss = 0.007170
grad_step = 000038, loss = 0.006774
grad_step = 000039, loss = 0.006209
grad_step = 000040, loss = 0.005773
grad_step = 000041, loss = 0.005626
grad_step = 000042, loss = 0.005728
grad_step = 000043, loss = 0.005912
grad_step = 000044, loss = 0.006002
grad_step = 000045, loss = 0.005930
grad_step = 000046, loss = 0.005735
grad_step = 000047, loss = 0.005520
grad_step = 000048, loss = 0.005383
grad_step = 000049, loss = 0.005355
grad_step = 000050, loss = 0.005390
grad_step = 000051, loss = 0.005407
grad_step = 000052, loss = 0.005368
grad_step = 000053, loss = 0.005289
grad_step = 000054, loss = 0.005211
grad_step = 000055, loss = 0.005159
grad_step = 000056, loss = 0.005122
grad_step = 000057, loss = 0.005076
grad_step = 000058, loss = 0.005007
grad_step = 000059, loss = 0.004936
grad_step = 000060, loss = 0.004888
grad_step = 000061, loss = 0.004873
grad_step = 000062, loss = 0.004868
grad_step = 000063, loss = 0.004834
grad_step = 000064, loss = 0.004761
grad_step = 000065, loss = 0.004675
grad_step = 000066, loss = 0.004613
grad_step = 000067, loss = 0.004582
grad_step = 000068, loss = 0.004560
grad_step = 000069, loss = 0.004522
grad_step = 000070, loss = 0.004464
grad_step = 000071, loss = 0.004397
grad_step = 000072, loss = 0.004336
grad_step = 000073, loss = 0.004281
grad_step = 000074, loss = 0.004230
grad_step = 000075, loss = 0.004171
grad_step = 000076, loss = 0.004110
grad_step = 000077, loss = 0.004049
grad_step = 000078, loss = 0.003984
grad_step = 000079, loss = 0.003915
grad_step = 000080, loss = 0.003845
grad_step = 000081, loss = 0.003783
grad_step = 000082, loss = 0.003716
grad_step = 000083, loss = 0.003641
grad_step = 000084, loss = 0.003565
grad_step = 000085, loss = 0.003487
grad_step = 000086, loss = 0.003405
grad_step = 000087, loss = 0.003324
grad_step = 000088, loss = 0.003241
grad_step = 000089, loss = 0.003157
grad_step = 000090, loss = 0.003072
grad_step = 000091, loss = 0.002985
grad_step = 000092, loss = 0.002900
grad_step = 000093, loss = 0.002813
grad_step = 000094, loss = 0.002724
grad_step = 000095, loss = 0.002633
grad_step = 000096, loss = 0.002545
grad_step = 000097, loss = 0.002462
grad_step = 000098, loss = 0.002382
grad_step = 000099, loss = 0.002298
grad_step = 000100, loss = 0.002233
plot()
Saved image to .//n_beats_100.png.
grad_step = 000101, loss = 0.002137
grad_step = 000102, loss = 0.002065
grad_step = 000103, loss = 0.001992
grad_step = 000104, loss = 0.001916
grad_step = 000105, loss = 0.001847
grad_step = 000106, loss = 0.001785
grad_step = 000107, loss = 0.001723
grad_step = 000108, loss = 0.001662
grad_step = 000109, loss = 0.001604
grad_step = 000110, loss = 0.001550
grad_step = 000111, loss = 0.001503
grad_step = 000112, loss = 0.001460
grad_step = 000113, loss = 0.001410
grad_step = 000114, loss = 0.001350
grad_step = 000115, loss = 0.001306
grad_step = 000116, loss = 0.001273
grad_step = 000117, loss = 0.001225
grad_step = 000118, loss = 0.001187
grad_step = 000119, loss = 0.001168
grad_step = 000120, loss = 0.001146
grad_step = 000121, loss = 0.001121
grad_step = 000122, loss = 0.001105
grad_step = 000123, loss = 0.001092
grad_step = 000124, loss = 0.001078
grad_step = 000125, loss = 0.001057
grad_step = 000126, loss = 0.001035
grad_step = 000127, loss = 0.001019
grad_step = 000128, loss = 0.001000
grad_step = 000129, loss = 0.000979
grad_step = 000130, loss = 0.000962
grad_step = 000131, loss = 0.000944
grad_step = 000132, loss = 0.000931
grad_step = 000133, loss = 0.000919
grad_step = 000134, loss = 0.000904
grad_step = 000135, loss = 0.000894
grad_step = 000136, loss = 0.000885
grad_step = 000137, loss = 0.000877
grad_step = 000138, loss = 0.000866
grad_step = 000139, loss = 0.000855
grad_step = 000140, loss = 0.000843
grad_step = 000141, loss = 0.000834
grad_step = 000142, loss = 0.000827
grad_step = 000143, loss = 0.000819
grad_step = 000144, loss = 0.000811
grad_step = 000145, loss = 0.000802
grad_step = 000146, loss = 0.000793
grad_step = 000147, loss = 0.000784
grad_step = 000148, loss = 0.000777
grad_step = 000149, loss = 0.000771
grad_step = 000150, loss = 0.000766
grad_step = 000151, loss = 0.000761
grad_step = 000152, loss = 0.000755
grad_step = 000153, loss = 0.000749
grad_step = 000154, loss = 0.000742
grad_step = 000155, loss = 0.000735
grad_step = 000156, loss = 0.000726
grad_step = 000157, loss = 0.000717
grad_step = 000158, loss = 0.000711
grad_step = 000159, loss = 0.000706
grad_step = 000160, loss = 0.000704
grad_step = 000161, loss = 0.000701
grad_step = 000162, loss = 0.000699
grad_step = 000163, loss = 0.000698
grad_step = 000164, loss = 0.000700
grad_step = 000165, loss = 0.000697
grad_step = 000166, loss = 0.000684
grad_step = 000167, loss = 0.000669
grad_step = 000168, loss = 0.000668
grad_step = 000169, loss = 0.000673
grad_step = 000170, loss = 0.000667
grad_step = 000171, loss = 0.000655
grad_step = 000172, loss = 0.000651
grad_step = 000173, loss = 0.000654
grad_step = 000174, loss = 0.000652
grad_step = 000175, loss = 0.000643
grad_step = 000176, loss = 0.000638
grad_step = 000177, loss = 0.000639
grad_step = 000178, loss = 0.000638
grad_step = 000179, loss = 0.000633
grad_step = 000180, loss = 0.000627
grad_step = 000181, loss = 0.000627
grad_step = 000182, loss = 0.000628
grad_step = 000183, loss = 0.000623
grad_step = 000184, loss = 0.000615
grad_step = 000185, loss = 0.000610
grad_step = 000186, loss = 0.000610
grad_step = 000187, loss = 0.000611
grad_step = 000188, loss = 0.000608
grad_step = 000189, loss = 0.000602
grad_step = 000190, loss = 0.000597
grad_step = 000191, loss = 0.000597
grad_step = 000192, loss = 0.000597
grad_step = 000193, loss = 0.000594
grad_step = 000194, loss = 0.000589
grad_step = 000195, loss = 0.000584
grad_step = 000196, loss = 0.000581
grad_step = 000197, loss = 0.000580
grad_step = 000198, loss = 0.000580
grad_step = 000199, loss = 0.000579
grad_step = 000200, loss = 0.000575
plot()
Saved image to .//n_beats_200.png.
grad_step = 000201, loss = 0.000571
grad_step = 000202, loss = 0.000568
grad_step = 000203, loss = 0.000568
grad_step = 000204, loss = 0.000574
grad_step = 000205, loss = 0.000589
grad_step = 000206, loss = 0.000592
grad_step = 000207, loss = 0.000571
grad_step = 000208, loss = 0.000554
grad_step = 000209, loss = 0.000569
grad_step = 000210, loss = 0.000572
grad_step = 000211, loss = 0.000551
grad_step = 000212, loss = 0.000553
grad_step = 000213, loss = 0.000561
grad_step = 000214, loss = 0.000545
grad_step = 000215, loss = 0.000541
grad_step = 000216, loss = 0.000548
grad_step = 000217, loss = 0.000539
grad_step = 000218, loss = 0.000531
grad_step = 000219, loss = 0.000537
grad_step = 000220, loss = 0.000533
grad_step = 000221, loss = 0.000525
grad_step = 000222, loss = 0.000527
grad_step = 000223, loss = 0.000529
grad_step = 000224, loss = 0.000525
grad_step = 000225, loss = 0.000530
grad_step = 000226, loss = 0.000542
grad_step = 000227, loss = 0.000554
grad_step = 000228, loss = 0.000556
grad_step = 000229, loss = 0.000546
grad_step = 000230, loss = 0.000518
grad_step = 000231, loss = 0.000504
grad_step = 000232, loss = 0.000517
grad_step = 000233, loss = 0.000529
grad_step = 000234, loss = 0.000518
grad_step = 000235, loss = 0.000500
grad_step = 000236, loss = 0.000498
grad_step = 000237, loss = 0.000506
grad_step = 000238, loss = 0.000505
grad_step = 000239, loss = 0.000497
grad_step = 000240, loss = 0.000488
grad_step = 000241, loss = 0.000488
grad_step = 000242, loss = 0.000492
grad_step = 000243, loss = 0.000491
grad_step = 000244, loss = 0.000483
grad_step = 000245, loss = 0.000477
grad_step = 000246, loss = 0.000478
grad_step = 000247, loss = 0.000481
grad_step = 000248, loss = 0.000478
grad_step = 000249, loss = 0.000471
grad_step = 000250, loss = 0.000467
grad_step = 000251, loss = 0.000468
grad_step = 000252, loss = 0.000468
grad_step = 000253, loss = 0.000465
grad_step = 000254, loss = 0.000462
grad_step = 000255, loss = 0.000458
grad_step = 000256, loss = 0.000456
grad_step = 000257, loss = 0.000455
grad_step = 000258, loss = 0.000454
grad_step = 000259, loss = 0.000452
grad_step = 000260, loss = 0.000450
grad_step = 000261, loss = 0.000448
grad_step = 000262, loss = 0.000445
grad_step = 000263, loss = 0.000442
grad_step = 000264, loss = 0.000440
grad_step = 000265, loss = 0.000439
grad_step = 000266, loss = 0.000437
grad_step = 000267, loss = 0.000436
grad_step = 000268, loss = 0.000435
grad_step = 000269, loss = 0.000434
grad_step = 000270, loss = 0.000433
grad_step = 000271, loss = 0.000433
grad_step = 000272, loss = 0.000434
grad_step = 000273, loss = 0.000437
grad_step = 000274, loss = 0.000441
grad_step = 000275, loss = 0.000446
grad_step = 000276, loss = 0.000450
grad_step = 000277, loss = 0.000445
grad_step = 000278, loss = 0.000434
grad_step = 000279, loss = 0.000419
grad_step = 000280, loss = 0.000410
grad_step = 000281, loss = 0.000409
grad_step = 000282, loss = 0.000413
grad_step = 000283, loss = 0.000418
grad_step = 000284, loss = 0.000420
grad_step = 000285, loss = 0.000417
grad_step = 000286, loss = 0.000409
grad_step = 000287, loss = 0.000401
grad_step = 000288, loss = 0.000395
grad_step = 000289, loss = 0.000395
grad_step = 000290, loss = 0.000396
grad_step = 000291, loss = 0.000397
grad_step = 000292, loss = 0.000398
grad_step = 000293, loss = 0.000395
grad_step = 000294, loss = 0.000391
grad_step = 000295, loss = 0.000389
grad_step = 000296, loss = 0.000387
grad_step = 000297, loss = 0.000385
grad_step = 000298, loss = 0.000385
grad_step = 000299, loss = 0.000388
grad_step = 000300, loss = 0.000392
plot()
Saved image to .//n_beats_300.png.
grad_step = 000301, loss = 0.000397
grad_step = 000302, loss = 0.000398
grad_step = 000303, loss = 0.000394
grad_step = 000304, loss = 0.000385
grad_step = 000305, loss = 0.000378
grad_step = 000306, loss = 0.000380
grad_step = 000307, loss = 0.000383
grad_step = 000308, loss = 0.000383
grad_step = 000309, loss = 0.000372
grad_step = 000310, loss = 0.000363
grad_step = 000311, loss = 0.000360
grad_step = 000312, loss = 0.000361
grad_step = 000313, loss = 0.000360
grad_step = 000314, loss = 0.000357
grad_step = 000315, loss = 0.000355
grad_step = 000316, loss = 0.000353
grad_step = 000317, loss = 0.000350
grad_step = 000318, loss = 0.000346
grad_step = 000319, loss = 0.000348
grad_step = 000320, loss = 0.000356
grad_step = 000321, loss = 0.000372
grad_step = 000322, loss = 0.000394
grad_step = 000323, loss = 0.000431
grad_step = 000324, loss = 0.000441
grad_step = 000325, loss = 0.000432
grad_step = 000326, loss = 0.000362
grad_step = 000327, loss = 0.000342
grad_step = 000328, loss = 0.000366
grad_step = 000329, loss = 0.000385
grad_step = 000330, loss = 0.000381
grad_step = 000331, loss = 0.000355
grad_step = 000332, loss = 0.000326
grad_step = 000333, loss = 0.000343
grad_step = 000334, loss = 0.000360
grad_step = 000335, loss = 0.000352
grad_step = 000336, loss = 0.000331
grad_step = 000337, loss = 0.000328
grad_step = 000338, loss = 0.000333
grad_step = 000339, loss = 0.000330
grad_step = 000340, loss = 0.000328
grad_step = 000341, loss = 0.000321
grad_step = 000342, loss = 0.000317
grad_step = 000343, loss = 0.000316
grad_step = 000344, loss = 0.000319
grad_step = 000345, loss = 0.000320
grad_step = 000346, loss = 0.000313
grad_step = 000347, loss = 0.000308
grad_step = 000348, loss = 0.000305
grad_step = 000349, loss = 0.000310
grad_step = 000350, loss = 0.000310
grad_step = 000351, loss = 0.000308
grad_step = 000352, loss = 0.000303
grad_step = 000353, loss = 0.000300
grad_step = 000354, loss = 0.000299
grad_step = 000355, loss = 0.000297
grad_step = 000356, loss = 0.000297
grad_step = 000357, loss = 0.000297
grad_step = 000358, loss = 0.000298
grad_step = 000359, loss = 0.000296
grad_step = 000360, loss = 0.000294
grad_step = 000361, loss = 0.000292
grad_step = 000362, loss = 0.000291
grad_step = 000363, loss = 0.000293
grad_step = 000364, loss = 0.000296
grad_step = 000365, loss = 0.000303
grad_step = 000366, loss = 0.000318
grad_step = 000367, loss = 0.000335
grad_step = 000368, loss = 0.000374
grad_step = 000369, loss = 0.000368
grad_step = 000370, loss = 0.000359
grad_step = 000371, loss = 0.000332
grad_step = 000372, loss = 0.000309
grad_step = 000373, loss = 0.000289
grad_step = 000374, loss = 0.000295
grad_step = 000375, loss = 0.000316
grad_step = 000376, loss = 0.000317
grad_step = 000377, loss = 0.000310
grad_step = 000378, loss = 0.000304
grad_step = 000379, loss = 0.000314
grad_step = 000380, loss = 0.000311
grad_step = 000381, loss = 0.000300
grad_step = 000382, loss = 0.000288
grad_step = 000383, loss = 0.000281
grad_step = 000384, loss = 0.000275
grad_step = 000385, loss = 0.000274
grad_step = 000386, loss = 0.000281
grad_step = 000387, loss = 0.000289
grad_step = 000388, loss = 0.000290
grad_step = 000389, loss = 0.000282
grad_step = 000390, loss = 0.000281
grad_step = 000391, loss = 0.000282
grad_step = 000392, loss = 0.000283
grad_step = 000393, loss = 0.000274
grad_step = 000394, loss = 0.000267
grad_step = 000395, loss = 0.000264
grad_step = 000396, loss = 0.000263
grad_step = 000397, loss = 0.000262
grad_step = 000398, loss = 0.000265
grad_step = 000399, loss = 0.000269
grad_step = 000400, loss = 0.000269
plot()
Saved image to .//n_beats_400.png.
grad_step = 000401, loss = 0.000268
grad_step = 000402, loss = 0.000270
grad_step = 000403, loss = 0.000280
grad_step = 000404, loss = 0.000293
grad_step = 000405, loss = 0.000313
grad_step = 000406, loss = 0.000328
grad_step = 000407, loss = 0.000345
grad_step = 000408, loss = 0.000340
grad_step = 000409, loss = 0.000333
grad_step = 000410, loss = 0.000307
grad_step = 000411, loss = 0.000285
grad_step = 000412, loss = 0.000257
grad_step = 000413, loss = 0.000254
grad_step = 000414, loss = 0.000274
grad_step = 000415, loss = 0.000288
grad_step = 000416, loss = 0.000296
grad_step = 000417, loss = 0.000283
grad_step = 000418, loss = 0.000267
grad_step = 000419, loss = 0.000254
grad_step = 000420, loss = 0.000250
grad_step = 000421, loss = 0.000251
grad_step = 000422, loss = 0.000253
grad_step = 000423, loss = 0.000256
grad_step = 000424, loss = 0.000262
grad_step = 000425, loss = 0.000268
grad_step = 000426, loss = 0.000264
grad_step = 000427, loss = 0.000255
grad_step = 000428, loss = 0.000245
grad_step = 000429, loss = 0.000242
grad_step = 000430, loss = 0.000240
grad_step = 000431, loss = 0.000238
grad_step = 000432, loss = 0.000236
grad_step = 000433, loss = 0.000239
grad_step = 000434, loss = 0.000245
grad_step = 000435, loss = 0.000252
grad_step = 000436, loss = 0.000260
grad_step = 000437, loss = 0.000268
grad_step = 000438, loss = 0.000282
grad_step = 000439, loss = 0.000289
grad_step = 000440, loss = 0.000299
grad_step = 000441, loss = 0.000299
grad_step = 000442, loss = 0.000298
grad_step = 000443, loss = 0.000278
grad_step = 000444, loss = 0.000251
grad_step = 000445, loss = 0.000232
grad_step = 000446, loss = 0.000232
grad_step = 000447, loss = 0.000241
grad_step = 000448, loss = 0.000248
grad_step = 000449, loss = 0.000253
grad_step = 000450, loss = 0.000259
grad_step = 000451, loss = 0.000273
grad_step = 000452, loss = 0.000275
grad_step = 000453, loss = 0.000276
grad_step = 000454, loss = 0.000256
grad_step = 000455, loss = 0.000243
grad_step = 000456, loss = 0.000238
grad_step = 000457, loss = 0.000235
grad_step = 000458, loss = 0.000228
grad_step = 000459, loss = 0.000225
grad_step = 000460, loss = 0.000229
grad_step = 000461, loss = 0.000234
grad_step = 000462, loss = 0.000231
grad_step = 000463, loss = 0.000228
grad_step = 000464, loss = 0.000231
grad_step = 000465, loss = 0.000237
grad_step = 000466, loss = 0.000242
grad_step = 000467, loss = 0.000241
grad_step = 000468, loss = 0.000243
grad_step = 000469, loss = 0.000249
grad_step = 000470, loss = 0.000262
grad_step = 000471, loss = 0.000275
grad_step = 000472, loss = 0.000283
grad_step = 000473, loss = 0.000280
grad_step = 000474, loss = 0.000277
grad_step = 000475, loss = 0.000263
grad_step = 000476, loss = 0.000249
grad_step = 000477, loss = 0.000229
grad_step = 000478, loss = 0.000221
grad_step = 000479, loss = 0.000220
grad_step = 000480, loss = 0.000218
grad_step = 000481, loss = 0.000217
grad_step = 000482, loss = 0.000218
grad_step = 000483, loss = 0.000225
grad_step = 000484, loss = 0.000234
grad_step = 000485, loss = 0.000244
grad_step = 000486, loss = 0.000252
grad_step = 000487, loss = 0.000261
grad_step = 000488, loss = 0.000266
grad_step = 000489, loss = 0.000276
grad_step = 000490, loss = 0.000266
grad_step = 000491, loss = 0.000256
grad_step = 000492, loss = 0.000241
grad_step = 000493, loss = 0.000234
grad_step = 000494, loss = 0.000224
grad_step = 000495, loss = 0.000211
grad_step = 000496, loss = 0.000207
grad_step = 000497, loss = 0.000210
grad_step = 000498, loss = 0.000215
grad_step = 000499, loss = 0.000218
grad_step = 000500, loss = 0.000222
plot()
Saved image to .//n_beats_500.png.
grad_step = 000501, loss = 0.000227
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
[[0.84494716 0.85173917 0.91982126 0.94924724 1.0005132 ]
 [0.8404573  0.90502167 0.9515069  1.0156515  0.98893595]
 [0.8917323  0.9109043  0.98744035 0.9931824  0.93325853]
 [0.91277105 0.987634   0.9873979  0.95127547 0.9190929 ]
 [0.9871777  0.9715863  0.9404709  0.9195719  0.86053354]
 [0.98151356 0.94363105 0.91092277 0.85818326 0.8526525 ]
 [0.93249357 0.88872457 0.85304385 0.8538998  0.80836034]
 [0.88361853 0.8320085  0.8520057  0.8233565  0.83789253]
 [0.81865317 0.82009923 0.8051789  0.8381301  0.8479222 ]
 [0.8349455  0.7940136  0.8382052  0.8440269  0.8117819 ]
 [0.78984696 0.822487   0.85217893 0.82912153 0.90803427]
 [0.8361259  0.8214631  0.81824076 0.9088633  0.9499912 ]
 [0.83840424 0.8452203  0.91487074 0.95092475 1.0007465 ]
 [0.8382889  0.9091408  0.9525909  1.0152363  0.9826664 ]
 [0.9015352  0.92487437 0.98757285 0.9875381  0.92241395]
 [0.9242831  0.99371225 0.97987044 0.93518466 0.8986427 ]
 [0.9957231  0.96720445 0.92562264 0.8989239  0.836252  ]
 [0.97689277 0.9269668  0.89444196 0.84017026 0.8389386 ]
 [0.928686   0.878396   0.8296054  0.84147036 0.80824786]
 [0.890289   0.8326509  0.8372346  0.82153463 0.84197664]
 [0.83414125 0.8260836  0.80348665 0.8443426  0.85518396]
 [0.8558707  0.8060713  0.8386737  0.8544816  0.82216567]
 [0.8029646  0.83064914 0.8611541  0.83730495 0.9087086 ]
 [0.8420081  0.8315914  0.824594   0.91038907 0.9497947 ]
 [0.8511131  0.8571421  0.9184343  0.951939   1.0099088 ]
 [0.8501026  0.91308224 0.9541924  1.0234331  1.0031667 ]
 [0.8981055  0.9202313  0.99445885 1.0074085  0.9475461 ]
 [0.92495763 1.0018206  0.9996927  0.9659087  0.9308222 ]
 [0.9988502  0.9852458  0.9514997  0.9322381  0.86673033]
 [0.9943326  0.95349574 0.9223083  0.86564445 0.85741055]
 [0.9391284  0.8957881  0.8591769  0.85928416 0.81637514]]

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
