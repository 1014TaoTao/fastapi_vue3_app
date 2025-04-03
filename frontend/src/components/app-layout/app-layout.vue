<template>
	<view class="layout" savepadding>
		<view class="header">
			<!-- 个人信息 -->
			<view class="info">
				<view class="user-profile">
					<image class="avatar" :src="formData.avatar || '/static/logo.png'"></image>
					<view class="user-info">
						<text class="name">{{ formData.name || '未登录' }}</text>
						<text class="username">@{{ formData.username || '未登录' }}</text>
					</view>
				</view>
				<view class="actions">
					<button type="warn" class="action-btn" @click="handleLogout">退出登录</button>
				</view>
			</view>
		</view>

		<view class="main">
			<slot name="main"></slot>
		</view>
	</view>
</template>

<script setup>
import { ref } from "vue";
import { onLoad } from "@dcloudio/uni-app";
import { detail_user, logout } from "@/api/apis";
import { useUserStore } from '@/stores/index'

// 初始化状态仓库
const userStore = useUserStore()

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

const tokenData = ref({
	token: uni.getStorageSync('token'),
});

const user_id = uni.getStorageSync('user_id');

onLoad(() => {
	console.log('safeAreaInsets', uni.getSystemInfo());
	handleDetail();
});

// 获取当前登录用户信息
async function handleDetail() {
	console.log('用户详情', user_id);
	const res = await detail_user(user_id);
	console.log('用户详情', res);
	formData.value = res.data;
}

// 退出登录
async function handleLogout() {
	const res = await logout(tokenData.value);
	console.log('退出登录', res);
	uni.removeStorageSync('token');
	uni.removeStorageSync('user_id');
	uni.reLaunch({ url: '/pages/login/login' });
}

</script>

<style lang="scss">
.layout {
	display: flex;
	flex-direction: column;
	min-height: calc(100vh - var(--window-bottom));
	padding: 20rpx;
	background-color: #f5f5f5;
	box-sizing: border-box; /* 确保 padding 包含在高度内 */

	.header {
		padding: 20rpx;
		background: #fff;
		border-radius: 16rpx;
		margin-bottom: 20rpx;
		box-shadow: 0 4rpx 12rpx rgba(0, 0, 0, 0.05);
		transition: all 0.3s ease;

		.info {
			background: linear-gradient(135deg, #c63a35 0%, #fab4b0 100%);
			padding: 30rpx;
			border-radius: 30rpx; /* 圆角 */
			box-shadow: 0 4rpx 20rpx rgba(79, 172, 254, 0.3);
			display: flex;
			justify-content: space-between;
			align-items: center;
			backdrop-filter: blur(10px);

			.user-profile {
				display: flex;
				align-items: center;
				gap: 20rpx;

				.avatar {
					width: 100rpx;
					height: 100rpx;
					border-radius: 50%;
					border: 4rpx solid rgba(255, 255, 255, 0.8);
					box-shadow: 0 4rpx 10rpx rgba(0, 0, 0, 0.1);
				}

				.user-info {
					display: flex;
					flex-direction: column;

					.name {
						font-size: 36rpx;
						font-weight: bold;
						color: #ffffff;
					}

					.username {
						font-size: 24rpx;
						color: rgba(255, 255, 255, 0.8);
					}
				}
			}

			.actions {
				display: flex;
				gap: 20rpx;

				.action-btn {
					padding: 0 30rpx;
					height: 60rpx;
					line-height: 60rpx;
					border-radius: 30rpx;
					font-size: 26rpx;
					border: none;

					&[type="warn"] {
						background: rgba(255, 255, 255, 0.2);
						color: #fff;
					}
				}
			}
		}

		&:active {
			transform: scale(0.98);
		}
	}

	.main {
		flex: 1;
		padding: 20rpx;
		background: #fff;
		border-radius: 16rpx;
		box-shadow: 0 4rpx 12rpx rgba(0, 0, 0, 0.05); // 阴影
		transition: all 0.3s ease; // 过渡效果

		&:active {
			transform: scale(0.98);
		}
	}
}
</style>