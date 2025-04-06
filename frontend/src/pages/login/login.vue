<template>
    <view class="login-container">
        <!-- 登录表单 -->
        <up-image class="logo" :src="LOGO_PATH" shape="circle" width="100" height="100" mode="aspectFit" />
        <up-text class="logo-text" :bold="true" align="center" size="24" lineHeight="40" text="用户管理系统" />
        <up-form ref="loginForm" class="auth-form" :model="formData" :rules="rules">
            <!-- 用户名 -->
            <up-form-item prop="username">
                <up-input v-model="formData.username" placeholder="请输入账号" prefix-icon="account" clearable />
            </up-form-item>

            <!-- 密码 -->
            <up-form-item prop="password">
                <up-input v-model="formData.password" type="password" placeholder="请输入密码" prefix-icon="lock" clearable
                    @keyup.enter="handleSubmit" />
            </up-form-item>

            <!-- 登录按钮 -->
            <up-button class="login-btn" type="primary" text="登录" :loading="loading" @click="handleSubmit" />
        </up-form>

        <!-- 底部链接 - 左右分开 -->
        <view class="footer-links">
            <up-text type="primary" @click="navigateTo('register')" text="注册账号" align="left"></up-text>
            <up-text type="primary" @click="navigateTo('forget')" text="忘记密码" align="right"></up-text>
        </view>
    </view>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '../../stores/index'
import { login } from '@/api/apis'

const LOGO_PATH = '/static/logo.png'
const loading = ref(false)
const loginForm = ref(null)

const formData = ref({
    username: '',
    password: ''
})

const rules = {
    username: { required: true, message: '请输入账号',trigger: ['change','blur'] },
    password: { required: true, message: '请输入密码',trigger: ['change','blur'] }
}

const handleSubmit = async () => {
    await loginForm.value.validate()
    loading.value = true

    const result = await login(formData.value)
    console.log('登录成功', result.data)
    useUserStore().setStore(result.data.user_info, result.data.access_token)

    uni.switchTab({ url: '/pages/home/home' })

    loading.value = false

}

const navigateTo = (page) => {
    uni.navigateTo({ url: `/pages/login/${page}` })
}

</script>

<style scoped lang="scss">
.login-container {
    padding: 60rpx;
    display: flex;
    flex-direction: column;
    align-items: center;

    .auth-form {
        margin-top: 40rpx;
        width: 100%;

        .login-btn {
            margin-top: 40rpx;
        }

    }

    .footer-links {
        margin-top: 40rpx;
        display: flex;
        width: 100%;
    }
}
</style>