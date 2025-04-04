<template>
	<app-layout>
		<template #main>
			<view class="me-container">
				<!-- 个人信息卡片 -->
				<up-card padding="40rpx" margin="0 0 30rpx 0">
					<template #head>
						<view class="user-info">
							<up-avatar :src="formData.avatar || '/static/logo.[ng]'" shape="circle" size="80"></up-avatar>
							<view class="user-detail">
								<up-text :text="formData.name" bold size="18"></up-text>
								<up-text :text="'@' + formData.username" type="info" margin="10rpx 0"></up-text>
								<up-tag :text="formData.is_superuser ? '管理员' : '普通用户'"
									:type="formData.is_superuser ? 'error' : 'primary'" size="mini"></up-tag>
							</view>
						</view>
					</template>
					<template #body>
						<up-text :text="'注册时间：' + formData.created_at" type="info" margin="20rpx 0 0 0"></up-text>
					</template>
				</up-card>

				<!-- 数据统计 -->
				<up-grid :border="false" col="4" align="center" class="stats-grid">
					<up-grid-item v-for="item in dataItems" :key="item.title" class="stats-item">
						<view class="stats-content">
							<up-icon :name="item.icon" :color="item.color" :size="22"></up-icon>
							<view class="stats-value">
								<up-text :text="item.value" size="22" bold></up-text>
							</view>
							<view class="stats-title">
								<up-text :text="item.title" type="info" size="16"></up-text>
							</view>
						</view>
					</up-grid-item>
				</up-grid>

				<!-- 功能菜单 -->
				<view class="menu-section">
					<up-cell-group>
						<up-cell v-for="item in menuItems" :key="item.title" :title="item.title" :icon="item.icon" isLink
							@click="handleMenuClick(item)"></up-cell>
					</up-cell-group>
				</view>

				<!-- 退出登录按钮 -->
				<view class="logout-btn">
					<up-button type="error" text="退出登录" :loading="loading" @click="handleLogout"></up-button>
				</view>
			</view>
		</template>
	</app-layout>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { onReady, onLoad } from '@dcloudio/uni-app';
import { detail_user, logout } from "@/api/apis";
import { useUserStore } from '@/stores/index';

const loading = ref(false);
const formData = ref({
	id: null,
	name: "",
	username: "",
	password: "",
	disabled: null,
	is_superuser: null,
	avatar: "",
	description: "",
	created_at: "",
	updated_at: "",
});

// 数据统计
const dataItems = ref([
	{ title: '系统消息', value: '3', icon: 'bell', color: '#2979ff' },
	{ title: '我的任务', value: '12', icon: 'calendar', color: '#19be6b' },
	{ title: '待处理', value: '5', icon: 'clock', color: '#ff9900' },
	{ title: '已完成', value: '128', icon: 'checkmark', color: '#909399' }
]);

// 功能菜单
const menuItems = ref([
	{ title: '个人资料', icon: 'account' },
	{ title: '账号安全', icon: 'lock' },
	{ title: '消息设置', icon: 'bell' },
	{ title: '帮助中心', icon: 'info' }
]);

onReady(() => {
	getUserInfo();
});

// 获取用户信息
const getUserInfo = async () => {
	loading.value = true;

	const res = await detail_user(uni.getStorageSync('user_id'));
	formData.value = res.data;
	console.log('formData赋值后:', formData.value);

	loading.value = false;
};

// 退出登录
const handleLogout = async () => {
	loading.value = true;

	await logout({ token: uni.getStorageSync('token') });
	useUserStore().clearUser();
	uni.reLaunch({ url: '/pages/login/login' });

	loading.value = false;

};

// 菜单点击
const handleMenuClick = (item) => {
	uni.showToast({ title: `点击了${item.title}`, icon: 'none' });
};


</script>

<style lang="scss" scoped>
.me-container {
	padding: 30rpx;
}

.user-info {
	display: flex;
	gap: 30rpx;
	align-items: flex-start;
}

.user-detail {
	display: flex;
	flex-direction: column;
	justify-content: center;
}

.stats-grid {
	background-color: #fff;
	border-radius: 12rpx;
	margin: 0 0 30rpx 0;
	padding: 30rpx 0;
}

.stats-item {
	position: relative;
	
	&::after {
		content: '';
		position: absolute;
		right: 0;
		top: 20%;
		height: 60%;
		width: 1px;
		background-color: #eee;
	}
	
	&:last-child::after {
		display: none;
	}
}

.stats-content {
	display: flex;
	flex-direction: column;
	align-items: center;
	gap: 12rpx;
}

.stats-value {
	margin: 8rpx 0;
}

.stats-title {
	text-align: center;
}

.menu-section {
	margin-bottom: 40rpx;
}

.logout-btn {
	padding: 20rpx 0;
}
</style>