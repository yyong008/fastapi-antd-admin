import { Link } from "@tanstack/react-router";

export function NewsItem(props: any) {
  const { data } = props;
  return (
    <div>
      <Link
        className="text-gray-900  hover:text-yellow-500"
        to={`/news/${props.data.id}`}
      >
        <h1 className="flex text-[16px] my-[10px]  before:block before:content-['·'] before:text-yellow-700 before:mr-[4px]">
          {data.title}
        </h1>
      </Link>
    </div>
  );
}