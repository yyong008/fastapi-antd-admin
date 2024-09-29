import request from "@/utils/request";

type TBlogCategory = {
  page: number;
  pageSize: number;
};

export const getBlogCategory = async (searchParams: TBlogCategory) => {
  try {
    const res = await request.get("/api/admin/blog/category/", {
      params: { page: searchParams.page, pageSize: searchParams.pageSize },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const getBlogById = async (id: number) => {
  try {
    const res = await request.get("/api/admin/blog/" + id);
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const createBlogCategory = async (data: any) => {
  try {
    const res = await request.post("/api/admin/blog/category/", data);
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const updateBlogCategoryById = async (id: number, data: any) => {
  try {
    const res = await request.put("/api/admin/blog/category/" + id, data);
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const deleteBlogCategoryByIds = async (ids: number[]) => {
  try {
    const res = await request.delete("/api/admin/blog/category/", {
      data: {
        ids,
      },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};
