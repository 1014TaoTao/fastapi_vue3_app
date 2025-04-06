<template>
	<app-layout>
		<template #main>
			<view class="me-container">
				<!-- 个人信息卡片 -->
				<up-card padding="40rpx" margin="0 0 30rpx 0">
					<template #head>
						<view class="user-info">
							<up-avatar :src="formData.avatar || '/static/logo.[ng]'" shape="circle"
								size="80"></up-avatar>
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
						<up-cell title="个人资料" icon="account" isLink @click="handleToDetail(formData.id)"></up-cell>
						<up-cell title="更新资料" icon="setting" isLink @click="handleToUpdate(formData.id)"></up-cell>
						<up-cell title="修改密码" icon="lock" isLink @click="handletoPassword()"></up-cell>
						<up-cell title="联系我们" icon="weixin-fill" isLink @click="showContact = true"></up-cell>
					</up-cell-group>
				</view>

				<!-- 联系我们弹窗 -->
				<up-popup :show="showContact" @close="showContact = false" mode="center" round="10"
					:maskCloseAble="true" :zIndex="100">
					<view class="contact-popup">
						<view class="popup-header">
							<up-text text="联系我们" size="18" bold></up-text>
							<up-icon name="close" size="20" color="#909399" @click="showContact = false"
								hover-class="icon-hover"></up-icon>
						</view>
						<view class="popup-content">
							<view class="qr-item" v-for="(item, index) in [contactConfig.wechat, contactConfig.group]"
								:key="index">
								<up-image :src="item.src" width="200rpx" height="260rpx" @click="previewImage(index)"></up-image>
								<up-text :text="item.title" margin="10rpx 0" type="info" size="14"></up-text>
							</view>
						</view>
						<view class="popup-footer">
							<up-text text="点击图片可放大查看" type="info" size="12"></up-text>
						</view>
					</view>
				</up-popup>

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
import { onLoad, onShow } from '@dcloudio/uni-app';
import { logout } from "@/api/apis";
import { useUserStore } from '../../stores/index';

const userStore = useUserStore();
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
	{ title: '用户数', value: '12' },
	{ title: '运行中', value: '3' },
	{ title: '已禁止', value: '9' },
	{ title: '管理员', value: '1' }
]);


onLoad(() => {
	loading.value = true;

	formData.value = userStore.userInfo;

	loading.value = false;
});

// 添加onShow生命周期钩子
onShow(() => {
    formData.value = userStore.userInfo;
});

// 跳转到个人资料详情页
const handleToDetail = (id) => {
	uni.navigateTo({
		url: `/pages/work/detail?id=${id}`
	});
};


// 跳转到修改个人资料页
const handleToUpdate = (id) => {
	uni.navigateTo({
		url: `/pages/work/update?id=${id}`
	});
};

// 跳转到修改密码页
const handletoPassword = () => {
	uni.navigateTo({
		url: `/pages/login/forget`
	});
};


// 联系方式配置
const contactConfig = {
	wechat: {
		src: '/static/images/wechat.jpg',
		title: '个人微信'
	},
	group: {
		src: '/static/images/wechat_group.jpg',
		title: '技术交流群'
	}
}

// 弹窗控制
const showContact = ref(false)

// 图片预览列表
const imageList = [contactConfig.wechat.src, contactConfig.group.src]

// 图片预览
const previewImage = (index) => {
	uni.previewImage({
		current: index,
		urls: imageList,
		indicator: 'number',
		loop: true,
		success: () => {
			// 使用plus接口设置预览图片的层级最高
			// #ifdef APP-PLUS
			var webview = plus.webview.currentWebview();
			webview.setStyle({
				popGesture: 'none',
				zindex: 999
			});
			// #endif
			console.log('图片预览成功')
		},
		fail: (err) => {
			console.error('图片预览失败:', err)
		}
	})
}

// 退出登录
const handleLogout = async () => {
	loading.value = true;

	await logout({ token: userStore.token });
	useUserStore().clear();
	uni.reLaunch({ url: '/pages/login/login' });

	loading.value = false;
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
	display: flex;
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

.contact-popup {
	width: 600rpx;
	padding: 40rpx;
	background: #fff;
	border-radius: 20rpx;
	position: relative;
	z-index: 100;

	.popup-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 40rpx;

		.icon-hover {
			opacity: 0.8;
		}
	}

	.popup-content {
		display: flex;
		justify-content: space-around;
		padding: 20rpx 0 40rpx;

		.qr-item {
			display: flex;
			flex-direction: column;
			align-items: center;
			padding: 20rpx;

			&:active {
				opacity: 0.8;
			}
		}
	}

	.popup-footer {
		text-align: center;
		padding: 20rpx 0 0;
		border-top: 1px solid #eee;
	}
}

// 添加全局样式确保预览图片始终在最上层
:deep(.uni-preview-image) {
	z-index: 999999 !important;
}
</style>