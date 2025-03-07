def upload_s3_pipeline(ti):
    file_name= ti.xcom_pull(task_id='reddit_extraction',keys='return_value')

    s3= cennect_to_s3()
    create_bucket_if_not_exist(s3,AWS_BUCKET_NAME)
    upload_to_s3(s3, file_path, bucket, file_path.split('/')[-1])