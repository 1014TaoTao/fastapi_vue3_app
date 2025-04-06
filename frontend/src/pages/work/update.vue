<template>
    <view class="update-container">
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
            <up-form-item label="账号:">
                <up-input v-model="formData.username" placeholder="账号" :readonly="true" disabled />
            </up-form-item>

            <!-- 状态 -->
            <up-form-item label="状态:" prop="disabled">
                <up-switch v-model="formData.disabled" activeColor="#f56c6c"></up-switch>
            </up-form-item>


            <!-- 描述 -->
            <up-form-item label="描述:" prop="description">
                <up-textarea v-model="formData.description" placeholder="请输入描述信息"/>
            </up-form-item>

            <!-- 只读信息展示 -->
            <up-form-item label="类型:">
                <up-tag :text="formData.is_superuser ? '管理员' : '普通用户'"
                    :type="formData.is_superuser ? 'error' : 'primary'"></up-tag>
            </up-form-item>

            <up-form-item label="创建时间:">
                <up-text type="info" :text="formData.created_at"></up-text>
            </up-form-item>

            <up-form-item label="更新时间:">
                <up-text type="info" :text="formData.updated_at"></up-text>
            </up-form-item>

            <!-- 确认按钮 -->
            <up-button class="btn" type="primary" text="确认" :loading="loading" @click="handleSubmit" />
        </up-form>
    </view>
</template>

<script setup>
import { ref } from 'vue';
import { onLoad, onReady } from '@dcloudio/uni-app';
import { detail_user, update_user, upload_file } from '../../api/apis';
import { useUserStore } from '../../stores/index';

const userStore = useUserStore();
const form = ref(null);
const loading = ref(false);

const formData = ref({
    id: null,
    name: "",
    username: "",
    password: "",
    disabled: false,
    is_superuser: false,
    avatar: "",
    description: "",
    created_at: "",
    updated_at: "",
});

// 添加fileList响应式数据
const fileList = ref([]);

// 表单验证规则
const rules = {
    name: { required: true, message: '请输入用户名', trigger: ['change','blur'] },
    disabled: { required: true, message: '请选择状态'},
    description: { required: false },
    avatar: { required: false }
}

onLoad((options) => {
    // 获取用户详情
    handleDetail(options.id);
});

// 回显数据
const handleDetail = async (id) => {
    loading.value = true;

    const result = await detail_user(id);
    
    formData.value = result.data;
    
    // 如果有头像则处理成fileList格式
    if (formData.value.avatar) {
        fileList.value = [{
            url: formData.value.avatar,
            status: 'success',
            message: '加载成功'
        }];
    }

    loading.value = false;

}

// 提交表单
const handleSubmit = async () => {

    await form.value.validate();
    loading.value = true

    const result = await update_user(formData.value.id, formData.value);
    console.log('更新用户成功', result.data);

    userStore.setUser(result.data);
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
.update-container {
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
