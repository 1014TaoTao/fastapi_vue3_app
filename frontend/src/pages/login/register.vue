<template>
    <view class="forgot-container">
        
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

            <!-- 登录按钮 -->
            <up-button class="btn" type="primary" text="确认" :loading="isLoading" @click="handleSubmit"/>
            
            <up-text type="info" @click="handleGo" align="center" lineHeight="40" text="返回登录" />
        </up-form>
    </view>
</template>

<script setup>
import { ref } from 'vue';
import { onReady } from '@dcloudio/uni-app';
import { register } from '@/api/apis';

const form = ref(null);
const isLoading = ref(false);

const formData = ref({
    name: '',
    username: '',
    password: '',
});

// 表单验证规则
const rules = {
    name: { required: true, message: '请输入用户名' },
    username: { required: true, message: '请输入账号' },
    password: { required: true, message: '请输入密码' }
}

onReady(() => {
    console.log('这是注册用户页面')
});


const handleSubmit = async () => {
    try {
        await form.value.validate();
        isLoading.value = true

        const result = await register(formData.value);
        console.log('注册用户成功', result.data);

        // 跳转到登录页面
        uni.navigateTo({ url: '/pages/login/login' });
    } catch (error) {
        console.error('注册用户失败', error);
    } finally {
        isLoading.value = false
    }
};

function handleGo() {
    uni.navigateTo({ url: '/pages/login/login' }); 
};
</script>

<style lang="scss" scoped>
.forgot-container {
    padding: 60rpx 60rpx;

    .btn {
        margin-top: 40rpx;
    }
}

</style>

