<template>
    <view class="login-container">
        
        <!-- 顶部logo和标题 -->
        <view class="header">
            <image class="logo" src="/static/logo.png" mode="aspectFit"></image>
            <text class="system-title">用户信息管理系统</text>
        </view>
        
        <!-- 登录表单 -->
        <uni-forms ref="form" v-model="formData" class="auth-form" :rules="rules">
            <uni-forms-item label="账号" name="username">
                <uni-easyinput 
                    v-model="formData.username" 
                    prefixIcon="person" 
                    placeholder="请输入账号" 
                    placeholder-class="input-placeholder"
                />
            </uni-forms-item>
            <uni-forms-item label="密码" name="password">
                <uni-easyinput 
                    v-model="formData.password" 
                    type="password" 
                    prefixIcon="locked" 
                    placeholder="请输入密码" 
                    placeholder-class="input-placeholder"
                />
            </uni-forms-item>
            
            <button 
                type="primary" 
                @click="handleSubmit"
                :loading="loading"
            >登录</button>
            
        </uni-forms>
        
        <view class="quick-actions">
            <text class="action-link" @click="handleGoResgiter">注册用户</text>
            <text class="action-link" @click="handleGoForget">忘记密码？</text>
        </view>
    </view>
</template>

<script setup>
    import { ref } from 'vue';
    import { onLoad } from '@dcloudio/uni-app';
    import { login } from '../../api/apis';

    const form = ref(null);
    const loading = ref(false);

    const formData = ref({
        username: '',
        password: ''
    });

    // 表单验证规则
    const rules = {
        username: {
            rules: [{
                required: true,
                errorMessage: '账号不能为空'
            }]
        },
        password: {
            rules: [{
                required: true,
                errorMessage: '密码不能为空'
            }]
        }
    };
    
    onLoad(() => {
        console.log('登录页面')
    });
    
    async function handleSubmit() {
        // 先进行完整的前端验证
        form.value.validate().then(async () => {
            loading.value = true;
            // 发送登录请求
            const res = await login(formData.value);
            console.log('登录成功', res);
            // 登录成功处理
            uni.setStorageSync('token', res.data.access_token);
            uni.setStorageSync('user_id', res.data.user_id.toString());
            loading.value = false;
            uni.switchTab({ url: '/pages/home/home' });
        }).catch(err => {
            console.log('表单验证失败', err);
        });
    };
    
    function handleGoResgiter() {
        uni.navigateTo({ url: '/pages/login/register' }); 
    }

    function handleGoForget() {
        uni.navigateTo({ url: '/pages/login/forget' }); 
    }
</script>

<style lang="scss" scoped>
.login-container {
    box-sizing: border-box;
    padding: 60rpx 80rpx;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    
    .header {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 80rpx;
        
        .logo {
            width: 180rpx;
            height: 180rpx;
            margin-bottom: 30rpx;
        }
        
        .system-title {
            font-size: 36rpx;
            font-weight: bold;
            color: #333;
        }
    }
    
    .auth-form {
        flex: 1;
        display: flex;
        flex-direction: column;
        
        :deep(.uni-forms-item__label) {
            display: none;
        }
        
        :deep(.button) {
            width: 100%;
            height: 90rpx;
            line-height: 90rpx;
            font-size: 32rpx;
            border-radius: 12rpx;
            margin-top: 40rpx;
        }
    }
    
    .quick-actions {
        display: flex;
        justify-content: center;
        gap: 40rpx;
        margin: 40rpx 0;
        
        .action-link {
            font-size: 28rpx;
            color: #2979ff;
            padding: 12rpx 0;
            position: relative;
            transition: all 0.3s;
            
            &:hover {
                color: #1750d0;
            }
        }
    }
    
    .input-placeholder {
        color: #bbb;
        font-size: 30rpx;
    }
}
</style>