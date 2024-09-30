// getProfileLinkListByCategoryId
import request from "@/utils/request";

type TProfileLinkCategory = {
  page: number;
  pageSize: number;
};

export const getProfileLinkListByCategoryId = async (
  categoryId: number,
  searchParams: TProfileLinkCategory
) => {
  try {
    const res = await request.get("/api/admin/profile/link/" + categoryId, {
      params: { page: searchParams.page, pageSize: searchParams.pageSize },
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const getProfileLinkById = async (id: number) => {
  try {
    const res = await request.get("/api/admin/profile/link/" + id);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const createProfileLink = async (data: any) => {
  try {
    const res = await request.post("/api/admin/profile/link/", data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const udpateProfileLinkById = async (id: number, data: any) => {
  try {
    const res = await request.put("/api/admin/profile/link/" + id, data);
    return res;
  } catch (error) {
    console.error(error);
  }
}

export const deleteProfileLinkByIds = async (ids: number[]) => {
  try {
    const res = await request.delete("/api/admin/profile/link/", {
      data: {
        ids
      }
    });
    return res;
  } catch (error) {
    console.error(error);
  }
}
