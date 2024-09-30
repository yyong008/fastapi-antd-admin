import request from "@/utils/request";

type TProfileLinkCategory = {
  page: number;
  pageSize: number;
};

export const getProfileLinkCategory = async (
  searchParams: TProfileLinkCategory
) => {
  try {
    const res = await request.get("/api/admin/profile/link/category/", {
      params: { page: searchParams.page, pageSize: searchParams.pageSize },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const getProfileLinkCategoryById = async (id: number) => {
  try {
    const res = await request.get(`/api/admin/profile/link/category/${id}`);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const createProfileLinkCategory = async (data: any) => {
  try {
    const res = await request.post("/api/admin/profile/link/category/", data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const udpateProfileLinkCategoryById = async (id: number, data: any) => {
  try {
    const res = await request.put("/api/admin/profile/link/category/" +id, data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const deleteProfileLinkCategoryByIds = async (ids: number[]) => {
  try {
    const res = await request.delete(`/api/admin/profile/link/category/`, {
      data: { ids }
    });
    return res;
  } catch (error) {
    console.error(error);
  }
}

