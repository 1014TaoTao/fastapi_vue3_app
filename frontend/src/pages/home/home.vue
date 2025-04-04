<template>
	<app-layout>
		<template #main>
			<view class="home-container">
				<!-- 搜索框 -->
				<up-search 
					:placeholder="'搜索用户'" 
					v-model="pageQuery.name" 
					:show-action="false"
					@search="handleUserList" 
					@clear="handleClearSearch" 
				/>
				
				<!-- 列表容器 -->
				<up-list :border="false" height="auto">
					<up-list-item v-for="item in tableData" :key="item.id">
						<up-cell :border="false" :label="item.created_at">
							<template #icon>
								<up-avatar shape="square" size="35"
									:src="item.avatar || '/static/default-avatar.png'"
									custom-style="margin-right: 10rpx"></up-avatar>
							</template>
							<template #title>
								<view class="cell-content">
									<text class="name">{{ item.name }}</text>
								</view>
							</template>
							<template #right-icon>
								<view class="tag-group">
									<up-tag :type="item.disabled ? 'error' : 'primary'" size="mini"
										:text="item.disabled ? '禁用' : '启用'" custom-style="margin-left: 8rpx" />
									<up-tag v-if="item.is_superuser" type="info" size="mini" text="管理员" plain
										custom-style="margin-left: 8rpx" />
								</view>
							</template>
						</up-cell>
					</up-list-item>
				</up-list>
				<!-- 加载更多 -->
				<up-loadmore 
					:status="loadStatus" 
					:load-text="{ loadmore: '上拉或点击加载更多' }" 
					@loadmore="loadMore" 
				/>
				<!-- 空数据提示 -->
				<up-empty v-if="pagination.total === 0" mode="data" text="暂无用户数据"></up-empty>
			</view>
		</template>
	</app-layout>
</template>

<script setup>
import { ref, reactive } from "vue";
import { onLoad } from '@dcloudio/uni-app';
import { list_user } from "@/api/apis";

// 响应式数据
const loadStatus = ref('loadmore');
const tableData = ref([]);
const pageQuery = ref({
	name: '',
	offset: 0,
	limit: 8
});
// 分页配置
const pagination = reactive({
	total: 0, // 总数据条数
	hasNext: null, // 是否有下一页
});

// 初始化加载
onLoad(() => {
	handleUserList();
});

// 获取用户列表
const handleUserList = async () => {
	loadStatus.value = 'loading';
	try {
		const result = await list_user(pageQuery.value);
		// 确保 API 返回的数据结构正确
		if (result && result.data.items) {
			if (pageQuery.value.offset === 0) {
				tableData.value = result.data.items;
			} else {
				tableData.value = [...tableData.value, ...result.data.items];
			}
			// 更新分页状态
			pagination.hasNext = result.data.has_next;
			pagination.total = result.data.total;
			loadStatus.value = pagination.hasNext ? 'loadmore' : 'nomore';
		} else {
			throw new Error('API 数据结构异常');
		}
	} catch (error) {
		loadStatus.value = 'error';
		console.error('加载用户列表失败:', error);
	}
};

// 加载更多
const loadMore = () => {
	if (pagination.hasNext && loadStatus.value === 'loadmore') {
		pageQuery.value.offset += pageQuery.value.limit;
		handleUserList();
	}
};

// 清除搜索框时重置查询条件并重新加载数据
const handleClearSearch = () => {
	pageQuery.value.name = '';
	pageQuery.value.offset = 0;
	handleUserList();
};
</script>

<style lang="scss" scoped>
.home-container {
	padding: 30rpx;
	background-color: #f8f8f8;
}
</style>