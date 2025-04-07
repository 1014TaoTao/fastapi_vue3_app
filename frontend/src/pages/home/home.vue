<template>
	<app-layout>
		<template #main>
			<view class="home-container">
				<up-search :placeholder="'搜索书名/作者/分类'" @search="handleSearch" clear="handleClearSearch" />

				<view class="scroll-content">
					<!-- 紧凑轮播图 -->
					<view class="swiper-section">
						<up-swiper :list="swiperList">
							<template v-slot:item="{ item }">
								<up-image :src="item.image" width="100%" height="160rpx" mode="aspectFill"
									radius="12" />
							</template>
						</up-swiper>
					</view>

					<!-- 分类导航 -->
					<view class="category-nav">
						<scroll-view scroll-x class="nav-scroll">
							<view v-for="(item, index) in categories" :key="index" class="nav-item"
								:class="{ active: currentCategory === index }" @click="switchCategory(index)">
								{{ item }}
							</view>
						</scroll-view>
					</view>

					<!-- 热门小说推荐 -->
					<view class="novel-section">
						<view class="section-header">
							<text class="title">热门小说</text>
							<text class="more">更多 ></text>
						</view>
						<scroll-view scroll-x class="novel-scroll">
							<view v-for="(item, index) in hotNovels" :key="index" class="novel-card">
								<up-image :src="item.cover" width="200rpx" height="280rpx" radius="12" />
								<text class="novel-title">{{ item.title }}</text>
								<text class="novel-author">{{ item.author }}</text>
							</view>
						</scroll-view>
					</view>

					<!-- 排行榜 -->
					<view class="ranking-section">
						<view class="section-header">
							<text class="title">本周热榜</text>
						</view>
						<view class="ranking-list">
							<view v-for="(item, index) in rankingList" :key="index" class="ranking-item">
								<text class="rank-num" :class="{ 'top3': index < 3 }">{{ index + 1 }}</text>
								<up-image :src="item.cover" width="120rpx" height="160rpx" radius="8" />
								<view class="rank-info">
									<text class="book-title">{{ item.title }}</text>
									<text class="book-author">{{ item.author }}</text>
									<text class="book-hot">{{ item.hot }}人在读</text>
								</view>
							</view>
						</view>
					</view>
				</view>
			</view>
		</template>
	</app-layout>
</template>

<script setup>
import { ref } from 'vue'

const swiperList = ref([
	'/static/banner/banner01.jpg',
	'/static/banner/banner02.jpg',
	'/static/banner/banner03.jpg'
])

const currentCategory = ref(0)
const categories = ref(['推荐', '小说', '文学', '青春', '励志', '生活', '经管', '科技'])

const hotNovels = ref([
	{ cover: 'https://bookcover.yuewen.com/qdbimg/349573/1001535109/150.webp', title: '三体', author: '刘慈欣' },
	{ cover: 'https://bookcover.yuewen.com/qdbimg/349573/1042581400/150.webp', title: '活着', author: '余华' },
	{ cover: 'https://bookcover.yuewen.com/qdbimg/349573/1039864976/150.webp', title: '白夜行', author: '东野圭吾' },
	// ...更多小说
])


const rankingList = ref([
	{ cover: 'https://bookcover.yuewen.com/qdbimg/349573/1015190643/90.webp', title: '云边有个小卖部', author: '张嘉佳', hot: '12.5万' },
	{ cover: 'https://bookcover.yuewen.com/qdbimg/349573/1030657157/90.webp', title: '克拉克公园', author: '史蒂夫', hot: '10.2万' },
	{ cover: 'https://bookcover.yuewen.com/qdbimg/349573/1005053098/90.webp', title: '平原上的摩西', author: '双雪涛', hot: '8.9万' },
])

const switchCategory = (index) => {
	currentCategory.value = index
}

const handleSearch = (value) => {
	console.log('搜索:', value)
}
</script>

<style lang="scss" scoped>
.home-container {
	padding: 60rpx 20rpx;

	.scroll-content {
		padding: 20rpx 24rpx;
	}
}

/* 轮播图优化 */
.swiper-section {
	margin: 20rpx 0;

	:deep(.up-swiper) {
		box-shadow: 0 4rpx 12rpx rgba(0, 0, 0, 0.04);
	}
}

/* 分类导航 */
.category-nav {
	margin: 20rpx 0;

	.nav-scroll {
		white-space: nowrap;

		.nav-item {
			display: inline-block;
			padding: 16rpx 30rpx;
			font-size: 28rpx;
			color: #666;

			&.active {
				color: #2979ff;
				font-weight: 500;
			}
		}
	}
}

/* 热门小说推荐 */
.novel-section {
	margin: 30rpx 0;

	.novel-scroll {
		white-space: nowrap;
		padding: 20rpx 0;

		.novel-card {
			display: inline-block;
			margin-right: 24rpx;
			width: 200rpx;

			.novel-title {
				font-size: 26rpx;
				color: #333;
				margin-top: 12rpx;
			}

			.novel-author {
				font-size: 22rpx;
				color: #999;
			}
		}
	}
}

/* 排行榜 */
.ranking-section {
	margin: 30rpx 0;

	.ranking-item {
		display: flex;
		align-items: center;
		padding: 20rpx 0;
		border-bottom: 1rpx solid #eee;

		.rank-num {
			width: 40rpx;
			font-size: 32rpx;
			font-weight: bold;
			color: #999;

			&.top3 {
				color: #ff6b6b;
			}
		}

		.rank-info {
			margin-left: 20rpx;

			.book-title {
				font-size: 28rpx;
				color: #333;
			}

			.book-author {
				font-size: 24rpx;
				color: #666;
			}

			.book-hot {
				font-size: 22rpx;
				color: #ff6b6b;
			}
		}
	}
}

.section-header {
	display: flex;
	justify-content: space-between;
	align-items: center;
	margin-bottom: 20rpx;

	.title {
		font-size: 32rpx;
		font-weight: 500;
		color: #333;
	}

	.more {
		font-size: 24rpx;
		color: #999;
	}
}
</style>