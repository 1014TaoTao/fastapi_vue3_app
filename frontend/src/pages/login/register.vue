<template>
    <view class="forgot-container">
        
        <uni-forms ref="form" v-model="formData" :rules="rules">
            <uni-forms-item name="name">
                <uni-easyinput 
                    v-model="formData.name" 
                    prefixIcon="person" 
                    placeholder="请输入用户名" 
                />
            </uni-forms-item>

            <uni-forms-item name="username">
                <uni-easyinput 
                    v-model="formData.username" 
                    prefixIcon="person" 
                    placeholder="请输入账号" 
                />
            </uni-forms-item>
            
            <uni-forms-item name="password">
                <uni-easyinput 
                    v-model="formData.password" 
                    type="password" 
                    prefixIcon="locked" 
                    placeholder="请输入密码" 
                />
            </uni-forms-item>
            
            <button 
                type="primary" 
                @click="handleSubmit"
                :loading="loading"
            >确认</button>
        </uni-forms>
        
        <view class="action-link" @click="handleGo">返回登录</view>
    </view>
</template>

<script setup>
import { ref } from 'vue';
import { onReady } from '@dcloudio/uni-app';
import { register } from '../../api/apis';

const form = ref(null);
const loading = ref(false);

const formData = ref({
    name: '',
    username: '',
    password: '',
});

// 表单验证规则
const rules = {
    name: {
        rules: [{
            required: true,
            errorMessage: '用户名不能为空'
        }]
    },
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

onReady(() => {
    console.log('这是注册用户页面')
});

async function handleSubmit() {
    // 先进行完整的前端验证
    form.value.validate().then(async () => {
        // 先进行完整的前端验证
        loading.value = true;
        // 发送登录请求
        const res = await register(formData.value);
        console.log('注册用户成功', res.data);
        // 跳转到登录页面
        uni.navigateTo({ url: '/pages/login/login' });
        
        loading.value = false;
    }).catch(err => {
        console.log('表单验证失败', err);
    });
};

function handleGo() {
    uni.navigateTo({ url: '/pages/login/login' }); 
};
</script>

<style lang="scss" scoped>
.forgot-container {
    padding: 40rpx 60rpx;
    
    .form-title {
        font-size: 40rpx;
        font-weight: bold;
        text-align: center;
        margin: 40rpx 0 60rpx;
        color: #333;
    }
    
    :deep(.uni-forms-item__label) {
        display: none;
    }
    
    :deep(.uni-easyinput__content) {
        background-color: #f8f8f8;
        border-radius: 12rpx;
    }
    
    .button {
        margin-top: 40rpx;
        height: 90rpx;
        line-height: 90rpx;
        font-size: 32rpx;
        border-radius: 12rpx;
    }
    
    .action-link {
        display: block;
        text-align: center;
        margin-top: 30rpx;
        color: #666;
        font-size: 28rpx;
    }
}
</style>

