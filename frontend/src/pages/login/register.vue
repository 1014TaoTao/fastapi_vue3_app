<template>
    <view class="register-container">
        
        <up-form ref="form" :model="formData" :rules="rules" class="auth-form">
            <!-- 用户名 -->
            <up-form-item prop="name">
                <up-input v-model="formData.name" placeholder="请输入用户名" prefix-icon="account" clearable />
            </up-form-item>

            <!-- 账号 -->
            <up-form-item prop="username">
                <up-input v-model="formData.username" placeholder="请输入账号" prefix-icon="account" clearable />
            </up-form-item>

            <!-- 密码 -->
            <up-form-item prop="password">
                <up-input v-model="formData.password" type="password" placeholder="请输入密码" prefix-icon="lock" clearable
                    @keyup.enter="handleSubmit" />
            </up-form-item>

            <!-- 确认按钮 -->
            <up-button class="btn" type="primary" text="确认" :loading="loading" @click="handleSubmit"/>
            
        </up-form>
    </view>
</template>

<script setup>
import { ref } from 'vue';
import { onReady } from '@dcloudio/uni-app';
import { register } from '@/api/apis';

const form = ref(null);
const loading = ref(false);

const formData = ref({
    name: '',
    username: '',
    password: '',
});

// 表单验证规则
const rules = {
    name: { required: true, message: '请输入用户名',trigger: ['change','blur'] },
    username: { required: true, message: '请输入账号',trigger: ['change','blur'] },
    password: { required: true, message: '请输入密码',trigger: ['change','blur'] }
}

onReady(() => {
    console.log('这是注册用户页面')
});


const handleSubmit = async () => {
    await form.value.validate();
    loading.value = true

    const result = await register(formData.value);
    console.log('注册用户成功', result.data);

    // 跳转到登录页面
    uni.navigateBack();

    loading.value = false

};

</script>

<style lang="scss" scoped>
.register-container {
    padding: 60rpx 60rpx;

    .btn {
        margin-top: 40rpx;
    }
}

</style>

