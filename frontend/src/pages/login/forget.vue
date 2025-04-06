<template>
    <view class="forgot-container">
        <up-form ref="form" :model="formData" :rules="rules">
            <!-- 账号 -->
            <up-form-item prop="username">
                <up-input v-model="formData.username" placeholder="请输入账号" prefix-icon="account" clearable />
            </up-form-item>

            <!-- 旧密码 -->
            <up-form-item prop="old_password">
                <up-input v-model="formData.old_password" type="password" placeholder="请输入旧密码" prefix-icon="lock" clearable />
            </up-form-item>

            <!-- 新密码 -->
            <up-form-item prop="new_password">
                <up-input v-model="formData.new_password" type="password" placeholder="请输入新密码" prefix-icon="lock"
                    clearable @keyup.enter="handleSubmit" />
            </up-form-item>

            <up-form-item prop="confirm_password">
                <up-input v-model="formData.confirm_password" type="password" placeholder="请确认新密码" prefix-icon="lock"
                    clearable @keyup.enter="handleSubmit" />
            </up-form-item>


            <!-- 确认按钮 -->
            <up-button class="btn" type="primary" text="确认" :loading="loading" @click="handleSubmit" />

        </up-form>
        <view>

        </view>
    </view>
</template>

<script setup>
import { ref } from 'vue';
import { onReady } from '@dcloudio/uni-app';
import { forgot_password } from '@/api/apis';
import { useUserStore } from '../../stores/index';

const userStore = useUserStore();
const loading = ref(false);
const form = ref(null);

const formData = ref({
    username: '',
    old_password: '',
    new_password: '',
    confirm_password: ''
});

// 表单验证规则
const rules = {
    username: { required: true, message: '请输入账号',trigger: ['change','blur'] },
    old_password: { required: true, message: '请输入旧密码',trigger: ['change','blur'] },
    new_password: { required: true, message: '请输入新密码',trigger: ['change','blur'] },
    confirm_password: { required: true, message: '请确认新密码',trigger: ['change','blur'] }
}

onReady(() => {
    console.log('这是忘记密码页面')
});

const handleSubmit = async () => {
    await form.value.validate();
    loading.value = true

    const result = await forgot_password(formData.value);
    console.log('密码重置成功', result.data);

    userStore.clear()
    // 跳转到登录页面
    uni.navigateTo({ url: '/pages/login/login' });

    loading.value = false

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
