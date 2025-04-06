<template>
    <view class="create-container">
        <up-form ref="form" :model="formData" :rules="rules" labelWidth="80" class="auth-form">
            <!-- 头像 -->
            <up-form-item label="头像:" prop="avatar">
                <up-upload 
                    :fileList="fileList" 
                    @afterRead="afterRead" 
                    @delete="deletePic" 
                    name="头像"
                    :maxCount="1" 
                    :previewFullImage="true">
                </up-upload>
            </up-form-item>

            <!-- 用户名 -->
            <up-form-item label="用户名:" prop="name">
                <up-input v-model="formData.name" placeholder="请输入用户名" clearable />
            </up-form-item>

            <!-- 账号 -->
            <up-form-item label="账号:" prop="username">
                <up-input v-model="formData.username" placeholder="请输入账号" clearable />
            </up-form-item>

            <!-- 密码 -->
            <up-form-item label="密码:" prop="password">
                <up-input v-model="formData.password" type="password" placeholder="请输入旧密码" prefix-icon="lock" clearable />
            </up-form-item>

            <!-- 状态 -->
            <up-form-item label="状态:" prop="disabled">
                <up-switch v-model="formData.disabled" activeColor="#f56c6c"></up-switch>
            </up-form-item>


            <!-- 描述 -->
            <up-form-item label="描述:" prop="description">
                <up-textarea v-model="formData.description" placeholder="请输入描述信息" count/>
            </up-form-item>


            <!-- 确认按钮 -->
            <up-button class="btn" type="primary" text="确认" :loading="loading" @click="handleSubmit" />
        </up-form>
    </view>
</template>

<script setup>
import { ref } from 'vue';
import { onLoad, onReady } from '@dcloudio/uni-app';
import { create_user, upload_file } from '../../api/apis';

const form = ref(null);
const loading = ref(false);

const formData = ref({
    name: "",
    username: "",
    password: "",
    disabled: false,
    avatar: "",
    description: "",
});

// 添加fileList响应式数据
const fileList = ref([]);

// 表单验证规则
const rules = {
    name: { required: true, message: '请输入用户名', trigger: ['change','blur'] },
    username: { required: true, message: '请输入账号', trigger: ['change','blur'] },
    password: { required: true, message: '请输入密码', trigger: ['change','blur'] },
    disabled: { required: true, message: '请选择状态'},
    description: { required: false },
    avatar: { required: false }
}

onLoad(() => {
    // 获取用户详情
    console.log("这是创建用户页面");
});

// 提交表单
const handleSubmit = async () => {

    await form.value.validate();
    loading.value = true

    const result = await create_user(formData.value);
    console.log('创建用户成功', result.data);

    setTimeout(() => {uni.navigateBack();}, 1500);

    loading.value = false
};

// 上传图片
const afterRead = async (event) => {
    loading.value = true;

    const file = event.file;

    // 确保使用临时文件路径
    const result = await upload_file(file.url);
    
    // 更新表单数据中的头像URL
    formData.value.avatar = result.data;
    
    // 更新文件列表
    fileList.value = [{
        url: result.data,
        status: 'success',
        message: result.message,
    }];

    loading.value = false;

};

// 删除图片
const deletePic = (event) => {
    fileList.value.splice(event.index, 1);
};

</script>

<style lang="scss" scoped>
.create-container {
    padding: 30rpx;

    .auth-form {
        background-color: #fff;
        padding: 30rpx;
        border-radius: 12rpx;
    }

    .btn {
        margin-top: 40rpx;
    }
}
</style>
