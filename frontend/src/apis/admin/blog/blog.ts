import request from "@/utils/request";

type TBlogCategory = {
  page: number;
  pageSize: number;
  categoryId?: number;
  tagId?: number;
};

export const getBlog = async (searchParams: TBlogCategory) => {
  try {
    const res = await request.get("/api/admin/blog/", {
      params: {
        page: searchParams.page,
        pageSize: searchParams.pageSize,
        categoryId: searchParams.categoryId,
        tagId: searchParams.tagId,
      },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const getBlogById = async (id: number) => {
  try {
    const res = await request.get(`/api/admin/blog/${id}`);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const createBlog = async (data: any) => {
  try {
    const res = await request.post("/api/admin/blog/", data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const updateBlogById = async (id: number, data: any) => {
  try {
    const res = await request.put(`/api/admin/blog/${id}`, data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const deleteBlogByIds = async (ids: number[]) => {
  try {
    const res = await request.delete("/api/admin/blog/", {
      data: {
        ids,
      },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
}
