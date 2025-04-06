<template>
    <view class="detail-container">
        <up-cell-group>
            <up-cell title="头像" :border="true">
                <template #right-icon>
                    <up-avatar :src="formData.avatar" shape="circle" size="40" mode="scaleToFill"
                        bgColor="#c0c4cc" color="#ffffff" fontSize="35px" name="level">
                    </up-avatar>
                </template>
            </up-cell>
            <up-cell title="编号" :value="formData.id" :border="true"></up-cell>
            <up-cell title="用户名" :value="formData.name" :border="true"></up-cell>
            <up-cell title="账号" :value="formData.username" :border="true"></up-cell>
            <up-cell title="状态">
                <template #value>
                    <up-tag :text="formData.disabled ? '禁用' : '启用'" :type="formData.disabled ? 'warning' : 'success'" plain plainFill></up-tag>
                </template>
            </up-cell>
            <up-cell title="类型">
                <template #value>
                    <up-tag :text="formData.is_superuser ? '管理员' : '普通用户'" :type="formData.is_superuser ? 'error' : 'primary'" plain plainFill ></up-tag>
                </template>
            </up-cell>
            <up-cell title="描述" :value="formData.description || '暂无描述'" :border="true"></up-cell>
            <up-cell title="创建时间" :value="formData.created_at" :border="true"></up-cell>
            <up-cell title="更新时间" :value="formData.updated_at" :border="true"></up-cell>
        </up-cell-group>
    </view>
</template>

<script setup>
import { ref } from 'vue'
import { onLoad } from '@dcloudio/uni-app'
import { detail_user } from "../../api/apis";

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


onLoad((options) => {
    // 获取用户详情
    handleDetail(options.id);
})

const handleDetail = async (id) => {
    loading.value = true;
    // 获取用户详情
    const result = await detail_user(id);
    console.log('用户详情', result.data);
    formData.value = result.data;

    loading.value = false;
}

</script>

<style lang="scss" scoped>
.detail-container {
    padding: 60rpx 60rpx;
}
</style>
