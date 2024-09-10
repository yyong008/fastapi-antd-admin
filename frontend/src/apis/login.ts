import request from '@/utils/request'

type LoginData = {
  username: string;
  password: string
}

export const login = async (data: LoginData) => {
  try {
    const res = await request.post("/api/login",data)
    return res
  } catch (error) {
    console.error(error)
  }
}
